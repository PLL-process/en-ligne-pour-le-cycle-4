# -*- coding: utf-8 -*-
"""tests_controle_gestes_outil.py — le banc de l'encart qui parle du mauvais outil.

Rejoue le cas réel du 08/09 (un encart Arduino sur une page qui n'emploie que le
tableur, le mot « arduino » n'étant que dans un <script>), les cas qui doivent
passer, et le dépôt réel.

Usage : python3 _outils/tests_controle_gestes_outil.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_gestes_outil as C  # noqa: E402

ENCART = ('<section class="card gestes-outil"><h2>🧰 Avant de commencer — les quatre gestes '
          'de %s</h2><ol><li>Ouvrir.</li></ol></section>')

def page(outil, corps):
    return "<html><body>%s%s</body></html>\n" % (ENCART % outil, corps)

def jouer(racine):
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO()
    try:
        with contextlib.redirect_stdout(s):
            code = C.main()
    finally:
        C.DEPOT = ancien
    return code, s.getvalue()

def main():
    echecs, n = [], 0
    def cas(titre, contenu, doit_refuser, attendu=""):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            pathlib.Path(tmp, "sequence_x.html").write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if doit_refuser and code == 0: echecs.append(titre + " : accepté, alors qu'il fallait refuser")
        elif not doit_refuser and code != 0: echecs.append(titre + " : refusé\n     " + texte.strip())
        elif attendu and attendu not in texte: echecs.append(titre + " : message sans « %s »" % attendu)

    cas("Tableur, et la page ouvre un tableur", page("Tableur", "<p>Ouvre le tableur.</p>"), False)
    cas("le cas du 08/09 : Arduino, le mot seulement dans un <script>",
        page("Arduino", "<p>Ouvre le tableur.</p><script>const c=/arduino/;</script>"),
        True, "ne l'emploie nulle part")
    cas("Arduino, mais la page téléverse un programme",
        page("Arduino", "<p>Téléverse ton programme dans la carte.</p>"), False)
    cas("le mot dans un alt seulement ne compte pas",
        page("Onshape", '<img alt="capture Onshape"><p>Rien d\'autre.</p>'), True)
    cas("un outil inconnu est refusé, pas deviné", page("Tinkercad", "<p>Ouvre Tinkercad.</p>"),
        True, "inconnu de OUTILS")
    cas("une page sans encart n'est pas jugée", "<html><body><p>rien</p></body></html>", False)

    n += 1
    code, texte = jouer(C.DEPOT)
    if code != 0: echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip())

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — l'encart qui parle d'un autre outil que sa page est refusé" % n)
    print("\n%d / %d" % (n, n)); return 0

if __name__ == "__main__":
    sys.exit(main())
