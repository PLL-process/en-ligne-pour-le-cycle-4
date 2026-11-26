# -*- coding: utf-8 -*-
"""Les documents du QCM de 3e_C8.1, écrits depuis le modèle `mat_station.py` (règles d'or n°233 et n°345, 26/11/2026).

Le QCM se lit sur des documents dessinés pour le téléphone (`_outils/document_qcm.py`). Leurs nombres ne sont pas
recopiés à la main : ce script les calcule avec le modèle du mât, puis écrit `documents_qcm_3e_C8.1.json`.

    python3 documents_qcm.py             écrit le fichier de données
    python3 documents_qcm.py --verifier  dit s'il est à jour (0) ou non (1), sans rien écrire
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C8.1.json   (dessine les SVG)
"""
import json
import os
import sys

import mat_station as M

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C8.1.json")
H = M.HAUTEUR_MESURE
COURT = {"Tube aluminium Ø50 × 3": "Tube alu Ø50", "Barre pleine acier Ø20": "Barre acier Ø20",
         "Tube PVC Ø50 × 3": "Tube PVC Ø50", "Poutre bois 40 × 40": "Poutre bois 40×40",
         "Tube acier galvanisé Ø33,7 × 2,6": "Tube acier Ø33,7"}
NOTE_PROFILS = ("Ø : diamètre, en millimètres · alu : aluminium · PVC : plastique rigide · tube acier : "
                "galvanisé contre la rouille.")


def v1(x):
    return ("%.1f" % x).replace(".", ",")


def nm(x):
    return "%d N·m" % round(x / 1000)


def mille(n):
    return ("%d" % n) if n < 1000 else ("%d %03d" % (n // 1000, n % 1000))


def donnees():
    hm = mille(H)
    lignes_m = [[COURT[p.nom], nm(p.moment(H, "banc")), nm(p.moment(H, "vent"))] for p in M.PROFILES]
    lignes_v = [[COURT[p.nom], v1(p.coefficient(H, "vent", "elastique")), "%d mm" % round(p.fleche(H, "vent"))]
                for p in M.PROFILES]
    lignes_r = [["%s mm" % mille(h), "%d" % len(M.retenus(h, "vent", "rupture")),
                 "%d" % len(M.retenus(h, "vent", "elastique"))] for h in M.HAUTEURS]

    def dire(lignes, a, b, unite=""):
        return " ".join("%s : %s %s, %s %s." % (l[0], a, l[1], b, l[2]) for l in lignes)

    def en_lettres(t):
        return (t.replace(" N·m", " newtons-mètres").replace(" mm", " millimètres").replace("Ø", "diamètre ")
                .replace("×", "sur"))

    return {
        "qcm": ["qcm_3e_C8.1_mat-de-la-station.html"],
        "documents": {
            "doc_moment_banc_vent": {
                "titre": "Le moment au pied du mât",
                "sous_titre": "Mât de %s mm. Le banc pousse %d N en tête ; le vent de %d km/h appuie sur toute la "
                              "hauteur." % (hm, M.POUSSEE_BANC, M.VENT_REFERENCE),
                "desc": en_lettres("Le moment au pied d'un mât de %s mm, pour chaque profilé : sous la poussée du banc, "
                                   "%d newtons en tête, puis sous le vent de %d kilomètres par heure. "
                                   % (hm, M.POUSSEE_BANC, M.VENT_REFERENCE)
                                   + dire(lignes_m, "banc", "vent")),
                "blocs": [{"tableau": {"colonnes": ["Profilé", "Banc", "Vent"],
                                       "largeurs": [170, 76, 76], "lignes": lignes_m}}],
                "note": "N·m : newton-mètre · N : newton · mm : millimètre · km/h : kilomètre par heure. "
                        + NOTE_PROFILS,
            },
            "doc_verdict_vent": {
                "titre": "Le mât sous le vent, profilé par profilé",
                "sous_titre": "Mât de %s mm, vent de %d km/h, sur la limite élastique. Exigé : k ≥ %d et "
                              "flèche ≤ %d mm." % (hm, M.VENT_REFERENCE, M.COEF_EXIGE, M.FLECHE_MAX),
                "desc": en_lettres("Le mât de %s mm sous le vent de %d kilomètres par heure, calculé sur la limite "
                                   "élastique ; il faut un coefficient de sécurité d'au moins %d et une flèche en tête "
                                   "d'au plus %d mm. " % (hm, M.VENT_REFERENCE, M.COEF_EXIGE, M.FLECHE_MAX)
                                   + dire(lignes_v, "coefficient", "flèche")),
                "blocs": [{"tableau": {"colonnes": ["Profilé", "k", "Flèche"],
                                       "largeurs": [170, 66, 86], "lignes": lignes_v}}],
                "note": "k : coefficient de sécurité · flèche : de combien la tête du mât se déplace · mm : "
                        "millimètre · km/h : kilomètre par heure. " + NOTE_PROFILS,
            },
            "doc_retenus_reglage": {
                "titre": "Combien de profilés passent ?",
                "sous_titre": "Sous le vent de %d km/h. Passe : k ≥ %d et flèche ≤ %d mm, sur "
                              "%d profilés." % (M.VENT_REFERENCE, M.COEF_EXIGE, M.FLECHE_MAX, len(M.PROFILES)),
                "desc": "Le nombre de profilés qui passent, sur %d, sous le vent de %d kilomètres par heure, selon la "
                        "hauteur du mât et la limite choisie ; un profilé passe avec un coefficient d'au moins %d et "
                        "une flèche d'au plus %d millimètres. " % (len(M.PROFILES), M.VENT_REFERENCE, M.COEF_EXIGE,
                                                                    M.FLECHE_MAX)
                        + " ".join("Mât de %s : %s sur la rupture, %s sur la limite élastique."
                                   % (l[0].replace(" mm", " millimètres"), l[1], l[2]) for l in lignes_r),
                "blocs": [{"tableau": {"colonnes": ["Mât de", "Sur la rupture", "Sur l'élastique"],
                                       "largeurs": [100, 106, 116], "lignes": lignes_r}}],
                "note": "Sur la rupture : la limite où le mât casse. Sur l'élastique : la limite où il reste tordu. "
                        "mm : millimètre · km/h : kilomètre par heure.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        a_jour = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C8.1.json est à jour du modèle" if a_jour
              else "✘ documents_qcm_3e_C8.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if a_jour else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
