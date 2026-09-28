# -*- coding: utf-8 -*-
"""tests_controle_navigation_seances.py — le banc de la séance qui ne mène nulle part.

Rejoue le cas réel du 28/09 (31 pages sur 40 sans bouton de fin de séance, règle
n°101), les cas qui doivent passer, et le dépôt réel.

Usage : python3 _outils/tests_controle_navigation_seances.py
"""
import contextlib, io, os, pathlib, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_navigation_seances as C  # noqa: E402

TABS3 = ('<div class="seance-tabs"><button class="seance-tab active" data-panel="s1" '
         'id="tab-s1">Séance 1</button><button class="seance-tab" data-panel="s2" '
         'id="tab-s2">Séance 2</button><button class="seance-tab" data-panel="s3" '
         'id="tab-s3">Séance 3</button></div>')
BOUTON = ('<p class="page-suivante"><button class="btn vers-seance" data-vers="%s" '
          'type="button">%s ›</button></p>')


def page(p1_extra="", p2_extra="", tabs=TABS3):
    # Fermeture sur sa propre ligne : c'est la forme réelle de toutes les pages
    # du dépôt, et c'est ce que `fin_reelle_du_panneau` reconnaît.
    return ("<html><body>%s\n"
            '<div class="seance-panel" id="s1">Contenu 1.\n%s\n</div>\n'
            '<div class="seance-panel" id="s2">Contenu 2.\n%s\n</div>\n'
            '<div class="seance-panel" id="s3">Contenu 3.\n</div>\n'
            "</body></html>\n") % (tabs, p1_extra, p2_extra)


def jouer(racine):
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO()
    try:
        with contextlib.redirect_stdout(s):
            code = C.main(muet=True)
    finally:
        C.DEPOT = ancien
    return code, s.getvalue()


def par_la_ligne_de_commande(args=()):
    ici = os.path.dirname(os.path.abspath(__file__))
    r = subprocess.run([sys.executable, os.path.join(ici, "controle_navigation_seances.py")] + list(args),
                        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    echecs, n = [], 0

    def cas(titre, contenu, doit_refuser, attendu=""):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            pathlib.Path(tmp, "sequence_x.html").write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if doit_refuser and code == 0:
            echecs.append(titre + " : accepté, alors qu'il fallait refuser")
        elif not doit_refuser and code != 0:
            echecs.append(titre + " : refusé\n     " + texte.strip())
        elif attendu and attendu not in texte:
            echecs.append(titre + " : message sans « %s »\n     %s" % (attendu, texte.strip()))

    cas("les deux boutons présents, vers le bon panneau",
        page(BOUTON % ("s2", "Séance 2"), BOUTON % ("s3", "Séance 3")), False)

    cas("le premier bouton absent",
        page("", BOUTON % ("s3", "Séance 3")),
        True, "aucun bouton .vers-seance vers « s2 »")

    cas("le bouton pointe sur le mauvais panneau (data-vers=\"s3\" au lieu de \"s2\")",
        page(BOUTON % ("s3", "Séance 3 (erreur)"), BOUTON % ("s3", "Séance 3")),
        True, "aucun bouton .vers-seance vers « s2 »")

    cas("le dernier onglet n'a besoin de rien : conforme sans bouton en s3",
        page(BOUTON % ("s2", "Séance 2"), BOUTON % ("s3", "Séance 3")), False)

    # Bug réel du 28/09/2026 (3e_C1.5, 4e_C1.4) : le bouton cite le bon
    # panneau, mais posé APRÈS la fermeture du panneau — donc hors de lui,
    # affiché en permanence quel que soit l'onglet actif. Seul le banc au
    # navigateur l'avait vu ; ce cas verrouille que le contrôle statique le
    # voit désormais aussi.
    orphelin = ('<html><body>%s\n'
                '<div class="seance-panel" id="s1">Contenu 1.\n</div>\n'
                '%s\n'
                '<div class="seance-panel" id="s2">Contenu 2.\n%s\n</div>\n'
                '<div class="seance-panel" id="s3">Contenu 3.\n</div>\n'
                '</body></html>\n') % (TABS3, BOUTON % ("s2", "Séance 2"), BOUTON % ("s3", "Séance 3"))
    cas("le bouton cite le bon panneau mais est posé APRÈS la fermeture du panneau (orphelin, toujours visible)",
        orphelin, True, "aucun bouton .vers-seance vers « s2 »")

    TABS_HORS = TABS3.replace(
        '</div>',
        '<button class="seance-tab hors" data-panel="shors" id="tab-shors">Hors parcours</button></div>')
    cas("un onglet « hors » (bonus hors compétence) n'exige de bouton ni vers lui, ni depuis lui",
        ('<html><body>%s'
         '<div class="seance-panel" id="s1">1.%s</div>'
         '<div class="seance-panel" id="s2">2.%s</div>'
         '<div class="seance-panel" id="s3">3.</div>'
         '<div class="seance-panel" id="shors">Bonus, hors du parcours normal.</div>'
         '</body></html>\n') % (TABS_HORS, BOUTON % ("s2", "Séance 2"), BOUTON % ("s3", "Séance 3")),
        False)

    # Bug réel du 28/09/2026 (4e_C1.4) : le panneau « hors » (bloc Python, hors
    # compétence) est intercalé PHYSIQUEMENT entre s1 et s2 dans le fichier, bien
    # qu'exclu de la chaîne logique. Un bouton égaré dedans (au lieu d'être dans
    # s1) se faisait compter à tort comme le bouton de s1, parce que la recherche
    # allait jusqu'au prochain onglet de la chaîne LOGIQUE (s2) au lieu de
    # s'arrêter au tout premier panneau suivant DANS LE FICHIER.
    hors_intercale = ('<html><body>%s\n'
                       '<div class="seance-panel" id="s1">Contenu 1.\n</div>\n'
                       '<div class="seance-panel" id="shors">Bonus.\n%s\n</div>\n'
                       '<div class="seance-panel" id="s2">Contenu 2.\n%s\n</div>\n'
                       '<div class="seance-panel" id="s3">Contenu 3.\n</div>\n'
                       '</body></html>\n') % (TABS_HORS, BOUTON % ("s2", "Séance 2"), BOUTON % ("s3", "Séance 3"))
    cas("le panneau « hors » est intercalé entre s1 et s2 : un bouton égaré dedans ne compte pas pour s1",
        hors_intercale, True, "aucun bouton .vers-seance vers « s2 »")

    # La fermeture d'un panneau peut porter un commentaire de fin de bloc sur la
    # même ligne (ex. `</div><!-- fin de #s1 -->`, forme réelle de 4e_C1.4) : un
    # bouton posé correctement juste avant cette fermeture ne doit pas être exclu
    # à tort (bug réel du 28/09/2026, trouvé en corrigeant ce même fichier).
    fermeture_commentee = ("<html><body>%s\n"
                            '<div class="seance-panel" id="s1">Contenu 1.\n%s\n</div><!-- fin de #s1 -->\n'
                            '<div class="seance-panel" id="s2">Contenu 2.\n%s\n</div>\n'
                            '<div class="seance-panel" id="s3">Contenu 3.\n</div>\n'
                            "</body></html>\n") % (TABS3, BOUTON % ("s2", "Séance 2"), BOUTON % ("s3", "Séance 3"))
    cas("la fermeture porte un commentaire de fin de bloc sur la même ligne : le bouton posé juste avant n'est pas exclu à tort",
        fermeture_commentee, False)

    cas("une page à un seul onglet n'est pas jugée (rien à enchaîner)",
        '<html><body><button class="seance-tab" data-panel="s1">Séance 1</button>'
        '<div class="seance-panel" id="s1">Seule.</div></body></html>', False)

    cas("une page sans onglet n'est pas jugée", "<html><body><p>rien</p></body></html>", False)

    # Règle d'or n°299 : une racine sans page .html est une panne, pas un succès muet.
    n += 1
    with tempfile.TemporaryDirectory() as tmp:
        pathlib.Path(tmp, "notes.md").write_text("# rien à lire", encoding="utf-8")
        code, texte = jouer(tmp)
    if code != 2:
        echecs.append("une racine sans page .html : sortie %d au lieu de 2" % code)
    elif "EN PANNE" not in texte:
        echecs.append("une racine sans page .html : la panne n'est pas annoncée")

    # Le dépôt réel.
    n += 1
    code, texte = jouer(C.DEPOT)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip())

    # Le vrai point d'entrée, en sous-processus (règle d'or n°299 : un script doit
    # écrire quelque chose de chiffré, pas rester muet en cas de panne silencieuse).
    n += 1
    code, texte = par_la_ligne_de_commande()
    if code != 0:
        echecs.append("lancé en ligne de commande, le contrôle sort à %d :\n     %s"
                       % (code, texte.strip()[:400]))
    if not any(c.isdigit() for c in texte):
        echecs.append("lancé en ligne de commande, le contrôle n'écrit aucun chiffre")

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n))
        return 1
    print("✅ %d contrôles — une séance sans bouton vers la suivante, ou pointant au mauvais "
          "endroit, est refusée" % n)
    print("\n%d / %d" % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
