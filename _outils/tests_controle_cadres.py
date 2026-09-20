# -*- coding: utf-8 -*-
"""tests_controle_cadres.py — le banc du cadre Vittascience interdit.

Usage : python3 _outils/tests_controle_cadres.py
"""
import contextlib, io, os, pathlib, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_cadres as C  # noqa: E402


def jouer(racine):
    """Le contrôle joué sur une racine d'essai — stdout ET stderr, car la
    panne de la règle n°299 part volontairement sur la sortie d'erreur."""
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main()
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

    cas("une racine sans la moindre page est une panne, pas un succès",
        {"notes.md": "# rien à lire ici"}, True, "EN PANNE")

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
    # Deux fichiers, pas un : sans la page hors archive, cette racine ne faisait
    # RIEN ouvrir au contrôle, qui sortait à 0 — le cas passait au vert en ne
    # prouvant rien (règle d'or n°299).
    cas("l'archive est une trace, pas une ressource — et le reste est bien lu",
        {"_archive-anciennes-versions/v.html": '<iframe src="https://fr.vittascience.com/python/"></iframe>',
         "s.html": '<p>une page ordinaire, sans cadre</p>'}, False, "1 page(s) lues")

    n += 1
    code, texte = jouer(C.DEPOT)
    if code != 0: echecs.append("le dépôt réel porte encore des cadres :\n     " + texte.strip())

    # Le VRAI point d'entrée, en sous-processus (règle d'or n°299).
    n += 1
    echecs.extend(reproches_de_la_ligne_de_commande('controle_cadres.py'))

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — un cadre <iframe> vers fr.vittascience.com est refusé" % n)
    print("\n%d / %d" % (n, n)); return 0


if __name__ == "__main__":
    sys.exit(main())
