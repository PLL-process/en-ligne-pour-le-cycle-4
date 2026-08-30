# -*- coding: utf-8 -*-
"""tests_pointeurs_codes.py — les trois promesses qu'un pointeur ne doit plus faire.

Un README de pointeur affirme trois choses vérifiables :

  1. « **Ce dossier ne porte aucune ressource propre.** »
  2. « **Ce code y est évalué.** »
  3. « **c'est à vous de dire où vous l'évaluez.** »

Les trois étaient écrites de confiance. La première a failli coûter cher : le
jour où `5e_C8.1` et `3e_C8.1` ont reçu leur propre lot, relancer l'outil aurait
remplacé deux lots complets par un renvoi. La deuxième était fausse pour trois
pointeurs sur dix. La troisième renvoyait l'enseignant à lui-même **sans avoir
regardé ailleurs** : le jour où `3e_C7.2` a reçu dix questions dans la banque du
boîtier, le README a continué de dire que personne ne l'évaluait.

Ce banc vérifie qu'aucune des trois ne peut plus être écrite sans avoir été
mesurée — sur le dépôt réel quand c'est possible, sur un index fabriqué quand la
réponse ne doit pas dépendre de l'état du dépôt.

Usage : python3 _outils/tests_pointeurs_codes.py
Sortie : 0 si tout passe, 1 sinon.
"""

import os
import pathlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pointeurs_codes as PC  # noqa: E402
from controle_couverture import SEUIL_EVALUABLE, banques_du_depot  # noqa: E402

DEPOT = PC.DEPOT
C8 = "theme-3-creation-conception-realisation-innovations/C8-valider-les-solutions-techniques-par-des"
C7 = "theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des"

#: dossiers qui portent leur propre lot — un pointeur les écraserait
AVEC_LOT = [
    C8 + "/5e/5e_C8.1",
    C8 + "/3e/3e_C8.1",
    C8 + "/3e/3e_C8.2",
]

#: dossiers qui n'ont vraiment aucune ressource propre
#: (`5e_C7.2` y figurait jusqu'au 30/08/2026 ; il porte désormais son lot « Le
#: dé, en mieux », et un dossier de contrôle qui grandit cesse d'être un
#: contrôle)
SANS_LOT = [
    C7 + "/4e/4e_C7.2",
    "theme-3-creation-conception-realisation-innovations"
    "/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.2",
]


def readme_est_engendre(dossier):
    """Le README de ce dossier est-il celui qu'écrit `pointeurs_codes.py` ?"""
    readme = dossier / "README.md"
    return readme.exists() and PC.SIGNATURE in readme.read_text(encoding="utf-8")


def main():
    echecs = []
    controles = 0

    # ── 1. « ce dossier ne porte aucune ressource propre » ──────────────────
    for rel in AVEC_LOT:
        controles += 1
        d = DEPOT / rel
        if not d.is_dir():
            echecs.append("dossier de contrôle absent : %s" % rel)
        elif not PC.porte_son_lot(d):
            echecs.append("%s porte un lot et l'outil ne le voit pas — un pointeur "
                          "l'écraserait" % rel)
    for rel in SANS_LOT:
        controles += 1
        d = DEPOT / rel
        if not d.is_dir():
            echecs.append("dossier de contrôle absent : %s" % rel)
        elif PC.porte_son_lot(d):
            echecs.append("%s ne porte aucun lot et l'outil croit le contraire" % rel)

    # ── 2. un lot ne se cache jamais derrière un renvoi ─────────────────────
    # Un dossier peut GRANDIR : recevoir son propre lot et son propre README. La
    # table est alors en retard, et ce n'est pas une faute — l'outil le signale
    # et n'écrase rien. Ce qui reste interdit, c'est un dossier qui porte un lot
    # ET garde le README engendré, lequel affirme le contraire.
    for code, (dossier, _cible, _t, _q, _e) in sorted(PC.POINTEURS.items()):
        controles += 1
        d = DEPOT / dossier
        if d.is_dir() and PC.porte_son_lot(d) and readme_est_engendre(d):
            echecs.append("le pointeur %s vise un dossier qui porte un lot DERRIÈRE le "
                          "README engendré : celui-ci affirme « aucune ressource propre » "
                          "et c'est faux" % code)

    # ── 3. « ce code y est évalué » — déclaration contre mesure ─────────────
    index = banques_du_depot()
    for code, (dossier, cible, _t, _q, evalue) in sorted(PC.POINTEURS.items()):
        controles += 1
        n, _banques = PC.mesure(code, dossier, cible, index)
        if bool(evalue) != (n >= SEUIL_EVALUABLE):
            echecs.append("%s : déclaré « %s », mesuré %d question(s) dans la banque de la "
                          "cible (seuil %d)"
                          % (code, "évalué" if evalue else "non évalué", n, SEUIL_EVALUABLE))

    # ── 4. « la notion s'évalue ailleurs » doit dire OÙ ─────────────────────
    # On ne pose pas la question au dépôt : la réponse changerait avec lui. On
    # fabrique un index où le code n'est nulle part dans la cible et bien
    # présent ailleurs — le cas exact de `3e_C7.2` le 30/08/2026.
    faux_index = {("3e", "C7.2"): [
        ("%s/3e/3e_C7.6/qcm_3e_C7.6_le-boitier.html" % C7, 10, False),
        ("%s/3e/3e_C7.1/qcm_3e_C7_capteur-confort-ny.html" % C7, 0, False),
    ]}
    dossier, cible = "%s/3e/3e_C7.2" % C7, "../3e_C7.1/sequence_3e_C7_capteur-confort-ny.html"
    controles += 1
    dedans, _ou = PC.mesure("3e_C7.2", dossier, cible, faux_index)
    if dedans != 0:
        echecs.append("mesure() compte %d question(s) dans la banque de la cible, alors "
                      "qu'elle n'en porte aucune" % dedans)
    controles += 1
    dehors, ou = PC.mesure_ailleurs("3e_C7.2", dossier, cible, faux_index)
    if dehors != 10 or ou != ["qcm_3e_C7.6_le-boitier.html"]:
        echecs.append("mesure_ailleurs() dit %d question(s) dans %s — attendu 10 dans "
                      "qcm_3e_C7.6_le-boitier.html" % (dehors, ou))
    controles += 1
    phrase = PC.ENSEIGNE_AILLEURS.format(code="3e_C7.2", n=dehors,
                                         banques=", ".join("`%s`" % b for b in ou))
    if "qcm_3e_C7.6_le-boitier.html" not in phrase or "10" not in phrase:
        echecs.append("la phrase « évalué ailleurs » ne nomme ni la banque ni le nombre")
    controles += 1
    if "c'est à vous de dire où vous l'évaluez" not in PC.ENSEIGNE:
        echecs.append("la phrase ENSEIGNE a changé : ce banc ne teste plus ce qu'il croit")
    if "c'est à vous de dire où" in PC.ENSEIGNE_AILLEURS:
        echecs.append("ENSEIGNE_AILLEURS renvoie encore l'enseignant à lui-même alors "
                      "qu'une banque évalue le code")

    # ── 4 bis. le thème annoncé est celui du référentiel, pas celui du gabarit
    # Le modèle portait « thème 3 » EN DUR, parce que les dix premiers pointeurs
    # étaient tous du thème 3. Les onze suivants sont du thème 1 (règle n°256).
    for code, attendu in (("5e_C3.3", 1), ("3e_C1.2", 1), ("4e_C7.2", 3),
                          ("4e_C9.2", 3)):
        controles += 1
        if PC.theme(code) != attendu:
            echecs.append("%s : thème %s, attendu %d" % (code, PC.theme(code), attendu))
    controles += 1
    if "thème {theme}" not in PC.MODELE:
        echecs.append("le gabarit ne lit plus le thème : il est redevenu écrit en dur")

    # ── 5. l'outil lui-même doit passer, sans rien avoir à réécrire ─────────
    controles += 1
    if PC.main(etat=True) != 0:
        echecs.append("pointeurs_codes.py --etat sort en erreur")

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — dossiers propres, cibles, déclarations mesurées" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
