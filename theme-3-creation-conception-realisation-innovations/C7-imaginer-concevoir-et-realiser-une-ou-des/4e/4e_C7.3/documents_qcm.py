# -*- coding: utf-8 -*-
"""Les documents du QCM de 4e_C7.3, calculés par le modèle du lot (règles d'or n°233 et n°345, 27/11/2026).

Aucun nombre n'est recopié : tout vient de `materiaux.py` (les six matériaux candidats, les six exigences du bac, la
masse, le prix et le coût sur quinze ans calculés). Un nombre changé dans le modèle change le document du QCM — et
`--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_4e_C7.3.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C7.3.json
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import materiaux as M  # noqa: E402

SORTIE = os.path.join(ICI, "documents_qcm_4e_C7.3.json")
OBJ = "bac"
DUREE = 15                     # la durée de comparaison de la séquence
COURT = {"pin": "Pin nu", "pin_autoclave": "Pin traité", "pvc": "PVC", "pp_recycle": "PP recyclé",
         "acier_galva": "Acier galva.", "teck": "Teck"}
LONG = {"pin": "le pin non traité", "pin_autoclave": "le pin traité autoclave", "pvc": "le PVC",
        "pp_recycle": "le polypropylène recyclé", "acier_galva": "l'acier galvanisé", "teck": "le teck"}


def eur(x):
    return M.vg(x, 2) + " €"


def maj(t):
    return t[0].upper() + t[1:]


def donnees():
    ex = M.OBJETS[OBJ]["exigences"]
    t = M.table(OBJ, M.CANDIDATS[OBJ])
    val = lambda l, c: l["valeurs"][c]
    tenue = [[COURT[l["cle"]], "%d MPa" % val(l, "sigma"), "%d ans" % val(l, "uv"), "%d / 5" % val(l, "sel")]
             for l in t]
    suite = [[COURT[l["cle"]], "%d / 5" % val(l, "eau"), "%d %%" % val(l, "recyc"), M.vg(l["masse"], 1) + " kg"]
             for l in t]
    retenus = [l for l in t if l["retenu"]]
    cout = []
    for l in retenus:
        total, n = M.cout_sur(l["cle"], OBJ, DUREE)
        cout.append([COURT[l["cle"]], "%d ans" % val(l, "uv"), eur(l["cout"]), eur(total)])
    dire_t = " ".join(
        "%s : %d mégapascals, %d ans au soleil, %d sur 5 au sel, %d sur 5 à l'eau, %d pour cent recyclable, %s "
        "kilogrammes." % (maj(LONG[l["cle"]]), val(l, "sigma"), val(l, "uv"), val(l, "sel"), val(l, "eau"),
                          val(l, "recyc"), M.vg(l["masse"], 1)) for l in t)
    dire_c = " ".join(
        "%s : il dure %d ans, un bac coûte %s euros, et %s euros sur %d ans." % (
            maj(LONG[l["cle"]]), val(l, "uv"), M.vg(l["cout"], 2), M.vg(M.cout_sur(l["cle"], OBJ, DUREE)[0], 2), DUREE)
        for l in retenus)
    exigences = [["Résistance", "au moins %d MPa" % ex["sigma"]], ["Soleil", "au moins %d ans" % ex["uv"]],
                 ["Sel", "au moins %d / 5" % ex["sel"]], ["Eau", "au moins %d / 5" % ex["eau"]],
                 ["Recyclable", "au moins %d %%" % ex["recyc"]], ["Masse", "au plus %d kg" % ex["masse_max"]]]
    return {
        "qcm": ["qcm_4e_C7.3_bac-du-jardin.html"],
        "documents": {
            "doc_criteres_bac": {
                "titre": "Six matériaux pour le bac du jardin",
                "sous_titre": "Le cahier des charges du bac, puis ce que tient chaque matériau.",
                "desc": "Le cahier des charges du bac du jardin : résistance d'au moins %d mégapascals, au moins %d ans "
                        "au soleil, au moins %d sur 5 au sel, au moins %d sur 5 à l'eau, au moins %d pour cent "
                        "recyclable, au plus %d kilogrammes. Puis les six matériaux. %s"
                        % (ex["sigma"], ex["uv"], ex["sel"], ex["eau"], ex["recyc"], ex["masse_max"], dire_t),
                "blocs": [
                    {"fiches": [{"titre": "Ce que le bac exige", "accent": True, "paires": exigences}]},
                    {"intertitre": "Ce que tient chaque matériau"},
                    {"tableau": {"colonnes": ["Matériau", "Résistance", "Soleil", "Sel"],
                                 "largeurs": [100, 82, 70, 70], "lignes": tenue}},
                    {"intertitre": "À l'eau, en fin de vie, sur la balance"},
                    {"tableau": {"colonnes": ["Matériau", "Eau", "Recyclable", "Masse"],
                                 "largeurs": [100, 62, 80, 80], "lignes": suite}},
                ],
                "note": "PP : polypropylène · MPa : mégapascal (résistance) · Soleil : années avant de griser ou de fendre · Sel, Eau : "
                        "tenue de 1 à 5 · Recyclable : part de la matière qu'on sait recycler · kg : kilogramme, masse "
                        "du bac.",
            },
            "doc_cout_bac": {
                "titre": "Les trois retenus, sur %d ans" % DUREE,
                "sous_titre": "Combien dure chaque bac, son prix, et ce qu'il coûte sur %d ans." % DUREE,
                "desc": "Les trois matériaux retenus pour le bac, leur durée de vie, le prix d'un bac et le coût sur "
                        "%d ans, remplacements compris. %s" % (DUREE, dire_c),
                "blocs": [{"tableau": {"colonnes": ["Matériau", "Durée", "Un bac", "%d ans" % DUREE],
                                       "largeurs": [96, 64, 80, 82], "lignes": cout}}],
                "note": "PP : polypropylène · Durée : années avant qu'il faille le remplacer · %d ans : prix d'un bac × nombre de bacs "
                        "achetés pour couvrir %d ans." % (DUREE, DUREE),
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C7.3.json est à jour du modèle" if ok
              else "✘ documents_qcm_4e_C7.3.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
