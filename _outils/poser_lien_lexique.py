# -*- coding: utf-8 -*-
"""poser_lien_lexique.py — un lexique que rien ne désigne n'existe pas pour l'élève.

`generer_lexique.py` écrit la page. Il ne la relie à rien. Résultat mesuré sur le
Thème 1 : **13 lexiques produits, 11 séquences qui les désignent** — les deux lots
héritage `3e_C1.5` et `4e_C1.4` portent un lexique que personne n'ouvrira jamais,
faute d'un chemin pour y aller.

Ce script pose le lien dans la barre de navigation de la séquence, à côté de
« ⌂ Accueil », exactement comme le font les onze séquences du Thème 1 qui l'ont :

    <nav id="navharm"><a href="…/index.html">⌂ Accueil</a><a href="lexique_X.html">📖 Lexique</a></nav>

Il ne pose que si le fichier de lexique EXISTE réellement à côté de la séquence :
on ne fabrique pas un lien vers une page absente (règle n°183 — un bouton qui ne
mène nulle part apprend à ne plus cliquer sur les boutons).

    python3 _outils/poser_lien_lexique.py --etat            dit où le lien manque
    python3 _outils/poser_lien_lexique.py --theme theme-2-… pose les liens manquants
"""

import argparse
import glob
import os
import re
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

NAV = re.compile(r'(<nav\b[^>]*\bid="navharm"[^>]*>)(.*?)(</nav>)', re.S | re.I)


def lexique_voisin(sequence):
    """Le lexique du même dossier, s'il existe."""
    trouves = sorted(glob.glob(os.path.join(os.path.dirname(sequence), "lexique_*.html")))
    return os.path.basename(trouves[0]) if trouves else None


def poser(sequence, appliquer):
    with open(sequence, encoding="utf-8") as f:
        t = f.read()
    lex = lexique_voisin(sequence)
    if not lex:
        return "pas de lexique dans le dossier", False
    if re.search(r'href="lexique_[^"]*\.html"', t):
        return "déjà relié", False
    m = NAV.search(t)
    if not m:
        return "aucune barre de navigation où poser le lien", False
    if appliquer:
        lien = '<a href="%s">📖 Lexique</a>' % lex
        t = t[:m.end(2)] + lien + t[m.end(2):]
        with open(sequence, "w", encoding="utf-8") as f:
            f.write(t)
    return "→ %s" % lex, True


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--etat", action="store_true", help="ne touche à rien")
    ap.add_argument("--theme", default="theme-2-structure-fonctionnement-comportement")
    a = ap.parse_args(argv)

    base = os.path.join(RACINE, a.theme)
    sequences = sorted(p for p in glob.glob(base + "/**/sequence*.html", recursive=True)
                       if "_archive" not in p)
    poses = ignores = 0
    for s in sequences:
        mot, fait = poser(s, appliquer=not a.etat)
        marque = ("⏳" if a.etat else "✅") if fait else "  "
        print("  %s %-56s %s" % (marque, os.path.basename(s)[:54], mot))
        poses += fait
        ignores += not fait
    print("\n  %d lien(s) %s · %d séquence(s) sans rien à faire"
          % (poses, "à poser" if a.etat else "posé(s)", ignores))
    return 0


if __name__ == "__main__":
    sys.exit(main())
