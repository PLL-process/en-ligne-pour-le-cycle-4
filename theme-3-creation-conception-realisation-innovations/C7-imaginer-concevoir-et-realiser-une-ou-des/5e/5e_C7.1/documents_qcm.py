# -*- coding: utf-8 -*-
"""Les documents du QCM de 5e_C7.1, lus dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : ses nombres sont ceux de la page. Ce script les y LIT (la situation de M. Alvarez,
le planning de l'activité 1a), si bien qu'un nombre changé dans la séquence change le document du QCM — et que
`--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_5e_C7.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C7.1.json
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_5e_C7.1.json")
SEQ = open(os.path.join(ICI, "sequence_5e_C7_mini-projet-objet.html"), encoding="utf-8").read()

# la situation : les nombres que M. Alvarez a relevés
assert "Deux cents élèves entrent en\nhuit minutes" in SEQ and "vingt casiers ouverts" in SEQ
assert "<b>trois chutes en un mois</b>" in SEQ
# le planning de l'activité 1a : numéro, nom de la tâche (placeholder), durée en minutes
PLANNING = [(int(n), nom, int(m)) for n, nom, m in re.findall(
    r'<tr><td>(\d)</td><td><input id="a1t\d" placeholder="([^"]+)"[^>]*></td><td>(\d+)</td></tr>', SEQ)]
assert [p[0] for p in PLANNING] == [1, 2, 3, 4], PLANNING
NOMS = {"Besoin": "Le besoin", "2 solutions": "Deux solutions", "Matériau": "Le matériau", "Prototype": "Le prototype"}


def donnees():
    debut, lignes = 0, []
    for n, nom, m in PLANNING:
        lignes.append([str(n), NOMS[nom], "%d min" % m, "%d → %d" % (debut, debut + m)])
        debut += m
    dire = " ".join("Tâche %s, %s : %s, de la minute %s." % (l[0], l[1].lower(), l[2].replace("min", "minutes"),
                                                             l[3].replace(" → ", " à la minute ")) for l in lignes)
    return {
        "qcm": ["qcm_5e_C7_mini-projet.html"],
        "documents": {
            "doc_releve_hall": {
                "titre": "Ce que M. Alvarez a relevé",
                "sous_titre": "Le hall de la Brooklyn Middle School, le matin, avant la sonnerie.",
                "desc": "Ce que M. Alvarez, qui s'occupe du bâtiment, a relevé dans le hall : deux cents élèves entrent "
                        "en huit minutes ; vingt casiers ouverts, sans porte, contre le mur ; trois chutes en un mois, "
                        "sur des sacs posés par terre ; le hall est un grand espace ouvert.",
                "blocs": [{"fiches": [
                    {"titre": "Les élèves", "lignes": ["200 élèves entrent en 8 minutes."]},
                    {"titre": "Les casiers", "lignes": ["20 casiers ouverts, sans porte, contre le mur."]},
                    {"titre": "Les sacs", "lignes": ["3 chutes en un mois, sur des sacs posés par terre."]},
                    {"titre": "Le hall", "lignes": ["Un grand espace ouvert."]},
                ]}],
                "note": "Relevé tel que M. Alvarez le donne : chaque ligne est un fait, aucune n'est un avis.",
            },
            "doc_planning_equipe": {
                "titre": "Le planning de l'équipe",
                "sous_titre": "Les quatre tâches du mini-projet, dans l'ordre, avec leur durée prévue.",
                "desc": "Le planning de l'équipe, quatre tâches dans l'ordre, chacune avec sa durée prévue et ses minutes "
                        "de début et de fin, comptées depuis le début du projet. " + dire,
                "blocs": [{"tableau": {"colonnes": ["N°", "Tâche", "Durée", "Minutes"],
                                       "largeurs": [36, 128, 70, 88], "lignes": lignes}}],
                "note": "min : minute · « 20 → 45 » : la tâche commence à la minute 20 et finit à la minute 45, "
                        "comptées depuis le début du projet.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C7.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_5e_C7.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
