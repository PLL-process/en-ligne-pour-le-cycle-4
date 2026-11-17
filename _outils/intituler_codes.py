# -*- coding: utf-8 -*-
"""intituler_codes.py — chaque étiquette de code du programme dit sa compétence au survol (17/11/2026).

LE CONSTAT
----------
Pascal, le 17/11/2026, sur `3e_C4.1` : « En passant ma souris au-dessus de la puce, je ne vois pas à quoi correspond la
compétence. Comme c'est le cas dans les autres séquences. Vérifie que ce ne soit pas le cas partout. » Mesure du même
jour : 362 étiquettes de code (« 3e_C4.1 », « 4e_C7.1 · C7.2 · C7.3 », « 4e_C4.1 → C4.9 »…) dans les pages des trois
thèmes, **263 sans bulle**, dans 92 pages ; les 99 autres disaient « Programme 2024 — 5e_C2.1 : Faire la liste des
interacteurs extérieurs d'un objet ou système technique. » (Shenzhen, et quelques lots). La règle n°314 le demandait
pour le CRCN ; rien ne le vérifiait pour les codes du programme.

CE QUE FAIT L'OUTIL
-------------------
Une étiquette, c'est un élément `.badge…` (ou un enfant `span`, `a`, `li` d'un `.badges`) dont le texte porte un code
du programme. L'outil lit ses codes — `3e_C4.1` ; `C7.2` après un code de niveau (même niveau) ; `C4.1 → C4.9`, la
plage entière — et lui donne la bulle :

    title="Programme 2024 — 3e_C4.1 : Élaborer et dimensionner la chaîne d’énergie d’un objet ou système technique."

une ligne par code quand l'étiquette en porte plusieurs. Les intitulés viennent de `_outils/data_competences.py`, seule
autorité du dépôt ; le sigle OST y est écrit en toutes lettres (n°313). Une bulle déjà posée qui nomme chaque
intitulé est gardée ; une bulle « Code de rangement… » qui le paraphrase (4e_C2.1), ou l'intitulé seul avec son
sigle (4e_C1.1), est remplacée ; une bulle d'un autre contenu est signalée, jamais écrasée.

  python3 _outils/intituler_codes.py [--ecrire] [page.html | dossier …]   (sans chemin : les trois thèmes)
  python3 _outils/intituler_codes.py --etat [--strict]                    mesure ; --strict sort à 1 s'il en reste

Sortie : 0 rien à faire ou tout écrit · 1 il reste des étiquettes sans bulle (sans --ecrire, ou --strict) · 2 rien lu.
"""
from __future__ import annotations

import html
import os
import re
import sys

from bs4 import BeautifulSoup

OUT = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(OUT)
sys.path.insert(0, OUT)
import data_competences as DC  # noqa: E402

NIVEAUX = {"5": DC.COMP_5E, "4": DC.COMP_4E, "3": DC.COMP_3E}
CODE = re.compile(r"\b([345])e_C(\d)\.(\d+)\b")
JETON = re.compile(r"\b(?:([345])e_)?C(\d)\.(\d+)\b|→")
OST = [("de l’OST", "de l’objet ou du système technique"), ("plusieurs OST", "plusieurs objets ou systèmes techniques"), ("les OST", "les objets ou systèmes techniques"),
       ("d’OST", "d’objets ou de systèmes techniques"), ("l’OST", "l’objet ou le système technique"),
       ("nouvel OST", "nouvel objet ou système technique"), ("un OST", "un objet ou système technique")]


def intitule(niv: str, comp: str, sous: str):
    for code, texte, _ in NIVEAUX[niv].get("C" + comp, []):
        if code == "C%s.%s" % (comp, sous):
            for a, b in OST:
                texte = texte.replace(a, b)
            return texte.strip()
    return None


def codes_de(texte: str):
    """Les codes d'une étiquette, dans l'ordre : [(niveau, compétence, sous-compétence)]."""
    out, niv, plage = [], None, False
    for m in JETON.finditer(texte):
        if m.group(0) == "→":
            plage = True
            continue
        n, c, s = m.group(1) or niv, m.group(2), m.group(3)
        if not n:
            continue
        niv = n
        if plage and out and out[-1][0] == n and out[-1][1] == c:
            debut = int(out[-1][2])
            out += [(n, c, str(k)) for k in range(debut + 1, int(s) + 1) if intitule(n, c, str(k))]
        else:
            out.append((n, c, s))
        plage = False
    vus = []
    for x in out:
        if x not in vus:
            vus.append(x)
    return vus


def bulle(codes):
    lignes = []
    for n, c, s in codes:
        t = intitule(n, c, s)
        if t:
            lignes.append("%se_C%s.%s : %s" % (n, c, s, t))
    if not lignes:
        return None
    return "Programme 2024 — " + lignes[0] if len(lignes) == 1 else "Programme 2024 —\n" + "\n".join(lignes)


def etiquettes(soupe):
    for el in soupe.find_all(["span", "a", "li", "div", "p"]):
        cls = el.get("class") or []
        par = el.parent
        pcls = (par.get("class") or []) if par is not None else []
        if not (any("badge" in c for c in cls) or ("badges" in pcls and el.name in ("span", "a", "li"))):
            continue
        if el.find(class_=re.compile("badge")):
            continue
        texte = el.get_text(" ", strip=True)
        if CODE.search(texte):
            yield el, texte


def decalages(s: str):
    """Début de chaque ligne (1-indexée) dans le texte : pour retrouver une balise par sa position."""
    d, pos = [0, 0], 0
    for ligne in s.splitlines(keepends=True):
        pos += len(ligne)
        d.append(pos)
    return d


def sans_bulles(s: str) -> str:
    """Retire les bulles « Programme 2024 — … » : un générateur qui remplace les étiquettes de son gabarit les retrouve."""
    return re.sub(r' title="Programme 2024 —[^"]*"', "", s)


def poser_texte(s: str) -> str:
    """Pose les bulles dans un texte HTML (pour un générateur, juste avant d'écrire sa page)."""
    return analyser(s)[0]


def traiter(p: str, ecrire: bool):
    s = open(p, encoding="utf-8").read()
    if not CODE.search(s):
        return 0, 0, 0, []
    u, a_poser, deja, n, autres = analyser(s)
    if ecrire and u != s:
        open(p, "w", encoding="utf-8").write(u)
    return a_poser, deja, n, autres


def analyser(s: str):
    """(texte avec les bulles, étiquettes à poser, déjà à jour, bulles écrites, bulles d'un autre contenu)."""
    if not CODE.search(s):
        return s, 0, 0, 0, []
    soupe = BeautifulSoup(s, "html.parser")
    D = decalages(s)
    a_poser, deja, autres, edits = 0, 0, [], []
    for el, texte in etiquettes(soupe):
        voulu = bulle(codes_de(texte))
        if not voulu:
            continue
        titre = el.get("title") or ""
        if titre == voulu:
            deja += 1
            continue
        if titre and all(intitule(*c)[:40] in titre.replace("'", "’") or intitule(*c)[:40].replace("’", "'") in titre
                         for c in codes_de(texte) if intitule(*c)):
            deja += 1
            continue
        # une bulle « Code de rangement… » (4e_C2.1) paraphrasait sans donner l'intitulé : elle est remplacée
        brut = [t for n, c, x in codes_de(texte) for code, t, _ in NIVEAUX[n].get("C" + c, []) if code == "C%s.%s" % (c, x)]
        if titre and not titre.startswith(("Programme 2024", "Code de rangement")) and titre.strip() not in brut:
            autres.append("%s (bulle « %s »)" % (texte[:40], titre[:40]))
            continue
        a_poser += 1
        if el.sourceline is None:
            continue
        debut = D[el.sourceline] + el.sourcepos
        fin = s.index(">", debut)
        balise = s[debut:fin]
        attr = ' title="%s"' % html.escape(voulu, quote=True).replace("\n", "&#10;")
        if re.search(r'\stitle="[^"]*"', balise):
            neuve = re.sub(r'\stitle="[^"]*"', attr, balise, count=1)
        else:
            neuve = re.sub(r"^(<\w+)", r"\1" + attr, balise, count=1)
        edits.append((debut, fin, neuve))
    for debut, fin, neuve in sorted(edits, reverse=True):
        s = s[:debut] + neuve + s[fin:]
    return s, a_poser, deja, len(edits), autres


def pages(chemins):
    out = []
    for c in chemins or [os.path.join(DEPOT, t) for t in sorted(os.listdir(DEPOT)) if t.startswith("theme-")]:
        if os.path.isfile(c):
            out.append(c)
            continue
        for d, _, fs in os.walk(c):
            if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d:
                continue
            out += [os.path.join(d, f) for f in sorted(fs) if f.endswith(".html")]
    return sorted(out)


def main(argv):
    ecrire, etat, strict = "--ecrire" in argv, "--etat" in argv, "--strict" in argv
    ps = pages([a for a in argv if not a.startswith("--")])
    if not ps:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    tot_a = tot_d = tot_e = 0
    for p in ps:
        a, d, e, autres = traiter(p, ecrire and not etat)
        tot_a += a; tot_d += d; tot_e += e
        nom = os.path.relpath(p, DEPOT)
        if a and not (ecrire and not etat):
            print("  %s %s — %d étiquette(s) sans bulle" % ("✘" if strict else "⚠", nom, a))
        for x in autres:
            print("  ⚠ %s — bulle d'un autre contenu, à voir : %s" % (nom, x))
    if ecrire and not etat:
        print("%d page(s) lues · %d bulle(s) écrite(s) · %d déjà à jour" % (len(ps), tot_e, tot_d))
        return 0
    print("%d page(s) lues · %d étiquette(s) de code · %d avec leur bulle · %d sans"
          % (len(ps), tot_a + tot_d, tot_d, tot_a))
    return 1 if (tot_a and (strict or not etat)) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
