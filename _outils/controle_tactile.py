#!/usr/bin/env python3
"""controle_tactile.py — les pages se touchent du doigt sans gêne (06/11/2026).

Pascal, le 06/11/2026, après l'essai des skills `mobile-native` (Emil Kowalski) et `audit` (Impeccable) sur 4e_C9.1 :
« corriger le P1 sur tout le site (zoom iOS) … oui ». Deux règles, vérifiées dans le texte des pages :

1. ZOOM iOS. Sur iPhone et iPad, un champ écrit en moins de 16 px fait zoomer la page dès qu'on le touche, et elle ne
   dézoome pas. Toute page qui a un champ (input, textarea, select) porte donc, dans une feuille de style ordinaire
   (pas sous <noscript>, pas réservée à l'impression), la règle :
       @media (pointer:coarse){input,textarea,select{font-size:16px!important}}
   Les gabarits qui fabriquent des pages (dnb_gabarit.html, gabarit_qcm.tpl, gabarit_style.css, kit.css) la portent
   aussi, pour qu'une page régénérée la garde.
2. LIEN D'ÉVITEMENT. Quand une page a un lien « Aller au contenu » (.skip-link), c'est le premier lien du corps de la
   page, hors de la barre de navigation : au clavier, c'est le premier arrêt.

Usage : python3 _outils/controle_tactile.py        Sortie 1 s'il y a un écart.
La mesure dans un navigateur (champs à 16 px, aucun défilement de côté à 390 px au toucher) est dans le journal.
"""
import glob
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARQUE = "@media (pointer:coarse){input,textarea,select{font-size:16px!important}}"
GABARITS = ["_outils/dnb_gabarit.html",
            "theme-1-objets-systemes-usages-interactions/ateliers-representations/_generation/gabarit_qcm.tpl",
            "theme-1-objets-systemes-usages-interactions/ateliers-representations/_generation/kit.css"]


def regle_active(s):
    """la règle est dans une feuille ordinaire : ni sous <noscript>, ni dans un <style media=…>"""
    for m in re.finditer(r"<style(\s[^>]*)?>(.*?)</style>", s, re.S):
        if m.group(1) and "media=" in m.group(1):
            continue
        if s.rfind("<noscript", 0, m.start()) > s.rfind("</noscript>", 0, m.start()):
            continue
        if MARQUE in m.group(2):
            return True
    return False


def main():
    os.chdir(DEPOT)
    ecarts, n_champs, n_saut = [], 0, 0
    pages = [p for p in glob.glob("**/*.html", recursive=True)
             if not p.startswith(("node_modules", "_archive")) and "/_archive" not in p and p != "_outils/dnb_gabarit.html"]
    for p in sorted(pages):
        s = open(p, encoding="utf-8", errors="ignore").read()
        if re.search(r"<(input|select|textarea)\b", s):
            n_champs += 1
            if not regle_active(s):
                ecarts.append("zoom iOS · " + p + " : un champ, mais pas la règle des 16 px au toucher")
        if 'class="skip-link"' in s:
            n_saut += 1
            corps = s[s.find("<body"):]
            premier = re.search(r"<a\b[^>]*>", corps)
            nav = re.search(r"<nav\b.*?</nav>", corps, re.S)
            if not premier or "skip-link" not in premier.group(0) or (nav and "skip-link" in nav.group(0)):
                ecarts.append("clavier · " + p + " : « Aller au contenu » n'est pas le premier lien de la page")
    gabarits = GABARITS + glob.glob("theme-*/**/_generation/gabarit_style.css", recursive=True)
    for g in gabarits:
        if os.path.exists(g) and MARQUE not in open(g, encoding="utf-8").read():
            ecarts.append("gabarit · " + g + " : la règle des 16 px au toucher manque")
    for e in ecarts:
        print("✘ " + e)
    if ecarts:
        print("✘ %d écart(s) : %d pages à champs, %d pages à lien d'évitement, %d gabarits" % (len(ecarts), n_champs, n_saut, len(gabarits)))
        return 1
    print("✅ chaque champ passe à 16 px au toucher (%d pages, %d gabarits) ; « Aller au contenu » est le premier lien (%d pages)"
          % (n_champs, len(gabarits), n_saut))
    return 0


if __name__ == "__main__":
    sys.exit(main())
