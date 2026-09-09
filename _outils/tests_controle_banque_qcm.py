# -*- coding: utf-8 -*-
"""tests_controle_banque_qcm.py — le banc de la ligne « Banque » qui ment.

Rejoue les formes réelles du dépôt : le gabarit copié vingt et une fois (codes d'un
autre lot, images imaginaires), le « Sainte-Luce 5e » de trois QCM du thème 1, une
image ajoutée sans mettre la ligne à jour, un QCM rangé par catégories dont la ligne
cite des codes en marge, une ancienne ligne citée entre guillemets, et un QCM sans
ligne du tout (qui n'a rien à prouver).

Usage : python3 _outils/tests_controle_banque_qcm.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_banque_qcm as C  # noqa: E402

def q(c, img=False):
    return '{c:"%s",n:"x",q:"?",%s o:["a","b"],r:0},\n' % (c, ' img:{src:"i.svg",alt:"un document"},' if img else '')

def qcm(ligne, questions):
    return ('<html><body><script>"use strict";\n%s\nconst QUESTIONS = [\n%s];\n</script></body></html>\n'
            % (ligne, "".join(questions)))

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
            pathlib.Path(tmp, "qcm_x.html").write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if doit_refuser and code == 0: echecs.append(titre + " : accepté, alors qu'il fallait refuser")
        elif not doit_refuser and code != 0: echecs.append(titre + " : refusé\n     " + texte.strip())
        elif attendu and attendu not in texte: echecs.append(titre + " : message sans « %s »\n     %s" % (attendu, texte.strip()))

    VRAI = [q("3e_C7.3")] * 20 + [q("3e_C4.2")] * 10
    cas("une ligne juste", qcm("/* Banque : 30 questions (20 3e_C7.3 + 10 3e_C4.2), 0 illustrée. */", VRAI), False)
    cas("le gabarit copié : codes d'un autre lot, images imaginaires",
        qcm("/* Banque : 30 questions (10 4e_C8.1 + 10 4e_C8.2 + 10 4e_C8.3), 3 illustrees (regle images v2) */", VRAI),
        True, "annonce 10 C8.1 + 10 C8.2 + 10 C8.3")
    cas("« Sainte-Luce 5e, seul code 5e_C1.2 » sur un QCM qui n'en a pas",
        qcm("/* Banque de questions — Sainte-Luce 5e : 30 questions sur le seul code 5e_C1.2, réparties par thème. 8 illustrées. */",
            [q("3e_C1.5")] * 10 + [q("3e_C1.3")] * 10 + [q("3e_C1.4")] * 10),
        True, "annonce 30 C1.2")
    cas("une image ajoutée sans mettre la ligne à jour",
        qcm("/* Banque : 30 questions (20 3e_C7.3 + 10 3e_C4.2), 3 illustrées. */",
            [q("3e_C7.3", img=True)] * 4 + [q("3e_C7.3")] * 16 + [q("3e_C4.2")] * 10),
        True, "annonce 3 illustrée(s), en contient 4")
    cas("le nombre de questions faux", qcm("/* Banque : 30 questions (20 3e_C7.3 + 10 3e_C4.2), 0 illustrée. */", VRAI[:-1]),
        True, "annonce 30 questions, en contient 29")
    cas("un code s'écrit avec ou sans niveau (4e_C8.1 ≡ C8.1)",
        qcm("/* Banque : 30 questions (20 C7.3 + 10 C4.2), 0 illustrée. */", VRAI), False)
    cas("la forme « A : k · B : k »", qcm("/* Banque de questions — 30 questions (3e_C7.3 : 20 · 3e_C4.2 : 10). */", VRAI), False)
    cas("un QCM par catégories : les codes cités en marge ne sont pas comptés",
        qcm("/* Banque : 30 questions (10 ELA + 10 SIM + 10 SEU — codes 3e_C7.1, 3e_C8.1), 0 illustrée. */",
            [q("ELA")] * 10 + [q("SIM")] * 10 + [q("SEU")] * 10), False)
    cas("par catégories, mais les catégories fausses", 
        qcm("/* Banque : 30 questions (15 ELA + 15 SIM), 0 illustrée. */",
            [q("ELA")] * 10 + [q("SIM")] * 10 + [q("SEU")] * 10), True, "contient 10 ELA + 10 SIM + 10 SEU")
    cas("l'ancienne ligne citée entre guillemets n'est pas une promesse",
        qcm("/* Banque : 30 questions (20 3e_C7.3 + 10 3e_C4.2), 0 illustrée. L'ancienne disait "
            "« 10 4e_C8.1 + 10 4e_C8.2 + 10 4e_C8.3, 3 illustrees ». */", VRAI), False)
    cas("un QCM sans ligne « Banque » n'a rien à prouver", qcm("/* rien */", VRAI), False)
    cas("une ligne sans aucun chiffre n'est pas jugée", qcm("/* Banque : les questions du lot. */", VRAI), False)

    n += 1
    code, texte = jouer(C.DEPOT)
    if code != 0: echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip()[:600])

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — une ligne « Banque » qui ment est refusée, une ligne juste passe" % n)
    print("\n%d / %d" % (n, n)); return 0

if __name__ == "__main__":
    sys.exit(main())
