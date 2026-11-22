# -*- coding: utf-8 -*-
"""mesurer_entrelacement.py — le QCM entrelace ses compétences (règle d'or n°371, en essai).

LE CONSTAT (audit du 22/11/2026, PR #867)
-----------------------------------------
Sur 70 QCM du gabarit maison qui marquent leurs questions par compétence (`c:"…"`), 69 les posent PAR BLOCS : toutes
les questions d'une compétence, puis toutes celles de la suivante (médiane : 3 changements de compétence pour 30
questions). Le mode « 10 questions » prend un échantillon régulier ; le parcours complet garde l'ordre des blocs.
Or mélanger des questions de compétences voisines aide l'élève à les DISTINGUER (Rohrer et Taylor, 2007 ;
méta-analyse de Brunmair et Richter, 2019 : effet net quand les notions se ressemblent, plus faible ailleurs) — chaîne
d'énergie et chaîne d'information, formes d'énergie, capteur et actionneur.

LA RÈGLE (n°371, en essai)
--------------------------
Un QCM propose, à côté du parcours complet (dont l'ordre peut être voulu : une question posée avant un schéma), un
mode « 🔀 Entraînement mélangé » qui alterne les compétences, dans un ordre fixe (pas de hasard : deux élèves voisins
voient la même chose, et l'enseignant aussi).

CE QU'IL MESURE
---------------
Pour chaque `qcm*.html` (hors archives et `_outils`) qui porte `const QUESTIONS = [ … ]` avec au moins deux
compétences : le nombre de changements de compétence dans l'ordre du fichier, le maximum possible, et la présence d'un
bouton `data-mode="melange"`. `--ordre <fichier>` imprime l'ordre entrelacé proposé (indices), calculé par
`ordre_entrelace()` : un tour par compétence, tant qu'il en reste.

Mesure seulement : sortie 0 dès qu'au moins une banque est lue ; 2 EN PANNE si aucune (n°299).
Usage : python3 _outils/mesurer_entrelacement.py [chemins…] [--muet] [--ordre <qcm.html>]
"""
import os
import re
import statistics
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "_exports"}
BANQUE = re.compile(r"const\s+QUESTIONS\s*=\s*\[(.*?)\];", re.S)
CODE = re.compile(r'\bc\s*:\s*"([^"]+)"')
MODE = re.compile(r'data-mode="melange"')


def qcms(departs):
    for depart in departs:
        if os.path.isfile(depart):
            yield depart
            continue
        for dossier, sous, noms in os.walk(depart):
            sous[:] = sorted(d for d in sous if d not in IGNORES and not d.startswith("."))
            for nom in sorted(noms):
                if nom.startswith("qcm") and nom.endswith(".html"):
                    yield os.path.join(dossier, nom)


def codes_de(texte):
    m = BANQUE.search(texte)
    return CODE.findall(m.group(1)) if m else []


def changements(codes):
    return sum(1 for a, b in zip(codes, codes[1:]) if a != b)


def ordre_entrelace(codes):
    """Indices des questions, un tour par compétence (dans l'ordre de première apparition), tant qu'il en reste.
    Déterministe : la même banque donne toujours le même ordre."""
    files, ordre_c = {}, []
    for i, c in enumerate(codes):
        if c not in files:
            files[c] = []
            ordre_c.append(c)
        files[c].append(i)
    sortie = []
    while any(files[c] for c in ordre_c):
        for c in ordre_c:
            if files[c]:
                sortie.append(files[c].pop(0))
    return sortie


def main(argv):
    if "--ordre" in argv:
        f = argv[argv.index("--ordre") + 1]
        codes = codes_de(open(f, encoding="utf-8").read())
        o = ordre_entrelace(codes)
        print(" ".join(str(i + 1) for i in o))
        print(f"changements de compétence : {changements(codes)} → {changements([codes[i] for i in o])}")
        return 0 if codes else 2
    muet = "--muet" in argv
    departs = [a for a in argv if not a.startswith("--")] or [RACINE]
    lignes = []
    for chemin in qcms(departs):
        try:
            texte = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        codes = codes_de(texte)
        if len(codes) < 10 or len(set(codes)) < 2:
            continue
        maxi = changements([codes[i] for i in ordre_entrelace(codes)])
        lignes.append((os.path.relpath(chemin, RACINE), len(codes), len(set(codes)), changements(codes), maxi,
                       bool(MODE.search(texte))))
    if not lignes:
        print("⛔ EN PANNE : aucune banque marquée par compétence n'a été lue (n°299).")
        return 2
    par_blocs = [l for l in lignes if l[3] <= l[2]]
    avec_mode = [l for l in lignes if l[5]]
    if not muet:
        for rel, n, k, ch, mx, mode in lignes:
            print(f"{'·' if mode else '▫'} {rel} — {n} questions, {k} compétences, {ch} changement(s) sur {mx} possibles"
                  + (" · mode mélangé présent" if mode else ""))
    print(f"{len(lignes)} banque(s) lues · {len(par_blocs)} posées par blocs de compétence · médiane "
          f"{statistics.median(l[3] for l in lignes)} changement(s) · {len(avec_mode)} avec un mode « Entraînement mélangé »")
    print("📏 mesure (règle n°371 en essai) : aucune banque n'est refusée")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
