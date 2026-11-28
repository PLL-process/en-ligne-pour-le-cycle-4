# -*- coding: utf-8 -*-
"""Le document du QCM de 3e_C4.1, lu dans la séquence elle-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT dans l'activité 2 (« Dimensionner pour tenir 72 h ») la ligne des ressources — la consommation de la
station, la tension de la batterie, les deux relations — et les batteries du catalogue proposées au choix. Le document
« Dimensionner la batterie » les montre sans aucun résultat de calcul : faire le calcul, c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_3e_C4.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C4.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C4.1.json")
SEQ = open(os.path.join(ICI, "sequence_3e_C4.1-C4.2_energie_station.html"), encoding="utf-8").read()


def clair(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


_a = SEQ[SEQ.index("Dimensionner pour tenir 72 h"):]
_a = _a[:_a.index("Le crash-test cyclone")]
RES = clair(re.search(r"<b>Ressources\s*:</b>(.*?)</div>", _a, re.S).group(1))
CONSO = re.search(r"conso de la station : (\d+) W en continu", RES).group(1)
TENSION = re.search(r"batterie (\d+) V", RES).group(1)
DUREE = re.search(r"tenir (\d+) h", SEQ[SEQ.index("Dimensionner pour tenir"):][:40]).group(1)
assert "énergie (Wh) = puissance (W) × durée (h)" in RES and "capacité (Ah) = énergie (Wh) ÷ tension (V)" in RES, RES
CATALOGUE = [re.match(r"(\d+) Ah", v).group(1) for v in re.findall(r'name="d2_3" id="d2_3__\d" value="([^"]+)"', _a)
             if re.match(r"\d+ Ah", v)]
CATALOGUE = sorted(set(CATALOGUE), key=int)
assert (CONSO, TENSION, DUREE, CATALOGUE) == ("6", "12", "72", ["20", "40", "100"]), (CONSO, TENSION, DUREE, CATALOGUE)


def donnees():
    return {
        "qcm": ["qcm_3e_C4.1-C4.2_energie_station.html"],
        "documents": {
            "doc_dimensionner_batterie": {
                "titre": "Dimensionner la batterie",
                "sous_titre": "W : watts · Wh : wattheures · Ah : ampères-heures · V : volts · h : heures.",
                "desc": "Les données pour dimensionner la batterie de la station. Le besoin : la station consomme %s W "
                        "(watts) en continu ; elle doit tenir %s h (heures) sans réseau, pendant un cyclone ; sa batterie "
                        "est sous %s V (volts). Les deux relations : énergie (Wh, wattheures) = puissance (W) × durée "
                        "(h) ; capacité (Ah, ampères-heures) = énergie (Wh) ÷ tension (V). Le catalogue propose des "
                        "batteries de %s Ah. Le document ne donne aucun résultat de calcul."
                        % (CONSO, DUREE, TENSION, ", ".join(CATALOGUE[:-1]) + " et " + CATALOGUE[-1]),
                "blocs": [
                    {"fiches": [{"titre": "Le besoin", "paires": [["Consommation", CONSO + " W en continu"],
                                                                  ["Autonomie exigée", DUREE + " h"],
                                                                  ["Tension", TENSION + " V"]]}]},
                    {"fiches": [{"titre": "Les deux relations",
                                 "lignes": ["énergie = puissance × durée", "   en Wh = W × h",
                                            "capacité = énergie ÷ tension", "   en Ah = Wh ÷ V"]}]},
                    {"fiches": [{"titre": "Le catalogue", "lignes": ["Batteries de " + " · ".join(c + " Ah" for c in CATALOGUE)]}]},
                ],
                "note": "Le document ne donne aucun résultat de calcul : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C4.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_3e_C4.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
