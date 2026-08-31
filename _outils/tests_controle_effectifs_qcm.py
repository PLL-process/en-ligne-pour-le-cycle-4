# -*- coding: utf-8 -*-
"""tests_controle_effectifs_qcm.py — le contrôle doit refuser, et ne pas crier au loup.

Ce banc joue sur des arborescences **fabriquées** les refus attendus et les
silences attendus — dont celui qui a failli coûter cher : un manifeste
posé dans le même dossier qu'une banque ne parle pas forcément d'elle. Sur le
dépôt réel, la première version du contrôle produisait neuf faux écarts sur
`4e_C4.7/`, qui porte quatre banques et un manifeste ne décrivant que l'une
d'elles (règles n°248 et n°263).

Le dernier cas exige que le dépôt réel passe.

Usage : python3 _outils/tests_controle_effectifs_qcm.py
Sortie : 0 si tout passe, 1 sinon.
"""

import contextlib
import io
import json
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_effectifs_qcm as CE  # noqa: E402


def page(total, par_code, dits=None, illustrees=0):
    """Une page de QCM minimale : une banque, et les nombres qu'elle affiche.

    `illustrees` donne le nombre de questions portant un bloc `img:{…}` — le
    nombre que `questions_illustrees` prétend décrire."""
    dits = dits or {}
    d = lambda cle: dits.get(cle, total)  # noqa: E731
    banque = []
    reste = illustrees
    for code, n in par_code.items():
        for i in range(n):
            img = ''
            if reste > 0:
                img = 'img:{src:"Images/s%d.svg",alt:"a"},' % reste
                reste -= 1
            banque.append('{c:"%s",n:"n%s%d",%sq:"?",o:["a","b","c","d"],r:0,'
                          'expl:"e",ex:"x",err:"r",d:["","b","c","d"],ret:"t"}'
                          % (code, code, i, img))
    return (
        '<html><body>\n'
        '<span class="badge theme">%d questions · lot</span>\n'
        '<b id="dRest" class="v-warn">%d</b>\n'
        '<button class="btn mode-actif" data-mode="complet">Parcours complet (%d)</button>\n'
        '<b id="qTot">%d</b>\n<b id="rTot">%d</b>\n'
        '<script>\n/* Banque de questions LOT X — %d questions (4 par code) */\n'
        'const QUESTIONS = [\n%s\n];\n</script></body></html>\n'
        % (d("badge"), d("dRest"), d("mode"), d("qTot"), d("rTot"), d("comm"),
           ",\n".join(banque)))


def lot(racine, total=8, par_code=None, dits=None, manifeste=None, nom_qcm="qcm_essai.html",
        lexique=None, illustrees=0):
    r = pathlib.Path(racine)
    r.mkdir(parents=True, exist_ok=True)
    par_code = par_code or {"C4.1": 4, "C4.2": 4}
    (r / nom_qcm).write_text(page(total, par_code, dits, illustrees), encoding="utf-8")
    if manifeste is not None:
        (r / "manifest_essai.json").write_text(json.dumps(manifeste, ensure_ascii=False),
                                               encoding="utf-8")
    if lexique is not None:
        annonce, entrees = lexique
        corps = "".join("<dt>mot%d</dt>" % i for i in range(entrees))
        (r / "lexique_essai.html").write_text(
            '<p class="sub">%d notions, tirées des QCM</p><dl>%s</dl>' % (annonce, corps),
            encoding="utf-8")
    return r


def jouer(racine):
    """Lance le contrôle sur cette racine et renvoie (code de sortie, texte)."""
    ancien = CE.DEPOT
    CE.DEPOT = str(racine)
    sortie = io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie):
            code = CE.main()
    finally:
        CE.DEPOT = ancien
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
            echecs.append("%s : refus correct mais le message ne dit pas « %s »\n     %s"
                          % (titre, attendu, texte.strip().replace("\n", "\n     ")))

    MANIFESTE = {"fichiers": {"qcm": "qcm_essai.html"},
                 "contenu": {"questions_qcm": 8,
                             "questions_par_code": {"5e_C4.1": 4, "5e_C4.2": 4}}}

    with tempfile.TemporaryDirectory() as tmp:
        b = pathlib.Path(tmp)

        # ── 1. une page qui dit vrai passe ──────────────────────────────────
        cas("une banque qui dit vrai sur sa taille",
            lot(b / "c1", manifeste=MANIFESTE, lexique=(3, 3)), False)

        # ── 2 à 6. chacun des cinq nombres de la page, pris séparément ──────
        for cle, quoi in (("badge", "badge de l'en-tête"),
                          ("dRest", "compteur « Restantes »"),
                          ("mode", "bouton « Parcours complet »"),
                          ("qTot", "total pendant le parcours"),
                          ("rTot", "total du bilan")):
            cas("le %s ment" % quoi,
                lot(b / ("c_" + cle), dits={cle: 99}, manifeste=MANIFESTE), True, quoi)

        # ── 7. le commentaire de tête de banque ─────────────────────────────
        cas("le commentaire de tête ment",
            lot(b / "c7", dits={"comm": 99}, manifeste=MANIFESTE), True,
            "commentaire de tête de banque")

        # ── 8. le manifeste ment sur le total ───────────────────────────────
        m8 = json.loads(json.dumps(MANIFESTE)); m8["contenu"]["questions_qcm"] = 99
        cas("le manifeste ment sur le total", lot(b / "c8", manifeste=m8), True, "questions_qcm")

        # ── 9. le manifeste ment sur un code ────────────────────────────────
        m9 = json.loads(json.dumps(MANIFESTE))
        m9["contenu"]["questions_par_code"]["5e_C4.2"] = 9
        cas("le manifeste ment sur un code", lot(b / "c9", manifeste=m9), True,
            "questions_par_code[5e_C4.2]")

        # ── 9 bis. le manifeste ment sur le nombre de questions ILLUSTRÉES ──
        # Ce champ n'était pas confronté avant le 31/08/2026 : deux manifestes
        # du dépôt étaient en écart, `5e_C6.1` et `5e_C2.1` (règle n°264).
        m9b = json.loads(json.dumps(MANIFESTE)); m9b["contenu"]["questions_illustrees"] = 9
        cas("le manifeste ment sur le nombre de questions illustrées",
            lot(b / "c9b", manifeste=m9b, illustrees=3), True, "questions_illustrees = 9")

        # ── 9 ter. le même, juste ────────────────────────────────────────────
        m9t = json.loads(json.dumps(MANIFESTE)); m9t["contenu"]["questions_illustrees"] = 3
        cas("le manifeste dit vrai sur le nombre de questions illustrées",
            lot(b / "c9t", manifeste=m9t, illustrees=3), False)

        # ── 9 quater. une banque SANS aucune image et un manifeste à zéro ────
        m9q = json.loads(json.dumps(MANIFESTE)); m9q["contenu"]["questions_illustrees"] = 0
        cas("une banque sans image, annoncée à zéro, passe",
            lot(b / "c9q", manifeste=m9q, illustrees=0), False)

        # ── 10. le lexique ment sur son nombre de notions ───────────────────
        cas("le lexique annonce plus de notions qu'il n'en porte",
            lot(b / "c10", manifeste=MANIFESTE, lexique=(30, 3)), True, "annonce 30 notions")

        # ── 11. LE CAS QUI A FAIT CRIER AU LOUP ─────────────────────────────
        # Un manifeste qui décrit une AUTRE banque du même dossier ne doit pas
        # être confronté à celle-ci. C'est `4e_C4.7/` : quatre banques, un
        # manifeste, neuf faux écarts dans la première version.
        r11 = lot(b / "c11", manifeste=MANIFESTE)
        autre = {"fichiers": {"qcm": "qcm_dun_autre_lot.html"},
                 "contenu": {"questions_qcm": 30,
                             "questions_par_code": {"4e_C4.9": 10}}}
        (r11 / "manifest_autre.json").write_text(json.dumps(autre, ensure_ascii=False),
                                                 encoding="utf-8")
        cas("un manifeste voisin qui décrit une AUTRE banque n'est pas confronté à celle-ci",
            r11, False)

        # ── 12. une page « qcm… » sans banque est écartée, pas refusée ──────
        r12 = lot(b / "c12", manifeste=MANIFESTE)
        (r12 / "qcm_sans_banque.html").write_text("<html><body>page vide</body></html>",
                                                  encoding="utf-8")
        cas("une page « qcm… » sans bloc QUESTIONS est écartée", r12, False)

        # ── 12 bis. un manifeste qui n'annonce PAS ses illustrations n'est
        # pas jugé là-dessus : ce contrôle confronte ce qui est déclaré, il
        # n'exige pas qu'on déclare (règle n°248).
        m12b = json.loads(json.dumps(MANIFESTE))
        m12b["contenu"].pop("questions_illustrees", None)
        cas("un manifeste muet sur ses illustrations n'est pas jugé là-dessus",
            lot(b / "c12b", manifeste=m12b, illustrees=3), False)

        # ── 13. un lexique sans nombre annoncé n'est pas jugé ───────────────
        r13 = lot(b / "c13", manifeste=MANIFESTE)
        (r13 / "lexique_muet.html").write_text("<dl><dt>a</dt><dt>b</dt></dl>",
                                               encoding="utf-8")
        cas("un lexique qui n'annonce aucun nombre n'est pas jugé", r13, False)

    # ── 14. le dépôt réel doit passer ───────────────────────────────────────
    controles += 1
    code, texte = jouer(CE.DEPOT)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     "
                      + texte.strip().replace("\n", "\n     "))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — le contrôle refuse chaque nombre faux, et se tait sur les "
          "voisins qui ne le concernent pas" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
