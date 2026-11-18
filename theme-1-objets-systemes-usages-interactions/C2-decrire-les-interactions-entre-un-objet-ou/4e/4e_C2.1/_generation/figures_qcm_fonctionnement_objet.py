# -*- coding: utf-8 -*-
"""Les deux figures du QCM « Comment expliquer le fonctionnement d'un objet ? » (4e_C2.1, 18/11/2026).

  · Images/notice_climatiseur_extrait.svg — un extrait de notice : les touches et leurs pictogrammes, une procédure en
    trois étapes, deux avertissements. Les questions la LISENT (n°331 : le document sous les yeux, complet).
  · Images/algorigramme_minuterie_climatiseur.svg — la minuterie du climatiseur, du langage naturel à l'algorigramme.

Fond clair, comme une notice imprimée. SVG écrit à la main (aucun raster, aucune référence distante).
Usage : python3 _generation/figures_qcm_fonctionnement_objet.py   (depuis le dossier du lot ou n'importe où)
"""
import os

ICI = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(ICI, "..", "Images")
ENCRE, FOND, BORD = "#1b2a41", "#fbfaf6", "#8a97a8"
POLICE = 'font-family="Segoe UI, Arial, sans-serif"'


def svg(largeur, hauteur, titre, desc, corps):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largeur} {hauteur}" width="{largeur}" '
            f'height="{hauteur}" style="width:100%;height:auto" role="img" aria-labelledby="t d" {POLICE}>\n'
            f'<title id="t">{titre}</title>\n<desc id="d">{desc}</desc>\n'
            f'<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" '
            f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{ENCRE}"/></marker></defs>\n'
            f'<rect x="0" y="0" width="{largeur}" height="{hauteur}" fill="{FOND}"/>\n' + corps + "</svg>\n")


def texte(x, y, s, taille=21, gras=False, ancre="start", couleur=ENCRE):
    g = ' font-weight="700"' if gras else ""
    return f'<text x="{x}" y="{y}" font-size="{taille}"{g} text-anchor="{ancre}" fill="{couleur}">{s}</text>\n'


def touche(cx, cy, dessin):
    return (f'<circle cx="{cx}" cy="{cy}" r="21" fill="#ffffff" stroke="{ENCRE}" stroke-width="2"/>\n'
            f'<g stroke="{ENCRE}" stroke-width="2.4" fill="none" stroke-linecap="round">{dessin(cx, cy)}</g>\n')


def marche(x, y):
    return f'<path d="M {x-7} {y-6} A 10 10 0 1 0 {x+7} {y-6}"/><line x1="{x}" y1="{y-12}" x2="{x}" y2="{y}"/>'


def flocon(x, y):
    import math
    traits = ""
    for a in (90, 30, 150):
        dx, dy = 12 * math.cos(math.radians(a)), 12 * math.sin(math.radians(a))
        traits += f'<line x1="{x-dx:.1f}" y1="{y-dy:.1f}" x2="{x+dx:.1f}" y2="{y+dy:.1f}"/>'
    # les petites branches qui font du trait un flocon (et non un astérisque)
    for a in range(30, 390, 60):
        bx, by = x + 8 * math.cos(math.radians(a)), y + 8 * math.sin(math.radians(a))
        for e in (a - 45, a + 45):
            traits += (f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx + 4.5 * math.cos(math.radians(e)):.1f}" '
                       f'y2="{by + 4.5 * math.sin(math.radians(e)):.1f}"/>')
    return traits


def goutte(x, y):
    return f'<path d="M {x} {y-12} C {x+3} {y-6} {x+9} {y} {x+9} {y+4} A 9 9 0 0 1 {x-9} {y+4} C {x-9} {y} {x-3} {y-6} {x} {y-12} Z"/>'


def helice(x, y):
    return "".join(f'<ellipse cx="{x}" cy="{y-7}" rx="4" ry="7" transform="rotate({a} {x} {y})"/>' for a in (0, 120, 240))


def horloge(x, y):
    return f'<circle cx="{x}" cy="{y}" r="11"/><line x1="{x}" y1="{y}" x2="{x}" y2="{y-7}"/><line x1="{x}" y1="{y}" x2="{x+6}" y2="{y+3}"/>'


def fleches(x, y):
    return (f'<path d="M {x-6} {y-3} L {x} {y-11} L {x+6} {y-3} Z" fill="{ENCRE}"/>'
            f'<path d="M {x-6} {y+3} L {x} {y+11} L {x+6} {y+3} Z" fill="{ENCRE}"/>')


def notice():
    c = texte(40, 52, "Extrait de la notice — climatiseur mobile", 28, True)
    c += f'<rect x="30" y="80" width="490" height="400" rx="14" fill="#ffffff" stroke="{BORD}" stroke-width="2"/>\n'
    c += texte(52, 120, "Les touches de la télécommande", 22, True)
    lignes = [(marche, "Marche / Arrêt"), (flocon, "Froid"), (goutte, "Déshumidifier"),
              (helice, "Ventilation seule"), (horloge, "Minuterie : programmer l’arrêt"),
              (fleches, "Régler la température ou la durée")]
    for i, (dessin, nom) in enumerate(lignes):
        y = 168 + i * 52
        c += touche(78, y, dessin) + texte(118, y + 7, nom, 21)
    c += f'<rect x="540" y="80" width="490" height="400" rx="14" fill="#ffffff" stroke="{BORD}" stroke-width="2"/>\n'
    c += texte(562, 120, "Programmer l’arrêt", 22, True)
    etapes = [(170, "1. Appuie sur la touche de l’horloge."), (226, "2. Règle la durée avec ▲ et ▼ :"),
              (256, "de 1 à 12 heures."), (312, "3. Attends 5 secondes :"), (342, "le voyant de l’horloge reste allumé.")]
    for y, s in etapes:
        c += texte(562 if s[0].isdigit() else 590, y, s, 21)
    c += f'<rect x="30" y="500" width="1000" height="112" rx="14" fill="#fff6d6" stroke="#b8860b" stroke-width="2"/>\n'
    c += f'<path d="M 78 526 L 108 582 L 48 582 Z" fill="#ffd21f" stroke="#111111" stroke-width="3" stroke-linejoin="round"/>\n'
    c += texte(78, 576, "!", 30, True, "middle", "#111111")
    c += texte(132, 548, "Ne bouche pas la sortie d’air.", 21, True)
    c += texte(132, 588, "Débranche l’appareil avant de le nettoyer.", 21, True)
    desc = ("Extrait de notice d'un climatiseur mobile. À gauche, les touches de la télécommande : marche-arrêt ; "
            "flocon, froid ; goutte, déshumidifier ; hélice, ventilation seule ; horloge, minuterie pour programmer "
            "l'arrêt ; flèches, régler la température ou la durée. À droite, programmer l'arrêt : 1. appuie sur la "
            "touche de l'horloge ; 2. règle la durée avec les flèches, de 1 à 12 heures ; 3. attends 5 secondes, le "
            "voyant de l'horloge reste allumé. En bas, deux avertissements avec le triangle de danger : ne bouche pas "
            "la sortie d'air ; débranche l'appareil avant de le nettoyer.")
    return svg(1060, 640, "Extrait de la notice d’un climatiseur mobile", desc, c)


def boite(x, y, l, h, lignes, fond):
    c = f'<rect x="{x}" y="{y}" width="{l}" height="{h}" rx="8" fill="{fond}" stroke="{ENCRE}" stroke-width="2"/>\n'
    y0 = y + h / 2 - (len(lignes) - 1) * 13 + 8
    return c + "".join(texte(x + l / 2, y0 + i * 26, s, 21, False, "middle") for i, s in enumerate(lignes))


def fleche(points):
    d = "M " + " L ".join(f"{x} {y}" for x, y in points)
    return f'<path d="{d}" fill="none" stroke="{ENCRE}" stroke-width="2.4" marker-end="url(#fl)"/>\n'


def algorigramme():
    c = texte(30, 44, "La minuterie du climatiseur", 26, True)
    c += f'<ellipse cx="250" cy="100" rx="90" ry="30" fill="#e9f7ec" stroke="{ENCRE}" stroke-width="2"/>\n' + texte(250, 107, "Début", 21, False, "middle")
    c += fleche([(250, 130), (250, 166)])
    c += boite(110, 168, 280, 58, ["Régler la durée"], "#e8f1fb")
    c += fleche([(250, 226), (250, 284)])
    c += (f'<path d="M 250 286 L 410 366 L 250 446 L 90 366 Z" fill="#fff3d6" stroke="{ENCRE}" stroke-width="2"/>\n'
          + texte(250, 360, "La durée est-elle", 21, False, "middle") + texte(250, 386, "écoulée ?", 21, False, "middle"))
    c += fleche([(410, 366), (488, 366)]) + texte(449, 352, "NON", 19, True, "middle")
    c += boite(490, 326, 250, 80, ["Continuer à rafraîchir", "la pièce"], "#e8f1fb")
    c += fleche([(615, 326), (615, 256), (264, 256)])
    c += fleche([(250, 446), (250, 508)]) + texte(262, 484, "OUI", 19, True)
    c += boite(110, 510, 280, 58, ["Arrêter le climatiseur"], "#e8f1fb")
    c += fleche([(250, 568), (250, 606)])
    c += f'<ellipse cx="250" cy="638" rx="90" ry="30" fill="#e9f7ec" stroke="{ENCRE}" stroke-width="2"/>\n' + texte(250, 645, "Fin", 21, False, "middle")
    desc = ("Algorigramme de la minuterie. Début ; régler la durée ; test : la durée est-elle écoulée ? Si NON : "
            "continuer à rafraîchir la pièce, puis une flèche revient avant le test. Si OUI : arrêter le climatiseur ; fin.")
    return svg(770, 690, "Algorigramme de la minuterie du climatiseur", desc, c)


if __name__ == "__main__":
    for nom, f in (("notice_climatiseur_extrait.svg", notice), ("algorigramme_minuterie_climatiseur.svg", algorigramme)):
        chemin = os.path.normpath(os.path.join(IMAGES, nom))
        open(chemin, "w", encoding="utf-8").write(f())
        print("écrit", os.path.relpath(chemin))
