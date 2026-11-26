# -*- coding: utf-8 -*-
"""tests_controle_mode_mission.py — le contrôle du mode mission éprouvé sur des cas dont on connaît la réponse (n°194).

Sortie : 0 tout passe · 1 un échec.
Usage : python3 _outils/tests_controle_mode_mission.py
"""
import contextlib
import io
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_mode_mission as c  # noqa: E402

BLOC = c.poser_mission.bloc()
QUESTION = '<fieldset class="qcm-groupe"><legend>Une question ?</legend><input type="radio" name="q" value="a"></fieldset>'
LONG = "<p>" + "du texte de leçon. " * 700 + "</p>"


def page(corps="", bloc=""):
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

    LECTURE = ("<!-- mode-lecture v1 : début — une partie par écran ; source unique : _outils/mode_lecture/ (poser.py). "
               "Ne pas le modifier dans la page. -->\n<script></script>\n<!-- mode-lecture v1 : fin -->")
    r, t = jouer({"theme-1/x/qcm_a.html": page(QUESTION)})
    cas("aucune page élève (un QCM seul) : sortie 2, pas 0 (n°299)", r == 2)
    r, t = jouer({"theme-1/x/sequence_a.html": page(QUESTION, BLOC)})
    cas("une séquence qui porte le bloc de la source : conforme", r == 0 and "1 sequence" in t)
    r, t = jouer({"theme-1/x/atelier_a.html": page(QUESTION)})
    cas("un atelier avec une question, sans le bloc : M1", r == 1 and "M1" in t)
    r, t = jouer({"theme-1/x/atelier_a.html": page('<p><a href="../atelier.html">Ouvrir l\'atelier</a></p>')})
    cas("un panneau court, sans champ, sans le bloc : M1 (« tout doit être en mode mission », 26/11/2026)", r == 1 and "M1" in t)
    r, t = jouer({"theme-1/x/synthese_eleve_a.html": page(LONG)})
    cas("une synthèse élève sans le bloc : M1", r == 1 and "M1" in t)
    r, t = jouer({"theme-1/x/lexique_a.html": page(LONG, BLOC)})
    cas("un lexique qui porte le bloc : conforme, compté", r == 0 and "1 lexique" in t)
    r, t = jouer({"theme-1/x/lexique_a.html": page(LONG, LECTURE)})
    cas("un lexique qui porte encore le mode lecture : M5 (et M1)", r == 1 and "M5" in t and "M1" in t)
    r, t = jouer({"theme-1/x/carte_des_representations.html": page(LONG)})
    cas("une page de repères, sans le bloc : M1 (rien n'est dispensé par son nom)", r == 1 and "M1" in t)
    r, t = jouer({"theme-1/x/cahier_a.html": page(QUESTION, BLOC.replace("Vérifier", "Verifier", 1))})
    cas("un bloc retouché dans la page : M3", r == 1 and "M3" in t)
    r, t = jouer({"theme-1/x/activite_a.html": page(QUESTION, BLOC + BLOC)})
    cas("deux blocs dans une page : M2", r == 1 and "M2" in t)
    r, t = jouer({"theme-2/C6/4e/4e_C6.2/tp_algorigrammes_domotique.html": page(QUESTION + LONG)})
    cas("l'ancienne dispense (TP à six phases) n'en est plus une : M1", r == 1 and "M1" in t)
    r, t = jouer({"theme-1/x/entrainement_a.html": page(QUESTION, BLOC), "theme-1/x/_generation/atelier_modele.html": page(QUESTION),
                  "theme-1/_archive-anciennes-versions/tp_vieux.html": page(QUESTION), "_outils/gabarit.html": page(QUESTION)})
    cas("ni l'archive, ni un dossier _generation, ni ce qui est hors des thèmes ne sont lus", r == 0 and "1 page(s) élève lue(s)" in t)
    r, t = jouer({"theme-1/x/qcm_a.html": page(QUESTION), "theme-1/x/miniquiz_b.html": page(QUESTION),
                  "theme-1/x/synthese_professeur_a.html": page(LONG), "theme-1/x/fiche_maths.html": page(LONG),
                  "theme-1/x/station_en_pieces.html": page(LONG), "theme-1/x/sequence_a.html": page(QUESTION, BLOC)})
    cas("un QCM, un mini-quiz, un document pour l'enseignant, une figure en cadre : hors mission, comptés", r == 0
        and "1 page(s) élève lue(s)" in t and "2 QCM" in t and "2 document pour l'enseignant" in t and "1 figure interactive" in t)
    r, t = jouer({"theme-1/x/vittascience_x.html": page('<meta http-equiv="refresh" content="0;url=sequence_a.html">'),
                  "theme-1/x/sequence_a.html": page(QUESTION, BLOC)})
    cas("une page de renvoi (meta refresh) : hors mission, comptée", r == 0 and "1 page de renvoi" in t)
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        r = c.main([os.path.dirname(os.path.dirname(os.path.abspath(__file__)))])
    cas("le site : chaque page élève porte le mode mission (sortie 0)", r == 0)
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
