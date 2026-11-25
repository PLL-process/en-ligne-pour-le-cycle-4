# -*- coding: utf-8 -*-
"""poser.py — le banc-eleve (règle d'or n°333) : une source unique, recopiée à l'identique dans chaque page qui s'en sert.

Le banc-eleve juge le programme que l'élève écrit dans l'éditeur Python de la page en l'EXÉCUTANT sur des entrées
choisies (`_outils/banc_eleve/LISEZMOI.md`). Son cœur est le même partout ; seule la table `BANC_ELEVE` (les essais et
leurs attendus) est propre à chaque page, et vit HORS des marques.

  python3 _outils/banc_eleve/poser.py <page.html> …    remet le cœur et le style de la source dans ces pages
  python3 _outils/banc_eleve/poser.py --verifier-tout  chaque page qui porte le banc en porte la version de la source

Sortie : 0 toutes les copies sont identiques à la source · 1 une copie diffère (ou une page n'a pas de style) ·
2 EN PANNE : aucune page ne porte le banc (n°299).
"""
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
THEMES = ("theme-1-objets-systemes-usages-interactions", "theme-2-structure-fonctionnement-comportement",
          "theme-3-creation-conception-realisation-innovations")
SOURCE = os.path.join(ICI, "banc_eleve.js")
STYLE = os.path.join(ICI, "banc_eleve.css")
BLOC = re.compile(r"/\* banc-eleve v[\d.]+ : début.*?/\* banc-eleve v[\d.]+ : fin \*/\n", re.S)
STYLE_BLOC = re.compile(r"<style>/\* banc-eleve \(règle d'or n°333.*?</style>\n", re.S)


def source():
    return open(SOURCE, encoding="utf-8").read(), "<style>" + open(STYLE, encoding="utf-8").read() + "</style>\n"


def etat(texte, js, css):
    """'absent' · 'identique' · 'différent' (le cœur ou le style ne sont pas ceux de la source)."""
    blocs = BLOC.findall(texte)
    if not blocs:
        return "absent"
    return "identique" if blocs == [js] and STYLE_BLOC.findall(texte) == [css] else "différent"


def remettre(texte, js, css):
    texte = BLOC.sub(lambda m: js, texte, count=1)
    if STYLE_BLOC.search(texte):
        texte = STYLE_BLOC.sub(lambda m: css, texte, count=1)
    else:
        texte = texte.replace("</head>", css + "</head>", 1)
    return texte


def pages():
    for t in THEMES:
        for d, sous, fichiers in os.walk(os.path.join(RACINE, t)):
            sous[:] = [s for s in sous if not s.startswith("_") and s not in (".git", "node_modules")]
            for f in sorted(fichiers):
                if f.endswith(".html"):
                    yield os.path.join(d, f)


def main(argv):
    js, css = source()
    if "--verifier-tout" in argv:
        n, faux = 0, []
        for p in pages():
            e = etat(open(p, encoding="utf-8").read(), js, css)
            if e == "absent":
                continue
            n += 1
            if e != "identique":
                faux.append(os.path.relpath(p, RACINE))
        print("banc-eleve (n°333) — %d page(s) le portent, %d identique(s) à la source" % (n, n - len(faux)))
        for f in faux:
            print("  ✘ %s : le cœur ou le style diffère de _outils/banc_eleve/ — relancer poser.py sur cette page" % f)
        if not n:
            print("✘ EN PANNE : aucune page ne porte le banc-eleve — ce contrôle n'a rien vérifié (n°299).")
            return 2
        return 1 if faux else 0
    chemins = [a for a in argv if not a.startswith("--")]
    if not chemins:
        print(__doc__)
        return 2
    for p in chemins:
        t = open(p, encoding="utf-8").read()
        if etat(t, js, css) == "absent":
            print("○ %s : pas de marque « banc-eleve v1 : début » — à poser à la main avec sa table BANC_ELEVE" % p)
            continue
        open(p, "w", encoding="utf-8").write(remettre(t, js, css))
        print("✅ %s" % p)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
