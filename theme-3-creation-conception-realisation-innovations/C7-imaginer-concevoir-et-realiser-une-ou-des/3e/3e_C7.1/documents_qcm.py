# -*- coding: utf-8 -*-
"""Le document neuf du QCM de 3e_C7.1, lu dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : le protocole d'essai de l'activité 2 est dans la page (le tableau des quatre
scénarios, chacun avec sa température). Ce script l'y LIT, avec la règle d'alerte que la page énonce. Un scénario ou une
température changés dans la séquence changent le document du QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_3e_C7.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C7.1.json
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C7.1.json")
SEQ = open(os.path.join(ICI, "sequence_3e_C7_capteur-confort-ny.html"), encoding="utf-8").read()

i = SEQ.index("<tr><th>Scénario</th><th>T (°C)</th><th>Ta prédiction</th><th>Observé au simulateur</th></tr>")
TABLE = SEQ[i:SEQ.index("</table>", i)]
SCENARIOS = re.findall(r"<tr><td>([^<]+)</td><td>(\d+)</td>", TABLE)
assert [s[0] for s in SCENARIOS] == ["Salle fraîche", "Seuil exact", "Surchauffe", "Retour au frais"], SCENARIOS
assert "strictement supérieur à 28" in SEQ
SEUIL = 28


def donnees():
    lignes = [[nom, "%s °C" % t, "", ""] for nom, t in SCENARIOS]
    dire = " ".join("%s : %s degrés." % (nom, t) for nom, t in SCENARIOS)
    return {
        "qcm": ["qcm_3e_C7_capteur-confort-ny.html"],
        "documents": {
            "doc_protocole_seuil": {
                "titre": "Le protocole d'essai du capteur",
                "sous_titre": "Quatre scénarios, joués au simulateur, dans cet ordre.",
                "desc": "Le protocole d'essai du capteur de confort. La règle : alerte si la température est "
                        "strictement supérieure à %d degrés Celsius. Quatre scénarios, dans l'ordre, avec leur "
                        "température : %s Le tableau a quatre colonnes, dans cet ordre : scénario, température, "
                        "prédiction, observé ; les deux dernières sont vides." % (SEUIL, dire),
                "blocs": [
                    {"fiches": [{"titre": "La règle du capteur", "accent": True,
                                 "lignes": ["Alerte si T est strictement supérieure à %d °C." % SEUIL]}]},
                    {"tableau": {"colonnes": ["Scénario", "T", "Prédiction", "Observé"],
                                 "largeurs": [118, 50, 80, 74], "lignes": lignes}},
                ],
                "note": "T : la température de la salle · °C : degré Celsius · les deux dernières colonnes se "
                        "remplissent pendant l'essai.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C7.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_3e_C7.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
