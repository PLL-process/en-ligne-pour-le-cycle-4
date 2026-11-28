# -*- coding: utf-8 -*-
"""Le document du QCM de 4e_C7.8, lu dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : le banc de la séquence porte ses données dans la page (`const CHAMPS` : chaque
champ qu'un message du jardin pourrait porter, avec ce qu'il dit et une valeur d'exemple). Ce script les y LIT. Le
document montre tous les champs possibles, sans dire lesquels sont requis : c'est ce que les questions font trouver.
Un champ changé dans la séquence change le document du QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_4e_C7.8.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C7.8.json
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C7.8.json")
SEQ = open(os.path.join(ICI, "sequence_4e_C7.8_le-jardin-publie.html"), encoding="utf-8").read()
_l = re.search(r"^const CHAMPS = (.*)$", SEQ, re.M).group(1)
CHAMPS, _ = json.JSONDecoder().raw_decode(_l)
assert [c["cle"] for c in CHAMPS][:5] == ["id", "h", "u", "t", "pompe"], CHAMPS


def ecrit(v):
    if v is False:
        return "false"
    if v is True:
        return "true"
    return str(v)


def donnees():
    lignes = ["%s : %s — %s." % (c["cle"], ecrit(c["val"]), c["lib"]) for c in CHAMPS]
    return {
        "qcm": ["qcm_4e_C7.8_le-jardin-publie.html"],
        "documents": {
            "doc_champs_message": {
                "titre": "Ce que le jardin pourrait envoyer",
                "sous_titre": "Les %d champs possibles d'un message, avec une valeur d'exemple." % len(CHAMPS),
                "desc": "Les %d champs qu'un message du jardin connecté pourrait porter, chacun avec une valeur "
                        "d'exemple et ce qu'il dit. " % len(CHAMPS) + " ".join(lignes),
                "blocs": [
                    {"tableau": {"colonnes": ["Champ", "Exemple"], "largeurs": [110, 212],
                                 "lignes": [[c["cle"], ecrit(c["val"])] for c in CHAMPS]}},
                    {"fiches": [{"titre": "Ce que dit chaque champ",
                                 "lignes": ["%s : %s." % (c["cle"], c["lib"].replace(" au moment de la mesure", ", quand on mesure")) for c in CHAMPS]}]},
                ],
                "note": "Le document ne dit pas lesquels envoyer : c'est la question. · false : faux, la pompe est "
                        "arrêtée · % : pour cent.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C7.8.json est à jour de la séquence" if ok
              else "✘ documents_qcm_4e_C7.8.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
