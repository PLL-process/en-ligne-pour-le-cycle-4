# -*- coding: utf-8 -*-
"""tests_controle_correction_complete.py — le banc de la règle d'or n°332 (la correction montre la production complète).

Chaque cas pose une page d'essai dans une racine vide, joue le contrôle, et vérifie qu'il relève ce qu'il doit relever —
et SURTOUT qu'il laisse passer ce qui montre déjà la production et donne son fichier, ou ce qui ne fait rien produire
avec un outil : un contrôle qui signale le juste finit désactivé (n°248).

Usage : python3 _outils/tests_controle_correction_complete.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_correction_complete as C  # noqa: E402
import controle_schema_sous_les_yeux as N331  # noqa: E402

SEQ = "theme-2-essai/C4/4e/sequence_4e_essai.html"
FAIT = '<div class="ligne-exo"><input type="checkbox" id="f1"><label for="f1">J\'ai construit mon fichier</label></div>'
CONSIGNE = "<p>📌 Consigne : construis l'algorigramme du trajet dans draw.io, puis enregistre ton fichier.</p>"
FIG = '<figure><svg viewBox="0 0 480 900"><rect width="10" height="10"/></svg><figcaption>L\'algorigramme complet</figcaption></figure>'
BOUTON = '<div class="telechargements"><button type="button" data-fichier="algo.drawio">algo.drawio</button></div>'


def page(corps):
    return "<!doctype html><html lang='fr'><body>%s</body></html>" % corps


def carte(titre, corps):
    return '<div class="carte"><h3>%s</h3>%s</div>' % (titre, corps)


def correction(corps):
    return '<details class="correction"><summary>✅ Correction</summary><div class="contenu">%s</div></details>' % corps


def jouer(racine, options=()):
    anciens = C.DEPOT, N331.DEPOT
    C.DEPOT = N331.DEPOT = str(racine)
    s, e = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main(list(options) + [str(racine)])
    finally:
        C.DEPOT, N331.DEPOT = anciens
    return code, s.getvalue() + e.getvalue()


def main():
    echecs, n = [], 0

    def cas(titre, fichiers, attendu_code, attendu="", absent="", options=()):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            for rel, contenu in fichiers.items():
                p = pathlib.Path(tmp, rel); p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp, options)
        if code != attendu_code:
            echecs.append("%s : sortie %d au lieu de %d\n     %s" % (titre, code, attendu_code, texte.strip()[:500]))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s" % (titre, attendu, texte.strip()[:500]))
        elif absent and absent in texte:
            echecs.append("%s : message avec « %s » alors qu'il ne devrait pas\n     %s" % (titre, absent, texte.strip()[:500]))

    # — n°299 : ne rien voir n'est pas être vert
    cas("une racine sans page élève est une panne", {"notes.md": "# rien"}, 2, "EN PANNE")
    cas("une synthèse ne fait rien produire : elle n'est pas lue", {"theme-1-x/synthese_eleve_x.html": page("<p>x</p>")}, 2, "EN PANNE")

    # — K1 : aucune correction
    cas("K1 · construire dans draw.io sans correction est relevé (⚠, sortie 0)",
        {SEQ: page(carte("Activité 3.2", CONSIGNE + FAIT))}, 0, "⚠ K1")
    cas("K1 · avec --strict, c'est un ✘ et la sortie vaut 1",
        {SEQ: page(carte("Activité 3.2", CONSIGNE + FAIT))}, 1, "✘ K1", options=["--strict"])

    # — K2 : une correction qui décrit sans montrer
    cas("K2 · une correction en mots seulement est relevée",
        {SEQ: page(carte("Activité 3.2", CONSIGNE + FAIT + correction("<p>Compare ton fichier au modèle.</p>")))}, 0, "⚠ K2")
    cas("K2 · un programme écrit en entier montre la production",
        {SEQ: page(carte("Activité 2", "<p>Écris ton programme dans l'éditeur Python, puis lance-le.</p>" + FAIT
                         + correction("<pre>a = 1\nb = 2\nif a < b:\n    print(a)\n</pre>") + BOUTON))}, 0, "✅")

    # — K3 : la production montrée, le fichier non donné
    cas("K3 · la figure sans le fichier est relevée",
        {SEQ: page(carte("Activité 3.2", CONSIGNE + FAIT + correction(FIG)))}, 0, "⚠ K3")
    cas("K3 · reste un ⚠ même avec --strict (un fichier n'a pas de sens partout)",
        {SEQ: page(carte("Activité 3.2", CONSIGNE + FAIT + correction(FIG)))}, 0, "⚠ K3", options=["--strict"])
    cas("K3 · un lien vers un .odp donne le fichier",
        {SEQ: page(carte("Activité 4.3", "<p>Construis le diaporama dans Impress.</p>" + FAIT
                         + correction(FIG + '<a href="modele.odp">le modèle</a>')))}, 0, "✅")

    # — ce qui passe
    cas("la figure ET le bouton de téléchargement : rien à dire",
        {SEQ: page(carte("Activité 3.2", CONSIGNE + FAIT + correction(FIG + BOUTON)))}, 0, "✅")
    cas("un outil nommé sans demande de produire n'est pas une production",
        {SEQ: page(carte("Activité 1", "<p>draw.io est un logiciel gratuit, sans compte.</p>"
                         '<fieldset class="qcm-groupe"><legend>Il demande un compte ?</legend>'
                         '<input type="radio" name="q" id="q1" value="non"><label for="q1">non</label></fieldset>'))}, 0, "✅")
    cas("une question qui nomme l'outil n'est pas une consigne de production",
        {SEQ: page(carte("Activité 4.2", "<p>Quel format j'exporte pour mon diaporama ?</p>" + FAIT))}, 0, "✅")
    cas("l'encadré des rôles (« le pilote tient l'outil — le tableur ») ne compte pas",
        {SEQ: page(carte("Activité 3.1", '<section class="roles"><p>Le pilote tient l\'outil — le clavier, le capteur, '
                                          'le tableur. Il complète la fiche.</p></section>' + FAIT))}, 0, "✅")
    cas("un panneau qui contient des cartes n'est pas jugé à leur place",
        {SEQ: page('<section class="panneau"><p>Construis le diaporama dans Impress.</p>' + FAIT
                   + carte("Activité 4.3", "<p>Construis le diaporama dans Impress.</p>" + FAIT + correction(FIG + BOUTON))
                   + "</section>")}, 0, "✅")
    cas("l'encart « les quatre gestes » (un échauffement, l'éditeur en vrai) n'est pas jugé",
        {SEQ: page('<section class="card gestes-outil"><h2>Les quatre gestes de l\'éditeur Python</h2>'
                   "<p>Écris ton prénom dans l'éditeur Python, puis exécute.</p>" + FAIT + "</section>")}, 0, "✅")
    cas("un billet d'entrée se fait de mémoire : il n'est pas jugé",
        {SEQ: page(carte("🎫 Billet d'entrée", CONSIGNE + FAIT))}, 0, "✅")

    print("%d / %d cas réussis" % (n - len(echecs), n))
    for e in echecs:
        print("✘", e)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
