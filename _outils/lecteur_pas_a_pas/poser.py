# -*- coding: utf-8 -*-
"""Pose (ou met à jour) le lecteur pas à pas commun dans des pages.

    python3 _outils/lecteur_pas_a_pas/poser.py <page.html> [<page.html> …]

Le bloc (style + script de `lecteur.css` et `lecteur.js`, ce dossier) se place juste avant `</head>`, entre
deux marqueurs « lecteur-pas-a-pas … : début / fin ». Une page qui le porte déjà le reçoit à jour, à la même
place ; une page qui ne le porte pas le reçoit une fois. La page garde son dessin, ses scènes et son appel
`LecteurPasAPas(bloc, {…})` : ils ne sont pas touchés.

Le contrôle `_outils/controle_lecteur_pas_a_pas.py` refuse une page dont le bloc n'est pas celui d'ici.
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
VERSION = "v1"
DEBUT = "<!-- lecteur-pas-a-pas %s : début — lecteur commun des animations pas à pas ; source unique : " \
        "_outils/lecteur_pas_a_pas/ (poser.py). Ne pas le modifier dans la page. -->" % VERSION
FIN = "<!-- lecteur-pas-a-pas %s : fin -->" % VERSION
_BLOC_RE = re.compile(r"<!-- lecteur-pas-a-pas [^ ]+ : début.*?<!-- lecteur-pas-a-pas [^ ]+ : fin -->", re.S)


def bloc():
    css = (ICI / "lecteur.css").read_text(encoding="utf-8")
    js = (ICI / "lecteur.js").read_text(encoding="utf-8")
    return DEBUT + "\n<style>\n" + css + "</style>\n<script>\n" + js + "</script>\n" + FIN


def blocs_de(html):
    return _BLOC_RE.findall(html)


def poser(html):
    """Rend la page avec le bloc à jour, ou lève ValueError (deux blocs, pas de </head>)."""
    b = bloc()
    trouves = blocs_de(html)
    if len(trouves) > 1:
        raise ValueError("%d blocs du lecteur dans la page" % len(trouves))
    if trouves:
        return _BLOC_RE.sub(lambda _m: b, html, count=1)
    if html.count("</head>") != 1:
        raise ValueError("pas de </head> unique où poser le lecteur")
    return html.replace("</head>", b + "\n</head>", 1)


def main(args):
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
        if apres != avant:
            p.write_text(apres, encoding="utf-8")
            print("  ✔ %s — lecteur posé ou mis à jour" % p)
        else:
            print("  · %s — déjà à jour" % p)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
