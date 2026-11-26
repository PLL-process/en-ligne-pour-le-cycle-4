#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bilan_rendu.py — le bilan, par famille de pages, des mesures de `mesures_rendu.py`.

Usage : python3 bilan_rendu.py <rendu.json>
Code de sortie (n°299) : 0 bilan fait · 2 aucune page mesurée.
"""
import json, statistics, sys
from collections import Counter, defaultdict
from pathlib import Path


def famille(nom):
    for prefixe, f in (("synthese_professeur", "synthèse prof"), ("synthese_eleve", "synthèse élève"), ("synthese", "synthèse"),
                       ("sequence", "séquence"), ("qcm", "QCM"), ("lexique", "lexique"), ("atelier", "atelier"), ("tp", "TP")):
        if nom.startswith(prefixe):
            return f
    return "autre"


def principal():
    res = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    mes = [x for x in res if "arrets" in x]
    if not mes:
        print("PANNE — aucune page mesurée (code 2)"); return 2
    print(f"{len(res)} pages · {len(mes)} mesurées · {sum('renvoi' in x for x in res)} renvois · {sum('panne' in x for x in res)} pannes")
    for x in res:
        if "panne" in x:
            print("  ✘", x["page"], "—", x["panne"])

    def tableau(titre, extraire, n=8):
        pages, total, par_fam, motifs, ou = 0, 0, Counter(), Counter(), defaultdict(set)
        for x in mes:
            d = extraire(x) or {}
            if d:
                pages += 1; par_fam[famille(x["page"].rsplit("/", 1)[-1])] += 1
                for k, v in d.items():
                    total += v; motifs[k] += v; ou[k].add(x["page"])
        print(f"\n## {titre} : {pages} pages, {total} occurrences  [{', '.join(f'{k} {v}' for k, v in par_fam.most_common())}]")
        for k, v in motifs.most_common(n):
            ex = sorted(ou[k])[0].rsplit("/", 1)[-1]
            print(f"   {v:>5} × {k[:70]:<70} ({len(ou[k])} pages, ex. {ex[:50]})")

    tableau("Contrôles focalisables sans nom accessible", lambda x: x["sans_nom"])
    tableau("Éléments à la souris seulement (curseur main, ni natifs ni au clavier)", lambda x: x["souris_seule"])
    tableau("Focus sans indicateur visible (60 premiers arrêts)", lambda x: x["focus_invisible"])
    tableau("Focus caché sous une barre collante", lambda x: x["focus_cache"])
    tableau("Texte de 3 lignes et plus à l'interligne sous 1,4", lambda x: x["texte"]["serre"])
    tableau("Texte affiché sous 12 px (1 280 px)", lambda x: x["texte"]["petit"], 12)
    tableau("Cibles sous 24 × 24 px à 390 px", lambda x: x["mobile"]["petites"], 12)

    print("\n## Défilement horizontal")
    for cle in ("deborde_390", "deborde_320"):
        fautes = [x for x in mes if x["mobile"][cle] > 1]
        print(f"   {cle} : {len(fautes)} pages" + "".join(f"\n      {x['page'].rsplit('/', 1)[-1][:60]} +{x['mobile'][cle]} px ({x['mobile']['large_' + cle[-3:]]})" for x in fautes[:8]))

    print("\n## Longueur de ligne à 1 280 px (caractères par ligne des paragraphes de 2 lignes et plus ; le dépôt vise 45 à 90)")
    par = defaultdict(list)
    for x in mes:
        par[famille(x["page"].rsplit("/", 1)[-1])] += x["texte"]["cpl"]
    for f, v in sorted(par.items(), key=lambda y: -len(y[1])):
        if v:
            print(f"   {f:<15} {len(v):>5} paragraphes · médiane {statistics.median(v):.0f} · au-delà de 90 : {100 * sum(c > 90 for c in v) / len(v):.0f} % · au-delà de 110 : {100 * sum(c > 110 for c in v) / len(v):.0f} %")

    print("\n## Hauteur de la page à 390 px, en écrans de téléphone (au chargement)")
    par = defaultdict(list)
    for x in mes:
        par[famille(x["page"].rsplit("/", 1)[-1])].append(x["mobile"]["ecrans_390"])
    for f, v in sorted(par.items(), key=lambda y: -statistics.median(y[1])):
        print(f"   {f:<15} {len(v):>4} pages · médiane {statistics.median(v):.0f} écrans · maximum {max(v):.0f}")

    print("\n## Parcours au clavier")
    arr = [x["arrets"] for x in mes]
    premiers = Counter((x["premier"] or "—")[:28] for x in mes)
    print(f"   arrêts avant de boucler (plafond 60) : médiane {statistics.median(arr):.0f} · pages au plafond : {sum(a >= 60 for a in arr)}")
    print("   premier arrêt :", " · ".join(f"« {k} » {v}" for k, v in premiers.most_common(5)))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(principal())
