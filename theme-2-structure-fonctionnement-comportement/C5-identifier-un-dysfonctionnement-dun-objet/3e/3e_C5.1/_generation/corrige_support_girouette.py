# -*- coding: utf-8 -*-
"""3e_C5.1 — le corrigé du défi FreeCAD du Bonus : le support de girouette, d'après le plan coté
(Images/plan_cote_support_girouette.svg), et son STL (règles d'or n°332 et n°336, 16/11/2026).

La pièce, cote par cote (millimètres) :
  · platine 60 × 40 × 8, percée de deux trous Ø5 traversants, entraxe 40, centrés sur la largeur ;
  · fût cylindrique Ø12, haut de 35 au-dessus de la platine, au centre ;
  · alésage Ø6 dans le fût, sur ses 35 mm (le plan le dessine en pointillés dans le fût seul).
Ce sont les trois opérations de FreeCAD que la page décrit (Version 🅱) : protrusion de la platine, protrusion du fût,
perçages et alésage.

Produit :
1. `support_girouette_corrige.stl` — le maillage de la pièce (STL binaire, en millimètres), calculé par opérations
   booléennes (bibliothèque manifold3d : un solide fermé, sans trou de maillage, imprimable) ;
2. `Images/capture_corrige_support_girouette_3d.png` — la vue 3D de CE fichier STL, tracée par three.js dans Chromium
   (ombrage et arêtes vives, comme la vue « Ombré avec arêtes » d'un modeleur).

Dépendances : `pip install manifold3d` ; Playwright (Chromium) ; three.js 0.160.0 hors du dépôt
(`npm install three@0.160.0` dans un dossier à part), son chemin dans la variable THREE_JS
(…/node_modules/three/build/three.min.js).
Rejouer : THREE_JS=… python3 _generation/corrige_support_girouette.py   (depuis le dossier du lot)
"""
import json
import math
import os
import struct
import tempfile

import numpy as np
from manifold3d import Manifold, set_circular_segments

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STL = os.path.join(ICI, "support_girouette_corrige.stl")
PNG = os.path.join(ICI, "Images", "capture_corrige_support_girouette_3d.png")
THREE = os.environ.get("THREE_JS", "")

set_circular_segments(96)
platine = Manifold.cube((60, 40, 8), center=False).translate((-30, -20, 0))
trou = Manifold.cylinder(8 + 2, 2.5, 2.5).translate((0, 0, -1))
platine = platine - trou.translate((-20, 0, 0)) - trou.translate((20, 0, 0))
fut = Manifold.cylinder(35, 6, 6).translate((0, 0, 8))
alesage = Manifold.cylinder(35 + 1, 3, 3).translate((0, 0, 8))      # de la face de la platine au sommet du fût
piece = (platine + fut) - alesage

mesh = piece.to_mesh()
V = np.array(mesh.vert_properties)[:, :3]
F = np.array(mesh.tri_verts)
volume = piece.volume()
attendu = 60 * 40 * 8 - 2 * math.pi * 2.5 ** 2 * 8 + math.pi * (6 ** 2 - 3 ** 2) * 35
print("volume : %.1f mm³ (attendu %.1f) · %d triangles · genre %d" % (volume, attendu, len(F), piece.genus()))
assert abs(volume - attendu) / attendu < 0.005

# le STL binaire : 80 octets d'en-tête, le nombre de triangles, puis normale + 3 sommets par triangle
with open(STL, "wb") as f:
    f.write(b"support de girouette corrige - 3e_C5.1 - mm - CC0".ljust(80, b" "))
    f.write(struct.pack("<I", len(F)))
    for a, b, c in F:
        n = np.cross(V[b] - V[a], V[c] - V[a])
        n = n / (np.linalg.norm(n) or 1)
        f.write(struct.pack("<12fH", *n, *V[a], *V[b], *V[c], 0))
print("STL :", os.path.getsize(STL), "octets")

# la vue 3D de ce STL : on relit le fichier écrit, pour montrer exactement ce qu'il contient
with open(STL, "rb") as f:
    f.seek(80)
    nb = struct.unpack("<I", f.read(4))[0]
    tri = [struct.unpack("<12fH", f.read(50))[3:12] for _ in range(nb)]
if not THREE or not os.path.exists(THREE):
    raise SystemExit("THREE_JS : chemin de three.min.js introuvable — la vue 3D n'est pas refaite (le STL l'est).")
PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#fff}</style>
<script src="%s"></script></head><body><script>
const T = %s, L = 1400, H = 1000;
const r = new THREE.WebGLRenderer({antialias:true, preserveDrawingBuffer:true}); r.setSize(L, H); r.setPixelRatio(1);
document.body.appendChild(r.domElement);
const sc = new THREE.Scene();
const fond = document.createElement('canvas'); fond.width = 2; fond.height = 256; const g = fond.getContext('2d');
const gr = g.createLinearGradient(0, 0, 0, 256); gr.addColorStop(0, '#9fb3cf'); gr.addColorStop(1, '#eef2f8');
g.fillStyle = gr; g.fillRect(0, 0, 2, 256); sc.background = new THREE.CanvasTexture(fond);
const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.Float32BufferAttribute(T.flat(), 3));
geo.computeVertexNormals(); geo.rotateX(-Math.PI/2);                       // z du plan (la hauteur) vers le haut de l'écran
const mat = new THREE.MeshStandardMaterial({color:0xd9dde3, metalness:0.05, roughness:0.55, flatShading:false,
  polygonOffset:true, polygonOffsetFactor:1, polygonOffsetUnits:1});
sc.add(new THREE.Mesh(geo, mat));
sc.add(new THREE.LineSegments(new THREE.EdgesGeometry(geo, 25), new THREE.LineBasicMaterial({color:0x1d2a3a})));
sc.add(new THREE.HemisphereLight(0xffffff, 0x8a94a6, 1.15));
const d1 = new THREE.DirectionalLight(0xffffff, 1.3); d1.position.set(60, 120, 90); sc.add(d1);
const d2 = new THREE.DirectionalLight(0xffffff, 0.45); d2.position.set(-90, 40, -60); sc.add(d2);
const cam = new THREE.PerspectiveCamera(26, L/H, 1, 2000);
cam.position.set(95, 88, 120); cam.lookAt(0, 14, 0); cam.updateProjectionMatrix();
r.render(sc, cam); window.FINI = true;
</script></body></html>""" % ("file://" + THREE, json.dumps([list(t) for t in tri]))
from playwright.sync_api import sync_playwright  # noqa: E402
with tempfile.TemporaryDirectory() as tmp:
    html = os.path.join(tmp, "vue.html")
    open(html, "w", encoding="utf-8").write(PAGE)
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-gl=swiftshader", "--enable-unsafe-swiftshader", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1400, "height": 1000})
        pg.goto("file://" + html)
        pg.wait_for_function("window.FINI === true", timeout=20000)
        brut = os.path.join(tmp, "v.png")
        pg.locator("canvas").screenshot(path=brut)
        b.close()
    from PIL import Image
    im = Image.open(brut).convert("RGB")
    im = im.crop((150, 60, 1250, 940))
    os.makedirs(os.path.dirname(PNG), exist_ok=True)
    im.save(PNG, optimize=True)
print("vue 3D :", PNG, im.size)
