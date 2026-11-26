# -*- coding: utf-8 -*-
"""Pose (ou met à jour) le mode lecture — une partie par écran — dans des pages.

    python3 _outils/mode_lecture/poser.py <page.html> [<page.html> …]
    python3 _outils/mode_lecture/poser.py --verifier <page.html> […]     # ne rien écrire : le bloc est-il à jour ?

Le bloc (style + script de `lecture.css` et `lecture.js`, ce dossier) se place juste avant `</head>`, entre deux
marqueurs « mode-lecture … : début / fin » — comme le mode mission (`_outils/mode_mission/poser.py`) et la fiche
papier. Une page qui le porte déjà le reçoit à jour, à la même place. Rien d'autre dans la page n'est touché, et le
bloc ne porte aucune donnée propre à la page : ses parties sont lues dans la page elle-même.

Le mode lecture est allumé d'emblée pour l'élève ; un robot de test (`navigator.webdriver`) ouvre la page complète,
qui se mesure, se teste et s'imprime comme avant. Un générateur de pages l'appelle par `poser(html)`
(`_outils/generer_lexique.py`).
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
VERSION = "v1"
DEBUT = "<!-- mode-lecture %s : début — une partie par écran ; source unique : " \
        "_outils/mode_lecture/ (poser.py). Ne pas le modifier dans la page. -->" % VERSION
FIN = "<!-- mode-lecture %s : fin -->" % VERSION
_BLOC_RE = re.compile(r"<!-- mode-lecture [^ ]+ : début.*?<!-- mode-lecture [^ ]+ : fin -->", re.S)


def bloc():
    css = (ICI / "lecture.css").read_text(encoding="utf-8")
    js = (ICI / "lecture.js").read_text(encoding="utf-8")
    return DEBUT + "\n<style>\n" + css + "</style>\n<script>\n" + js + "</script>\n" + FIN


def blocs_de(html):
    return _BLOC_RE.findall(html)


def poser(html):
    """Rend la page avec le bloc à jour, ou lève ValueError (deux blocs, ou aucune place unique où le poser)."""
    b = bloc()
    trouves = blocs_de(html)
    if len(trouves) > 1:
        raise ValueError("%d blocs du mode lecture dans la page" % len(trouves))
    if trouves:
        return _BLOC_RE.sub(lambda _m: b, html, count=1)
    if html.count("</head>") == 1:
        return html.replace("</head>", b + "\n</head>", 1)
    corps = re.findall(r"<body[\s>]", html)
    if html.count("</head>") == 0 and len(corps) == 1:        # page engendrée sans </head> : juste avant <body>, comme la fiche papier
        return html.replace(corps[0], b + "\n" + corps[0], 1)
    raise ValueError("ni </head> unique, ni (sans </head>) <body> unique, où poser le mode lecture")


def main(args):
    verifier = "--verifier" in args
    pages = [a for a in args if not a.startswith("--")]
    if not pages:
        print(__doc__)
        return 2
    code = 0
    for chemin in pages:
        p = pathlib.Path(chemin)
        html = p.read_text(encoding="utf-8")
        try:
            neuf = poser(html)
        except ValueError as e:
            print("✘ %s : %s" % (chemin, e))
            code = 1
            continue
        if verifier:
            if not blocs_de(html):
                print("· %s : sans mode lecture" % chemin)
            elif neuf != html:
                print("✘ %s : bloc différent de la source (relancer poser.py)" % chemin)
                code = 1
            else:
                print("✅ %s : à jour" % chemin)
        elif neuf != html:
            p.write_text(neuf, encoding="utf-8")
            print("✎ %s : mode lecture %s" % (chemin, "mis à jour" if blocs_de(html) else "posé"))
        else:
            print("· %s : déjà à jour" % chemin)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
