# -*- coding: utf-8 -*-
"""Banc de controle_correction_illustree.py (règle d'or n°336) : chaque cas, une page jetable jugée.

Usage : python3 _outils/tests_controle_correction_illustree.py
"""
import io
import os
import sys
import tempfile
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_correction_illustree as C  # noqa: E402

RADIO = ('<fieldset class="qcm-groupe" id="q1"><legend>Ta réponse</legend>'
         '<label><input type="radio" name="q1" value="a"> a</label></fieldset>')
FIG = '<figure><img src="Images/x.svg" alt="le schéma complet"></figure>'


def page(*cartes):
    return "<!doctype html><html><body><main>%s</main></body></html>" % "".join(cartes)


def carte(titre, corps):
    return '<div class="activite"><h3>%s</h3>%s</div>' % (titre, corps)


def correction(dedans=""):
    return '<details class="correction"><summary>✅ Correction complète</summary><p>La réponse.</p>%s</details>' % dedans


def jouer(html, *args, nom="sequence_x.html", juges=None):
    with tempfile.TemporaryDirectory() as tmp:
        chemin = os.path.join(tmp, nom)
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(html)
        ancien_depot, ancien_juges = C.DEPOT, C.JUGES
        C.DEPOT = tmp
        if juges is not None:
            C.JUGES = {nom: juges}
        tampon = io.StringIO()
        try:
            with redirect_stdout(tampon):
                code = C.main([chemin, *args])
        finally:
            C.DEPOT, C.JUGES = ancien_depot, ancien_juges
        return code, tampon.getvalue()


def main():
    ok = ko = 0

    def cas(titre, html, code_attendu, present="", absent="", **kw):
        nonlocal ok, ko
        code, sortie = jouer(html, **kw)
        bon = code == code_attendu and (not present or present in sortie) and (not absent or absent not in sortie)
        ok += bon
        ko += not bon
        print(("✅ " if bon else "❌ ") + titre + ("" if bon else "\n   code %s · sortie :\n%s" % (code, sortie)))

    # D1 — un schéma muet dans la question : la correction doit montrer une figure
    MUET = '<object data="Images/chaine_muet.svg" type="image/svg+xml">schéma</object>'
    cas("D1 · schéma muet, correction sans figure : ✘", page(carte("Activité 2", MUET + RADIO + correction())), 1, "✘ D1")
    cas("D1 · schéma muet, correction avec le schéma complet : rien", page(carte("Activité 2", MUET + RADIO + correction(FIG))), 0,
        absent="D1 schéma")
    cas("D1 · une photo dont le nom contient « muet » (capteur muet) n'est pas un schéma muet",
        page(carte("Activité 2", '<img src="Images/capteur_muet.png" alt="">' + RADIO + correction())), 0, absent="✘ D1")

    # D2 / D3 — faire dessiner un schéma
    DESSINE = "<p>Dessine sur ton cahier la chaîne d'énergie du ventilateur.</p>"
    cas("D2 · faire dessiner, correction en mots seulement : ⚠", page(carte("Activité 3", DESSINE + RADIO + correction())), 0, "⚠ D2")
    code, sortie = jouer(page(carte("Activité 3", DESSINE + RADIO + correction())), "--strict")
    bon = code == 1 and "✘ D2" in sortie
    ok += bon
    ko += not bon
    print(("✅ " if bon else "❌ ") + "D2 · avec --strict, c'est un ✘")
    cas("D2 · faire dessiner, la correction montre le dessin : rien", page(carte("Activité 3", DESSINE + RADIO + correction(FIG))), 0,
        absent="D2 le dessin")
    cas("D3 · faire dessiner, sans correction : ⚠", page(carte("Activité 3", DESSINE + RADIO)), 0, "⚠ D3")
    cas("D2 · une question (« ? ») qui cite un schéma n'est pas une consigne de dessin",
        page(carte("Activité 3", "<p>Que représente le schéma de la chaîne ?</p>" + RADIO + correction())), 0, absent="D2 le dessin")
    cas("D2 · le corrigé d'un défi du Bonus (details.corrige-bonus) compte comme correction",
        page('<section class="card bonus"><h2>🎁 Bonus</h2>' + DESSINE + '<textarea id="b1"></textarea>'
             '<details class="corrige-bonus"><summary>🔍 Voir la correction</summary>' + FIG + '</details></section>'), 0,
        absent="D3 le bloc")
    cas("chaîne à compléter : le moteur pose la chaîne complète, rien à signaler",
        page(carte("Activité 2", DESSINE + "<div class='cac' data-cac='{\"dessin\":\"x\"}'>" + RADIO + "</div>" + correction())), 0,
        absent="D2 le dessin")
    cas("un outil nommé (draw.io) : la n°332 juge, pas la n°336",
        page(carte("Activité 4", "<p>Dessine la chaîne d'énergie dans draw.io, puis enregistre-la.</p>" + RADIO + correction())), 0,
        absent="D2 le dessin")
    cas("JUGES · un bloc jugé juste sort du compte, et se lit avec --juges",
        page(carte("Activité 3 — Lire", DESSINE + RADIO + correction())), 0, "1 bloc(s) jugés justes",
        absent="⚠ D2", juges={"Activité 3 — Lire": "la raison"})
    cas("n°299 · aucune page lisible : EN PANNE, sortie 2", "<html></html>", 2, "EN PANNE", nom="rien.txt")

    print("\n%d / %d" % (ok, ok + ko))
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
