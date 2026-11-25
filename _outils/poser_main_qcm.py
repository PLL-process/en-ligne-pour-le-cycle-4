# -*- coding: utf-8 -*-
"""poser_main_qcm.py — chaque QCM a sa région principale `<main id="principal">` (accessibilité, 22/11/2026).

LE CONSTAT
----------
Audit de « Programmer l'alerte » (3e_C6.1), 22/11/2026 : axe-core signalait au QCM « landmark-one-main » et
« region » (le contenu n'est dans aucune région). Mesure sur tout le site le même jour : **77 QCM sur 78** n'avaient
pas de `<main>`. Un lecteur d'écran saute à la région principale d'une touche ; sans elle, l'élève qui l'utilise
traverse la barre de navigation à chaque page. Décision de Pascal (carte blanche, 22/11/2026) : poser le `<main>` sur
tous les QCM.

CE QUE FAIT L'OUTIL
-------------------
Il ouvre `<main id="principal">` juste avant le titre `<h1>` (ou avant l'élément qui le contient, au même niveau que le
pied de page) et le ferme juste avant le pied de page `<footer>` (ou, pour une page sans pied, avant la mention de
licence ou la fin du `<body>`). La barre de navigation `#navharm` reste dehors. Les deux bornes sont posées au même
niveau de l'arbre : jamais de `<main>` qui chevauche une `<div>`. Idempotent (n°149) : une page qui a déjà son
`<main>` n'est pas touchée.

CE QU'IL NE FAIT PAS (n°146)
----------------------------
Une page dont le titre et le pied n'ont pas d'ancêtre commun lisible, ou dont la navigation tomberait dans le `<main>`,
est listée « à poser à la main », pas modifiée. Les générateurs `_generation/build_qcm.py` partent d'un QCM existant
comme gabarit et remplacent le `<h1>` et le pied par expressions régulières : le `<main>` posé ici y survit.

Sortie : 0 rien à poser (ou tout posé avec --ecrire) · 1 des QCM sans `<main>` (sans --ecrire) ou à poser à la main ·
2 EN PANNE (aucun QCM lu).
Usage : python3 _outils/poser_main_qcm.py [chemins…] [--ecrire]
"""
import os
import re
import sys
from html.parser import HTMLParser

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEMES = ("theme-1-objets-systemes-usages-interactions", "theme-2-structure-fonctionnement-comportement",
          "theme-3-creation-conception-realisation-innovations")
VIDES = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
OUVRE = '<main id="principal">\n'
FERME = '</main>\n'


class Relevé(HTMLParser):
    """La pile des éléments ouverts à chaque balise d'intérêt, avec les positions dans le texte."""

    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src, self.pile, self.vus = src, [], {}
        self.lignes = [0]
        for m in re.finditer("\n", src):
            self.lignes.append(m.end())
        self.feed(src)

    def pos(self):
        ligne, col = self.getpos()
        return self.lignes[ligne - 1] + col

    def handle_starttag(self, tag, attrs):
        p = self.pos()
        a = dict(attrs)
        if tag == "h1" and "h1" not in self.vus:
            self.vus["h1"] = (p, list(self.pile))
        if tag == "nav" and a.get("id") == "navharm":
            self.vus["nav"] = (p, list(self.pile))
        if tag == "footer":
            self.vus["footer"] = (p, list(self.pile))        # le dernier pied de page
        if tag == "main":
            self.vus["main"] = (p, list(self.pile))
        if tag == "p" and "licence-cc" in (a.get("class") or "") and "licence" not in self.vus:
            self.vus["licence"] = (p, list(self.pile))
        if tag not in VIDES:
            self.pile.append((tag, p))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag == "body" and "finbody" not in self.vus:
            self.vus["finbody"] = (self.pos(), list(self.pile[:-1]) if self.pile and self.pile[-1][0] == "body" else list(self.pile))
        for i in range(len(self.pile) - 1, -1, -1):
            if self.pile[i][0] == tag:
                del self.pile[i:]
                break


def bornes(src):
    """(ouverture, fermeture) ou (None, raison)."""
    r = Relevé(src)
    if "main" in r.vus:
        return None, "déjà posé"
    if "h1" not in r.vus:
        return None, "pas de <h1>"
    fin = r.vus.get("footer") or r.vus.get("licence") or r.vus.get("finbody")
    if not fin:
        return None, "ni pied de page ni fin de <body>"
    (ph1, pile_h1), (pfin, pile_fin) = r.vus["h1"], fin
    commun = 0
    while commun < min(len(pile_h1), len(pile_fin)) and pile_h1[commun] == pile_fin[commun]:
        commun += 1
    ouv = pile_h1[commun][1] if commun < len(pile_h1) else ph1
    fer = pile_fin[commun][1] if commun < len(pile_fin) else pfin
    if fer <= ouv:
        return None, "le pied de page précède le titre"
    if "nav" in r.vus and ouv <= r.vus["nav"][0] < fer:
        return None, "la navigation tomberait dans le <main>"
    return (ouv, fer), ""


def poser(src):
    b, raison = bornes(src)
    if not b:
        return src, raison
    ouv, fer = b
    debut_ligne = src.rfind("\n", 0, fer) + 1
    fer = debut_ligne if src[debut_ligne:fer].strip() == "" else fer
    debut_ligne = src.rfind("\n", 0, ouv) + 1
    ouv = debut_ligne if src[debut_ligne:ouv].strip() == "" else ouv
    return src[:ouv] + OUVRE + src[ouv:fer] + FERME + src[fer:], "posé"


def pages(chemins):
    if not chemins:
        chemins = [os.path.join(RACINE, t) for t in THEMES]
    for c in chemins:
        if os.path.isfile(c):
            yield c
            continue
        for d, sous, fichiers in os.walk(c):
            sous[:] = [s for s in sous if not s.startswith("_") and s not in (".git", "node_modules")]
            for f in sorted(fichiers):
                if f.startswith("qcm") and f.endswith(".html"):
                    yield os.path.join(d, f)


def main(argv):
    ecrire = "--ecrire" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    lus, poses, deja, main_ = 0, [], 0, []
    for p in pages(chemins):
        src = open(p, encoding="utf-8").read()
        lus += 1
        neuf, etat = poser(src)
        rel = os.path.relpath(p, RACINE)
        if etat == "déjà posé":
            deja += 1
        elif etat == "posé":
            poses.append(rel)
            if ecrire:
                open(p, "w", encoding="utf-8").write(neuf)
        else:
            main_.append((rel, etat))
    print("Région principale des QCM — %d QCM lus : %d avec <main>, %d %s, %d à poser à la main"
          % (lus, deja, len(poses), "posés" if ecrire else "sans <main> (à poser : --ecrire)", len(main_)))
    if lus == 0:
        print("✘ EN PANNE : aucun QCM lu (n°299).")
        return 2
    for rel, etat in main_:
        print("  ✘ %s — %s" % (rel, etat))
    if not ecrire:
        for rel in poses[:10]:
            print("  · %s" % rel)
    return 1 if main_ or (poses and not ecrire) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
