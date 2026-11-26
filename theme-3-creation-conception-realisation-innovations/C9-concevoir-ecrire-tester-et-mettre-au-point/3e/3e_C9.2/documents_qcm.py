# -*- coding: utf-8 -*-
"""Les documents du QCM de 3e_C9.2-C8.3, écrits depuis le programme de la station (règles d'or n°233 et n°345, 26/11/2026).

Le QCM se lit sur des documents dessinés pour le téléphone (`_outils/document_qcm.py`). Leurs nombres ne sont pas
recopiés à la main : les seuils, le format de la trace et les quatre niveaux viennent de
`station_alerte_cyclonique/station_alerte_cyclonique.ino`, et les deux programmes fautifs (la trace, la recette d'un
groupe) sont la même décision, avec UNE erreur chacun, écrite ci-dessous.

    python3 documents_qcm.py             écrit le fichier de données
    python3 documents_qcm.py --verifier  dit s'il est à jour (0) ou non (1), sans rien écrire
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C9.2.json   (dessine les SVG)
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C9.2.json")
INO = open(os.path.join(ICI, "station_alerte_cyclonique", "station_alerte_cyclonique.ino"), encoding="utf-8").read()

SEUIL = {m.group(1): int(m.group(2)) for m in re.finditer(r"const int SEUIL_(\w+)\s*=\s*(\d+);", INO)}
J, O, R = SEUIL["JAUNE"], SEUIL["ORANGE"], SEUIL["ROUGE"]
assert (J, O, R) == (63, 118, 178), SEUIL
# le format de la trace, tel que le programme l'écrit sur le moniteur série
assert 'Serial.print("vent(km/h)=");' in INO and 'Serial.print(" niveau=");' in INO
NOMS = ["veille", "tempête tropicale", "ouragan", "ouragan majeur"]


def niveau(v):
    """La décision du programme : le seuil le plus haut d'abord, « à partir de » = compris (≥)."""
    return 3 if v >= R else 2 if v >= O else 1 if v >= J else 0


def niveau_sans_jaune(v):
    """Le programme de la trace : le test « ≥ 63 » a été oublié (le bloc n'est pas branché)."""
    return 3 if v >= R else 2 if v >= O else 0


def niveau_strict_orange(v):
    """Le programme d'un groupe : « > 118 » au lieu de « ≥ 118 »."""
    return 3 if v >= R else 2 if v > O else 1 if v >= J else 0


TRACE = [71, 95, 131]
RECETTE = [40, 90, 150, 200, J - 1, J, O - 1, O, R - 1, R]


def donnees():
    trace = ["vent(km/h)=%d niveau=%d" % (v, niveau_sans_jaune(v)) for v in TRACE]
    lignes_r = [[str(i), "%d km/h" % v, "niveau %d" % niveau(v), "niveau %d" % niveau_strict_orange(v)]
                for i, v in enumerate(RECETTE, 1)]
    lignes_r += [["11", "chrono", "< 1 s", "0,4 s"],
                 ["12", "appui en alarme", "son coupé", "son coupé"],
                 ["13", "nouvelle alerte", "son repart", "son repart"]]
    legende = " · ".join(("%d : %s" % (i, n)).replace(" ", "\u00a0") for i, n in enumerate(NOMS))
    dire_r = " ".join("Essai %s, %s : attendu %s, observé %s." % tuple(l) for l in lignes_r)
    dire_r = (dire_r.replace("km/h", "kilomètres par heure").replace("< 1 s", "moins d'une seconde")
              .replace("0,4 s", "0,4 seconde"))
    return {
        "qcm": ["qcm_3e_C9.2-C8.3_station_alerte_cyclonique.html"],
        "documents": {
            "doc_trace_moniteur": {
                "titre": "La trace du moniteur série",
                "sous_titre": "Le potentiomètre tourne lentement : trois lignes écrites par la station.",
                "desc": "La trace du moniteur série, trois lignes écrites par la station pendant que le potentiomètre "
                        "tourne : " + " ; ".join(t.replace("vent(km/h)=", "vent ").replace(" niveau=",
                                                 " kilomètres par heure, niveau ") for t in trace)
                        + ". Le cahier des charges : niveau 0 veille en dessous de %d kilomètres par heure, niveau 1 "
                          "tempête tropicale à partir de %d, niveau 2 ouragan à partir de %d, niveau 3 ouragan majeur "
                          "à partir de %d." % (J, J, O, R),
                "blocs": [{"fiches": [
                    {"titre": "Ce qu'affiche le moniteur", "lignes": trace},
                    {"titre": "Ce que veut le cahier des charges", "accent": True,
                     "lignes": ["niveau 0 : veille, sous %d km/h" % J,
                                "niveau 1 : tempête tropicale, dès %d km/h" % J,
                                "niveau 2 : ouragan, dès %d km/h" % O,
                                "niveau 3 : ouragan majeur, dès %d km/h" % R]},
                ]}],
                "note": "km/h : kilomètre par heure · moniteur série : la fenêtre où le programme écrit ce qu'il "
                        "mesure, et le niveau qu'il choisit.",
            },
            "doc_courrier_exigences": {
                "titre": "Le courrier de la mairie",
                "sous_titre": "Ce que le prototype de station d'alerte doit faire, exigence par exigence.",
                "desc": "Le courrier de la mairie, exigence par exigence. Afficher en permanence le niveau et la "
                        "vitesse : veille en dessous de %d kilomètres par heure, tempête tropicale à partir de %d, "
                        "ouragan à partir de %d, ouragan majeur à partir de %d. Un seul voyant allumé à la fois. "
                        "Une alarme sonore en ouragan majeur seulement. Acquitter l'alarme d'un appui sur un bouton, "
                        "sans éteindre l'affichage ni le voyant. Réagir à un changement de vent en moins d'une "
                        "seconde." % (J, J, O, R),
                "blocs": [{"fiches": [
                    {"titre": "Afficher le niveau",
                     "lignes": ["Veille en dessous de %d km/h." % J,
                                "Tempête tropicale à partir de %d km/h." % J,
                                "Ouragan à partir de %d km/h." % O,
                                "Ouragan majeur à partir de %d km/h." % R]},
                    {"titre": "Alerter",
                     "lignes": ["Un seul voyant allumé à la fois.",
                                "Le son : en ouragan majeur seulement.",
                                "Un appui coupe le son, jamais l'affichage."]},
                    {"titre": "Réagir à un changement de vent", "accent": True,
                     "lignes": ["En moins d'une seconde."]},
                ]}],
                "note": "km/h : kilomètre par heure · acquitter : faire taire l'alarme en montrant qu'on l'a "
                        "entendue.",
            },
            "doc_recette_groupe": {
                "titre": "La recette d'un groupe",
                "sous_titre": "Les treize essais du protocole, au banc : l'attendu écrit avant, l'observé pendant.",
                "desc": "La recette d'un groupe, treize essais au banc, avec pour chacun l'attendu écrit avant et "
                        "l'observé pendant l'essai. Niveaux : " + legende + ". " + dire_r,
                "blocs": [{"tableau": {"colonnes": ["N°", "Entrée", "Attendu", "Observé"],
                                       "largeurs": [30, 126, 83, 83], "lignes": lignes_r}}],
                "note": "Niveau " + legende + " · km/h : kilomètre par heure · s : seconde.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        a_jour = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C9.2.json est à jour du programme" if a_jour
              else "✘ documents_qcm_3e_C9.2.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if a_jour else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
