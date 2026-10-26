# -*- coding: utf-8 -*-
"""Pose (ou met à jour) la fiche papier dans des pages.

    python3 _outils/impression_papier/poser.py <page.html> [<page.html> …]

Le bloc (style + script de `papier.css` et `papier.js`, ce dossier) se place juste avant `</head>` — ou, dans
une page qui omet la balise `</head>` (permis en HTML : les quatre pages engendrées de la station 3e_C9.2),
juste avant `<body>`, là où la tête finit —, entre deux marqueurs « fiche-papier … : début / fin ». Jamais en fin
de page : `controle_regle4.py` situe le bouton QCM à sa place dans le source, et 19 Ko ajoutés après lui le
décaleraient (constaté le 25/10/2026 sur la page 4 de la station). Une page qui le porte déjà le reçoit à jour, à la même
place ; une page qui ne le porte pas le reçoit une fois. Rien d'autre dans la page n'est touché : le bloc
n'agit qu'à l'impression (et ajoute, cachés à l'écran, les éléments que le papier remplace).

Le contrôle `_outils/controle_impression_papier.py` refuse une séquence sans le bloc, ou dont le bloc n'est pas celui d'ici.
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
VERSION = "v1"
DEBUT = "<!-- fiche-papier %s : début — la séquence imprimée en fiche d'élève ; source unique : " \
        "_outils/impression_papier/ (poser.py). Ne pas le modifier dans la page. -->" % VERSION
FIN = "<!-- fiche-papier %s : fin -->" % VERSION
_BLOC_RE = re.compile(r"<!-- fiche-papier [^ ]+ : début.*?<!-- fiche-papier [^ ]+ : fin -->", re.S)


def bloc():
    css = (ICI / "papier.css").read_text(encoding="utf-8")
    js = (ICI / "papier.js").read_text(encoding="utf-8")
    return DEBUT + "\n<style>\n" + css + "</style>\n<script>\n" + js + "</script>\n" + FIN


def blocs_de(html):
    return _BLOC_RE.findall(html)


def poser(html):
    """Rend la page avec le bloc à jour, ou lève ValueError (deux blocs, ou aucune place unique où le poser)."""
    b = bloc()
    trouves = blocs_de(html)
    if len(trouves) > 1:
        raise ValueError("%d blocs de la fiche papier dans la page" % len(trouves))
    if trouves:
        return _BLOC_RE.sub(lambda _m: b, html, count=1)
    if html.count("</head>") == 1:
        return html.replace("</head>", b + "\n</head>", 1)
    corps = re.findall(r"<body[\s>]", html)
    if html.count("</head>") == 0 and len(corps) == 1:
        return html.replace(corps[0], b + "\n" + corps[0], 1)
    raise ValueError("ni </head> unique, ni (sans </head>) <body> unique, où poser la fiche papier")


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
            print("  ✔ %s — fiche papier posée ou mise à jour" % p)
        else:
            print("  · %s — déjà à jour" % p)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
