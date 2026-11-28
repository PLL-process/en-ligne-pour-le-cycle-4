# -*- coding: utf-8 -*-
"""Les documents des QCM d'adressage et de Zigbee de 4e_C4.7 (règles d'or n°233 et n°345, 28/11/2026).

- « Le plan d'adressage de la serre » : LU dans la séquence (le tableau de l'activité « plan d'adressage » : appareil,
  adresse IP, masque, passerelle), et la remarque qui dit la passerelle prévue mais non installée.
- « Quatre liaisons sans fil » : les ordres de grandeur que les corrections du QCM Zigbee donnent déjà (q4 : 250 kbit/s
  pour Zigbee, 100 Mbit/s pour le Wi-Fi ; q6 : 10 à 100 m ; q21 : quelques centimètres pour le NFC ; q28 : 10 m pour
  le Bluetooth, 50 m pour le Wi-Fi). Le script vérifie que chacun y est encore écrit : si une correction change, il
  refuse. Le débit du Bluetooth (de l'ordre de 2 Mbit/s) et du NFC (de l'ordre de 400 kbit/s) sont les valeurs des
  normes, en ordre de grandeur.

    python3 documents_qcm.py             écrit documents_qcm_4e_C4.7.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C4.7.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C4.7.json")


def lire(nom):
    return open(os.path.join(ICI, nom), encoding="utf-8").read()


def clair(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


SEQ = lire("sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html")
_t = SEQ[SEQ.index('aria-label="Le plan d\'adressage du réseau'):]
_t = _t[:_t.index("</table>")]
PLAN = [[clair(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr)] for tr in re.findall(r"<tr><td.*?</tr>", _t, re.S)]
assert [p[0] for p in PLAN] == ["PC-Prof", "Imprimante", "Capteur-Serre", "Serveur-Serre"] and all(len(p) == 4 for p in PLAN), PLAN
assert "prévue au plan mais non installée" in clair(SEQ[SEQ.index("Remarque d'urbaniste"):][:400])

ZIG = clair(lire("qcm_4e_C4.7_zigbee_domotique.html"))
for morceau in ("250 kbit/s", "100 Mbit/s", "10 à 100 m", "quelques centimètres", "NFC : 5 cm", "Bluetooth : 10 m", "Wi-Fi : 50 m"):
    assert morceau in ZIG, morceau
LIAISONS = [  # liaison, portée, débit, énergie consommée
    ("Wi-Fi", "50 m", "100 Mbit/s", "forte"),
    ("Bluetooth", "10 m", "2 Mbit/s", "moyenne"),
    ("Zigbee", "10 à 100 m", "250 kbit/s", "faible"),
    ("NFC", "5 cm", "400 kbit/s", "faible"),
]


def donnees():
    return {
        "qcm": ["qcm_4e_C4.7_adressage_ip.html", "qcm_4e_C4.7_zigbee_domotique.html"],
        "documents": {
            "doc_plan_adressage_serre": {
                "titre": "Le plan d'adressage de la serre",
                "sous_titre": "Les appareils du réseau de la serre, et ce que chacun a reçu à la main.",
                "desc": "Le plan d'adressage du réseau de la serre. "
                        + " ".join("%s : adresse IP %s, masque %s, passerelle %s." % tuple(p) for p in PLAN)
                        + " La passerelle 192.168.20.1 est prévue au plan, mais pas encore installée.",
                "blocs": [
                    {"tableau": {"colonnes": ["Appareil", "Adresse IP"], "largeurs": [140, 182],
                                 "lignes": [[p[0], p[1]] for p in PLAN]}},
                    {"fiches": [{"titre": "Pour tous les appareils",
                                 "lignes": ["Masque : " + PLAN[0][2] + ".", "Passerelle : " + PLAN[0][3] + ", prévue, pas encore installée."]}]},
                ],
                "note": "Le plan ne dit pas quelle adresse donner à un nouvel appareil : c'est la question.",
            },
            "doc_quatre_liaisons": {
                "titre": "Quatre liaisons sans fil",
                "sous_titre": "Ordres de grandeur. Débit en Mbit/s (mégabits par seconde) ou en kbit/s (kilobits "
                              "par seconde).",
                "desc": "Quatre liaisons sans fil, en ordres de grandeur. "
                        + " ".join("%s : portée %s, débit %s, consommation %s." % l for l in LIAISONS)
                        .replace("100 Mbit/s", "100 Mbit/s (mégabits par seconde)", 1)
                        .replace("250 kbit/s", "250 kbit/s (kilobits par seconde)", 1)
                        + " Le document ne dit pas quelle liaison choisir.",
                "blocs": [{"tableau": {"colonnes": ["Liaison", "Portée", "Débit", "Énergie"],
                                       "largeurs": [80, 76, 82, 84],
                                       "lignes": [list(l) for l in LIAISONS]}}],
                "note": "Portée : la distance que couvre un appareil · cm : centimètres · Énergie : ce qu'il "
                        "consomme pour émettre · Le document ne dit pas quelle liaison choisir : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C4.7.json est à jour du lot" if ok
              else "✘ documents_qcm_4e_C4.7.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
