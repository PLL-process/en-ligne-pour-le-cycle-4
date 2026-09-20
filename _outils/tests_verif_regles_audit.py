# -*- coding: utf-8 -*-
"""tests_verif_regles_audit.py — le banc du vérificateur de règles d'audit.

POURQUOI CE BANC EXISTE SEULEMENT AUJOURD'HUI
---------------------------------------------
`verif_regles_audit.py` est l'outil le plus lu du dépôt : c'est lui qui écrit
« 60 séquence(s) analysée(s) · 136 manquement(s) » à la fin de chaque lot. Il
n'avait aucun banc. Or il rendait **0 dans tous les cas** — y compris sur une
cible mal écrite en argument, qui donnait « 0 séquence(s) analysée(s) » suivi
d'une sortie 0. Quelqu'un qui se trompe d'un caractère en passant un chemin
obtient donc un contrôle vert sur rien.

Le balayage du 19/09/2026 a mesuré la même chose sur les seize autres contrôles
du dépôt : recopiés dans une racine vide, **tous** sortaient à 0.

CE QUE CE BANC VÉRIFIE
----------------------
Deux choses, et la seconde est le second corollaire de la règle d'or n°299 :
que le contrôle voie ce qu'il doit voir, et qu'il le voie **par son point
d'entrée**, lancé en sous-processus comme on le lance vraiment.

Il ne juge PAS la justesse de chacune des treize règles mécaniques : elles ont
leur propre histoire dans le journal, et les éprouver une à une demanderait un
lot d'essai complet. Ce banc tient la porte d'entrée et la panne — c'est son
périmètre, et il le déclare (règle d'or n°47).

Usage : python3 _outils/tests_verif_regles_audit.py
"""
import contextlib
import io
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verif_regles_audit as V  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "verif_regles_audit.py")

SEQUENCE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Essai</title></head>
<body><h1>Une séquence d'essai</h1><p>Rien de particulier.</p></body></html>
"""


def jouer(argv):
    """`main()` appelé en direct — stdout ET stderr, car la panne part sur stderr."""
    sortie, erreur = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
        code = V.main(argv)
    return code, sortie.getvalue() + erreur.getvalue()


def par_la_ligne_de_commande(args=()):
    """Le contrôle lancé comme on le lance vraiment (règle d'or n°299).

    Un banc qui se contente d'appeler `main()` ne passe jamais par le point
    d'entrée : c'est ainsi que `controle_impression.mjs` est resté muet
    dix-sept jours sous un banc vert.
    """
    r = subprocess.run([sys.executable, SCRIPT] + list(args),
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=900)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    echecs, n = [], 0

    def cas(titre, fait):
        nonlocal n
        n += 1
        try:
            ennui = fait()
        except Exception as e:                      # noqa: BLE001
            ennui = "le banc lui-même a levé — %s" % e
        if ennui:
            echecs.append("%s : %s" % (titre, ennui))

    # ── 1. La panne : règle d'or n°299 ─────────────────────────────────────
    def cible_introuvable():
        code, texte = jouer(["verif_regles_audit.py", "theme-42-qui-nexiste-pas"])
        if code != 2:
            return ("sortie %d au lieu de 2 — une cible mal écrite donnait « 0 séquence(s) "
                    "analysée(s) » et un contrôle vert" % code)
        return None if "EN PANNE" in texte else "la panne n'est pas annoncée sur stderr"

    cas("une cible qui n'existe pas est une panne, pas « 0 manquement »", cible_introuvable)

    def racine_sans_sequence():
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            (bac / "lot" / "qcm_x.html").write_text(SEQUENCE, encoding="utf-8")
            V.RACINE = bac
            code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        if code != 2:
            return "sortie %d au lieu de 2 — aucune séquence, et le contrôle se dit content" % code
        return None if "EN PANNE" in texte else "la panne n'est pas annoncée"

    cas("une racine sans séquence est une panne (un QCM n'est pas une séquence)",
        racine_sans_sequence)

    # ── 2. Ce qu'il doit voir : les trois motifs de nom ─────────────────────
    def les_trois_motifs():
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "lot").mkdir()
            # Les trois formes que l'outil déclare regarder. Le trait d'union a
            # été ajouté après coup : six séquences étaient invisibles.
            for nom in ("sequence_a.html", "sequence-b.html", "sequence.html"):
                (bac / "lot" / nom).write_text(SEQUENCE, encoding="utf-8")
            V.RACINE = bac
            code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        if code != 0:
            return "sortie %d au lieu de 0" % code
        if "3 séquence(s) analysée(s)" not in texte:
            return ("les trois formes de nom ne sont pas toutes vues :\n     %s"
                    % texte.strip()[-300:])
        return None

    cas("sequence_x.html, sequence-x.html et sequence.html sont vues toutes les trois",
        les_trois_motifs)

    def archive_ecartee():
        bac = pathlib.Path(tempfile.mkdtemp())
        ancien = V.RACINE
        try:
            (bac / "_archive-anciennes-versions").mkdir()
            (bac / "_archive-anciennes-versions" / "sequence_v1.html").write_text(
                SEQUENCE, encoding="utf-8")
            (bac / "lot").mkdir()
            (bac / "lot" / "sequence_a.html").write_text(SEQUENCE, encoding="utf-8")
            V.RACINE = bac
            code, texte = jouer(["verif_regles_audit.py"])
        finally:
            V.RACINE = ancien
            shutil.rmtree(bac, ignore_errors=True)
        if code != 0:
            return "sortie %d au lieu de 0" % code
        if "1 séquence(s) analysée(s)" not in texte:
            return ("l'archive n'est pas écartée, ou la séquence hors archive n'est pas "
                    "lue :\n     %s" % texte.strip()[-300:])
        return None

    # Deux séquences, pas une : sans celle hors archive, la racine ne ferait
    # RIEN analyser et le cas passerait au vert en ne prouvant rien.
    cas("l'archive est une trace, pas une ressource — et le reste est bien analysé",
        archive_ecartee)

    # ── 3. Le VRAI point d'entrée, en sous-processus ───────────────────────
    def ligne_de_commande():
        code, texte = par_la_ligne_de_commande()
        if code != 0:
            return "sortie %d :\n     %s" % (code, texte.strip()[:400])
        if "séquence(s) analysée(s)" not in texte:
            return ("le script n'écrit pas son compte — un script muet ne prouve rien :\n"
                    "     %s" % (texte.strip()[:400] or "(rien du tout)"))
        return None

    cas("lancé en ligne de commande, le contrôle analyse le dépôt et le chiffre",
        ligne_de_commande)

    def sortie_json():
        code, texte = par_la_ligne_de_commande(["--json"])
        if code != 0:
            return "sortie %d" % code
        return None if texte.lstrip().startswith("[") else "la sortie --json n'est pas un tableau JSON"

    cas("--json rend un tableau, par la ligne de commande aussi", sortie_json)

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n))
        return 1
    print("✅ %d contrôles — le vérificateur voit les trois formes de nom, écarte l'archive, "
          "et refuse de sortir vert sans avoir analysé une séquence" % n)
    print("\n%d / %d" % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
