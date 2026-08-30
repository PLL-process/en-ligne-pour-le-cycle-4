# -*- coding: utf-8 -*-
"""tests_pointeurs_codes.py — les deux promesses qu'un pointeur ne doit plus faire.

Un README de pointeur affirme deux choses vérifiables :

  1. « **Ce dossier ne porte aucune ressource propre.** »
  2. « **Ce code y est évalué.** »

Les deux étaient écrites de confiance. La première a failli coûter cher : le
jour où `5e_C8.1` et `3e_C8.1` ont reçu leur propre lot, relancer l'outil aurait
remplacé deux lots complets par un renvoi. La seconde était fausse pour trois
pointeurs sur dix.

Ce banc vérifie qu'aucune des deux ne peut plus être écrite sans avoir été
mesurée — sur le dépôt réel, pas sur des exemples inventés.

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

#: dossiers qui portent leur propre lot — un pointeur les écraserait
AVEC_LOT = [
    C8 + "/5e/5e_C8.1",
    C8 + "/3e/3e_C8.1",
    C8 + "/3e/3e_C8.2",
]

#: dossiers qui n'ont vraiment aucune ressource propre
SANS_LOT = [
    "theme-3-creation-conception-realisation-innovations/"
    "C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.2",
    "theme-3-creation-conception-realisation-innovations/"
    "C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.6",
]


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

    # ── 2. aucun pointeur ne vise un dossier qui porte son lot ──────────────
    for code, (dossier, _cible, _t, _q, _e) in sorted(PC.POINTEURS.items()):
        controles += 1
        d = DEPOT / dossier
        if d.is_dir() and PC.porte_son_lot(d):
            echecs.append("le pointeur %s vise un dossier qui porte son propre lot : "
                          "retirer l'entrée de POINTEURS" % code)

    # ── 3. « ce code y est évalué » — déclaration contre mesure ─────────────
    index = banques_du_depot()
    for code, (dossier, cible, _t, _q, evalue) in sorted(PC.POINTEURS.items()):
        controles += 1
        n, _banques = PC.mesure(code, dossier, cible, index)
        if bool(evalue) != (n >= SEUIL_EVALUABLE):
            echecs.append("%s : déclaré « %s », mesuré %d question(s) dans la banque de la "
                          "cible (seuil %d)"
                          % (code, "évalué" if evalue else "non évalué", n, SEUIL_EVALUABLE))

    # ── 4. l'outil lui-même doit passer, sans rien avoir à réécrire ─────────
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
