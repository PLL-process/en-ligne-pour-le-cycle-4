# -*- coding: utf-8 -*-
"""Les documents du QCM de 4e_C7.1, lus dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : ses données sont celles de la page. Ce script les y LIT — les quatre tâches du
planning de l'activité 1b (nom et durée), et le tableau des matériaux de l'activité 3 (la réponse attendue de chaque
case, celle qui n'a pas de « pourquoi » d'erreur). Une durée ou une case changée dans la séquence change le document du
QCM — et `--verifier` le dit.

    python3 documents_qcm.py             écrit documents_qcm_4e_C7.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C7.1.json
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C7.1.json")
SEQ = open(os.path.join(ICI, "sequence_4e_C7_jardin-conception.html"), encoding="utf-8").read()

# le planning de l'activité 1b : numéro, nom de la tâche (placeholder), durée en minutes
PLANNING = [(int(n), nom, int(m)) for n, nom, m in re.findall(
    r'<tr><td>(\d)</td><td><input id="a1t\d" placeholder="([^"]+)"[^>]*></td><td>(\d+)</td></tr>', SEQ)]
assert [p[0] for p in PLANNING] == [1, 2, 3, 4], PLANNING
NOMS = {"Besoin": "Formuler le besoin du jardinier", "2 solutions": "Dessiner deux supports",
        "Matériau": "Comparer les matériaux", "Prototype": "Fabriquer le prototype"}
DESORDRE = [4, 1, 3, 2]      # l'ordre où la liste est donnée : l'organiser, c'est le travail demandé

# le tableau de l'activité 3 : pour chaque matériau, la réponse attendue de chaque colonne
i = SEQ.index("<th>Matériau</th><th>Tenue humidité / gel</th>")
TABLE = SEQ[i:SEQ.index("</table>", i)]
MATERIAUX = []
for nom, cases in re.findall(r"<tr><td>([^<]+)</td>(.*?)</tr>", TABLE, re.S):
    vals = []
    for fs in re.findall(r"<fieldset.*?</fieldset>", cases, re.S):
        bonnes = [v for v, attr in re.findall(r'value="([^"]+)"([^>]*)>', fs) if "data-pourquoi" not in attr]
        assert len(bonnes) == 1, (nom, bonnes)
        vals.append(bonnes[0])
    MATERIAUX.append([nom] + vals)
assert [m[0] for m in MATERIAUX] == ["Bois palette", "Plastique récup", "Carton renforcé"], MATERIAUX
LONG = {"Bois palette": "le bois de palette", "Plastique récup": "le plastique récupéré",
        "Carton renforcé": "le carton renforcé"}


def donnees():
    par_n = {n: (nom, m) for n, nom, m in PLANNING}
    taches = [[NOMS[par_n[n][0]], "%d min" % par_n[n][1]] for n in DESORDRE]
    dire_t = " ".join("%s : %d minutes." % (NOMS[par_n[n][0]], par_n[n][1]) for n in DESORDRE)
    dire_m = " ".join("%s : tenue à la pluie et au gel %s, découpe %s, impact environnemental %s."
                      % (LONG[m[0]][0].upper() + LONG[m[0]][1:], m[1].lower(), m[2].lower(), m[3].lower())
                      for m in MATERIAUX)
    return {
        "qcm": ["qcm_4e_C7_jardin-conception.html"],
        "documents": {
            "doc_taches_jardin": {
                "titre": "Les tâches du projet du jardin",
                "sous_titre": "Données dans le désordre, chacune avec sa durée.",
                "desc": "Les quatre tâches du projet du jardin, données dans le désordre, avec leur durée. " + dire_t,
                "blocs": [{"tableau": {"colonnes": ["Tâche", "Durée"], "largeurs": [236, 86], "lignes": taches}}],
                "note": "min : minute · la liste ne dit pas dans quel ordre mener les tâches.",
            },
            "doc_tableau_materiaux": {
                "titre": "Trois matériaux pour le boîtier",
                "sous_titre": "Après le banc météo : ce que chacun tient, se laisse faire, et coûte au monde.",
                "desc": "Le tableau des trois matériaux pour le boîtier du jardin, rempli après le banc météo. " + dire_m,
                "blocs": [{"tableau": {"colonnes": ["Matériau", "Pluie", "Découpe", "Impact"],
                                       "largeurs": [128, 58, 76, 60], "lignes": MATERIAUX}}],
                "note": "Pluie : tenue à l'humidité et au gel · Découpe : facilité à le couper avec les outils "
                        "du collège · Impact : impact environnemental.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C7.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_4e_C7.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
