# -*- coding: utf-8 -*-
"""tests_controle_boutons_vivants.py — le banc du contrôle « un bouton appelle une fonction qui existe ».

Chaque cas rejoue une forme rencontrée dans le dépôt :
  · `onclick="checkSection('chk1')"` sans `function checkSection` nulle part (4e_C1.4, 09/09/2026) ;
  · `x.onclick = () => checkSection('chk1')` — la même absence, par affectation ;
  · une fonction définie par `const f = () =>`, par `window.f =`, par `function f(` : acceptées ;
  · un appel natif (`window.print()`, `document.getElementById(...)`) : ignoré ;
  · l'archive : écartée ;
  · le dépôt réel : doit passer.

Usage : python3 _outils/tests_controle_boutons_vivants.py
"""

import contextlib
import io
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_boutons_vivants as C  # noqa: E402


def page(corps, script=""):
    return ("<!doctype html><html><head><meta charset=\"utf-8\"></head><body>%s"
            "<script>%s</script></body></html>\n" % (corps, script))


def jouer(racine):
    ancien = C.DEPOT
    C.DEPOT = str(racine)
    sortie = io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie):
            code = C.main()
    finally:
        C.DEPOT = ancien
    return code, sortie.getvalue()


def main():
    echecs, controles = [], 0

    def cas(titre, fichiers, doit_refuser, attendu=""):
        nonlocal controles
        controles += 1
        with tempfile.TemporaryDirectory() as tmp:
            for ch, contenu in fichiers.items():
                p = pathlib.Path(tmp) / ch
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if doit_refuser and code == 0:
            echecs.append("%s : accepté, alors qu'il fallait refuser\n     %s" % (titre, texte.strip()))
        elif not doit_refuser and code != 0:
            echecs.append("%s : refusé\n     %s" % (titre, texte.strip()))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s" % (titre, attendu, texte.strip()))

    cas("un onclick vers une fonction absente (4e_C1.4)",
        {"lot/sequence_x.html": page('<button onclick="checkSection(\'chk1\')">Vérifier</button>')},
        True, "checkSection()")
    cas("une affectation .onclick vers une fonction absente",
        {"lot/sequence_x.html": page('<button id="chk1">Vérifier</button>',
                                     "document.getElementById('chk1').onclick = () => checkSection('chk1');")},
        True, "checkSection()")
    cas("function f( — acceptée",
        {"lot/sequence_x.html": page('<button onclick="verifier(1)">ok</button>', "function verifier(n){}")}, False)
    cas("const f = () => — acceptée",
        {"lot/sequence_x.html": page('<button onclick="verifier()">ok</button>', "const verifier = () => 1;")}, False)
    cas("window.f = — acceptée",
        {"lot/sequence_x.html": page('<button onclick="verifier()">ok</button>', "window.verifier = function(){};")}, False)
    cas("les appels natifs sont ignorés",
        {"lot/sequence_x.html": page('<button onclick="window.print()">PDF</button>'
                                     '<button onclick="document.getElementById(\'x\').scrollIntoView()">↓</button>')},
        False, "chaque bouton appelle")
    cas("l'archive est écartée",
        {"_archive-anciennes-versions/vieux.html": page('<button onclick="fantome()">x</button>')}, False)

    controles += 1
    code, texte = jouer(C.DEPOT)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip().replace("\n", "\n     "))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — un bouton mort ne passe plus sans bruit" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
