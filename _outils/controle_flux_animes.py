#!/usr/bin/env python3
"""controle_flux_animes.py — chaque chaîne d'énergie ou d'information du site a ses flux animés (15/11/2026).

Demande de Pascal du 15/11/2026 : « les chaînes d'énergie et chaîne d'information devront être animées (tous les flux) ».
Lit chaque SVG et chaque page des trois thèmes qui dessine une chaîne (un nom de fonction et au moins une flèche) et
signale celles dont les flèches n'ont pas leurs perles animées (`_outils/animer_flux.py`, qui les pose).
Les chaînes à compléter (`_outils/chaine_a_completer/`) dessinent les leurs au chargement : `controle_chaine_a_completer.py`
vérifie qu'elles portent l'outil à jour.

Usage : python3 _outils/controle_flux_animes.py [fichier…]
Sortie : 0 tout est animé · 1 une chaîne au moins ne l'est pas (nommée) · 2 rien n'a pu être lu (règle d'or n°299).
"""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import animer_flux  # noqa: E402

RACINE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def fichiers():
    out = []
    for motif in ("theme-*/**/*.svg", "theme-*/**/*.html"):
        for f in glob.glob(os.path.join(RACINE, motif), recursive=True):
            if "_archive" in f or os.sep + "node_modules" + os.sep in f:
                continue
            out.append(f)
    return sorted(out)


def main(argv):
    liste = [a for a in argv if not a.startswith("--")] or fichiers()
    lus = chaines = 0
    ecarts = []
    for f in liste:
        try:
            texte = open(f, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        lus += 1
        if not animer_flux.FONCTIONS.search(texte):
            continue
        chaines += 1
        reste = animer_flux.a_animer(texte, f.endswith(".html"))
        if reste:
            ecarts.append((os.path.relpath(f, RACINE), reste))
    if not lus:
        print("✘ rien n'a pu être lu")
        return 2
    for f, n in ecarts:
        print("✘ %s : %d chaîne(s) aux flux fixes — python3 _outils/animer_flux.py %s --ecrire" % (f, n, f))
    print("%d fichier(s) lus, %d portent un nom de fonction · %s" % (
        lus, chaines, "✅ chaque chaîne a ses flux animés" if not ecarts else "✘ %d fichier(s) aux flux fixes" % len(ecarts)))
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
