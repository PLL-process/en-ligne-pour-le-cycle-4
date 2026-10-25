# -*- coding: utf-8 -*-
"""controle_sigles.py — règle d'or n°313 : un sigle garde ses capitales.

LE CONSTAT
----------
Le 25/10/2026, Pascal : « FAST doit toujours être écrit en majuscules, car je l'ai vu en minuscules ». C'était
l'index du site : « Activité — Diagramme fast », cinq fois. Le libellé y est tiré du nom de fichier
(`atelier_diagramme_fast.html`), écrit en minuscules ; le même mécanisme donnait « Dnb algorigrammes »,
« Pix crcn jardin », « Repartir qcm », « Adressage ip ». FAST est un sigle (Function Analysis System
Technique) : en minuscules, il se lit comme le mot anglais « fast », rapide — c'est même un distracteur du QCM
de l'atelier.

LA RÈGLE
--------
Un sigle s'écrit toujours dans sa forme : FAST, QCM, DNB, CRCN, SysML… dans le texte, les titres, les
libellés de l'index, les options et les messages. Les noms de fichiers, les adresses et les identifiants
de code ne changent pas (`qcm_fast.html`, `module="fast"`) : ce ne sont pas des textes lus.

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Pages lues : toutes les pages HTML sous theme-* (élève et professeur) et les schémas SVG (leur texte, leur
titre, leur description), hors archive et dossiers « _… », plus l'index et le README racine (fichiers
engendrés par `make_index.py`).
Textes lus : le texte de la page (hors <script>, <style>, <pre>, <code>), le <title>, les attributs lus par
l'élève ou par un lecteur d'écran (title, alt, aria-label, placeholder), et les chaînes du JavaScript de la
page (questions de QCM, messages des vérificateurs). Dans le README, le texte hors `code`.

Mesuré : chaque sigle de la liste SIGLES, écrit comme un mot (pas collé à « _ », « . », « / », « - »), a
exactement la forme de la liste.

Toléré, et pourquoi :
  - le mot cité entre guillemets français, « fast » : c'est le mot anglais dont le QCM parle ;
  - une chaîne JavaScript qui n'est qu'un identifiant (« "gps" », clé d'un objet) : elle n'est pas lue.

NON mesuré : le texte des images PNG ; les fichiers Markdown autres que le README racine (rapports de tests,
fiches, où « fast » est souvent le nom du module) ; « IP » (la commande Cisco « ip route » s'écrit en
minuscules) ; « wifi » (nom commun, écrit en minuscules par l'usage).

Usage : python3 _outils/controle_sigles.py [--muet] [chemin…]
Sortie : 0 rien à reprendre · 1 au moins un sigle mal écrit · 2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import os
import re
import sys
import warnings

from bs4 import BeautifulSoup, Comment, MarkupResemblesLocatorWarning, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIGLES = ["FAST", "QCM", "DNB", "CRCN", "SysML", "SADT", "UML", "NFC", "RFID", "CAO", "DAO", "TBT", "LCD",
          "GPS", "USB"]
MOT = re.compile(r"(?<![\w./@\\-])(%s)(?![\w/@\\-]|\.\w)" % "|".join(SIGLES), re.I)
FORME = {s.lower(): s for s in SIGLES}
CHAINE_JS = re.compile(r'"((?:[^"\\\n]|\\.)*)"|\'((?:[^\'\\\n]|\\.)*)\'|`((?:[^`\\]|\\.)*)`', re.S)


def pages(racines):
    vues = set()
    for r in racines:
        r = os.path.abspath(r)
        if os.path.isfile(r):
            vues.add(r)
            continue
        for d, sous, fichiers in os.walk(r):
            rel = os.path.relpath(d, DEPOT)
            sous[:] = [s for s in sous if not s.startswith((".", "_", "node_modules"))]
            if rel == "." and r == DEPOT:
                sous[:] = [s for s in sous if s.startswith("theme-")]
                for f in ("index.html", "README.md"):
                    if f in fichiers:
                        vues.add(os.path.join(d, f))
                continue
            for f in fichiers:
                if f.endswith((".html", ".svg")):
                    vues.add(os.path.join(d, f))
    return sorted(vues)


def textes(chemin):
    """Les textes lus d'une page : [(provenance, texte)]."""
    src = open(chemin, encoding="utf-8", errors="replace").read()
    if chemin.endswith(".md"):
        return [("texte", re.sub(r"`[^`]*`", " ", src))]
    out = []
    soup = BeautifulSoup(src, "html.parser")
    for sc in soup.find_all("script"):
        for m in CHAINE_JS.finditer(sc.string or sc.get_text() or ""):
            t = next(g for g in m.groups() if g is not None)
            if re.fullmatch(r"[\w-]+", t):  # un identifiant, pas un texte lu
                continue
            out.append(("script", BeautifulSoup(t, "html.parser").get_text(" ")))
    for t in soup(["script", "style", "pre", "code", "template"]):
        t.decompose()
    for c in soup.find_all(string=lambda x: isinstance(x, Comment)):
        c.extract()
    out.append(("texte", soup.get_text(" ")))
    for t in soup.find_all(True):
        for a in ("title", "alt", "aria-label", "placeholder"):
            if t.get(a):
                out.append((a, str(t.get(a))))
    return out


def ecarts(chemin):
    res = []
    for prov, t in textes(chemin):
        for m in MOT.finditer(t):
            mot = m.group(1)
            bonne = FORME[mot.lower()]
            if mot == bonne:
                continue
            avant, apres = t[max(0, m.start() - 2):m.start()], t[m.end():m.end() + 2]
            if "«" in avant and "»" in apres:  # le mot cité : « fast », le mot anglais
                continue
            res.append(dict(provenance=prov, ecrit=mot, forme=bonne,
                            extrait=re.sub(r"\s+", " ", t[max(0, m.start() - 35):m.end() + 25]).strip()))
    return res


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    muet = "--muet" in argv
    cibles = [a for a in argv if not a.startswith("--")] or [DEPOT]
    liste = pages(cibles)
    if not liste:
        print("⛔ PANNE — aucune page lue sous %s : un contrôle qui n'a rien lu n'est pas vert (règle d'or n°299)."
              % ", ".join(cibles), file=sys.stderr)
        return 2
    total, pages_ko, lus = 0, 0, 0
    for p in liste:
        e = ecarts(p)
        lus += 1
        if e:
            pages_ko += 1
            total += len(e)
            if not muet:
                print("✘ %s" % os.path.relpath(p, DEPOT))
                for x in e:
                    print("    « %s » au lieu de « %s » (%s) — …%s…" % (x["ecrit"], x["forme"], x["provenance"], x["extrait"]))
    print("%d page(s) lues · sigles suivis : %s" % (lus, ", ".join(SIGLES)))
    if total:
        print("✘ %d sigle(s) mal écrit(s), dans %d page(s) (règle d'or n°313)" % (total, pages_ko))
        return 1
    print("✅ chaque sigle garde ses capitales (règle d'or n°313)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
