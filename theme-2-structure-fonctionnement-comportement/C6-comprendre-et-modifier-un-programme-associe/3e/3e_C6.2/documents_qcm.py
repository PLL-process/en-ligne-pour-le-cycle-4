# -*- coding: utf-8 -*-
"""Le document du QCM de 3e_C6.2, lu dans la séquence elle-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT les huit instructions de l'auto-test dans la correction de l'activité 3 (« 1. » à « 8. »), et
l'instruction manquante qu'elle ajoute (« ajouter organe à pannes »), avec la liste vide du pas ② de l'activité 2.
Le document « Le programme de l'auto-test » les montre dans l'ordre, indentées : il ne dit pas ce que produit le
programme pour un cas donné — c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_3e_C6.2.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C6.2.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C6.2.json")
SEQ = open(os.path.join(ICI, "sequence_3e_C6.2_auto_test_station.html"), encoding="utf-8").read()
NB = " "

_c = SEQ[SEQ.index("<b>1.</b> <code>organes = "):]
_c = _c[:_c.index("</details>")]
INSTR = {int(n): html.unescape(code) for n, code in re.findall(r"<b>(\d)\.</b> <code>(.*?)</code>", _c)}
assert sorted(INSTR) == list(range(1, 9)), INSTR
assert "<code>ajouter organe à pannes</code>" in _c and "<code>pannes = liste vide</code>" in SEQ
INSTR[8] = INSTR[8].replace("SINON ", "")   # « SINON envoyer(…) » : le SINON prend sa ligne

PROG = [(0, INSTR[1]), (0, INSTR[2]), (0, "pannes = liste vide"), (0, INSTR[3]), (1, INSTR[4]), (2, INSTR[5]),
        (2, "ajouter organe à pannes"), (0, INSTR[6]), (1, INSTR[7]), (0, "SINON"), (1, INSTR[8])]
assert PROG[3][1].startswith("POUR CHAQUE") and PROG[7][1] == "SI defauts > 0 ALORS", PROG


def _ligne(niv, t):
    t = t.replace(" = ", NB + "=" + NB).replace(" + ", NB + "+" + NB).replace(" > ", NB + ">" + NB)
    return NB * 4 * niv + t


# la liste des organes, trop longue pour une ligne du téléphone, passe à la ligne après la virgule, alignée
assert PROG[0][1] == "organes = [anemometre, gyrophare, sirene, radio]", PROG[0]
LIGNES = [_ligne(0, "organes = [anemometre, gyrophare,"), NB * 11 + "sirene, radio]"] + [_ligne(n, t) for n, t in PROG[1:]]


def donnees():
    return {
        "qcm": ["qcm_3e_C6.2_auto_test.html"],
        "documents": {
            "doc_programme_auto_test": {
                "titre": "Le programme de l'auto-test",
                "sous_titre": "Chaque matin, la station vérifie ses quatre organes, puis prévient le gardien.",
                "desc": "Le programme de l'auto-test, dans l'ordre : " + " / ".join(
                    ("(décalée %d fois) " % n if n else "") + t for n, t in PROG)
                        + ". Le document ne dit pas ce que produit le programme dans un cas donné.",
                "blocs": [{"fiches": [{"titre": "Le programme, dans l'ordre", "lignes": LIGNES}]}],
                "note": "tester(organe) répond VRAI si l'organe marche · Une ligne décalée appartient à celle du dessus.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C6.2.json est à jour de la séquence" if ok
              else "✘ documents_qcm_3e_C6.2.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
