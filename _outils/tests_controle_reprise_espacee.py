# -*- coding: utf-8 -*-
"""Banc de `controle_reprise_espacee.py` et de `mesurer_entrelacement.py` (règles d'or n°369, n°371, n°372, en essai).

Chaque cas est une petite page écrite ici : le banc prouve que la mesure voit ce qu'elle dit voir (n°299).
Usage : python3 _outils/tests_controle_reprise_espacee.py   — sortie 0 si tous les cas passent.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_reprise_espacee as cre  # noqa: E402
import mesurer_entrelacement as me  # noqa: E402

P1 = '<div class="seance-panel active" id="s1" role="tabpanel"><p>séance 1</p></div>'


def s(n, corps):
    return f'<div class="seance-panel" id="s{n}" role="tabpanel">{corps}</div>'


REPRISE_OK = ('<section data-reprise><h3>🔁 Reprise</h3><fieldset><legend>Q1</legend></fieldset>'
              '<fieldset><legend>Q2</legend></fieldset></section>')
RAPPEL = '<details class="rappel-ouverture"><summary>📖 Rappel</summary><p>…</p></details>'
BILAN_OK = '<section data-bilan><h3>Bilan</h3><textarea data-flou></textarea></section>'
BILAN_SANS = '<section><h2>Bilan</h2><p>…</p></section>'

CAS = [
    ("séance 2 sans reprise", P1 + s(2, RAPPEL + "<p>activité</p>") + BILAN_OK, 1, ["R1"], True),
    ("reprise conforme avant le rappel", P1 + s(2, REPRISE_OK + RAPPEL) + BILAN_OK, 1, [], True),
    ("reprise d'une seule question", P1 + s(2, '<div data-reprise><fieldset></fieldset></div>') + BILAN_OK, 1, ["R2"], True),
    ("reprise après le rappel déplié", P1 + s(2, RAPPEL + REPRISE_OK) + BILAN_OK, 1, ["R3"], True),
    ("deux séances, une seule reprise", P1 + s(2, REPRISE_OK) + s(3, "<p>x</p>") + BILAN_OK, 2, ["R1"], True),
    ("bilan sans « ce qui reste flou »", P1 + s(2, REPRISE_OK) + BILAN_SANS, 1, [], False),
    ("une seule séance : rien à exiger", P1 + BILAN_OK, 0, [], True),
]


def main():
    echecs = 0
    for nom, page, n_attendu, codes_attendus, flou_attendu in CAS:
        n, manques, flou = cre.mesurer_page(page)
        codes = [c.split()[0] for _, c in manques]
        ok = n == n_attendu and codes == codes_attendus and flou == flou_attendu
        echecs += not ok
        print(("✔" if ok else "✘"), nom, "" if ok else f"→ {n} {codes} {flou}")
    # entrelacement : déterministe, un tour par compétence
    codes = ["A"] * 3 + ["B"] * 3 + ["C"] * 2
    o = me.ordre_entrelace(codes)
    ok = o == [0, 3, 6, 1, 4, 7, 2, 5] and me.changements(codes) == 2 and me.changements([codes[i] for i in o]) == 7
    echecs += not ok
    print(("✔" if ok else "✘"), "ordre entrelacé A B C A B C A B", "" if ok else f"→ {o}")
    print(f"{len(CAS) + 1 - echecs}/{len(CAS) + 1} cas passent")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
