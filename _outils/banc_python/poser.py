#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Poser dans une page le petit Python de la page (banc_python.js), entre ses marqueurs, ou dire si la copie est à jour.

Pourquoi (audit de « Programmer l'alerte », 3e_C6.1, 21/11/2026 ; règle d'or n°369) : une validation de programme
exécute le programme de l'élève et compare ses sorties au cahier des charges ; elle ne cherche pas des motifs dans
son texte. La page reste monofichier et hors ligne (règle d'or n°305) : le script est COPIÉ dans la page, comme le
mode mission ; la source unique est `_outils/banc_python/banc_python.js`.

Usage :
    python3 _outils/banc_python/poser.py <page.html>              # pose ou remplace le bloc
    python3 _outils/banc_python/poser.py <page.html> --verifier   # sortie 1 si la copie diffère de la source
    python3 _outils/banc_python/poser.py --verifier-tout [racine] # toutes les pages qui portent le bloc
Le bloc se pose juste avant le premier `<script>` qui suit `</footer>` (le script de la page, qui s'en sert) ; à
défaut, avant `</body>`. Sortie 2 si rien n'a été lu (règle d'or n°299).
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "banc_python.js"
DEBUT = "<!-- banc-python v1 : début — un petit Python exécuté dans la page, hors ligne ; source unique : _outils/banc_python/ (poser.py). Ne pas le modifier dans la page. -->"
FIN = "<!-- banc-python v1 : fin -->"
BLOC_RE = re.compile(re.escape("<!-- banc-python v1 : début") + r".*?" + re.escape(FIN), re.S)


def bloc():
    return DEBUT + "\n<script>\n" + SOURCE.read_text(encoding="utf-8").rstrip() + "\n</script>\n" + FIN


def poser(chemin):
    s = chemin.read_text(encoding="utf-8")
    neuf = bloc()
    if BLOC_RE.search(s):
        s2 = BLOC_RE.sub(lambda m: neuf, s, count=1)
    else:
        i = s.find("</footer>")
        j = s.find("<script", i) if i >= 0 else -1
        if j < 0:
            j = s.rfind("</body>")
        if j < 0:
            print("✘ ni </footer> suivi d'un script, ni </body> : rien posé dans", chemin)
            return 1
        s2 = s[:j] + neuf + "\n" + s[j:]
    if s2 != s:
        chemin.write_text(s2, encoding="utf-8")
        print("✔ banc-python posé dans", chemin)
    else:
        print("= banc-python déjà à jour dans", chemin)
    return 0


def verifier(chemin):
    s = chemin.read_text(encoding="utf-8")
    m = BLOC_RE.search(s)
    if not m:
        print("✘ pas de bloc banc-python dans", chemin)
        return 1
    if m.group(0) != bloc():
        print("✘ la copie de banc-python diffère de la source :", chemin, "— rejouer poser.py")
        return 1
    if len(BLOC_RE.findall(s)) > 1:
        print("✘ deux blocs banc-python dans", chemin)
        return 1
    print("✔ banc-python à jour :", chemin)
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--verifier-tout":
        racine = pathlib.Path(argv[1] if len(argv) > 1 else ".")
        pages = [p for p in racine.rglob("*.html") if "_archive" not in p.parts and "banc-python v1 : début" in p.read_text(encoding="utf-8", errors="ignore")]
        if not pages:
            print("rien n'a été lu : aucune page ne porte le bloc banc-python (n°299)")
            return 2
        return max(verifier(p) for p in pages)
    chemin = pathlib.Path(argv[0])
    if not chemin.is_file():
        print("✘ fichier introuvable :", chemin)
        return 2
    return verifier(chemin) if "--verifier" in argv[1:] else poser(chemin)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
