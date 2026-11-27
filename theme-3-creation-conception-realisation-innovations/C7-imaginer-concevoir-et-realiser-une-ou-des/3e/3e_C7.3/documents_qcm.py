# -*- coding: utf-8 -*-
"""Le document du QCM de 3e_C7.3, calculé par le modèle du lot (règles d'or n°233 et n°345, 27/11/2026).

Aucun nombre n'est recopié : tout vient de `materiaux.py` (les six matériaux candidats, les cinq exigences du boîtier,
l'épaisseur de paroi et la masse calculées pour chacun). Un nombre changé dans le modèle change le document du QCM — et
`--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_3e_C7.3.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C7.3.json
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import materiaux as M  # noqa: E402

SORTIE = os.path.join(ICI, "documents_qcm_3e_C7.3.json")
OBJ = "boitier"
COURT = {"pla": "PLA", "petg": "PETG", "pvc": "PVC", "alu": "Aluminium", "inox": "Inox 316", "pp_recycle": "PP recyclé"}
LONG = {"pla": "le PLA", "petg": "le PETG", "pvc": "le PVC", "alu": "l'aluminium anodisé", "inox": "l'inox 316",
        "pp_recycle": "le polypropylène recyclé"}


def maj(t):
    return t[0].upper() + t[1:]


def donnees():
    ex = M.OBJETS[OBJ]["exigences"]
    cles = M.CANDIDATS[OBJ]
    mat = M.MATERIAUX
    ep = {k: M.epaisseur(k, OBJ) * 1000 for k in cles}
    ms = {k: M.masse(k, OBJ) for k in cles}
    tenue = [[COURT[k], "%d MPa" % mat[k]["sigma"], ("%d an" if mat[k]["uv"] == 1 else "%d ans") % mat[k]["uv"], "%d / 5" % mat[k]["sel"]] for k in cles]
    forme = [[COURT[k], M.vg(ep[k], 2) + " mm", "%d °C" % mat[k]["chaud"], M.vg(ms[k], 3) + " kg"] for k in cles]
    dire = " ".join("%s : %d mégapascals, %d an(s) au soleil, %d sur 5 au sel, paroi de %s millimètres, %d degrés au "
                    "soleil, %s kilogramme." % (maj(LONG[k]), mat[k]["sigma"], mat[k]["uv"], mat[k]["sel"],
                                                M.vg(ep[k], 2), mat[k]["chaud"], M.vg(ms[k], 3)) for k in cles)
    exige = [["Résistance", "au moins %d MPa" % ex["sigma"]], ["Soleil", "au moins %d ans" % ex["uv"]],
             ["Sel", "au moins %d / 5" % ex["sel"]], ["Chaleur", "au plus %d °C" % ex["chaud"]],
             ["Masse", "au plus %s kg" % M.vg(ex["masse_max"], 1)]]
    return {
        "qcm": ["qcm_3e_C7.3_boitier-de-la-station.html"],
        "documents": {
            "doc_criteres_boitier": {
                "titre": "Six matériaux pour le boîtier",
                "sous_titre": "Le cahier des charges du boîtier, puis ce que donne chaque matériau.",
                "desc": "Le cahier des charges du boîtier de la station d'alerte : résistance d'au moins %d mégapascals, "
                        "au moins %d ans au soleil, %d sur 5 au sel, au plus %d degrés au soleil, au plus %s "
                        "kilogramme. Puis les six matériaux candidats, avec l'épaisseur de paroi que demande chacun et "
                        "la masse du boîtier qui en résulte. %s"
                        % (ex["sigma"], ex["uv"], ex["sel"], ex["chaud"], M.vg(ex["masse_max"], 1), dire),
                "blocs": [
                    {"fiches": [{"titre": "Ce que le boîtier exige", "accent": True, "paires": exige}]},
                    {"intertitre": "Ce que tient chaque matériau"},
                    {"tableau": {"colonnes": ["Matériau", "Résistance", "Soleil", "Sel"],
                                 "largeurs": [100, 82, 70, 70], "lignes": tenue}},
                    {"intertitre": "Sa paroi, sa chaleur, sa masse"},
                    {"tableau": {"colonnes": ["Matériau", "Paroi", "Chaleur", "Masse"],
                                 "largeurs": [100, 74, 66, 82], "lignes": forme}},
                ],
                "note": "MPa : mégapascal (résistance) · Soleil : années avant de se dégrader · Sel : tenue à l'air "
                        "marin, de 1 à 5 · Paroi : épaisseur calculée pour la même rigidité · Chaleur : température "
                        "du boîtier au soleil · kg : kilogramme · PLA, PETG, PVC, PP : des plastiques.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C7.3.json est à jour du modèle" if ok
              else "✘ documents_qcm_3e_C7.3.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
