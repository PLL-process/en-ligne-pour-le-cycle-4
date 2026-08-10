# -*- coding: utf-8 -*-
"""Audit des règles d'or mécanisables, sur tout le dépôt.

Ce script ne juge pas la qualité pédagogique : il constate des FAITS
vérifiables sur les fichiers. Chaque constat renvoie à la règle qui le motive.
Il n'écrit rien, il rapporte.

Se lance DEPUIS LA RACINE du dépôt, car il parcourt les trois thèmes :

    python3 theme-3-creation-conception-realisation-innovations/audit/audit_spiralaire.py \
        > theme-3-creation-conception-realisation-innovations/audit/AUDIT_HARMONISATION.md

Il vit dans le dossier du thème 3 et non à la racine : la garde-périmètre
n'accepte à la racine qu'une liste fermée de fichiers, et elle a raison.
"""
import re, sys
from pathlib import Path
from collections import defaultdict

R = Path(".")   # la racine du dépôt : lancer le script depuis là
IGNORE = ("_archive-anciennes-versions", "node_modules", ".git", "_outils", "_generation")

RE_NAV   = re.compile(r'<nav[^>]*id="navharm".*?</nav>', re.S)
RE_HREF  = re.compile(r'href="([^"#?]+)')
RE_SEQ   = re.compile(r'sequence_[\w.\-]+\.html$')
RE_NIV   = re.compile(r'[\\/](4e|3e)[\\/]')
RE_RAP   = re.compile(r'rappel-spiralaire|Ce que tu as déjà fait|&#128260;')
RE_BONUS = re.compile(r'(?is)<section[^>]*class="[^"]*bonus[^"]*".*?</section>')
RE_CORR  = re.compile(r'corrige-bonus|<details')
RE_RESO  = re.compile(r'(?:src|href)="(https?://[^"]+)"')

def pages():
    for p in sorted(R.rglob("*.html")):
        s = str(p)
        if any(i in s for i in IGNORE):
            continue
        if p.name in ("index.html",) or p.parent == R:
            continue
        yield p

def audite(p):
    h = p.read_text(encoding="utf-8", errors="replace")
    faits = []

    # n°88 — d'où l'on vient, où l'on va, comment on sort
    nav = RE_NAV.search(h)
    if not nav:
        faits.append(("n°88", "aucune barre de navigation — page sans sortie"))
    else:
        liens = RE_HREF.findall(nav.group(0))
        morts = [x for x in liens if not (p.parent / x).resolve().exists()]
        if morts:
            faits.append(("n°88", "lien(s) de navigation mort(s) : " + ", ".join(morts[:3])))
        if not any(RE_SEQ.search(x) for x in liens) and not RE_SEQ.search(p.name):
            faits.append(("n°88", "aucun retour vers une séquence"))

    # n°87 — clé de voûte : une page de 4e ou de 3e s'appuie sur un prérequis
    porte_prerequis = (RE_NIV.search(str(p))
                       and p.name.startswith(("sequence_", "tp_", "atelier_"))
                       and "Synthèses" not in str(p))
    if porte_prerequis and not RE_RAP.search(h):
        faits.append(("n°87", "séance de 4e/3e sans rappel de ce que l'élève a déjà produit"))

    # n°86 — un bonus sans corrigé n'est pas un bonus
    for b in RE_BONUS.findall(h):
        if not RE_CORR.search(b):
            faits.append(("n°86", "bloc bonus sans corrigé replié"))
            break

    # n°40 — une page doit fonctionner hors ligne
    ext = {u.split("/")[2] for u in RE_RESO.findall(h)}
    if ext:
        faits.append(("n°40", "appelle le réseau : " + ", ".join(sorted(ext)[:3])))

    # images annoncées mais absentes (la classe de bug des « fenêtres blanches »)
    imgs = re.findall(r'<img[^>]+src="([^"]+)"', h)
    abs_ = [i for i in imgs if not i.startswith(("http", "data:"))
            and not (p.parent / i).exists()]
    if abs_:
        faits.append(("images", "%d image(s) annoncée(s) et absente(s)" % len(abs_)))

    return faits

def main():
    par_regle = defaultdict(list)
    total = 0
    for p in pages():
        total += 1
        for regle, quoi in audite(p):
            par_regle[regle].append((str(p), quoi))

    ordre = ["n°88", "n°87", "n°86", "images", "n°40"]
    TITRES = {
      "n°88": "n°88 — une page se juge aussi sur ce qu'on peut en faire quand on y est arrivé",
      "n°87": "n°87 (CLÉ DE VOÛTE) — toute séance qui s'appuie sur un prérequis s'ouvre par un rappel",
      "n°86": "n°86 — un bonus sans corrigé n'est pas un bonus, c'est un devoir non rendu",
      "images": "Images annoncées et absentes — les « fenêtres blanches »",
      "n°40": "n°40 — une page doit fonctionner hors ligne",
    }
    print("# Audit du dépôt — les règles d'or mécanisables\n")
    print("Constats de FAITS vérifiés sur les fichiers, pas de jugements pédagogiques.")
    print("**%d pages examinées.**\n" % total)
    print("| Règle | Pages concernées |\n|---|---|")
    for r in ordre:
        print("| %s | **%d** |" % (r, len({f for f, _ in par_regle[r]})))
    print()
    for r in ordre:
        items = par_regle[r]
        if not items:
            print("## %s\n\nAucun manquement.\n" % TITRES[r]); continue
        print("## %s\n" % TITRES[r])
        print("%d page(s).\n" % len({f for f, _ in items}))
        vus = set()
        for f, quoi in items:
            if f in vus: continue
            vus.add(f)
            print("- `%s` — %s" % (f, quoi))
        print()
    print("---\n")
    print("## Périmètre de cet audit\n")
    print("**Vérifié mécaniquement** : présence et validité des liens de navigation, présence")
    print("d'un rappel spiralaire sur les pages de 4e et de 3e, présence d'un corrigé dans les")
    print("blocs bonus, existence réelle des images annoncées, appels réseau.\n")
    print("**NON couvert** : la qualité du rappel — nomme-t-il une PRODUCTION ou seulement une")
    print("notion, dit-il ce qui change, est-il auto-suffisant ? La justesse des corrigés. La")
    print("pertinence des situations déclenchantes. Un script détecte l'absence d'un bloc, jamais")
    print("la platitude de son contenu. Ces jugements-là restent humains.")

main()
