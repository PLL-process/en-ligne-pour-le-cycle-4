# -*- coding: utf-8 -*-
"""Les documents du QCM de 3e_C4.7, lus dans la séquence elle-même (règles d'or n°233 et n°345, 28/11/2026).

- « La table de routage de R2 » : les trois règles de la consigne de l'activité 4 (« Ta table : réseau 198.51.100.x → R1
  · … »), sans aucun paquet aiguillé.
- « Trois paquets, à l'arrivée » : les paquets du schéma de l'activité 3 (`Images/decoupage_en_paquets.svg`) dans leur
  ordre d'arrivée, n°3, n°1, n°2 — sans le message reconstitué.

    python3 documents_qcm.py             écrit documents_qcm_3e_C4.7.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_3e_C4.7.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_3e_C4.7.json")
SEQ = open(os.path.join(ICI, "sequence_3e_C4.7-C4.8_internet_sainte_luce.html"), encoding="utf-8").read()
SVG = open(os.path.join(ICI, "Images", "decoupage_en_paquets.svg"), encoding="utf-8").read()


def clair(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).strip()


_c = clair(SEQ[SEQ.index("tu ES le routeur R2"):][:400])
REGLES = re.findall(r"(réseau [\d.]+x|tout le reste) → (R\d)", _c)
assert REGLES == [("réseau 198.51.100.x", "R1"), ("réseau 203.0.113.x", "R4"), ("tout le reste", "R3")], REGLES

TEXTES = [html.unescape(t).strip() for t in re.findall(r"<text[^>]*>([^<]*)", SVG)]
CONTENU = {}
for k, t in enumerate(TEXTES):
    m = re.match(r"n°(\d)/3 · IP dest\.", t)
    if m:
        CONTENU[m.group(1)] = TEXTES[k + 1]
_i = TEXTES.index("Arrivée (parfois dans le désordre) :")
ARRIVEE = [t[2:] for t in TEXTES[_i + 1:_i + 4]]
assert ARRIVEE == ["3", "1", "2"] and len(CONTENU) == 3, (ARRIVEE, CONTENU)


def donnees():
    return {
        "qcm": ["qcm_3e_C4.7-C4.8_internet_sainte_luce.html"],
        "documents": {
            "doc_table_routage_r2": {
                "titre": "La table de routage de R2",
                "sous_titre": "Pour chaque paquet, le routeur R2 lit l'adresse de destination, puis cherche la "
                              "règle qui lui correspond.",
                "desc": "La table de routage du routeur R2, en trois règles : "
                        + " ; ".join("%s : envoyer vers %s" % r for r in REGLES)
                        + ". Le document n'aiguille aucun paquet.",
                "blocs": [{"tableau": {"colonnes": ["Destination", "Envoyer vers"], "largeurs": [210, 112],
                                       "lignes": [[r[0], r[1]] for r in REGLES]}}],
                "note": "x : n'importe quel nombre · Le document n'aiguille aucun paquet : c'est la question.",
            },
            "doc_paquets_arrivee": {
                "titre": "Trois paquets, à l'arrivée",
                "sous_titre": "Un message d'alerte, découpé en trois paquets, arrive au téléphone dans cet ordre.",
                "desc": "Trois paquets d'un même message arrivent dans cet ordre : "
                        + " ; ".join("le paquet n°%s sur 3, qui porte « %s »" % (n, CONTENU[n].strip("« »"))
                                     for n in ARRIVEE)
                        + ". Chaque en-tête porte aussi l'adresse IP de l'expéditeur et celle du destinataire. "
                          "Le document ne dit pas le message reconstitué.",
                "blocs": [{"tableau": {"colonnes": ["Arrivé", "En-tête", "Contenu"], "largeurs": [70, 96, 156],
                                       "lignes": [["%s%s" % (k + 1, "er" if k == 0 else "e"), "n°%s / 3" % n,
                                                   CONTENU[n]] for k, n in enumerate(ARRIVEE)]}}],
                "note": "Chaque en-tête porte aussi l'adresse IP de l'expéditeur et celle du destinataire · Le "
                        "document ne dit pas le message reconstitué : c'est la question.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_3e_C4.7.json est à jour de la séquence" if ok
              else "✘ documents_qcm_3e_C4.7.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
