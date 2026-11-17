# -*- coding: utf-8 -*-
"""trois_lignes.py — avant de commencer, trois lignes : apprendre, savoir faire, réussir (règle d'or n°337, 17/11/2026).

LE CONSTAT
----------
Pascal, le 17/11/2026, à la lecture d'un audit du QCM de Shenzhen : « Avant de commencer, et dans toutes les séquences,
l'élève devrait lire trois informations très simples : ce qu'il va apprendre, ce qu'il doit savoir faire et comment
réussir. » L'ouverture des séquences disait la situation, la problématique, l'hypothèse ; le référentiel (« je serai
capable de… ») y est replié, dans les mots du programme. Rien ne le disait à l'élève, dans ses mots, avant de commencer.

CE QUE FAIT L'OUTIL
-------------------
  --poser <page> <données.json>   pose (ou réécrit) la carte « 🎯 Avant de commencer : trois choses à lire » en tête de
                                  l'ouverture de la séquence : dans le volet `#ouverture` (le « 📖 Rappel » de la n°311),
                                  juste après ses badges ; une page sans ce volet est refusée (souvent une page
                                  engendrée : la carte se pose dans son générateur). Données :
                                  {"apprendre": [lignes], "savoir_faire": [lignes], "reussir": [lignes]} — une idée par
                                  ligne, HTML court permis (b, &nbsp;, « »). Pose aussi le style, une fois : la
                                  carte porte son propre cadre (largeur, fond, bordure), pour les gabarits anciens
                                  dont la classe `card` n'a pas de style à l'écran ; un style plus ancien est remplacé.
  --verifier <page> <données.json> dit si la carte de la page est celle des données (0 / 1).
  --etat [--strict] [racine]      mesure les séquences du dépôt (pages `sequence…` qui portent le mode mission) : la
                                  carte est là, en tête de l'ouverture (avant la barre d'onglets), avec ses trois
                                  rubriques, chacune de 1 à 3 lignes et de 40 mots au plus. ⚠ par défaut (sortie 0 :
                                  la généralisation est en cours) ; --strict sort à 1 sur le premier manque.
Le QCM a sa propre carte, posée par `_outils/qcm_aides/poser.py` (« ce que tu vas revoir »).

Sortie : 0 · 1 (--verifier, --strict) · 2 rien lu, ou données refusées.
"""
from __future__ import annotations

import json
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTE_RE = re.compile(r'<section class="card trois-lignes" id="trois-lignes">.*?</section>\n', re.S)
RUBRIQUES = (("apprendre", "📚 Ce que tu vas apprendre"), ("savoir_faire", "🛠 Ce que tu dois savoir faire"),
             ("reussir", "✅ Comment réussir"))
MAX_MOTS = 40
CSS = '''/* avant de commencer, trois lignes : apprendre, savoir faire, réussir (règle d'or n°337) */
section.trois-lignes{max-width:960px;margin-left:auto;margin-right:auto;box-sizing:border-box;padding:14px 18px;border-radius:12px;border:1px solid var(--border,rgba(127,127,127,.35));background:var(--panel,rgba(127,127,127,.08))}
.trois-lignes-liste{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:10px}
.trois-lignes-liste li{border-left:3px solid var(--head,#61dafb);padding:2px 0 2px 12px;line-height:1.55}
'''
# le style d'une pose plus ancienne : il est remplacé, jamais doublé
CSS_RE = re.compile(r"/\* avant de commencer, trois lignes[^\n]*\*/\n(?:[^\n]*trois-lignes[^\n]*\n)+")


class Refus(Exception):
    pass


def mots(html: str) -> int:
    return len(re.sub(r"<[^>]+>|&nbsp;", " ", html).split())


def carte(d: dict) -> str:
    items = []
    for cle, titre in RUBRIQUES:
        lignes = d.get(cle) or []
        if not 1 <= len(lignes) <= 3:
            raise Refus("%s : %d ligne(s) ; il en faut de 1 à 3 (trois informations très simples)" % (cle, len(lignes)))
        if sum(mots(x) for x in lignes) > MAX_MOTS:
            raise Refus("%s : %d mots ; %d au plus" % (cle, sum(mots(x) for x in lignes), MAX_MOTS))
        items.append("    <li><b>%s</b>\n    <br>%s</li>" % (titre, "\n    <br>".join(lignes)))
    return ('<section class="card trois-lignes" id="trois-lignes">\n'
            '  <h2>🎯 Avant de commencer&nbsp;: trois choses à lire</h2>\n'
            '  <ul class="trois-lignes-liste">\n%s\n  </ul>\n</section>\n' % "\n".join(items))


def poser(s: str, d: dict) -> str:
    c = carte(d)
    if CARTE_RE.search(s):
        s = CARTE_RE.sub(lambda _: c, s, count=1)
    else:
        m = re.search(r'<details class="rappel-ouverture" id="ouverture"[^>]*>\s*<summary>.*?</summary>\n', s, re.S)
        if m:
            pos = m.end()
            b = re.match(r'<div class="badges">.*?</div>\n', s[pos:], re.S)
            if b:
                pos += b.end()
        else:
            # sans volet « 📖 Rappel » (n°311), la page n'a pas d'ouverture reconnaissable — souvent une page engendrée :
            # la carte se pose dans son générateur, pas ici.
            raise Refus("pas de volet #ouverture (n°311) : page engendrée ou ancienne — poser la carte dans son générateur")
        s = s[:pos] + c + s[pos:]
    if CSS_RE.search(s):
        s = CSS_RE.sub(lambda _: CSS, s, count=1)
    elif ".trois-lignes-liste{" not in s:
        i = s.find("</style>")
        if i < 0:
            raise Refus("aucune feuille de style dans la page")
        s = s[:i] + CSS + s[i:]
    return s


def juger(s: str):
    """Les manques de la carte d'une séquence (liste vide : conforme)."""
    m = CARTE_RE.search(s)
    if not m:
        return ["pas de carte « Avant de commencer »"]
    out = []
    tabs = s.find('class="seance-tabs"')
    if tabs > 0 and m.start() > tabs:
        out.append("la carte est après la barre d'onglets : elle doit ouvrir la séquence")
    for cle, titre in RUBRIQUES:
        lm = re.search(r"<li><b>%s</b>(.*?)</li>" % re.escape(titre), m.group(0), re.S)
        if not lm:
            out.append("rubrique absente : %s" % titre); continue
        lignes = [x for x in lm.group(1).split("<br>") if x.strip()]
        if not 1 <= len(lignes) <= 3:
            out.append("%s : %d ligne(s)" % (titre, len(lignes)))
        if mots(lm.group(1)) > MAX_MOTS:
            out.append("%s : %d mots (%d au plus)" % (titre, mots(lm.group(1)), MAX_MOTS))
    return out


def etat(racine: str, strict: bool) -> int:
    lues, manques = 0, []
    for d, _, fs in os.walk(racine):
        if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d:
            continue
        for f in fs:
            if not (f.startswith("sequence") and f.endswith(".html")):
                continue
            p = os.path.join(d, f)
            s = open(p, encoding="utf-8").read()
            if "mode-mission v1" not in s:
                continue
            lues += 1
            j = juger(s)
            if j:
                manques.append((os.path.relpath(p, racine), j))
    if not lues:
        print("✘ aucune séquence lue : rien n'a été vérifié")
        return 2
    for rel, j in sorted(manques):
        print("  %s %s — %s" % ("✘" if strict else "⚠", rel, " ; ".join(j)))
    print("%d séquence(s) lues · %d avec « Avant de commencer » en trois lignes · %d à poser"
          % (lues, lues - len(manques), len(manques)))
    return 1 if (strict and manques) else 0


def main(argv) -> int:
    if "--etat" in argv:
        autres = [a for a in argv if not a.startswith("--")]
        return etat(autres[0] if autres else DEPOT, "--strict" in argv)
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2 or not ({"--poser", "--verifier"} & set(argv)):
        print(__doc__)
        return 2
    page, donnees = args
    try:
        s = open(page, encoding="utf-8").read()
        u = poser(s, json.load(open(donnees, encoding="utf-8")))
    except (Refus, OSError, json.JSONDecodeError) as e:
        print("✘ %s" % e)
        return 2
    if "--verifier" in argv:
        print(("✅ à jour : " if u == s else "✘ à reposer : ") + page)
        return 0 if u == s else 1
    if u != s:
        open(page, "w", encoding="utf-8").write(u)
        print("✍ posée : %s" % page)
    else:
        print("✅ déjà à jour : %s" % page)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
