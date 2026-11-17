# -*- coding: utf-8 -*-
"""corriger_billet.py — le billet d'entrée reçoit sa correction complète (règle n°336, 17/11/2026).

LE CONSTAT
----------
Pascal, le 17/11/2026 : « chaque exercice devrait avoir son bouton de correction », en mode mission comme en page
complète. Le relevé du même jour (126 pages, 720 blocs d'exercice) trouve 15 billets d'entrée qui se vérifient
(« 2 / 3 réponses justes ») sans jamais montrer la bonne réponse : l'élève sait qu'il s'est trompé, pas sur quoi.
Le mode mission montrait le pourquoi d'une mauvaise proposition ; la page complète, rien.

CE QUE FAIT L'OUTIL
-------------------
Dans chaque bloc dont le titre dit « Billet d'entrée », pour chaque question à choix (`fieldset` à boutons radio) :
la bonne réponse est la proposition SANS `data-pourquoi` (les autres portent le pourquoi de leur erreur, écrit pour le
mode mission) ; si le vérificateur de la page la nomme aussi (`be_1:"…"` dans le script), les deux doivent dire la
même chose, sinon l'outil refuse. Il écrit, sous le message de vérification du billet :

    <details class="correction correction-billet">  ✅ Correction complète du billet
      1. la question — ✅ la bonne réponse — ✘ chaque autre proposition, avec son pourquoi, une par ligne

Le mode mission l'ouvre de lui-même une fois le billet vérifié (n°336) ; en page complète, elle reste repliée sous
le bouton. Rejouable : une correction déjà posée par l'outil est réécrite, jamais doublée.

Ce qu'il ne fait pas : une question ouverte (zone de texte) du billet n'a pas de réponse à extraire — l'outil la
nomme (« à écrire à la main ») et ne pose rien pour elle.

Usage : python3 _outils/corriger_billet.py [--ecrire] [--muet] <page.html | dossier> …   (sans chemin : le dépôt)
Sortie : 0 rien à poser ou tout posé · 1 un billet à corriger reste (sans --ecrire) ou un refus · 2 rien lu.
"""
from __future__ import annotations

import html
import os
import re
import sys

from bs4 import BeautifulSoup

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TITRE = re.compile(r"billet d.entr[ée]e", re.I)
MARQUE = "correction-billet"
NEUTRE = re.compile(r"^\s*je ne sais pas", re.I)


def pages(chemins):
    vues = []
    for c in chemins or [DEPOT]:
        if os.path.isfile(c):
            vues.append(os.path.abspath(c)); continue
        for d, _, fs in os.walk(c):
            if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d:
                continue
            for f in fs:
                if f.endswith(".html") and not f.startswith(("qcm", "lexique", "synthese")):
                    p = os.path.join(d, f)
                    if TITRE.search(open(p, encoding="utf-8").read()):
                        vues.append(p)
    return sorted(set(vues))


def attendus_du_script(texte: str) -> dict:
    """Les réponses que le vérificateur de la page attend : `be_1:"…"` (ou 'be_1':'…')."""
    out = {}
    for m in re.finditer(r"""['"]?(\w+)['"]?\s*:\s*"((?:[^"\\]|\\.)*)\"""", texte):
        out.setdefault(m.group(1), html.unescape(m.group(2).replace('\\"', '"')))
    return out


def interne(tag) -> str:
    """Le HTML intérieur d'une balise, sur une ligne."""
    return re.sub(r"\s+", " ", "".join(str(x) for x in tag.contents)).strip()


def correction(section_html: str, script: dict, nom: str):
    soupe = BeautifulSoup(section_html, "html.parser")
    items, a_la_main, refus = [], [], []
    for fs in soupe.select("fieldset"):
        radios = fs.select("input[type=radio]")
        lg = fs.find("legend")
        q = interne(lg) if lg else "(question sans intitulé)"
        if not radios:
            continue
        # « je ne sais pas encore » n'est ni la bonne réponse ni une erreur à expliquer (règle n°26 : le billet aiguille)
        neutres = [r for r in radios if NEUTRE.search(r.get("value", ""))]
        bonnes = [r for r in radios if not r.get("data-pourquoi") and r not in neutres]
        if len(bonnes) != 1:
            refus.append("%s : %d proposition(s) sans pourquoi — il en faut une seule (la bonne) ; écrire le pourquoi"
                         " de chaque mauvaise proposition (data-pourquoi), puis relancer" % (fs.get("id") or q[:40], len(bonnes)))
            continue
        b = bonnes[0]
        att = script.get(fs.get("id") or b.get("name") or "")
        if att is not None and html.unescape(att) != html.unescape(b.get("value", "")):
            refus.append("%s : le vérificateur attend « %s », la page laisse sans pourquoi « %s »"
                         % (fs.get("id"), att[:50], b.get("value", "")[:50]))
            continue

        def libelle(r):
            lab = soupe.find("label", attrs={"for": r.get("id")}) if r.get("id") else None
            return interne(lab) if lab else html.escape(r.get("value", ""))
        lignes = ["<b>%s</b>" % q, "✅ <b>%s</b>" % libelle(b)]
        for r in radios:
            if r is b or r in neutres:
                continue
            lignes.append("✘ «&nbsp;%s&nbsp;»&nbsp;: %s" % (libelle(r), html.escape(r.get("data-pourquoi", ""), quote=False)))
        items.append("    <li>" + "\n    <br>".join(lignes) + "</li>")
    for t in soupe.select("textarea"):
        a_la_main.append(t.get("aria-label") or t.get("id") or "zone de texte")
    if not items:
        return None, a_la_main, refus
    bloc = ('<details class="correction %s">\n  <summary>✅ Correction complète du billet — ouvre-la après avoir vérifié</summary>\n'
            '  <ol class="corr-billet">\n%s\n  </ol>\n</details>' % (MARQUE, "\n".join(items)))
    return bloc, a_la_main, refus


def traiter(p: str, ecrire: bool, muet: bool):
    t = open(p, encoding="utf-8").read()
    script = {}
    for s in re.findall(r"<script[^>]*>(.*?)</script>", t, re.S):
        script.update(attendus_du_script(s))
    poses, restes, refus, main = 0, 0, [], []
    pos = 0
    while True:
        m = re.search(r"<h[23][^>]*>[^<]*(?:<[^>]+>[^<]*)*?</h[23]>", t[pos:])
        if not m:
            break
        h_debut, h_fin = pos + m.start(), pos + m.end()
        pos = h_fin
        if not TITRE.search(BeautifulSoup(m.group(0), "html.parser").get_text()):
            continue
        debut = max(t.rfind("<section", 0, h_debut), t.rfind("<div class=\"card", 0, h_debut))
        balise = "section" if t.startswith("<section", debut) else "div"
        fin = t.find("</%s>" % balise, h_fin)
        if debut < 0 or fin < 0:
            refus.append("bloc du billet introuvable autour de %r" % m.group(0)[:60]); continue
        span = t[debut:fin]
        autre = re.search(r'<details class="(?:correction|corrige)(?![^"]*%s)[^"]*"' % MARQUE, span)
        if autre:
            continue          # le billet a déjà sa correction, écrite à la main : on n'y touche pas
        bloc, a_la_main, r = correction(span, script, os.path.basename(p))
        refus += r; main += a_la_main
        if not bloc:
            continue
        deja = re.search(r'<details class="correction %s">.*?</details>' % MARQUE, span, re.S)
        if deja and deja.group(0) == bloc:
            continue
        restes += 1
        if not ecrire:
            continue
        if deja:
            span2 = span[:deja.start()] + bloc + span[deja.end():]
        else:
            fb = re.search(r'<p class="feedback[^"]*"[^>]*>\s*</p>', span)
            if fb:
                span2 = span[:fb.end()] + "\n  " + bloc + span[fb.end():]
            else:
                aide = span.find('<details class="aide')
                span2 = (span[:aide] + bloc + "\n  " + span[aide:]) if aide > 0 else span + "\n  " + bloc + "\n"
        t = t[:debut] + span2 + t[fin:]
        pos = debut + len(span2)
        poses += 1
    if ecrire and poses:
        open(p, "w", encoding="utf-8").write(t)
    nom = os.path.relpath(p, DEPOT)
    if not muet or refus or (restes and not ecrire):
        etat = "✘" if refus else ("✍ posée" if ecrire and poses else ("⚠ à poser" if restes else "✅"))
        print("%s %s%s" % (etat, nom, (" · à la main : " + ", ".join(main)) if main else ""))
        for r in refus:
            print("    · refus : " + r)
    return poses, (0 if ecrire else restes), refus


def main(argv):
    ecrire, muet = "--ecrire" in argv, "--muet" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    ps = pages(chemins)
    if not ps:
        print("✘ aucune page avec un billet d'entrée : rien n'a été vérifié"); return 2
    tot_p = tot_r = tot_ref = 0
    for p in ps:
        a, b, c = traiter(p, ecrire, muet)
        tot_p += a; tot_r += b; tot_ref += len(c)
    print("%d page(s) lues · %d correction(s) posée(s) · %d billet(s) sans correction · %d refus"
          % (len(ps), tot_p, tot_r, tot_ref))
    return 1 if (tot_r or tot_ref) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
