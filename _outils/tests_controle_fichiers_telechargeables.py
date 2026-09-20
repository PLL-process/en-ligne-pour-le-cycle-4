# -*- coding: utf-8 -*-
"""tests_controle_fichiers_telechargeables.py — le banc de la règle n°289.

Il rejoue, sur des lots fabriqués, ce que le contrôle doit refuser et ce qu'il ne
doit PAS refuser — chaque « ne doit pas » vient d'un cas réel du dépôt :

  · `truc.csv`, `finalV2 (copie).csv` : les noms d'un dossier en désordre que
    `5e_C1.1` donne en EXEMPLE — du récit, pas des fichiers ;
  · un nom dans un `alt`, un `href`, un `<script>` : pas une mention visible ;
  · une page HTML ou une image nommée : un lien ou un affichage, pas un
    téléchargement ;
  · un fichier promis (« fourni avec le TP ») et absent : `de_50.step` ;
  · un lien sans `download` : les trois pages de `3e_C9.2` ;
  · un lien dont la cible n'est pas le fichier nommé.

Usage : python3 _outils/tests_controle_fichiers_telechargeables.py
Sortie : 0 si tout passe, 1 sinon.
"""

import contextlib
import io
import os
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_fichiers_telechargeables as C  # noqa: E402


def page(corps):
    return ("<!doctype html><html><head><meta charset=\"utf-8\"><style>.x{color:red}</style>"
            "</head><body><nav><a href=\"../index.html\">Accueil</a></nav>%s"
            "<script>const f='fantome.csv';</script></body></html>\n" % corps)


def ecrire(racine, chemin, contenu=""):
    p = pathlib.Path(racine) / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contenu, encoding="utf-8")
    return p


def jouer(racine, tolerees=None):
    anciens = (C.DEPOT, C.TOLEREES)
    C.DEPOT = str(racine)
    C.TOLEREES = tolerees if tolerees is not None else {}
    sortie, erreur = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
            code = C.main()
    finally:
        C.DEPOT, C.TOLEREES = anciens
    return code, sortie.getvalue() + erreur.getvalue()


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
    echecs, controles = [], 0

    def cas(titre, fichiers, doit_refuser, attendu="", tolerees=None):
        """`fichiers` : {chemin: contenu} d'un lot jetable, jugé."""
        nonlocal controles
        controles += 1
        with tempfile.TemporaryDirectory() as tmp:
            for ch, contenu in fichiers.items():
                ecrire(tmp, ch, contenu)
            code, texte = jouer(tmp, tolerees)
        if doit_refuser and code == 0:
            echecs.append("%s : accepté, alors qu'il fallait refuser\n     %s"
                          % (titre, texte.strip().replace("\n", "\n     ")))
        elif not doit_refuser and code != 0:
            echecs.append("%s : refusé\n     %s" % (titre, texte.strip().replace("\n", "\n     ")))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s"
                          % (titre, attendu, texte.strip().replace("\n", "\n     ")))

    LIE = '<p>Ouvre <a href="releves.csv" download>📥 <code>releves.csv</code></a> dans un tableur.</p>'

    # ══ la forme juste ═══════════════════════════════════════════════════════
    cas("un CSV nommé, lié avec download, présent dans le lot",
        {"lot/sequence_x.html": page(LIE), "lot/releves.csv": "a;b\n"}, False,
        "chaque fichier nommé")
    cas("le fichier dans un sous-dossier du lot, lien relatif",
        {"lot/sequence_x.html": page('<p>(<a href="code/station.ino" download>station.ino</a>)</p>'),
         "lot/code/station.ino": "void setup(){}"}, False)
    cas("deux mentions, toutes deux liées",
        {"lot/tp_x.html": page(LIE + LIE), "lot/releves.csv": ""}, False)

    # ══ CE QU'IL DOIT REFUSER ════════════════════════════════════════════════
    cas("un CSV présent dans le lot et nommé sans lien",
        {"lot/sequence_x.html": page("<p>Ouvre <code>releves.csv</code> dans un tableur.</p>"),
         "lot/releves.csv": ""}, True, "n'a pas de lien")
    cas("deux mentions dont une seule est liée",
        {"lot/sequence_x.html": page(LIE + "<p>Puis reprends <code>releves.csv</code>.</p>"),
         "lot/releves.csv": ""}, True, "une mention au moins")
    cas("un lien sans download (les trois pages de 3e_C9.2)",
        {"lot/sequence_x.html": page('<p>(<a href="station.ino">station.ino</a>)</p>'),
         "lot/station.ino": ""}, True, "sans `download`")
    cas("un lien qui enveloppe le nom mais pointe ailleurs",
        {"lot/sequence_x.html": page('<p><a href="autre.csv" download>releves.csv</a></p>'),
         "lot/releves.csv": "", "lot/autre.csv": ""}, True, "pointe ailleurs")
    cas("un fichier PROMIS et absent (de_50.step)",
        {"lot/tp_x.html": page("<p>Sinon : ouvre le fichier <code>de_50.step</code> fourni avec le TP.</p>")},
        True, "est promis")
    cas("la même promesse, nommée dans TOLEREES avec sa raison",
        {"lot/tp_x.html": page("<p>ouvre le fichier <code>de_50.step</code> fourni avec le TP.</p>")},
        False, "tolérée", tolerees={"lot/tp_x.html": "raison écrite, et ce qui la débloquera"})

    # ══ CE QU'IL NE DOIT PAS REFUSER ═════════════════════════════════════════
    cas("les noms d'un dossier en désordre, donnés en exemple (5e_C1.1)",
        {"lot/sequence_x.html": page("<p>14 entrées, dont <code>truc.csv</code>, "
                                     "<code>finalV2 (copie).csv</code>, identique à "
                                     "<code>finalV2.csv</code>. Personne ne retrouve rien.</p>")},
        False, "du récit")
    cas("un nom dans un alt, un href, un title — pas une mention visible",
        {"lot/sequence_x.html": page('<img src="Images/s.svg" alt="le schéma issu de releves.csv">'
                                     '<a href="releves.csv" download title="releves.csv">le relevé</a>'),
         "lot/releves.csv": ""}, False)
    cas("un nom dans un <script> ou un <style> n'est pas lu",
        {"lot/sequence_x.html": page("<p>rien</p>"), "lot/fantome.csv": ""}, False)
    cas("une page HTML nommée est un lien, pas un fichier à prendre",
        {"lot/sequence_x.html": page("<p>Voir <code>qcm_x.html</code>.</p>"), "lot/qcm_x.html": ""},
        False)
    cas("une image nommée s'affiche, elle ne se télécharge pas",
        {"lot/sequence_x.html": page("<p>Production : <code>book-train.svg</code>.</p>"),
         "lot/book-train.svg": ""}, False)
    # Chacun de ces deux cas ajoute une séquence ordinaire : sans elle, la
    # racine ne faisait RIEN ouvrir au contrôle et le vert ne prouvait rien
    # (règle d'or n°299).
    cas("un QCM ou une synthèse ne sont pas jugés (seuls sequence/tp/atelier)",
        {"lot/qcm_x.html": page("<p>Ouvre <code>releves.csv</code>.</p>"), "lot/releves.csv": "",
         "lot/sequence_ok.html": page("<p>une séquence sans fichier nommé</p>")},
        False)
    cas("l'archive est écartée, et le reste est bien lu",
        {"_archive-anciennes-versions/sequence_x.html": page("<p>Ouvre <code>releves.csv</code>.</p>"),
         "_archive-anciennes-versions/releves.csv": "",
         "lot/sequence_ok.html": page("<p>une séquence sans fichier nommé</p>")}, False)

    # ══ une tolérée redevenue propre est signalée ════════════════════════════
    controles += 1
    with tempfile.TemporaryDirectory() as tmp:
        ecrire(tmp, "lot/sequence_x.html", page(LIE))
        ecrire(tmp, "lot/releves.csv", "")
        _c, texte = jouer(tmp, {"lot/sequence_x.html": "raison périmée"})
    if "peut sortir de TOLEREES" not in texte:
        echecs.append("une tolérée redevenue propre n'est pas signalée\n     " + texte.strip())

    # ══ le dépôt réel doit passer ════════════════════════════════════════════
    controles += 1
    code, texte = jouer(C.DEPOT, C.TOLEREES)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     " + texte.strip().replace("\n", "\n     "))

    # Règle d'or n°299 — une racine sans page à juger est une panne.
    controles += 1
    with tempfile.TemporaryDirectory() as tmp:
        ecrire(tmp, "notes.md", "# rien à juger")
        code, texte = jouer(tmp)
    if code != 2:
        echecs.append("une racine sans séquence : sortie %d au lieu de 2 — le contrôle annonce que chaque fichier se prend d'un clic sans avoir ouvert une page" % code)
    elif "EN PANNE" not in texte:
        echecs.append("une racine sans séquence : la panne n'est pas annoncée")

    # Le VRAI point d'entrée, en sous-processus (règle d'or n°299).
    controles += 1
    echecs.extend(reproches_de_la_ligne_de_commande('controle_fichiers_telechargeables.py'))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — un fichier nommé se prend d'un clic, et le récit n'est pas accusé"
          % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
