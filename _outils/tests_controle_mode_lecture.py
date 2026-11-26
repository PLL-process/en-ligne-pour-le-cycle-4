# -*- coding: utf-8 -*-
"""tests_controle_mode_lecture.py — le contrôle du mode lecture éprouvé sur des cas dont on connaît la réponse (n°194).

Sortie : 0 tout passe · 1 un échec.
Usage : python3 _outils/tests_controle_mode_lecture.py
"""
import contextlib
import io
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_mode_lecture as c  # noqa: E402

BLOC = c.poser_lecture.bloc()
CORPS = "<h1>Synthèse</h1><section><h2>Un</h2><p>a</p></section><section><h2>Deux</h2><p>b</p></section>"


def page(corps=CORPS, bloc=""):
    return "<!DOCTYPE html><html><head><title>t</title>" + bloc + "</head><body><main>" + corps + "</main></body></html>"


def jouer(fichiers):
    """écrit les fichiers dans un dossier neuf, joue le contrôle dessus ; rend (sortie, texte)"""
    with tempfile.TemporaryDirectory() as d:
        for nom, contenu in fichiers.items():
            p = os.path.join(d, nom)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(contenu)
        tampon = io.StringIO()
        with contextlib.redirect_stdout(tampon):
            r = c.main([d])
        return r, tampon.getvalue()


def main():
    ok = total = 0

    def cas(nom, bon):
        nonlocal ok, total
        total += 1
        ok += bool(bon)
        print("%s %s" % ("✅" if bon else "❌", nom))

    r, t = jouer({"theme-1/x/sequence_a.html": page()})
    cas("aucun document à lire : sortie 2, pas 0 (n°299)", r == 2)
    r, t = jouer({"theme-1/x/Synthèses/synthese_eleve_a.html": page(bloc=BLOC)})
    cas("une synthèse élève qui porte le bloc de la source : conforme", r == 0 and "1 synthese" in t)
    r, t = jouer({"theme-1/x/lexique_a.html": page(bloc=BLOC)})
    cas("un lexique qui porte le bloc de la source : conforme", r == 0 and "1 lexique" in t)
    r, t = jouer({"theme-1/x/Synthèses/synthese_eleve_a.html": page()})
    cas("une synthèse élève sans le bloc : L1", r == 1 and "L1" in t)
    r, t = jouer({"theme-1/x/lexique_a.html": page()})
    cas("un lexique sans le bloc : L1", r == 1 and "L1" in t)
    r, t = jouer({"theme-1/x/lexique_a.html": page(bloc=BLOC + BLOC)})
    cas("deux blocs dans une page : L2", r == 1 and "L2" in t)
    r, t = jouer({"theme-1/x/lexique_a.html": page(bloc=BLOC.replace("Suivant", "Suivante", 1))})
    cas("un bloc retouché dans la page : L3", r == 1 and "L3" in t)
    r, t = jouer({"theme-1/x/Synthèses/synthese_professeur_a.html": page(), "theme-1/x/lexique_a.html": page(bloc=BLOC)})
    cas("la synthèse du professeur n'est pas un document à lire par l'élève", r == 0 and "1 document(s) à lire" in t)
    r, t = jouer({"theme-1/x/lexique_a.html": page(bloc=BLOC), "theme-1/_archive-anciennes-versions/lexique_vieux.html": page(),
                  "theme-1/x/_generation/lexique_modele.html": page()})
    cas("ni l'archive ni un dossier _generation ne sont lus", r == 0 and "1 document(s) à lire" in t)
    c.SANS_LECTURE["x/lexique_b.html"] = "essai du banc"
    try:
        r, t = jouer({"theme-1/x/lexique_a.html": page(bloc=BLOC), "theme-1/x/lexique_b.html": page()})
        cas("une page dispensée, sans le bloc : acceptée, et comptée", r == 0 and "1 dispense" in t)
        r, t = jouer({"theme-1/x/lexique_b.html": page(bloc=BLOC)})
        cas("une page dispensée qui porte le bloc : L4, dispense périmée", r == 1 and "L4" in t)
    finally:
        del c.SANS_LECTURE["x/lexique_b.html"]
    cas("poser : la page reçoit le bloc une fois, et une seconde pose ne change rien",
        c.poser_lecture.poser(c.poser_lecture.poser(page())) == c.poser_lecture.poser(page()) and len(c.poser_lecture.blocs_de(c.poser_lecture.poser(page()))) == 1)
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        r = c.main([os.path.dirname(os.path.dirname(os.path.abspath(__file__)))])
    cas("le site : chaque synthèse élève et chaque lexique porte le mode lecture (sortie 0)", r == 0)
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
