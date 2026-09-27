# -*- coding: utf-8 -*-
"""controle_debordement.py — règle d'or n°135, second passage : le filet mobile mécanisé.

LE CONSTAT
----------
La n°135 (26/08/2026) a posé un filet CSS — un tableau devient défilable horizontalement
sous un point de rupture mobile plutôt que d'écraser la page — sur environ 44 séquences,
à la main, avec trois sélecteurs précis (`section.card table`, `table.refs`, `table.recette`).
Elle n'a jamais été mécanisée : rien ne vérifiait qu'un tableau NOUVEAU, ou d'une classe
différente (`voc`, `competences`, `comparatif`…), ou sans classe du tout, recevait le même
traitement. Le 27/09/2026, pendant l'audit factuel qui a suivi la correction du TP du dé
(#449), Pascal a demandé « qu'est-ce qui est mieux ? » à propos d'un tableau resté exposé —
la réponse (le filet suffit partout où les colonnes portent des valeurs parallèles ; les
cartes ne se justifient que si une colonne porte une idée à elle seule, ce que n°135
documentait déjà) a aussi révélé l'ampleur du trou : sur les 145 pages élève, 67 portaient
au moins un tableau de 3 colonnes ou plus sans la moindre protection — le corpus avait
grandi, la règle n'avait pas suivi.

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Mêmes pages que controle_hierarchie.py (règle n°307) : séquences (sequence_*, sequence-*),
TP, ateliers, activités, entraînements, fiches de TP, pages Vittascience, synthèses élève.
Hors archive. Déclaré ici à nouveau, pas importé : un contrôle qui renvoie à un autre pour
dire ce qu'il regarde oblige à ouvrir deux fichiers pour répondre à une question simple.

MESURÉ, donc établi
--------------------
Une page qui contient au moins un `<table>` d'au moins TABLE_COLONNES (3) colonnes doit
porter, dans son CSS (un ou plusieurs `<style>`), une règle qui rend un tableau défilable
horizontalement sous un point de rupture mobile : `overflow-x:auto` dans un bloc
`@media (max-width: …px)`. Le sélecteur précis n'est PAS vérifié — `table`, `.voc`,
`section.card table` comptent également — parce que l'usage du dépôt est un filet unique
par page qui couvre tous ses tableaux, jamais un filet par classe. Un tableau ≥3 colonnes
sans un tel bloc nulle part sur sa page est un écart.

NON mesuré, donc NON couvert, et à juger à l'œil : si une colonne mérite en réalité une
carte plutôt qu'une position dans un tableau (n°135 documente le critère : « quand chaque
colonne porte une idée ») ; le rendu réel dans un navigateur — ce contrôle lit le CSS
textuellement, il ne fait tourner aucun moteur de rendu.

Usage : python3 _outils/controle_debordement.py [--muet] [--json] [chemin…]
Sortie : 0 rien à reprendre · 1 au moins un écart · 2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import json
import os
import re
import sys

from bs4 import BeautifulSoup

import panne

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)
MOTIFS = ("sequence_", "sequence-", "sequence.html", "tp_", "atelier", "activite",
          "entrainement", "fiche_maths", "vittascience", "synthese_eleve")

TABLE_COLONNES = 3

# Un bloc @media(max-width:…) contenant une règle overflow-x:auto quelque part : un seul
# niveau d'accolades imbriquées suffit à couvrir le CSS réellement écrit dans ce dépôt
# (un @media contient des sélecteurs plats, jamais de règle imbriquée plus profond).
RE_MEDIA_MOBILE = re.compile(r'@media[^{]*max-width\s*:\s*\d+px[^{]*\{((?:[^{}]*\{[^{}]*\})*[^{}]*)\}',
                              re.S | re.I)
RE_OVERFLOW = re.compile(r'overflow-x\s*:\s*auto', re.I)


def texte(el) -> str:
    return " ".join(el.get_text(" ").split())


def a_filet_mobile(style_text: str) -> bool:
    return any(RE_OVERFLOW.search(bloc.group(1)) for bloc in RE_MEDIA_MOBILE.finditer(style_text))


def colonnes(table) -> int:
    return max((len(tr.find_all(["th", "td"])) for tr in table.find_all("tr")), default=0)


def analyser(chemin: str) -> list:
    soupe = BeautifulSoup(open(chemin, encoding="utf-8", errors="replace").read(), "lxml")
    style_text = " ".join(s.get_text() for s in soupe.find_all("style"))
    if a_filet_mobile(style_text):
        return []
    ecarts = []
    for t in soupe.find_all("table"):
        n = colonnes(t)
        if n < TABLE_COLONNES:
            continue
        classes = t.get("class") or []
        entete = t.find_previous(["h1", "h2", "h3", "h4", "summary"])
        premiere = t.find("tr")
        ecarts.append({"colonnes": n, "classe": " ".join(classes) or "(sans classe)",
                       "sous": texte(entete)[:60] if entete else "",
                       "debut": texte(premiere)[:90] if premiere else ""})
    return ecarts


def pages(racines):
    vues = set()
    for racine in racines:
        if os.path.isfile(racine):
            vues.add(os.path.abspath(racine))
            continue
        for dossier, _, fichiers in os.walk(racine):
            if any(e in dossier for e in ECARTES) or "/." in dossier.replace(os.sep, "/"):
                continue
            rel = os.path.relpath(dossier, DEPOT).replace(os.sep, "/")
            if not rel.startswith("theme-"):
                continue
            for f in fichiers:
                if f.endswith(".html") and f.startswith(MOTIFS):
                    vues.add(os.path.join(dossier, f))
    return sorted(vues)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    muet, en_json = "--muet" in argv, "--json" in argv
    cibles = [a for a in argv if not a.startswith("--")] or [DEPOT]
    lues = pages([os.path.abspath(c) for c in cibles])
    if not lues:
        return panne.rien_vu("aucune page élève (séquence, TP, atelier, synthèse élève…) sous %s"
                             % " · ".join(cibles))
    rapport = {os.path.relpath(f, DEPOT).replace(os.sep, "/"): analyser(f) for f in lues}
    total_pages = sum(1 for r in rapport.values() if r)
    total_tables = sum(len(r) for r in rapport.values())
    if en_json:
        print(json.dumps({"pages": len(lues), "pages_en_ecart": total_pages,
                          "tableaux_en_ecart": total_tables, "detail": rapport},
                         ensure_ascii=False, indent=1))
        return 1 if total_tables else 0
    for f, ecarts in rapport.items():
        if ecarts:
            print("\n── %s" % f)
            for e in ecarts:
                print("   ✘ tableau %d colonnes, classe %-14s · « %s… » (sous « %s »)"
                      % (e["colonnes"], e["classe"], e["debut"], e["sous"]))
    if total_tables:
        print("\n%d page(s) lues · %d page(s) en écart · %d tableau(x) sans filet mobile"
              % (len(lues), total_pages, total_tables))
        return 1
    if not muet:
        print("%d page(s) lues · ✅ aucun tableau de %d colonnes ou plus sans filet mobile"
              % (len(lues), TABLE_COLONNES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
