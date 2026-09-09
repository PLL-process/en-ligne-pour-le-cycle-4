# -*- coding: utf-8 -*-
"""tests_controle_entete_qcm.py — le banc du QCM qui se présente sous un autre nom.

Rejoue les formes réelles du 09/09 : le menu « Compétence à réviser » copié d'un autre lot
(mode « cible » vide), le pied de page d'un autre lot, le sous-titre d'un autre niveau, et
les cas qui doivent passer — un QCM qui revisite des codes d'un autre niveau et le dit
(4e_C1.4), un distracteur d'un autre niveau dans une question, un QCM à catégories,
un QCM ancien sans questions codées.

Usage : python3 _outils/tests_controle_entete_qcm.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_entete_qcm as C  # noqa: E402

def q(c): return '{c:"%s",n:"x",q:"?",o:["a","b"],r:0},\n' % c

def qcm(niveau="5e", h1="QCM — Le lot", sub="", badges="", options=None, pied=None, questions=None, labels=None, corps=""):
    questions = questions if questions is not None else [q("C1.3")] * 2 + [q("C1.4")] * 2
    labels = labels or {"C1.3": "5e_C1.3 — a", "C1.4": "5e_C1.4 — b"}
    options = options if options is not None else list(labels)
    pied = pied if pied is not None else "QCM d’entraînement 5e_C1.3 · 5e_C1.4 · Thème 1"
    opts = "".join('<option value="%s">%s</option>' % (o, labels.get(o, o)) for o in options)
    carte = ",".join('"%s":"%s"' % kv for kv in labels.items())
    return ('<html><head><title>Thème 1 · %s — %s</title></head><body><h1>%s</h1><p class="sub">%s</p>'
            '<div class="badges">%s</div>%s<select id="selComp">%s</select><footer><p>%s</p></footer>'
            '<script>const QUESTIONS=[\n%s];\nconst COMP_LABELS={%s};</script></body></html>\n'
            % (niveau, h1, h1, sub, badges, corps, opts, pied, "".join(questions), carte))

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
    def cas(titre, contenu, doit_refuser, attendu="", lot="5e_C1.3"):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            d = pathlib.Path(tmp, lot); d.mkdir(); (d / "qcm_x.html").write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if doit_refuser and code == 0: echecs.append(titre + " : accepté, alors qu'il fallait refuser")
        elif not doit_refuser and code != 0: echecs.append(titre + " : refusé\n     " + texte.strip())
        elif attendu and attendu not in texte: echecs.append(titre + " : message sans « %s »\n     %s" % (attendu, texte.strip()))

    cas("un QCM qui dit vrai", qcm(), False, "dit vrai")
    cas("le menu d'un autre lot : le mode « cible » ne rend rien",
        qcm(options=["BOI", "LIR", "MOD"], labels={"C1.3": "5e_C1.3 — a", "C1.4": "5e_C1.4 — b", "BOI": "La boîte", "LIR": "Lire", "MOD": "Modifier"}),
        True, "ne rend rien")
    cas("une option manquante (4e_C4.7 sans C4.9)", qcm(options=["C1.3"]), True, "ne rend rien")
    cas("le pied de page d'un autre lot", qcm(pied="QCM d’entraînement 4e_C8.1 · C8.2 · C8.3 · Thème 3 · New York"),
        True, "pied nomme un autre niveau")
    cas("le pied qui ne nomme pas le lot", qcm(pied="QCM d’entraînement 5e_C1.2 · Thème 1"), True, "ne nomme ni C1.3")
    cas("le sous-titre d'un autre niveau", qcm(sub="Comparer des principes (5e_C1.2)"), False)  # même niveau : toléré ici
    cas("le sous-titre d'un autre niveau, vraiment", qcm(niveau="3e", sub="Comparer des principes (5e_C1.2)"), True,
        "sous-titre nomme un autre niveau", lot="3e_C1.5")
    cas("un QCM qui revisite des codes d'un autre niveau et le dit (4e_C1.4)",
        qcm(niveau="4e", h1="QCM (4e_C1.4, avec 5e_C1.5 et 5e_C1.6)", badges="4e_C1.4 · 5e_C1.5 · 5e_C1.6",
            questions=[q("C1.4")] * 2 + [q("C1.5")] * 2 + [q("C1.6")] * 2,
            labels={"C1.4": "4e_C1.4 — a", "C1.5": "5e_C1.5 — b", "C1.6": "5e_C1.6 — c"},
            pied="QCM d’entraînement 4e_C1.4 · 5e_C1.5 · 5e_C1.6 · Thème 1"), False, lot="4e_C1.4")
    cas("un distracteur d'un autre niveau dans une QUESTION n'est pas jugé",
        qcm(corps='<p>« Compléter un programme » correspond au code… 5e_C1.1 / 3e_C9.2</p>'), False)
    cas("un QCM à catégories, menu et pied justes",
        qcm(niveau="3e", questions=[q("ELA")] * 2 + [q("SIM")] * 2, labels={"ELA": "3e_C7.1 — a", "SIM": "3e_C8.1 — b"},
            pied="QCM d’entraînement 3e_C7.1 · 3e_C8.1 · Thème 3"), False, lot="3e_C7.1")
    cas("un QCM ancien sans questions codées n'est pas jugé sur son pied",
        '<html><head><title>QCM</title></head><body><h1>QCM</h1><footer><p>Refais le QCM.</p></footer></body></html>', False,
        lot="4e_C2.1")

    n += 1
    code, texte = jouer(C.DEPOT)
    if code != 0: echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip()[:500])
    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — un QCM qui se présente sous le nom d'un autre lot est refusé" % n)
    print("\n%d / %d" % (n, n)); return 0

if __name__ == "__main__":
    sys.exit(main())
