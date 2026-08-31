# -*- coding: utf-8 -*-
"""tests_controle_rapports_tests.py — refuser la promesse fausse, pas la dette.

Ce banc joue sur des arborescences fabriquées la distinction qui fait tout le
sel de ce contrôle : un rapport **sans** script est une dette et passe ; un
rapport qui **nomme** un script absent est une promesse fausse et est refusé —
sauf s'il avoue lui-même que le script manque.

Sans cette dernière échappatoire, le contrôle signalerait précisément les
rapports qui ont dit la vérité sur leur propre erreur passée (règle d'or n°248).

Usage : python3 _outils/tests_controle_rapports_tests.py
Sortie : 0 si tout passe, 1 sinon.
"""

import contextlib
import io
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_rapports_tests as CR  # noqa: E402


def lot(racine, rapport, scripts=(), pages=("sequence_essai.html",)):
    """Un dossier de lot : un rapport, d'éventuels scripts, et les pages qu'une
    suite pourrait conduire. `pages=()` fabrique un dossier d'AUDIT — un rapport
    qui relate une mesure, sans page à piloter."""
    r = pathlib.Path(racine)
    r.mkdir(parents=True, exist_ok=True)
    (r / "rapport_tests_essai.md").write_text(rapport, encoding="utf-8")
    for s in scripts:
        (r / s).write_text("// vide\n", encoding="utf-8")
    for f in pages:
        (r / f).write_text("<html></html>\n", encoding="utf-8")
    return r


def jouer(racine):
    ancien = CR.DEPOT
    CR.DEPOT = str(racine)
    sortie = io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie):
            code = CR.main()
    finally:
        CR.DEPOT = ancien
    return code, sortie.getvalue()


def main():
    echecs, controles = [], 0

    def cas(titre, racine, doit_refuser, attendu=""):
        nonlocal controles
        controles += 1
        code, texte = jouer(racine)
        if doit_refuser and code == 0:
            echecs.append("%s : accepté, alors qu'il fallait refuser" % titre)
        elif not doit_refuser and code != 0:
            echecs.append("%s : refusé\n     %s" % (titre, texte.strip().replace("\n", "\n     ")))
        elif attendu and attendu not in texte:
            echecs.append("%s : refus correct, message sans « %s »" % (titre, attendu))

    with tempfile.TemporaryDirectory() as tmp:
        b = pathlib.Path(tmp)

        # ── 1. un rapport qui cite un script LIVRÉ passe ────────────────────
        cas("un rapport dont le script est dans le dossier",
            lot(b / "c1", "# R\n\nSuite : `tests_essai.mjs` — 3 tests.\n\n| a | ✅ |\n",
                ["tests_essai.mjs"]), False)

        # ── 2. un rapport qui cite un script ABSENT est refusé ──────────────
        cas("un rapport qui nomme un script introuvable",
            lot(b / "c2", "# R\n\nSuite : `tests_lot42.js` — 23 tests, tous exécutés.\n\n| a | ✅ |\n"),
            True, "tests_lot42.js")

        # ── 3. le même, mais qui AVOUE dans la phrase ───────────────────────
        cas("un rapport qui avoue dans la même phrase",
            lot(b / "c3", "# R\n\nSuite : `tests_lot42.js`, qui n'a jamais été commité.\n\n| a | ✅ |\n"),
            False)

        # ── 4. le même, l'aveu dans la phrase SUIVANTE ──────────────────────
        # C'est la forme réelle des six rapports corrigés le 31/08/2026.
        cas("un rapport qui avoue juste après",
            lot(b / "c4",
                "# R\n\nSuite : `tests_lot42.js` — 23 tests, tous exécutés le 24/07/2026.\n\n"
                "> **Ce script n'est pas dans le dépôt et n'y a jamais été commité** — les "
                "coches disent ce qui a été observé.\n\n| a | ✅ |\n"),
            False)

        # ── 5. l'aveu trop loin ne compte pas ───────────────────────────────
        cas("un aveu noyé six cents caractères plus loin ne vaut pas aveu",
            lot(b / "c5",
                "# R\n\nSuite : `tests_lot42.js` — 23 tests.\n\n" + ("Blabla. " * 90)
                + "\n\nCe script n'a jamais été commité.\n\n| a | ✅ |\n"),
            True, "tests_lot42.js")

        # ── 6. une DETTE passe, et elle est comptée ─────────────────────────
        controles += 1
        code, texte = jouer(lot(b / "c6", "# R\n\n| a | ✅ |\n| b | ✅ |\n"))
        if code != 0:
            echecs.append("un rapport sans script du tout est refusé, alors que c'est une dette")
        elif "sans aucun script" not in texte or "2 ✅" not in texte:
            echecs.append("la dette n'est pas comptée ni nommée dans le relevé\n     "
                          + texte.strip().replace("\n", "\n     "))

        # ── 5 bis. une suite PYTHON compte autant qu'une suite JavaScript ───
        # Le 31/08/2026, ce contrôle ne connaissait que .mjs/.js : il a déclaré
        # en dette treize dossiers portant une suite Python — 103 coches — dont
        # les deux qu'il mettait en tête de file, verts l'un et l'autre.
        controles += 1
        _c, texte = jouer(lot(b / "c5bis",
                              "# R\n\nSuite : `tests_essai.py` — 3 tests.\n\n| a | ✅ |\n",
                              ["tests_essai.py"]))
        if "LOT(S) portent des coches" in texte:
            echecs.append("un dossier portant une suite Python est compté en dette")

        controles += 1
        code, _t = jouer(lot(b / "c5ter",
                             "# R\n\nSuite : `tests_fantome.py`, 3 tests.\n\n| a | ✅ |\n"))
        if code == 0:
            echecs.append("une citation de script PYTHON absent n'est pas refusée")

        # ── 6 bis. un rapport d'AUDIT n'entre pas dans la file d'attente ────
        # Sans cette distinction, les trois dossiers de gouvernance du dépôt
        # occupaient la tête de file — 115 coches qu'aucune suite ne peut payer.
        controles += 1
        _c, texte = jouer(lot(b / "c6bis", "# Audit\n\n| a | ✅ |\n| b | ✅ |\n", pages=()))
        if "LOT(S) portent des coches" in texte:
            echecs.append("un rapport d'audit est compté comme un lot en attente de suite")
        if "rapport(s) d'AUDIT écartés" not in texte:
            echecs.append("les rapports d'audit écartés ne sont pas nommés dans le relevé")

        # ── 7. un rapport sans coche ni script n'encombre pas le relevé ─────
        controles += 1
        _c, texte = jouer(lot(b / "c7", "# R\n\nRien à signaler.\n"))
        if "sans aucun script" in texte:
            echecs.append("un rapport sans coche est compté comme une dette")

        # ── 8. une citation coupée par un retour à la ligne est vue (n°262) ──
        cas("une citation qui va à la ligne",
            lot(b / "c8", "# R\n\nSuite :\n`tests_lot42.js` — 23 tests, tous exécutés.\n\n| a | ✅ |\n"),
            True, "tests_lot42.js")

    # ── 9. le dépôt réel doit passer ────────────────────────────────────────
    controles += 1
    code, texte = jouer(CR.DEPOT)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     "
                      + texte.strip().replace("\n", "\n     "))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — la promesse fausse est refusée, la dette est comptée sans être "
          "refusée" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
