# -*- coding: utf-8 -*-
"""controle_gestes_outil.py — l'encart « les quatre gestes » nomme l'outil de SA page.

LE CONSTAT
----------
Le 08/09/2026, Pascal lit dans `4e_C1.1` : « Ouvre l'éditeur (Arduino ou mBlock) et
crée un nouveau programme. » — dans une séquence qui ne programme rien et ouvre un
CSV dans un tableur. L'encart (règle d'or n°93, les gestes d'outil réenseignés à
chaque niveau) avait été posé le 11/08 par un choix par mots-clés qui lisait aussi
le CODE de la page : le mot « arduino » n'y figurait que dans le vérificateur
JavaScript d'une activité. Mesuré sur les 22 encarts du dépôt : un seul faux.

CE QU'IL MESURE
---------------
Pour chaque page qui porte `<section class="card gestes-outil">`, l'outil nommé dans
son titre (« les quatre gestes de/du X ») doit apparaître dans le TEXTE VISIBLE de la
page HORS de l'encart — ni dans un <script>, ni dans un <style>, ni dans une balise.
Sinon la page est refusée : elle enseigne les gestes d'un outil qu'elle n'emploie pas.

Les outils connus et les mots qui les trahissent sont dans OUTILS. Un outil inconnu
est refusé aussi : il faut l'ajouter ici, avec ses mots, plutôt que de le deviner.

Usage :
    python3 _outils/controle_gestes_outil.py           # rapport complet
    python3 _outils/controle_gestes_outil.py --muet    # seulement les refus
Sortie : 0 si chaque encart parle de l'outil de sa page, 1 sinon.
"""

import glob
import html
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

ENCART = re.compile(r'<section class="card gestes-outil".*?</section>', re.S)
TITRE = re.compile(r"quatre gestes (?:de |du |d')\s*([^<]+)<", re.I)

#: l'outil tel que l'encart le nomme → ce que la page doit dire ailleurs
OUTILS = {
    "arduino": r"arduino|mblock|t[ée]l[ée]vers",
    "onshape": r"onshape",
    "packet tracer": r"packet\s*tracer",
    "tableur": r"tableur|libreoffice|\bcalc\b|classeur",
    "vittascience": r"vittascience",
    "mblock": r"mblock",
    "thonny": r"thonny",
    "freecad": r"freecad",
}


def pages(racine):
    return sorted(f for f in glob.glob(os.path.join(racine, "**", "*.html"), recursive=True)
                  if not any(e in f for e in ECARTES))


def _texte_visible(fragment):
    fragment = re.sub(r"<(script|style)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    return html.unescape(re.sub(r"<[^>]+>", " ", fragment))


def juger(chemin):
    """None si la page n'a pas d'encart ; sinon (outil, nb d'occurrences, motif)."""
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    m = ENCART.search(texte)
    if not m:
        return None
    t = TITRE.search(m.group(0))
    outil = t.group(1).strip().lower() if t else ""
    reste = _texte_visible(texte[:m.start()] + texte[m.end():])
    motif = OUTILS.get(outil)
    if motif is None:
        return outil or "(sans titre)", -1, None
    return outil, len(re.findall(motif, reste, re.I)), motif


def main(muet=False):
    vus, ecarts = 0, []
    for f in pages(DEPOT):
        r = juger(f)
        if r is None:
            continue
        vus += 1
        outil, n, motif = r
        rel = os.path.relpath(f, DEPOT).replace(os.sep, "/")
        if n < 0:
            ecarts.append((rel, "outil « %s » inconnu de OUTILS : ajoute-le avec ses mots" % outil))
        elif n == 0:
            ecarts.append((rel, "l'encart enseigne « %s », et la page ne l'emploie nulle part "
                                "(aucun mot du motif /%s/ hors de l'encart)" % (outil, motif)))
    if not muet:
        print("%d encart(s) « les quatre gestes » lus · %d écart(s)" % (vus, len(ecarts)))
        print("     NON LU : que les quatre gestes soient JUSTES pour cet outil et cette version —\n"
              "     cela se vérifie devant le logiciel, pas dans un script.")
    if ecarts:
        print("\n⛔ %d encart(s) parlent d'un outil que leur page n'emploie pas :" % len(ecarts))
        for rel, d in ecarts:
            print("  %s\n     %s" % (rel, d))
        return 1
    print("\n✅ chaque encart « les quatre gestes » nomme l'outil de sa page")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
