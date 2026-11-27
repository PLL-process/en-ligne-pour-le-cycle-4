# -*- coding: utf-8 -*-
"""Les documents du QCM de 5e_C7.3, calculés par le modèle du lot (règles d'or n°233 et n°345, 27/11/2026).

Aucun nombre n'est recopié : tout vient de `materiaux.py` (les caractéristiques des six matériaux, les exigences du banc,
la masse et le prix de l'assise calculés). Un nombre changé dans le modèle change le document du QCM — et `--verifier`
le dit.

    python3 documents_qcm.py             écrit documents_qcm_5e_C7.3.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C7.3.json
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import materiaux as M  # noqa: E402

SORTIE = os.path.join(ICI, "documents_qcm_5e_C7.3.json")
COURT = {"pin": "Pin nu", "pin_autoclave": "Pin traité", "teck": "Teck", "pvc": "PVC",
         "acier_galva": "Acier galva.", "beton": "Béton"}
LONG = {"pin": "le pin non traité", "pin_autoclave": "le pin traité autoclave", "teck": "le teck", "pvc": "le PVC",
        "acier_galva": "l'acier galvanisé", "beton": "le béton"}


def eur(x):
    return M.vg(x, 2) + " €"


def donnees():
    ex = M.OBJETS["banc"]["exigences"]
    t = M.table("banc", M.CANDIDATS["banc"])
    v = {l["cle"]: l for l in t}
    tenue = [[COURT[l["cle"]], "%d MPa" % l["valeurs"]["sigma"], "%d ans" % l["valeurs"]["uv"],
              "%d / 5" % l["valeurs"]["sel"]] for l in t]
    chaleur = [[COURT[l["cle"]], "%d °C" % l["valeurs"]["chaud"], M.vg(l["masse"], 1) + " kg"] for l in t]
    prix = [[COURT[l["cle"]], M.vg(M.MATERIAUX[l["cle"]]["prix"], 2) + " €", M.vg(l["masse"], 1) + " kg",
             eur(l["cout"])] for l in t]
    dire_tenue = " ".join(
        "%s : résistance %d mégapascals, %d ans au soleil, %d sur 5 au sel, %d degrés au soleil, %s kilogrammes."
        % (LONG[k][0].upper() + LONG[k][1:], l["valeurs"]["sigma"], l["valeurs"]["uv"], l["valeurs"]["sel"],
           l["valeurs"]["chaud"], M.vg(l["masse"], 1)) for k, l in v.items())
    dire_prix = " ".join(
        "%s : %s euros le kilogramme, %s kilogrammes, %s euros l'assise."
        % (LONG[k][0].upper() + LONG[k][1:], M.vg(M.MATERIAUX[k]["prix"], 2), M.vg(l["masse"], 1),
           M.vg(l["cout"], 2)) for k, l in v.items())
    exigences = [["Résistance", "au moins %d MPa" % ex["sigma"]], ["Soleil", "au moins %d ans" % ex["uv"]],
                 ["Sel", "au moins %d / 5" % ex["sel"]], ["Chaleur", "au plus %d °C" % ex["chaud"]],
                 ["Masse", "au plus %d kg" % ex["masse_max"]]]
    return {
        "qcm": ["qcm_5e_C7.3_banc-de-la-cour.html"],
        "documents": {
            "doc_criteres_banc": {
                "titre": "Six matériaux pour l'assise du banc",
                "sous_titre": "Le cahier des charges du banc, puis ce que tient chaque matériau.",
                "desc": "Le cahier des charges de l'assise du banc de la cour : résistance d'au moins %d mégapascals, "
                        "au moins %d ans au soleil, au moins %d sur 5 au sel, au plus %d degrés au soleil, au plus %d "
                        "kilogrammes. Puis les six matériaux. %s"
                        % (ex["sigma"], ex["uv"], ex["sel"], ex["chaud"], ex["masse_max"], dire_tenue),
                "blocs": [
                    {"fiches": [{"titre": "Ce que le banc exige", "accent": True, "paires": exigences}]},
                    {"intertitre": "Ce que tient chaque matériau"},
                    {"tableau": {"colonnes": ["Matériau", "Résistance", "Soleil", "Sel"],
                                 "largeurs": [100, 82, 70, 70], "lignes": tenue}},
                    {"intertitre": "Au soleil, et sur la balance"},
                    {"tableau": {"colonnes": ["Matériau", "Chaleur", "Masse"],
                                 "largeurs": [120, 92, 110], "lignes": chaleur}},
                ],
                "note": "MPa : mégapascal (résistance) · Soleil : années avant de griser ou de fendre · Sel : tenue "
                        "à l'air marin, de 1 à 5 · Chaleur : température de l'assise au soleil de midi · kg : "
                        "kilogramme, masse de l'assise.",
            },
            "doc_prix_banc": {
                "titre": "Le prix de l'assise",
                "sous_titre": "La même assise de 1,60 m, dans chacun des six matériaux.",
                "desc": "Pour chacun des six matériaux, le prix au kilogramme, la masse de l'assise et son prix. "
                        + dire_prix,
                "blocs": [{"tableau": {"colonnes": ["Matériau", "Prix au kg", "Masse", "Assise"],
                                       "largeurs": [106, 66, 68, 82], "lignes": prix}}],
                "note": "kg : kilogramme · prix de l'assise = prix au kilogramme × masse de l'assise ; la masse vient "
                        "du volume de l'assise et de la masse volumique du matériau.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C7.3.json est à jour du modèle" if ok
              else "✘ documents_qcm_5e_C7.3.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
