# -*- coding: utf-8 -*-
"""Les documents du QCM de 3e_C7.5, lus dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

L'établi de la séquence porte ses données dans la page : le catalogue des dix constituants (`const CONST`), le courant
que fournit l'USB (`const BUDGET`), celui de l'alimentation externe, et le programme téléversé dans la carte. Ce script
les y LIT : un courant ou une ligne du programme changés dans la séquence changent le document du QCM — et
`--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_3e_C7.5.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C7.5.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C7.5.json")
SEQ = open(os.path.join(ICI, "sequence_3e_C7.5_station-a-equiper.html"), encoding="utf-8").read()

_l = re.search(r"^const CONST = (.*)$", SEQ, re.M).group(1)
CONST, _ = json.JSONDecoder().raw_decode(_l[_l.index("["):])
BUDGET = int(re.search(r"^const BUDGET = (\d+);", SEQ, re.M).group(1))
EXTERNE = int(re.search(r"l'alimentation externe \((\d+) mA\)", SEQ).group(1))
PROG = re.search(r'<div class="prog">(vent = .*?)</div>', SEQ, re.S).group(1)
PROG = [html.unescape(re.sub(r'<span class="cm">.*?</span>', "", l)).rstrip() for l in PROG.split("\n")]
assert PROG[0].startswith("vent = analogRead(A0)") and len(PROG) == 6, PROG

COURT = {"carte": "Carte UNO", "shield": "Base Shield", "anemo": "Anémomètre", "pluie": "Capteur de pluie",
         "lcd": "Écran LCD", "bandeau": "Bandeau de 8 DEL", "buzzer": "Buzzer", "sd": "Module carte SD",
         "usb": "Câble USB", "alim": "Batterie + panneau"}
SOURCES = ("usb", "alim")


def milliers(n):
    return "{:,}".format(n).replace(",", " ")


def donnees():
    conso = [[COURT[c["id"]], "%d mA" % c["mA"]] for c in CONST if c["id"] not in SOURCES]
    dire_c = " ".join("%s : %d milliampères." % (COURT[c["id"]], c["mA"]) for c in CONST if c["id"] not in SOURCES)
    code = [l.strip() for l in PROG]
    prog = ["%s%s" % ("→ " if PROG[i].startswith("    ") else "", code[i]) for i in range(len(code))]
    return {
        "qcm": ["qcm_3e_C7.5_station-a-equiper.html"],
        "documents": {
            "doc_catalogue_station": {
                "titre": "Le carton de la station",
                "sous_titre": "Les constituants proposés, et le courant que demande chacun.",
                "desc": "Le catalogue des constituants proposés pour la station d'alerte, avec le courant que demande "
                        "chacun. " + dire_c + " Le câble USB fournit jusqu'à %d milliampères ; la batterie 5 volts et "
                        "son panneau solaire, jusqu'à %s milliampères." % (BUDGET, milliers(EXTERNE)),
                "blocs": [
                    {"tableau": {"colonnes": ["Constituant", "Demande"], "largeurs": [218, 104], "lignes": conso}},
                    {"fiches": [{"titre": "Ce que fournissent les sources", "accent": True,
                                 "paires": [["Câble USB", "jusqu'à %d mA" % BUDGET],
                                            ["Batterie + panneau", "jusqu'à %s mA" % milliers(EXTERNE)]]}]},
                ],
                "note": "mA : milliampère · la batterie est une très basse tension, 5 V (volts) · SD : la carte "
                        "mémoire · DEL : diode électroluminescente.",
            },
            "doc_programme_station": {
                "titre": "Le programme de la station",
                "sous_titre": "Celui qui est téléversé dans la carte.",
                "desc": "Le programme téléversé dans la carte de la station, ligne par ligne : " + " ; ".join(code) + ".",
                "blocs": [{"fiches": [{"titre": "Programme", "lignes": prog}]}],
                "note": "→ : ligne qui dépend du « si » ou du « sinon » au-dessus · analogRead(A0) : lire le port "
                        "analogique A0 · enregistrer : écrire sur la carte SD · digitalWrite(6, HAUT) : mettre la "
                        "sortie D6 à l'état haut, le bandeau passe au rouge.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C7.5.json est à jour de la séquence" if ok
              else "✘ documents_qcm_3e_C7.5.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
