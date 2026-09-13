# -*- coding: utf-8 -*-
"""tests_controle_cadres.py — le banc du cadre Vittascience interdit.

Usage : python3 _outils/tests_controle_cadres.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_cadres as C  # noqa: E402


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
    def cas(titre, fichiers, doit_refuser, attendu=""):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            for rel, contenu in fichiers.items():
                p = pathlib.Path(tmp, rel); p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if doit_refuser and code == 0: echecs.append(titre + " : accepté, alors qu'il fallait refuser")
        elif not doit_refuser and code != 0: echecs.append(titre + " : refusé\n     " + texte.strip())
        elif attendu and attendu not in texte: echecs.append(titre + " : message sans « %s »" % attendu)

    cas("le lien-bouton du gabarit passe",
        {"s.html": '<a class="btn vs-lien" href="https://fr.vittascience.com/python/" target="_blank">▶</a>'}, False)
    cas("le cadre Python du 12/09 est refusé",
        {"s.html": '<iframe loading="lazy" src="https://fr.vittascience.com/python/?mode=mixed&amp;console=bottom"></iframe>'},
        True, "1 cadre(s)")
    cas("le code d'intégration officiel embed=1 est refusé aussi (SAMEORIGIN mesuré)",
        {"s.html": "<iframe width='100%' src=\"https://fr.vittascience.com/arduino/?link=6a8e2a2348ed2&embed=1\"></iframe>"},
        True, "1 page(s)")
    cas("deux cadres dans une page, comptés",
        {"s.html": '<iframe src="https://fr.vittascience.com/a"></iframe><iframe src="https://fr.vittascience.com/b"></iframe>'},
        True, "2 cadre(s)")
    cas("un cadre vers un autre site n'est pas l'affaire de ce contrôle",
        {"s.html": '<iframe src="https://www.youtube-nocookie.com/embed/x"></iframe>'}, False)
    cas("l'archive est une trace, pas une ressource",
        {"_archive-anciennes-versions/v.html": '<iframe src="https://fr.vittascience.com/python/"></iframe>'}, False)

    n += 1
    code, texte = jouer(C.DEPOT)
    if code != 0: echecs.append("le dépôt réel porte encore des cadres :\n     " + texte.strip())

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — un cadre <iframe> vers fr.vittascience.com est refusé" % n)
    print("\n%d / %d" % (n, n)); return 0


if __name__ == "__main__":
    sys.exit(main())
