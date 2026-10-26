# -*- coding: utf-8 -*-
"""Chaque séquence s'imprime en fiche papier : le bloc commun, à jour, une fois.

    python3 _outils/controle_impression_papier.py [racine]

Sortie 0 : chaque page `sequence*.html` (hors archives) porte le bloc « fiche-papier », une fois, identique à la source
           `_outils/impression_papier/` ; aucune autre page ne porte une copie périmée.
Sortie 1 : une page refusée, nommée, avec la raison.
Sortie 2 : aucune séquence lue (règle n°299 : un contrôle qui n'a rien vérifié est en panne).

Pourquoi : demande de Pascal du 25/10/2026 (« les consignes ne sont pas vues […] cela fait beaucoup de pages »). La
fiche papier est une source unique posée par `poser.py` : une correction faite à la source doit arriver dans toutes
les séquences, et une séquence nouvelle ne doit pas s'imprimer comme un écran.

Ce qu'il NE vérifie PAS : le rendu imprimé (contraste : `controle_impression.mjs` ; pages, champs, séances : le banc
`_outils/impression_papier/banc_papier.py`). Les archives ne sont pas lues.
"""
import importlib.util
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("poser_papier", ICI / "impression_papier" / "poser.py")
poser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser)


def defauts(html, est_sequence):
    d = []
    blocs = poser.blocs_de(html)
    if len(blocs) > 1:
        d.append("%d blocs de la fiche papier" % len(blocs))
    if blocs and blocs[0] != poser.bloc():
        d.append("bloc de la fiche papier différent de la source (relancer poser.py)")
    if est_sequence and not blocs:
        d.append("séquence sans la fiche papier")
    return d


def main(racine="."):
    pages = [p for p in sorted(pathlib.Path(racine).rglob("*.html"))
             if "_archive-anciennes-versions" not in p.parts and ".git" not in p.parts]
    sequences = [p for p in pages if p.name.startswith("sequence")]
    if not sequences:
        print("⛔ aucune séquence lue sous %s : rien n'a été vérifié" % racine)
        return 2
    refus = []
    for p in pages:
        d = defauts(p.read_text(encoding="utf-8", errors="replace"), p.name.startswith("sequence"))
        if d:
            refus.append((p, d))
    print("%d page(s) lues · %d séquence(s)" % (len(pages), len(sequences)))
    for p, d in refus:
        print("  ✘ %s — %s" % (p, " ; ".join(d)))
    print("""
PÉRIMÈTRE : pages .html hors archives ; les séquences doivent porter la fiche papier. NON vu : le rendu imprimé
(`controle_impression.mjs`, `_outils/impression_papier/banc_papier.py`).""")
    if refus:
        return 1
    print("✅ chaque séquence s'imprime en fiche papier, à jour")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
