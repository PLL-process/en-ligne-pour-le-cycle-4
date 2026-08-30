# -*- coding: utf-8 -*-
"""tests_controle_liens.py — rejouer les erreurs qui ont fait naître l'outil.

Deux familles de cas, et les deux comptent autant :

  · **ce qu'il doit voir** — la barre de navigation d'une synthèse recopiée
    depuis une page qui vit un dossier plus haut. C'est l'erreur réelle : seize
    liens morts dans quatre fichiers livrés, et rien à l'œil ne la distingue
    d'une barre juste.

  · **ce sur quoi il ne doit pas crier** — les cinq fausses alertes de la
    première version. Une adresse en commentaire HTML n'est pas un lien ; une
    adresse fabriquée par un script (`${q.img}`) n'est pas un chemin. Un contrôle
    neuf qui trouve beaucoup de fautes a d'abord tort (règle d'or n°248), et
    c'est ici qu'on l'écrit.

Les cas travaillent sur une arborescence temporaire, pas sur le dépôt : un test
qui dépend de l'état du dépôt cesse de tester le jour où le dépôt change.

Usage : python3 _outils/tests_controle_liens.py
Sortie : 0 si tout passe, 1 sinon.
"""
import os
import pathlib
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from controle_liens import adresses, locale, parcourir, taire  # noqa: E402

#: la barre de navigation telle qu'elle a été livrée dans `Synthèses/` — fausse
NAV_FAUSSE = ('<nav id="navharm"><a href="../../../../index.html">Accueil</a>'
              '<a href="sequence_5e_C8.1_patere-du-hall.html">La séquence</a>'
              '<a href="qcm_5e_C8.1_patere-du-hall.html">Le QCM</a></nav>')
#: la même, corrigée d'un niveau
NAV_JUSTE = ('<nav id="navharm"><a href="../../../../../index.html">Accueil</a>'
             '<a href="../sequence_5e_C8.1_patere-du-hall.html">La séquence</a>'
             '<a href="../qcm_5e_C8.1_patere-du-hall.html">Le QCM</a></nav>')


def arborescence(racine, nav):
    """Un lot minuscule, à la forme exacte de ceux du dépôt."""
    lot = racine / "theme-3" / "C8" / "5e" / "5e_C8.1"
    (lot / "Synthèses").mkdir(parents=True)
    (racine / "index.html").write_text("<a href='theme-3/C8/5e/5e_C8.1/x.html'>x</a>",
                                       encoding="utf-8")
    (lot / "sequence_5e_C8.1_patere-du-hall.html").write_text("<p>séquence</p>", encoding="utf-8")
    (lot / "qcm_5e_C8.1_patere-du-hall.html").write_text("<p>qcm</p>", encoding="utf-8")
    (lot / "Synthèses" / "synthese_eleve_5e_C8.1.html").write_text(nav, encoding="utf-8")
    return lot


def cas_nav_fausse():
    """Les trois liens de la barre recopiée sont morts, et l'outil les nomme."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        arborescence(racine, NAV_FAUSSE)
        _v, casses, _e, _t = parcourir(racine, tout=True)
        adr = sorted(a for _p, a in casses)
        attendu = sorted(["../../../../index.html",
                          "sequence_5e_C8.1_patere-du-hall.html",
                          "qcm_5e_C8.1_patere-du-hall.html"])
        return adr == attendu, "cassés = %s" % adr
    finally:
        shutil.rmtree(racine)


def cas_nav_juste():
    """La même barre corrigée d'un niveau ne doit plus rien déclencher."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        arborescence(racine, NAV_JUSTE)
        _v, casses, _e, _t = parcourir(racine, tout=True)
        return not casses, "cassés = %s" % [a for _p, a in casses]
    finally:
        shutil.rmtree(racine)


def cas_commentaire():
    """Une photo proposée dans un bloc `<!-- … -->` n'est pas un lien mort."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "p.html").write_text(
            "<p>texte</p>\n<!-- 📷 à décommenter :\n"
            '<figure><img src="photos/absente.jpg" alt="a"></figure>\n-->\n',
            encoding="utf-8")
        _v, casses, _e, tues = parcourir(racine, tout=True)
        return (not casses and tues == 1), "cassés = %s, zones tues = %d" % (
            [a for _p, a in casses], tues)
    finally:
        shutil.rmtree(racine)


def cas_gabarit():
    """`src="${q.img}"` est fabriqué à l'exécution : ce n'est pas un chemin."""
    return (not locale("${q.img}") and not locale("{{ image }}")
            and locale("../images/vraie.png")), "les trois formes"


def cas_script():
    """Une adresse à l'intérieur d'un <script> n'est pas suivie par le contrôle."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "p.html").write_text(
            '<p>ok</p><script>var t = \'<img src="absente.png">\';</script>',
            encoding="utf-8")
        _v, casses, _e, _t = parcourir(racine, tout=True)
        return not casses, "cassés = %s" % [a for _p, a in casses]
    finally:
        shutil.rmtree(racine)


def cas_markdown():
    """En Markdown, un lien de texte compte ; un lien dans un bloc de code, non."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "R.md").write_text(
            "Voir [la séquence](sequence_absente.html).\n\n"
            "```\n[exemple](aussi_absente.html)\n```\n", encoding="utf-8")
        _v, casses, _e, _t = parcourir(racine, tout=True)
        adr = [a for _p, a in casses]
        return adr == ["sequence_absente.html"], "cassés = %s" % adr
    finally:
        shutil.rmtree(racine)


def cas_ancre_seule():
    """Un lien `#partie-2` reste dans la page : il n'y a pas de fichier à trouver."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "p.html").write_text('<a href="#partie-2">bas de page</a>', encoding="utf-8")
        v, casses, _e, _t = parcourir(racine, tout=True)
        return (v == 0 and not casses), "vérifiés = %d, cassés = %d" % (v, len(casses))
    finally:
        shutil.rmtree(racine)


def cas_ancre_sur_fichier():
    """`page.html#partie-2` : on vérifie le fichier, et on s'arrête là."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "page.html").write_text("<h2 id='autre'>x</h2>", encoding="utf-8")
        (racine / "p.html").write_text('<a href="page.html#partie-2">là</a>', encoding="utf-8")
        _v, casses, _e, _t = parcourir(racine, tout=True)
        return not casses, "cassés = %s" % [a for _p, a in casses]
    finally:
        shutil.rmtree(racine)


def cas_espace_encode():
    """Un nom de fichier avec un espace s'écrit `%20` dans une adresse."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "mon fichier.html").write_text("x", encoding="utf-8")
        (racine / "p.html").write_text('<a href="mon%20fichier.html">là</a>', encoding="utf-8")
        _v, casses, _e, _t = parcourir(racine, tout=True)
        return not casses, "cassés = %s" % [a for _p, a in casses]
    finally:
        shutil.rmtree(racine)


def cas_distant():
    """Une adresse distante n'est pas de son ressort, et il ne la compte pas."""
    return (not locale("https://onshape.com") and not locale("mailto:x@y.fr")
            and not locale("//cdn.exemple/x.js")), "trois formes distantes"


def cas_taire_ne_recolle_pas():
    """Deux morceaux séparés par un commentaire ne doivent pas se retrouver collés."""
    t, n = taire('<a href="a.html"><!-- x -->b.html</a>', ".html")
    return (n == 1 and adresses(t, ".html") == ["a.html"]), "adresses = %s" % adresses(t, ".html")


CAS = [
    ("la barre recopiée d'un dossier plus haut : trois liens morts", cas_nav_fausse),
    ("la même barre corrigée : plus rien", cas_nav_juste),
    ("une photo proposée en commentaire n'est pas un lien", cas_commentaire),
    ("une adresse de gabarit n'est pas un chemin", cas_gabarit),
    ("une adresse construite dans un <script> n'est pas suivie", cas_script),
    ("Markdown : le texte compte, le bloc de code non", cas_markdown),
    ("un lien d'ancre seul ne désigne aucun fichier", cas_ancre_seule),
    ("une ancre sur un fichier : on vérifie le fichier", cas_ancre_sur_fichier),
    ("un espace encodé %20 se résout comme un espace", cas_espace_encode),
    ("les adresses distantes ne sont pas comptées", cas_distant),
    ("taire une zone ne recolle pas ses bords", cas_taire_ne_recolle_pas),
]


def main():
    echecs = []
    for nom, f in CAS:
        ok, detail = f()
        if not ok:
            echecs.append("%s — %s" % (nom, detail))
    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (len(CAS) - len(echecs), len(CAS)))
        return 1
    print("✅ %d contrôles — l'erreur réelle est vue, et les cinq fausses alertes de la "
          "première version ne reviennent pas" % len(CAS))
    print("\n%d / %d" % (len(CAS), len(CAS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
