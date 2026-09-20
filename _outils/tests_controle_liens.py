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

S'y ajoute l'angle mort que la première version déclarait sans le combler : les
**ancres**. `page.html#partie-2` était réputé juste tant que `page.html`
existait. Six cas le couvrent maintenant, dans les deux sens — l'ancre morte
qu'il faut voir, et les quatre formes sur lesquelles il ne doit pas crier
(`#top`, `name="…"`, une cible Markdown, une ancre dans la page même).

Les cas travaillent sur une arborescence temporaire, pas sur le dépôt : un test
qui dépend de l'état du dépôt cesse de tester le jour où le dépôt change.

Usage : python3 _outils/tests_controle_liens.py
Sortie : 0 si tout passe, 1 sinon.
"""
import contextlib
import io
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_liens  # noqa: E402
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
        casses = parcourir(racine, tout=True)["casses"]
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
        casses = parcourir(racine, tout=True)["casses"]
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
        r = parcourir(racine, tout=True)
        casses, tues = r["casses"], r["tues"]
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
        casses = parcourir(racine, tout=True)["casses"]
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
        casses = parcourir(racine, tout=True)["casses"]
        adr = [a for _p, a in casses]
        return adr == ["sequence_absente.html"], "cassés = %s" % adr
    finally:
        shutil.rmtree(racine)


def cas_ancre_seule():
    """Un lien `#partie-2` reste dans la page : il n'y a pas de fichier à trouver."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "p.html").write_text('<a href="#partie-2">bas de page</a>', encoding="utf-8")
        r = parcourir(racine, tout=True)
        v, casses = r["verifies"], r["casses"]
        return (v == 0 and not casses), "vérifiés = %d, cassés = %d" % (v, len(casses))
    finally:
        shutil.rmtree(racine)


def cas_ancre_sur_fichier():
    """`page.html#partie-2` : le fichier existe, la section non — c'est un défaut.

    C'est l'angle mort de la première version : elle s'arrêtait au fichier. Un
    lien d'ancre morte ne mène pas ailleurs, il mène en haut de la bonne page,
    et le lecteur croit avoir mal cliqué.
    """
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "page.html").write_text("<h2 id='autre'>x</h2>", encoding="utf-8")
        (racine / "p.html").write_text('<a href="page.html#partie-2">là</a>', encoding="utf-8")
        r = parcourir(racine, tout=True)
        return (not r["casses"] and [a for _p, a in r["ancres_mortes"]]
                == ["page.html#partie-2"]), "ancres mortes = %s" % r["ancres_mortes"]
    finally:
        shutil.rmtree(racine)


def cas_ancre_juste():
    """La même ancre, présente dans la page visée : rien à signaler."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "page.html").write_text('<h2 id="partie-2">x</h2>', encoding="utf-8")
        (racine / "p.html").write_text('<a href="page.html#partie-2">là</a>', encoding="utf-8")
        r = parcourir(racine, tout=True)
        return (not r["ancres_mortes"] and r["ancres_verifiees"] == 1,
                "vérifiées = %d, mortes = %s" % (r["ancres_verifiees"], r["ancres_mortes"]))
    finally:
        shutil.rmtree(racine)


def cas_ancre_dans_la_page():
    """Une ancre sans chemin vise la page elle-même — et se vérifie aussi."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "p.html").write_text(
            '<a href="#bas">descendre</a><a href="#absent">nulle part</a>'
            '<h2 id="bas">bas</h2>', encoding="utf-8")
        r = parcourir(racine, tout=True)
        return ([a for _p, a in r["ancres_mortes"]] == ["#absent"]
                and r["verifies"] == 0), "mortes = %s, liens = %d" % (
                    r["ancres_mortes"], r["verifies"])
    finally:
        shutil.rmtree(racine)


def cas_ancre_top():
    """`#top` remonte en haut de page : le navigateur n'a besoin d'aucun id."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "p.html").write_text('<a href="#top">remonter</a>', encoding="utf-8")
        r = parcourir(racine, tout=True)
        return not r["ancres_mortes"], "mortes = %s" % r["ancres_mortes"]
    finally:
        shutil.rmtree(racine)


def cas_ancre_vers_markdown():
    """Une ancre vers un `.md` n'est pas vérifiable : l'identifiant naît au rendu."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "R.md").write_text("## Une partie\n", encoding="utf-8")
        (racine / "p.html").write_text('<a href="R.md#une-partie">là</a>', encoding="utf-8")
        r = parcourir(racine, tout=True)
        return (not r["ancres_mortes"] and r["ancres_non_verifiables"] == 1,
                "mortes = %s, non vérifiables = %d" % (
                    r["ancres_mortes"], r["ancres_non_verifiables"]))
    finally:
        shutil.rmtree(racine)


def cas_ancre_name():
    """L'ancienne forme `name="…"` compte autant qu'un `id`."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "page.html").write_text('<a name="vieille">x</a>', encoding="utf-8")
        (racine / "p.html").write_text('<a href="page.html#vieille">là</a>', encoding="utf-8")
        r = parcourir(racine, tout=True)
        return not r["ancres_mortes"], "mortes = %s" % r["ancres_mortes"]
    finally:
        shutil.rmtree(racine)


def cas_espace_encode():
    """Un nom de fichier avec un espace s'écrit `%20` dans une adresse."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        (racine / "mon fichier.html").write_text("x", encoding="utf-8")
        (racine / "p.html").write_text('<a href="mon%20fichier.html">là</a>', encoding="utf-8")
        casses = parcourir(racine, tout=True)["casses"]
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


def panne_sur_racine_vide(module, attribut, prepare, appel):
    """Règle d'or n°299 : sur une racine où il n'y a RIEN à ouvrir, un contrôle
    doit sortir à 2 en le disant sur stderr — et surtout pas à 0 en se déclarant
    content d'un dépôt qu'il n'a pas lu.

    Rend (ça_va, détail), la forme attendue par la liste CAS.
    """
    racine = pathlib.Path(tempfile.mkdtemp())
    ancien = getattr(module, attribut)
    try:
        prepare(racine)
        setattr(module, attribut, str(racine) if isinstance(ancien, str) else racine)
        sortie, erreur = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
            code = appel()
        texte = sortie.getvalue() + erreur.getvalue()
    finally:
        setattr(module, attribut, ancien)
        shutil.rmtree(racine, ignore_errors=True)
    if code != 2:
        return False, ("sortie %d au lieu de 2 — le contrôle se déclare content "
                       "sans avoir rien ouvert" % code)
    if "EN PANNE" not in texte:
        return False, "la panne n'est pas annoncée : %s" % texte.strip()[:200]
    return True, ""


def cas_racine_sans_page():
    """Une racine sans page .html ni .md : « aucun lien mort » serait un mensonge."""
    return panne_sur_racine_vide(
        controle_liens, "DEPOT",
        lambda r: (r / "notes.txt").write_text("rien à suivre ici", encoding="utf-8"),
        lambda: controle_liens.main(tout=True))


def cas_ligne_de_commande():
    """Le VRAI point d'entrée, en sous-processus (règle d'or n°299)."""
    ennuis = reproches_de_la_ligne_de_commande("controle_liens.py")
    return (not ennuis), (" ; ".join(ennuis) if ennuis else "")


CAS = [
    ("la barre recopiée d'un dossier plus haut : trois liens morts", cas_nav_fausse),
    ("la même barre corrigée : plus rien", cas_nav_juste),
    ("une photo proposée en commentaire n'est pas un lien", cas_commentaire),
    ("une adresse de gabarit n'est pas un chemin", cas_gabarit),
    ("une adresse construite dans un <script> n'est pas suivie", cas_script),
    ("Markdown : le texte compte, le bloc de code non", cas_markdown),
    ("un lien d'ancre seul ne désigne aucun fichier", cas_ancre_seule),
    ("une ancre morte sur un fichier existant est un défaut", cas_ancre_sur_fichier),
    ("la même ancre, présente : rien à signaler", cas_ancre_juste),
    ("une ancre sans chemin vise la page elle-même", cas_ancre_dans_la_page),
    ("#top est toujours valide, sans identifiant", cas_ancre_top),
    ("une ancre vers un .md n'est pas vérifiable, et c'est compté", cas_ancre_vers_markdown),
    ("l'ancienne forme name= compte autant qu'un id", cas_ancre_name),
    ("un espace encodé %20 se résout comme un espace", cas_espace_encode),
    ("les adresses distantes ne sont pas comptées", cas_distant),
    ("taire une zone ne recolle pas ses bords", cas_taire_ne_recolle_pas),
    ("une racine sans page est une panne, pas un succès", cas_racine_sans_page),
    ("le contrôle travaille quand on le lance en ligne de commande", cas_ligne_de_commande),
]


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
