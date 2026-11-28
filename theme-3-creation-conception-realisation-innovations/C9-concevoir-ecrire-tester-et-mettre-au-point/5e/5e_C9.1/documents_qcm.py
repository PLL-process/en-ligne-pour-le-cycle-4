# -*- coding: utf-8 -*-
"""Les documents du QCM de 5e_C9.1, lus dans la séquence elle-même (règles d'or n°233 et n°345, 27/11/2026).

Ce lot n'a pas de fichier de modèle : ses données sont dans la page. Ce script les y LIT.
- Activité 4 : le programme du responsable (six lignes) et son banc de trois tests (montes, descendus, attendu) — le
  document « Le programme du compteur » les montre, sans la colonne « obtenu » : trouver ce qu'il donne, c'est la
  question.
- Activité 5 : la règle de la barrière et son banc de trois tests (places, attendu) — le document « Le banc de la
  barrière », sans dire quel test est le cas limite.

    python3 documents_qcm.py             écrit documents_qcm_5e_C9.1.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_5e_C9.1.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_5e_C9.1.json")
SEQ = open(os.path.join(ICI, "sequence_5e_C9.1-C9.3_boite_etiquetee.html"), encoding="utf-8").read()


def clair(t):
    return re.sub(r"[ \t]+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


def banc(etiquette):
    t = SEQ[SEQ.index('aria-label="%s"' % etiquette):]
    t = t[:t.index("</table>")]
    return [[clair(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr)[:-2]]
            for tr in re.findall(r"<tr>(<td>.*?)</tr>", t, re.S)]


_i = SEQ.index("voici le programme JOINT")
PROGRAMME = clair(re.search(r'<pre class="code">(.*?)</pre>', SEQ[_i:], re.S).group(1)).split("\n")
assert PROGRAMME[0] == "places = 24" and len(PROGRAMME) == 6, PROGRAMME
COMPTEUR = banc("Banc de tests du programme du compteur")          # [test, montes, descendus, attendu]
assert [l[0][:2] for l in COMPTEUR] == ["T1", "T2", "T3"] and all(len(l) == 4 for l in COMPTEUR), COMPTEUR
BARRIERE = banc("Banc de tests de la barrière")                    # [test, places, attendu]
assert [l[0][:2] for l in BARRIERE] == ["B1", "B2", "B3"] and all(len(l) == 3 for l in BARRIERE), BARRIERE
REGLE = clair(re.search(r"la barrière obéit à la règle\s*<code>(.*?)</code>", SEQ).group(1))
assert REGLE.startswith("SI places > 0"), REGLE


def sans_verdict(nom):
    """Le nom du test, sans ce qui désigne la réponse (« LE CAS LIMITE »)."""
    return re.sub(r"\s*LE CAS LIMITE\s*:\s*", " ", nom.split(" — ", 1)[1]).strip()


def donnees():
    return {
        "qcm": ["qcm_5e_C9.1-C9.3_boite_etiquetee.html"],
        "documents": {
            "doc_programme_compteur": {
                "titre": "Le programme du compteur",
                "sous_titre": "Le programme envoyé par le responsable du Cyclone, et son banc de trois tests. Le "
                              "besoin : afficher le bon nombre de places libres.",
                "desc": "Le programme du compteur, ligne par ligne : "
                        + " ; ".join("ligne %d, %s" % (k + 1, l) for k, l in enumerate(PROGRAMME))
                        + ". Son banc de trois tests, où montes et descendus remplacent les lignes 2 et 3 : "
                        + " ".join("%s, %s : montes %s, descendus %s, attendu %s." % (l[0].split(" — ")[0],
                                   l[0].split(" — ")[1].lower(), l[1], l[2], l[3]) for l in COMPTEUR)
                        + " Le document ne dit pas ce que le programme affiche.",
                "blocs": [
                    {"tableau": {"colonnes": ["Ligne", "Instruction"], "largeurs": [64, 258],
                                 "lignes": [[str(k + 1), l] for k, l in enumerate(PROGRAMME)]}},
                    {"tableau": {"colonnes": ["Test", "montes", "descendus", "attendu"],
                                 "largeurs": [64, 82, 100, 76],
                                 "lignes": [[l[0].split(" — ")[0]] + l[1:] for l in COMPTEUR]}},
                ],
                "note": "Au banc, montes et descendus remplacent les valeurs des lignes 2 et 3 · Le document ne dit "
                        "pas ce que le programme affiche : c'est la question.",
            },
            "doc_banc_barriere": {
                "titre": "Le banc de la barrière",
                "sous_titre": "La règle qui commande la barrière du Cyclone, et son banc de trois tests.",
                "desc": "La barrière du Cyclone obéit à la règle : %s. Son banc de trois tests : " % REGLE
                        + " ".join("%s, %s : places %s, attendu %s." % (l[0].split(" — ")[0],
                                   sans_verdict(l[0]).lower(), l[1], l[2]) for l in BARRIERE)
                        + " Le document ne dit pas quel test est le plus important.",
                "blocs": [
                    {"fiches": [{"titre": "La règle", "lignes": [p.strip() for p in REGLE.split(", ")]}]},
                    {"tableau": {"colonnes": ["Test", "places", "attendu"], "largeurs": [64, 110, 148],
                                 "lignes": [[l[0].split(" — ")[0], l[1], l[2]] for l in BARRIERE]}},
                    {"fiches": [{"titre": "Ce que vise chaque test",
                                 "lignes": ["%s : %s." % (l[0].split(" — ")[0], sans_verdict(l[0]))
                                            for l in BARRIERE]}]},
                ],
                "note": "Le document ne dit pas quel test est le plus important : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_5e_C9.1.json est à jour de la séquence" if ok
              else "✘ documents_qcm_5e_C9.1.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
