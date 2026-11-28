# -*- coding: utf-8 -*-
"""Les documents du QCM de 3e_C4.3, lus dans le lot lui-même (règles d'or n°233 et n°345, 28/11/2026).

- « Un extrait des mesures de la station » : six lignes du fichier `donnees/mesures_station_48h_simulees.csv` (une toutes
  les huit heures), avec l'heure, le vent, la pression et la vigilance. Données SIMULÉES, comme le dit le fichier.
- « Le baromètre et son CAN » : l'étendue du baromètre et le nombre de bits de son CAN, LUS dans la consigne de
  l'activité du simulateur de la séquence — sans le plus grand nombre que sort le CAN, ni la valeur d'un palier.

    python3 documents_qcm.py             écrit documents_qcm_3e_C4.3.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C4.3.json
"""
import csv
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C4.3.json")
SEQ = open(os.path.join(ICI, "sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html"), encoding="utf-8").read()
_csv = open(os.path.join(ICI, "donnees", "mesures_station_48h_simulees.csv"), encoding="utf-8").read().splitlines()
assert _csv[0].startswith("# Données SIMULÉES")
LIGNES = list(csv.DictReader(_csv[1:], delimiter=";"))
EXTRAIT = [l for k, l in enumerate(LIGNES) if k % 8 == 0][:6]
assert len(EXTRAIT) == 6


def court(h):
    j, hm = h.split()
    return "%s/%s %s" % (j[8:10], j[5:7], hm[:5])


_c = re.sub(r"<[^>]+>", " ", SEQ[SEQ.index("Le baromètre simulé mesure"):][:300])
_c = re.sub(r"\s+", " ", html.unescape(_c))
MIN, MAX, BITS = re.search(r"mesure de (\d+) hPa \(hectopascals\) à (\d+) hPa et son CAN travaille sur (\d+) bits", _c).groups()
assert (MIN, MAX, BITS) == ("868", "1018", "10")


def donnees():
    return {
        "qcm": ["qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html"],
        "documents": {
            "doc_extrait_mesures_station": {
                "titre": "Un extrait des mesures de la station",
                "sous_titre": "Sainte-Luce, du 28 au 29 août : une mesure toutes les huit heures. Données simulées.",
                "desc": "Un extrait du fichier de mesures de la station de Sainte-Luce, données simulées, une ligne toutes "
                        "les huit heures. "
                        + " ".join("Le %s : vent %s km/h (kilomètres par heure), pression %s hPa (hectopascals), "
                                   "vigilance %s." % (court(l["horodatage"]), l["vent_kmh"], l["pression_hpa"], l["vigilance"])
                                   for l in EXTRAIT[:1])
                        + " " + " ".join("Le %s : vent %s km/h, pression %s hPa, vigilance %s."
                                         % (court(l["horodatage"]), l["vent_kmh"], l["pression_hpa"], l["vigilance"])
                                         for l in EXTRAIT[1:]),
                "blocs": [{"tableau": {"colonnes": ["Heure", "Vent", "Pression", "Vigilance"],
                                       "largeurs": [94, 56, 80, 92],
                                       "lignes": [[court(l["horodatage"]), l["vent_kmh"], l["pression_hpa"], l["vigilance"]]
                                                  for l in EXTRAIT]}}],
                "note": "Vent en km/h (kilomètres par heure) · Pression en hPa (hectopascals) · Données simulées à but "
                        "pédagogique, aucune mesure réelle de Météo-France.",
            },
            "doc_can_barometre": {
                "titre": "Le baromètre et son CAN",
                "sous_titre": "Le CAN, convertisseur analogique-numérique, change la tension du capteur en un nombre "
                              "entier N.",
                "desc": "Le baromètre de la station mesure de %s hPa (hectopascals) à %s hPa. Son CAN, convertisseur "
                        "analogique-numérique, travaille sur %s bits : il change la tension du capteur en un nombre "
                        "entier N. Le document ne dit ni le plus grand N possible, ni ce que vaut un palier." % (MIN, MAX, BITS),
                "blocs": [
                    {"fiches": [{"titre": "Le baromètre", "paires": [["Plus basse pression", MIN + " hPa"],
                                                                     ["Plus haute pression", MAX + " hPa"]]}]},
                    {"fiches": [{"titre": "Son CAN", "paires": [["Nombre de bits", BITS], ["Il sort", "un entier N"]]}]},
                ],
                "note": "hPa : hectopascals · Le document ne dit ni le plus grand N possible, ni ce que vaut un "
                        "palier : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C4.3.json est à jour du lot" if ok
              else "✘ documents_qcm_3e_C4.3.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
