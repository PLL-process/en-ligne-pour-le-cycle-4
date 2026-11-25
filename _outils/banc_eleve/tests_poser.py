# -*- coding: utf-8 -*-
"""tests_poser.py — `poser.py` du banc-eleve éprouvé sur des cas dont on connaît la réponse (règle n°194).

Sortie : 0 tout passe · 1 un échec.
Usage : python3 _outils/banc_eleve/tests_poser.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import poser  # noqa: E402

JS, CSS = poser.source()
TABLE = "const BANC_ELEVE = {vs1: {essais: []}};\n"


def page(js, css=CSS):
    return "<html><head>" + css + "</head><body><script>" + TABLE + js + "</script></body></html>"


def main():
    ok = total = 0

    def cas(nom, bon):
        nonlocal ok, total
        total += 1
        ok += bool(bon)
        print("%s %s" % ("✅" if bon else "❌", nom))

    cas("la source porte ses deux marques, début et fin", JS.startswith("/* banc-eleve v1 : début") and JS.endswith("/* banc-eleve v1 : fin */\n"))
    cas("une page sans le banc : « absent »", poser.etat("<html></html>", JS, CSS) == "absent")
    cas("une page avec le cœur et le style de la source : « identique »", poser.etat(page(JS), JS, CSS) == "identique")
    retouche = JS.replace("1500", "15000", 1)
    cas("un cœur retouché dans la page : « différent »", poser.etat(page(retouche), JS, CSS) == "différent")
    cas("un style retouché dans la page : « différent »", poser.etat(page(JS, CSS.replace("#15803d", "#00ff00")), JS, CSS) == "différent")
    remis = poser.remettre(page(retouche), JS, CSS)
    cas("remettre : le cœur redevient celui de la source", poser.etat(remis, JS, CSS) == "identique")
    cas("remettre : la table BANC_ELEVE de la page, hors des marques, ne bouge pas", TABLE in remis)
    sans_style = page(JS, css="")
    cas("remettre : un style manquant est posé avant </head>", poser.etat(poser.remettre(sans_style, JS, CSS), JS, CSS) == "identique")
    cas("le site : chaque page qui porte le banc est identique à la source (sortie 0)", poser.main(["--verifier-tout"]) == 0)
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
