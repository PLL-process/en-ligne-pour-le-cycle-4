# -*- coding: utf-8 -*-
"""controle_hierarchie.py — règle d'or n°307 : la hiérarchie se voit avant de se lire.

LE CONSTAT
----------
Le 27/09/2026, Pascal : « il y a dans mes séquences de gros blocs qui mériteraient d'être
hiérarchisés ». La n°33 (aérer : une idée, un bloc ; une liste, des lignes) est mécanisée
depuis juillet, mais elle ne regarde qu'UN paragraphe à la fois — un <p> de plus de 110 mots.
Elle ne voit ni la liste écrite en ligne dans un paragraphe court, ni la suite de paragraphes
courts dont aucun ne porte de repère, ni la cellule de tableau qui devient un pavé sur un
téléphone. Ce contrôle mesure ce que la n°33 ne mesure pas : la hiérarchie VISIBLE d'un bloc,
ce que l'œil attrape avant de lire.

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Pages lues : les pages que lit un élève — séquences (sequence_*, sequence-*), TP, ateliers,
activités, entraînements, fiches de TP, pages Vittascience, synthèses élève. Hors archive.
Texte visible seulement : ni script, ni style, ni commentaire, ni <template>.

Mesuré, donc établi :
  H1  énumération en ligne — un paragraphe ou un item porte au moins trois entrées numérotées
      (①②③, « 1. 2. 3. », « 1) 2) 3) », « a) b) c) ») dont au moins deux commencent au milieu
      d'une ligne. Une entrée par ligne (n°33, second volet ; n°97 pour les corrections).
      Écartée : la chaîne fléchée « capteur (1) → carte (2) → écran (3) », où le numéro suit
      son mot et précède une flèche — elle se lit comme un schéma, pas comme une liste.
  H2  mur sans repère — au moins trois paragraphes consécutifs d'un même bloc, 170 mots ou
      plus au total, dont AUCUN ne s'ouvre sur un repère : un gras dans les trois premiers mots,
      un encadré typé (paragraphe porteur d'une classe : retenir, piege, note…) ou un champ
      de réponse (une question qui porte son choix se voit à son contrôle).
  H3  paragraphe tout en gras — plus de 40 mots dont plus de 60 % en gras : quand tout est
      appuyé, plus rien ne l'est. En deçà, c'est la phrase-clé qu'on veut voir : elle reste.
  H4  cellule-pavé — une ligne de cellule de tableau de plus de 50 mots : sur un téléphone, le
      tableau se lit colonne par colonne, et la cellule devient un mur étroit. Une cellule déjà
      découpée en lignes (<br>, paragraphes, items) est jugée à sa plus longue ligne.
  H5  item-pavé — un item de liste dont le texte de tête (hors sous-blocs typés, sous-listes,
      figures et volets) a une ligne de plus de 60 mots sans s'ouvrir sur un gras, ou de plus
      de 100 mots même avec : le gras de tête laisse l'œil parcourir les items, il ne rend pas
      un item court.
  H6  pavé hors séquence — un paragraphe de plus de 110 mots (seuil de la n°33) sur une page
      que verif_regles_audit.py ne lit pas : TP, ateliers, fiches, synthèses élève. Sur les
      séquences, c'est la n°33 de verif_regles_audit.py qui le compte : pas deux fois.

NON mesuré, donc NON couvert, et à juger à l'œil : la pertinence d'un intertitre, l'ordre des
idées dans un bloc, le choix de ce qui mérite le gras.

Usage : python3 _outils/controle_hierarchie.py [--muet] [--json] [chemin…]
Sortie : 0 rien à reprendre · 1 au moins un écart · 2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import json
import os
import re
import sys

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

import panne

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)
MOTIFS = ("sequence_", "sequence-", "sequence.html", "tp_", "atelier", "activite",
          "entrainement", "fiche_maths", "vittascience", "synthese_eleve")

MUR_MOTS, MUR_PARAS = 170, 3
GRAS_MOTS, GRAS_PART = 40, 0.60
CELLULE_MOTS = 50
ITEM_MOTS, ITEM_MOTS_ANCRE = 60, 100
PAVE_MOTS = 110                      # seuil de la n°33 (verif_regles_audit.SEUIL_PAVE_MOTS)
SEQUENCE = ("sequence_", "sequence-", "sequence.html")   # pages lues par verif_regles_audit

# Un marqueur d'entrée : il PRÉCÈDE son contenu (espace puis autre chose qu'une flèche).
_SUITE = r"(?=\s+[^\s→⟶➜])"
FAMILLES = {
    "①②③": [re.compile(c) for c in "①②③④⑤⑥⑦⑧⑨"],
    "1. 2. 3.": [re.compile(r"(?:(?<=^)|(?<=[\s:;(«]))%d\.%s" % (i, _SUITE)) for i in range(1, 10)],
    "1) 2) 3)": [re.compile(r"(?:(?<=^)|(?<=[\s:;«]))\(?%d\)%s" % (i, _SUITE)) for i in range(1, 10)],
    "a) b) c)": [re.compile(r"(?:(?<=^)|(?<=[\s:;«]))\(?%s\)%s" % (l, _SUITE)) for l in "abcdefghi"],
}


def mots(texte: str) -> int:
    return len(texte.split())


def texte(el) -> str:
    return " ".join(el.get_text(" ").split())


def lignes(el) -> str:
    """Le texte d'un bloc, avec un saut de ligne à chaque <br> — une entrée placée après un
    <br> commence une ligne, et c'est exactement ce que demande la n°33."""
    morceaux = []
    for d in el.descendants:
        if isinstance(d, Tag) and d.name == "br":
            morceaux.append("\n")
        elif isinstance(d, NavigableString) and not isinstance(d, Comment):
            # Un saut de ligne du SOURCE n'est qu'un blanc à l'écran : seul <br> coupe la ligne.
            morceaux.append(str(d).replace("\n", " ").replace("\r", " "))
    return "\n".join(" ".join(l.split()) for l in "".join(morceaux).split("\n"))


def texte_de_tete(li: Tag) -> str:
    """Le texte propre d'un item : sans ses sous-listes, figures, volets, ni sous-blocs typés
    (un <span class="voir"> ou un <div class="avertir"> est déjà un repère à part)."""
    parts = []
    for c in li.children:
        if isinstance(c, Tag):
            if c.name in ("ul", "ol", "details", "table", "figure") or (c.get("class") and c.name != "b"):
                continue
            parts.append(c.get_text(" "))
        else:
            parts.append(str(c))
    return " ".join(" ".join(parts).split())


def lignes_de_tete(li: Tag) -> str:
    """Le texte de tête d'un item, ligne par ligne (<br>), sans ses sous-blocs."""
    copie = BeautifulSoup(str(li), "lxml").li
    for c in list(copie.children):
        if isinstance(c, Tag) and (c.name in ("ul", "ol", "details", "table", "figure")
                                   or (c.get("class") and c.name != "b")):
            c.decompose()
    return lignes(copie)


def enumeration_en_ligne(bloc: Tag) -> str | None:
    """Rend la famille de marqueurs si le bloc porte ≥ 3 entrées dont ≥ 2 en milieu de ligne."""
    if bloc.name == "li":
        copie = BeautifulSoup(str(bloc), "lxml").li
        for sous in copie.find_all(["ul", "ol", "details", "table", "figure"]):
            sous.decompose()
        bloc = copie
    t = lignes(bloc)
    for nom, marqueurs in FAMILLES.items():
        pos, trouves, en_ligne = 0, 0, 0
        for m in marqueurs:
            r = m.search(t, pos)
            if not r:
                break
            trouves += 1
            debut_de_ligne = t.rfind("\n", 0, r.start())
            avant = t[debut_de_ligne + 1:r.start()].strip(" («")
            # « Pour a) : » en tête de ligne : un seul mot court avant le marqueur, l'entrée
            # commence bien sa ligne.
            if avant and not re.fullmatch(r"\w{1,10}", avant):
                en_ligne += 1
            pos = r.end()
        if trouves >= 3 and en_ligne >= 2:
            return nom
    return None


def ancre(p: Tag) -> bool:
    """Un bloc s'ouvre sur un repère : il est typé (classe), il porte un champ de réponse, ou
    un gras commence dans ses TROIS premiers mots — « La <b>borne inclinée</b> » se repère
    aussi bien que « <b>Borne inclinée :</b> ». Un émoji de tête ne compte pas comme mot."""
    if p.get("class"):
        return True
    if p.find(["select", "input", "textarea", "button"]):
        return True
    vus = 0
    for d in p.descendants:
        if isinstance(d, Tag) and d.name in ("strong", "b") and texte(d):
            return True
        if isinstance(d, NavigableString) and not isinstance(d, Comment) \
                and not (d.parent and d.parent.name in ("strong", "b")):
            vus += sum(1 for m in d.split() if any(ch.isalnum() for ch in m))
            if vus >= 3:
                return False
    return False


def prose(el) -> bool:
    return isinstance(el, Tag) and el.name == "p"


def analyser(chemin: str) -> dict:
    soupe = BeautifulSoup(open(chemin, encoding="utf-8", errors="replace").read(), "lxml")
    for t in soupe(["script", "style", "noscript", "template"]):
        t.decompose()
    ecarts = {"H1": [], "H2": [], "H3": [], "H4": [], "H5": [], "H6": []}
    hors_sequence = not os.path.basename(chemin).startswith(SEQUENCE)

    def titre(el):
        h = el.find_previous(["h1", "h2", "h3", "h4", "summary"])
        return texte(h)[:60] if h else ""

    for bloc in soupe.find_all(["p", "li"]):
        famille = enumeration_en_ligne(bloc)
        if famille:
            ecarts["H1"].append({"famille": famille, "sous": titre(bloc), "debut": texte(bloc)[:90]})

    for parent in soupe.find_all(True):
        suite = []

        def clore():
            if len(suite) >= MUR_PARAS:
                n = sum(mots(texte(x)) for x in suite)
                if n >= MUR_MOTS:
                    ecarts["H2"].append({"mots": n, "paragraphes": len(suite), "sous": titre(suite[0]),
                                         "debut": texte(suite[0])[:90]})
        for c in parent.children:
            if isinstance(c, NavigableString) and not c.strip():
                continue
            if prose(c) and not ancre(c):
                suite.append(c)
            else:
                clore()
                suite = []
        clore()

    for p in soupe.find_all("p"):
        n = mots(texte(p))
        if hors_sequence and n > PAVE_MOTS:
            ecarts["H6"].append({"mots": n, "sous": titre(p), "debut": texte(p)[:90]})
        if n > GRAS_MOTS:
            gras = sum(mots(texte(g)) for g in p.find_all(["strong", "b"]) if not g.find_parent(["strong", "b"]))
            if gras / n > GRAS_PART:
                ecarts["H3"].append({"mots": n, "sous": titre(p), "debut": texte(p)[:90]})

    for cel in soupe.find_all(["td", "th"]):
        # Une cellule déjà découpée en lignes (<br>, paragraphes, items) est hiérarchisée :
        # on juge sa plus longue ligne, pas son total.
        for bloc in cel.find_all(["p", "li", "div"]):
            bloc.insert_before(BeautifulSoup("<br>", "lxml").br)
        n = max(mots(l) for l in lignes(cel).split("\n"))
        if n > CELLULE_MOTS:
            ecarts["H4"].append({"mots": n, "sous": titre(cel), "debut": texte(cel)[:90]})

    for li in soupe.find_all("li"):
        # Comme la cellule : un item découpé par <br> se juge à sa plus longue ligne.
        n = max(mots(l) for l in lignes_de_tete(li).split("\n"))
        if n > ITEM_MOTS_ANCRE or (n > ITEM_MOTS and not ancre(li)):
            ecarts["H5"].append({"mots": n, "sous": titre(li), "debut": texte_de_tete(li)[:90]})
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


NOMS = {"H1": "énumération en ligne", "H2": "mur sans repère", "H3": "paragraphe tout en gras",
        "H4": "cellule-pavé", "H5": "item-pavé", "H6": "pavé hors séquence"}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    muet, en_json = "--muet" in argv, "--json" in argv
    cibles = [a for a in argv if not a.startswith("--")] or [DEPOT]
    lues = pages([os.path.abspath(c) for c in cibles])
    if not lues:
        return panne.rien_vu("aucune page élève (séquence, TP, atelier, synthèse élève…) sous %s"
                             % " · ".join(cibles))
    rapport = {os.path.relpath(f, DEPOT).replace(os.sep, "/"): analyser(f) for f in lues}
    total = {k: sum(len(r[k]) for r in rapport.values()) for k in NOMS}
    if en_json:
        print(json.dumps({"pages": len(lues), "total": total, "detail": rapport}, ensure_ascii=False, indent=1))
        return 1 if any(total.values()) else 0
    for f, r in rapport.items():
        if any(r.values()):
            print("\n── %s" % f)
            for k, liste in r.items():
                for e in liste:
                    mesure = ("%d mots · " % e["mots"]) if "mots" in e else ("%s · " % e["famille"])
                    print("   ✘ %s %-22s %s« %s… » (sous « %s »)" % (k, NOMS[k], mesure, e["debut"], e["sous"]))
    if any(total.values()):
        print("\n%d page(s) lues · %s" % (len(lues), " · ".join("%s %s : %d" % (k, NOMS[k], v) for k, v in total.items())))
        return 1
    if not muet:
        print("%d page(s) lues · ✅ aucune énumération en ligne, aucun mur sans repère, aucun "
              "paragraphe tout en gras, aucune cellule-pavé, aucun item-pavé, aucun pavé hors séquence"
              % len(lues))
    return 0


if __name__ == "__main__":
    sys.exit(main())
