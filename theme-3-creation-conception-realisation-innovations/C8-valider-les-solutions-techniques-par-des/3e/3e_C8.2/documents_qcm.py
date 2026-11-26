# -*- coding: utf-8 -*-
"""Les documents du QCM de 3e_C8.2, écrits depuis le modèle `profils_3e_C8.2.py` (règles d'or n°233 et n°345, 26/11/2026).

Le QCM se lit sur des documents dessinés pour le téléphone (`_outils/document_qcm.py`). Leurs nombres ne sont pas
recopiés à la main : ce script les calcule avec le modèle des cinq candidats-mâts, puis écrit
`documents_qcm_3e_C8.2.json`.

    python3 documents_qcm.py             écrit le fichier de données
    python3 documents_qcm.py --verifier  dit s'il est à jour (0) ou non (1), sans rien écrire
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C8.2.json   (dessine les SVG)
"""
import importlib.util
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C8.2.json")

# le nom du modèle porte un point (`profils_3e_C8.2.py`) : on le charge par son chemin
_spec = importlib.util.spec_from_file_location("profils", os.path.join(ICI, "profils_3e_C8.2.py"))
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

COURT = {"Tube aluminium Ø50 × 3": "Tube alu Ø50", "Barre pleine acier Ø20": "Barre acier Ø20",
         "Tube PVC Ø50 × 3": "Tube PVC Ø50", "Poutre bois 40 × 40": "Poutre bois 40×40",
         "Tube acier galvanisé Ø33,7 × 2,6": "Tube acier Ø33,7"}
NOTE_PROFILS = ("Ø : diamètre, en millimètres · alu : aluminium · PVC : plastique rigide · tube acier : "
                "galvanisé contre la rouille.")


def v1(x):
    return ("%.1f" % x).replace(".", ",")


def mille(n):
    n = int(round(n))
    return ("%d" % n) if n < 1000 else ("%d %03d" % (n // 1000, n % 1000))


def en_lettres(t):
    t = t.replace("rupture ≥", "rupture d'au moins").replace("flèche ≤", "flèche d'au plus").replace("×", " sur ")
    return (t.replace(" kN", " kilonewtons").replace(" N", " newtons").replace(" mm", " millimètres")
            .replace("Ø", "diamètre ").replace("≥", "au moins").replace("≤", "au plus"))


def donnees():
    h = mille(P.L)
    lignes_essai = [[COURT[p.nom], "%d N" % p.flexion, "%s mm" % v1(p.fleche_essai)] for p in P.PROFILS]
    lignes_deux = [[COURT[p.nom], "%s kN" % v1(p.traction), "%d N" % p.flexion] for p in P.PROFILS]

    def dire(lignes, a, b):
        return " ".join("%s : %s %s, %s %s." % (l[0], a, l[1], b, l[2]) for l in lignes)

    proto = [
        {"titre": "Comment on charge",
         "lignes": ["Sollicitation : flexion, une poussée en tête du mât.",
                    "Toujours pareils : hauteur %s mm, fixation au pied, point de poussée." % h,
                    "Un profilé neuf à chaque essai."]},
        {"titre": "Ce qu'on mesure",
         "lignes": ["Charge d'essai : %d N pour chacun." % P.CHARGE_ESSAI,
                    "Mesure : flèche en tête, au millimètre."]},
        {"titre": "La règle de décision, écrite avant", "accent": True,
         "lignes": ["Retenu si : rupture d'au moins %d N et flèche d'au plus %d mm." % (P.EXIGE, P.FLECHE_MAX),
                    "Si un profilé casse avant la charge d'essai : ________"]},
    ]
    desc_proto = " ".join(c["titre"] + ". " + " ".join(c["lignes"]) for c in proto)
    desc_proto = en_lettres(desc_proto.replace(" : ________", " : la ligne est laissée vide."))

    return {
        "qcm": ["qcm_3e_C8.2_mat-de-la-station.html"],
        "documents": {
            "doc_releve_flexion": {
                "titre": "Le relevé du banc, en flexion",
                "sous_titre": "Mât de %s mm encastré au pied, poussé en tête. Exigé : rupture ≥ %d N, flèche ≤ %d mm "
                              "sous %d N." % (h, P.EXIGE, P.FLECHE_MAX, P.CHARGE_ESSAI),
                "desc": en_lettres("Le relevé du banc en flexion, pour un mât de %s mm encastré au pied et poussé en "
                                   "tête ; il faut une rupture d'au moins %d N et une flèche d'au plus %d mm sous "
                                   "une charge d'essai de %d N. " % (h, P.EXIGE, P.FLECHE_MAX, P.CHARGE_ESSAI)
                                   + dire(lignes_essai, "rupture à", "flèche de")),
                "blocs": [{"tableau": {"colonnes": ["Profilé", "Rupture", "Flèche"],
                                       "largeurs": [150, 72, 100], "lignes": lignes_essai}}],
                "note": "N : newton · mm : millimètre · flèche : de combien la tête du mât se déplace, sous %d N. "
                        % P.CHARGE_ESSAI + NOTE_PROFILS,
            },
            "doc_traction_flexion": {
                "titre": "Deux essais, les cinq mêmes mâts",
                "sous_titre": "La charge de rupture de chaque profilé : tiré dans son axe (traction), puis poussé en "
                              "tête (flexion).",
                "desc": en_lettres("La charge de rupture des cinq profilés, de %s mm de haut : tirés dans leur axe, "
                                   "en traction, puis poussés en tête, en flexion. " % h
                                   + dire(lignes_deux, "traction", "flexion")),
                "blocs": [{"tableau": {"colonnes": ["Profilé", "Traction", "Flexion"],
                                       "largeurs": [170, 76, 76], "lignes": lignes_deux}}],
                "note": "N : newton · kN : kilonewton, 1 000 N · " + NOTE_PROFILS,
            },
            "doc_protocole_groupe": {
                "titre": "Le protocole d'un groupe",
                "sous_titre": "Pour une poussée de %d N en tête du mât, avec un coefficient de sécurité de %d."
                              % (P.CHARGE_ESSAI, P.COEF),
                "desc": "Le protocole d'un groupe, pour une poussée de %d newtons en tête du mât, avec un "
                        "coefficient de sécurité de %d. " % (P.CHARGE_ESSAI, P.COEF) + desc_proto,
                "blocs": [{"fiches": proto}],
                "note": "N : newton · mm : millimètre · flèche : de combien la tête du mât se déplace.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        a_jour = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C8.2.json est à jour du modèle" if a_jour
              else "✘ documents_qcm_3e_C8.2.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if a_jour else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
