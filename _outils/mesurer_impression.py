# -*- coding: utf-8 -*-
"""mesurer_impression.py — imprime une page comme le fait l'élève, et mesure ce que le papier gaspille.

    python3 _outils/mesurer_impression.py page.html [autre.html …] [--pdf DOSSIER] [--fond] [--police NOM]

Pour chaque page : le nombre de feuilles A4, le blanc laissé en bas de chaque page (sauf la dernière), et les
TITRES RESTÉS SEULS en bas de page, leur contenu parti à la page suivante.

D'où vient cet outil
--------------------
Le 29/10/2026, Pascal imprime la synthèse élève de 5e_C1.1 (Chengdu) « directement à partir du site », en PDF :
« Esthétiquement, c'est parfait. Pédagogiquement aussi […] Ajuster de façon à ce qu'il n'y ait pas de blancs et que
l'on puisse imprimer moins de pages. » Son PDF faisait quatre pages, deux d'entre elles finissant par un titre
seul suivi d'un quart de page vide. Rejoué ici à l'identique : 4 pages, mêmes deux titres, 24 % de blanc. La version
réécrite le matin même (n°316) en faisait six, dont une première page à 41 % de blanc.

Comment il mesure
-----------------
- L'impression : Chromium, A4, marges de 10 mm (celles du dialogue d'impression par défaut), SANS les arrière-plans
  (la case « Graphiques d'arrière-plan » est décochée par défaut chez l'élève) ; `--fond` les ajoute.
- La police : le conteneur imprime en Inter, Pascal en Segoe UI (Windows). `--police 'Liberation Sans'` impose une
  autre police au corps de la page (Liberation Sans a les largeurs d'Arial) : une page qui tient en deux feuilles
  dans les deux polices tient chez l'élève.
- Le blanc : chaque page est tramée à 40 ppp ; la dernière rangée qui porte plus de 4 % de pixels non blancs marque
  le bas du contenu. Les filets verticaux d'un cadre qui continue sur la page suivante ne comptent donc pas comme
  du contenu — c'est exactement ce qu'on voit sur le papier : un cadre vide.
- Le titre seul : la dernière ligne de texte de la page est comparée aux titres h1–h4 de la page HTML.

Ce qu'il ne fait PAS : il ne refuse rien (sortie 0). C'est la MESURE du pilote ; la règle et son contrôle viendront
après la mesure de tout le dépôt, comme pour les n°300 et n°302.
"""
import argparse
import logging
import os
import re
import subprocess
import sys
import tempfile

logging.getLogger("pdfminer").setLevel(logging.ERROR)

SEUIL_REMPLI = 0.04   # part de pixels non blancs pour qu'une rangée compte comme contenu
CLAIR = 235           # niveau de gris au-dessus duquel un pixel est « blanc »


def imprimer(page_html, pdf, fond, police=None):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith(("file:", "data:", "blob:")) else r.abort())
        pg.goto("file://" + os.path.abspath(page_html))
        if police:
            pg.add_style_tag(content="body{font-family:'%s',sans-serif!important}" % police.replace("'", ""))
        pg.wait_for_timeout(400)
        titres = pg.evaluate("""() => [...document.querySelectorAll('h1,h2,h3,h4')]
            .map(h => h.innerText.replace(/\\s+/g, ' ').trim()).filter(Boolean)""")
        pg.pdf(path=pdf, format="A4", print_background=fond,
               margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"})
        b.close()
    return titres


def norme(t):
    return re.sub(r"\W+", "", t.lower())


def mesurer(pdf, titres):
    import pdfplumber
    from PIL import Image
    nt = [norme(t) for t in titres]
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-r", "40", "-png", pdf, os.path.join(tmp, "p")], check=True)
        images = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
        pages = []
        with pdfplumber.open(pdf) as doc:
            for i, page in enumerate(doc.pages):
                lignes = {}
                for w in page.extract_words(keep_blank_chars=True, use_text_flow=True):
                    lignes.setdefault(round(w["bottom"]), []).append(w)
                derniere = ""
                if lignes:
                    derniere = " ".join(w["text"] for w in sorted(lignes[max(lignes)], key=lambda w: w["x0"]))
                d = norme(derniere)
                seul = bool(d) and any(d == t or (len(d) > 8 and t.startswith(d)) for t in nt)
                im = Image.open(os.path.join(tmp, images[i])).convert("L")
                larg, haut = im.size
                px = im.load()
                bas = 0
                for y in range(haut):
                    if sum(1 for x in range(larg) if px[x, y] < CLAIR) > SEUIL_REMPLI * larg:
                        bas = y
                pages.append({"rempli": bas / haut, "titre_seul": derniere if seul else ""})
    return pages


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--pdf", help="dossier où garder les PDF produits")
    ap.add_argument("--fond", action="store_true", help="imprimer aussi les arrière-plans")
    ap.add_argument("--police", help="police imposée au corps de la page (ex. 'Liberation Sans')")
    a = ap.parse_args()
    for page_html in a.pages:
        dossier = a.pdf or tempfile.mkdtemp()
        os.makedirs(dossier, exist_ok=True)
        pdf = os.path.join(dossier, os.path.splitext(os.path.basename(page_html))[0] + ".pdf")
        pages = mesurer(pdf, imprimer(page_html, pdf, a.fond, a.police))
        n = len(pages)
        blancs = [1 - p["rempli"] for p in pages[:-1]]
        seuls = [p["titre_seul"] for p in pages if p["titre_seul"]]
        print(f"{page_html}" + (f"  [police : {a.police}]" if a.police else "") + f"\n  {n} page(s) · plus grand blanc {max(blancs, default=0):.0%} · "
              f"{len(seuls)} titre(s) seul(s) en bas de page")
        for k, p in enumerate(pages, 1):
            ligne = f"    p{k} : remplie à {p['rempli']:.0%}" + ("" if k < n else " (dernière)")
            if p["titre_seul"]:
                ligne += f" · ⚠ titre seul en bas : « {p['titre_seul'][:70]} »"
            print(ligne)
        if a.pdf:
            print(f"  PDF : {pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
