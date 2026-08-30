# -*- coding: utf-8 -*-
"""tests_controle_couverture.py — ce que l'outil doit refuser de croire.

Un diagnostic qui se trompe est pire qu'un diagnostic absent : il rassure.
Les deux règles que `controle_couverture.py` applique — « ce texte nomme-t-il
ce code ? » et « ce fichier enseigne-t-il ou oriente-t-il ? » — sont donc
vérifiées ici sur des cas construits pour les mettre en défaut.

Usage : python3 _outils/tests_controle_couverture.py
Sortie : 0 si tout passe, 1 sinon.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from controle_couverture import ORIENTATION, SEUIL_EVALUABLE, _motif  # noqa: E402

#: (code, niveau, texte, doit_correspondre, pourquoi ce cas existe)
NOMMAGE = [
    ("C7.1", "3e", "le code 3e_C7.1 est cité", True,
     "forme préfixée, séparée par un souligné"),
    ("C7.1", "3e", "synthese_eleve_3e_C7.1.html", True,
     "un nom de fichier nomme le code aussi bien qu'une phrase"),
    ("C7.4", "5e", "matrice_couverture_5e_C7.4.csv", True,
     "le point de l'extension ne doit pas casser la reconnaissance"),
    ("C4.1", "4e", "qcm_4e_C4.1-C4.9_jardin.html", True,
     "un intervalle de codes nomme bien le premier"),
    ("C7.1", "3e", "voir C7.1 plus bas", True,
     "le code peut être écrit sans son niveau"),
    ("C9.1", "3e", "3e C9.1 avec une espace", True,
     "le niveau peut être séparé par une espace"),
    ("C1.1", "5e", "le code 5e_C1.10 n'existe pas", False,
     "C1.1 ne doit jamais être lu dans C1.10 — règle d'or n°229"),
    ("C7.1", "3e", "XC7.1 collé à une lettre", False,
     "une lettre devant n'est pas une frontière"),
    ("C7.1", "3e", "2.C7.1 collé à un point", False,
     "un point devant non plus : 2.C7.1 est une numérotation"),
]

#: (chemin relatif, est_une_piece_d_orientation, pourquoi)
ORIENTE = [
    ("README.md", True, "un README dit où aller, il n'enseigne pas"),
    ("manifest_lot_04.json", True, "un manifeste inventorie"),
    ("lexique_3e_C7.1.html", True, "un lexique définit des mots, pas un geste"),
    ("SOURCES_MEDIAS.md", True, "une liste de sources n'est pas une preuve de couverture"),
    ("Synthèses/synthese_eleve.html", False, "une synthèse enseigne"),
    ("fiche_pedagogique_4e_C7.md", False, "une fiche atteste"),
    ("matrice_couverture_4e_C7.csv", False, "une matrice atteste"),
    ("qcm_4e_C7.html", False, "un QCM évalue"),
    ("sequence_3e_C7.1.html", False, "une séquence enseigne"),
]


def main():
    echecs = []

    for code, niveau, texte, attendu, pourquoi in NOMMAGE:
        obtenu = bool(_motif(niveau, code).search(texte))
        if obtenu != attendu:
            echecs.append("nommage %s dans %r : attendu %s, obtenu %s (%s)"
                          % (code, texte, attendu, obtenu, pourquoi))

    for rel, attendu, pourquoi in ORIENTE:
        obtenu = bool(ORIENTATION.search(rel))
        if obtenu != attendu:
            echecs.append("orientation %r : attendu %s, obtenu %s (%s)"
                          % (rel, attendu, obtenu, pourquoi))

    if SEUIL_EVALUABLE != 5:
        echecs.append("le seuil d'évaluabilité a changé sans que ce test le sache "
                      "(%d) — voir controle_echantillonnage.py" % SEUIL_EVALUABLE)

    total = len(NOMMAGE) + len(ORIENTE) + 1
    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (total - len(echecs), total))
        return 1
    print("✅ %d contrôles — nommage, orientation, seuil" % total)
    print("\n%d / %d" % (total, total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
