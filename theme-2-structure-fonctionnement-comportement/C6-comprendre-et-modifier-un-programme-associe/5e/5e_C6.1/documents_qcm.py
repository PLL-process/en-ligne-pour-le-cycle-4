# -*- coding: utf-8 -*-
"""Le document du QCM de 5e_C6.1, lu dans la séquence elle-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT les six étapes de l'algorithme du lampadaire dans la correction de l'activité 2 (« a) L'ordre des
étapes »). Le document « L'algorithme du lampadaire » les montre dans l'ordre, sans dire ce qu'est chaque donnée ni
pourquoi les cas sont rangés ainsi : c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_5e_C6.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C6.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_5e_C6.1.json")
SEQ = open(os.path.join(ICI, "sequence_5e_C6.1-C6.3_programmer_lampadaire.html"), encoding="utf-8").read()
_c = SEQ[SEQ.index("a) L'ordre des étapes"):]
_c = _c[:_c.index("b) Les mots-clés")]
_c = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", _c)))
ETAPES = [e.strip() for e in re.findall(r"[①②③④⑤⑥]\s*([^①②③④⑤⑥]+)", _c)]
ETAPES = [re.sub(r"\s+([:;])", "\u00a0\\1", e) for e in ETAPES]
ETAPES = [re.sub(r" (\S+)$", "\u00a0\\1", e.replace(" %", "\u00a0%").replace("en veille à 30", "en veille\u00a0à\u00a030")) for e in ETAPES]   # pas de mot seul en fin d'étape
assert len(ETAPES) == 6 and ETAPES[0].startswith("Mesurer") and ETAPES[-1].startswith("Recommencer"), ETAPES


def donnees():
    return {
        "qcm": ["qcm_5e_C6.1-C6.3_programmer_lampadaire.html"],
        "documents": {
            "doc_algorithme_lampadaire": {
                "titre": "L'algorithme du lampadaire",
                "sous_titre": "Le programme du lampadaire, traduit en français, étape par étape.",
                "desc": "L'algorithme du lampadaire, en six étapes : "
                        + " ".join("%d. %s" % (k + 1, e) for k, e in enumerate(ETAPES))
                        + " Le document ne dit pas quelles données viennent des capteurs.",
                "blocs": [{"fiches": [{"titre": "Les étapes, dans l'ordre",
                                       "lignes": ["%d. %s" % (k + 1, e) for k, e in enumerate(ETAPES)]}]}],
                "note": "lux : l'unité d'éclairement · Le document ne range pas les données : c'est la "
                        "question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C6.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_5e_C6.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
