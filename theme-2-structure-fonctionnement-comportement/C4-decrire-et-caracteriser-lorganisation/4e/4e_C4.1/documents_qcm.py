# -*- coding: utf-8 -*-
"""Le document du QCM de 4e_C4.1, lu dans le lot lui-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT l'extrait de la table « mesures_jardin » dans le schéma de la séquence (`Images/table_donnees_jardin.svg`,
celui de l'activité « du capteur à la table »), et la règle d'arrosage dans l'aide de la séquence (« 38 < seuil 40 »).
Le document « Un extrait de la table du jardin » montre les lignes et la règle, sans la raison écrite à côté de chaque
arrosage : la retrouver, c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_4e_C4.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C4.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C4.1.json")
SVG = open(os.path.join(ICI, "Images", "table_donnees_jardin.svg"), encoding="utf-8").read()
SEQ = open(os.path.join(ICI, "sequence_4e_C4.1-C4.9_jardin_connecte.html"), encoding="utf-8").read()

TEXTES = [html.unescape(t).strip() for t in re.findall(r"<text[^>]*>([^<]*)", SVG)]
_i = TEXTES.index("arrosage_declenche") + 1
LIGNES = []
while _i + 4 < len(TEXTES) and re.fullmatch(r"\d{3}", TEXTES[_i]):
    ident, horo, capteur, hum, arr = TEXTES[_i:_i + 5]
    LIGNES.append((ident, horo.split()[1], capteur, hum, "OUI" if arr.startswith("OUI") else "non"))
    _i += 5
assert [l[0] for l in LIGNES] == ["341", "342", "343", "356", "357", "371"], LIGNES
DATE = TEXTES[TEXTES.index("arrosage_declenche") + 2].split()[0]
SEUIL = re.search(r"38 &lt; seuil (\d+)", SEQ).group(1)
assert SEUIL == "40"


def donnees():
    return {
        "qcm": ["qcm_4e_C4.1-C4.9_jardin_connecte.html"],
        "documents": {
            "doc_table_mesures_jardin": {
                "titre": "Un extrait de la table du jardin",
                "sous_titre": "La table « mesures_jardin » du %s : une ligne par mesure téléversée." % DATE,
                "desc": "Un extrait de la table « mesures_jardin » du %s. " % DATE
                        + " ".join("Ligne %s : %s, %s, humidité %s %%, arrosage %s." % l for l in LIGNES)
                        + " La règle du jardin : arroser un bac quand son humidité passe sous le seuil de %s %%." % SEUIL
                        + " Le document ne dit pas pourquoi chaque arrosage s'est déclenché.",
                "blocs": [
                    {"tableau": {"colonnes": ["id", "heure · capteur", "humidité", "arrosage"],
                                 "largeurs": [50, 120, 70, 82],
                                 "lignes": [[l[0], "%s · %s" % (l[1], l[2]), l[3] + " %", l[4]] for l in LIGNES]}},
                    {"fiches": [{"titre": "La règle du jardin",
                                 "lignes": ["Arroser un bac quand son humidité passe sous le seuil de %s %%." % SEUIL]}]},
                ],
                "note": "humidité : en % (pour cent) · Le document ne dit pas pourquoi chaque arrosage s'est "
                        "déclenché : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C4.1.json est à jour du lot" if ok
              else "✘ documents_qcm_4e_C4.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
