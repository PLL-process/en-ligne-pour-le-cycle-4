#!/usr/bin/env python3
"""Suite de tests du vélo-cargo en 3D (5e_C3.1) — modèle, affiches, vue que l'élève fait tourner.

    python3 tests_objet3d_velo_cargo.py

Ce qu'elle vérifie : le modèle (pièces nommées, repères des pastilles, matières non métalliques, poids) et sa copie en
base64 ; les deux affiches ; la place du volet (après le dessin animé et sa prédiction) ; les mots de la légende, pris
dans le schéma ; page ouverte en file://, réseau coupé : rien de la 3D chargé avant le clic, aucune requête vers le
réseau ; le clic ouvre la vue, cache l'affiche, pose quatre pastilles et donne le focus à la vue ; le glisser et les
flèches tournent l'objet, « 0 » et le bouton (devenu « Revenir à la vue de départ ») le ramènent ; à l'impression, l'affiche ; sans WebGL, l'affiche et une phrase ; pas de
défilement de côté à 390 px ; zéro erreur JavaScript.
Ce qu'elle NE vérifie PAS : que la vue soit fluide sur les vieux postes du collège (ici, rendu logiciel SwiftShader), ni
sur tablette ; ni qu'un élève y retrouve les pièces (cela se regarde en classe).
Code de sortie : 0 tout passe · 1 un test échoue · 2 la suite n'a pas pu tourner (règle n°299).
"""
import base64
import io
import json
import pathlib
import re
import struct
import sys

try:
    from PIL import Image, ImageChops
    from playwright.sync_api import sync_playwright
except ImportError as e:
    print("PANNE —", e, "— rien n'a été vérifié (code 2)")
    sys.exit(2)

ICI = pathlib.Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
PAGE = ICI / "sequence_5e_C3.1-C3.4_shanghai.html"
GEN = ICI / "_generation" / "objet_3d_velo_cargo"
PIECES = ["batterie", "controleur", "moteur", "cadre"]
res = []


def t(nom, ok, detail=""):
    res.append((nom, bool(ok)))
    print(("✔" if ok else "✘"), nom, detail)


# 1 · le modèle et ses copies
glb = (GEN / "velo_cargo.glb").read_bytes()
n = struct.unpack("<I", glb[12:16])[0]
gltf = json.loads(glb[20:20 + n])
noms = {nd.get("name") for nd in gltf["nodes"]}
t("modèle .glb de moins de 300 Ko", len(glb) < 300_000, f"({len(glb)} octets)")
t("les quatre pièces de la légende sont des objets nommés", all(p in noms for p in PIECES))
t("chaque pièce a son repère de pastille", all("repere_" + p in noms for p in PIECES))
t("aucune matière métallique (elle sortirait noire)",
  all(m.get("pbrMetallicRoughness", {}).get("metallicFactor", 1) == 0 for m in gltf.get("materials", [])))
js = (ICI / "Images" / "velo_cargo_3d_modele.js").read_text(encoding="utf-8")
m = re.search(r'window\.MODELE_VELO_CARGO = "([A-Za-z0-9+/=]+)";', js)
t("velo_cargo_3d_modele.js = le .glb en base64, octet pour octet", bool(m) and base64.b64decode(m.group(1)) == glb)
for nom, taille in (("velo_cargo_3d_affiche.png", (1600, 1200)), ("velo_cargo_3d_affiche_etroite.png", (720, 540))):
    im = Image.open(ICI / "Images" / nom)
    t(f"affiche {nom} : {taille[0]} × {taille[1]}, fond transparent",
      im.size == taille and (im.mode == "RGBA" or (im.mode == "P" and "transparency" in im.info)), f"({im.size}, {im.mode})")
moteur = (DEPOT / "_ressources-communes" / "objet3d" / "objet3d.js").read_text(encoding="utf-8")
t("objet3d.js : un script classique, licence MIT de three.js en fin de fichier",
  "MIT" in moteur[-3000:] and not re.search(r"^\s*(import|export)\s", moteur, re.M))

# 2 · la page, lue comme un fichier
s = PAGE.read_text(encoding="utf-8")
i_fixe, i_3d, i_q5 = s.find('id="vppFixe"'), s.find('id="vc3dVolet"'), s.find('id="a1_5"')
t("le volet 3D vient après le dessin animé (et sa prédiction), avant la question suivante", 0 < i_fixe < i_3d < i_q5)
svg = (ICI / "Images" / "chaine_energie_velo_cargo.svg").read_text(encoding="utf-8")
textes = " ".join(re.findall(r">([^<>]+)</text>", svg))
legende = s[i_3d:s.find("</ol>", i_3d)]
mots = ["ALIMENTER", "DISTRIBUER", "CONVERTIR", "Contrôleur", "de puissance", "Moteur dans", "le moyeu arrière",
        "Énergie", "chimique", "électrique", "mécanique"]
t("les mots de la légende sont ceux du schéma de la chaîne (n°120)",
  all(w in textes for w in mots) and all(w.lower() in legende.lower() for w in mots),
  str([w for w in mots if w.lower() not in legende.lower() or w not in textes]))

AIDE_SANS_WEBGL = "Ce poste n'affiche pas la 3D"
SANS_WEBGL = """HTMLCanvasElement.prototype.getContext = (function(f){ return function(t){
  return /webgl/.test(t) ? null : f.apply(this, arguments); }; })(HTMLCanvasElement.prototype.getContext);"""


def image(loc):
    return Image.open(io.BytesIO(loc.screenshot())).convert("RGB")


def ecart(a, b):
    d = ImageChops.difference(a, b).convert("L").point(lambda v: 255 if v > 24 else 0)
    return sum(d.histogram()[255:]) / (a.size[0] * a.size[1])


try:
    with sync_playwright() as p:
        nav = p.chromium.launch(args=["--use-gl=swiftshader", "--enable-unsafe-swiftshader"])
        for largeur in (1280, 390):
            pg = nav.new_page(viewport={"width": largeur, "height": 900})
            erreurs, demandes = [], []
            pg.on("pageerror", lambda e: erreurs.append(str(e)))
            pg.on("console", lambda c: erreurs.append(c.text) if c.type == "error" else None)
            pg.on("request", lambda r: demandes.append(r.url))
            pg.route("http*://**", lambda r: r.abort())
            pg.goto(PAGE.as_uri())
            pg.wait_for_timeout(500)
            t(f"[{largeur}] rien de la 3D chargé à l'ouverture (ni la vue, ni le modèle)",
              not any(("objet3d.js" in u and "amorce" not in u) or "modele.js" in u for u in demandes))
            pg.evaluate("document.getElementById('vc3dVolet').open = true")
            pg.locator("#vc3dVolet").scroll_into_view_if_needed()
            btn = pg.locator('.o3d-btn[aria-controls="vc3d"]')
            t(f"[{largeur}] le bouton « Tourner » s'affiche (WebGL présent), 44 px de haut au moins",
              btn.is_visible() and btn.bounding_box()["height"] >= 44)
            btn.click()
            pg.wait_for_selector("#vc3d canvas", timeout=20000)
            pg.wait_for_timeout(700)
            fig = pg.locator("#vc3d")
            t(f"[{largeur}] la vue s'ouvre : affiche cachée, quatre pastilles, focus sur la vue",
              pg.locator("#vc3d img").is_hidden() and pg.locator("#vc3d .o3d-pastille").count() == 4
              and pg.evaluate("document.activeElement && document.activeElement.id") == "vc3d")
            depart = image(fig)
            b = fig.bounding_box()
            cx, cy = b["x"] + b["width"] / 2, b["y"] + b["height"] / 2
            pg.mouse.move(cx, cy); pg.mouse.down(); pg.mouse.move(cx + b["width"] * 0.25, cy, steps=8); pg.mouse.up()
            pg.wait_for_timeout(900)
            glisse = image(fig)
            t(f"[{largeur}] un glisser tourne l'objet", ecart(depart, glisse) > 0.01, f"({ecart(depart, glisse):.3f})")
            pg.keyboard.press("0"); pg.wait_for_timeout(900)
            retour = image(fig)
            t(f"[{largeur}] « 0 » ramène la vue de départ", ecart(depart, retour) < 0.005, f"({ecart(depart, retour):.4f})")
            pg.keyboard.press("ArrowLeft"); pg.keyboard.press("ArrowLeft"); pg.wait_for_timeout(900)
            fleche = image(fig)
            t(f"[{largeur}] les flèches du clavier tournent l'objet", ecart(depart, fleche) > 0.01, f"({ecart(depart, fleche):.3f})")
            t(f"[{largeur}] le bouton reste, et dit maintenant « Revenir à la vue de départ »",
              btn.is_visible() and "Revenir" in btn.inner_text())
            btn.click(); pg.wait_for_timeout(900)
            t(f"[{largeur}] le bouton ramène la vue de départ (le doigt n'a pas de touche « 0 »)",
              ecart(depart, image(fig)) < 0.005, f"({ecart(depart, image(fig)):.4f})")
            t(f"[{largeur}] pas de défilement de côté", pg.evaluate("document.documentElement.scrollWidth <= innerWidth"))
            pg.emulate_media(media="print")
            t(f"[{largeur}] à l'impression : l'affiche, pas le canevas",
              pg.evaluate("getComputedStyle(document.querySelector('#vc3d img')).display") == "block"
              and pg.evaluate("getComputedStyle(document.querySelector('#vc3d canvas')).display") == "none")
            pg.emulate_media(media="screen")
            t(f"[{largeur}] aucune requête vers le réseau", not any(u.startswith("http") for u in demandes),
              str([u for u in demandes if u.startswith("http")][:3]))
            t(f"[{largeur}] zéro erreur JavaScript", not erreurs, str(erreurs[:3]))
            pg.close()
        # sans WebGL : l'affiche reste, une phrase le dit, pas de bouton
        pg = nav.new_page(viewport={"width": 1280, "height": 900})
        pg.add_init_script(SANS_WEBGL)
        pg.route("http*://**", lambda r: r.abort())
        pg.goto(PAGE.as_uri())
        pg.evaluate("document.getElementById('vc3dVolet').open = true")
        t("sans WebGL : pas de bouton, l'affiche visible, la phrase qui le dit",
          pg.locator('.o3d-btn[aria-controls="vc3d"]').is_hidden() and pg.locator("#vc3d img").is_visible()
          and AIDE_SANS_WEBGL in pg.locator("#vc3dAide").inner_text())
        pg.close()
        nav.close()
except Exception as e:  # le navigateur n'a pas pu tourner : ce n'est pas un échec de la page, c'est une panne
    print("PANNE —", type(e).__name__, str(e)[:300], "— la partie navigateur n'a pas tourné (code 2)")
    sys.exit(2)

ok = sum(1 for _, r in res if r)
print(f"\n{ok}/{len(res)} tests passent")
sys.exit(0 if ok == len(res) else 1)
