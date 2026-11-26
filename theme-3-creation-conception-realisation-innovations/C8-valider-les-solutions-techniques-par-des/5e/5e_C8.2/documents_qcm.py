# -*- coding: utf-8 -*-
"""Les documents du QCM de 5e_C8.2, écrits depuis le modèle de la patère (règles d'or n°233 et n°345, 25/11/2026).

Le QCM se lit sur des documents dessinés pour le téléphone (`_outils/document_qcm.py`). Les charges de rupture du banc
ne sont pas recopiées à la main : elles viennent de `../5e_C8.1/patere.py`, le modèle qui les calcule (σ_r × 10 mm² ÷ g,
la section des éprouvettes du banc). L'exigence du gestionnaire est celle de la séquence : un sac de 8 kg, un
coefficient de 5, soit 40 kg. Ce que l'essai ne voit pas reprend la correction de l'activité 4.

    python3 documents_qcm.py             écrit documents_qcm_5e_C8.2.json
    python3 documents_qcm.py --verifier  dit s'il est à jour (0) ou non (1), sans rien écrire
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C8.2.json   (dessine les SVG)
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "5e_C8.1"))
import patere as P  # noqa: E402

SORTIE = os.path.join(ICI, "documents_qcm_5e_C8.2.json")
SAC, COEF = 8, 5                 #: le cahier des charges de la séquence 5e_C8.2 : un sac de 8 kg, un coefficient de 5
EXIGE = SAC * COEF               #: 40 kg
SECTION = 10                     #: mm², la section des éprouvettes du banc
ANGLE_MORT = {                   #: ce que l'essai de traction ne voit pas (correction de l'activité 4)
    "Bois (pin)": "Un nœud dans la pièce, et il casse bien plus tôt.",
    "PLA imprimé en 3D": "En travers des couches, il se déchire à moins de la moitié.",
    "PVC rigide": "Il flue : sous une charge permanente, il se déforme lentement.",
    "Aluminium": "Léger et solide ; il se raye, et plie avant de casser.",
    "Acier doux": "En bord de mer, sans protection, il rouille.",
}
PLASTIQUES = "PLA : plastique des imprimantes 3D (trois dimensions) · PVC : plastique rigide, celui des tuyaux."


def kg(x):
    return "%d kg" % round(x)


def donnees():
    alu = P.PAR_NOM["Aluminium"]
    lignes = [[m.nom, kg(m.charge_casse)] for m in P.MATERIAUX]
    return {
        "qcm": ["qcm_5e_C8.2_patere-du-hall.html"],
        "documents": {
            "doc_releve_banc": {
                "titre": "Le relevé du banc d'essai",
                "sous_titre": "Essai de traction, une éprouvette neuve de %d mm² par matériau. Valeurs simulées." % SECTION,
                "desc": "Le relevé du banc d'essai : essai de traction, une éprouvette neuve de %d millimètres carrés par "
                        "matériau, valeurs simulées. Exigé : %d kilogrammes, un sac de %d kilogrammes avec un coefficient "
                        "de %d. Charge de rupture : " % (SECTION, EXIGE, SAC, COEF)
                        + " ; ".join("%s, %s" % (l[0], l[1].replace(" kg", " kilogrammes")) for l in lignes) + ".",
                "blocs": [
                    {"fiches": [{"titre": "Ce qu'exige le gestionnaire", "accent": True,
                                 "lignes": ["Un sac de %d kg, un coefficient de %d : la patère doit tenir %d kg." % (
                                     SAC, COEF, EXIGE)]}]},
                    {"tableau": {"colonnes": ["Matériau", "Casse à"], "largeurs": [200, 122], "lignes": lignes}},
                ],
                "note": "kg : kilogramme · mm² : millimètre carré. " + PLASTIQUES,
            },
            "doc_fiche_essai": {
                "titre": "La fiche d'essai de l'aluminium",
                "sous_titre": "Ce que l'élève a noté au banc, avec sa mesure.",
                "desc": "La fiche d'essai de l'aluminium. Essai de traction : on tire dans l'axe de l'éprouvette. "
                        "Éprouvette neuve, de %d millimètres carrés de section, la même pour les cinq matériaux. Charge "
                        "ajoutée par paliers, jusqu'à la rupture. Rupture à %s. Valeurs simulées." % (
                            SECTION, kg(alu.charge_casse).replace(" kg", " kilogrammes")),
                "blocs": [{"fiches": [
                    {"titre": "Comment l'essai a été fait",
                     "lignes": ["Essai de traction : on tire dans l'axe de l'éprouvette.",
                                "Éprouvette neuve, de %d mm² de section, la même pour les cinq matériaux." % SECTION,
                                "Charge ajoutée par paliers, jusqu'à la rupture."]},
                    {"titre": "Ce qui a été relevé", "paires": [["Rupture à", kg(alu.charge_casse)],
                                                                ["Valeurs", "simulées"]]},
                ]}],
                "note": "kg : kilogramme · mm² : millimètre carré.",
            },
            "doc_angles_morts": {
                "titre": "Ce que l'essai de traction ne voit pas",
                "sous_titre": "Les cinq matériaux tiennent au banc. Le hall, lui, a ses contraintes.",
                "desc": "Le hall du collège : l'air de la Martinique est salé ; les sacs y arrivent trempés par l'averse "
                        "de midi ; exigé %d kilogrammes. Pour chaque matériau, sa charge de rupture au banc et ce que "
                        "l'essai de traction ne voit pas. " % EXIGE
                        + " ".join("%s, %s : %s" % (m.nom, kg(m.charge_casse).replace(" kg", " kilogrammes"),
                                                     ANGLE_MORT[m.nom]) for m in P.MATERIAUX),
                "blocs": [{"fiches": [{"titre": "Le hall du collège", "accent": True,
                                       "lignes": ["L'air de la Martinique est salé.",
                                                  "Les sacs y arrivent trempés par l'averse de midi.",
                                                  "Exigé : %d kg." % EXIGE]}]
                           + [{"titre": "%s · %s" % (m.nom, kg(m.charge_casse)), "lignes": [ANGLE_MORT[m.nom]]}
                              for m in P.MATERIAUX]}],
                "note": "kg : kilogramme. PLA, PVC : deux plastiques.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        a_jour = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C8.2.json est à jour du modèle" if a_jour
              else "✘ documents_qcm_5e_C8.2.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if a_jour else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
