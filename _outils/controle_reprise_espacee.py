# -*- coding: utf-8 -*-
"""controle_reprise_espacee.py — ce qui compte revient (règles d'or n°369 et n°372, en essai).

LE CONSTAT (audit du 22/11/2026, PR #867)
-----------------------------------------
Le volet « 📖 Rappel » (n°311) RÉEXPLIQUE à l'élève ce qu'il a vu ; il ne lui fait pas RETROUVER. Or le fait de
retrouver de mémoire, à quelques jours d'intervalle, est ce qui fait tenir un acquis (effet de test et espacement :
Roediger et Karpicke, 2006 ; Cepeda et al., 2006 ; méta-analyse d'Adesope et al., 2017). Mesuré le 22/11 : sur les
113 séances n°2 et suivantes des 60 pages de séquence, 8 au plus s'ouvrent sur une question de mémoire. Le « rappel en
début de séance » était noté « à concevoir » dans `docs/mode-mission/PLAN.md` depuis le 11/11.

LES RÈGLES
----------
n°369 (clé de voûte) — Ce qui compte revient. Toute séance, à partir de la deuxième, s'ouvre sur un bloc de reprise :
au moins deux questions de récupération, posées AVANT tout rappel déplié, sur ce qui a été appris dans une séance
précédente. La correction de la reprise renvoie au rappel.
n°372 — Le bilan dit ce qui reste flou et quand on le reprend.

CE QU'IL MESURE
---------------
Dans chaque page de séquence (`sequence*.html`, hors archives et `_outils`) :
  R1  chaque panneau de séance `id="s2"`, `id="s3"`… contient un bloc `data-reprise` (balise quelconque) ;
  R2  ce bloc porte au moins deux questions (`fieldset`, ou éléments `data-question`) ;
  R3  il vient AVANT le volet « 📖 Rappel » (`details.rappel-ouverture`) quand la séance en a un ;
  R4  le bilan de la page (un élément `data-bilan`, ou le bloc titré « Bilan ») contient un champ `data-flou`
      (« ce qui reste flou, et quand je le reprends »).
Ce que la machine ne peut pas juger : que les questions portent bien sur une séance précédente, et sur un acquis
qui compte (🔑, n°353). Le skill `reprise-espacee` le fait relire.

STATUT : MESURE (règles en essai, n°147)
----------------------------------------
Sans option, il compte et sort à 0 : la règle est en essai, la mesure de départ est presque nulle partout, et un
rouge permanent apprendrait à ne plus regarder. Avec `--strict`, il sort à 1 dès qu'une séance ≥ 2 n'a pas sa
reprise. Il passera en contrôle (référence datée, n°273) quand Pascal aura adopté la règle.

Sortie : 0 mesure faite (ou rien à redire) · 1 avec --strict, au moins un manque · 2 EN PANNE (aucune page lue, n°299).
Usage : python3 _outils/controle_reprise_espacee.py [chemins…] [--strict] [--muet]
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "_exports"}

#: un panneau de séance est un <div> OU une <section> (4e_C1.4, entre autres : vu au pilote du 22/11/2026)
PANNEAU = re.compile(r'<(?:div|section)\b[^>]*\bclass="[^"]*\bseance-panel\b[^"]*"[^>]*\bid="s(\d+)"[^>]*>'
                     r'|<(?:div|section)\b[^>]*\bid="s(\d+)"[^>]*\bclass="[^"]*\bseance-panel\b[^"]*"[^>]*>')
REPRISE = re.compile(r'<(\w+)\b[^>]*\bdata-reprise\b[^>]*>')
RAPPEL = re.compile(r'<details\b[^>]*\bclass="[^"]*\brappel-ouverture\b')
QUESTION = re.compile(r'<fieldset\b|\bdata-question\b')
BILAN = re.compile(r'\bdata-bilan\b|<h[23][^>]*>[^<]*\bBilan\b', re.I)
FLOU = re.compile(r'\bdata-flou\b')


def pages(departs):
    for depart in departs:
        if os.path.isfile(depart):
            yield depart
            continue
        for dossier, sous, noms in os.walk(depart):
            sous[:] = sorted(d for d in sous if d not in IGNORES and not d.startswith("."))
            for nom in sorted(noms):
                if nom.startswith("sequence") and nom.endswith(".html"):
                    yield os.path.join(dossier, nom)


def fin_du_bloc(texte, debut, balise):
    """Fin approximative de l'élément ouvert en `debut` : on compte les balises de même nom."""
    ouvre = re.compile(r'<%s\b' % balise, re.I)
    ferme = re.compile(r'</%s\s*>' % balise, re.I)
    i, prof = debut + 1, 1
    while prof and i < len(texte):
        o, f = ouvre.search(texte, i), ferme.search(texte, i)
        if not f:
            return len(texte)
        if o and o.start() < f.start():
            prof, i = prof + 1, o.end()
        else:
            prof, i = prof - 1, f.end()
    return i


def mesurer_page(texte):
    """Rend (séances ≥ 2, manques par séance [(n, code)], bilan_avec_flou: bool|None)."""
    reperes = [(m.start(), int(m.group(1) or m.group(2))) for m in PANNEAU.finditer(texte)]
    manques, compte = [], 0
    for k, (pos, n) in enumerate(reperes):
        if n < 2:
            continue
        compte += 1
        fin = reperes[k + 1][0] if k + 1 < len(reperes) else len(texte)
        corps = texte[pos:fin]
        r = REPRISE.search(corps)
        if not r:
            manques.append((n, "R1 pas de bloc data-reprise"))
            continue
        bloc = corps[r.start():fin_du_bloc(corps, r.start(), r.group(1))]
        if len(QUESTION.findall(bloc)) < 2:
            manques.append((n, "R2 moins de deux questions dans la reprise"))
        rap = RAPPEL.search(corps)
        if rap and rap.start() < r.start():
            manques.append((n, "R3 la reprise vient après le « 📖 Rappel » déplié"))
    b = BILAN.search(texte)
    flou = None if not b else bool(FLOU.search(texte, b.start()))
    return compte, manques, flou


def main(argv):
    strict, muet = "--strict" in argv, "--muet" in argv
    departs = [a for a in argv if not a.startswith("--")] or [RACINE]
    lues = seances = sans = 0
    sans_flou, detail = 0, []
    for chemin in pages(departs):
        try:
            texte = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        lues += 1
        n, manques, flou = mesurer_page(texte)
        seances += n
        sans += len(manques)
        if flou is False:
            sans_flou += 1
        if manques or flou is False:
            detail.append((os.path.relpath(chemin, RACINE), manques, flou))
    if not lues:
        print("⛔ EN PANNE : aucune page de séquence lue (n°299).")
        return 2
    if not muet:
        for rel, manques, flou in detail:
            print(rel)
            for n, code in manques:
                print(f"   · séance {n} : {code}")
            if flou is False:
                print("   · R4 le bilan ne demande pas ce qui reste flou ni quand on le reprend (data-flou)")
    print(f"{lues} page(s) de séquence lues · {seances} séance(s) n°2 et suivantes · {sans} sans reprise conforme · "
          f"{sans_flou} bilan(s) sans « ce qui reste flou »")
    print("ℹ Non vu : que la reprise porte sur une séance PRÉCÉDENTE et sur un acquis 🔑 (skill `reprise-espacee`).")
    if strict and (sans or sans_flou):
        print("✘ ce qui compte revient : chaque séance ≥ 2 s'ouvre sur une reprise — règles d'or n°369 et n°372 (--strict)")
        return 1
    if sans or sans_flou:
        print("📏 mesure (règles n°369 et n°372 en essai) : rien n'est refusé sans --strict")
        return 0
    print("✅ chaque séance n°2 et suivante s'ouvre sur une reprise, et chaque bilan dit ce qui reste flou")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
