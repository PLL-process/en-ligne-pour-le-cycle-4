# -*- coding: utf-8 -*-
"""Le document du QCM de 3e_C7.7, calculé par le modèle du lot (règles d'or n°233 et n°345, 27/11/2026).

Aucun nombre n'est recopié : tout vient de `moyens.py` (les cinq traits du dessin du boîtier, et ce que tient
l'imprimante 3D : paroi étanche, surplomb, détail dans l'épaisseur, tolérance, angles internes). Un nombre changé dans
le modèle change le document du QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_3e_C7.7.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C7.7.json
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import moyens as M  # noqa: E402

SORTIE = os.path.join(ICI, "documents_qcm_3e_C7.7.json")
PIECE, MOYEN = "boitier", "impression"
NOM = {"epaisseur": "Paroi étanche", "surplomb": "Casquette", "res_z": "Rainure du joint",
       "tol": "Jeu couvercle", "r_int": "Angles internes"}


def mm(x):
    return M.vg(x, 2).rstrip("0").rstrip(",") + " mm"


def donnees():
    p, m = M.PIECES[PIECE], M.MOYENS[MOYEN]
    traits = {c: v for c, _, v, _ in p["traits"]}
    dessin = {"epaisseur": mm(traits["epaisseur"]), "surplomb": "%d°" % traits["surplomb"],
              "res_z": mm(traits["res_z"]), "tol": mm(traits["tol"]),
              "r_int": "vifs" if traits["r_int"] == 0 else mm(traits["r_int"])}
    machine = {"epaisseur": mm(m["e_etanche"]) + " min.", "surplomb": "%d° max." % m["surplomb"],
               "res_z": mm(m["res_z"]) + " min.", "tol": "± " + mm(m["tol"]),
               "r_int": "vifs" if m["r_int"] == 0 else mm(m["r_int"])}
    dit = {"epaisseur": "au moins %s millimètre" % M.vg(m["e_etanche"], 1),
           "surplomb": "au plus %d degrés" % m["surplomb"],
           "res_z": "au moins %s millimètre" % M.vg(m["res_z"], 1),
           "tol": "à %s millimètre près" % M.vg(m["tol"], 1), "r_int": "des angles vifs"}
    vu = {"epaisseur": "%s millimètres" % M.vg(traits["epaisseur"], 1), "surplomb": "%d degrés" % traits["surplomb"],
          "res_z": "%s millimètre" % M.vg(traits["res_z"], 1), "tol": "%s millimètre" % M.vg(traits["tol"], 1),
          "r_int": "des angles vifs"}
    lignes = [[NOM[c], dessin[c], machine[c]] for c in NOM]
    dire = " ".join("%s : dessin, %s ; l'imprimante tient %s." % (NOM[c], vu[c], dit[c]) for c in NOM)
    return {
        "qcm": ["qcm_3e_C7.7_produire-le-boitier.html"],
        "documents": {
            "doc_dessin_boitier": {
                "titre": "Le dessin du boîtier, face à l'imprimante",
                "sous_titre": "Cinq cotes du dessin, et ce que tient l'imprimante 3D en PETG.",
                "desc": "Le dessin du boîtier de la station, en PETG, face à ce que tient l'imprimante 3D (buse de 0,4 "
                        "millimètre, couches de 0,2 millimètre). " + dire,
                "blocs": [{"tableau": {"colonnes": ["Cote", "Dessin", "Imprimante"],
                                       "largeurs": [126, 80, 116], "lignes": lignes}}],
                "note": "min. : au moins · max. : au plus · ± : à … près · mm : millimètre · ° : degré, l'inclinaison par rapport à la verticale · l'imprimante dépose "
                        "des couches de 0,2 mm avec une buse de 0,4 mm · au-delà de son surplomb, il lui faut un "
                        "support · PETG : un plastique d'impression.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C7.7.json est à jour du modèle" if ok
              else "✘ documents_qcm_3e_C7.7.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
