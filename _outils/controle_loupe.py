# -*- coding: utf-8 -*-
"""Règle d'or n°92 — l'agrandisseur d'images posé dans les pages est le v2, une seule fois.

    python3 _outils/controle_loupe.py [racine]

Sortie 0 : toutes les pages lues ont au plus un agrandisseur, et c'est le v2.
Sortie 1 : une page porte encore le v1 (marqueur « loupe-images-v1 »), un agrandisseur
           sans marqueur, ou deux agrandisseurs. Elle est nommée.
Sortie 2 : aucune page lue (règle n°299 : un contrôle qui n'a rien vérifié est en panne).

Pourquoi ce contrôle : le v1 agrandissait un schéma SVG écrit dans la page sans les couleurs
ni la police de la page (formes noires, texte qui déborde : constat de Pascal, 25/10/2026),
et sa légende recouvrait l'image (journal du 24/09/2026). Cinq générateurs posent la loupe
(`theme-3-…/audit/loupe.py` est leur source unique) et deux gabarits la portent : une
régénération avec une vieille copie la ferait revenir en silence.

Ce qu'il NE vérifie PAS : que l'agrandissement soit fidèle et lisible (cela se mesure au
navigateur : `_outils/banc_loupe.py`), ni qu'une page qui a des images ait un agrandisseur.
Les archives (`_archive-anciennes-versions/`) ne sont pas lues : versions gelées.
"""
import pathlib
import re
import sys

SIGNE = "var fond, grande, legende, dernier = null;"   # la fonction de l'agrandisseur, v1 comme v2


def lire(racine):
    pages = []
    for p in sorted(pathlib.Path(racine).rglob("*")):
        if p.suffix not in (".html", ".tpl") or "_archive-anciennes-versions" in p.parts or ".git" in p.parts:
            continue
        pages.append((p, p.read_text(encoding="utf-8", errors="replace")))
    return pages


def defauts(html):
    d = []
    if "loupe-images-v1" in html:
        d.append("agrandisseur v1 (marqueur loupe-images-v1)")
    n = html.count(SIGNE)
    if n > 1:
        d.append("%d agrandisseurs dans la même page" % n)
    if n and "loupe-images-v2" not in html:
        d.append("agrandisseur sans le marqueur loupe-images-v2")
    if n and "function figer(" not in html:
        d.append("agrandisseur qui ne recopie pas les styles du schéma (v1)")
    return d


def main(racine="."):
    pages = lire(racine)
    if not pages:
        print("⛔ aucune page lue sous %s : rien n'a été vérifié" % racine)
        return 2
    equipees = sum(1 for _, h in pages if SIGNE in h)
    refus = [(p, d) for p, h in pages for d in [defauts(h)] if d]
    print("%d page(s) lues · %d avec un agrandisseur" % (len(pages), equipees))
    for p, d in refus:
        print("  ✘ %s — %s" % (p, " ; ".join(d)))
    print("""
PÉRIMÈTRE : pages .html et gabarits .tpl hors archives. Vérifié : marqueur v2, une seule
fonction d'agrandisseur, recopie des styles du schéma (figer). NON vu : la fidélité et la
lisibilité de l'image agrandie (`_outils/banc_loupe.py`, au navigateur).""")
    if refus:
        return 1
    print("✅ chaque agrandisseur est le v2, et chaque page n'en a qu'un")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
