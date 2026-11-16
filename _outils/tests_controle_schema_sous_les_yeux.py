# -*- coding: utf-8 -*-
"""tests_controle_schema_sous_les_yeux.py — le banc de la règle d'or n°331 (le schéma sous les yeux).

Chaque cas pose une page d'essai dans une racine vide, joue le contrôle, et vérifie qu'il
refuse ce qu'il doit refuser — et SURTOUT qu'il laisse passer ce qui montre déjà son schéma,
ou ce qui se fait de mémoire par construction : un contrôle qui refuse le juste finit désactivé.

Usage : python3 _outils/tests_controle_schema_sous_les_yeux.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_schema_sous_les_yeux as C  # noqa: E402
from tests_controle_cadres import par_la_ligne_de_commande  # noqa: E402

SEQ = "theme-2-essai/C4/4e/sequence_4e_essai.html"
RADIO = ('<fieldset class="qcm-groupe"><legend>Bloc 1 ?</legend>'
         '<input type="radio" name="q" id="q1" value="A"><label for="q1">A</label></fieldset>')
FIG = '<figure><svg viewBox="0 0 600 200"><rect width="10" height="10"/></svg><figcaption>Fig. 1</figcaption></figure>'


def page(corps):
    return "<!doctype html><html lang='fr'><body>%s</body></html>" % corps


def carte(titre, corps):
    return '<div class="carte"><h3>%s</h3>%s</div>' % (titre, corps)


def jouer(racine):
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main([str(racine)])
    finally:
        C.DEPOT = ancien
    return code, s.getvalue() + e.getvalue()


def main():
    echecs, n = [], 0

    def cas(titre, fichiers, attendu_code, attendu="", absent=""):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            for rel, contenu in fichiers.items():
                p = pathlib.Path(tmp, rel); p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if code != attendu_code:
            echecs.append("%s : sortie %d au lieu de %d\n     %s" % (titre, code, attendu_code, texte.strip()[:500]))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s" % (titre, attendu, texte.strip()[:500]))
        elif absent and absent in texte:
            echecs.append("%s : message avec « %s » alors qu'il ne devrait pas\n     %s" % (titre, absent, texte.strip()[:500]))

    # — n°299 : ne rien voir n'est pas être vert
    cas("une racine sans page élève est une panne", {"notes.md": "# rien"}, 2, "EN PANNE")
    cas("un QCM seul n'est pas une page lue ici", {"theme-1-x/qcm_essai.html": page("<p>x</p>")}, 2, "EN PANNE")
    cas("une page sans question passe", {SEQ: page("<h2>Titre</h2><p>Regarde le schéma plus haut.</p>")}, 0, "1 page(s) lues")

    # — S1 : le renvoi explicite vers un schéma hors du bloc
    cas("S1 · « le schéma ci-dessus » sans figure dans la carte est refusé",
        {SEQ: page(carte("Doc", FIG) + carte("Activité 1", '<div class="consigne">Lis le schéma ci-dessus.</div>' + RADIO))},
        1, "✘ S1")
    cas("S1 · « la chaîne d'énergie de la séance 2 » est un renvoi",
        {SEQ: page(carte("Activité 3", "<p>Reprends la chaîne d'énergie de la séance 2.</p>" + RADIO))}, 1, "renvoi « de la séance 2 »")
    cas("S1 · la même carte AVEC sa figure passe",
        {SEQ: page(carte("Activité 1", '<div class="consigne">Lis le schéma ci-dessus.</div>' + FIG + RADIO))}, 0, "✅")
    cas("S1 · une image est une figure", {SEQ: page(carte("A", "<p>schéma ci-dessus</p><img src='x.png' alt='schéma'>" + RADIO))}, 0)
    cas("S1 · un <object> SVG est une figure",
        {SEQ: page(carte("A", "<p>schéma ci-dessous</p><object class='figure' data='x.svg' type='image/svg+xml'></object>" + RADIO))}, 0)
    cas("S1 · une icône aria-hidden n'est pas une figure",
        {SEQ: page(carte("A", "<p>schéma ci-dessus</p><img src='i.png' alt='' aria-hidden='true'>" + RADIO))}, 1, "✘ S1")
    cas("S1 · un SVG de 20 unités est une icône, pas une figure",
        {SEQ: page(carte("A", "<p>schéma ci-dessus</p><svg viewBox='0 0 20 20'></svg>" + RADIO))}, 1, "✘ S1")

    # — S2 : nommé sans figure, listé mais non bloquant
    cas("S2 · « complète la chaîne d'information » sans figure est signalé en ⚠, sortie 0",
        {SEQ: page(carte("Activité 2", "<p>Complète la chaîne d'information du jardin.</p>" + RADIO))}, 0, "⚠ S2")
    cas("S2 · la figure lève le ⚠",
        {SEQ: page(carte("Activité 2", "<p>Complète la chaîne d'information du jardin.</p>" + FIG + RADIO))}, 0, absent="⚠ S2")

    # — écarts voulus : ce qui se fait de mémoire, la production de l'élève, les tableaux
    cas("un billet d'entrée se fait de mémoire : pas signalé",
        {SEQ: page(carte("🎫 Billet d'entrée", "<p>Lis le schéma ci-dessus.</p>" + RADIO))}, 0, absent="S1")
    cas("« Avant de commencer : ce que je vérifie » se fait de mémoire",
        {SEQ: page(carte("🔄 Avant de commencer : ce que je vérifie", "<p>Je sais lire un algorigramme.</p>" + RADIO))}, 0, absent="S2")
    cas("« mon algorigramme » est la production de l'élève, pas un document",
        {SEQ: page(carte("Activité 4", "<p>J'exporte mon algorigramme en SVG.</p>" + RADIO))}, 0, absent="S2")
    cas("une cellule de tableau comparatif ne pose pas de question sur le schéma",
        {SEQ: page(carte("Activité 4", "<table><tr><td>qualité d'algorigramme</td></tr></table>" + RADIO))}, 0, absent="S2")
    cas("la correction repliée ne compte pas",
        {SEQ: page(carte("Activité 5", RADIO + "<details class='correction'><summary>Correction</summary><p>Voir le schéma plus haut.</p></details>"))}, 0, absent="S1")

    # — S3 : le schéma replié dans un dépliant fermé (Pascal, 15/11/2026 : « le mettre dehors »)
    REPLIE = "<details><summary>🖼 Le schéma, à ouvrir</summary>" + FIG + "</details>"
    cas("S3 · la seule figure du bloc, dans un dépliant fermé, est signalée (⚠, sortie 0)",
        {SEQ: page(carte("Activité 2", "<p>Complète la chaîne d'énergie.</p>" + REPLIE + RADIO))}, 0, "⚠ S3")
    cas("S3 · le même dépliant ouvert (open) ne cache rien",
        {SEQ: page(carte("Activité 2", "<p>Complète la chaîne d'énergie.</p>" + REPLIE.replace("<details>", "<details open>") + RADIO))}, 0, absent="S3 schéma replié :")
    cas("S3 · une figure à découvert à côté d'une figure repliée : le schéma est sous les yeux",
        {SEQ: page(carte("Activité 2", "<p>Complète la chaîne d'énergie.</p>" + FIG + REPLIE + RADIO))}, 0, absent="S3 schéma replié :")
    cas("S3 · une figure dans une aide, un guide pas à pas ou un dévoilement voulu n'est pas un schéma replié",
        {SEQ: page(carte("Activité 2", "<p>Construis-la.</p><details class='aide2'><summary>Aide</summary>" + FIG + "</details>"
                         "<details class='guide-replie'><summary>Guide</summary>" + FIG + "</details>"
                         "<details class='ppa-fixe'><summary>À ouvrir après l'animation</summary>" + FIG + "</details>" + RADIO))}, 0, absent="S3 schéma replié :")

    # — le point d'entrée parle et sort proprement (n°299). Sur le dépôt réel, 1 est une sortie
    #    légitime tant qu'il reste des renvois hors bloc à corriger : seuls 2 (rien lu) et une
    #    sortie muette sont des pannes.
    code, texte = par_la_ligne_de_commande("controle_schema_sous_les_yeux.py")
    if code not in (0, 1):
        echecs.append("lancé en ligne de commande, le contrôle sort à %d :\n     %s" % (code, texte.strip()[:400]))
    if not any(c.isdigit() for c in texte):
        echecs.append("lancé en ligne de commande, le contrôle n'écrit AUCUN chiffre (règle n°299)")

    if echecs:
        print("✘ %d/%d cas en échec :" % (len(echecs), n))
        for e in echecs:
            print(" -", e)
        return 1
    print("✅ %d/%d cas passent — controle_schema_sous_les_yeux.py refuse les renvois hors bloc et laisse passer le juste" % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
