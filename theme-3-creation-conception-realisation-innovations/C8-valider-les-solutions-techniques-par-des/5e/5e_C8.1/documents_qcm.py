# -*- coding: utf-8 -*-
"""Les documents du QCM de 5e_C8.1, écrits depuis le modèle `patere.py` (règles d'or n°233 et n°345, 25/11/2026).

Le QCM se lit sur des documents dessinés pour le téléphone (`_outils/document_qcm.py`). Leurs nombres ne sont pas
recopiés à la main : ce script les calcule avec le modèle de la patère, puis écrit `documents_qcm_5e_C8.1.json`.

    python3 documents_qcm.py             écrit le fichier de données
    python3 documents_qcm.py --verifier  dit s'il est à jour (0) ou non (1), sans rien écrire
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C8.1.json   (dessine les SVG)
"""
import json
import os
import sys

import patere as P

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_5e_C8.1.json")
COURT = {"Bois (pin)": "Bois (pin)", "PLA imprimé en 3D": "PLA", "PVC rigide": "PVC",
         "Aluminium": "Aluminium", "Acier doux": "Acier doux"}


def v1(x):
    """Un nombre à une décimale, écrit à la française."""
    return ("%.1f" % x).replace(".", ",")


def kg(x):
    return "%d kg" % round(x)


def donnees():
    service = P.MATERIAUX[0].contrainte(P.CHARGE_SERVICE)
    lignes_k = [[COURT[m.nom], v1(m.sigma_r / service), v1(m.coefficient())] for m in P.MATERIAUX]
    lignes_pc = [[COURT[m.nom], kg(m.charge_deforme), kg(m.charge_casse)] for m in P.MATERIAUX]
    retenus = [m for m in P.MATERIAUX if m.retenu]
    lignes_cd = [[COURT[m.nom], v1(m.coefficient()), "%d €" % round(m.cout_total),
                  (v1(m.heures_total) if m.heures_total % 1 else "%d" % m.heures_total) + " h"] for m in retenus]

    def dire(lignes, a, b):
        return " ".join("%s : %s %s, %s %s." % (l[0], a, l[1], b, l[2]) for l in lignes)

    plastiques = "PLA : plastique des imprimantes 3D (trois dimensions) · PVC : plastique rigide, celui des tuyaux."
    return {
        "qcm": ["qcm_5e_C8.1_patere-du-hall.html"],
        "documents": {
            "doc_deux_coefficients": {
                "titre": "Le coefficient de sécurité du crochet",
                "sous_titre": "Sous %d kg, la charge de service. Le gestionnaire exige %d au moins." % (
                    P.CHARGE_SERVICE, P.COEF_EXIGE),
                "desc": "Le coefficient de sécurité du crochet, sous %d kilogrammes ; le gestionnaire exige %d au moins. "
                        "Pour chaque matériau, calculé sur la rupture, puis sur la limite élastique. " % (
                            P.CHARGE_SERVICE, P.COEF_EXIGE) + dire(lignes_k, "sur la rupture", "sur l'élastique"),
                "blocs": [{"tableau": {"colonnes": ["Matériau", "Sur la rupture", "Sur l'élastique"],
                                       "largeurs": [100, 106, 116], "lignes": lignes_k}}],
                "note": "Sur la rupture : la limite où le crochet casse. Sur l'élastique : la limite où il plie pour "
                        "toujours. " + plastiques,
            },
            "doc_plie_casse": {
                "titre": "Quand le crochet plie, quand il casse",
                "sous_titre": "Plie à : il reste tordu, calculé par la simulation. Casse à : relevé au banc d'essai.",
                "desc": "Pour chaque matériau du crochet, la charge à partir de laquelle il plie pour toujours, calculée "
                        "par la simulation, et la charge à laquelle il casse, relevée au banc d'essai. "
                        + dire(lignes_pc, "plie à", "casse à").replace(" kg", " kilogrammes"),
                "blocs": [{"tableau": {"colonnes": ["Matériau", "Plie à", "Casse à"],
                                       "largeurs": [130, 96, 96], "lignes": lignes_pc}}],
                "note": "kg : kilogramme. " + plastiques,
            },
            "doc_cout_delai": {
                "titre": "Les %d patères : marge, coût, délai" % P.NOMBRE,
                "sous_titre": "Les quatre matériaux qui tiennent (k\u00a0≥\u00a0%d). L'atelier dispose de 8 heures." % P.COEF_EXIGE,
                "desc": "Les quatre matériaux qui tiennent, pour %d patères ; l'atelier dispose de 8 heures. " % P.NOMBRE
                        + " ".join("%s : coefficient %s, coût %s, %s d'atelier." % (l[0], l[1], l[2].replace("€", "euros"),
                                   l[3].replace(" h", " heures")) for l in lignes_cd),
                "blocs": [{"tableau": {"colonnes": ["Matériau", "k", "Coût", "Atelier"],
                                       "largeurs": [110, 62, 80, 70], "lignes": lignes_cd}}],
                "note": "k : coefficient de sécurité, sur la limite élastique · € : euro · h : heure · "
                        "Acier : galvanisé contre la rouille, compris dans le coût. " + plastiques,
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        a_jour = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C8.1.json est à jour du modèle" if a_jour
              else "✘ documents_qcm_5e_C8.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if a_jour else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
