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

    # ── la position (règle n°297 complétée le 13/09/2026) ──
    def page2(outil, avant, apres):
        return "<html><body>%s%s%s</body></html>\n" % (avant, ENCART % outil, apres)
    SIT = "<h2>📖 La situation : un réseau qui ne répond pas</h2><p>Le capteur se tait.</p>"
    ACT = "<h2>🧱 Activité 1 — Construire</h2><p>Ouvre Packet Tracer et monte le réseau.</p>"
    cas("à sa porte : après la situation, collé à l'activité qui ouvre l'outil",
        page2("Packet Tracer", SIT, ACT), False)
    cas("le cas du 13/09 : l'encart précède la situation",
        page2("Packet Tracer", "", SIT + ACT), True, "précède la situation")
    cas("l'encart après la première activité : plus aucune activité ne le suit",
        page2("Packet Tracer", SIT + ACT, "<h2>🏁 Bilan</h2><p>Fini.</p>"), True, "aucune activité ne le suit")
    cas("un bloc visible s'intercale entre l'encart et l'activité",
        page2("Packet Tracer", SIT, "<h2>🔀 Trois façons</h2><p>Au choix.</p>" + ACT), True, "s'intercale")
    cas("collé à une activité qui ne parle pas de l'outil",
        page2("Packet Tracer", SIT, "<h2>Activité 1 — Lire</h2><p>Lis le plan.</p>" + ACT.replace("Activité 1", "Activité 2")),
        True, "n'ouvre pas l'outil")
    cas("le cartouche « Activité n » d'un <h3> ne compte pas comme un bloc intercalé",
        page2("Packet Tracer", SIT, '<div class="seance-panel"><div class="activite"><header><span class="num">Activité 3</span>'
              '<h3>Construire le réseau</h3></header><p>Ouvre Packet Tracer.</p></div></div>'), False)
    cas("un <h3> ne clôt pas le bloc d'une séance <h2>",
        page2("Vittascience", SIT, '<h2>Séance 2 — Les types</h2><p>Prédis, puis teste dans Vittascience.</p><h3>Teste</h3>'
              '<a href="https://fr.vittascience.com/python/">▶ Ouvrir l’éditeur</a>'), False)
    cas("Vittascience : une mention n'ouvre pas — position non jugée, pas refusée",
        page2("Vittascience", "", SIT + "<h2>Séance 1 — Lire</h2><p>Blocs Vittascience ou Python, même raisonnement.</p>"),
        False, "position(s) non jugée(s)")
    cas("Vittascience : un lien vers fr.vittascience.com ouvre — et la position est jugée",
        page2("Vittascience", "", SIT + '<h2>Séance 1 — Coder</h2><p>Ouvre Vittascience :</p><a href="https://fr.vittascience.com/python/">▶</a>'),
        True, "précède la situation")

    n += 1
    code, texte = jouer(C.DEPOT)
    if code != 0: echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip())

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — l'encart qui parle d'un autre outil que sa page, ou qui n'est pas à sa porte, est refusé" % n)
    print("\n%d / %d" % (n, n)); return 0

if __name__ == "__main__":
    sys.exit(main())
