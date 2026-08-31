# -*- coding: utf-8 -*-
"""controle_rapports_tests.py — un rapport qui cite un script doit le livrer.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le 31/08/2026, deux lots ont reçu la suite de tests que leur rapport annonçait
depuis des semaines (`5e_C8.2`, puis `5e_C4.1`). Chaque fois, le rapport citait
un script — et chaque fois, ce script n'était pas dans le dépôt.

Mesure faite sur les **63 rapports** du dépôt :

  · **31** portent des coches vertes et **aucun script** dans leur dossier ;
  · **7** vont plus loin : ils **nomment** un script — `tests_lot05.js` à
    `tests_lot11.js` — qui n'a jamais été commité. Un lecteur qui suit la
    référence ne trouve rien.

La différence entre les deux compte. Un rapport sans script est une **dette** :
il dit ce qu'il a vu, il ne trompe personne, et la suite reste à écrire. Un
rapport qui cite un script absent fait une **promesse fausse** : il attribue ses
résultats à un objet vérifiable, et l'objet n'existe pas (règle d'or n°259).

Ce contrôle **refuse la seconde**, et **compte la première sans la refuser**.

CE QU'IL LIT
------------
Le texte est **aplati** avant lecture : une citation ne s'arrête pas en fin de
ligne (règle d'or n°262). Il reconnaît un nom de script cité entre accents
graves — `tests_…​.js` ou `.mjs` — et cherche le fichier dans le dossier du
rapport.

L'ÉCHAPPATOIRE, DÉCLARÉE
------------------------
Une citation **accompagnée d'un aveu** n'est pas une promesse : quand la phrase
dit que le script n'a jamais été commité, qu'il est absent ou introuvable, le
rapport est honnête et le contrôle se tait. C'est le cas des rapports corrigés
qui racontent leur propre erreur passée — sans cette échappatoire, on
signalerait précisément les fichiers qui ont dit la vérité (règle d'or n°248).

CE QU'IL NE FAIT PAS
--------------------
Il ne lance rien et ne juge aucun résultat : qu'une suite passe est l'affaire de
la suite. Il ne compte pas non plus un script vivant hors du dossier du lot —
la convention de la maison est de le livrer à côté de ce qu'il vérifie.

Usage :
    python3 _outils/controle_rapports_tests.py           # rapport complet
    python3 _outils/controle_rapports_tests.py --muet    # seulement les écarts
Sortie : 0 si aucun rapport ne cite un script absent, 1 sinon.
"""

import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

#: un script cité entre accents graves
CITATION = re.compile(r"`((?:tests?|test)[\w.\-]*\.(?:mjs|js))`")

#: un script livré à côté de ce qu'il vérifie
SCRIPT = re.compile(r"^(?:tests?_.*\.(?:mjs|js)|.*\.test\.(?:mjs|js))$", re.I)

#: une page qu'une suite pourrait conduire. Un rapport dont le dossier n'en porte
#: aucune n'est pas un lot en attente de suite : c'est un rapport d'AUDIT, qui
#: relate une mesure et non le comportement d'une page. Les compter ensemble
#: mettait en tête de file trois dossiers qu'aucune suite ne peut servir — une
#: file d'attente doit nommer ce qu'on peut réellement payer (règle n°248).
PAGE_CONDUISIBLE = re.compile(r"^(?:sequence|qcm|tp|atelier)[_-].*\.html$", re.I)

#: la phrase avoue que le script manque — la citation n'est alors pas une promesse
AVEU = re.compile(r"jamais\s+(?:été\s+)?commit|n'a\s+jamais\s+existé|n'est\s+pas\s+dans\s+le\s+dépôt"
                  r"|introuvable|absent|manquant|n'existe\s+pas|pas\s+livré", re.I)

FIN_DE_PHRASE = re.compile(r"(?<=[.!?;:])\s")


def phrase_autour(plat, debut, fin):
    """La phrase qui porte la citation, dans le texte aplati (règle n°262)."""
    gauche = max((m.end() for m in FIN_DE_PHRASE.finditer(plat, 0, debut)), default=0)
    m = FIN_DE_PHRASE.search(plat, fin)
    return plat[gauche:m.start() + 1 if m else min(len(plat), fin + 200)].strip()


def rapports(racine):
    for dossier, _, fichiers in os.walk(racine):
        if any(e in dossier for e in ECARTES):
            continue
        for f in sorted(fichiers):
            if re.match(r"rapport_tests.*\.md$", f, re.I):
                yield os.path.join(dossier, f)


def scripts_du_dossier(dossier):
    return sorted(f for f in os.listdir(dossier) if SCRIPT.match(f))


def pages_conduisibles(dossier):
    return sorted(f for f in os.listdir(dossier) if PAGE_CONDUISIBLE.match(f))


def main(muet=False):
    fantomes, dettes, audits = [], [], []
    lus = avoues = 0

    for chemin in rapports(DEPOT):
        dossier = os.path.dirname(chemin)
        nom = os.path.relpath(chemin, DEPOT)
        livres = scripts_du_dossier(dossier)
        texte = open(chemin, encoding="utf-8", errors="replace").read()
        plat = re.sub(r"\s+", " ", texte)
        coches = texte.count("✅")

        for m in CITATION.finditer(plat):
            lus += 1
            cite = m.group(1)
            if cite in livres:
                continue
            # L'aveu peut suivre la citation dans la phrase suivante — un rapport
            # écrit « Suite : `x.js` … Ce script n'a jamais été commité. » est
            # honnête. La fenêtre est déclarée : la phrase porteuse, plus les
            # 400 caractères qui la suivent.
            contexte = (phrase_autour(plat, m.start(), m.end())
                        + " " + plat[m.end():m.end() + 400])
            if AVEU.search(contexte):
                avoues += 1
                continue
            fantomes.append("%s\n     cite `%s`, absent du dossier — %d coche(s) verte(s) lui "
                            "sont attribuées" % (nom, cite, coches))

        if coches and not livres:
            if pages_conduisibles(dossier):
                dettes.append((coches, nom))
            else:
                audits.append((coches, nom))

    if not muet:
        print("%d citation(s) de script lues dans les rapports du dépôt · %d accompagnées d'un "
              "aveu (le rapport dit lui-même que le script manque)" % (lus, avoues))
        if dettes:
            total = sum(c for c, _ in dettes)
            print("\n%d LOT(S) portent des coches sans aucun script dans leur dossier — "
                  "%d coches au total.\n     Ce n'est pas une faute, c'est une dette : ils "
                  "disent ce qu'ils ont vu, et\n     leur suite reste à écrire (règle n°259). "
                  "Les plus fournis d'abord :" % (len(dettes), total))
            for c, nom in sorted(dettes, reverse=True)[:12]:
                print("     %4d ✅  %s" % (c, os.path.dirname(nom)))
        if audits:
            print("\n     (%d rapport(s) d'AUDIT écartés de cette file, %d coches : leur dossier "
                  "ne porte\n     aucune page qu'une suite pourrait conduire — ils relatent une "
                  "mesure, pas le\n     comportement d'une page. Les lister ici mettrait en tête "
                  "de file des dossiers\n     qu'aucune suite ne peut servir.)"
                  % (len(audits), sum(c for c, _ in audits)))

    if fantomes:
        print("\n⛔ %d rapport(s) attribuent leurs résultats à un script qui n'existe pas :"
              % len(fantomes))
        for f in fantomes:
            print("  " + f)
        print("\n     Un rapport peut n'avoir pas de suite — il le dit alors. Ce qu'il ne peut\n"
              "     pas faire, c'est nommer un fichier introuvable comme source de ses coches.")
        return 1
    print("\n✅ aucun rapport n'attribue ses résultats à un script absent")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
