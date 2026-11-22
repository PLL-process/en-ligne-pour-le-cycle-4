# -*- coding: utf-8 -*-
"""tests_poser_main_qcm.py — `poser_main_qcm.py` éprouvé sur des cas dont on connaît la réponse (règle n°194).

Sortie : 0 tout passe · 1 un échec.
Usage : python3 _outils/tests_poser_main_qcm.py
"""
import os
import sys
import tempfile
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import poser_main_qcm as pm  # noqa: E402

NAV = '<nav id="navharm"><a href="../../index.html">⌂ Accueil</a></nav>\n'


class Arbre(HTMLParser):
    """Vrai si chaque balise fermante ferme la dernière ouverte (pas de chevauchement), et la profondeur du <main>."""

    def __init__(self, src):
        super().__init__()
        self.pile, self.ok, self.main_dans = [], True, None
        self.feed(src)

    def handle_starttag(self, tag, attrs):
        if tag in pm.VIDES:
            return
        if tag == "main":
            self.main_dans = [t for t in self.pile]
        self.pile.append(tag)

    def handle_endtag(self, tag):
        if not self.pile or self.pile[-1] != tag:
            self.ok = False
            if tag in self.pile:
                del self.pile[self.pile.index(tag):]
            return
        self.pile.pop()


def bien_forme(src):
    a = Arbre(src)
    return a.ok


CAS = [
    ("titre et pied au même niveau, navigation dehors", "posé",
     "<body>\n" + NAV + "<h1>QCM</h1>\n<div class=\"card\">q</div>\n<footer>pied</footer>\n</body>",
     lambda s: s.index('<main id="principal">') > s.index("</nav>") and s.index("</main>") < s.index("<footer>")),
    ("titre dans un en-tête : le <main> s'ouvre avant l'en-tête, au niveau du pied", "posé",
     "<body>\n" + NAV + "<header class=\"hero\"><h1>QCM</h1></header>\n<section>q</section>\n<footer>pied</footer>\n</body>",
     lambda s: s.index('<main id="principal">') < s.index('<header class="hero">')),
    ("tout dans un conteneur : le <main> reste dans le conteneur", "posé",
     "<body>\n" + NAV + "<div class=\"wrap\">\n<h1>QCM</h1>\n<p>q</p>\n<footer>pied</footer>\n</div>\n</body>",
     lambda s: s.index('<div class="wrap">') < s.index('<main id="principal">') and s.index("</main>") < s.index("</div>")),
    ("sans pied : fermeture avant la licence", "posé",
     "<body>\n" + NAV + "<h1>QCM</h1>\n<p>q</p>\n<p class=\"licence-cc\">CC BY-NC-SA</p>\n</body>",
     lambda s: s.index("</main>") < s.index('class="licence-cc"')),
    ("déjà posé : rien ne change (idempotent, n°149)", "déjà posé",
     "<body>\n" + NAV + "<main id=\"principal\">\n<h1>QCM</h1>\n</main>\n<footer>pied</footer>\n</body>", None),
    ("la navigation tomberait dedans : à la main", "la navigation tomberait dans le <main>",
     "<body>\n<div class=\"wrap\"><h1>QCM</h1>\n" + NAV + "<p>q</p></div>\n<footer>pied</footer>\n</body>", None),
    ("sans titre : à la main", "pas de <h1>", "<body>\n" + NAV + "<p>q</p>\n<footer>pied</footer>\n</body>", None),
]


def main():
    ok = 0
    for nom, attendu, src, verif in CAS:
        neuf, etat = pm.poser(src)
        bon = etat == attendu
        if bon and etat == "posé":
            bon = neuf.count('<main id="principal">') == 1 and neuf.count("</main>") == 1 and bien_forme(neuf) and verif(neuf)
            # idempotent : reposer ne change plus rien
            bon = bon and pm.poser(neuf) == (neuf, "déjà posé")
        if bon and etat != "posé":
            bon = neuf == src
        ok += bon
        print("%s %s — attendu « %s », obtenu « %s »" % ("✅" if bon else "❌", nom, attendu, etat))
    total = len(CAS)
    with tempfile.TemporaryDirectory() as d:
        r = pm.main([d])
        bon = r == 2
        ok += bon
        total += 1
        print("%s aucun QCM lu = EN PANNE (2)" % ("✅" if bon else "❌"))
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
