# -*- coding: utf-8 -*-
"""Les documents du QCM de 4e_C7.7, calculés par le modèle du lot (règles d'or n°233 et n°345, 27/11/2026).

Aucun nombre n'est recopié : tout vient de `moyens.py` (les cinq moyens de l'atelier pour le support du capteur, ce
qu'ils tiennent, ce qu'ils acceptent, leur temps de préparation et leur temps par pièce, et ce que le support exige).
Un nombre changé dans le modèle change le document du QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_4e_C7.7.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C7.7.json
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import moyens as M  # noqa: E402

SORTIE = os.path.join(ICI, "documents_qcm_4e_C7.7.json")
PIECE = "support"
COURT = {"laser": "Découpe laser", "fraiseuse": "Fraiseuse", "impression": "Impression 3D",
         "sciage": "Sciage à la main", "thermoformage": "Thermoformage"}


def mm(x):
    return M.vg(x, 2).rstrip("0").rstrip(",") + " mm"


def donnees():
    p = M.PIECES[PIECE]
    cles = M.MOYENS_PAR_PIECE[PIECE]
    traits = {c: v for c, _, v, _ in p["traits"]}
    capac = []
    for c in cles:
        m = M.MOYENS[c]
        capac.append([COURT[c], mm(m["tol"]), "vif" if m["r_int"] == 0 else mm(m["r_int"]),
                      "oui" if m["traversant"] else "non"])
    matieres = ["%s : %s." % (COURT[c], ", ".join(M.MOYENS[c]["matieres"])) for c in cles]
    tps = [[COURT[c], M.duree_txt(M.MOYENS[c]["prep"]), M.duree_txt(M.MOYENS[c]["min_piece"])] for c in cles]
    dire_c = " ".join("%s : tolérance %s, angle interne %s, %s, matières : %s." % (
        COURT[c], mm(M.MOYENS[c]["tol"]).replace("mm", "millimètre"),
        "vif" if M.MOYENS[c]["r_int"] == 0 else "arrondi à " + mm(M.MOYENS[c]["r_int"]).replace("mm", "millimètre"),
        "il perce de part en part" if M.MOYENS[c]["traversant"] else "il ne perce pas",
        ", ".join(M.MOYENS[c]["matieres"])) for c in cles)
    dire_t = " ".join("%s : %s, puis %s par pièce." % (
        COURT[c], "aucune préparation" if M.MOYENS[c]["prep"] == 0 else
        M.duree_txt(M.MOYENS[c]["prep"]).replace("min", "minutes").replace(" h", " heure") + " de préparation",
        M.duree_txt(M.MOYENS[c]["min_piece"]).replace("min", "minutes")) for c in cles)
    exige = [["Matière", p["matiere"]], ["Fente", "à %s près" % mm(traits["tol"])],
             ["Paroi", mm(traits["epaisseur"])], ["Perçages", "deux, traversants"]]
    return {
        "qcm": ["qcm_4e_C7.7_support-du-capteur.html"],
        "documents": {
            "doc_moyens_support": {
                "titre": "Cinq moyens pour le support",
                "sous_titre": "Ce que le support exige, puis ce que sait faire chaque moyen de l'atelier.",
                "desc": "Le support du capteur d'humidité exige : du PMMA, une fente à %s près, une paroi de %s, deux "
                        "perçages traversants. Les cinq moyens de l'atelier. %s"
                        % (mm(traits["tol"]).replace("mm", "millimètre"),
                           mm(traits["epaisseur"]).replace("mm", "millimètres"), dire_c),
                "blocs": [
                    {"fiches": [{"titre": "Ce que le support exige", "accent": True, "paires": exige}]},
                    {"intertitre": "Ce que sait faire chaque moyen"},
                    {"tableau": {"colonnes": ["Moyen", "Tolérance", "Angle", "Perce"],
                                 "largeurs": [124, 76, 70, 52], "lignes": capac}},
                    {"fiches": [{"titre": "Les matières qu'il accepte", "lignes": matieres}]},
                ],
                "note": "mm : millimètre · Tolérance : l'écart qu'il tient sur une cote · Angle : l'angle interne "
                        "le plus vif qu'il laisse · Perce : il traverse la plaque · PMMA : le verre acrylique · PVC, PLA, PETG, PP : des plastiques.",
            },
            "doc_temps_support": {
                "titre": "Le temps de chaque moyen",
                "sous_titre": "Une préparation payée une fois, puis un temps pour chaque pièce.",
                "desc": "Le temps de chaque moyen pour le support du capteur. %s Temps de machine disponible avant "
                        "la date : %s." % (dire_t, M.duree_txt(p["temps_dispo"]).replace(" h", " heures")),
                "blocs": [
                    {"tableau": {"colonnes": ["Moyen", "Préparation", "Par pièce"],
                                 "largeurs": [140, 96, 86], "lignes": tps}},
                    {"fiches": [{"titre": "Temps de machine disponible", "accent": True,
                                 "lignes": ["%s avant la date." % M.duree_txt(p["temps_dispo"])]}]},
                ],
                "note": "min : minute · h : heure · temps total = préparation + nombre de pièces × temps par pièce.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C7.7.json est à jour du modèle" if ok
              else "✘ documents_qcm_4e_C7.7.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
