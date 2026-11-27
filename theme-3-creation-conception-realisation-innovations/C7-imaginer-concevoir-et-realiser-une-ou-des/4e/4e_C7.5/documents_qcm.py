# -*- coding: utf-8 -*-
"""Les documents du QCM de 4e_C7.5, lus dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

L'établi de la séquence porte ses données dans la page : les constituants (`const CONST`), les trois prototypes livrés
(`const CAS`) et le programme téléversé dans la carte. Ce script les y LIT : un courant, un port, un cas ou une ligne du
programme changés dans la séquence changent le document du QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_4e_C7.5.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C7.5.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C7.5.json")
SEQ = open(os.path.join(ICI, "sequence_4e_C7.5_jardin-incomplet.html"), encoding="utf-8").read()

CONST = {c["id"]: c for c in json.loads(re.search(r"^const CONST = (\[.*\]);$", SEQ, re.M).group(1))}
BUDGET = int(re.search(r"^const BUDGET = (\d+);", SEQ, re.M).group(1))
EXTERNE = int(re.search(r"l'alimentation externe \((\d+) mA\)", SEQ).group(1))
CAS = {k: (txt, dict(re.findall(r'(\w+):"([^"]+)"', ports))) for k, txt, ports in re.findall(
    r'"(\d)": \{txt:"([^"]+)",\s*ports:\{(.*?)\}\}', SEQ, re.S)}
assert sorted(CAS) == ["1", "2", "3"], CAS
PROG = re.search(r'<div class="prog">(humidite = .*?)</div>', SEQ, re.S).group(1)
PROG = [html.unescape(re.sub(r'<span class="cm">.*?</span>', "", l)).rstrip() for l in PROG.split("\n")]
assert PROG[0].startswith("humidite = analogRead(A0)") and len(PROG) == 6, PROG

COURT = {"carte": "Carte UNO", "shield": "Base Shield", "hum": "Capteur d'humidité", "temp": "Capteur de température",
         "relais": "Module relais", "pompe": "Pompe", "lcd": "Écran LCD", "alim": "Alimentation externe",
         "usb": "Câble USB"}
PORT = {"SOCLE": "", "I2C": "I2C", "ALIM EXT": ""}
COMMUNS = ["carte", "shield", "usb"]


def monte(ports):
    noms = []
    for cid, p in ports.items():
        if cid in COMMUNS:
            continue
        lieu = PORT.get(p, p)
        noms.append(COURT[cid].lower().replace("écran lcd", "écran LCD") + (" sur " + lieu if lieu else ""))
    return noms


def donnees():
    fiches_cas, dire_cas = [], []
    for k in sorted(CAS):
        txt, ports = CAS[k]
        symptome = txt.split(" — ", 1)[1]
        noms = monte(ports)
        fiches_cas.append({"titre": "Cas %s" % k, "lignes": ["On observe : " + symptome, "Monté : " + ", ".join(noms) + "."]})
        dire_cas.append("Cas %s. Symptôme : %s Monté, en plus de la carte, du Base Shield et du câble USB : %s."
                        % (k, symptome, ", ".join(noms)))
    conso = [[COURT[i], "%d mA" % CONST[i]["mA"]] for i in ["pompe", "carte", "relais", "lcd", "hum", "temp"]]
    dire_conso = " ".join("%s : %d milliampères." % (COURT[i], CONST[i]["mA"])
                          for i in ["pompe", "carte", "relais", "lcd", "hum", "temp"])
    code = [l.strip() for l in PROG]
    prog = ["%s%s" % ("→ " if PROG[i].startswith("    ") else "", code[i]) for i in range(len(code))]
    return {
        "qcm": ["qcm_4e_C7.5_jardin-incomplet.html"],
        "documents": {
            "doc_cas_jardin": {
                "titre": "Trois prototypes livrés",
                "sous_titre": "Pour chacun : ce qu'on observe, et ce qui est monté.",
                "desc": "Trois prototypes du jardin connecté, livrés incomplets ou mal montés. " + " ".join(dire_cas),
                "blocs": [{"fiches": fiches_cas}],
                "note": "Dans les trois cas, la carte, le Base Shield et le câble USB sont montés · I2C : le port de "
                        "l'écran · A0 : un port analogique · D4 : un port numérique.",
            },
            "doc_courant_jardin": {
                "titre": "Le courant du jardin connecté",
                "sous_titre": "Ce que demande chaque constituant, et ce que fournit chaque source.",
                "desc": "Ce que demande chaque constituant du jardin connecté. " + dire_conso
                        + " Le câble USB fournit jusqu'à %d milliampères ; l'alimentation externe 5 volts, jusqu'à "
                          "%d milliampères." % (BUDGET, EXTERNE),
                "blocs": [
                    {"tableau": {"colonnes": ["Constituant", "Demande"], "largeurs": [218, 104], "lignes": conso}},
                    {"fiches": [{"titre": "Ce que fournissent les sources", "accent": True,
                                 "paires": [["Câble USB", "jusqu'à %d mA" % BUDGET],
                                            ["Alimentation externe", "jusqu'à %s mA" % "{:,}".format(EXTERNE).replace(",", "\u00a0")]]}]},
                ],
                "note": "mA : milliampère · l'alimentation externe est une très basse tension, 5 V (volts).",
            },
            "doc_programme_jardin": {
                "titre": "Le programme de la carte",
                "sous_titre": "Celui qui est téléversé dans la carte du jardin.",
                "desc": "Le programme téléversé dans la carte du jardin, ligne par ligne : " + " ; ".join(code) + ".",
                "blocs": [{"fiches": [{"titre": "Programme", "lignes": prog}]}],
                "note": "→ : ligne qui dépend du « si » au-dessus · analogRead(A0) : lire le port analogique A0 · "
                        "digitalWrite(4, HAUT) : mettre la sortie D4 à l'état haut, le relais se ferme · BAS : il "
                        "s'ouvre.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C7.5.json est à jour de la séquence" if ok
              else "✘ documents_qcm_4e_C7.5.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
