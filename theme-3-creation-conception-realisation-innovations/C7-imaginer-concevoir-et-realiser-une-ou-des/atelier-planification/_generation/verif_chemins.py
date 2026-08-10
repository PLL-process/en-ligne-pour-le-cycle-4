# -*- coding: utf-8 -*-
"""Règle d'or n°88 — une page se juge aussi sur ce qu'on peut en faire.

On ne relit pas les liens : on les SUIT. Une page destinée aux élèves doit
pouvoir répondre à quatre questions, du point de vue de l'élève :

    comment j'arrive ici · où suis-je · comment je repars · et ensuite

Ce script contrôle les trois dernières sur les fichiers eux-mêmes. La
première — être listée dans l'index — est du ressort de `make_index.py`.

    python3 _generation/verif_chemins.py <page.html> [page.html …]

Sortie non nulle au moindre manquement : ce script refuse, il n'avertit pas.
"""
import re
import sys
from pathlib import Path

RE_NAV = re.compile(r'<nav[^>]*id="navharm".*?</nav>', re.S)
RE_HREF = re.compile(r'href="([^"#]+)')
RE_SEQ = re.compile(r'sequence_[\w.\-]+\.html$')   # les noms portent des tirets


def controler(page: Path):
    manquements = []
    html = page.read_text(encoding="utf-8")

    nav = RE_NAV.search(html)
    if not nav:
        return ["aucune barre de navigation (id=\"navharm\") — la page est une impasse"]

    liens = RE_HREF.findall(nav.group(0))
    if not liens:
        return ["barre de navigation vide"]

    morts = [h for h in liens if not (page.parent / h).resolve().exists()]
    if morts:
        manquements.append("lien(s) mort(s) dans la navigation : " + ", ".join(morts))

    if not any(h.endswith("index.html") for h in liens):
        manquements.append("aucun retour vers l'accueil")

    if not any(RE_SEQ.search(h) for h in liens):
        manquements.append("aucun retour vers une séquence — c'est ce qui distingue "
                           "une page d'une impasse")

    # « Et ensuite ? » : la suite doit être nommée quelque part dans la page.
    if not re.search(r"qcm_|Prêt&middot;e à t'entraîner|Pour t'entraîner", html):
        manquements.append("la suite n'est nommée nulle part (QCM ou activité suivante)")

    return manquements


def main(pages):
    total = 0
    for p in pages:
        p = Path(p)
        m = controler(p)
        total += len(m)
        if m:
            print("✘ %s" % p.name)
            for x in m:
                print("     %s" % x)
        else:
            print("✔ %s" % p.name)

    print("\n%d manquement(s) sur %d page(s)." % (total, len(pages)))
    print("""
PÉRIMÈTRE DE CE CONTRÔLE
  Vérifié mécaniquement : présence de la barre de navigation, existence réelle
  de chaque fichier visé, retour vers l'accueil, retour vers une séquence,
  mention de la suite.
  NON couvert : la justesse du fil d'ariane (l'atelier vient-il vraiment après
  cette activité-là), et la seule chose qui compte vraiment — un élève posé
  devant la page sait-il, sans qu'on le lui dise, d'où il vient et où il va.
  Celle-là se relève en salle.""")
    return 1 if total else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1:]))
