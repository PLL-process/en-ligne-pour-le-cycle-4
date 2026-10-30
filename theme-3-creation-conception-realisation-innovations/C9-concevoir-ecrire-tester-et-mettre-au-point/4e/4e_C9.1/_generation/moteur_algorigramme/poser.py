# -*- coding: utf-8 -*-
"""Pose (ou met à jour) le moteur des algorigrammes et chronogrammes animés dans des pages.

    python3 poser.py <page.html> [<page.html> …]
    python3 poser.py --verifier <page.html> [<page.html> …]   # sortie 1 si une page porte un bloc différent

Le bloc (style + script de `moteur.css` et `moteur.js`, ce dossier) se place juste avant `</head>`, entre deux
marqueurs « moteur-algorigramme … : début / fin ». Une page qui le porte déjà le reçoit à jour, à la même place ;
une page qui ne le porte pas le reçoit une fois. La page garde son dessin, ses déclarations (blocs, flèches,
variantes, série, chronogramme) et son appel `MoteurAlgorigramme({…})` : ils ne sont pas touchés.

Pilote : 4e_C9.1, la pompe qui s'affole (30/10/2026). Quand un deuxième lot s'en servira, ce dossier ira dans
`_outils/moteur_algorigramme/`, avec un contrôle sur le modèle de `_outils/controle_lecteur_pas_a_pas.py`.
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
VERSION = "v1"
DEBUT = "<!-- moteur-algorigramme %s : début — algorigrammes et chronogrammes animés ; source unique : " \
        "4e_C9.1/_generation/moteur_algorigramme/ (poser.py). Ne pas le modifier dans la page. -->" % VERSION
FIN = "<!-- moteur-algorigramme %s : fin -->" % VERSION
_BLOC_RE = re.compile(r"<!-- moteur-algorigramme [^ ]+ : début.*?<!-- moteur-algorigramme [^ ]+ : fin -->", re.S)


def bloc():
    css = (ICI / "moteur.css").read_text(encoding="utf-8")
    js = (ICI / "moteur.js").read_text(encoding="utf-8")
    return DEBUT + "\n<style>\n" + css + "</style>\n<script>\n" + js + "</script>\n" + FIN


def poser(html):
    """Rend la page avec le bloc à jour, ou lève ValueError (deux blocs, pas de </head>)."""
    b = bloc()
    trouves = _BLOC_RE.findall(html)
    if len(trouves) > 1:
        raise ValueError("%d blocs du moteur dans la page" % len(trouves))
    if trouves:
        return _BLOC_RE.sub(lambda _m: b, html, count=1)
    if html.count("</head>") != 1:
        raise ValueError("pas de </head> unique où poser le moteur")
    return html.replace("</head>", b + "\n</head>", 1)


def main(args):
    verifier = "--verifier" in args
    args = [a for a in args if a != "--verifier"]
    if not args:
        print(__doc__)
        return 2
    code = 0
    for chemin in args:
        p = pathlib.Path(chemin)
        avant = p.read_text(encoding="utf-8")
        try:
            apres = poser(avant)
        except ValueError as e:
            print("  ✘ %s — %s" % (p, e)); code = 1
            continue
        if apres == avant:
            print("  · %s — déjà à jour" % p)
        elif verifier:
            print("  ✘ %s — le bloc du moteur n'est pas celui de la source (relancer poser.py)" % p); code = 1
        else:
            p.write_text(apres, encoding="utf-8")
            print("  ✔ %s — moteur posé ou mis à jour" % p)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
