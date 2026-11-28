# -*- coding: utf-8 -*-
"""Le document du QCM de 5e_C5.1, lu dans la séquence elle-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT les six observations de l'inspecteur dans la séquence (`const ZONES`, activité 1) : ce qu'on VOIT, zone par
zone, sans le classement (normal, anomalie, anomalie grave). Classer, et désigner la pièce, c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_5e_C5.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C5.1.json
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_5e_C5.1.json")
SEQ = open(os.path.join(ICI, "sequence_5e_C5.1-C5.3_depanner_lampadaire.html"), encoding="utf-8").read()
_z = SEQ[SEQ.index("const ZONES = {"):]
_z = _z[:_z.index("};")]
ZONES = [(m.group(2), m.group(3)) for m in re.finditer(r'(\d):"Zone \d — ([^:]+?) : (.*?)",?\n', _z)]
assert len(ZONES) == 6, ZONES
for _, obs in ZONES:
    assert not re.search(r"anomalie|normal(?!\b)", obs.split("Rien d'anormal")[0]), obs


def donnees():
    return {
        "qcm": ["qcm_5e_C5.1-C5.3_depanner_lampadaire.html"],
        "documents": {
            "doc_carnet_inspection": {
                "titre": "Le carnet d'inspection du lampadaire n°3",
                "sous_titre": "Lundi matin, après l'orage : ce que l'inspecteur a vu, zone par zone.",
                "desc": "Le carnet d'inspection du lampadaire n°3, lundi matin après l'orage. "
                        + " ".join("Zone %d, %s : %s" % (k + 1, z, o) for k, (z, o) in enumerate(ZONES))
                        + " Le carnet ne classe aucune observation.",
                "blocs": [{"fiches": [{"titre": "%d. %s" % (k + 1, z[0].upper() + z[1:]),
                                       "lignes": [(o[0].upper() + o[1:]).replace("« ", "«\u00a0").replace(" »", "\u00a0»")]}
                                      for k, (z, o) in enumerate(ZONES)]}],
                "note": "Le carnet ne classe aucune observation : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C5.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_5e_C5.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
