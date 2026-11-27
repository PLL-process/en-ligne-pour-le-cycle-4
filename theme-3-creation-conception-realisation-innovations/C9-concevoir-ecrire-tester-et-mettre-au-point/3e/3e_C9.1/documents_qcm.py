# -*- coding: utf-8 -*-
"""Les documents des deux QCM de 3e_C9.1, lus dans les pages du lot (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : ses données sont dans ses pages. Ce script les y LIT.
- Le banc de démonstration de l'activité 5 de la séquence (les quatre tests T1 à T4, avec air, train_arrive et le
  résultat attendu) et la fonction du document 3 (ses trois branches) : le document « Le banc de la ventilation »
  montre la fonction et le banc, sans la colonne « obtenu » — trouver ce qu'elle renvoie, c'est la question.
- Les définitions des quatre types dans `vocabulaire_3e_C9.1.json` (la phrase qui dit comment la valeur s'écrit, sans
  l'exemple de la séance) : la carte « Les quatre familles de valeurs ».
- L'aide-mémoire des commandes du robot, dans le TP mBot2 (`#apiTable`) : six de ses lignes, sans le mot « capteur »
  ni le mot « actionneur » — les reconnaître, c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_3e_C9.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C9.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C9.1.json")


def lire(nom):
    return open(os.path.join(ICI, nom), encoding="utf-8").read()


def clair(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


SEQ = lire("sequence_3e_C9.1_variables_types_systemes.html")
TP = lire("tp_mbot2_python.html")
VOC = json.loads(lire("vocabulaire_3e_C9.1.json"))

# Le banc de démonstration (activité 5) : une ligne par test
_b = SEQ[SEQ.index('aria-label="Banc de démonstration'):]
_b = _b[:_b.index("</table>")]
BANC = []
for tr in re.findall(r"<tr><td>(T\d) — ([^<]+)</td>(.*?)</tr>", _b, re.S):
    cases = dict(re.findall(r'data-l="(air|train_arrive|attendu)">([^<]*)<', tr[2]))
    BANC.append((tr[0], tr[1].strip(), cases["air"], cases["train_arrive"], cases["attendu"]))
assert [t[0] for t in BANC] == ["T1", "T2", "T3", "T4"], BANC

# La fonction du document 3 : ses trois branches
_f = clair(re.search(r'<pre class="code">(def vitesse_ventilation\(air, train_arrive\):.*?)</pre>', SEQ, re.S).group(1))
BRANCHES = re.findall(r"(if air > 100|elif train_arrive|else): return (\d)", _f)
assert [b[1] for b in BRANCHES] == ["3", "2", "1"], _f

# Les quatre types : la définition, jusqu'à l'exemple de la séance (« Ici, … »)
TYPES = []
for mot in ("int", "float", "str", "bool"):
    d = next(e["definition"] for e in VOC if e["mot"] == mot)
    d = d.split(" Ici,")[0].replace("En Python, le type ", "Le type ")
    d = re.sub(r", comme .*?\.(?=\s|$)", ".", d)                     # l'exemple chiffré de la séance part : la question le pose
    TYPES.append((mot, d))

# L'aide-mémoire du robot (TP mBot2)
_a = TP[TP.index('id="apiTable"'):]
_a = _a[:_a.index("</table>")]
API = {}
for tr in re.findall(r"<tr><td data-th=\"Ce que fait le robot\">(.*?)</td><td data-th=\"Commande\">(.*?)</td>", _a, re.S):
    API[re.sub(r"^\W+", "", clair(tr[0])).split(" (")[0]] = clair(tr[1])
GARDES = ["Écrire, puis passer à la ligne", "Allumer ses lumières", "Avancer", "Tourner sur place",
          "Arrêter les moteurs", "Mesurer la distance devant lui"]
assert all(g in API for g in GARDES), sorted(API)


def donnees():
    sens = {"if air > 100": "si air > 100", "elif train_arrive": "sinon, si un train arrive", "else": "sinon"}
    return {
        "qcm": ["qcm_3e_C9.1_variables_types_systemes.html", "qcm_python_variables.html"],
        "documents": {
            "doc_banc_ventilation": {
                "titre": "Le banc de la ventilation",
                "sous_titre": "La fonction vitesse_ventilation(air, train_arrive), et les quatre tests écrits avant "
                              "de l'exécuter.",
                "desc": "La fonction vitesse_ventilation : "
                        + " ; ".join("%s, elle renvoie %s" % (sens[b[0]], b[1]) for b in BRANCHES)
                        + ". Le banc de quatre tests, écrit avant d'exécuter : "
                        + " ".join("%s, %s : air %s, train_arrive %s, attendu %s." % (t[0], t[1].lower(), *t[2:]) for t in BANC)
                        + " Le banc ne dit pas ce que la fonction renvoie.",
                "blocs": [
                    {"fiches": [{"titre": "La fonction, dans l'ordre",
                                 "lignes": ["%s, elle renvoie %s." % (sens[b[0]].capitalize(), b[1])
                                            for b in BRANCHES]}]},
                    {"tableau": {"colonnes": ["Test", "air", "train_arrive", "attendu"],
                                 "largeurs": [70, 70, 112, 70],
                                 "lignes": [[t[0], t[2], t[3], t[4]] for t in BANC]}},
                    {"fiches": [{"titre": "Ce que vise chaque test",
                                 "lignes": ["%s : %s." % (t[0], t[1].lower().replace("le cas limite", "le cas limite, "
                                                                                      "air = 100 pile"))
                                            for t in BANC]}]},
                ],
                "note": "air : un indice de qualité de l'air, de simulation · Le document ne dit pas ce que la "
                        "fonction renvoie : c'est la question.",
            },
            "doc_familles_valeurs": {
                "titre": "Les quatre familles de valeurs",
                "sous_titre": "Ce que dit chaque type de Python : comment sa valeur s'écrit.",
                "desc": "Les quatre types de valeurs de Python. " + " ".join("%s : %s%s" % (m, d[0].lower(), d[1:]) for m, d in TYPES),
                "blocs": [{"fiches": [{"titre": m, "lignes": [d]} for m, d in TYPES]}],
                "note": "Le document ne range aucune valeur : c'est la question.",
            },
            "doc_commandes_mbot2": {
                "titre": "Six commandes du robot mBot2",
                "sous_titre": "Extrait de l'aide-mémoire du TP : ce que fait le robot, et la commande Python.",
                "desc": "Six commandes du robot mBot2, dont le boîtier à écran s'appelle CyberPi. "
                        + " ".join("%s : %s." % (g, API[g]) for g in GARDES),
                "blocs": [{"fiches": [{"titre": g, "lignes": [API[g]]} for g in GARDES]}],
                "note": "Le document ne dit pas quel élément du robot est un capteur ou un actionneur : c'est la "
                        "question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C9.1.json est à jour des pages du lot" if ok
              else "✘ documents_qcm_3e_C9.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
