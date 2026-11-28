#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""habiller.py — assemble, pour chaque frein, la vue large, la loupe et les pastilles numérotées.

`generer.py` (Blender) rend chaque frein deux fois : la roue entière (`large`, 960 × 676) et le frein de près
(`loupe`, 480 × 480). Ce script pose la loupe dans un rond à droite de la roue, trace le trait qui la relie à
l'endroit qu'elle montre, et ajoute les pastilles ① à ⑤ : elles renvoient à la légende écrite dans la page.

    python3 habiller.py RENDUS SORTIE [--freins patins,disque]

Sorties, par frein, dans SORTIE :
  <frein>_compose.mp4          le film assemblé, presque sans perte (assembler.sh l'encode pour la page)
  <frein>_complet_sombre.png   sa dernière image : l'affiche du film (règle d'or n°176, l'image complète)
  <frein>_complet_clair.png    la même sur fond clair, pour l'impression (n°102)

Les pastilles apparaissent à la fin du film, une par une ; elles sont toutes sur l'affiche.
Dépendances : Pillow, ffmpeg. Codes de sortie : 0 fait, 1 un film manque ou ffmpeg a échoué, 2 mauvais appel.
"""
import json
import math
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

LARG, HAUT, FPS, DUREE = 960, 676, 24, 4.5
COTE = 480                               # côté de l'image de la loupe
LOUPE = (460, 98)                        # son coin haut gauche dans l'image assemblée
RAYON = 232                              # rayon du rond de la loupe
CENTRE = (LOUPE[0] + COTE // 2, LOUPE[1] + COTE // 2)
K = 3                                    # on dessine trois fois plus grand, puis on réduit : traits lisses
PASTILLE = 32                            # rayon d'une pastille
DEBUT, PAS, FONDU = 84 / FPS, 4 / FPS, 0.25   # les pastilles : la première, l'écart entre deux, le fondu

ENCRE = {"sombre": dict(trait="#e4eaf5", bord="#0b1b39", fond="#ffffff", chiffre="#0b1b39"),
         "clair": dict(trait="#0b1b39", bord="#ffffff", fond="#0b1b39", chiffre="#ffffff")}

# Pour chaque frein : où la loupe regarde, puis les pastilles (numéro, vue, repère de generer.py, décalage en pixels).
# Les mêmes numéros disent la même chose pour les trois freins :
#   1 le levier · 2 ce qui transmet · 3 ce qui pousse · 4 ce qui frotte sans tourner · 5 ce qui tourne et frotte
PLAN = {
    "patins": dict(zone=("zone", 30), pastilles=[
        (1, "large", "levier", (-64, 4)), (2, "large", "cable", (62, -4)),
        (3, "loupe", "bras", (-2, 40)), (4, "loupe", "patin", (-30, 80)), (5, "loupe", "jante", (92, 84))]),
    "disque": dict(zone=("zone", 30), pastilles=[
        (1, "large", "levier", (-64, 4)), (2, "large", "durite", (-62, -6)),
        (3, "loupe", "etrier", (66, -96)), (4, "loupe", "plaquette", (-74, 96)), (5, "loupe", "disque", (0, 6))]),
    "tambour": dict(zone=("zone", 30), pastilles=[
        (1, "large", "levier", (-64, 4)), (2, "large", "cable", (64, -4)),
        (3, "loupe", "came", (78, -78)), (4, "loupe", "machoire", (70, 66)), (5, "loupe", "tambour", (0, 0))]),
}


def police(taille):
    for chemin in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                   "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
                   r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf",
                   "/Library/Fonts/Arial Bold.ttf"):
        if os.path.exists(chemin):
            return ImageFont.truetype(chemin, taille)
    raise SystemExit("habiller.py : aucune police grasse trouvée (DejaVu Sans Bold, Liberation, Segoe UI, Arial).")


def toile():
    return Image.new("RGBA", (LARG * K, HAUT * K), (0, 0, 0, 0))


def reduire(im):
    return im.resize((LARG, HAUT), Image.LANCZOS)


def trait(d, a, b, encre, epais=3):
    """Un trait clair bordé de sombre (ou l'inverse) : il se lit sur le pneu comme sur le fond."""
    for couleur, e in ((encre["bord"], epais + 3), (encre["trait"], epais)):
        d.line([(a[0] * K, a[1] * K), (b[0] * K, b[1] * K)], fill=couleur, width=e * K)


def rond(d, c, r, encre, epais=3):
    for couleur, e, rr in ((encre["bord"], epais + 3, r + 1.5), (encre["trait"], epais, r)):
        d.ellipse([(c[0] - rr) * K, (c[1] - rr) * K, (c[0] + rr) * K, (c[1] + rr) * K], outline=couleur,
                  width=int(e * K))


def vers(a, b, distance):
    """Le point à `distance` de a, en allant vers b."""
    n = math.hypot(b[0] - a[0], b[1] - a[1]) or 1.0
    return (a[0] + (b[0] - a[0]) * distance / n, a[1] + (b[1] - a[1]) * distance / n)


def point(reperes, vue, nom):
    x, y = reperes[vue][nom]
    return (x, y) if vue == "large" else (LOUPE[0] + x, LOUPE[1] + y)


def masque():
    m = Image.new("L", (COTE * K, COTE * K), 0)
    c = COTE * K / 2
    ImageDraw.Draw(m).ellipse([c - RAYON * K, c - RAYON * K, c + RAYON * K, c + RAYON * K], fill=255)
    return m.resize((COTE, COTE), Image.LANCZOS)


def decor(frein, reperes, fond):
    """Le rond de la loupe, le petit rond sur la roue, et le trait qui les relie."""
    encre, im = ENCRE[fond], toile()
    d = ImageDraw.Draw(im)
    nom, r = PLAN[frein]["zone"]
    z = point(reperes, "large", nom)
    trait(d, vers(z, CENTRE, r), vers(CENTRE, z, RAYON), encre)
    rond(d, z, r, encre)
    rond(d, CENTRE, RAYON, encre, epais=4)
    return reduire(im)


def pastille(frein, reperes, fond, numero, vue, nom, decalage):
    encre, im = ENCRE[fond], toile()
    d = ImageDraw.Draw(im)
    ancre = point(reperes, vue, nom)
    c = (ancre[0] + decalage[0], ancre[1] + decalage[1])
    if math.hypot(*decalage) > PASTILLE:                    # la pastille est à côté de la pièce : un trait y mène
        trait(d, c, ancre, encre, epais=2)
        d.ellipse([(ancre[0] - 4.5) * K, (ancre[1] - 4.5) * K, (ancre[0] + 4.5) * K, (ancre[1] + 4.5) * K],
                  fill=encre["trait"], outline=encre["bord"], width=K)
    d.ellipse([(c[0] - PASTILLE) * K, (c[1] - PASTILLE) * K, (c[0] + PASTILLE) * K, (c[1] + PASTILLE) * K],
              fill=encre["fond"], outline=encre["bord"], width=3 * K)
    d.text((c[0] * K, c[1] * K), str(numero), font=police(41 * K), fill=encre["chiffre"], anchor="mm")
    return reduire(im)


def habiller(frein, rendus, sortie):
    with open(os.path.join(rendus, frein + "_reperes.json"), encoding="utf-8") as f:
        reperes = json.load(f)
    rond_loupe = masque()
    travail = os.path.join(sortie, "_calques")
    os.makedirs(travail, exist_ok=True)
    calques = {}
    for fond in ("sombre", "clair"):
        couches = [decor(frein, reperes, fond)] + [pastille(frein, reperes, fond, *p)
                                                   for p in PLAN[frein]["pastilles"]]
        calques[fond] = couches
        image = Image.open(os.path.join(rendus, "%s_large_%s.png" % (frein, fond))).convert("RGBA")
        loupe = Image.open(os.path.join(rendus, "%s_loupe_%s.png" % (frein, fond))).convert("RGBA")
        image.paste(loupe, LOUPE, rond_loupe)
        for couche in couches:
            image.alpha_composite(couche)
        image.convert("RGB").save(os.path.join(sortie, "%s_complet_%s.png" % (frein, fond)))
    # le film : sur fond sombre seulement
    chemins = []
    rond_loupe.save(os.path.join(travail, frein + "_masque.png"))
    for i, couche in enumerate(calques["sombre"]):
        chemins.append(os.path.join(travail, "%s_calque%d.png" % (frein, i)))
        couche.save(chemins[-1])
    entrees = ["-i", os.path.join(rendus, frein + "_large_maitre.mp4"),
               "-i", os.path.join(rendus, frein + "_loupe_maitre.mp4"),
               "-loop", "1", "-framerate", str(FPS), "-t", str(DUREE), "-i", os.path.join(travail, frein + "_masque.png")]
    for c in chemins:
        entrees += ["-loop", "1", "-framerate", str(FPS), "-t", str(DUREE), "-i", c]
    graphe = ["[1:v]format=yuva444p[lv]", "[2:v]format=gray[mk]", "[lv][mk]alphamerge[lp]",
              "[0:v][lp]overlay=%d:%d[v0]" % LOUPE, "[v0][3:v]overlay=0:0[v1]"]
    for k in range(1, len(chemins)):
        graphe.append("[%d:v]fade=t=in:st=%.3f:d=%.3f:alpha=1[p%d]" % (3 + k, DEBUT + (k - 1) * PAS, FONDU, k))
        graphe.append("[v%d][p%d]overlay=0:0[v%d]" % (k, k, k + 1))
    film = os.path.join(sortie, frein + "_compose.mp4")
    commande = ["ffmpeg", "-y", "-v", "error"] + entrees + [
        "-filter_complex", ";".join(graphe), "-map", "[v%d]" % len(chemins), "-t", str(DUREE), "-r", str(FPS),
        "-c:v", "libx264", "-crf", "8", "-preset", "slow", "-pix_fmt", "yuv420p", "-an", film]
    subprocess.run(commande, check=True)
    return film


def main(args):
    if len(args) < 2:
        print(__doc__)
        return 2
    rendus, sortie = args[0], args[1]
    freins = args[args.index("--freins") + 1].split(",") if "--freins" in args else list(PLAN)
    os.makedirs(sortie, exist_ok=True)
    for frein in freins:
        for vue in ("large", "loupe"):
            if not os.path.exists(os.path.join(rendus, "%s_%s_maitre.mp4" % (frein, vue))):
                print("habiller.py : il manque %s_%s_maitre.mp4 dans %s" % (frein, vue, rendus))
                return 1
        try:
            print("assemblé :", habiller(frein, rendus, sortie))
        except subprocess.CalledProcessError as e:
            print("habiller.py : ffmpeg a échoué pour %s (%s)" % (frein, e))
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
