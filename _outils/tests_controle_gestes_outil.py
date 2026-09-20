# -*- coding: utf-8 -*-
"""tests_controle_gestes_outil.py — le banc de l'encart qui parle du mauvais outil.

Rejoue le cas réel du 08/09 (un encart Arduino sur une page qui n'emploie que le
tableur, le mot « arduino » n'étant que dans un <script>), les cas qui doivent
passer, et le dépôt réel.

Usage : python3 _outils/tests_controle_gestes_outil.py
"""
import contextlib, io, os, pathlib, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_gestes_outil as C  # noqa: E402

ENCART = ('<section class="card gestes-outil"><h2>🧰 Avant de commencer — les quatre gestes '
          'de %s</h2><ol><li>Ouvrir.</li></ol></section>')

def page(outil, corps):
    return "<html><body>%s%s</body></html>\n" % (ENCART % outil, corps)

def jouer(racine, toleres=None):
    """stdout ET stderr : la panne de la règle n°299 part sur stderr."""
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main(toleres=toleres)
    finally:
        C.DEPOT = ancien
    return code, s.getvalue() + e.getvalue()

def par_la_ligne_de_commande(script, args=()):
    """Le contrôle lancé comme on le lance vraiment : `python _outils/<script>`.

    Deuxième corollaire de la règle d'or n°299. Un banc qui se contente
    d'appeler `main()` ne passe jamais par le point d'entrée — c'est ainsi que
    `controle_impression.mjs` est resté muet dix-sept jours sous un banc vert.
    Rend (code de sortie, stdout + stderr).
    """
    ici = os.path.dirname(os.path.abspath(__file__))
    r = subprocess.run([sys.executable, os.path.join(ici, script)] + list(args),
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=900)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def reproches_de_la_ligne_de_commande(script):
    """Les deux reproches que la règle n°299 fait à un point d'entrée : sortir
    en erreur, et surtout ne rien écrire du tout. Un script muet n'imprime aucun
    chiffre ; toute mention chiffrée prouve au contraire qu'il a travaillé."""
    ennuis = []
    code, texte = par_la_ligne_de_commande(script)
    if code != 0:
        ennuis.append("lancé en ligne de commande, %s sort à %d :\n     %s"
                      % (script, code, texte.strip()[:400]))
    if not any(c.isdigit() for c in texte):
        ennuis.append("lancé en ligne de commande, %s n'écrit AUCUN chiffre — un script "
                      "muet ne prouve rien (règle d'or n°299) :\n     %s"
                      % (script, texte.strip()[:400] or "(rien du tout)"))
    return ennuis


def main():
    echecs, n = [], 0
    def cas(titre, contenu, doit_refuser, attendu="", toleres=None):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            pathlib.Path(tmp, "sequence_x.html").write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp, toleres if toleres is not None else {})
        if doit_refuser and code == 0: echecs.append(titre + " : accepté, alors qu'il fallait refuser")
        elif not doit_refuser and code != 0: echecs.append(titre + " : refusé\n     " + texte.strip())
        elif attendu and attendu not in texte: echecs.append(titre + " : message sans « %s »" % attendu)

    # Règle d'or n°299 — une racine sans page n'est pas « aucun écart », c'est une panne.
    n += 1
    with tempfile.TemporaryDirectory() as tmp:
        pathlib.Path(tmp, "notes.md").write_text("# rien à lire", encoding="utf-8")
        code, texte = jouer(tmp, {})
    if code != 2:
        echecs.append("une racine sans page .html : sortie %d au lieu de 2 — le contrôle se déclare content sans avoir rien ouvert" % code)
    elif "EN PANNE" not in texte:
        echecs.append("une racine sans page .html : la panne n'est pas annoncée")

    # Depuis le 13/09 (vague 2 étape 1), une page sans activité qui ouvre l'outil est refusée :
    # les cas qui doivent passer portent donc une activité qui ouvre l'outil, collée à l'encart.
    cas("Tableur, et la page ouvre un tableur",
        page("Tableur", "<h2>Activité 1 — Relever</h2><p>Ouvre le tableur.</p>"), False)
    cas("le cas du 08/09 : Arduino, le mot seulement dans un <script>",
        page("Arduino", "<p>Ouvre le tableur.</p><script>const c=/arduino/;</script>"),
        True, "ne l'emploie nulle part")
    cas("Arduino, mais la page téléverse un programme",
        page("Arduino", "<h2>Activité 1 — Programmer</h2><p>Téléverse ton programme dans la carte.</p>"), False)
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
    # ── l'ouverture (durci le 13/09/2026, vague 2 étape 1) : pas de porte, pas d'encart ──
    MENTION = page2("Vittascience", "", SIT + "<h2>Séance 1 — Lire</h2><p>Blocs Vittascience ou Python, même raisonnement.</p>")
    cas("Vittascience : une mention n'ouvre pas — l'encart est refusé (avant le 13/09 : seulement signalé)",
        MENTION, True, "pas de porte, pas d'encart")
    cas("Packet Tracer cité dans « Choix de l'outil » seulement — refusé, le cas des six pages du thème 2",
        page2("Packet Tracer", SIT, "<h2>🧰 Choix de l'outil</h2><p>Cisco Packet Tracer (approfondissement).</p>"
              "<h2>Activité 1 — Jouer au routeur</h2><p>Sans poste.</p>"), True, "aucune activité de la page n'ouvre")
    cas("la même page, tolérée nommément, passe et le dit",
        MENTION, False, "TOLÉRÉS nommément", toleres={"sequence_x.html": "raison écrite"})
    cas("une tolérance dont la page n'a plus d'encart est annoncée périmée, sans refus",
        "<html><body><p>rien</p></body></html>", False, "périmée", toleres={"sequence_x.html": "raison écrite"})
    cas("Vittascience : un lien vers fr.vittascience.com ouvre — et la position est jugée",
        page2("Vittascience", "", SIT + '<h2>Séance 1 — Coder</h2><p>Ouvre Vittascience :</p><a href="https://fr.vittascience.com/python/">▶</a>'),
        True, "précède la situation")

    n += 1
    code, texte = jouer(C.DEPOT, C.TOLERES)
    if code != 0: echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip())

    # Le VRAI point d'entrée, en sous-processus (règle d'or n°299).
    n += 1
    echecs.extend(reproches_de_la_ligne_de_commande('controle_gestes_outil.py'))

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — l'encart qui parle d'un autre outil que sa page, ou qui n'est pas à sa porte, est refusé" % n)
    print("\n%d / %d" % (n, n)); return 0

if __name__ == "__main__":
    sys.exit(main())
