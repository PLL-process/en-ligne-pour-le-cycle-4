# -*- coding: utf-8 -*-
"""assembler.py — du modèle velo_cargo.glb (écrit par generer.py, dans Blender) aux fichiers que lit la page.

    python3 assembler.py

1. Images/velo_cargo_3d_modele.js : le .glb en base64 dans un script classique (window.MODELE_VELO_CARGO), parce
   qu'une page ouverte en file:// (clé USB, réseau du collège) ne peut pas lire un .glb par fetch().
2. Les deux affiches (l'image fixe que la page montre avant le clic, à l'impression et sans WebGL) : la vue de départ
   elle-même, rendue par objet3d.js dans Chromium, pastilles comprises, fond transparent (rien de sombre à
   l'impression). Deux tailles pour que les pastilles gardent 26 px à l'écran : Images/velo_cargo_3d_affiche.png
   (800 × 600, rendue ×2) et Images/velo_cargo_3d_affiche_etroite.png (360 × 270, ×2, écrans de 600 px et moins).
   Palette de 256 couleurs (Pillow), comme les autres PNG du dépôt.

Les options (direction, pastilles) sont LUES dans la page : une seule source, la figure #vc3d de la séquence.
"""
import base64
import html
import json
import re
import sys
import tempfile
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ICI = Path(__file__).resolve().parent
LOT = ICI.parents[1]
DEPOT = LOT.parents[3]
PAGE = LOT / "sequence_5e_C3.1-C3.4_shanghai.html"
COMMUN = DEPOT / "_ressources-communes" / "objet3d"


def options_de_la_page():
    s = PAGE.read_text(encoding="utf-8")
    m = re.search(r'<figure class="o3d" id="vc3d"[^>]*data-o3d-options=\'([^\']*)\'', s)
    if not m:
        print("PANNE — figure #vc3d introuvable dans la séquence : rien n'est écrit (code 2)", file=sys.stderr)
        sys.exit(2)
    return html.unescape(m.group(1))


def ecrire_modele():
    glb = (ICI / "velo_cargo.glb").read_bytes()
    cible = LOT / "Images" / "velo_cargo_3d_modele.js"
    cible.write_text("/* Modèle simplifié du vélo-cargo S1 (_generation/objet_3d_velo_cargo/generer.py, Blender), en base64 :"
                     " une page en file:// ne lit pas un .glb par fetch(). Écrit par assembler.py. */\n"
                     'window.MODELE_VELO_CARGO = "' + base64.b64encode(glb).decode() + '";\n', encoding="utf-8")
    return cible


def ecrire_affiches(options):
    sorties = []
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
        b = p.chromium.launch(args=["--use-gl=swiftshader", "--enable-unsafe-swiftshader"])
        for (l, h, nom) in ((800, 600, "velo_cargo_3d_affiche.png"), (360, 270, "velo_cargo_3d_affiche_etroite.png")):
            page = Path(tmp) / "affiche.html"
            page.write_text(f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<link rel="stylesheet" href="{(COMMUN / 'objet3d.css').as_uri()}">
<style>html,body{{margin:0;background:transparent;font-family:"Segoe UI",system-ui,-apple-system,sans-serif}}.o3d{{width:{l}px;height:{h}px;border:0;border-radius:0;background:transparent;margin:0;max-height:none}}</style></head>
<body><figure class="o3d" id="vc3d" data-o3d-moteur="{(COMMUN / 'objet3d.js').as_uri()}"
 data-o3d-modele="{(LOT / 'Images' / 'velo_cargo_3d_modele.js').as_uri()}" data-o3d-global="MODELE_VELO_CARGO"
 data-o3d-options='{html.escape(options, quote=True)}'></figure><button type="button" class="o3d-btn" aria-controls="vc3d" hidden>3D</button>
<script src="{(COMMUN / 'objet3d-amorce.js').as_uri()}"></script></body></html>""", encoding="utf-8")
            pg = b.new_page(viewport={"width": l, "height": h}, device_scale_factor=2)
            pg.route("http*://**", lambda r: r.abort())        # rien ne vient du réseau
            pg.goto(page.as_uri())
            pg.click(".o3d-btn")
            pg.wait_for_selector(".o3d-pastille", timeout=20000)
            pg.wait_for_timeout(600)
            brut = Path(tmp) / nom
            pg.locator("#vc3d").screenshot(path=str(brut), omit_background=True)
            pg.close()
            cible = LOT / "Images" / nom
            Image.open(brut).convert("RGBA").quantize(colors=256, method=Image.Quantize.FASTOCTREE).save(cible, optimize=True)
            sorties.append(cible)
        b.close()
    return sorties


if __name__ == "__main__":
    opts = options_de_la_page()
    json.loads(opts)                                      # des options illisibles arrêtent tout
    for f in [ecrire_modele()] + ecrire_affiches(opts):
        print(f.relative_to(DEPOT), f.stat().st_size, "octets")
