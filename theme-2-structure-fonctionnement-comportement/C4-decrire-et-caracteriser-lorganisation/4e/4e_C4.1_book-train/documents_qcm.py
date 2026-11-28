# -*- coding: utf-8 -*-
"""Le document du QCM du Book Train (4e_C4.1), lu dans le lot lui-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT les étapes du trajet du livre dans l'algorigramme corrigé de la séquence
(`Images/algorigramme_book-train_correction.svg`) et les remet dans l'ordre, en texte : sans les symboles, sans les
mots « Entrée » et « Sortie », sans les flèches OUI / NON. Choisir le symbole de chaque étape, et trouver où mène un
NON, c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_4e_C4.1_book-train.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C4.1_book-train.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C4.1_book-train.json")
SVG = open(os.path.join(ICI, "Images", "algorigramme_book-train_correction.svg"), encoding="utf-8").read()
TEXTES = [html.unescape(t).strip() for t in re.findall(r"<text[^>]*>([^<]*)", SVG)]
TEXTES = TEXTES[:TEXTES.index("FIN") + 1]          # après FIN : les étiquettes OUI / NON des flèches


def etapes():
    """Recolle les lignes coupées du dessin : une étape commence par une majuscule, ou par « Entrée : » / « Sortie : »."""
    out = []
    for t in TEXTES:
        if out and (t[:1].islower() or t.startswith("(")):
            out[-1] += " " + t
        else:
            out.append(t)
    propre = []
    for e in out:
        e = re.sub(r"^(Entrée|Sortie) : ", "", e)
        e = {"DÉBUT": "Début", "FIN": "Fin"}.get(e, e)
        propre.append(e[0].upper() + e[1:])
    return propre


ETAPES = etapes()
assert ETAPES[0] == "Début" and ETAPES[-1] == "Fin" and len(ETAPES) == 10, ETAPES
assert any(e.endswith("?") for e in ETAPES)


def donnees():
    return {
        "qcm": ["qcm_book-train.html"],
        "documents": {
            "doc_trajet_book_train": {
                "titre": "Le trajet du livre, dans l'ordre",
                "sous_titre": "Les étapes du Book Train, de la commande au retour du wagonnet, avant d'être dessinées "
                              "en algorigramme.",
                "desc": "Les dix étapes du trajet du livre dans le Book Train, dans l'ordre : "
                        + " ".join("%d. %s%s" % (k + 1, e, "" if e.endswith("?") else ".") for k, e in enumerate(ETAPES))
                        + " Le document ne dit ni le symbole de chaque étape, ni où mène une réponse NON.",
                "blocs": [{"fiches": [{"titre": "Les étapes",
                                       "lignes": ["%d. %s%s" % (k + 1, e, "" if e.endswith("?") else ".")
                                                  for k, e in enumerate(ETAPES)]}]}],
                "note": "Le document ne dit ni le symbole de chaque étape, ni où mène une réponse NON : c'est la "
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
        print("✅ documents_qcm_4e_C4.1_book-train.json est à jour du lot" if ok
              else "✘ documents_qcm_4e_C4.1_book-train.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
