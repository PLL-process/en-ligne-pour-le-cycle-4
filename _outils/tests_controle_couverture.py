# -*- coding: utf-8 -*-
"""tests_controle_couverture.py — ce que l'outil doit refuser de croire.

Un diagnostic qui se trompe est pire qu'un diagnostic absent : il rassure.
Les trois règles que `controle_couverture.py` applique — « ce texte nomme-t-il
ce code ? », « ce fichier enseigne-t-il ou oriente-t-il ? » et « à quel(s)
code(s) cette étiquette se rattache-t-elle ? » — sont donc vérifiées ici sur
des cas construits pour les mettre en défaut.

La troisième famille de cas existe parce que la première version de l'outil ne
lisait pas les légendes `COMP_LABELS` : elle a conclu que sept banques ne
nommaient aucun code, alors qu'elles le nommaient toutes. Chaque cas de
`LEGENDES` est un exemple réel du dépôt, y compris les deux sur lesquels je
m'étais trompé.

Usage : python3 _outils/tests_controle_couverture.py
Sortie : 0 si tout passe, 1 sinon.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from controle_couverture import (ORIENTATION, SEUIL_EVALUABLE,  # noqa: E402
                                 _motif, codes_de_letiquette)

#: (étiquette, libellé de la légende, niveau, codes attendus, pourquoi)
LEGENDES = [
    ("PAR", "4e_C8.1 — 🖐️ Paramétrer la simulation", "4e", ["C8.1"],
     "le cas qui a fait tomber la première version de l'outil"),
    ("PRO", "4e_C8.2 — 📐 Proposer un protocole", "4e", ["C8.2"],
     "j'avais lu C8.3 dans les questions ; la légende dit C8.2"),
    ("SEU", "CRCN 3.4 · 1.3 · 5.1 — 📐 Le seuil, le programme, le diagnostic",
     "3e", [],
     "une légende peut déclarer un groupe HORS du référentiel — ce n'est pas un manque"),
    ("ID", "Information et données — 4e_C4.4 · C4.5 · C4.6", "4e",
     ["C4.4", "C4.5", "C4.6"],
     "une légende peut nommer plusieurs codes : les questions sont partagées"),
    ("C6.1", "5e_C6.1 — Identifier les données du programme", "5e", ["C6.1"],
     "étiquette et légende disent la même chose : un seul code, pas deux"),
    ("MOD", "5e_C9.2 · C9.3 — 🔧 Modifier et régler", "5e", ["C9.2", "C9.3"],
     "le second code est écrit sans son niveau"),
    ("C4.2", "", "5e", ["C4.2"],
     "sans légende, l'étiquette elle-même fait foi"),
]

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

    for etiquette, libelle, niveau, attendu, pourquoi in LEGENDES:
        obtenu = codes_de_letiquette(etiquette, libelle, niveau)
        if obtenu != attendu:
            echecs.append("légende %r → %r : attendu %s, obtenu %s (%s)"
                          % (etiquette, libelle[:40], attendu, obtenu, pourquoi))

    # ── un compteur qui ne nomme personne ne se corrige pas ─────────────────
    # Le relevé sautait les lignes VIDE et se contentait d'un « VIDE 11 » dans
    # le résumé. Onze dossiers du thème 1 sont restés muets des semaines
    # derrière ce nombre. On vérifie ici une PROPRIÉTÉ, pas un compte : quel
    # que soit l'état du dépôt, tout code en VIDE doit être NOMMÉ dans la
    # sortie. Le jour où il n'y en aura plus, le test passera tout autant.
    import contextlib
    import io
    from controle_couverture import main as releve_complet
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        releve_complet()
    sortie = tampon.getvalue()
    controles_muets = 1
    if "dossier(s) MUET(S)" not in sortie:
        echecs.append("le relevé ne comporte plus de section « dossiers muets » : "
                      "les VIDE redeviennent invisibles")
    else:
        from controle_couverture import parcourir
        muets = [l["libelle"] for l in parcourir() if l["etat"] == "VIDE"]
        controles_muets += len(muets)
        for code in muets:
            if code not in sortie:
                echecs.append("%s est en VIDE et n'est nommé nulle part dans le "
                              "relevé — il resterait invisible" % code)

    if SEUIL_EVALUABLE != 5:
        echecs.append("le seuil d'évaluabilité a changé sans que ce test le sache "
                      "(%d) — voir controle_echantillonnage.py" % SEUIL_EVALUABLE)

    total = len(NOMMAGE) + len(ORIENTE) + len(LEGENDES) + 1 + controles_muets
    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (total - len(echecs), total))
        return 1
    print("✅ %d contrôles — nommage, orientation, légendes, seuil, et chaque "
          "dossier muet nommé" % total)
    print("\n%d / %d" % (total, total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
