# -*- coding: utf-8 -*-
"""Le document du QCM de 4e_C9.1, lu dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : ses données sont dans la page. Ce script les y LIT : la règle d'arrosage avec sa
plage horaire (le pseudo-code de la correction de l'activité 2) et les six essais du tableau de l'activité 4 (numéro,
scénario, entrées). Le document « La règle et ses six essais » les montre sans la colonne « attendu » : trouver ce que
fait la pompe, c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_4e_C9.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C9.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C9.1.json")
SEQ = open(os.path.join(ICI, "sequence_4e_C9_jardin-programme.html"), encoding="utf-8").read()


def clair(t):
    return re.sub(r"[ \t]+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


_i = SEQ.index("Pseudo-code attendu")
REGLE = [l.strip() for l in clair(re.search(r'<div class="py">(.*?)</div>', SEQ[_i:], re.S).group(1)).split("\n")]
assert REGLE[0] == "SEUIL = 40" and REGLE[-1] == "FIN SI" and any(" ET heure" in l for l in REGLE), REGLE
_t = SEQ[SEQ.index('aria-label="Tableau d\'essais à remplir"'):]
_t = _t[:_t.index("</table>")]
ESSAIS = [(n, clair(sc), clair(e)) for n, sc, e in re.findall(
    r'<tr><td data-label="Essai n° ">(\d)</td><td>(.*?)</td><td data-label="Entrées : ">(.*?)</td>', _t)]
assert [e[0] for e in ESSAIS] == ["1", "2", "3", "4", "5", "6"], ESSAIS
ENTREES = [re.match(r"H = (\d+) · (\d+) h$", e[2]).groups() for e in ESSAIS]


def donnees():
    return {
        "qcm": ["qcm_4e_C9_jardin-programme.html"],
        "documents": {
            "doc_regle_essais_arrosage": {
                "titre": "La règle et ses six essais",
                "sous_titre": "La règle d'arrosage du jardin, avec sa plage horaire, et le tableau d'essais écrit "
                              "avant de lancer le programme.",
                "desc": "La règle d'arrosage, ligne par ligne : " + " ; ".join(REGLE) + ". Le tableau de six essais : "
                        + " ".join("Essai %s, %s : H = %s, %s h." % (e[0], e[1].lower(), h, hr)
                                   for e, (h, hr) in zip(ESSAIS, ENTREES))
                        + " Le document ne dit pas ce que fait la pompe.",
                "blocs": [
                    {"fiches": [{"titre": "La règle", "lignes": [m for l in REGLE for m in re.split(r" (?=ET )", l)]}]},
                    {"tableau": {"colonnes": ["Essai", "H", "heure"], "largeurs": [80, 110, 132],
                                 "lignes": [[e[0], h, hr + " h"] for e, (h, hr) in zip(ESSAIS, ENTREES)]}},
                    {"fiches": [{"titre": "Ce que vise chaque essai",
                                 "lignes": ["%s : %s." % (e[0], e[1][0].upper() + e[1][1:]) for e in ESSAIS]}]},
                ],
                "note": "H : l'humidité du sol, en % (pour cent) · h : heure · Le document ne dit pas ce que fait la "
                        "pompe : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C9.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_4e_C9.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
