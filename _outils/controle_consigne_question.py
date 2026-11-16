# -*- coding: utf-8 -*-
"""controle_consigne_question.py — règle d'or n°335 : une consigne par question, une à la fois.

LE CONSTAT
----------
Le 15/11/2026, Pascal, sur `3e_C9.1` en mode mission (séance 4, « ① La traduction — complète la fonction ») : trois
questions dont l'énoncé était « ▢1 : », « ▢2 : », « ▢3 : » — « ici il n'y a pas de consignes, il faudrait une règle
d'or et une révision de toutes les séquences » ; puis : « même si cela paraît logique, il faut une consigne, et une à
la fois ». En mode mission, chaque question a son écran : un énoncé réduit à une étiquette n'y dit plus rien.

PÉRIMÈTRE (règle n°47)
----------------------
Pages lues : les pages élève (mêmes motifs que `controle_schema_sous_les_yeux.py`), hors archive, hors QCM.
L'unité jugée est la QUESTION : un `fieldset.qcm-groupe` et son énoncé (`legend`), rangées de réponses courtes
(`qcm-rangee`, `qcm-court`) comprises — « ▢1 : » en était une. Les cases d'un tableau de questions (`qcm-cellule`, ou
tout groupe posé dans un `<table>`) et les rangées d'une grille lettrée (`qcm-grille`) sont comptées à part : leur
consigne est celle du tableau ou de la grille, qui doit se tenir juste au-dessus (C2).

Mesuré, donc établi :
  C1  ÉNONCÉ SANS CONSIGNE (✘ avec --strict, ⚠ sinon) — une question isolée dont l'énoncé, numérotation et symboles
      ôtés, n'est ni une vraie question (« ? »), ni une consigne (un verbe à l'impératif en tête : choisis, coche,
      indique…). Une étiquette (« ▢1 : », « a) », « Bloc 3 ») comme une phrase à compléter (« Après la ligne 3, passages
      vaut : ») : décision de Pascal du 15/11/2026, 18 h 35, « tout réécrire » (937 énoncés sur 77 pages).
  C2  TABLEAU OU GRILLE SANS CONSIGNE (⚠) — un tableau de questions, ou une grille (ses rangées à la suite), dont aucun
      élément juste avant ne porte une consigne (un verbe à l'impératif) ou une question. Le bloc des réponses lettrées
      d'une grille ne compte pas : en mission, il devient la réserve d'étiquettes.

NON mesuré, donc à juger à l'œil : que la consigne soit LA bonne (qu'elle dise exactement ce qu'on attend) ; « une à la
fois » au sens strict (une consigne qui demande deux choses) ; la donnée nécessaire sur le même écran (n°331).

Usage : python3 _outils/controle_consigne_question.py [--strict] [--muet] [--json] [chemin…]
Sortie : 0 sans ✘ · 1 au moins un ✘ (--strict) · 2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import json
import os
import re
import sys

from bs4 import BeautifulSoup, Tag

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_schema_sous_les_yeux as n331  # noqa: E402  (même périmètre de pages)

DEPOT = n331.DEPOT

IMPERATIFS = (
    "choisis coche indique complète complete classe associe range relie donne trouve place sélectionne selectionne "
    "repère repere écris ecris nomme dis relève releve calcule compare identifie prédis predis reporte vérifie verifie "
    "explique justifie numérote numerote ordonne mets remets pose lis observe estime mesure note souligne entoure "
    "décide decide tranche corrige retrouve traduis cherche propose barre déduis deduis devine attribue rattache "
    "sépare separe trie raye recopie suis teste exécute execute imagine situe localise relis regarde clique ouvre "
    "rédige redige cite dessine réponds reponds"
).split()
CLES = ("qcm-cles", "cles-grille")  # le bloc des réponses lettrées d'une grille
NUMEROTATION = re.compile(r"^[\s\W\d_]*?(?:[a-z]\)|\d+[.)°]|[①-⑳]|▢\s*\d+|q\d+|question\s+\d+)?[\s\W_]*", re.I)


def net(t):
    return re.sub(r"\s+", " ", t or "").strip()


def mots(t):
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ0-9'’-]+", t)


# les mots qui peuvent précéder l'impératif sans en changer le sens (« Puis choisis… », « À toi : indique… ») ; « mesure »,
# « note », « place » sont aussi des noms : l'impératif se cherche en tête, après ces seuls mots-là (« Comparer la mesure… »
# n'est pas une consigne)
CONNECTEURS = set("puis ensuite maintenant alors et enfin abord d'abord d’abord toi à ton tour ici là".split())


def imperatif_en_tete(ws):
    for w in ws[:4]:
        lw = w.lower()
        if lw in CONNECTEURS:
            continue
        return lw in IMPERATIFS
    return False


def est_consigne(texte):
    """une vraie question (« … ? »), ou une consigne qui commence par un verbe à l'impératif (« Choisis… ») ; une phrase
    à compléter (« Après la ligne 3, passages vaut : ») n'en est pas une (décision de Pascal du 15/11/2026, 18 h 35)"""
    t = net(texte)
    if "?" in t:
        return True
    reste = NUMEROTATION.sub("", t, count=1)
    m = mots(reste)
    if not m:
        return False
    if imperatif_en_tete(m):
        return True
    # la condition d'abord, puis l'action (« Pour chaque scénario, prédis… », « Si la LED reste éteinte, vérifie… ») :
    # c'est l'ordre que demande le texte aéré ; le verbe vient juste après la virgule
    # (une condition peut avoir deux temps : « Pour chaque position, de 1 à 6, choisis… »)
    parts = reste.split(",")
    for k in range(1, min(3, len(parts))):
        avant, apres = ",".join(parts[:k]), ",".join(parts[k:])
        if len(mots(avant)) <= 10 and imperatif_en_tete(mots(apres)):
            return True
    return False


def ecarts_page(html):
    soupe = BeautifulSoup(html, "html.parser")
    for t in soupe.find_all(n331.HORS_TEXTE):
        t.decompose()
    ecarts = []
    groupes_vus = set()
    for f in soupe.select("fieldset.qcm-groupe"):
        classes = f.get("class") or []
        lg = f.find("legend")
        enonce = net(lg.get_text(" ")) if lg else ""
        en_tableau = "qcm-cellule" in classes or f.find_parent("table") is not None
        # une rangée de réponses courtes (qcm-rangee, qcm-court) est une question comme une autre : elle a son énoncé
        en_grille = "qcm-grille" in classes
        if en_tableau or en_grille:
            # la consigne est celle du tableau ou de la grille : un élément juste avant lui. Les rangées d'une grille se
            # suivent : la grille commence à la première. Son bloc de réponses lettrées (« Les réponses possibles —
            # choisis une lettre… ») ne compte pas : en mission, il devient la réserve d'étiquettes, et ne dit plus
            # ce qu'on associe à quoi.
            porteur = f.find_parent("table") or f.find_parent(class_=re.compile(r"qcm-grille|grille"))
            if porteur is None:
                porteur = f
                while en_grille:
                    prec = porteur.find_previous_sibling()
                    if isinstance(prec, Tag) and prec.name == "fieldset" and "qcm-grille" in (prec.get("class") or []):
                        porteur = prec
                    else:
                        break
            # un tableau qui défile (div.defile, et son cadre) : sa consigne se tient avant l'enveloppe
            while (porteur.parent is not None and porteur.parent.name == "div"
                   and not any(c in (porteur.parent.get("class") or []) for c in ("exo", "activite", "card"))
                   and len([c for c in porteur.parent.children if isinstance(c, Tag)]) == 1):
                porteur = porteur.parent
            if id(porteur) in groupes_vus:
                continue
            groupes_vus.add(id(porteur))
            avant = [x for x in porteur.find_previous_siblings(limit=5) if isinstance(x, Tag)
                     and not any(c in (x.get("class") or []) for c in CLES)][:3]
            texte_avant = " ".join(net(x.get_text(" ")) for x in avant)
            cap = porteur.find("caption")
            if cap:
                texte_avant += " " + net(cap.get_text(" "))
            phrases = re.split(r"(?<=[.!?:;])\s+", texte_avant)
            if not any(est_consigne(p) for p in phrases if p):
                ecarts.append({"code": "C2", "question": enonce[:70] or f.get("id", "?"), "id": f.get("id", "")})
            continue
        if not est_consigne(enonce):
            ecarts.append({"code": "C1", "question": enonce[:70] or "(sans énoncé)", "id": f.get("id", "")})
    return ecarts


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    strict, muet, en_json = "--strict" in argv, "--muet" in argv, "--json" in argv
    liste = n331.pages([a for a in argv if not a.startswith("--")] or [DEPOT])
    if not liste:
        print("EN PANNE : aucune page élève lue (règle n°299).")
        return 2
    c1 = c2 = 0
    par_page = {}
    for chemin in liste:
        try:
            html = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        e = ecarts_page(html)
        if e:
            par_page[os.path.relpath(chemin, DEPOT).replace(os.sep, "/")] = e
            c1 += sum(1 for x in e if x["code"] == "C1")
            c2 += sum(1 for x in e if x["code"] == "C2")
    if en_json:
        print(json.dumps({"pages_lues": len(liste), "C1": c1, "C2": c2, "par_page": par_page}, ensure_ascii=False, indent=1))
    else:
        print("%d page(s) lues — règle d'or n°335, une consigne par question, une à la fois" % len(liste))
        if not muet:
            for page, e in par_page.items():
                print("\n%s" % page)
                for x in e:
                    if x["code"] == "C1":
                        print("  %s C1 énoncé sans consigne — « %s » (#%s)" % ("✘" if strict else "⚠", x["question"], x["id"]))
                    else:
                        print("  ⚠ C2 tableau ou grille sans consigne juste au-dessus — « %s » (#%s)" % (x["question"], x["id"]))
        print("\n%d C1 (énoncé sans consigne) · %d C2 (tableau ou grille sans consigne) · %d page(s)"
              % (c1, c2, len(par_page)))
        if not par_page:
            print("✅ chaque question porte sa consigne")
    return 1 if strict and c1 else 0


if __name__ == "__main__":
    sys.exit(main())
