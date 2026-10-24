# -*- coding: utf-8 -*-
"""controle_marqueurs.py — toute pointe de flèche (<marker>) est mesurée en pixels, pas en « traits ».

LE CONSTAT
----------
Un `<marker>` SVG sans `markerUnits` se mesure par défaut en multiples de l'épaisseur du trait qui le
porte : `markerWidth="8"` sur un trait de 12 donne une pointe de 96 px. La pointe grandit avec le trait,
sans que rien dans le fichier ne le dise. Mesuré le 03/10/2026 (thème 1) puis le 05/10/2026 (thème 2) :
des pointes plus larges que le dernier segment qui les porte (la pointe déborde, recouvre le départ du
tracé et les étiquettes voisines), et des marqueurs partagés par des traits d'épaisseurs différentes, dont
la pointe changeait de taille d'un tracé à l'autre. Dans `energie_stockage_transformation.svg` (4e_C4.1),
des pointes de 96 px sur des tracés de 80 px mangeaient les mots « électrique » et « hydraulique ».

La correction (journal du 03/10/2026) : `markerUnits="userSpaceOnUse"`, un `viewBox` qui garde le dessin,
`markerWidth`/`markerHeight` en pixels, le marqueur dédoublé quand les traits n'ont pas la même épaisseur.

CE QU'IL MESURE
---------------
Dans chaque .svg, .html, .py, .js, .mjs du dépôt (hors `_archive-anciennes-versions` et `_outils`), chaque
balise `<marker …>` doit
  1. porter `markerUnits="userSpaceOnUse"` — absent, ou `strokeWidth` écrit en toutes lettres : refusé ;
  2. porter alors `markerWidth` ET `markerHeight` — sans eux, la pointe vaut 3 px (valeur par défaut).
Une balise écrite sur plusieurs lignes, ou fabriquée par un générateur Python ou une chaîne JavaScript,
est lue comme les autres : c'est le texte du fichier qui est regardé, pas l'image.

NON LU : que la pointe tienne dans le dernier segment du tracé, et que le dessin soit identique à
celui d'avant la conversion. Cela se mesure au rendu (avant/après, au pixel près), pas dans un script :
le journal du 05/10/2026 dit comment.

TOLERES : fichiers qui n'ont pas encore reçu la correction, nommés un à un, avec la raison. Du 05/10 au
24/10/2026, ceux du thème 3 (16 SVG et `gantt_premium.py`) ; la liste est vide depuis. Une tolérance dont le fichier
est devenu conforme est annoncée « périmée » ; elle se retire dans la PR suivante qui touche `_outils/`.

Usage :
    python3 _outils/controle_marqueurs.py           # rapport complet
    python3 _outils/controle_marqueurs.py --muet    # seulement les refus
Sortie : 0 si chaque marqueur est en pixels, 1 sinon, 2 si rien n'a pu être lu (règle d'or n°299).
"""
import os
import re
import sys

import panne

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "__pycache__",
           ".playwright-mcp", "captures"}
EXTENSIONS = (".svg", ".html", ".py", ".js", ".mjs")
BALISE = re.compile(r"<marker\b[^>]*>")

#: fichiers pas encore corrigés, tolérés NOMMÉMENT, avec la raison. Vide depuis le 24/10/2026 : les
#: 17 fichiers du thème 3 tolérés le 05/10/2026 sont conformes depuis la fusion de leur PR. Le mécanisme
#: reste, pour la prochaine correction qui ne pourrait pas se faire dans la même PR.
TOLERES = {}


def fichiers(racine):
    for dossier, sous, noms in os.walk(racine):
        sous[:] = [d for d in sous if d not in ECARTES]
        for nom in noms:
            if nom.lower().endswith(EXTENSIONS):
                yield os.path.join(dossier, nom)


def attribut(balise, nom):
    m = re.search(r'\b%s\s*=\s*["\']([^"\']*)["\']' % nom, balise)
    return m.group(1) if m else None


def reproche(balise):
    """None si la balise est conforme, sinon la phrase qui dit pourquoi."""
    unites = attribut(balise, "markerUnits")
    ident = attribut(balise, "id") or "(sans id)"
    if unites != "userSpaceOnUse":
        return "marqueur « %s » : markerUnits %s — la pointe grandit avec le trait" % (
            ident, "absent" if unites is None else "= « %s »" % unites)
    if attribut(balise, "markerWidth") is None or attribut(balise, "markerHeight") is None:
        return "marqueur « %s » : userSpaceOnUse sans markerWidth/markerHeight — la pointe vaut 3 px" % ident
    return None


def main(muet=False, toleres=None):
    toleres = TOLERES if toleres is None else toleres
    lus, vus, ecarts, signales, avec_ecart = 0, 0, [], [], set()
    for chemin in fichiers(DEPOT):
        try:
            texte = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        lus += 1
        rel = os.path.relpath(chemin, DEPOT).replace(os.sep, "/")
        griefs = []
        for m in BALISE.finditer(texte):
            vus += 1
            g = reproche(m.group(0))
            if g:
                griefs.append("ligne %d : %s" % (texte.count("\n", 0, m.start()) + 1, g))
        if griefs:
            avec_ecart.add(rel)
            (signales if rel in toleres else ecarts).append((rel, griefs))
    if not lus:
        return panne.rien_vu("aucun fichier %s sous %s" % ("/".join(EXTENSIONS), DEPOT))
    perimes = sorted(rel for rel in toleres if rel not in avec_ecart)
    if not muet:
        print("%d fichier(s) lus · %d marqueur(s) · %d fichier(s) en écart · %d toléré(s) nommément"
              % (lus, vus, len(ecarts), len(signales)))
        print("     NON LU : que la pointe tienne dans le dernier segment du tracé, et que le dessin\n"
              "     soit identique à celui d'avant : cela se mesure au rendu, pas dans un script.")
        if signales:
            print("\n⚠ %d fichier(s) pas encore corrigés, TOLÉRÉS nommément (TOLERES) :" % len(signales))
            for rel, griefs in signales:
                print("  %s  (%d marqueur(s))\n     %s" % (rel, len(griefs), toleres[rel]))
        if perimes:
            print("\nℹ %d tolérance(s) périmée(s) — le fichier est conforme ou absent, retirer l'entrée de TOLERES :"
                  % len(perimes))
            for rel in perimes:
                print("  %s" % rel)
    if ecarts:
        print("\n⛔ %d fichier(s) avec des marqueurs en « multiples du trait » :" % len(ecarts))
        for rel, griefs in ecarts:
            print("  %s" % rel)
            for g in griefs:
                print("     %s" % g)
        return 1
    print("\n✅ chaque pointe de flèche est mesurée en pixels (markerUnits=\"userSpaceOnUse\")")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
