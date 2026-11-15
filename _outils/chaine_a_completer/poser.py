# -*- coding: utf-8 -*-
"""Pose (ou met à jour) la chaîne à compléter commune dans des pages.

    python3 _outils/chaine_a_completer/poser.py <page.html> [<page.html> …]

Le bloc (style + script de `chaine.css` et `chaine.js`, ce dossier) se place juste avant `</head>`, entre deux
marqueurs « chaine-a-completer … : début / fin ». Une page qui le porte déjà le reçoit à jour, à la même place ;
une page qui ne le porte pas le reçoit une fois. La page garde son dessin (`window.CAC_DESSINS`) et ses étapes
(`div.cac[data-cac]`) : ils ne sont pas touchés.

Le contrôle `_outils/controle_chaine_a_completer.py` refuse une page dont le bloc n'est pas celui d'ici.
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
VERSION = "v1"
DEBUT = "<!-- chaine-a-completer %s : début — les étiquettes posées dans le schéma des chaînes ; source unique : " \
        "_outils/chaine_a_completer/ (poser.py). Ne pas le modifier dans la page. -->" % VERSION
FIN = "<!-- chaine-a-completer %s : fin -->" % VERSION
_BLOC_RE = re.compile(r"<!-- chaine-a-completer [^ ]+ : début.*?<!-- chaine-a-completer [^ ]+ : fin -->", re.S)


def bloc():
    css = (ICI / "chaine.css").read_text(encoding="utf-8")
    js = (ICI / "chaine.js").read_text(encoding="utf-8")
    return DEBUT + "\n<style>\n" + css + "</style>\n<script>\n" + js + "</script>\n" + FIN


def blocs_de(html):
    return _BLOC_RE.findall(html)


def poser(html):
    """Rend la page avec le bloc à jour, ou lève ValueError (deux blocs, pas de </head>)."""
    b = bloc()
    trouves = blocs_de(html)
    if len(trouves) > 1:
        raise ValueError("%d blocs de la chaîne à compléter dans la page" % len(trouves))
    if trouves:
        return _BLOC_RE.sub(lambda _m: b, html, count=1)
    if html.count("</head>") != 1:
        raise ValueError("pas de </head> unique où poser la chaîne à compléter")
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
            print("  ✔ %s — chaîne à compléter posée ou mise à jour" % p)
        else:
            print("  · %s — déjà à jour" % p)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
