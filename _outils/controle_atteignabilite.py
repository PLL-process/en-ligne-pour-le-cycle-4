# -*- coding: utf-8 -*-
"""controle_atteignabilite.py — un fichier livré qu'aucun chemin n'atteint n'est pas livré.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le 31/08/2026, la suite du lot `3e_C5.1` ne trouvait que **quatre** liens
internes dans sa séquence : l'index, le lexique, le QCM, une ancre. Ses deux
synthèses n'y figuraient pas.

En marchant depuis `index.html` de lien en lien sur tout le dépôt :

  · **76** synthèses au total ;
  · **20** atteignables ;
  · **56** atteignables par **aucun chemin** — ni depuis le tableau de bord, ni
    depuis la séquence à laquelle elles appartiennent.

Ce n'était pas un défaut d'un lot : **40 séquences sur 46** ne lient pas leurs
synthèses, ce qui en faisait la règle. La cause tenait en une ligne :
`_outils/make_index.py` ne lisait que le dossier du code, et les synthèses
vivent dans un sous-dossier `Synthèses/`.

Une synthèse est pourtant le document que l'élève emporte. Le correctif s'est
fait au générateur, en un endroit plutôt qu'en quarante : il en reste **quatre**
inatteignables, plus une page de repères — toutes déclarées ci-dessous.

CE QU'IL FAIT
-------------
Il part de `index.html`, suit les liens locaux `href`/`src`/`data` vers des
pages HTML, de proche en proche, et compare le résultat à toutes les pages du
dépôt. Une page que la marche n'atteint pas est **refusée**, sauf si elle est
nommée dans `TOLEREES` avec sa raison et ce qui la débloquera.

POURQUOI UNE LISTE DE TOLÉRÉES PLUTÔT QU'UN SIMPLE COMPTE
---------------------------------------------------------
Un compte laisse la dette grandir sans bruit. Une liste nommée fait l'inverse :
elle acte les cinq cas connus, elle dit pour chacun ce qui le résoudra, et elle
**refuse la sixième** — celle qu'on ajouterait demain sans s'en apercevoir. Le
jour où une PR sœur en règle une, sa ligne se retire d'ici.

CE QU'IL NE FAIT PAS
--------------------
Il ne vérifie pas qu'un lien pointe sur un fichier existant — c'est
`controle_liens.py`. Il ne juge pas la profondeur d'un chemin : une page à cinq
clics de l'entrée est atteignable, même si elle est mal placée. Et il ne suit
que les liens **écrits dans le HTML** : une page qu'un script construirait à
l'exécution lui est invisible, et c'est une raison de plus pour ne pas
construire sa navigation en JavaScript.

Usage :
    python3 _outils/controle_atteignabilite.py           # rapport complet
    python3 _outils/controle_atteignabilite.py --muet    # seulement les refus
Sortie : 0 si toute page du dépôt est atteignable depuis l'index, 1 sinon.
"""

import os
import re
import sys
from urllib.parse import unquote

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTREE = "index.html"
ECARTES = ("_archive-anciennes-versions", "_outils")

#: Les pages qu'aucun chemin n'atteint encore, chacune avec sa raison et ce qui
#: la débloquera. Cette liste ne doit que RÉTRÉCIR : une entrée s'en retire le
#: jour où sa PR passe, et rien ne s'y ajoute sans une décision écrite.
TOLEREES = {
    # Vide au 31/08/2026, et c'est un fait mesuré, pas un vœu : les 338 pages du
    # dépôt sont atteignables depuis l'index. Les cinq entrées qui figuraient ici
    # ont été retirées une à une, à mesure que leur PR passait :
    #   · les 4 synthèses des ateliers CAO et planification — PR #329, leurs huit
    #     pages portent désormais le bloc « Les traces à garder » ;
    #   · `_reperes/carte_des_representations.html` — PR #330, la synthèse
    #     professeur de `5e_C1.1` répond au lien que la carte lui adressait déjà,
    #     et ce fichier-ci le pose maintenant au pied de l'index.
    # Une entrée ne s'ajoute ici qu'avec sa raison ET ce qui la débloquera
    # (règle d'or n°273 : une liste d'exceptions ne peut que rétrécir).
}

#: Un lien local vers une page. On lit `href`, `src` et `data` : une séquence
#: appelle ses schémas par `data=` et ses pages par `href=`, et un `<object>`
#: peut porter une page comme un SVG.
LIEN = re.compile(r'(?:href|src|data)\s*=\s*"([^"#?]+\.html)[^"]*"', re.I)


def pages(racine):
    for dossier, _, fichiers in os.walk(racine):
        rel = os.path.relpath(dossier, racine)
        if any(e in rel.split(os.sep) for e in ECARTES):
            continue
        for f in sorted(fichiers):
            if f.lower().endswith(".html"):
                yield os.path.relpath(os.path.join(dossier, f), racine).replace(os.sep, "/")


def marcher(racine, depart=ENTREE):
    """Les pages atteintes depuis `depart`, de lien en lien."""
    vues, pile = set(), [depart]
    while pile:
        rel = os.path.normpath(pile.pop()).replace(os.sep, "/")
        if rel in vues:
            continue
        plein = os.path.join(racine, rel)
        if not os.path.isfile(plein) or "_archive-anciennes-versions" in rel:
            continue
        vues.add(rel)
        texte = open(plein, encoding="utf-8", errors="replace").read()
        for u in LIEN.findall(texte):
            u = unquote(u)
            if u.startswith(("http://", "https://", "//", "mailto:")):
                continue
            pile.append(os.path.join(os.path.dirname(rel), u))
    return vues


def main(muet=False):
    toutes = sorted(pages(DEPOT))
    vues = marcher(DEPOT)
    perdues = [p for p in toutes if p not in vues]
    tolerees = [p for p in perdues if p in TOLEREES]
    refusees = [p for p in perdues if p not in TOLEREES]
    fantomes = [p for p in TOLEREES if p not in perdues]

    if not muet:
        syntheses = [p for p in toutes if "/Synthèses/" in p]
        print("%d page(s) HTML dans le dépôt · %d atteignables depuis %s en suivant les liens "
              "· %d non" % (len(toutes), len(vues & set(toutes)), ENTREE, len(perdues)))
        print("     dont %d synthèse(s), %d atteignable(s)"
              % (len(syntheses), sum(1 for s in syntheses if s in vues)))
        if tolerees:
            print("\n%d page(s) tolérée(s), chacune avec sa raison écrite :" % len(tolerees))
            for p in tolerees:
                print("  %s\n     %s" % (p, TOLEREES[p]))
        print("\n     NON LU : qu'un lien pointe sur un fichier existant (c'est "
              "`controle_liens.py`) ;\n     la profondeur d'un chemin ; et toute navigation "
              "construite en JavaScript,\n     qui reste invisible à une lecture du HTML.")

    if fantomes:
        print("\n⚠ %d page(s) tolérée(s) sont désormais atteignables — leur ligne peut sortir "
              "de TOLEREES :" % len(fantomes))
        for p in sorted(fantomes):
            print("  " + p)

    if refusees:
        print("\n⛔ %d page(s) que la marche depuis %s n'atteint pas :" % (len(refusees), ENTREE))
        for p in refusees:
            print("  " + p)
        print("\n     Une page peut n'être atteignable par personne — on le dit alors, dans\n"
              "     TOLEREES, avec la raison et ce qui la débloquera. Ce qu'elle ne peut pas\n"
              "     faire, c'est exister sans que personne puisse l'ouvrir (règle n°272).")
        return 1
    print("\n✅ toute page du dépôt est atteignable depuis l'index, hors tolérées déclarées")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
