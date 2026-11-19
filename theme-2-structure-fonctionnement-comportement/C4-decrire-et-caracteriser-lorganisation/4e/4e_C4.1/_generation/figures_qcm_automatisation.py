# -*- coding: utf-8 -*-
"""Les deux figures du QCM « Automatiser le jardin » (4e_C4.1, 18-19/11/2026).

  · Images/chronogramme_eclairage_jardin.svg — de 16 h à 22 h : la luminosité (avec le seuil « nuit » de 50 lux),
    le signal de présence et la LED de l'allée. La LED s'allume à chaque présence, même en plein jour : c'est le
    défaut que l'élève lit, puis corrige (4e_C6.1).
  · Images/algorigramme_eclairage_corrige.svg — le programme corrigé : la LED ne s'allume que s'il fait nuit ET que
    quelqu'un passe (4e_C6.2).
Les questions LISENT ces figures (n°331 : document sous les yeux, complet). Fond clair. SVG écrit à la main.
Usage : python3 _generation/figures_qcm_automatisation.py
"""
import os

ICI = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(ICI, "..", "Images")
ENCRE, FOND, GRIS = "#1b2a41", "#fbfaf6", "#8a97a8"
POLICE = 'font-family="Segoe UI, Arial, sans-serif"'


def svg(l, h, titre, desc, corps):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {l} {h}" width="{l}" height="{h}" '
            f'style="width:100%;height:auto" role="img" aria-labelledby="t d" {POLICE}>\n'
            f'<title id="t">{titre}</title>\n<desc id="d">{desc}</desc>\n'
            f'<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" '
            f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{ENCRE}"/></marker></defs>\n'
            f'<rect x="0" y="0" width="{l}" height="{h}" fill="{FOND}"/>\n' + corps + "</svg>\n")


def texte(x, y, s, t=21, gras=False, ancre="start", c=ENCRE):
    g = ' font-weight="700"' if gras else ""
    return f'<text x="{x}" y="{y}" font-size="{t}"{g} text-anchor="{ancre}" fill="{c}">{s}</text>\n'


# ── le chronogramme ──
X0, X1 = 250, 1010            # 16 h → 22 h
H0, H1 = 16, 22
def xh(h):                    # heure (décimale) → abscisse
    return X0 + (h - H0) / (H1 - H0) * (X1 - X0)

PRESENCES = [17.0, 20.0, 21.5]          # trois passages
DUREE_LED = 10 / 60                     # la LED reste allumée 10 minutes


def chronogramme():
    c = texte(30, 44, "L’éclairage de l’allée du jardin, de 16 h à 22 h", 26, True)
    # bande « nuit » (après 19 h, quand la luminosité passe sous 50 lux), sur les trois pistes
    c += f'<rect x="{xh(19):.1f}" y="70" width="{X1 - xh(19):.1f}" height="470" fill="#e7ebf3"/>\n'
    c += texte((xh(19) + X1) / 2, 92, "il fait nuit (moins de 50 lux)", 20, True, "middle", "#3b4a66")
    pistes = [("Luminosité", "(en lux)", 110, 230), ("Présence", "(0 ou 1)", 270, 380), ("LED de l’allée", "(0 ou 1)", 420, 530)]
    for nom, unite, haut, bas in pistes:
        c += texte(30, (haut + bas) / 2 - 4, nom, 21, True) + texte(30, (haut + bas) / 2 + 24, unite, 20)
        c += f'<line x1="{X0}" y1="{bas}" x2="{X1}" y2="{bas}" stroke="{GRIS}" stroke-width="1.5"/>\n'
        c += f'<line x1="{X0}" y1="{haut - 10}" x2="{X0}" y2="{bas}" stroke="{GRIS}" stroke-width="1.5"/>\n'
    # luminosité : de 800 lux à 0, passe sous 50 lux à 19 h
    pts = []
    for i in range(0, 61):
        h = H0 + i * 0.1
        lux = max(0.0, 800 * (1 - ((h - 16) / 3.12) ** 1.6)) if h < 19.12 else 0.0   # 50 lux à 19 h
        y = 230 - lux / 800 * 115
        pts.append(f"{xh(h):.1f},{y:.1f}")
    c += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#c77700" stroke-width="3"/>\n'
    yseuil = 230 - 50 / 800 * 115
    c += (f'<line x1="{X0}" y1="{yseuil:.1f}" x2="{X1}" y2="{yseuil:.1f}" stroke="#3b4a66" stroke-width="1.5" '
          f'stroke-dasharray="6 5"/>\n')
    c += texte(xh(19.9), 205, "seuil « nuit » : 50 lux", 20, False, "start", "#3b4a66")
    # présence et LED : tout ou rien
    def creneaux(haut, bas, debuts, duree, couleur):
        d = f"M {X0} {bas}"
        for h in debuts:
            d += f" L {xh(h):.1f} {bas} L {xh(h):.1f} {haut} L {xh(h + duree):.1f} {haut} L {xh(h + duree):.1f} {bas}"
        d += f" L {X1} {bas}"
        return f'<path d="{d}" fill="none" stroke="{couleur}" stroke-width="3"/>\n'
    c += creneaux(300, 380, PRESENCES, 4 / 60, "#1f6fb2")
    c += creneaux(450, 530, PRESENCES, DUREE_LED, "#2e8b57")
    c += texte(X0 - 12, 306, "1", 20, False, "end") + texte(X0 - 12, 386, "0", 20, False, "end")
    c += texte(X0 - 12, 456, "1", 20, False, "end") + texte(X0 - 12, 536, "0", 20, False, "end")
    # axe du temps
    for h in range(H0, H1 + 1):
        c += f'<line x1="{xh(h):.1f}" y1="560" x2="{xh(h):.1f}" y2="570" stroke="{ENCRE}" stroke-width="1.5"/>\n'
        c += texte(xh(h), 596, f"{h} h", 20, False, "middle")
    c += f'<line x1="{X0}" y1="560" x2="{X1}" y2="560" stroke="{ENCRE}" stroke-width="1.5"/>\n'
    c += texte(X1, 628, "temps (en heures)", 20, False, "end")
    desc = ("Chronogramme de 16 h à 22 h, en trois pistes. Luminosité, en lux : elle baisse de 800 lux à 16 h jusqu'à "
            "0 ; elle passe sous le seuil « nuit » de 50 lux vers 19 h. Présence, 0 ou 1 : trois passages, à 17 h, "
            "20 h et 21 h 30. LED de l'allée, 0 ou 1 : elle s'allume 10 minutes à chaque passage, à 17 h, 20 h et "
            "21 h 30 — même à 17 h, quand il fait encore jour.")
    return svg(1040, 640, "Chronogramme de l’éclairage de l’allée du jardin", desc, c)


# ── l'algorigramme corrigé ──
def boite(x, y, l, h, lignes, fond):
    c = f'<rect x="{x}" y="{y}" width="{l}" height="{h}" rx="8" fill="{fond}" stroke="{ENCRE}" stroke-width="2"/>\n'
    y0 = y + h / 2 - (len(lignes) - 1) * 13 + 8
    return c + "".join(texte(x + l / 2, y0 + i * 26, s, 21, False, "middle") for i, s in enumerate(lignes))


def fleche(points):
    d = "M " + " L ".join(f"{x} {y}" for x, y in points)
    return f'<path d="{d}" fill="none" stroke="{ENCRE}" stroke-width="2.4" marker-end="url(#fl)"/>\n'


def algorigramme():
    c = texte(30, 44, "Le programme corrigé de l’éclairage", 26, True)
    c += f'<ellipse cx="300" cy="100" rx="90" ry="30" fill="#e9f7ec" stroke="{ENCRE}" stroke-width="2"/>\n' + texte(300, 107, "Début", 21, False, "middle")
    c += fleche([(300, 130), (300, 166)])
    c += boite(140, 168, 320, 70, ["Lire la luminosité", "et la présence"], "#e8f1fb")
    c += fleche([(300, 238), (300, 296)])
    c += (f'<path d="M 300 298 L 490 388 L 300 478 L 110 388 Z" fill="#fff3d6" stroke="{ENCRE}" stroke-width="2"/>\n'
          + texte(300, 382, "Il fait nuit ET", 21, False, "middle") + texte(300, 408, "quelqu’un passe ?", 21, False, "middle"))
    c += fleche([(300, 478), (300, 536)]) + texte(312, 514, "OUI", 19, True)
    c += boite(140, 538, 320, 70, ["Allumer la LED", "pendant 10 minutes"], "#e8f1fb")
    c += fleche([(490, 388), (566, 388)]) + texte(528, 374, "NON", 19, True, "middle")
    c += boite(568, 348, 240, 80, ["Laisser la LED", "éteinte"], "#e8f1fb")
    # les deux branches remontent AVANT « Lire » : le programme relit les capteurs, en boucle
    c += fleche([(688, 348), (688, 148), (314, 148)])
    c += fleche([(140, 573), (60, 573), (60, 148), (286, 148)])
    desc = ("Algorigramme corrigé. Début ; lire la luminosité et la présence ; test : il fait nuit ET quelqu'un passe ? "
            "Si OUI : allumer la LED pendant 10 minutes. Si NON : laisser la LED éteinte. Dans les deux cas, une "
            "flèche remonte avant « Lire la luminosité et la présence » : le programme relit les capteurs et tourne "
            "en boucle.")
    return svg(840, 640, "Algorigramme corrigé de l’éclairage de l’allée", desc, c)


if __name__ == "__main__":
    for nom, f in (("chronogramme_eclairage_jardin.svg", chronogramme), ("algorigramme_eclairage_corrige.svg", algorigramme)):
        chemin = os.path.normpath(os.path.join(IMAGES, nom))
        open(chemin, "w", encoding="utf-8").write(f())
        print("écrit", os.path.relpath(chemin))
