# -*- coding: utf-8 -*-
"""Le document du QCM de 4e_C5.1, lu dans le lot lui-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT dans le schéma de l'activité 3 (`Images/choix_procedes_support.svg`) ce qu'on sait de la pièce à refaire,
de son environnement, et les noms des trois procédés candidats — sans aucune des cases ✔ / ✘ du tableau de choix :
choisir, c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_4e_C5.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C5.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C5.1.json")
SVG = open(os.path.join(ICI, "Images", "choix_procedes_support.svg"), encoding="utf-8").read()
T = [html.unescape(t).strip() for t in re.findall(r"<text[^>]*>([^<]*)", SVG)]
_p = T.index("La pièce à refaire")
PIECE = T[_p + 1:_p + 4]                    # diamètre, forme, état
_e = T.index("Son environnement : le jardin")
ENV = [T[_e + 1], T[_e + 2], "%s %s" % (T[_e + 3], T[_e + 4]), T[_e + 5]]
PROCEDES = [t for t in T if re.match(r"^(🖨|✂|🪚) ", t)]
assert PIECE[0] == "⌀ 10,0 mm" and len(PROCEDES) == 3 and ENV[-1].startswith("la pièce vivra DEHORS"), (PIECE, ENV, PROCEDES)
assert not any("✔" in x or "✘" in x for x in PIECE + ENV + PROCEDES)


def donnees():
    return {
        "qcm": ["qcm_4e_C5.1-C5.3_depanner_jardin.html"],
        "documents": {
            "doc_clip_a_refaire": {
                "titre": "Le clip-support à refaire",
                "sous_titre": "Ce qu'on sait de la pièce cassée, de l'endroit où elle vivra, et les procédés de "
                              "l'atelier.",
                "desc": "Le clip-support du capteur d'humidité, à refaire. La pièce : diamètre du capteur qu'elle tient "
                        "10,0 mm (millimètres) ; %s ; %s. Son environnement, le jardin : %s. Les procédés de l'atelier : "
                        "%s. Le document ne dit pas lequel choisir."
                        % (PIECE[1], PIECE[2], ", ".join(ENV), ", ".join(re.sub(r"^\W+\s*", "", p) for p in PROCEDES)),
                "blocs": [
                    {"fiches": [{"titre": "La pièce", "lignes": ["Diamètre du capteur à tenir : 10,0 mm.",
                                                                 PIECE[1][0].upper() + PIECE[1][1:] + ".",
                                                                 PIECE[2][0].upper() + PIECE[2][1:] + "."]}]},
                    {"fiches": [{"titre": "Son environnement : le jardin",
                                 "lignes": [", ".join(ENV[:3]).replace("soleil + UV", "Soleil et UV") + ".",
                                            ENV[3][0].upper() + ENV[3][1:] + "."]}]},
                    {"fiches": [{"titre": "Les procédés de l'atelier", "lignes": PROCEDES}]},
                ],
                "note": "mm : millimètres · UV : les rayons ultraviolets du soleil · Le document ne dit pas quel "
                        "procédé choisir : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C5.1.json est à jour du lot" if ok
              else "✘ documents_qcm_4e_C5.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
