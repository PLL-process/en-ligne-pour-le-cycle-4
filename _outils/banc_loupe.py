# -*- coding: utf-8 -*-
"""Banc de l'agrandisseur v2 (règle d'or n°92), au navigateur, sur les pages du dépôt.

    python3 _outils/banc_loupe.py [racine] [--captures <dossier>] [--largeurs 1280,390,1920,853x1.5]

Pour chaque page équipée (hors archives et gabarits à jetons), à 1280 px :
  · chaque schéma SVG armé s'agrandit : l'image se charge, la légende ne la
    recouvre pas, l'image tient dans la largeur, Échap referme et rend le focus au schéma ;
  · FIDÉLITÉ : l'image agrandie ressemble au schéma de la page — écart moyen des couleurs entre
    les deux, réduits à la même vignette (0 = identiques, 1 = tout l'inverse). Le schéma est
    photographié sans son cadre (bordure et marge intérieure de la page, que l'agrandissement
    ne reprend pas : sur un QR code de 120 px, ce cadre faisait à lui seul un écart de 0,35).
    Un schéma qui perd ses couleurs ou son fond (le défaut du v1) s'écarte nettement ;
  · la première image <img> armée et visible s'agrandit, sans recouvrement ;
  · zéro erreur JavaScript.
Puis, sur les pages qui ont un schéma armé, aux autres largeurs : chargement, recouvrement,
largeur (« 853x1.5 » = 1280 px zoomé à 150 %).

Sortie 0 : tout est vert ; 1 : un refus, nommé ; 2 : aucune page lue.
Ce qu'il NE juge PAS : la lisibilité d'un schéma pour un élève (cela se regarde : --captures
écrit une capture par page et par largeur) ; les schémas des séances non affichées au chargement,
que la loupe n'arme pas (elle arme ce qui est visible à l'ouverture de la page — comportement
inchangé depuis le v1).
"""
import io
import pathlib
import sys

from PIL import Image, ImageChops, ImageStat
from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
SEUIL_FIDELITE = 0.12

args = sys.argv[1:]
captures = None
largeurs = ["1280", "390", "1920", "853x1.5"]
if "--captures" in args:
    i = args.index("--captures"); captures = pathlib.Path(args[i + 1]); del args[i:i + 2]
    captures.mkdir(parents=True, exist_ok=True)
if "--largeurs" in args:
    i = args.index("--largeurs"); largeurs = args[i + 1].split(","); del args[i:i + 2]
RACINE = pathlib.Path(args[0] if args else ICI.parent).resolve()

pages = []
for p in sorted(RACINE.rglob("*.html")):
    if "_archive-anciennes-versions" in p.parts:
        continue
    h = p.read_text(encoding="utf-8", errors="replace")
    if "loupe-images-v2" in h and "@@" not in h:
        pages.append(p)
if not pages:
    print("⛔ aucune page équipée lue sous %s" % RACINE)
    sys.exit(2)

MESURE = """() => {
  const f = document.querySelector('.loupe-fond'), g = f && f.querySelector('img'), l = f && f.querySelector('.loupe-legende');
  if (!f || !g) return null;
  const ri = g.getBoundingClientRect(), rl = l.getBoundingClientRect();
  return {charge: g.complete && g.naturalWidth > 0, ouvert: f.getAttribute('data-ouvert') === 'oui',
          recouvre: rl.height > 0 && rl.top < ri.bottom - 1 && rl.bottom > ri.top + 1,
          largeur: ri.right <= window.innerWidth + 1 && ri.left >= -1, h: ri.height, w: ri.width};
}"""


CONTENU = """(s) => {
  const r = s.getBoundingClientRect(), c = getComputedStyle(s), n = (k) => parseFloat(c[k]) || 0;
  const x = r.left + n('borderLeftWidth') + n('paddingLeft'), y = r.top + n('borderTopWidth') + n('paddingTop');
  return {x: x, y: y, width: r.right - n('borderRightWidth') - n('paddingRight') - x,
          height: r.bottom - n('borderBottomWidth') - n('paddingBottom') - y};
}"""


def vignette(png, w=48, h=None):
    im = Image.open(io.BytesIO(png)).convert("RGB")
    h = h or max(1, round(im.height * w / im.width))
    return im.resize((w, h), Image.LANCZOS)


def ecart(a, b):
    b = b.resize(a.size, Image.LANCZOS)
    return sum(ImageStat.Stat(ImageChops.difference(a, b)).mean) / (3 * 255)


refus, mesures, total_svg, total_img, avec_svg = [], [], 0, 0, []
with sync_playwright() as pw:
    nav = pw.chromium.launch()
    ctx = nav.new_context(viewport={"width": 1280, "height": 800})
    for p in pages:
        nom = str(p.relative_to(RACINE))
        pg = ctx.new_page()
        err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto(p.as_uri()); pg.wait_for_timeout(350)
        n_svg = pg.evaluate("document.querySelectorAll('svg.loupe-cliquable').length")
        if n_svg:
            avec_svg.append(p)
        for k in range(n_svg):
            svg = pg.locator("svg.loupe-cliquable").nth(k)
            try:
                svg.scroll_into_view_if_needed(timeout=3000)
            except Exception:
                continue                                  # schéma armé puis masqué (onglet) : rien à cliquer
            if not svg.is_visible():
                continue
            avant = vignette(pg.screenshot(clip=svg.evaluate(CONTENU)))   # le dessin, sans le cadre de la page
            svg.click()
            try:
                pg.wait_for_function("(() => { const g = document.querySelector('.loupe-fond img'); return g && g.complete && g.naturalWidth > 0; })()", timeout=4000)
            except Exception:
                pass
            pg.wait_for_timeout(250)
            m = pg.evaluate(MESURE)
            total_svg += 1
            if not m or not m["charge"]:
                refus.append((nom, "schéma %d : l'image agrandie ne se charge pas" % (k + 1)))
            else:
                apres = vignette(pg.locator(".loupe-fond img").screenshot(), avant.width, avant.height)
                e = ecart(avant, apres)
                mesures.append((e, nom, k + 1))
                if e > SEUIL_FIDELITE:
                    refus.append((nom, "schéma %d : agrandissement infidèle (écart %.2f)" % (k + 1, e)))
                if m["recouvre"]:
                    refus.append((nom, "schéma %d : la légende recouvre l'image" % (k + 1)))
                if not m["largeur"]:
                    refus.append((nom, "schéma %d : l'image dépasse la largeur" % (k + 1)))
                if captures is not None and k == 0:
                    pg.screenshot(path=str(captures / (nom.replace("/", "__") + "__1280.png")))
            pg.keyboard.press("Escape"); pg.wait_for_timeout(120)
            ferme = pg.evaluate("!document.querySelector('.loupe-fond[data-ouvert]')")
            focus = pg.evaluate("document.activeElement && document.activeElement.tagName.toLowerCase() === 'svg'")
            if not (ferme and focus):
                refus.append((nom, "schéma %d : Échap ne referme pas, ou le focus ne revient pas" % (k + 1)))
        img = pg.locator("img.loupe-cliquable:visible").first
        if img.count():
            try:
                img.scroll_into_view_if_needed(timeout=3000); img.click(timeout=3000)
                pg.wait_for_function("(() => { const g = document.querySelector('.loupe-fond img'); return g && g.complete && g.naturalWidth > 0; })()", timeout=4000)
                m = pg.evaluate(MESURE); total_img += 1
                if not m or not m["charge"]:
                    refus.append((nom, "image : ne se charge pas"))
                elif m["recouvre"]:
                    refus.append((nom, "image : la légende recouvre l'image"))
                pg.keyboard.press("Escape")
            except Exception as ex:
                refus.append((nom, "image : %s" % str(ex).splitlines()[0][:120]))
        if err:
            refus.append((nom, "erreur JavaScript : %s" % err[0][:160]))
        pg.close()
    ctx.close()

    # Autres largeurs, sur les pages qui ont un schéma armé
    for L in largeurs:
        if L == "1280":
            continue
        w, _, z = L.partition("x")
        z = float(z or 1)
        ctx = nav.new_context(viewport={"width": int(w), "height": int(800 / z) if z > 1 else 800}, device_scale_factor=z)
        for p in avec_svg:
            nom = str(p.relative_to(RACINE))
            pg = ctx.new_page(); pg.goto(p.as_uri()); pg.wait_for_timeout(300)
            svg = pg.locator("svg.loupe-cliquable").first
            if not svg.count() or not svg.is_visible():
                pg.close(); continue
            try:
                svg.scroll_into_view_if_needed(timeout=3000); svg.click(timeout=3000)
                pg.wait_for_function("(() => { const g = document.querySelector('.loupe-fond img'); return g && g.complete && g.naturalWidth > 0; })()", timeout=4000)
            except Exception:
                pass
            pg.wait_for_timeout(200)
            m = pg.evaluate(MESURE)
            if not m or not m["charge"]:
                refus.append((nom, "%s : l'image agrandie ne se charge pas" % L))
            else:
                if m["recouvre"]:
                    refus.append((nom, "%s : la légende recouvre l'image" % L))
                if not m["largeur"]:
                    refus.append((nom, "%s : l'image dépasse la largeur" % L))
                if captures is not None:
                    pg.screenshot(path=str(captures / (nom.replace("/", "__") + "__" + L + ".png")))
            pg.close()
        ctx.close()
    nav.close()

mesures.sort(reverse=True)
print("%d page(s) lues · %d schéma(s) SVG agrandi(s) · %d image(s) agrandie(s) · %d page(s) avec schéma armé"
      % (len(pages), total_svg, total_img, len(avec_svg)))
if mesures:
    print("fidélité (écart moyen, 0 = identique) : médiane %.3f · pire %.3f (%s, schéma %d)"
          % (mesures[len(mesures) // 2][0], mesures[0][0], mesures[0][1], mesures[0][2]))
for nom, quoi in refus:
    print("  ✘ %s — %s" % (nom, quoi))
if refus:
    sys.exit(1)
print("✅ chaque schéma et chaque image s'agrandit fidèlement, sans légende par-dessus, et se referme")
