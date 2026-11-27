# -*- coding: utf-8 -*-
"""Les documents du QCM de 5e_C7.5, lus dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

L'établi de la séquence porte ses données dans la page (`const CONST`, `const ATTENDU`, `const BUDGET`, et le programme
téléversé dans la carte). Ce script les y LIT : un port, un courant ou une ligne du programme changés dans la séquence
changent le document du QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_5e_C7.5.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C7.5.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_5e_C7.5.json")
SEQ = open(os.path.join(ICI, "sequence_5e_C7.5_eclairage-du-preau.html"), encoding="utf-8").read()

CONST = json.loads(re.search(r"^const CONST = (\[.*\]);$", SEQ, re.M).group(1))
ATTENDU = json.loads(re.search(r"^const ATTENDU = (\{.*?\});", SEQ, re.M).group(1))
BUDGET = int(re.search(r"^const BUDGET = (\d+);", SEQ, re.M).group(1))
PROG = re.search(r'<div class="prog">(.*?)</div>', SEQ, re.S).group(1)
PROG = [html.unescape(re.sub(r"<span class=\"cm\">.*?</span>", "", l)).rstrip() for l in PROG.split("\n")]
assert PROG[0].startswith("lumiere = analogRead(A0)") and len(PROG) == 5, PROG

COURT = {"carte": "Carte UNO", "shield": "Base Shield", "lum": "Capteur de lumière", "del": "Module DEL",
         "usb": "Câble USB"}
PLACE = {"carte": "sur l'établi", "shield": "sur la carte", "usb": "sur la carte"}


def donnees():
    lignes, dire = [], []
    for c in CONST:
        port = ATTENDU.get(c["id"], PLACE.get(c["id"], "?"))
        mA = "%d mA" % c["mA"] if c["id"] != "usb" else "—"
        lignes.append([COURT[c["id"]], port, mA])
        dire.append("%s : %s, %s." % (c["nom"] if c["id"] != "usb" else "Câble USB", "port " + port if c["id"] in ATTENDU else port,
                                      "%d milliampères" % c["mA"] if c["id"] != "usb"
                                      else "il fournit jusqu'à %d milliampères" % BUDGET))
    code = [l.strip() for l in PROG]
    prog = ["%s%s" % ("→ " if PROG[i].startswith("    ") else "", code[i]) for i in range(len(code))]
    return {
        "qcm": ["qcm_5e_C7.5_eclairage-du-preau.html"],
        "documents": {
            "doc_montage_preau": {
                "titre": "Le prototype de l'éclairage du préau",
                "sous_titre": "Les cinq constituants montés, et le courant que chacun demande.",
                "desc": "Le prototype de l'éclairage du préau, cinq constituants. " + " ".join(dire),
                "blocs": [{"tableau": {"colonnes": ["Constituant", "Branché sur", "Courant"],
                                       "largeurs": [150, 100, 72], "lignes": lignes}}],
                "note": "mA : milliampère · le câble USB fournit jusqu'à %d mA à tout le montage." % BUDGET,
            },
            "doc_programme_preau": {
                "titre": "Le programme de la carte",
                "sous_titre": "Celui qui est téléversé dans la carte du préau.",
                "desc": "Le programme téléversé dans la carte, ligne par ligne : " + " ; ".join(code) + ".",
                "blocs": [{"fiches": [{"titre": "Programme", "lignes": prog}]}],
                "note": "→ : ligne qui dépend de la ligne « si » ou « sinon » au-dessus · analogRead(A0) : lire le port analogique A0 · digitalWrite(5, HAUT) : mettre la sortie D5 "
                        "à l'état haut, la DEL s'allume · BAS : à l'état bas, elle s'éteint.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C7.5.json est à jour de la séquence" if ok
              else "✘ documents_qcm_5e_C7.5.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
