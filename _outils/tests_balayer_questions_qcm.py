# -*- coding: utf-8 -*-
"""tests_balayer_questions_qcm.py — le balayage des questions se prouve par ses refus.

Ce banc joue `balayer_questions_qcm.mjs` en sous-processus (n°299, second corollaire) sur des copies d'un vrai QCM du
dépôt, dont une seule chose est changée à chaque fois :
  1. la copie telle quelle (ses figures ôtées, pour qu'elle se lise hors de son dossier) ................. sortie 0 ;
  2. une proposition plus large que l'écran ........................................ sortie 1, « B1 débordement » ;
  3. un pourquoi plus large que l'écran : invisible avant de répondre ............... sortie 0 sans `--apres` ;
  4. le même, avec `--apres` ...................................... sortie 1, « après une réponse fausse » ;
  5. une figure dont le fichier manque ...................................... sortie 1, « B2 image non décodée » ;
  6. une figure présente, décrite en cinq lettres ................................. sortie 1, « B3 alt » ;
  7. un dossier sans QCM ..................................................... sortie 2 (en panne, pas vert).
Ce qui dépasse est un bloc de 700 px de large, pas un mot sans espace : le banc reste vrai le jour où le gabarit
saura couper les mots longs.
Non joué : B4 (un document affiché à moins de 300 px). Le gabarit étire les figures sur toute la largeur ; B4 garde
contre un style qui les rapetisserait.

Usage : python3 _outils/tests_balayer_questions_qcm.py
Sortie : 0 si tout passe · 1 sinon · 2 si le banc ne peut pas tourner (Node ou Playwright absent, QCM de base illisible).
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(ICI)
OUTIL = os.path.join(ICI, "balayer_questions_qcm.mjs")
BASE = os.path.join(DEPOT, "theme-1-objets-systemes-usages-interactions", "C1-decrire-les-liens-entre-usages-et-evolutions",
                    "3e", "3e_C1.5", "qcm_numerique_societe.html")
LARGE = '<span style="display:inline-block;width:700px">un bloc de 700 px</span>'
SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 100"><rect width="350" height="100" fill="#0d2347"/></svg>\n'


def fin_de_chaine(s, debut):
    """Le rang du guillemet qui ferme la chaîne ouverte en `debut`."""
    k = debut + 1
    while s[k] != '"':
        k += 2 if s[k] == "\\" else 1
    return k


def muter(src, option=None, pourquoi=None, img=None):
    """La première question de la banque, changée d'une seule façon."""
    i = src.index("const QUESTIONS")
    if img:
        j = src.index("o:[", i)
        src = src[:j] + "img:{src:%s,alt:%s},\n " % (json.dumps(img[0]), json.dumps(img[1], ensure_ascii=False)) + src[j:]
    if option:
        j = src.index('"', src.index("o:[", i))
        src = src[:j] + json.dumps(option, ensure_ascii=False) + src[fin_de_chaine(src, j) + 1:]
    if pourquoi:
        j = src.index("d:[", i) + 3
        morceaux = []
        while src[j] != "]":
            if src[j] == '"':
                f = fin_de_chaine(src, j)
                morceaux.append('""' if f == j + 1 else json.dumps(pourquoi, ensure_ascii=False))   # la bonne réponse garde son « "" »
                j = f + 1
            else:
                j += 1
        src = src[:src.index("d:[", i)] + "d:[" + ",".join(morceaux) + src[j:]
    return src


def main():
    try:
        base = open(BASE, encoding="utf-8").read()
        base = re.sub(r'\n?\s*img:\{src:"[^"]*",\s*alt:"(?:[^"\\]|\\.)*"\},?', "", base)
        assert "const QUESTIONS" in base and 'id="btnValider"' in base
    except (OSError, AssertionError):
        print("❌ EN PANNE : le QCM de base est introuvable ou n'est plus au gabarit maison (%s)" % os.path.relpath(BASE, DEPOT))
        return 2

    echecs, controles = [], 0
    with tempfile.TemporaryDirectory() as tmp:
        b = pathlib.Path(tmp)

        def cas(titre, attendue, contenu, apres=False, contient="", fichiers=()):
            nonlocal controles
            controles += 1
            d = b / ("cas%d" % controles)
            d.mkdir()
            if contenu is not None:
                (d / "qcm_banc.html").write_text(contenu, encoding="utf-8")
            for nom, texte in fichiers:
                (d / nom).parent.mkdir(parents=True, exist_ok=True)
                (d / nom).write_text(texte, encoding="utf-8")
            r = subprocess.run(["node", OUTIL, "--muet"] + (["--apres"] if apres else []) + [str(d)],
                               capture_output=True, text=True, cwd=DEPOT)
            texte = r.stdout + r.stderr
            if "le paquet `playwright` manque" in texte or "Cannot find package" in texte:
                return "panne"
            if r.returncode != attendue:
                echecs.append("%s : sortie %d, attendue %d\n     %s" % (titre, r.returncode, attendue, texte.strip()[-400:]))
            elif contient and contient not in texte:
                echecs.append("%s : message sans « %s »\n     %s" % (titre, contient, texte.strip()[-400:]))
            return "joué"

        try:
            if cas("la copie telle quelle", 0, base, contient="0 QCM en écart") == "panne":
                print("❌ EN PANNE : Playwright manque pour Node — banc non exécuté (n°299)")
                return 2
        except FileNotFoundError:
            print("❌ EN PANNE : Node manque — banc non exécuté (n°299)")
            return 2
        cas("une proposition plus large que l'écran", 1, muter(base, option=LARGE), contient="Q1 · B1 débordement")
        cas("un pourquoi plus large que l'écran, sans --apres : invisible avant de répondre", 0, muter(base, pourquoi=LARGE))
        cas("le même, avec --apres", 1, muter(base, pourquoi=LARGE), apres=True, contient="après une réponse fausse")
        cas("une figure dont le fichier manque", 1,
            muter(base, img=("Images/absente.svg", "Une figure décrite en plus de vingt caractères.")), contient="B2 image non décodée")
        cas("une figure présente, décrite en cinq lettres", 1, muter(base, img=("Images/presente.svg", "Image")),
            contient="B3 alt absent ou trop court", fichiers=[("Images/presente.svg", SVG)])
        cas("la même figure, décrite", 0, muter(base, img=("Images/presente.svg", "Un rectangle bleu, large de 350 unités.")),
            contient="1 illustrées", fichiers=[("Images/presente.svg", SVG)])
        cas("un dossier sans QCM : en panne, pas vert", 2, None, contient="aucun QCM lu")

    print("%d / %d tests passés" % (controles - len(echecs), controles))
    for e in echecs:
        print("  ✘ " + e)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
