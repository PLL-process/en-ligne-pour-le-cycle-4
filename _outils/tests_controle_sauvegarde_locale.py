# -*- coding: utf-8 -*-
"""tests_controle_sauvegarde_locale.py — le contrôle de la sauvegarde locale éprouvé sur des cas connus (n°194).

Écrit le 25/11/2026, avec la règle « le mode mission se lit à part » : le bloc du mode, le même dans toutes les pages,
ne doit ni créer l'obligation d'effacer (une page qui n'enregistre rien), ni la remplir (une page qui enregistre sans
bouton, ou sans note).

Sortie : 0 tout passe · 1 un échec.
Usage : python3 _outils/tests_controle_sauvegarde_locale.py
"""
import contextlib
import importlib.util
import io
import os
import pathlib
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import controle_sauvegarde_locale as c  # noqa: E402

_spec = importlib.util.spec_from_file_location("poser_mission", ICI / "mode_mission" / "poser.py")
_poser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_poser)
BLOC = _poser.bloc()
_spec_l = importlib.util.spec_from_file_location("poser_lecture", ICI / "mode_lecture" / "poser.py")
_poser_l = importlib.util.module_from_spec(_spec_l)
_spec_l.loader.exec_module(_poser_l)
BLOC_LECTURE = _poser_l.bloc()
#: un bloc qui porterait la note et un bouton : même ainsi, il ne remplit pas l'obligation de la page
BLOC_BAVARD = BLOC.replace("</script>", '/* data-note="poste-partage" <button id="btnReset">Effacer ma sauvegarde</button> */</script>', 1)

ENREGISTRE = '<script>const KEY="seq_x";function sauver(){localStorage.setItem(KEY,"{}");}</script>'
BOUTON = '<button class="btn ghost" id="btnReset" type="button">🗑 Effacer ma sauvegarde</button>'
NOTE = '<p class="saved-note" data-note="poste-partage">🖥️ Ordinateur partagé…</p>'


def page(corps="", tete=""):
    return "<!DOCTYPE html><html><head><title>t</title>" + tete + "</head><body><main>" + corps + "</main></body></html>"


def jouer(fichiers):
    """écrit les fichiers dans un dossier neuf, joue le contrôle dessus ; rend (sortie, texte)"""
    with tempfile.TemporaryDirectory() as d:
        for nom, contenu in fichiers.items():
            p = os.path.join(d, nom)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(contenu)
        tampon = io.StringIO()
        with contextlib.redirect_stdout(tampon):
            r = c.main(["--racine", d])
        return r, tampon.getvalue()


def main():
    ok = total = 0

    def cas(nom, bon):
        nonlocal ok, total
        total += 1
        ok += bool(bon)
        print("%s %s" % ("✅" if bon else "❌", nom))

    conforme = page(ENREGISTRE + BOUTON + NOTE)
    r, t = jouer({"t/lisezmoi.html": page("<p>rien</p>")})
    cas("aucune page qui enregistre : sortie 2, pas 0 (n°299)", r == 2)
    r, t = jouer({"t/sequence_a.html": conforme})
    cas("une séquence qui enregistre, avec son bouton et sa note : conforme", r == 0 and "1 page(s) lues" in t)
    r, t = jouer({"t/sequence_a.html": page(ENREGISTRE + NOTE)})
    cas("elle enregistre sans bouton d'effacement : refus", r == 1 and "sans aucun moyen d'effacer" in t)
    r, t = jouer({"t/sequence_a.html": page(ENREGISTRE + BOUTON)})
    cas("elle enregistre sans note « ordinateur partagé » : refus", r == 1 and "aucune note" in t)
    r, t = jouer({"t/sequence_a.html": conforme, "t/tp_a.html": page("<p>un TP</p>", BLOC)})
    cas("une page qui ne porte que le mode mission : comptée à part, pas refusée",
        r == 0 and "1 page(s) lues" in t and "1 page(s) n'enregistrent rien" in t)
    r, t = jouer({"t/tp_a.html": page("<p>un TP</p>", BLOC)})
    cas("seulement des pages « mode mission seul » : rien n'a été vérifié, sortie 2", r == 2)
    r, t = jouer({"t/sequence_a.html": page(ENREGISTRE, BLOC)})
    cas("le bloc du mode n'excuse pas une page qui enregistre sans bouton ni note : deux refus",
        r == 1 and "sans aucun moyen d'effacer" in t and "aucune note" in t)
    r, t = jouer({"t/sequence_a.html": page(ENREGISTRE, BLOC_BAVARD)})
    cas("même un bloc qui porterait une note et un bouton ne remplit pas l'obligation de la page", r == 1 and "2 refus" in t)
    r, t = jouer({"t/sequence_a.html": page(ENREGISTRE + BOUTON + NOTE, BLOC)})
    cas("une séquence conforme qui porte aussi le mode : conforme, comptée une fois",
        r == 0 and "1 page(s) lues" in t and "n'enregistrent rien" not in t)
    cas("sans_mission : retire le bloc et rien d'autre", c.sans_mission(page("<p>a</p>", BLOC)) == page("<p>a</p>"))
    r, t = jouer({"t/sequence_a.html": conforme, "t/Synthèses/synthese_eleve_a.html": page("<p>une synthèse</p>", BLOC_LECTURE)})
    cas("une synthèse qui ne porte que le mode lecture : comptée à part, pas refusée",
        r == 0 and "1 page(s) lues" in t and "1 page(s) n'enregistrent rien" in t)
    r, t = jouer({"t/sequence_a.html": page(ENREGISTRE, BLOC_LECTURE)})
    cas("le bloc du mode lecture n'excuse pas une page qui enregistre sans bouton ni note : deux refus", r == 1 and "2 refus" in t)
    cas("sans_mission : retire aussi le bloc du mode lecture, et les deux ensemble",
        c.sans_mission(page("<p>a</p>", BLOC + BLOC_LECTURE)) == page("<p>a</p>"))
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        r = c.main(["--racine", str(ICI.parent), "--muet"])
    cas("le site : aucune page qui enregistre sans savoir effacer ni prévenir (sortie 0)", r == 0)
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
