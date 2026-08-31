# -*- coding: utf-8 -*-
"""tests_controle_medias.py — refuser l'image sans provenance, compter le reste.

Ce banc joue sur des arborescences fabriquées la ligne que ce contrôle trace :
une image dont **rien** ne dit d'où elle vient est refusée ; une image que son
`SOURCES_MEDIAS.md` ne nomme pas encore, ou qu'aucune page n'affiche, est
comptée et nommée sans être refusée.

Il garde aussi le piège qui s'est refermé le jour où le contrôle a été écrit :
documenter une image la faisait **disparaître** du relevé des orphelines, parce
que le `SOURCES_MEDIAS.md` la nomme. Un document qui décrit n'emploie pas.

Usage : python3 _outils/tests_controle_medias.py
Sortie : 0 si tout passe, 1 sinon.
"""

import contextlib
import io
import json
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_medias as CM  # noqa: E402

SVG = '<svg xmlns="http://www.w3.org/2000/svg"><title>t</title></svg>\n'


def lot(racine, images=(), sources=None, page_cite=(), manifeste=None, fiche_cite=()):
    """Un lot : des images, un éventuel SOURCES_MEDIAS.md, une page et une fiche
    qui en citent certaines, un éventuel manifeste."""
    r = pathlib.Path(racine)
    (r / "Images").mkdir(parents=True, exist_ok=True)
    for i in images:
        (r / "Images" / i).write_text(SVG, encoding="utf-8")
    if sources is not None:
        (r / "SOURCES_MEDIAS.md").write_text(sources, encoding="utf-8")
    (r / "sequence_essai.html").write_text(
        "<html><body>" + "".join('<img src="Images/%s" alt="a">' % i for i in page_cite)
        + "</body></html>\n", encoding="utf-8")
    if fiche_cite:
        (r / "fiche_pedagogique_essai.md").write_text(
            "# Fiche\n\n" + "\n".join("Voir `Images/%s`." % i for i in fiche_cite),
            encoding="utf-8")
    if manifeste is not None:
        (r / "manifest_essai.json").write_text(json.dumps(manifeste, ensure_ascii=False),
                                               encoding="utf-8")
    return r


def tableau(*noms):
    """Un SOURCES_MEDIAS.md qui nomme ces fichiers."""
    return ("# Sources\n\n| Fichier | Licence |\n|---|---|\n"
            + "".join("| `Images/%s` | CC0 |\n" % n for n in noms))


def jouer(racine):
    ancien = CM.DEPOT
    CM.DEPOT = str(racine)
    sortie = io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie):
            code = CM.main()
    finally:
        CM.DEPOT = ancien
    return code, sortie.getvalue()


def main():
    echecs, controles = [], 0

    def cas(titre, racine, doit_refuser, attendu=""):
        nonlocal controles
        controles += 1
        code, texte = jouer(racine)
        if doit_refuser and code == 0:
            echecs.append("%s : accepté, alors qu'il fallait refuser" % titre)
        elif not doit_refuser and code != 0:
            echecs.append("%s : refusé\n     %s" % (titre, texte.strip().replace("\n", "\n     ")))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s"
                          % (titre, attendu, texte.strip().replace("\n", "\n     ")))

    def dit(titre, racine, attendu, present=True):
        nonlocal controles
        controles += 1
        _c, texte = jouer(racine)
        if (attendu in texte) != present:
            echecs.append("%s : « %s » %s dans le relevé\n     %s"
                          % (titre, attendu, "manque" if present else "ne devrait pas être",
                             texte.strip().replace("\n", "\n     ")))

    with tempfile.TemporaryDirectory() as tmp:
        b = pathlib.Path(tmp)

        # ── 1. un lot documenté et employé passe ────────────────────────────
        cas("un lot dont chaque image est documentée et affichée",
            lot(b / "c1", images=["a.svg"], sources=tableau("a.svg"), page_cite=["a.svg"]),
            False)

        # ── 2. AUCUN SOURCES_MEDIAS.md : refus ──────────────────────────────
        cas("un dossier d'images sans aucun SOURCES_MEDIAS.md",
            lot(b / "c2", images=["a.svg"], page_cite=["a.svg"]),
            True, "AUCUN SOURCES_MEDIAS.md")

        # ── 3. une image promise par un manifeste et absente : refus ────────
        cas("un manifeste qui promet une image absente du disque",
            lot(b / "c3", images=["a.svg"], sources=tableau("a.svg"), page_cite=["a.svg"],
                manifeste={"fichiers": {"images": ["Images/a.svg", "Images/fantome.svg"]}}),
            True, "fantome.svg")

        # ── 4. une image non nommée par un SOURCES_MEDIAS.md EXISTANT ───────
        # C'est une dette : elle est comptée et nommée, elle n'est pas refusée.
        r4 = lot(b / "c4", images=["a.svg", "b.svg"], sources=tableau("a.svg"),
                 page_cite=["a.svg", "b.svg"])
        cas("une image qu'un SOURCES_MEDIAS.md existant ne nomme pas encore", r4, False)
        dit("cette dette est nommée dans le relevé", r4, "b.svg")

        # ── 5. une image qu'aucune page n'affiche : comptée, pas refusée ────
        r5 = lot(b / "c5", images=["a.svg", "orpheline.svg"],
                 sources=tableau("a.svg", "orpheline.svg"), page_cite=["a.svg"])
        cas("une image qu'aucune page n'affiche", r5, False)
        dit("l'orpheline est nommée dans le relevé", r5, "orpheline.svg")

        # ── 6. LE PIÈGE : documenter ne doit pas rendre invisible ───────────
        # Le SOURCES_MEDIAS.md du cas 5 NOMME `orpheline.svg`. Si le contrôle
        # comptait ce document comme un emploi, l'image sortirait du relevé au
        # moment exact où on s'en occupe.
        dit("une orpheline documentée reste comptée comme orpheline", r5,
            "qu'aucune page n'affiche")

        # ── 7. une image citée par la seule FICHE n'est pas orpheline ───────
        # Ce qui parle d'une ressource vit rarement dans son dossier (n°263) :
        # une image présentée au professeur dans la fiche est employée.
        r7 = lot(b / "c7", images=["a.svg", "f.svg"], sources=tableau("a.svg", "f.svg"),
                 page_cite=["a.svg"], fiche_cite=["f.svg"])
        cas("une image citée par la seule fiche pédagogique", r7, False)
        dit("elle n'est pas comptée orpheline", r7, "f.svg", present=False)

        # ── 8. une orpheline NOMMÉE par le manifeste est une décision ───────
        # `5e_C1.2` range deux SVG sous `herite_conserve` : gardés exprès.
        r8 = lot(b / "c8", images=["a.svg", "gardee.svg"],
                 sources=tableau("a.svg", "gardee.svg"), page_cite=["a.svg"],
                 manifeste={"fichiers": {"images": ["Images/a.svg"],
                                         "herite_conserve": ["Images/gardee.svg"]}})
        cas("une orpheline que le manifeste nomme quand même", r8, False)
        dit("elle est rangée parmi les gardées exprès", r8, "gardées exprès")
        dit("et non parmi les oubliées", r8, "qu'aucune page n'affiche", present=False)

        # ── 9. un dossier Images vide n'est pas un lot à médias ─────────────
        r9 = b / "c9"
        (r9 / "Images").mkdir(parents=True)
        (r9 / "sequence_essai.html").write_text("<html></html>", encoding="utf-8")
        cas("un dossier Images vide, sans SOURCES_MEDIAS.md, ne déclenche rien", r9, False)

        # ── 10. toutes les extensions du dépôt sont reconnues (n°269) ───────
        r10 = b / "c10"
        (r10 / "Images").mkdir(parents=True)
        for ext in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"):
            (r10 / "Images" / ("i" + ext)).write_bytes(b"\x00")
        (r10 / "sequence_essai.html").write_text("<html></html>", encoding="utf-8")
        cas("un dossier de rasters sans SOURCES_MEDIAS.md est refusé, quelle que soit "
            "l'extension", r10, True, "6 média(s)")

    # ── 11. le dépôt réel doit passer ───────────────────────────────────────
    controles += 1
    code, texte = jouer(CM.DEPOT)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     "
                      + texte.strip().replace("\n", "\n     "))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — l'image sans provenance est refusée, la dette et l'orpheline "
          "sont comptées, et documenter ne rend rien invisible" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
