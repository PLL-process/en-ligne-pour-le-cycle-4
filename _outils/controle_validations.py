# -*- coding: utf-8 -*-
"""controle_validations.py — une activité « validée » dit la vérité (règles d'or n°322 et n°333 ; audit de `3e_C4.1`, 17/11/2026).

LE CONSTAT
----------
L'audit externe de `3e_C4.1` du 17/11/2026 a lu le code des vérifications (`const CHECKS = {…}`) au lieu de regarder
l'écran : l'activité 1 annonçait « 11 / 11 » et validait à 10 ; l'activité 4 annonçait « 8 / 8 » et validait à 7, avec
une justification acceptée sur sa longueur et quelques mots (« vent sel vent sel… » passait) ; l'ordre des deux essais du
simulateur, exigé par la consigne, n'était pas vérifié ; une réponse changée après la vérification laissait l'activité
validée. Le skill `validations-qui-disent-vrai` en tire la méthode ; cet outil en mesure ce qui se lit dans le source.

CE QU'IL MESURE (pages élèves qui portent `const CHECKS = {`)
------------------------------------------------------------
  V1 ✘  le seuil codé n'est pas celui que l'activité annonce : « 🎯 Critère de réussite : 6 / 6 » et `valide: ok>=5` ;
  V1 ⚠  une tolérance que la page n'annonce pas : `valide: ok>=5` sur `total:6`, sans « 5 / 6 » ni « 5 sur 6 » écrit ;
  V3 ⚠  une réponse changée après la vérification ne retire pas la validation (aucun `__valid[…] = false`) ;
  V4 ⚠  une réponse écrite validée par la machine (longueur, `.length`, `mots.size`, mots-clés) sans que le message dise
        qu'elle sera relue par le professeur ;
  V5 ⚠  un simulateur (curseur `type="range"`) dont la page ne dit pas que son modèle est simplifié.

Ce qui ne se lit pas dans le source se juge à la main (skill `validations-qui-disent-vrai`) : l'ordre exigé de deux essais
(V2), une question qui affiche le résultat de la précédente (outil `controle_propositions_indices.py`, I3).

  python3 _outils/controle_validations.py [page.html | dossier …] [--muet] [--detail]

Sortie : 0 aucun ✘ · 1 un seuil codé contredit l'annonce (V1 ✘) · 2 aucune page lue (n°299).
"""
from __future__ import annotations

import html as H
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation", "_outils"}
ENTREE = re.compile(r"\n\s*(\d+)\s*:\s*function\s*\(\s*\)\s*\{")
SEUIL = re.compile(r"valide\s*:\s*([^}\n]*)")
TOTAL = re.compile(r"total\s*:\s*(\d+)")
OK_GE = re.compile(r"\bok\s*>=\s*(\d+)")
OK_EQ = re.compile(r"\bok\s*===?\s*(\d+)")
ANNONCE = re.compile(r"(\d+)\s*(?:/|sur|réponses? justes? sur|bonnes? réponses? sur|justes? sur)\s*(\d+)")
ECRIT = re.compile(r"\.length\s*>=?\s*\d|mots\.size|\btxt\(\s*[\"'][^\"']+[\"']\s*\)|\.test\(\s*j\s*\)")
RELU = re.compile(r"relue?s? par (ton|le|ta|votre) professeur|ton professeur (la|le) relira|à (faire )?relire", re.I)
REVOQUE = re.compile(r"__valid\s*\[[^\]]+\]\s*=\s*false")
SIMPLIFIE = re.compile(r"mod[èe]le simplifi|simulation (théorique )?simplifi|sans aucune perte|hypoth[èe]ses? du simulateur", re.I)


def pages(chemins):
    out = []
    for c in chemins or [os.path.join(DEPOT, t) for t in sorted(os.listdir(DEPOT)) if t.startswith("theme-")]:
        if os.path.isfile(c):
            out.append(c)
            continue
        for d, sous, fs in os.walk(c):
            sous[:] = [x for x in sous if x not in EXCLUS and not x.startswith(".banc")]
            out += [os.path.join(d, f) for f in sorted(fs)
                    if f.endswith(".html") and not f.lower().startswith("qcm") and "synthese" not in f.lower()]
    return sorted(out)


def texte(s: str) -> str:
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def entrees(src: str):
    """{numéro: corps de la fonction} des vérifications de la page."""
    i = src.find("const CHECKS")
    if i < 0:
        return {}
    fin = src.find("\n};", i)
    bloc = src[i: fin if fin > 0 else i + 40000]
    ms = list(ENTREE.finditer(bloc))
    return {m.group(1): bloc[m.end(): (ms[k + 1].start() if k + 1 < len(ms) else len(bloc))] for k, m in enumerate(ms)}


def critere(src: str, n: str) -> str:
    """Le critère de réussite affiché dans l'activité du bouton data-check=n (texte), ou ''."""
    corps = re.sub(r"<script\b.*?</script>", "", src, flags=re.S)
    for m in re.finditer(r'data-check="%s"' % re.escape(n), corps):
        debut = corps.rfind('class="activite"', 0, m.start())
        suite = corps.find('class="activite"', m.end())
        zone = corps[max(debut, 0): suite if suite > 0 else len(corps)]
        cs = list(re.finditer(r'class="critere"[^>]*>(.*?)</(?:div|p)>', zone, re.S))
        if cs:
            return texte(cs[-1].group(1))
    return ""


def analyser(src: str):
    """[(gravité, code, message)] d'une page."""
    out = []
    E = entrees(src)
    for n, corps in E.items():
        v = SEUIL.search(corps)
        t = TOTAL.search(corps)
        if not v or not t:
            continue
        total = int(t.group(1))
        ge, eq = OK_GE.search(v.group(1)), OK_EQ.search(v.group(1))
        seuil = int(ge.group(1)) if ge else int(eq.group(1)) if eq else None
        crit = critere(src, n)
        annonces = [(int(a), int(b)) for a, b in ANNONCE.findall(crit)]
        if seuil is not None:
            sur_total = [a for a, b in annonces if b == total]
            if sur_total and seuil not in sur_total:
                out.append(("✘", "V1", "activité %s : le critère annonce %s, le code valide à %d / %d"
                            % (n, " et ".join("%d / %d" % (a, total) for a in sur_total), seuil, total)))
            elif seuil < total and not sur_total:
                out.append(("⚠", "V1", "activité %s : le code valide à %d / %d, la page ne l'annonce pas (critère : « %s »)"
                            % (n, seuil, total, crit[:70] or "aucun")))
        if ECRIT.search(corps) and not RELU.search(corps):
            out.append(("⚠", "V4", "activité %s : une réponse écrite validée par la machine, sans « relue par ton professeur »" % n))
    if E and "data-check" in src and not REVOQUE.search(src):
        out.append(("⚠", "V3", "une réponse changée après la vérification ne retire pas la validation"))
    if 'type="range"' in src and E and not SIMPLIFIE.search(texte(src)):
        out.append(("⚠", "V5", "un simulateur à curseurs, sans dire que son modèle est simplifié"))
    return out


def main(argv):
    muet, detail = "--muet" in argv, "--detail" in argv
    ps = pages([a for a in argv if not a.startswith("--")])
    lues = avec = refus = 0
    compte = {}
    for p in ps:
        src = open(p, encoding="utf-8").read()
        lues += 1
        if "const CHECKS" not in src:
            continue
        avec += 1
        res = analyser(src)
        nom = os.path.relpath(p, DEPOT)
        for g, code, msg in res:
            compte[(g, code)] = compte.get((g, code), 0) + 1
            if g == "✘":
                refus += 1
            if g == "✘" or (detail and not muet):
                print("  %s %s %s — %s" % (g, code, nom, msg))
    if not lues:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    resume = " · ".join("%s %s : %d" % (g, c, k) for (g, c), k in sorted(compte.items()))
    print("%d page(s) lues · %d avec des vérifications · %s" % (lues, avec, resume or "rien à signaler"))
    if not detail and any(g == "⚠" for g, _ in compte):
        print("  (⚠ : une mesure ; --detail les nomme page par page)")
    return 1 if refus else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
