# -*- coding: utf-8 -*-
"""Le document du QCM de 4e_C6.1, lu dans la séquence elle-même (règles d'or n°233 et n°345, 28/11/2026).

Ce script LIT les deux lignes du programme corrigé du jardin dans la correction de l'activité 2 (« LIGNE 1 »,
« LIGNE 2 »). Le document « Le programme corrigé du jardin » les montre, avec le cas « sinon » : il ne dit pas ce que
fait la pompe dans un scénario donné, ni quelle règle un scénario teste — c'est la question.

    python3 documents_qcm.py             écrit documents_qcm_4e_C6.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C6.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C6.1.json")
SEQ = open(os.path.join(ICI, "sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html"), encoding="utf-8").read()


def _ligne(n):
    i = SEQ.index("LIGNE %d — <b>SI</b>" % n)
    t = SEQ[i:SEQ.index("<br>", i + 5)]
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()
    return t[len("LIGNE %d — " % n):].rstrip(".")


L1, L2 = _ligne(1), _ligne(2)
assert L1 == "SI humidité < 35 % ET (heure < 8 h OU heure > 17 h) ALORS pompe ON", L1
assert L2 == "SI humidité > 45 % ALORS pompe OFF", L2
SINON = "SINON : la pompe garde l'état qu'elle avait"
assert "garde son état" in SEQ


def _nb(t):   # pas de mot seul en bout de ligne : unités et petits mots collés
    t = t.replace(" %", " %").replace(" h", " h").replace(" :", " :")
    return re.sub(r" (\S+)$", " \\1", t)


def donnees():
    return {
        "qcm": ["qcm_4e_C6.1-C6.3_ajuster_programme_jardin.html"],
        "documents": {
            "doc_programme_corrige_jardin": {
                "titre": "Le programme corrigé du jardin",
                "sous_titre": "Les règles de la pompe, relues à chaque mesure de l'humidité du sol (en %, pour cent).",
                "desc": "Le programme corrigé du jardin, relu à chaque mesure. Ligne 1 : " + L1 + ". Ligne 2 : "
                        + L2 + ". " + SINON + ". Le document ne dit pas ce que fait la pompe dans un cas donné.",
                "blocs": [{"fiches": [
                    {"titre": "Ligne 1 · démarrer", "lignes": [_nb("SI humidité < 35 %"), _nb("ET (heure < 8 h OU heure > 17 h)"), _nb("ALORS pompe ON")]},
                    {"titre": "Ligne 2 · arrêter", "lignes": [_nb("SI humidité > 45 %"), _nb("ALORS pompe OFF")]},
                    {"titre": "Sinon", "lignes": [_nb("la pompe garde l'état qu'elle avait")]},
                ]}],
                "note": "ON\u00a0: allumée · OFF\u00a0: éteinte · h\u00a0: l'heure de\u00a0la\u00a0journée.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C6.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_4e_C6.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
