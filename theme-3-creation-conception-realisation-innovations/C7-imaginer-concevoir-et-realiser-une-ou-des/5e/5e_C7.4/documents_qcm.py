# -*- coding: utf-8 -*-
"""Les documents du QCM de 5e_C7.4, calculés par le modèle du lot (règles d'or n°233 et n°345, 27/11/2026).

Aucun nombre n'est recopié : tout vient de `energie.py` (le montage du hall, les sources, le panneau en Martinique).
Un nombre changé dans le modèle change le document du QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_5e_C7.4.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C7.4.json
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import energie as E  # noqa: E402

SORTIE = os.path.join(ICI, "documents_qcm_5e_C7.4.json")
LIEU = E.LIEUX["5e"]
COURT = {"Carte Arduino UNO": "Carte UNO", "DEL indicatrice": "DEL", "Capteur de présence du sac": "Capteur"}
SRC = {"Pile 9 V alcaline": "Pile 9 V", "4 piles AA alcalines": "4 piles AA",
       "Accu Li-ion 18650 rechargeable": "Accu Li-ion"}


def v(x, dec):
    return E.wh_txt(x, dec).replace(".", ",")


def g(x):
    return ("%g" % x).replace(".", ",")


def donnees():
    total, det = E.energie_jour(E.MONTAGES["5e"])
    det = sorted(det, key=lambda d: -d[3])
    conso = [[COURT[n], g(ma) + " mA", "%s h" % g(h), v(wh, 3 if wh < 0.1 else 2) + " Wh"] for n, ma, h, wh in det]
    conso.append(["Total", "", "", v(total, 2) + " Wh"])
    stock = [s for s in E.SOURCES if s.capacite]
    sec = next(s for s in E.SOURCES if s.nom.startswith("Secteur"))
    pan = next(s for s in E.SOURCES if s.nom.startswith("Panneau"))
    sources = [[SRC[s.nom], v(s.brute, 2) + " Wh", "%d %%" % round(s.conversion * 100), v(s.utile, 1) + " Wh"]
               for s in stock]
    recolte = E.solaire(1, LIEU)
    dire_conso = " ".join("%s : %s milliampères pendant %s heures, %s wattheures." % (n, g(ma), g(h),
                          v(wh, 3 if wh < 0.1 else 2)) for n, ma, h, wh in det)
    dire_src = " ".join("%s : %s wattheures stockés, rendement %d pour cent, %s wattheures utiles." % (
        s.nom.replace(" V ", " volts "), v(s.brute, 2), round(s.conversion * 100), v(s.utile, 1)) for s in stock)
    return {
        "qcm": ["qcm_5e_C7.4_indicateur-du-hall.html"],
        "documents": {
            "doc_conso_hall": {
                "titre": "Ce que consomme l'indicateur du hall",
                "sous_titre": "Trois composants, sous 5 V (volts), pendant une journée de classe.",
                "desc": "Ce que consomme l'indicateur du hall en une journée, sous 5 volts. " + dire_conso
                        + " Total : %s wattheures par jour." % v(total, 2),
                "blocs": [{"tableau": {"colonnes": ["Composant", "Courant", "Durée", "Énergie"],
                                       "largeurs": [104, 70, 58, 90], "lignes": conso}}],
                "note": "Capteur : le capteur de présence du sac · mA : milliampère · h : heure · Wh : wattheure · "
                        "énergie = courant × 5 V × durée.",
            },
            "doc_sources_hall": {
                "titre": "Cinq sources pour l'indicateur",
                "sous_titre": "Ce que chacune stocke, et ce qui arrive vraiment au montage, sous 5 V (volts).",
                "desc": "Cinq sources d'énergie pour l'indicateur du hall. " + dire_src
                        + " Le secteur, par un adaptateur USB : pas de réserve, rendement %d pour cent. Le panneau "
                          "solaire de 1 watt crête, avec son accumulateur : %s wattheures par jour %s."
                        % (round(sec.conversion * 100), v(recolte, 1), E.EN_LIEU[LIEU]),
                "blocs": [
                    {"tableau": {"colonnes": ["Source", "Stockée", "Rendement", "Utile"],
                                 "largeurs": [96, 78, 76, 72], "lignes": sources}},
                    {"fiches": [
                        {"titre": "Secteur (adaptateur USB)", "lignes": ["Pas de réserve : il donne tant qu'il y a "
                                                                         "du réseau, rendement %d %%."
                                                                         % round(sec.conversion * 100)]},
                        {"titre": "Panneau 1 W crête + accu",
                         "lignes": ["%s Wh par jour %s." % (v(recolte, 1), E.EN_LIEU[LIEU])]},
                    ]},
                ],
                "note": "Wh : wattheure · Stockée : l'énergie dans la source · Utile : ce qui arrive au montage, "
                        "sous 5 V · W crête : watt crête, la puissance du panneau en plein soleil.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C7.4.json est à jour du modèle" if ok
              else "✘ documents_qcm_5e_C7.4.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
