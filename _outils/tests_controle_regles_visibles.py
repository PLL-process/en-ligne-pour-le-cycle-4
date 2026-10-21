# -*- coding: utf-8 -*-
"""tests_controle_regles_visibles.py — le banc de la règle d'or n°309 : l'élève lit le savoir, pas la fabrique.

Rejoue les cas réels du 21/10/2026 (un numéro de règle sous un plan de métro, « convention du dépôt » dans la
légende d'un schéma, un pied de page « v1 Grok — v2 mise en conformité règles 11/13 (Fable) », « recopié, pas
reformulé » dans un titre, un nom de lot dans une nouveauté de l'index, un numéro de règle dans la chaîne d'un QCM),
les cas qui doivent passer (le même texte dans un commentaire HTML, CSS ou JavaScript ; « Règle d'or du schéma » sans
numéro ; une synthèse professeur ; le modèle de TP ; une règle du cours exemptée nommément), la panne d'une racine
vide (règle d'or n°299) et le dépôt réel.

Usage : python3 _outils/tests_controle_regles_visibles.py
"""
import contextlib, io, os, pathlib, shutil, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_regles_visibles as C  # noqa: E402

PAGE = '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>t</title>%s</head><body>%s</body></html>\n'
SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 50">%s</svg>\n'


def page(corps, tete=""):
    return PAGE % (tete, corps)


def jouer(racine):
    """stdout ET stderr : la panne de la règle n°299 part sur stderr."""
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main()
    finally:
        C.DEPOT = ancien
    return code, s.getvalue() + e.getvalue()


def lancer(script, cwd=None):
    """Le contrôle lancé comme on le lance vraiment : `python <script>` (règle d'or n°299)."""
    r = subprocess.run([sys.executable, script], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=300, cwd=cwd)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    echecs, n = [], 0

    def cas(titre, fichiers, doit_refuser, attendu=""):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            for nom, contenu in fichiers.items():
                p = pathlib.Path(tmp, nom); p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if doit_refuser and code != 1: echecs.append("%s : sortie %d au lieu de 1\n     %s" % (titre, code, texte.strip()))
        elif not doit_refuser and code != 0: echecs.append("%s : refusé\n     %s" % (titre, texte.strip()))
        elif attendu and attendu not in texte: echecs.append("%s : message sans « %s »" % (titre, attendu))

    # ── les cas réels : refusés ─────────────────────────────────────────────
    cas("le plan de métro : « (règle n°8 : le bon outil pour la bonne question) » dans un texte SVG",
        {"a.svg": SVG % '<text>Plan simplifié (règle n°8 : le bon outil pour la bonne question)</text>'}, True, "un numéro de règle")
    cas("« règle d'or n°18 » dans un titre de section",
        {"s.html": page("<h2>Le contrat de la séquence (règle d'or n°18)</h2>")}, True, "ligne 1")
    cas("l'apostrophe typographique : « règle d’or n°12 »",
        {"s.html": page("<p>modernisation prévue (règle d’or n°12)</p>")}, True)
    cas("un numéro de règle dans une infobulle (attribut title)",
        {"s.html": page('<span title="Ressource héritée (règle d\'or n°12)">🛠</span>')}, True)
    cas("un numéro de règle dans le <desc> d'un SVG",
        {"a.svg": SVG % "<desc>Schéma disposé selon la règle n°6.</desc>"}, True)
    cas("un numéro de règle dans la chaîne JavaScript d'un QCM (ce que l'élève lit en correction)",
        {"qcm.html": page("", '<script>const QUESTIONS=[{ret:"Rien d\'autre (règle n°47)."}];</script>')}, True)
    cas("« (règle 18) » sans n°, entre parenthèses",
        {"s.html": page("<p>algorigramme, blocs↔Python (règle 18)</p>")}, True)
    cas("« CRCN règle 7 » dans un badge",
        {"s.html": page('<span class="badge">CRCN règle 7</span>')}, True)
    cas("le pied de page de version : « v1 Grok — v2 mise en conformité règles 11/13 (Fable, 01/08/2026) »",
        {"s.html": page("<footer>New York · v1 Grok — v2 mise en conformité règles 11/13 (Fable, 01/08/2026)</footer>")}, True)
    cas("« convention du dépôt » dans la légende d'un SVG",
        {"a.svg": SVG % "<text>Schéma original · convention du dépôt : information en haut</text>"}, True, "« du dépôt » / « ce dépôt »")
    cas("« ce dépôt » coupé par un retour à la ligne",
        {"s.html": page("<p>codes de classement internes à ce\n  dépôt</p>")}, True)
    cas("« recopié, pas reformulé » dans un titre",
        {"s.html": page("<h2>🎯 Ce que dit le programme — recopié, pas reformulé</h2>")}, True, "recopié, pas reformulé")
    cas("un nom de lot dans une nouveauté : « lot 3e_C9.2 »", {"s.html": page("<p>(lot 3e_C9.2)</p>")}, True, "un lot ou une vague")
    cas("un nom de lot nommé : « Lot Shanghai 5e »", {"s.html": page("<p>Lot Shanghai 5e « Quel véhicule ? »</p>")}, True)
    cas("« LOT 04 » dans les données de l'index", {"index.html": page('<script>var N=[{"lot":"Thème 2 — LOT 04"}];</script>')}, True)
    cas("« décision de Pascal »", {"s.html": page("<p>décision de Pascal, 02/09</p>")}, True)
    cas("« journal des décisions » en lien visible", {"s.html": page('<a href="J.md">Le journal des décisions</a>')}, True)
    cas("deux traces dans la même page : le fichier est refusé et chaque ligne est dite",
        {"s.html": page("<p>a (règle n°1)</p>\n<p>b du dépôt</p>")}, True, "ligne 2")

    # ── les cas qui doivent passer ──────────────────────────────────────────
    cas("le même numéro dans un commentaire HTML : permis",
        {"s.html": page("<!-- règle d'or n°308 : un bloc se capture -->\n<p>Bonjour</p>")}, False)
    cas("dans un commentaire CSS : permis",
        {"s.html": page("<p>x</p>", "<style>/* Règle d'or n°303 — un lien se lit */ p{color:red}</style>")}, False)
    cas("dans un commentaire JavaScript, sur une ligne et en bloc : permis",
        {"s.html": page("<p>x</p>", "<script>\n// règle n°18 : le concept invariant\n/* règle d'or n°12 */\nvar a=1; // du dépôt\n</script>")}, False)
    cas("une URL dans un script n'est pas prise pour un commentaire (la ligne qui suit est lue)",
        {"s.html": page("", '<script>var u="https://exemple.fr/a"; var m="(règle n°5)";</script>')}, True)
    cas("« Règle d'or du schéma » sans numéro : une règle de métier enseignée à l'élève",
        {"s.html": page("<p>📐 Règle d'or du schéma : l'INFORMATION en haut, l'ÉNERGIE en bas.</p>")}, False)
    cas("« la règle du jeu », « règle de trois » : permis",
        {"s.html": page("<p>La règle du jeu&nbsp;: on applique la règle de trois. Règle 1 : une variable = une boîte.</p>")}, False)
    cas("une synthèse professeur peut citer la fabrique",
        {"synthese_professeur_5e_C1.1.html": page("<p>(règle n°42) · lot 5e_C1.1 · Fable</p>"), "ok.html": page("<p>Bonjour</p>")}, False)
    cas("une fiche pour les collègues aussi",
        {"fiche_maths_tp_4e_socle.html": page("<p>(règle d'or n°81 du dépôt)</p>"), "ok.html": page("<p>Bonjour</p>")}, False)
    cas("le modèle de TP destiné aux auteurs est exempté nommément",
        {"atelier/tp_modele_demonstration.html": page("<p>Règle n°79 : le premier geste est un rangement.</p>"), "ok.html": page("<p>Bonjour</p>")}, False)
    cas("les archives, _outils et _generation ne sont pas jugés",
        {"_archive-anciennes-versions/vieux.html": page("<p>(règle n°1)</p>"),
         "_outils/gabarit.html": page("<p>(règle n°2)</p>"),
         "a/_generation/page.html": page("<p>(règle n°3)</p>"), "ok.html": page("<p>Bonjour</p>")}, False)
    cas("la règle du cours « Règle n°1 » du fichier exempté passe, et le dit",
        {"memoire_boites_etiquetees.svg": SVG % "<text>Règle n°1 : une variable = une boîte</text><text>Règle n°2 : x</text>"}, False)
    cas("… mais une autre trace dans le même fichier exempté est refusée",
        {"memoire_boites_etiquetees.svg": SVG % "<text>Règle n°1 : une variable = une boîte</text><text>(règle n°8)</text>"}, True)
    cas("un SVG et une page sans aucune trace : verts",
        {"a.svg": SVG % "<text>Plan simplifié, non à l'échelle — comme tous les plans de métro du monde.</text>",
         "s.html": page("<p>Ces codes servent à ranger les séquences ; ils ne viennent pas du programme officiel.</p>")}, False)

    # ── règle d'or n°299 : une racine sans fichier lisible n'est pas « aucune trace », c'est une panne ──
    n += 1
    with tempfile.TemporaryDirectory() as tmp:
        pathlib.Path(tmp, "notes.md").write_text("# rien à lire", encoding="utf-8")
        code, texte = jouer(tmp)
    if code != 2: echecs.append("une racine sans fichier lisible : sortie %d au lieu de 2" % code)
    elif "EN PANNE" not in texte: echecs.append("une racine sans fichier lisible : la panne n'est pas annoncée")

    # … et au vrai point d'entrée : le script recopié dans une racine vide sort à 2, pas à 0.
    n += 1
    ici = os.path.dirname(os.path.abspath(__file__))
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "_outils"))
        for f in ("controle_regles_visibles.py", "panne.py"):
            shutil.copy(os.path.join(ici, f), os.path.join(tmp, "_outils", f))
        code, texte = lancer(os.path.join(tmp, "_outils", "controle_regles_visibles.py"))
    if code != 2: echecs.append("lancé en ligne de commande sur une racine vide, le contrôle sort à %d (attendu 2) :\n     %s" % (code, texte.strip()))

    # Le dépôt réel, par le point d'entrée, avec des chiffres à l'écran (un script muet ne prouve rien).
    n += 1
    code, texte = lancer(os.path.join(ici, "controle_regles_visibles.py"))
    if code != 0: echecs.append("le dépôt réel ne passe pas (code %d) :\n     %s" % (code, texte.strip()[:800]))
    elif not any(c.isdigit() for c in texte): echecs.append("lancé en ligne de commande, le contrôle n'écrit AUCUN chiffre (règle d'or n°299)")

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — la fabrique visible est refusée partout où elle peut se cacher, et permise là où elle a le droit d'être" % n)
    print("\n%d / %d" % (n, n)); return 0


if __name__ == "__main__":
    sys.exit(main())
