#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""spirale_fibonacci.py — la spirale « de Fibonacci » du presse-papier, en SVG, sur la sortie standard.

Usage : python3 _generation/spirale_fibonacci.py > /tmp/spirale.svg
Le tracé est incrusté dans `fiche_arts_tp_4e_socle.html` (figure « La spirale, construite sur les
cotes de l'objet ») : relancer le script redonne le même SVG, octet pour octet.

Le rectangle fait 89 × 55 mm — la largeur du socle sur plats et l'arête du dé du TP de 4e.

Chaque carré est découpé dans le rectangle restant ; chaque quart de cercle est
centré sur le coin du carré qui touche le carré suivant. Les coordonnées sont en
millimètres (1 unité = 1 mm), puis mises à l'échelle dans le viewBox.
"""
S = 8          # 1 mm → 8 unités SVG
MX, MY = 40, 28  # marges (étiquettes)
W, H = 89, 55

# (côté, x, y, coin du centre, étiquette-objet)
carres = [
    (55, 0,  0,  "br", "arête du dé"),
    (34, 55, 0,  "bl", "≈ rayon de la moulure (35)"),
    (21, 68, 34, "tl", "points du dé"),
    (13, 55, 42, "tr", "épaisseur de la plinthe"),
    (8,  55, 34, "br", "arrondi du dé"),
    (5,  63, 34, "bl", "arrondi du socle · pointe enfoncée · moulure"),
    (3,  65, 39, "tl", "moulure"),
    (2,  63, 40, "tr", ""),
    (1,  63, 39, "br", ""),
    (1,  64, 39, "bl", ""),
]

def X(v): return round(MX + v * S, 1)
def Y(v): return round(MY + v * S, 1)

def coin(c, x, y, cote):
    return {"br": (x + cote, y + cote), "bl": (x, y + cote),
            "tl": (x, y), "tr": (x + cote, y)}[c]

# arcs : du point « de départ » au point « d'arrivée », sens horaire à l'écran
def arc(c, x, y, cote):
    cx, cy = coin(c, x, y, cote)
    r = cote
    if c == "br":   p0, p1 = (cx - r, cy), (cx, cy - r)
    elif c == "bl": p0, p1 = (cx, cy - r), (cx + r, cy)
    elif c == "tl": p0, p1 = (cx + r, cy), (cx, cy + r)
    else:           p0, p1 = (cx, cy + r), (cx - r, cy)
    return p0, p1

# vérification de continuité
prev = None
for cote, x, y, c, _ in carres:
    p0, p1 = arc(c, x, y, cote)
    if prev is not None:
        assert prev == p0, (prev, p0, cote)
    prev = p1
# vérification du pavage : somme des aires = 89 × 55
assert sum(c * c for c, *_ in carres) == W * H, sum(c * c for c, *_ in carres)

couleurs = {55: "#61dafb", 34: "#81fba1", 21: "#ffd66b", 13: "#c68ef2", 8: "#ff9f6b",
            5: "#ff7b88", 3: "#9bbefc", 2: "#9bbefc", 1: "#9bbefc"}

out = []
vw, vh = MX * 2 + W * S, MY * 2 + H * S
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}" role="img" '
           f'aria-labelledby="spirale-titre spirale-desc" class="spirale">')
out.append('<title id="spirale-titre">La spirale de Fibonacci construite sur les cotes du presse-papier</title>')
out.append('<desc id="spirale-desc">Un rectangle de 89 sur 55 millimètres découpé en carrés de côtés 55, 34, 21, 13, 8, 5, 3, 2, 1 et 1 ; '
           'un quart de cercle dans chaque carré forme une spirale qui s’enroule vers le petit coin.</desc>')
out.append('<style>.spirale .cadre{fill:none;stroke:#e4eaf5;stroke-width:3}'
           '.spirale .carre{fill-opacity:.13;stroke-width:1.6}.spirale .arc{fill:none;stroke:#fff;stroke-width:4.5;stroke-linecap:round}'
           '.spirale text{font-family:"Segoe UI",system-ui,Arial,sans-serif;fill:#e4eaf5}'
           '.spirale .num{font-weight:700}.spirale .cote{fill:#9bbefc;font-size:21px}</style>')
out.append(f'<rect class="cadre" x="{X(0)}" y="{Y(0)}" width="{W*S}" height="{H*S}" rx="2"/>')
for cote, x, y, c, _ in carres:
    col = couleurs[cote]
    out.append(f'<rect class="carre" x="{X(x)}" y="{Y(y)}" width="{cote*S}" height="{cote*S}" fill="{col}" stroke="{col}"/>')
# étiquettes des nombres (seulement si le carré est assez grand)
tailles = {55: 56, 34: 44, 21: 34, 13: 24, 8: 16, 5: 11}
for cote, x, y, c, _ in carres:
    if cote in tailles:
        fs = tailles[cote]
        out.append(f'<text class="num" x="{X(x + cote/2)}" y="{Y(y + cote/2)}" font-size="{fs}" '
                   f'text-anchor="middle" dominant-baseline="central" fill="{couleurs[cote]}">{cote}</text>')
# la spirale
d = []
first = True
for cote, x, y, c, _ in carres:
    p0, p1 = arc(c, x, y, cote)
    if first:
        d.append(f"M {X(p0[0])} {Y(p0[1])}")
        first = False
    d.append(f"A {cote*S} {cote*S} 0 0 1 {X(p1[0])} {Y(p1[1])}")
out.append(f'<path class="arc" d="{" ".join(d)}"/>')
# cotes du rectangle
out.append(f'<text class="cote" x="{X(W/2)}" y="{Y(0) - 9}" text-anchor="middle">89 mm — le socle, d’un plat à l’autre</text>')
out.append(f'<text class="cote" transform="translate({X(0) - 10} {Y(H/2)}) rotate(-90)" text-anchor="middle">55 mm — l’arête du dé</text>')
out.append('</svg>')
svg = "\n".join(out)
import sys
sys.stdout.write(svg + "\n")
