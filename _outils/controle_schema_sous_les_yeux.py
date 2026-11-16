# -*- coding: utf-8 -*-
"""controle_schema_sous_les_yeux.py — règle d'or n°331 (clé de voûte) : l'élève répond le schéma sous les yeux.

LE CONSTAT
----------
Le 15/11/2026, Pascal, sur le Book Train (`4e_C4.1`) : « l'élève ne visualise pas la chaîne
d'énergie et d'information, il faudrait la représenter tout en affichant la question. Même chose
pour les solutions techniques : il ne visualise pas le schéma s'il ne le voit pas là. » Sur la
page, le schéma d'ensemble était trois cartes au-dessus du tableau « quelle solution pour quelle
fonction », et l'activité 2.1 disait « regarde bien les schémas » alors que la chaîne d'énergie
n'apparaissait que deux activités plus bas. Les compétences C4 sont des compétences de LECTURE
d'un schéma : sans le schéma sous les yeux, la question teste la mémoire, pas la lecture.

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Pages lues : les pages que lit un élève — séquences, TP, ateliers, activités, entraînements,
fiches, pages Vittascience, synthèses élève (mêmes motifs que `controle_hierarchie.py`). Hors
archive, hors QCM (un QCM met sa figure dans la question : `controle_banque_qcm.py`).

L'unité jugée est le BLOC DE QUESTION : l'ancêtre le plus proche d'un champ de réponse qui est
une carte d'activité (`.carte`, `section.card`, `.activite`, `.activite-en-ligne`, `.exercice`,
un `<section>` ou un `<article>`). Un champ de réponse : groupe de boutons radio, liste
déroulante, case à cocher, zone de texte, champ texte.

Mesuré, donc établi :
  S1  renvoi vers un schéma hors du bloc (✘, fait sortir à 1) — le bloc porte un champ de
      réponse, son texte nomme un schéma ET le renvoie ailleurs (« plus haut », « ci-dessus »,
      « ci-dessous », « de la séance 2 », « de l'activité 1.3 ») ET le bloc n'a aucune figure.
  S2  schéma nommé, aucune figure dans le bloc (⚠, listé, ne fait pas sortir à 1 : règle n°248,
      un contrôle qui signale du correct finit ignoré) — même chose sans le renvoi. Une partie
      de ces blocs est juste (« conçois l'algorigramme avant toute référence ») : à juger.
      Un schéma nommé — « schéma », « diagramme », « chaîne d'énergie », « chaîne
      d'information », « algorigramme », « organigramme », « figure 4 », « Fig. 4 ».
      Aucune figure : ni `<figure>`, `<picture>`, `<object>`, `<embed>`,
      `<iframe>` ou `<canvas>`, ni `<img>` (hors icône déclarée `aria-hidden`), ni SVG d'au
      moins 120 unités de large, ni élément de classe `figure`, `schema` ou `diagramme`.
      Écartés : un schéma au possessif (« mon algorigramme », « TA chaîne ») — c'est la
      production de l'élève, pas un document à montrer ; les cellules de tableau et les
      légendes (un tableau comparatif cite un mot sans poser de question dessus) ; les billets d'entrée et de sortie, passeports, bilans,
      « avant de commencer », hypothèses de départ, problématiques et piqûres de rappel, qui
      se font de mémoire par construction (n°330).

NON mesuré, donc à juger à l'œil : que la figure présente soit LE schéma dont parle la question ;
qu'elle soit muette sur ce que la question demande (une figure qui porte la réponse n'est pas
un appui, c'est un corrigé) ; qu'elle reste visible pendant qu'on répond (épinglée, ou côte à
côte : `.schema-sous-les-yeux` et `.carte.cote-a-cote` du pilote Book Train) ; sa lisibilité
(n°325, `controle_schemas.mjs`).

  S3  schéma replié (⚠, listé — ajout du 15/11/2026, Pascal : « le mettre dehors », le schéma hors des dépliants) — le
      bloc a des figures, mais toutes dans un <details> fermé qui n'est ni une correction, ni une aide, ni les pièges :
      l'élève ne les voit pas en répondant.

Usage : python3 _outils/controle_schema_sous_les_yeux.py [--muet] [--json] [chemin…]
Sortie : 0 aucun renvoi hors bloc · 1 au moins un ✘ S1 · 2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import json
import os
import re
import sys

from bs4 import BeautifulSoup, Comment, Tag

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)
MOTIFS = ("sequence_", "sequence-", "sequence.html", "tp_", "atelier", "activite",
          "entrainement", "fiche_maths", "vittascience", "synthese_eleve")

CHAMPS = "fieldset.qcm-groupe, input[type=radio], select, input[type=checkbox], textarea, input[type=text]"
CLASSES_BLOC = ("carte", "card", "activite", "activite-en-ligne", "exercice", "bloc-exercice", "etape")
BALISES_BLOC = ("section", "article")

MENTION = re.compile(
    r"\b(sch[ée]mas?|diagrammes?|cha[îi]nes?\s+d['’](?:[ée]nergie|information)|algorigrammes?|organigrammes?"
    r"|fig\.\s*\d+|figures?\s+\d+)\b", re.IGNORECASE)
#: « mon algorigramme », « TA chaîne » : la production de l'élève, pas un document à montrer
POSSESSIF = re.compile(r"\b([mts]on|[mts]a|[mts]es|notre|votre|leurs?)\s*$", re.IGNORECASE)
RENVOI = re.compile(
    r"(plus\s+haut|plus\s+bas|ci-dessus|ci-dessous|au-dessus|(?:de|dans|en)\s+la\s+s[ée]ance\s+\d|"
    r"(?:de|dans)\s+l['’]activit[ée]\s+\d|onglet)", re.IGNORECASE)
HORS_TEXTE = ("script", "style", "template", "noscript")
#: un tableau comparatif cite un mot sans poser de question dessus : ses cellules ne comptent pas
HORS_MENTION = ("td", "th", "figcaption")
#: un billet (entrée ou sortie) et un bilan se font de mémoire, par construction (n°330)
BLOCS_DE_MEMOIRE = re.compile(r"(billet|bilan|auto-positionne|passeport|avant de commencer|ce que je v[ée]rifie|"
                              r"hypoth[èe]se|probl[ée]matique|piq[ûu]re de rappel)", re.IGNORECASE)
LARGEUR_ICONE = 120


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


def est_bloc(t: Tag) -> bool:
    if t.name in BALISES_BLOC:
        return True
    classes = t.get("class") or []
    return any(c in CLASSES_BLOC for c in classes)


def bloc_de(champ: Tag):
    for p in champ.parents:
        if isinstance(p, Tag) and est_bloc(p):
            return p
    return None


def est_correction(t: Tag) -> bool:
    classes = t.get("class") or []
    return any(c in ("correction", "corrige", "corrigé") for c in classes)


def texte_visible(bloc: Tag) -> str:
    copie = BeautifulSoup(str(bloc), "html.parser")
    for t in copie.find_all(HORS_TEXTE):
        t.decompose()
    for c in copie.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for t in list(copie.find_all(["details", "div", "section"])):
        if t.attrs is not None and est_correction(t):
            t.decompose()
    for t in list(copie.find_all(class_="visually-hidden")) + list(copie.find_all(HORS_MENTION)):
        if t.attrs is not None:
            t.decompose()
    return re.sub(r"\s+", " ", copie.get_text(" ")).strip()


def largeur_svg(svg: Tag) -> float:
    vb = (svg.get("viewBox") or svg.get("viewbox") or "").replace(",", " ").split()
    if len(vb) == 4:
        try:
            return float(vb[2])
        except ValueError:
            pass
    w = (svg.get("width") or "0").replace("px", "")
    try:
        return float(w)
    except ValueError:
        return 0.0


def a_une_figure(bloc: Tag) -> bool:
    if bloc.find(["figure", "canvas", "picture", "object", "embed", "iframe"]):
        return True
    if bloc.find(class_=lambda c: c in ("figure", "schema", "schéma", "diagramme")):
        return True
    for img in bloc.find_all("img"):
        if img.get("aria-hidden") != "true":
            return True
    for svg in bloc.find_all("svg"):
        if svg.get("aria-hidden") == "true":
            continue
        if largeur_svg(svg) >= LARGEUR_ICONE:
            return True
    return False


#: un dépliant qui PEUT garder sa figure fermée : la correction, les aides, les pièges (ils s'ouvrent après coup)
#: les dévoilements voulus (« à ouvrir après l'expérience », « après avoir rangé les étapes », « après l'animation ») et les
#: guides de gestes (captures d'un logiciel, fenêtres de Windows, guide pas à pas) : ce ne sont pas des schémas à lire pour répondre
DEPLIANTS_PERMIS = ("correction", "corrige", "corrigé", "aide", "aide1", "aide2", "pieges-replies", "pieges", "bonus-replie",
                    "geste-images", "gestes-fenetres", "guide-replie", "hpp-observe", "document-replie", "ppa-fixe")


def figures_repliees(bloc: Tag):
    """(figures visibles, figures repliées) du bloc, hors corrections et aides : une figure est repliée quand un
    <details> fermé la cache (S3 — Pascal, 15/11/2026, « le mettre dehors » : le schéma hors des dépliants)."""
    visibles, repliees = 0, 0
    for f in bloc.find_all(["figure", "img", "svg", "object", "picture", "canvas"]):
        if f.name == "img" and f.get("aria-hidden") == "true":
            continue
        if f.name == "svg" and (f.get("aria-hidden") == "true" or largeur_svg(f) < LARGEUR_ICONE):
            continue
        if f.find_parent("figure") is not None and f.name != "figure":
            continue   # la figure compte une fois, par son <figure>
        d = f.find_parent("details")
        cache = None
        while d is not None and d is not bloc and bloc in d.parents:
            classes = d.get("class") or []
            if any(c in DEPLIANTS_PERMIS or c.startswith("aide") for c in classes):
                cache = "permis"
                break
            if not d.has_attr("open"):
                cache = "replie"
            d = d.find_parent("details")
        if cache == "permis":
            continue
        if cache == "replie":
            repliees += 1
        else:
            visibles += 1
    return visibles, repliees


def titre_de(bloc: Tag) -> str:
    h = bloc.find(["h2", "h3", "h4", "legend"])
    t = re.sub(r"\s+", " ", h.get_text(" ")).strip() if h else ""
    return t[:70] or ("#" + bloc.get("id") if bloc.get("id") else bloc.name)


def ecarts_page(html: str):
    soupe = BeautifulSoup(html, "html.parser")
    for t in soupe.find_all(HORS_TEXTE):
        t.decompose()
    ecarts, vus = [], set()
    for champ in soupe.select(CHAMPS):
        bloc = bloc_de(champ)
        if bloc is None or id(bloc) in vus:
            continue
        vus.add(id(bloc))
        vis, rep = figures_repliees(bloc)
        if rep and not vis and not BLOCS_DE_MEMOIRE.search(titre_de(bloc) + " " + " ".join(bloc.get("class") or [])):
            ecarts.append({"code": "S3", "bloc": titre_de(bloc), "detail": "%d figure(s), toutes dans un dépliant fermé" % rep,
                           "extrait": ""})
            continue
        if a_une_figure(bloc):
            continue
        if BLOCS_DE_MEMOIRE.search(titre_de(bloc) + " " + " ".join(bloc.get("class") or []) + " " + (bloc.get("id") or "")):
            continue
        texte = texte_visible(bloc)
        m = next((x for x in MENTION.finditer(texte) if not POSSESSIF.search(texte[:x.start()])), None)
        if not m:
            continue
        fenetre = texte[max(0, m.start() - 60): m.end() + 60]
        r = RENVOI.search(fenetre)
        if r:
            ecarts.append({"code": "S1", "bloc": titre_de(bloc), "detail": "renvoi « %s »" % r.group(1),
                           "extrait": fenetre.strip()})
        else:
            ecarts.append({"code": "S2", "bloc": titre_de(bloc), "detail": "mention « %s »" % m.group(0),
                           "extrait": fenetre.strip()})
    return ecarts


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    muet, en_json = "--muet" in argv, "--json" in argv
    cibles = [a for a in argv if not a.startswith("--")] or [DEPOT]
    liste = pages(cibles)
    if not liste:
        print("EN PANNE : aucune page élève lue (règle n°299).")
        return 2
    s1, s2, s3, par_page = 0, 0, 0, {}
    for chemin in liste:
        try:
            html = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        e = ecarts_page(html)
        if e:
            par_page[os.path.relpath(chemin, DEPOT).replace(os.sep, "/")] = e
            s1 += sum(1 for x in e if x["code"] == "S1")
            s2 += sum(1 for x in e if x["code"] == "S2")
            s3 += sum(1 for x in e if x["code"] == "S3")
    if en_json:
        print(json.dumps({"pages_lues": len(liste), "S1": s1, "S2": s2, "S3": s3, "par_page": par_page},
                         ensure_ascii=False, indent=1))
    else:
        print("%d page(s) lues — règle d'or n°331, l'élève répond le schéma sous les yeux" % len(liste))
        if not muet:
            for page, e in par_page.items():
                print("\n%s" % page)
                for x in e:
                    signe = {"S1": "✘ S1 renvoi vers un schéma hors du bloc", "S2": "⚠ S2 schéma nommé, aucune figure dans le bloc",
                             "S3": "⚠ S3 schéma replié : la figure est dans un dépliant fermé"}[x["code"]]
                    print("  %s — %s — %s\n     « %s »" % (signe, x["bloc"], x["detail"], x["extrait"]))
        print("\n%d ✘ (renvoi explicite vers un schéma qui n'est pas dans le bloc) · %d ⚠ (schéma nommé sans figure : à juger) · %d ⚠ S3 (schéma replié) · %d page(s) concernées"
              % (s1, s2, s3, len(par_page)))
        if not s1 and not s2 and not s3:
            print("✅ chaque bloc de question qui nomme un schéma le montre")
    return 1 if s1 else 0


if __name__ == "__main__":
    sys.exit(main())
