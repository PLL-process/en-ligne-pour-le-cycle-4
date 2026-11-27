# -*- coding: utf-8 -*-
"""Les documents du QCM de 3e_C7.8, lus dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : le banc de la séquence porte ses données dans la page (`const CHAMPS` : chaque
champ qu'un message d'une station pourrait porter, avec ce qu'il dit et une valeur d'exemple), et l'activité 4 énonce
les six essais de la recette. Ce script les y LIT. Le premier document montre tous les champs possibles, sans dire
lesquels envoyer ; le second, les six essais, sans dire ce que chacun prouve : c'est ce que les questions font trouver.

    python3 documents_qcm.py             écrit documents_qcm_3e_C7.8.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C7.8.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C7.8.json")
SEQ = open(os.path.join(ICI, "sequence_3e_C7.8_deux-stations.html"), encoding="utf-8").read()
_l = re.search(r"^const CHAMPS = (.*)$", SEQ, re.M).group(1)
CHAMPS, _ = json.JSONDecoder().raw_decode(_l[_l.index("["):])
assert [c["cle"] for c in CHAMPS][:6] == ["id", "v", "u", "t", "niv", "seq"], CHAMPS
_i = SEQ.index("Activité 4 — Écrire les essais")
_t = SEQ[_i:SEQ.index("</section>", _i)]
ESSAIS = [html.unescape(re.sub("<[^>]+>", "", m)).strip() for m in re.findall(
    r'<fieldset class="qcm-groupe qcm-grille" id="a4c\d"[^>]*>\s*<legend[^>]*>(.*?)</legend>', _t, re.S)]
assert len(ESSAIS) == 6, ESSAIS


def ecrit(v):
    return {False: "false", True: "true"}.get(v, str(v)) if isinstance(v, bool) else str(v)


def donnees():
    dits = ["%s : %s." % (c["cle"], c["lib"]) for c in CHAMPS]
    return {
        "qcm": ["qcm_3e_C7.8_deux-stations.html"],
        "documents": {
            "doc_message_station": {
                "titre": "Ce qu'une station pourrait envoyer",
                "sous_titre": "Les %d champs possibles d'un message, avec une valeur d'exemple." % len(CHAMPS),
                "desc": "Les %d champs qu'un message d'une station d'alerte pourrait porter, chacun avec une valeur "
                        "d'exemple et ce qu'il dit. " % len(CHAMPS)
                        + " ".join("%s, exemple %s : %s." % (c["cle"], ecrit(c["val"]), c["lib"]) for c in CHAMPS),
                "blocs": [
                    {"tableau": {"colonnes": ["Champ", "Exemple"], "largeurs": [96, 226],
                                 "lignes": [[c["cle"], ecrit(c["val"])] for c in CHAMPS]}},
                    {"fiches": [{"titre": "Ce que dit chaque champ", "lignes": dits}]},
                ],
                "note": "Le document ne dit pas lesquels envoyer : c'est la question · km/h : kilomètre par heure.",
            },
            "doc_essais_station": {
                "titre": "Les six essais de la recette",
                "sous_titre": "Deux stations, Le Robert et Sainte-Anne, et la règle : alerte si les deux annoncent "
                              "au moins le niveau 2.",
                "desc": "Les six essais de la recette de la liaison entre les stations du Robert et de Sainte-Anne. "
                        + " ".join("Essai %d : %s." % (k + 1, e) for k, e in enumerate(ESSAIS)),
                "blocs": [{"fiches": [{"titre": "Essai %d" % (k + 1), "lignes": [e + "."]}
                                      for k, e in enumerate(ESSAIS)]}],
                "note": "Le document ne dit pas ce que prouve chaque essai : c'est la question · km/h : kilomètre par "
                        "heure.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C7.8.json est à jour de la séquence" if ok
              else "✘ documents_qcm_3e_C7.8.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
