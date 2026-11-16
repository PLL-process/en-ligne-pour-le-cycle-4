# -*- coding: utf-8 -*-
"""controle_correction_illustree.py — règle d'or n°336 : la correction se voit ; quand la réponse est un dessin,
elle montre le dessin.

LE CONSTAT
----------
Le 16/11/2026, Pascal : « le mode mission, sauf erreur de ma part, ne contient pas les corrections ; j'aimerais avoir les
corrections dans toutes les séquences » — « et les corrections : si un schéma ou une capture d'écran est nécessaire,
cela doit être fait » — « on devrait y mettre une règle d'or ». Mesuré le même jour : sur les 60 séquences qui portent le
mode mission, les 474 corrections étaient toutes sur un écran (l'écran « je retiens »), mais repliées sous leur titre :
elles passaient inaperçues. Le mode mission les ouvre désormais une fois l'activité vérifiée (`_outils/mode_mission/`,
mesuré par son banc : « corrections ouvertes après vérification »).

Ce contrôle-ci mesure l'autre moitié de la règle : la correction d'une réponse qui SE DESSINE montre le dessin.
Une production faite avec un OUTIL (draw.io, Vittascience, le tableur…) relève de la n°332 (`controle_correction_
complete.py` : la capture et le fichier) ; une chaîne à compléter reçoit son corrigé du moteur commun
(`_outils/chaine_a_completer/` : la chaîne complète, posée en tête de la correction).

PÉRIMÈTRE (règle n°47) — les pages et le découpage en blocs de la n°331 (`controle_schema_sous_les_yeux.py`), hors QCM et
synthèses ; les blocs que juge la n°332 (un outil nommé) sont laissés à la n°332.

Mesuré, donc établi :
  D1  ✘  la question montre un schéma MUET (fichier `…_muet…`) et la correction ne montre aucune figure : l'élève ne voit
         jamais le schéma complet.
  D2  ⚠  le bloc fait DESSINER ou COMPLÉTER un schéma (dessine, trace, schématise, construis, complète, représente,
         recopie… à moins de 120 signes de : schéma, chaîne, algorigramme, croquis, diagramme, bête à cornes, pieuvre,
         câblage, circuit, graphique, courbe, carte mentale), sans chaîne à compléter, et aucune correction du bloc ne
         montre de figure (⚠ ; ✘ avec --strict).
  D3  ⚠  le bloc fait dessiner (D2), et n'a aucune correction.
Pourquoi D2 et D3 en ⚠ : la mesure lit des verbes ; « complète le schéma » peut viser un schéma déjà montré qu'il suffit
de nommer (règle n°248 : un contrôle qui signale du correct finit ignoré). Les blocs jugés justes vont dans JUGES, avec
leur raison.

NON mesuré, donc à juger à l'œil : que la figure de la correction soit le dessin COMPLET attendu, juste, et lisible
(n°315, n°325).

Usage : python3 _outils/controle_correction_illustree.py [--strict] [--muet] [--json] [chemin…]
Sortie : 0 sans ✘ · 1 au moins un ✘ · 2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import json
import os
import re
import sys

from bs4 import BeautifulSoup, Tag

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_schema_sous_les_yeux as n331  # noqa: E402  (même périmètre, même découpage en blocs)
import controle_correction_complete as n332  # noqa: E402  (ce qui se fait avec un outil est à la n°332)

DEPOT = n331.DEPOT
DESSIN = re.compile(
    r"\b(dessine|trace|sch[ée]matise|construis|compl[èe]te|repr[ée]sente|recopie|reproduis|esquisse)\w*\b"
    r"[^.!?]{0,120}?\b(sch[ée]ma|cha[îi]ne|algorigramme|croquis|diagramme|b[êe]te\s+[àa]\s+cornes|pieuvre|c[âa]blage|"
    r"circuit|graphique|courbe|carte\s+mentale)", re.IGNORECASE)
MUET = re.compile(r"[_-]muet\.svg\b", re.IGNORECASE)          # la convention des schémas muets (n°331) : …_muet.svg

#: Les blocs jugés justes, un par un (lus le 16/11/2026) : {page: {début du titre du bloc: raison}}.
T1, T2, T3 = n331.T1, n331.T2, n331.T3
A = T1 + "ateliers-representations/"
JUGES: dict = {
    A + "cas-utilisation-sysml/atelier_4e_cas-utilisation-sysml.html": {
        "Exercice 1 — Du verbatim": "« dessiner les systèmes » est dans la définition de SysML, au lexique"},
    A + "croquis/atelier_3e_croquis.html": {
        "Exercice 3 — Du croquis au schéma": "on choisit une façon de représenter (tableau des cinq façons) ; rien à dessiner"},
    A + "exigences-sysml/atelier_4e_exigences-sysml.html": {
        "Exercice 1 — Lire le diagramme des exigences": "un diagramme à lire, montré dans le bloc ; rien à dessiner"},
    A + "fast/atelier_5e_fast.html": {
        "Exercice 1 — Lire le FAST": "un FAST à lire, montré dans le bloc ; « on dessine son diagramme » le présente"},
    T2 + "C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html": {
        "Le voyage de la donnée": "« tracer des courbes » est une proposition du QCM, pas une consigne",
        "🎁 Bonus (facultatif": "la page trace elle-même la courbe des mesures de l'élève, sous sa table"},
    T2 + "C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train/sequence_4e_C4.1-C4.2-C4.4_book-train.html": {
        "Activité 1.2 — Qui informe, qui agit": "« complète le diagramme fonctionnel » cite un sujet d'évaluation ; l'activité classe"},
    T2 + "C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/sequence_5e_C4.1-C4.8_lampadaire_intelligent.html": {
        "« détecter un passant »": "« on dessine son diagramme FAST » le présente ; la question classe fonction ou solution"},
    T3 + "C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html": {
        "Exercice 2 — Du croquis au schéma": "on choisit une façon de représenter ; rien à dessiner"},
    T3 + "C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/sequence_4e_C8_jardin-validation.html": {
        "📐 Activité 1 — Le protocole en diagramme": "le diagramme à remettre en ordre est dans le bloc (n°331) ; « il se DESSINE » est l'encadré À retenir"},
    T3 + "C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html": {
        "De l'algorithme écrit à l'algorigramme": "l'algorigramme à recopier est montré dans le bloc"},
    T3 + "C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html": {
        "De l'algorithme écrit à l'algorigramme": "l'algorigramme à recopier est montré dans le bloc"},
}


def est_correction(t: Tag) -> bool:
    """Une correction : celles de la n°331, et le corrigé d'un défi du Bonus des ateliers (`details.corrige-bonus`)."""
    return n331.est_correction(t) or "corrige-bonus" in (t.get("class") or [])


def corrections(bloc: Tag):
    return [t for t in bloc.find_all(["details", "div", "section"]) if est_correction(t)]


def juge(page: str, bloc: str):
    for debut, raison in JUGES.get(page, {}).items():
        if bloc.startswith(debut):
            return raison
    return None


def ecarts_page(html: str):
    soupe = BeautifulSoup(html, "html.parser")
    for t in soupe.find_all(n331.HORS_TEXTE):
        t.decompose()
    ecarts, vus = [], set()
    for champ in soupe.select(n331.CHAMPS):
        bloc = n331.bloc_de(champ)
        if bloc is None or id(bloc) in vus:
            continue
        vus.add(id(bloc))
        titre = n331.titre_de(bloc)
        if n331.BLOCS_DE_MEMOIRE.search(titre + " " + " ".join(bloc.get("class") or []) + " " + (bloc.get("id") or "")):
            continue
        if any(c in n332.CARTES for d in bloc.find_all(True) for c in (d.get("class") or [])):
            continue
        cs = corrections(bloc)
        # ce que la question montre ou demande : le bloc sans ses corrections ni ses aides
        copie = BeautifulSoup(str(bloc), "html.parser")
        for d in list(copie.find_all(True)):
            if d.attrs is None or getattr(d, "decomposed", False):
                continue
            if est_correction(d) or re.search(r"\baide", " ".join(d.get("class") or [])):
                d.decompose()
        texte = n331.texte_visible(copie)
        if n332.OUTIL.search(texte) and n332.PRODUIRE.search(texte):
            continue                                                   # la n°332 la juge
        montre = any(n332.montre(c) for c in cs)
        muets = [o for o in copie.find_all(["object", "img"]) if MUET.search((o.get("data") or "") + (o.get("src") or ""))]
        if muets and not montre:
            ecarts.append({"code": "D1", "bloc": titre, "mot": (muets[0].get("data") or muets[0].get("src")).split("/")[-1]})
            continue
        if copie.select_one(n331.CHAINE_A_COMPLETER):
            continue                                                   # le moteur pose la chaîne complète dans la correction
        consignes = " ".join(x for x in re.split(r"(?<=[.!?])\s+", texte) if not x.rstrip().endswith("?"))
        m = DESSIN.search(consignes)
        if m and not montre:
            ecarts.append({"code": "D3" if not cs else "D2", "bloc": titre, "mot": m.group(0)[:70]})
    return ecarts


SIGNES = {"D1": "schéma muet, jamais montré complet", "D2": "le dessin attendu n'est pas montré dans la correction",
          "D3": "le bloc fait dessiner et n'a pas de correction"}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    strict, muet, en_json, voir_juges = "--strict" in argv, "--muet" in argv, "--json" in argv, "--juges" in argv
    liste = n332.pages([a for a in argv if not a.startswith("--")] or [DEPOT])
    if not liste:
        print("EN PANNE : aucune page élève lue (règle n°299).")
        return 2
    compte, par_page, juges = {"D1": 0, "D2": 0, "D3": 0}, {}, []
    for chemin in liste:
        try:
            html = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        rel = os.path.relpath(chemin, DEPOT).replace(os.sep, "/")
        e = []
        for x in ecarts_page(html):
            r = juge(rel, x["bloc"]) if x["code"] != "D1" else None
            if r:
                juges.append((rel, x["bloc"], r))
            else:
                e.append(x)
                compte[x["code"]] += 1
        if e:
            par_page[rel] = e
    graves = compte["D1"] + (compte["D2"] + compte["D3"] if strict else 0)
    if en_json:
        print(json.dumps({"pages_lues": len(liste), **compte, "par_page": par_page,
                          "juges": [{"page": p, "bloc": b, "raison": r} for p, b, r in juges]}, ensure_ascii=False, indent=1))
    else:
        print("%d page(s) lues — règle d'or n°336, la correction se voit ; un dessin attendu y est dessiné" % len(liste))
        if not muet:
            for page, e in par_page.items():
                print("\n%s" % page)
                for x in e:
                    signe = "✘" if x["code"] == "D1" or strict else "⚠"
                    print("  %s %s %s — %s (« %s »)" % (signe, x["code"], SIGNES[x["code"]], x["bloc"], x["mot"]))
        if voir_juges and juges:
            print("\nJugés justes (JUGES) :")
            for p, b, r in juges:
                print("  ✓ %s — %s\n     %s" % (p.split("/")[-1], b, r))
        print("\n%d D1 (schéma muet sans le complet) · %d D2 (dessin attendu non montré) · %d D3 (sans correction) · "
              "%d page(s) · %d bloc(s) jugés justes" % (compte["D1"], compte["D2"], compte["D3"], len(par_page), len(juges)))
        if not par_page:
            print("✅ chaque correction d'un dessin attendu montre le dessin")
    return 1 if graves else 0


if __name__ == "__main__":
    sys.exit(main())
