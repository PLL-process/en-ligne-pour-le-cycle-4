# -*- coding: utf-8 -*-
"""controle_cadres.py — aucun <iframe> vers fr.vittascience.com : le site refuse d'être encadré.

LE CONSTAT
----------
Mesuré les 12 et 13/09/2026 : fr.vittascience.com répond « X-Frame-Options: SAMEORIGIN »
sur /python/, sur /arduino/ et sur son propre code d'intégration « ?link=…&embed=1 ».
Seize cadres, huit pages, un gabarit : aucun ne s'affichait, ni en local ni sur le site
publié — et treize portaient la phrase « si le cadre reste blanc, c'est la connexion, pas
ton ordinateur », fausse : le cadre reste blanc AVEC la connexion. Depuis l'étape 0 de la
vague 2, l'éditeur s'ouvre par un lien-bouton dans un nouvel onglet ; ce contrôle empêche
le retour du cadre.

Usage : python3 _outils/controle_cadres.py [--muet]
Sortie : 0 aucun cadre · 1 des cadres · 2 le contrôle n'a rien pu lire (règle n°299).
"""
import glob, os, re, sys

import panne

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)
CADRE = re.compile(r"<iframe\b[^>]*\bsrc=[\"']https?://fr\.vittascience\.com", re.I)


def pages(racine):
    """Les pages effectivement ouvertes — hors archive, qui est une trace."""
    return [f for f in sorted(glob.glob(os.path.join(racine, "**", "*.html"), recursive=True))
            if not any(e in f for e in ECARTES)]


def cadres(racine):
    for f in pages(racine):
        n = len(CADRE.findall(open(f, encoding="utf-8", errors="replace").read()))
        if n:
            yield os.path.relpath(f, racine).replace(os.sep, "/"), n


def main(muet=False):
    # Règle d'or n°299 : avant tout verdict, dire ce qu'on a ouvert. Recopié
    # dans une racine vide, ce contrôle écrivait « ✅ aucun cadre <iframe> » et
    # sortait à 0 — un succès franc sur un dépôt qu'il n'avait pas lu.
    lues = pages(DEPOT)
    if not lues:
        return panne.rien_vu("aucune page .html sous %s" % DEPOT)

    fautifs = list(cadres(DEPOT))
    if fautifs:
        print("⛔ %d cadre(s) <iframe> vers fr.vittascience.com dans %d page(s) — le site refuse "
              "d'être encadré (X-Frame-Options: SAMEORIGIN) ; remplace-les par le lien-bouton du "
              "gabarit _outils/gabarits/vittascience_embed.html :" % (sum(n for _, n in fautifs), len(fautifs)))
        for f, n in fautifs:
            print("  %s  (%d)" % (f, n))
        return 1
    if not muet:
        print("%d page(s) lues · ✅ aucun cadre <iframe> vers fr.vittascience.com "
              "hors archive" % len(lues))
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
