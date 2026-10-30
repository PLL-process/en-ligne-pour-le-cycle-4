# -*- coding: utf-8 -*-
"""Pose (ou met à jour) le moteur des chaînes pas à pas dans des pages, ou vérifie qu'il y est à jour.

    python3 poser.py <page.html> [<page.html> …]              # pose ou met à jour
    python3 poser.py --verifier <page.html> [<page.html> …]   # sortie 1 si une page porte un moteur périmé ou deux

Le bloc (style + script de `moteur_chaine.css` et `moteur_chaine.js`, ce dossier) se place juste avant `</head>`,
entre deux marqueurs « chaine-pas-a-pas … : début / fin », comme le lecteur commun (`_outils/lecteur_pas_a_pas/`).
La page garde sa déclaration (éléments, étapes) et son appel `ChainePasAPas(svg, CHAINE, {…})` : ils ne sont pas
touchés. Pilote du 30/10/2026 (5e_C4.1, la chaîne du lampadaire) : quand le moteur servira à d'autres chaînes, ce
dossier ira dans `_outils/chaine_pas_a_pas/`, avec un contrôle comme `_outils/controle_lecteur_pas_a_pas.py`.
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
VERSION = "v1"
DEBUT = "<!-- chaine-pas-a-pas %s : début — moteur des chaînes animées ; source unique : " \
        "5e_C4.1/_generation/chaine_pas_a_pas/ (poser.py). Ne pas le modifier dans la page. -->" % VERSION
FIN = "<!-- chaine-pas-a-pas %s : fin -->" % VERSION
_BLOC_RE = re.compile(r"<!-- chaine-pas-a-pas [^ ]+ : début.*?<!-- chaine-pas-a-pas [^ ]+ : fin -->", re.S)


def bloc():
    css = (ICI / "moteur_chaine.css").read_text(encoding="utf-8")
    js = (ICI / "moteur_chaine.js").read_text(encoding="utf-8")
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
    pages = [a for a in args if a != "--verifier"]
    if not pages:
        print(__doc__)
        return 2
    code = 0
    for chemin in pages:
        p = pathlib.Path(chemin)
        avant = p.read_text(encoding="utf-8")
        trouves = _BLOC_RE.findall(avant)
        if verifier:
            if len(trouves) != 1 or trouves[0] != bloc():
                print("  ✘ %s — %s" % (p, "moteur absent ou en double" if len(trouves) != 1 else "moteur différent de la source (relancer poser.py)"))
                code = 1
            else:
                print("  ✔ %s — moteur à jour" % p)
            continue
        try:
            apres = poser(avant)
        except ValueError as e:
            print("  ✘ %s — %s" % (p, e)); code = 1
            continue
        if apres != avant:
            p.write_text(apres, encoding="utf-8")
            print("  ✔ %s — moteur posé ou mis à jour" % p)
        else:
            print("  · %s — déjà à jour" % p)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
