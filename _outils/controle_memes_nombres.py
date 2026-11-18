# -*- coding: utf-8 -*-
"""controle_memes_nombres.py — un même attendu se dit avec les mêmes nombres et les mêmes mots partout (règle d'or n°338).

LE CONSTAT
----------
Audit « double regard » du QCM de Shenzhen, transmis par Pascal le 17/11/2026 : « la consigne demande 8 interacteurs
de 4 familles, mais le critère final évoque 6 interacteurs et 3 natures » ; « le QCM annonce 4 questions illustrées ; la
séquence en annonce 5 ». Relus dans le dépôt, ces deux écarts n'y étaient plus — mais la relecture en a trouvé d'autres
du même genre : le positionnement « ⭐ … je pense aussi aux conditions et aux règles », alors que la leçon dit qu'une
règle n'est pas un interacteur ; et le message du bilan du QCM, « Fonctions, chaînes d'énergie et d'information,
matériaux et réseau n'ont plus de secret pour toi », recopié du gabarit dans 26 QCM qui ne parlent d'aucune de ces
notions. Un élève qui lit deux nombres pour un même attendu ne sait pas lequel croire.

CE QUI EST MESURÉ
-----------------
  N1  le QCM annoncé par une séquence ou par le README de son lot (« 34 questions, dont 8 illustrées ») n'a pas ce
      nombre de questions, ou pas ce nombre de questions illustrées (compté dans `const QUESTIONS`) ;
  N2  dans un même bloc d'activité, « au moins N <mot> » n'a pas le même N partout (fiche, consigne, critère) ;
  N3  le message du bilan d'un QCM (« Remarquable ! … ») est le même mot pour mot dans des QCM de lots différents :
      un reste du gabarit, qui parle d'autres notions que celles du QCM.
NON mesuré, à lire : qu'un positionnement ou une correction reprenne ce que la leçon écarte (le cas des « règles ») ;
le skill `audit-double-regard` le fait lire.

Usage : python3 _outils/controle_memes_nombres.py [--strict] [--muet] [chemin…]
Sortie : 0 (mesure ; ⚠ seulement) · 1 au moins un écart avec --strict · 2 rien lu.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOMBRES = {"un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8,
           "neuf": 9, "dix": 10, "douze": 12, "quinze": 15, "vingt": 20}
ANNONCE = re.compile(r"(\d+)\s*(?:</b>)?\s*questions?\s*(?:</b>)?\s*(?:,\s*dont|·)\s*(?:<b>)?\s*(\d+)\s*(?:</b>)?\s*illustr", re.I)
AU_MOINS = re.compile(r"au moins\s+(\d+|%s)\s+([a-zàâçéèêëîïôûùüÿœ'’-]{4,})" % "|".join(NOMBRES), re.I)
BILAN = re.compile(r'const msg= note>=16\?"([^"]*)"')


def texte(html: str) -> str:
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).replace("&nbsp;", " ")


def qcm_reel(chemin: str):
    s = open(chemin, encoding="utf-8").read()
    b = re.search(r"const QUESTIONS = \[(.*?)\n\];", s, re.S)
    if not b:
        return None
    return len(re.findall(r"\bq:\"", b.group(1))), len(re.findall(r"\bimg:\{", b.group(1)))


def lots(chemins):
    vus = set()
    for c in chemins or [DEPOT]:
        for d, _, fs in os.walk(c):
            if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d or "_exports" in d:
                continue
            if any(f.startswith("qcm") and f.endswith(".html") for f in fs) or any(f.startswith("sequence") for f in fs):
                vus.add(d)
    return sorted(vus)


def main(argv) -> int:
    strict, muet = "--strict" in argv, "--muet" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    ecarts = []
    lus = 0
    bilans = defaultdict(set)
    for d in lots(chemins):
        fichiers = os.listdir(d)
        qcms = {f: qcm_reel(os.path.join(d, f)) for f in fichiers if f.startswith("qcm") and f.endswith(".html")}
        qcms = {k: v for k, v in qcms.items() if v}
        for f in qcms:
            m = BILAN.search(open(os.path.join(d, f), encoding="utf-8").read())
            if m:
                bilans[m.group(1)].add(os.path.relpath(os.path.join(d, f), DEPOT))
        for f in fichiers:
            if not ((f.startswith("sequence") and f.endswith(".html")) or f == "README.md"):
                continue
            p = os.path.join(d, f)
            lus += 1
            s = open(p, encoding="utf-8").read()
            # N1 : l'annonce du QCM du lot
            if len(qcms) == 1:
                (nq, (vn, vi)), = qcms.items()
                for m in ANNONCE.finditer(s):
                    n, i = int(m.group(1)), int(m.group(2))
                    if (n, i) != (vn, vi):
                        ecarts.append(("N1", os.path.relpath(p, DEPOT), "annonce %d questions dont %d illustrées ; %s en a %d dont %d"
                                       % (n, i, nq, vn, vi)))
            # N2 : « au moins N mot », bloc par bloc
            if f.endswith(".html"):
                # un bloc : une section, ou une activité (plusieurs activités vivent dans la section de leur séance)
                for bloc in re.split(r"<section\b|<div class=\"activite[\" ]", s):
                    vus = defaultdict(set)
                    for m in AU_MOINS.finditer(texte(bloc)):
                        k = m.group(1).lower()
                        n = int(k) if k.isdigit() else NOMBRES[k]
                        mot = m.group(2).lower().rstrip("s")
                        vus[mot].add(n)
                    for mot, ns in vus.items():
                        if len(ns) > 1:
                            titre = re.search(r"<h[234][^>]*>(.*?)</h[234]>", bloc, re.S)
                            ecarts.append(("N2", os.path.relpath(p, DEPOT), "« au moins … %s » : %s, dans « %s »"
                                           % (mot, " / ".join(map(str, sorted(ns))), texte(titre.group(1))[:60] if titre else "?")))
    # N3 : le message du bilan, recopié d'un lot à l'autre
    for msg, ou in bilans.items():
        dossiers = {os.path.dirname(x) for x in ou}
        if len(dossiers) > 1:
            ecarts.append(("N3", "%d QCM" % len(ou), "« %s… » — le même message de bilan dans %d lots : %s"
                           % (msg[:70], len(dossiers), ", ".join(sorted(os.path.basename(x) for x in ou)[:6]) + (" …" if len(ou) > 6 else ""))))
    if not lus and not bilans:
        print("✘ rien n'a été lu : aucune séquence, aucun README, aucun QCM")
        return 2
    marque = "✘" if strict else "⚠"
    if not muet:
        for code, ou, dit in ecarts:
            print("  %s %s %s — %s" % (marque, code, ou, dit))
    par = defaultdict(int)
    for c, *_ in ecarts:
        par[c] += 1
    print("%d page(s) et README lus, %d message(s) de bilan · N1 annonce du QCM : %d · N2 « au moins N » : %d · N3 bilan recopié : %d"
          % (lus, len(bilans), par["N1"], par["N2"], par["N3"]))
    if not ecarts:
        print("✅ chaque attendu se dit avec les mêmes nombres partout, et chaque bilan parle de son QCM (règle d'or n°338)")
    return 1 if (strict and ecarts) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
