# -*- coding: utf-8 -*-
"""tests_controle_atteignabilite.py — refuser l'inatteignable, sans crier au loup.

Ce banc joue sur des arborescences fabriquées ce que la marche depuis l'index
doit voir et ne pas voir : une page liée en chaîne est atteinte quelle que soit
sa profondeur ; une page qu'aucun lien ne désigne est refusée ; une page nommée
dans `TOLEREES` passe ; et une tolérée redevenue atteignable est signalée pour
que sa ligne sorte de la liste — sinon la liste ne rétrécit jamais.

Il garde aussi les deux formes de lien que ce dépôt emploie vraiment : `href`
pour les pages, `data` pour les `<object>`, et les chemins **accentués**
(`Synthèses/…`), que l'URL encode et que la marche doit décoder.

Usage : python3 _outils/tests_controle_atteignabilite.py
Sortie : 0 si tout passe, 1 sinon.
"""

import contextlib
import io
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_atteignabilite as CA  # noqa: E402


def page(*liens):
    return ("<html><body>"
            + "".join('<a href="%s">x</a>' % l for l in liens)
            + "</body></html>\n")


def ecrire(racine, chemin, contenu):
    p = pathlib.Path(racine) / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contenu, encoding="utf-8")
    return p


def jouer(racine, tolerees=None):
    anciens = (CA.DEPOT, CA.TOLEREES)
    CA.DEPOT = str(racine)
    CA.TOLEREES = tolerees if tolerees is not None else {}
    sortie = io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie):
            code = CA.main()
    finally:
        CA.DEPOT, CA.TOLEREES = anciens
    return code, sortie.getvalue()


def main():
    echecs, controles = [], 0

    def cas(titre, racine, doit_refuser, attendu="", tolerees=None):
        nonlocal controles
        controles += 1
        code, texte = jouer(racine, tolerees)
        if doit_refuser and code == 0:
            echecs.append("%s : accepté, alors qu'il fallait refuser" % titre)
        elif not doit_refuser and code != 0:
            echecs.append("%s : refusé\n     %s" % (titre, texte.strip().replace("\n", "\n     ")))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s"
                          % (titre, attendu, texte.strip().replace("\n", "\n     ")))

    with tempfile.TemporaryDirectory() as tmp:
        b = pathlib.Path(tmp)

        # ── 1. une chaîne de liens, aussi longue soit-elle, est atteinte ─────
        r1 = b / "c1"
        ecrire(r1, "index.html", page("a/sequence.html"))
        ecrire(r1, "a/sequence.html", page("qcm.html"))
        ecrire(r1, "a/qcm.html", page("../b/lexique.html"))
        ecrire(r1, "b/lexique.html", page())
        cas("une chaîne de quatre pages depuis l'index", r1, False)

        # ── 2. une page que rien ne désigne est refusée ──────────────────────
        r2 = b / "c2"
        ecrire(r2, "index.html", page("a/sequence.html"))
        ecrire(r2, "a/sequence.html", page())
        ecrire(r2, "a/Synthèses/synthese_eleve.html", page())
        cas("une synthèse qu'aucun lien ne désigne", r2, True, "synthese_eleve.html")

        # ── 3. la même, nommée dans TOLEREES avec sa raison ─────────────────
        cas("la même, déclarée dans TOLEREES", r2, False, "tolérée(s), chacune avec sa raison",
            tolerees={"a/Synthèses/synthese_eleve.html": "raison écrite, PR sœur annoncée"})

        # ── 4. LE CHEMIN ACCENTUÉ, encodé dans l'URL ────────────────────────
        # C'est la forme réelle du dépôt : `Synthèses/…`, que le générateur
        # d'index écrit encodé. Sans décodage, la marche croirait la page
        # inatteignable et le contrôle crierait au loup sur 72 fichiers.
        r4 = b / "c4"
        ecrire(r4, "index.html", page("a/Synth%C3%A8ses/synthese_eleve.html"))
        ecrire(r4, "a/Synthèses/synthese_eleve.html", page())
        cas("un lien vers un dossier accentué, encodé dans l'URL", r4, False)

        # ── 5. un lien porté par `data=` (les <object> du dépôt) ────────────
        r5 = b / "c5"
        ecrire(r5, "index.html", '<html><object data="a/fiche.html"></object></html>')
        ecrire(r5, "a/fiche.html", page())
        cas("un lien porté par data= et non par href=", r5, False)

        # ── 6. une tolérée redevenue atteignable est SIGNALÉE ───────────────
        # Sans ce signal, la liste des tolérées ne rétrécirait jamais : on
        # continuerait d'excuser des pages qui n'en ont plus besoin.
        controles += 1
        _c, texte = jouer(r1, {"b/lexique.html": "raison périmée"})
        if "peut sortir de TOLEREES" not in texte:
            echecs.append("une tolérée redevenue atteignable n'est pas signalée\n     "
                          + texte.strip().replace("\n", "\n     "))

        # ── 7. l'archive et _outils ne sont pas du contenu à atteindre ──────
        r7 = b / "c7"
        ecrire(r7, "index.html", page("a/sequence.html"))
        ecrire(r7, "a/sequence.html", page())
        ecrire(r7, "_archive-anciennes-versions/vieux.html", page())
        ecrire(r7, "_outils/gabarit.html", page())
        cas("une page d'archive ou d'outillage n'a pas à être atteignable", r7, False)

        # ── 8. un lien distant ne compte pas comme un chemin interne ────────
        r8 = b / "c8"
        ecrire(r8, "index.html", page("https://exemple.fr/a.html"))
        ecrire(r8, "a.html", page())
        cas("un lien http:// ne rend pas une page locale atteignable", r8, True, "a.html")

    # ── 9. le dépôt réel doit passer ────────────────────────────────────────
    controles += 1
    code, texte = jouer(CA.DEPOT, CA.TOLEREES)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     "
                      + texte.strip().replace("\n", "\n     "))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — l'inatteignable est refusé, la tolérée déclarée passe, et celle "
          "qui n'a plus besoin de l'être est signalée" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
