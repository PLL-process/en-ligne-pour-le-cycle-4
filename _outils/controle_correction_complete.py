# -*- coding: utf-8 -*-
"""controle_correction_complete.py — règle d'or n°332 : la correction montre la production complète, telle que l'outil
la rend, et donne son fichier.

LE CONSTAT
----------
Le 15/11/2026, Pascal, sur le Book Train (`4e_C4.1`, activité 3.2 « Construire l'algorigramme dans draw.io ») : « la
correction doit montrer l'algorigramme complet, de préférence de draw.io, car l'élève n'a encore aucune référence » ;
« il découvre ces outils » ; « fais-en une règle d'or et vérifie les autres séances à ce niveau aussi ». Sur la page :
la correction de 2.2 (la chaîne d'énergie dans draw.io) n'avait aucune figure, celle de 2.3 réservait le fichier corrigé
au professeur, et 4.3 (le diaporama de six diapositives) n'avait pas de correction du tout.

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Pages lues : les pages que lit un élève, comme `controle_schema_sous_les_yeux.py` (séquences, TP, ateliers, activités,
entraînements, pages Vittascience), hors archive, hors QCM et hors synthèses (elles ne font rien produire).

L'unité jugée est le BLOC D'ACTIVITÉ (même découpage que la n°331 : l'ancêtre le plus proche d'un champ de réponse ou
d'une case « j'ai fait » qui est une carte d'activité ; un panneau qui contient des cartes n'est pas jugé). Un bloc FAIT
PRODUIRE AVEC UN OUTIL quand son texte (hors correction, hors questions, hors encadré des rôles) nomme un outil — draw.io,
Impress, PowerPoint, un tableur, Vittascience, Scratch, mBlock, MakeCode, Tinkercad, Onshape, FreeCAD, Sweet Home 3D,
l'éditeur Python… — ET, à moins de 200 signes, demande de construire, dessiner, créer, programmer, modéliser, compléter,
enregistrer ou exporter.

Mesuré, donc établi :
  K1  aucune correction dans le bloc (⚠ par défaut ; ✘ avec --strict).
  K2  une correction, mais ni figure (image, SVG, figure, capture) ni programme écrit en entier (bloc de code) : elle
      décrit la production sans la montrer (⚠ ; ✘ avec --strict).
  K3  la production est montrée, mais son fichier n'est pas donné, ni dans la correction ni ailleurs dans l'activité (ni
      bouton de téléchargement `data-fichier`, ni lien `download`, ni lien vers un .drawio, .odp, .ods, .py, .sb3, .xlsx,
      .pptx…) (⚠, toujours : un fichier n'a pas de sens pour toutes les productions).
Pourquoi ⚠ par défaut : la mesure du 15/11/2026 relève des blocs justes par construction (un bloc qui fait seulement
ouvrir un outil, une manipulation libre) ; règle n°248, un contrôle qui signale du correct finit ignoré. La vague n°332
les juge un par un ; `--strict` sert à la vérifier page par page.

NON mesuré, donc à juger à l'œil : que la figure soit LA production complète (pas un morceau) ; qu'elle vienne de
l'outil (export, capture, ou dessin de même géométrie que le fichier donné) ; que le fichier donné soit le bon.

Usage : python3 _outils/controle_correction_complete.py [--strict] [--muet] [--json] [chemin…]
Sortie : 0 sans ✘ · 1 au moins un ✘ (--strict) · 2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import json
import os
import re
import sys

from bs4 import BeautifulSoup, Tag

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_schema_sous_les_yeux as n331  # noqa: E402  (même découpage en blocs, même périmètre de pages)

DEPOT = n331.DEPOT
MOTIFS = tuple(m for m in n331.MOTIFS if m != "synthese_eleve")
CHAMPS = n331.CHAMPS

OUTIL = re.compile(
    r"\b(draw\.?io|diagrams\.net|impress|powerpoint|diaporama|tableur|libreoffice\s+calc|excel|vittascience|scratch|"
    r"mblock|makecode|tinkercad|onshape|freecad|sweet\s*home|sketchup|thonny|[ée]diteur\s+python|fritzing)\b",
    re.IGNORECASE)
PRODUIRE = re.compile(
    r"\b(constru|dessin|cr[ée]e|r[ée]alis|programm|mod[ée]lis|compl[èe]t|enregistr|export|ins[èe]re|trace|place|"
    r"[ée]cris|code)\w*", re.IGNORECASE)
CARTES = ("carte", "card", "activite", "activite-en-ligne", "exercice", "bloc-exercice")
FICHIER = re.compile(r"\.(drawio|odp|ods|odt|odg|py|sb3|xlsx|pptx|docx|ino|stl|fcstd|sh3d)\b", re.IGNORECASE)


def pages(racines):
    return [p for p in n331.pages(racines) if os.path.basename(p).startswith(MOTIFS)]


def corrections(bloc: Tag):
    return [t for t in bloc.find_all(["details", "div", "section"]) if n331.est_correction(t)]


def montre(correction: Tag) -> bool:
    if n331.a_une_figure(correction):
        return True
    for pre in correction.find_all(["pre", "code"]):   # un programme écrit en entier
        if pre.get_text().count("\n") >= 3:
            return True
    return False


def donne_le_fichier(t: Tag) -> bool:
    if t.find(attrs={"data-fichier": True}) or t.find("a", attrs={"download": True}):
        return True
    return any(FICHIER.search(a.get("href") or "") for a in t.find_all("a"))


def ecarts_page(html: str):
    soupe = BeautifulSoup(html, "html.parser")
    for t in soupe.find_all(n331.HORS_TEXTE):
        t.decompose()
    ecarts, vus = [], set()
    for champ in soupe.select(CHAMPS):
        bloc = n331.bloc_de(champ)
        if bloc is None or id(bloc) in vus:
            continue
        vus.add(id(bloc))
        titre = n331.titre_de(bloc)
        if n331.BLOCS_DE_MEMOIRE.search(titre + " " + " ".join(bloc.get("class") or []) + " " + (bloc.get("id") or "")):
            continue
        # un panneau de séance qui contient des cartes d'activité n'est pas une activité : ses cartes sont jugées une à une
        if any(c in CARTES for d in bloc.find_all(True) for c in (d.get("class") or [])):
            continue
        # la consigne de production : l'outil nommé, et une demande de produire à moins de 200 signes ; les questions et
        # l'encadré des rôles (« le pilote tient l'outil — le clavier, le capteur, le tableur ») ne comptent pas
        copie = BeautifulSoup(str(bloc), "html.parser")
        for r in copie.select(".roles"):
            r.decompose()
        texte = " ".join(x for x in re.split(r"(?<=[.!?])\s+", n331.texte_visible(copie)) if not x.rstrip().endswith("?"))
        o = next((m for m in OUTIL.finditer(texte) if PRODUIRE.search(texte[max(0, m.start() - 200): m.end() + 200])), None)
        if not o:
            continue
        cs = corrections(bloc)
        if not cs:
            ecarts.append({"code": "K1", "bloc": titre, "outil": o.group(1)})
        elif not any(montre(c) for c in cs):
            ecarts.append({"code": "K2", "bloc": titre, "outil": o.group(1)})
        elif not (any(donne_le_fichier(c) for c in cs) or donne_le_fichier(bloc)):
            ecarts.append({"code": "K3", "bloc": titre, "outil": o.group(1)})
    return ecarts


SIGNES = {"K1": "aucune correction", "K2": "la correction décrit sans montrer",
          "K3": "production montrée, fichier non donné"}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    strict, muet, en_json = "--strict" in argv, "--muet" in argv, "--json" in argv
    liste = pages([a for a in argv if not a.startswith("--")] or [DEPOT])
    if not liste:
        print("EN PANNE : aucune page élève lue (règle n°299).")
        return 2
    compte, par_page = {"K1": 0, "K2": 0, "K3": 0}, {}
    for chemin in liste:
        try:
            html = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        e = ecarts_page(html)
        if e:
            par_page[os.path.relpath(chemin, DEPOT).replace(os.sep, "/")] = e
            for x in e:
                compte[x["code"]] += 1
    graves = compte["K1"] + compte["K2"]
    if en_json:
        print(json.dumps({"pages_lues": len(liste), **compte, "par_page": par_page}, ensure_ascii=False, indent=1))
    else:
        print("%d page(s) lues — règle d'or n°332, la correction montre la production complète" % len(liste))
        if not muet:
            for page, e in par_page.items():
                print("\n%s" % page)
                for x in e:
                    signe = ("✘ " if strict and x["code"] != "K3" else "⚠ ") + x["code"]
                    print("  %s %s — %s (outil : %s)" % (signe, SIGNES[x["code"]], x["bloc"], x["outil"]))
        print("\n%d K1 (aucune correction) · %d K2 (correction sans la production) · %d K3 (fichier non donné) · %d page(s)"
              % (compte["K1"], compte["K2"], compte["K3"], len(par_page)))
        if not par_page:
            print("✅ chaque activité qui fait produire avec un outil montre la production complète, et donne son fichier")
    return 1 if strict and graves else 0


if __name__ == "__main__":
    sys.exit(main())
