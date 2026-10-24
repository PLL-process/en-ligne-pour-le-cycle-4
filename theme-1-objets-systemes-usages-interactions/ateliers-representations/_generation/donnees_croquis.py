# -*- coding: utf-8 -*-
"""Atelier — Le croquis (croquis à main levée ; storyboard pour une suite de croquis).

Codes servis : 4e_C2.1, 4e_C7.2, 3e_C7.2. Pas de 5e : le programme nomme le croquis en 4e
(« en partant du langage naturel (texte, croquis) » ; « croquis, schéma, graphique, algorithme,
modélisation ») et en 3e (« croquis, schéma, graphique, algorithme, modélisation »).
Objet-fil de 4e : le jardin connecté ; de 3e : la station d'alerte cyclonique.

Le verbe change d'un niveau à l'autre, pas la notion :
  4e  PASSER du texte de l'usager au croquis, puis PROPOSER une pièce par un croquis coté ;
  3e  PROPOSER PLUSIEURS solutions, LIRE un croquis coté, puis CHOISIR quand passer au schéma
      ou à la modélisation.

Les croquis que l'élève LIT sont dessinés ici, au « crayon » : un trait épais, un peu irrégulier,
qui déborde aux coins — comme à main levée. Le tirage est fixé (graine) : le même dessin à
chaque construction. SVG originaux, CC0.
"""
import math
import random

import figures

e = figures.e

SLUG = "croquis"
COURT = "cq"
EMOJI = "✏️"
TITRE = "Le croquis"
TITRE_COURT = "le croquis (croquis à main levée)"
TITRE_COMPLET = "Le croquis, souvent appelé croquis à main levée"
ETIQUETTE = "✏️ croquis à main levée"
ETIQUETTE_COURTE = "Croquis"
MENTION_FICTION = ("Situations imaginées pour les exercices : Inès et la borne de vélos du front de mer, Mme Joseph et le "
                   "boîtier du jardin, la station d'alerte cyclonique, sa sirène, son boîtier et toutes leurs dimensions "
                   "sont inventés.")

# ─────────────────────────────────────────────────────────────────────────────
# Le crayon « main levée »
# ─────────────────────────────────────────────────────────────────────────────
ENCRE = "#26324a"      # le crayon noir
ROUGE = "#c0182b"      # le crayon rouge : cotes et flèches (le même que dans la zone de dessin)
PAPIER = "#fffdf7"
PEAU = "#f0c9a6"
TERRE = "#8a6a45"


class Crayon:
    """Des traits légèrement irréguliers, qui débordent un peu aux extrémités. Une graine par dessin :
    le tirage est le même à chaque construction."""

    def __init__(self, graine, amp=1.3):
        self.r = random.Random(graine)
        self.amp = amp

    def _bruit(self, a):
        return self.r.uniform(-a, a)

    def _points(self, pts, ferme=False, amp=None, pas=26, deborde=3.0):
        amp = self.amp if amp is None else amp
        pts = list(pts)
        if ferme:
            pts = pts + [pts[0]]
        out = []
        for i in range(len(pts) - 1):
            (x1, y1), (x2, y2) = pts[i], pts[i + 1]
            dx, dy = x2 - x1, y2 - y1
            L = math.hypot(dx, dy) or 1.0
            nx, ny = -dy / L, dx / L
            n = max(1, int(L / pas))
            for k in range(n):
                t = k / n
                b = self._bruit(amp) if (k or i) else self._bruit(amp / 2)
                out.append((x1 + dx * t + nx * b, y1 + dy * t + ny * b))
            if L > 14:   # un point juste avant le coin : le coin reste net
                t = (L - 4) / L
                out.append((x1 + dx * t + nx * self._bruit(amp / 2), y1 + dy * t + ny * self._bruit(amp / 2)))
        xl, yl = pts[-1]
        out.append((xl + self._bruit(amp / 2), yl + self._bruit(amp / 2)))
        if deborde and len(out) >= 2:
            (ax, ay), (bx, by) = out[0], out[1]
            L = math.hypot(bx - ax, by - ay) or 1.0
            d = self.r.uniform(0.5, deborde)
            out[0] = (ax - (bx - ax) / L * d, ay - (by - ay) / L * d)
            (ax, ay), (bx, by) = out[-2], out[-1]
            L = math.hypot(bx - ax, by - ay) or 1.0
            d = self.r.uniform(0.5, deborde) + (5 if ferme else 0)
            out[-1] = (bx + (bx - ax) / L * d, by + (by - ay) / L * d)
        return out

    @staticmethod
    def _chemin(p):
        if len(p) == 2:
            return "M%.1f,%.1f L%.1f,%.1f" % (p[0][0], p[0][1], p[1][0], p[1][1])
        d = ["M%.1f,%.1f" % p[0]]
        for i in range(1, len(p) - 1):
            mx, my = (p[i][0] + p[i + 1][0]) / 2, (p[i][1] + p[i + 1][1]) / 2
            d.append("Q%.1f,%.1f %.1f,%.1f" % (p[i][0], p[i][1], mx, my))
        d.append("L%.1f,%.1f" % p[-1])
        return " ".join(d)

    def _trace(self, p, ep, coul, opac=1.0, tirets=None):
        return ('<path d="%s" fill="none" stroke="%s" stroke-width="%.1f" stroke-linecap="round" stroke-linejoin="round"%s%s/>'
                % (self._chemin(p), coul, ep, (' stroke-dasharray="%s"' % tirets) if tirets else "",
                   (' opacity="%.2f"' % opac) if opac < 1 else ""))

    def trait(self, pts, ep=3.2, coul=ENCRE, ferme=False, amp=None, double=True, rempli=None, tirets=None):
        """Un trait (ou une forme fermée) passant par pts ; `double` repasse le trait une seconde fois, plus fin."""
        h = []
        if rempli:
            h.append('<polygon points="%s" fill="%s"/>' % (" ".join("%.1f,%.1f" % q for q in pts), rempli))
        h.append(self._trace(self._points(pts, ferme, amp), ep, coul, tirets=tirets))
        if double:
            h.append(self._trace(self._points(pts, ferme, (self.amp if amp is None else amp) * 1.15, deborde=4.5),
                                 max(1.0, ep * 0.42), coul, opac=0.45, tirets=tirets))
        return "".join(h)

    def rond(self, cx, cy, rx, ry=None, ep=3.0, coul=ENCRE, rempli=None, double=True, tirets=None):
        """Un rond (ou une ellipse) qui ne se referme pas tout à fait à l'endroit où il a commencé."""
        ry = ry or rx
        h = []
        if rempli:
            h.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>' % (cx, cy, rx, ry, rempli))
        for passe in range(2 if double else 1):
            a0 = self.r.uniform(0, 2 * math.pi)
            n = max(12, int(2 * math.pi * max(rx, ry) / 13))
            tour = 2 * math.pi + self.r.uniform(0.22, 0.42)
            pts = []
            for k in range(n + 1):
                a = a0 + tour * k / n
                f = 1 + self.r.uniform(-0.035, 0.035)
                pts.append((cx + rx * f * math.cos(a), cy + ry * f * math.sin(a)))
            h.append(self._trace(pts, ep if passe == 0 else max(1.0, ep * 0.42), coul, opac=1.0 if passe == 0 else 0.45,
                                 tirets=tirets))
        return "".join(h)

    def arc(self, cx, cy, r, a1, a2, ep=2.2, coul=ENCRE):
        """Un arc de cercle, de a1 à a2 (degrés, 0 = à droite, sens des aiguilles d'une montre)."""
        n = max(4, int(abs(a2 - a1) / 12))
        pts = []
        for k in range(n + 1):
            a = math.radians(a1 + (a2 - a1) * k / n)
            f = 1 + self.r.uniform(-0.03, 0.03)
            pts.append((cx + r * f * math.cos(a), cy + r * f * math.sin(a)))
        return self._trace(pts, ep, coul)

    def fleche(self, x1, y1, x2, y2, courbe=0.0, ep=4.0, coul=ROUGE, pointe=17, deux=False):
        """Une flèche de mouvement : un trait épais (courbé de `courbe` px), une pointe en deux coups de crayon."""
        L = math.hypot(x2 - x1, y2 - y1) or 1.0
        nx, ny = -(y2 - y1) / L, (x2 - x1) / L
        qx, qy = (x1 + x2) / 2 + nx * courbe, (y1 + y2) / 2 + ny * courbe

        def b(t):
            return ((1 - t) ** 2 * x1 + 2 * (1 - t) * t * qx + t ** 2 * x2,
                    (1 - t) ** 2 * y1 + 2 * (1 - t) * t * qy + t ** 2 * y2)
        n = max(4, int(L / 22))
        pts = []
        for k in range(n + 1):
            x, y = b(k / n)
            a = 0 if k in (0, n) else self.amp * 0.8
            pts.append((x + self._bruit(a), y + self._bruit(a)))
        h = [self._trace(pts, ep, coul)]

        def tete(xt, yt, xa, ya):
            ang = math.atan2(yt - ya, xt - xa)
            out = []
            for s in (-1, 1):
                a = ang + math.pi - s * math.radians(28 + self._bruit(3))
                out.append(self._trace([(xt, yt), (xt + pointe * math.cos(a), yt + pointe * math.sin(a))], ep, coul))
            return "".join(out)
        xa, ya = b(0.9)
        h.append(tete(x2, y2, xa, ya))
        if deux:
            xa, ya = b(0.1)
            h.append(tete(x1, y1, xa, ya))
        return "".join(h)


def ecrit(x, y, lignes, taille=15, coul=ENCRE, ancre="start", gras=False, italique=False, halo=True, inter=1.2):
    """Une légende écrite (une ou plusieurs lignes), centrée verticalement sur y, avec un liseré clair pour rester lisible."""
    if isinstance(lignes, str):
        lignes = [lignes]
    attrs = ['x="%.1f"' % x, 'y="%.1f"' % y, 'font-size="%s"' % taille, 'fill="%s"' % coul,
             'text-anchor="%s"' % ancre, 'dominant-baseline="middle"']
    if gras:
        attrs.append('font-weight="700"')
    if italique:
        attrs.append('font-style="italic"')
    if halo:
        attrs.append('stroke="%s" stroke-width="4" stroke-linejoin="round" paint-order="stroke"' % PAPIER)
    debut = -((len(lignes) - 1) / 2) * inter
    tsp = "".join('<tspan x="%.1f" dy="%.2fem">%s</tspan>' % (x, debut if i == 0 else inter, e(l)) for i, l in enumerate(lignes))
    return "<text %s>%s</text>" % (" ".join(attrs), tsp)


def fil(c, x1, y1, x2, y2, coul=ENCRE):
    """Le trait fin qui relie une légende à ce qu'elle nomme, avec un point au bout."""
    return (c.trait([(x1, y1), (x2, y2)], ep=1.5, coul=coul, double=False, amp=0.5)
            + '<circle cx="%.1f" cy="%.1f" r="2.8" fill="%s"/>' % (x2, y2, coul))


def cote(c, x1, y1, x2, y2, valeur, tx=None, ty=None, ancre="middle", attaches=(), coul=ROUGE, taille=15):
    """Une cote : la ligne de cote et ses deux pointes, les lignes d'attache, et la valeur."""
    h = [c.trait([(x1, y1), (x2, y2)], ep=1.8, coul=coul, double=False, amp=0.4)]
    L = math.hypot(x2 - x1, y2 - y1) or 1.0
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    for (px, py, sx, sy) in ((x1, y1, 1, 1), (x2, y2, -1, -1)):
        bx, by = px + sx * ux * 10, py + sy * uy * 10
        h.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
                 % (px, py, bx - uy * 3.6, by + ux * 3.6, bx + uy * 3.6, by - ux * 3.6, coul))
    for (ax, ay, bx, by) in attaches:
        h.append(c.trait([(ax, ay), (bx, by)], ep=1.2, coul=coul, double=False, amp=0.3))
    if tx is None:
        tx, ty = (x1 + x2) / 2 - uy * 13, (y1 + y2) / 2 + ux * 13 - (0 if abs(uy) > 0.5 else 0)
        if abs(uy) < 0.5:
            ty = (y1 + y2) / 2 - 12
    h.append(ecrit(tx, ty, valeur, taille=taille, coul=coul, gras=True, ancre=ancre))
    return "".join(h)


def pastille(x, y, marque, coul=ENCRE, r=16, taille=17):
    return ('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, r, coul)
            + ecrit(x, y, marque, taille=taille, coul="#ffffff", ancre="middle", gras=True, halo=False))


def feuille(largeur, hauteur):
    return ('<rect x="3" y="3" width="%d" height="%d" rx="8" fill="%s" stroke="#d9d2c0" stroke-width="1.5"/>'
            % (largeur - 6, hauteur - 6, PAPIER))


def croquis_svg(ident, largeur, hauteur, titre, desc, corps):
    return figures.svg(largeur, hauteur, titre, desc, feuille(largeur, hauteur) + corps, ident=ident)


def bonhomme(c, x, tete_y, pied_y, r=17, ep=3.4):
    """Une personne debout, vue de profil ou de face : une tête, un corps, deux jambes. Les bras se dessinent à part."""
    cou = tete_y + r
    hanche = cou + (pied_y - cou) * 0.48
    return "".join([c.rond(x, tete_y, r, ep=ep - 0.4, rempli=PEAU),
                    c.trait([(x, cou), (x + 3, hanche)], ep=ep + 2.2),
                    c.trait([(x + 3, hanche), (x - 14, pied_y)], ep=ep),
                    c.trait([(x + 3, hanche), (x + 18, pied_y)], ep=ep)])


# ─────────────────────────────────────────────────────────────────────────────
# Les dessins — 4e
# ─────────────────────────────────────────────────────────────────────────────
def _velo(c, F, R):
    """Un vélo de profil : roue avant F, roue arrière R (centres), cadre en losange."""
    (fx, fy), (rx, ry) = F, R
    bb = (fx + 0.5 * (rx - fx), fy + 4)
    s = (fx + 0.63 * (rx - fx), fy - 82)
    hd = (fx + 0.13 * (rx - fx), fy - 87)
    h = [c.rond(fx, fy, 40, ep=3.2), c.rond(rx, ry, 40, ep=3.2),
         c.trait([R, bb, s, R], ep=3.4, double=False), c.trait([s, hd, bb], ep=3.4, double=False),
         c.trait([hd, F], ep=3.4, double=False), c.rond(bb[0], bb[1], 8, ep=2.4, double=False),
         c.trait([s, (s[0], s[1] - 12)], ep=3.0, double=False),
         c.trait([(s[0] - 17, s[1] - 13), (s[0] + 17, s[1] - 14)], ep=5.2, double=False),
         c.trait([hd, (hd[0] - 4, hd[1] - 18), (hd[0] + 15, hd[1] - 22)], ep=3.6, double=False)]
    return "".join(h), (hd[0] + 15, hd[1] - 22)


def croquis_borne(ident, lettre, variante, titre, desc, graine):
    """Trois croquis de la même situation : A (le bon geste), B (le geste inversé), C (l'intérieur de la borne)."""
    W, H = 580, 380
    c = Crayon(graine)
    h = [c.trait([(18, 336), (150, 334), (320, 337), (460, 334), (562, 336)], ep=2.6, double=False)]
    if variante in ("A", "B"):
        bx = 170
        # la personne d'abord : le vélo passe devant ses jambes
        h.append(bonhomme(c, 284, 92, 334))
        # la borne
        h.append(c.trait([(bx, 112), (bx + 64, 112), (bx + 64, 336), (bx, 336)], ferme=True, ep=3.4))
        h.append(c.trait([(bx + 10, 126), (bx + 54, 126), (bx + 54, 160), (bx + 10, 160)], ferme=True, ep=2.3, double=False))
        h.append(c.trait([(bx + 17, 138), (bx + 46, 138)], ep=1.6, double=False))
        h.append(c.trait([(bx + 17, 148), (bx + 38, 148)], ep=1.6, double=False))
        h.append(c.rond(bx + 32, 178, 7, ep=2.2, rempli="#8fd99a", double=False))
        h.append(c.trait([(bx + 13, 194), (bx + 52, 194), (bx + 52, 222), (bx + 13, 222)], ferme=True, ep=2.3, double=False))
        h.append(c.arc(bx + 24, 208, 6, -60, 60, ep=1.8))
        h.append(c.arc(bx + 24, 208, 11, -60, 60, ep=1.8))
        # la pince qui tient la roue avant
        h.append(c.trait([(bx + 64, 300), (bx + 92, 300)], ep=5.5, double=False))
        velo, guidon = _velo(c, (290, 292), (460, 292))
        h.append(velo)
        # les bras d'Inès : l'un tend la carte au lecteur, l'autre tient le guidon
        h.append(c.trait([(281, 128), (252, 168), (226, 203)], ep=3.2))
        h.append(c.trait([(213, 196), (231, 191), (235, 205), (217, 210)], ferme=True, ep=2.0, double=False, rempli="#ffffff"))
        h.append(c.trait([(287, 132), (guidon[0] - 2, guidon[1] + 3)], ep=3.2))
        # les légendes ① et ②
        h.append(ecrit(14, 167, ["② la borne bipe,", "le voyant", "passe au vert"], taille=14))
        h.append(fil(c, 130, 172, bx + 24, 178))
        h.append(ecrit(14, 231, ["① je pose", "ma carte sur", "le lecteur"], taille=14))
        h.append(fil(c, 108, 236, bx + 13, 214))
        if variante == "A":
            h.append(c.fleche(360, 166, 548, 160, courbe=-10))
            h.append(ecrit(454, 116, ["③ je tire le vélo", "en arrière, vers moi"], taille=14, ancre="middle", coul=ROUGE, gras=True))
        else:
            h.append(c.fleche(548, 160, 360, 166, courbe=10))
            h.append(ecrit(454, 116, ["③ je pousse le vélo", "vers la borne"], taille=14, ancre="middle", coul=ROUGE, gras=True))
    else:
        # C : la borne ouverte, vue de l'intérieur ; ni usager, ni geste
        bx, bw = 190, 140
        h.append(c.trait([(bx, 60), (bx + bw, 60), (bx + bw, 336), (bx, 336)], ferme=True, ep=3.4))
        # la carte électronique
        h.append(c.trait([(bx + 25, 88), (bx + 115, 88), (bx + 115, 148), (bx + 25, 148)], ferme=True, ep=2.4, double=False,
                         rempli="#dfeedd"))
        for (x, y) in ((bx + 38, 100), (bx + 70, 100), (bx + 38, 124), (bx + 82, 124)):
            h.append(c.trait([(x, y), (x + 18, y), (x + 18, y + 14), (x, y + 14)], ferme=True, ep=1.6, double=False))
        # l'antenne du lecteur : une boucle de fil
        for k in (0, 7):
            h.append(c.trait([(bx + 14 + k, 176 + k), (bx + 64 - k, 176 + k), (bx + 64 - k, 216 - k), (bx + 14 + k, 216 - k)],
                             ferme=True, ep=1.8, double=False))
        h.append(c.trait([(bx + 64, 196), (bx + 80, 170), (bx + 70, 148)], ep=1.8, double=False))
        # les fils vers le verrou
        h.append(c.trait([(bx + 100, 148), (bx + 104, 200), (bx + 96, 250), (bx + 106, 290)], ep=1.8, double=False))
        # le verrou et la pince
        h.append(c.trait([(bx + 90, 286), (bx + 130, 286), (bx + 130, 312), (bx + 90, 312)], ferme=True, ep=2.6, double=False,
                         rempli="#e4e4e4"))
        h.append(c.trait([(bx + 130, 296), (bx + 168, 296), (bx + 168, 304), (bx + 130, 304)], ferme=True, ep=2.2, double=False))
        h.append(c.rond(410, 294, 40, ep=3.0))
        h.append(c.fleche(bx + 160, 326, bx + 112, 326, ep=3.2, pointe=12))
        # le câble d'alimentation, qui vient du sol
        h.append(c.trait([(bx + 50, 312), (bx + 46, 336), (bx + 30, 352), (bx - 10, 362)], ep=2.4, double=False))
        h.append(ecrit(14, 110, ["carte", "électronique"], taille=14))
        h.append(fil(c, 108, 112, bx + 25, 118))
        h.append(ecrit(14, 196, ["antenne", "du lecteur"], taille=14))
        h.append(fil(c, 96, 198, bx + 14, 196))
        h.append(ecrit(470, 210, ["verrou", "de la pince"], taille=14))
        h.append(fil(c, 466, 216, bx + 132, 290))
        h.append(ecrit(bx + 150, 356, ["le verrou recule"], taille=14, coul=ROUGE, gras=True, ancre="middle"))
        h.append(ecrit(14, 300, ["câble", "d'alimentation"], taille=14))
        h.append(fil(c, 118, 304, bx + 38, 346))
    h.append(pastille(26, 26, lettre))
    h.append(ecrit(50, 26, "Croquis " + lettre, taille=16, gras=True))
    return croquis_svg(ident, W, H, titre, desc, "".join(h))


BORNE_A = croquis_borne(
    "cq-borne-a", "A", "A", "Croquis A : prendre un vélo à la borne",
    "Croquis à main levée. Une personne debout à côté d'une borne de vélos ; un vélo est tenu par sa roue avant dans une "
    "pince de la borne. Légende 1 : je pose ma carte sur le lecteur — la main de la personne tient une carte contre le "
    "lecteur de la borne. Légende 2 : la borne bipe, le voyant passe au vert. Légende 3, écrite en rouge au-dessus d'une "
    "flèche rouge qui part du vélo et s'éloigne de la borne : je tire le vélo en arrière, vers moi.", 41)

BORNE_B = croquis_borne(
    "cq-borne-b", "B", "B", "Croquis B : prendre un vélo à la borne",
    "Le même croquis que le A, avec la même personne, la même borne et les mêmes légendes 1 et 2. Seule la flèche rouge "
    "change : elle va vers la borne. Légende 3 : je pousse le vélo vers la borne.", 41)

BORNE_C = croquis_borne(
    "cq-borne-c", "C", "C", "Croquis C : l'intérieur de la borne",
    "Croquis à main levée de la borne ouverte, vue de l'intérieur. Aucune personne. On voit une carte électronique, la "
    "boucle de fil de l'antenne du lecteur, des fils qui descendent vers le verrou de la pince, la roue avant d'un vélo "
    "tenue dans la pince, et le câble d'alimentation qui vient du sol. Une petite flèche rouge : le verrou recule.", 43)


def croquis_gardienne(ident, titre, desc):
    """Le croquis du réglage : la gardienne appuie sur « + », le soleil se reflète sur l'écran."""
    W, H = 640, 430
    c = Crayon(57)
    h = []
    # le soleil, et ses reflets sur l'écran
    h.append(c.rond(55, 55, 22, ep=3.0, rempli="#ffe27a"))
    for k in range(8):
        a = math.radians(k * 45 + 10)
        h.append(c.trait([(55 + 30 * math.cos(a), 55 + 30 * math.sin(a)), (55 + 42 * math.cos(a), 55 + 42 * math.sin(a))],
                         ep=2.6, double=False, coul="#b98a00"))
    h.append(ecrit(55, 108, "le soleil", taille=13, ancre="middle", italique=True))
    # le boîtier sur son piquet
    h.append(c.trait([(276, 330), (276, 428)], ep=3.0))
    h.append(c.trait([(304, 330), (304, 428)], ep=3.0))
    h.append(c.trait([(170, 95), (410, 95), (410, 330), (170, 330)], ferme=True, ep=3.6, rempli="#eef3f8"))
    h.append(c.trait([(195, 118), (385, 118), (385, 192), (195, 192)], ferme=True, ep=2.6, rempli="#ffffff", double=False))
    h.append(c.trait([(86, 74), (212, 134)], ep=1.6, double=False, coul="#b98a00", tirets="7 6"))
    h.append(c.trait([(82, 86), (206, 160)], ep=1.6, double=False, coul="#b98a00", tirets="7 6"))
    h.append(ecrit(300, 156, "18:00", taille=34, ancre="middle", gras=True, halo=False))
    for (x1, y1, x2, y2) in ((202, 186, 226, 124), (214, 188, 240, 124), (228, 188, 248, 136)):
        h.append(c.trait([(x1, y1), (x2, y2)], ep=2.0, double=False, coul="#b9c3d3"))
    for (x, lib) in ((215, "−"), (290, "+"), (365, "OK")):
        h.append(c.rond(x, 262, 22, ep=2.8, rempli="#ffffff", double=False))
        h.append(ecrit(x, 263, lib, taille=20 if lib != "OK" else 15, ancre="middle", gras=True, halo=False))
    # la gardienne : la tête, une main en visière, le corps, le bras qui appuie
    h.append(c.trait([(548, 262), (520, 292), (510, 426)], ep=3.4))
    h.append(c.trait([(574, 262), (604, 292), (612, 426)], ep=3.4))
    h.append(c.rond(560, 232, 28, ep=3.0, rempli=PEAU))
    h.append(c.rond(586, 206, 12, ep=2.4, rempli="#3b2a20", double=False))
    h.append('<circle cx="543" cy="230" r="2.6" fill="%s"/>' % ENCRE)
    h.append(c.trait([(534, 236), (530, 244), (536, 246)], ep=2.0, double=False))
    h.append(c.trait([(522, 212), (548, 202), (574, 206)], ep=6.0, coul="#a77a5a", double=False))
    h.append(c.trait([(525, 300), (476, 378), (394, 314)], ep=3.2))
    h.append(c.trait([(540, 322), (488, 398), (384, 340)], ep=3.2))
    h.append(c.rond(370, 318, 26, 21, ep=2.8, rempli=PEAU, double=False))
    h.append(c.trait([(352, 300), (302, 266), (296, 274), (344, 310)], ferme=True, ep=2.4, rempli=PEAU, double=False))
    # la bulle : ce qu'elle ressent
    h.append(c.trait([(404, 112), (630, 112), (630, 172), (566, 172), (556, 198), (548, 172), (404, 172)], ferme=True,
                     ep=2.4, rempli="#ffffff", double=False))
    h.append(ecrit(517, 142, ["Le soleil sur l'écran :", "je ne vois presque rien !"], taille=14, ancre="middle", halo=False))
    # le geste : appuyer sur +, vingt-quatre fois
    h.append(c.fleche(452, 222, 308, 250, courbe=16))
    h.append(ecrit(470, 212, "× 24", taille=17, coul=ROUGE, gras=True))
    # les légendes
    h.append(ecrit(12, 183, ["l'écran passe", "de 6:00 à 18:00"], taille=14))
    h.append(fil(c, 124, 186, 197, 168))
    h.append(ecrit(12, 307, ["le bouton + :", "une demi-heure", "par appui"], taille=14))
    h.append(fil(c, 104, 291, 276, 281))
    return croquis_svg(ident, W, H, titre, desc, "".join(h))


GARDIENNE = croquis_gardienne(
    "cq-gardienne", "Un croquis possible : la gardienne règle l'heure d'arrosage",
    "Croquis à main levée, en gros plan. À gauche, le boîtier du jardin sur son piquet : un écran qui affiche 18:00 et "
    "trois boutons, moins, plus et OK. La main de la gardienne appuie sur le bouton plus ; une flèche rouge marquée « fois "
    "24 » montre l'appui répété. À droite, la tête de la gardienne, une main en visière au-dessus des yeux, et une bulle : "
    "« Le soleil sur l'écran : je ne vois presque rien ! ». En haut à gauche, le soleil, dont les rayons se reflètent sur "
    "l'écran. Légendes : l'écran passe de 6:00 à 18:00 ; le bouton plus, une demi-heure par appui.")


def _hachures_terre(c, x1, y1, x2, y2, pas=18):
    """La terre en coupe : une surface irrégulière et des hachures obliques."""
    h = [c.trait([(x1, y1), ((x1 + x2) / 2, y1 + 3), (x2, y1 - 2)], ep=2.4, coul=TERRE, double=False)]
    x = x1 + 6
    while x < x2 - 4:
        h.append(c.trait([(x, y2 - 4), (min(x + 26, x2 - 2), max(y2 - 30, y1 + 8))], ep=1.4, coul=TERRE, double=False, amp=0.6))
        h.append(c.trait([(x + 4, (y1 + y2) / 2 + 6), (min(x + 22, x2 - 2), (y1 + y2) / 2 - 14)], ep=1.4, coul=TERRE,
                         double=False, amp=0.6))
        x += pas + 8
    return "".join(h)


def croquis_capteur(ident, titre, desc):
    """Le croquis coté du capteur d'humidité (de face et de côté) et du bord du bac en coupe : les données de l'exercice 3."""
    W, H = 640, 400
    c = Crayon(73, amp=1.0)
    VERT = "#dcebd8"
    h = []
    # de face
    contour = [(90, 60), (150, 60), (150, 340), (143, 360), (136, 340), (136, 150), (104, 150), (104, 340), (97, 360), (90, 340)]
    h.append(c.trait(contour, ferme=True, ep=3.0, rempli=VERT))
    h.append(c.trait([(90, 135), (150, 135)], ep=1.6, double=False))
    h.append(c.trait([(108, 82), (132, 82), (132, 112), (108, 112)], ferme=True, ep=2.0, double=False, rempli="#ffffff"))
    h.append(c.trait([(106, 46), (134, 46), (134, 60), (106, 60)], ferme=True, ep=2.2, double=False, rempli="#ffffff"))
    h.append(c.trait([(134, 53), (170, 54), (196, 50), (214, 24)], ep=2.6, double=False))
    # de côté
    h.append(c.trait([(262, 60), (286, 60), (286, 135), (277, 135), (277, 350), (274, 360), (271, 350), (271, 135), (262, 135)],
                     ferme=True, ep=2.8, rempli=VERT))
    # niveau de la terre
    h.append(c.trait([(70, 180), (300, 180)], ep=1.6, double=False, coul=TERRE, tirets="8 6"))
    h.append(ecrit(306, 180, "niveau de la terre", taille=13, coul=TERRE, italique=True))
    # cotes du capteur
    h.append(cote(c, 90, 30, 150, 30, "20", attaches=[(90, 58, 90, 24), (150, 58, 150, 24)], tx=120, ty=17))
    h.append(cote(c, 58, 60, 58, 360, "100", attaches=[(88, 60, 50, 60), (95, 360, 50, 360)], tx=50, ty=210, ancre="end"))
    h.append(cote(c, 178, 60, 178, 135, "25", attaches=[(152, 60, 186, 60), (152, 135, 186, 135)], tx=186, ty=98, ancre="start"))
    h.append(cote(c, 178, 180, 178, 360, "60", attaches=[(152, 180, 186, 180), (145, 360, 186, 360)], tx=186, ty=272, ancre="start"))
    h.append(cote(c, 262, 30, 286, 30, "8", attaches=[(262, 58, 262, 24), (286, 58, 286, 24)], tx=274, ty=17))
    h.append(ecrit(120, 386, "de face", taille=13, ancre="middle", italique=True))
    h.append(ecrit(274, 386, "de côté", taille=13, ancre="middle", italique=True))
    h.append(ecrit(300, 98, ["tête : l'électronique,", "à garder au sec"], taille=14))
    h.append(fil(c, 296, 98, 287, 98))
    h.append(ecrit(300, 288, ["pointes : à enfoncer", "dans la terre"], taille=14))
    h.append(fil(c, 296, 288, 278, 288))
    # le bord du bac, en coupe
    h.append(ecrit(540, 46, "le bord du bac, en coupe", taille=14, ancre="middle", gras=True))
    h.append(_hachures_terre(c, 516, 240, 628, 392))
    h.append(c.trait([(450, 392), (450, 120), (516, 120), (516, 392)], ep=3.0, rempli="#f3e2c4"))
    h.append(c.trait([(468, 140), (472, 220), (466, 300), (470, 380)], ep=1.2, double=False, coul="#b08a55"))
    h.append(c.trait([(496, 150), (492, 240), (498, 330), (494, 388)], ep=1.2, double=False, coul="#b08a55"))
    h.append(cote(c, 450, 100, 516, 100, "22", attaches=[(450, 118, 450, 92), (516, 118, 516, 92)], tx=483, ty=86))
    h.append(cote(c, 606, 120, 606, 240, "40", attaches=[(518, 120, 614, 120), (596, 240, 614, 240)], tx=598, ty=180, ancre="end"))
    h.append(ecrit(444, 330, ["planche", "de pin"], taille=14, ancre="end"))
    h.append(fil(c, 446, 330, 468, 330))
    h.append(ecrit(572, 330, "terre", taille=14, ancre="middle", italique=True, coul=TERRE))
    h.append(ecrit(628, 386, "cotes en mm", taille=13, ancre="end", gras=True))
    return croquis_svg(ident, W, H, titre, desc, "".join(h))


CAPTEUR = croquis_capteur(
    "cq-capteur", "Croquis coté du capteur d'humidité et du bord du bac",
    "Croquis coté, à main levée, cotes en millimètres. À gauche, le capteur d'humidité vu de face : une tête rectangulaire, "
    "avec un petit composant et un connecteur d'où part un câble, prolongée vers le bas par deux pointes. Cotes : longueur "
    "totale 100 ; largeur 20 ; hauteur de la tête 25 ; les 60 derniers millimètres, sous le niveau de la terre, sont à "
    "enfoncer. Au milieu, le même capteur vu de côté : la tête a 8 millimètres d'épaisseur. Légendes : la tête, "
    "l'électronique, est à garder au sec ; les pointes sont à enfoncer dans la terre. À droite, le bord du bac en coupe : "
    "une planche de pin de 22 millimètres d'épaisseur ; la terre arrive 40 millimètres sous le haut de la planche.")


def croquis_support(ident, titre, desc):
    """Un croquis possible pour l'exercice 3 : un crochet qui s'enfile sur le bord du bac et tient le capteur dans une fente."""
    W, H = 640, 400
    c = Crayon(81, amp=1.0)
    h = []
    h.append(_hachures_terre(c, 186, 250, 628, 392))
    h.append(c.trait([(120, 392), (120, 130), (186, 130), (186, 392)], ep=3.0, rempli="#f3e2c4"))
    h.append(c.trait([(140, 150), (144, 250), (138, 380)], ep=1.2, double=False, coul="#b08a55"))
    h.append(c.trait([(166, 160), (162, 270), (168, 386)], ep=1.2, double=False, coul="#b08a55"))
    # le capteur
    h.append(c.trait([(327, 184), (341, 184), (341, 356), (338, 370), (335, 356), (335, 200), (333, 200), (333, 356), (330, 370),
                      (327, 356)], ferme=True, ep=2.2, rempli="#dcebd8", double=False))
    # le crochet
    crochet = [(102, 198), (102, 110), (352, 110), (352, 184), (316, 184), (316, 126), (202, 126), (202, 172), (188, 172),
               (188, 126), (118, 126), (118, 198)]
    h.append(c.trait(crochet, ferme=True, ep=3.2, rempli="#ffe3b0"))
    h.append(c.trait([(326, 110), (342, 110), (342, 184), (326, 184)], ferme=True, ep=1.6, double=False, tirets="5 4"))
    h.append(c.trait([(334, 110), (330, 92), (300, 84), (252, 88), (226, 72)], ep=2.4, double=False))
    # cotes
    h.append(cote(c, 118, 230, 188, 230, "24", attaches=[(118, 200, 118, 238), (188, 174, 188, 238)], tx=153, ty=216))
    h.append(cote(c, 188, 214, 352, 214, "55", attaches=[(352, 186, 352, 222)], tx=270, ty=202))
    # légendes
    h.append(ecrit(14, 58, ["crochet en PLA", "(imprimé en 3D)"], taille=14))
    h.append(fil(c, 72, 74, 108, 112))
    h.append(ecrit(394, 152, "fente 21 × 9", taille=14))
    h.append(fil(c, 390, 152, 353, 152))
    h.append(ecrit(14, 330, ["bord du bac", "(planche de 22)"], taille=14))
    h.append(fil(c, 116, 318, 140, 318))
    h.append(ecrit(420, 300, "capteur d'humidité", taille=14))
    h.append(fil(c, 416, 300, 342, 300))
    h.append(ecrit(540, 350, "terre", taille=14, ancre="middle", italique=True, coul=TERRE))
    # les flèches de montage
    h.append(c.fleche(150, 18, 150, 100))
    h.append(ecrit(166, 34, ["① on enfile le crochet", "sur le bord, vers le bas"], taille=14, coul=ROUGE, gras=True))
    h.append(c.fleche(380, 44, 380, 120))
    h.append(ecrit(394, 62, ["② puis le capteur glisse", "dans la fente"], taille=14, coul=ROUGE, gras=True))
    h.append(ecrit(628, 386, "cotes en mm", taille=13, ancre="end", gras=True))
    return croquis_svg(ident, W, H, titre, desc, "".join(h))


SUPPORT = croquis_support(
    "cq-support", "Un croquis possible : le crochet qui tient le capteur",
    "Croquis coté, en coupe, cotes en millimètres. Le bord du bac est une planche ; à sa droite, la terre. Un crochet en "
    "PLA, imprimé en 3D, s'enfile sur le haut de la planche : son ouverture mesure 24, pour une planche de 22. Il se "
    "prolonge par un bras au-dessus de la terre, long de 55 depuis la planche, qui se termine par un fourreau percé d'une "
    "fente de 21 sur 9. Le capteur d'humidité est glissé dans cette fente : sa tête reste dans le fourreau, ses pointes sont "
    "dans la terre. Deux flèches rouges de montage : 1, on enfile le crochet sur le bord, vers le bas ; 2, puis le capteur "
    "glisse dans la fente.")


# ─────────────────────────────────────────────────────────────────────────────
# Les dessins — 3e
# ─────────────────────────────────────────────────────────────────────────────
def _sirene(c, x0, y0):
    """Une sirène : un petit boîtier et un pavillon tourné vers la droite (vers le village)."""
    return "".join([c.trait([(x0 - 22, y0 - 11), (x0, y0 - 11), (x0, y0 + 11), (x0 - 22, y0 + 11)], ferme=True, ep=2.6,
                            rempli="#ffd9a8", double=False),
                    c.trait([(x0, y0 - 8), (x0 + 46, y0 - 22), (x0 + 46, y0 + 22), (x0, y0 + 8)], ferme=True, ep=2.8,
                            rempli="#ffd9a8"),
                    c.rond(x0 + 46, y0, 6, 22, ep=2.4, double=False)])


def _vent(c, ox, y=66):
    return c.fleche(ox + 22, y, ox + 88, y, ep=3.6, pointe=14) + ecrit(ox + 55, y - 16, "vent", taille=14, coul=ROUGE,
                                                                        gras=True, ancre="middle")


def croquis_sirene(ident, titre, desc):
    """Trois croquis rapides pour fixer la sirène sur le poteau : un corrigé possible de l'exercice 4."""
    W, H = 720, 420
    c = Crayon(97)
    h = []
    for k in (1, 2):
        h.append(c.trait([(240 * k, 14), (240 * k, 406)], ep=1.4, double=False, coul="#b9b2a0", tirets="6 6"))
    titres = ["collier serré", "platine au sommet", "bras en équerre"]
    for k in range(3):
        ox = 240 * k
        h.append(c.trait([(ox + 14, 400), (ox + 120, 402), (ox + 226, 399)], ep=2.4, double=False))
        h.append(pastille(ox + 24, 26, str(k + 1), r=14, taille=15))
        h.append(ecrit(ox + 46, 26, titres[k], taille=15, gras=True))
        h.append(_vent(c, ox))
    # ① collier
    ox = 0
    h.append(c.trait([(ox + 100, 400), (ox + 100, 92), (ox + 124, 92), (ox + 124, 400)], ep=3.0, rempli="#e3e7ec"))
    for y in (176, 204):
        h.append(c.trait([(ox + 96, y - 5), (ox + 140, y - 5), (ox + 140, y + 5), (ox + 96, y + 5)], ferme=True, ep=2.4,
                         double=False, rempli="#c9ced6"))
        h.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (ox + 134, y, ENCRE))
    h.append(c.trait([(ox + 140, 168), (ox + 150, 168), (ox + 150, 212), (ox + 140, 212)], ferme=True, ep=2.4, double=False,
                     rempli="#c9ced6"))
    h.append(_sirene(c, ox + 172, 190))
    h.append(ecrit(ox + 10, 252, ["collier serré", "par 2 boulons"], taille=13))
    h.append(fil(c, ox + 66, 238, ox + 98, 207))
    h.append(ecrit(ox + 196, 244, "sirène", taille=13, ancre="middle"))
    h.append(fil(c, ox + 196, 234, ox + 200, 210))
    h.append(cote(c, ox + 100, 320, ox + 124, 320, "Ø 60", tx=ox + 94, ty=320, ancre="end"))
    # ② platine au sommet
    ox = 240
    h.append(c.trait([(ox + 100, 400), (ox + 100, 190), (ox + 124, 190), (ox + 124, 400)], ep=3.0, rempli="#e3e7ec"))
    h.append(c.trait([(ox + 84, 180), (ox + 140, 180), (ox + 140, 190), (ox + 84, 190)], ferme=True, ep=2.6, double=False,
                     rempli="#c9ced6"))
    for x in (ox + 106, ox + 120):
        h.append(c.trait([(x, 168), (x, 180)], ep=2.6, double=False))
    h.append(_sirene(c, ox + 124, 157))
    h.append(ecrit(ox + 10, 124, ["platine vissée", "au sommet", "(4 vis)"], taille=13))
    h.append(fil(c, ox + 50, 146, ox + 88, 182))
    h.append(cote(c, ox + 152, 190, ox + 152, 400, "3 m", attaches=[(ox + 142, 190, ox + 160, 190)], tx=ox + 160, ty=300,
                  ancre="start"))
    # ③ bras en équerre
    ox = 480
    h.append(c.trait([(ox + 100, 400), (ox + 100, 110), (ox + 124, 110), (ox + 124, 400)], ep=3.0, rempli="#e3e7ec"))
    h.append(c.trait([(ox + 124, 140), (ox + 200, 140), (ox + 200, 150), (ox + 124, 150)], ferme=True, ep=2.6, double=False,
                     rempli="#c9ced6"))
    h.append(c.trait([(ox + 124, 214), (ox + 160, 150)], ep=3.2))
    h.append(_sirene(c, ox + 186, 161))
    h.append(cote(c, ox + 124, 122, ox + 200, 122, "50 cm", attaches=[(ox + 200, 138, ox + 200, 114)], tx=ox + 162, ty=106))
    h.append(ecrit(ox + 132, 262, ["bras + jambe", "de force"], taille=13))
    h.append(fil(c, ox + 150, 248, ox + 142, 184))
    return croquis_svg(ident, W, H, titre, desc, "".join(h))


SIRENE = croquis_sirene(
    "cq-sirene", "Trois croquis rapides pour fixer la sirène sur le poteau",
    "Trois croquis à main levée côte à côte, séparés par des pointillés, chacun avec une flèche rouge marquée « vent ». "
    "Solution 1, collier serré : la sirène est tenue sur le côté du poteau par deux colliers serrés par deux boulons ; une "
    "cote donne le diamètre du poteau, 60 millimètres. Solution 2, platine au sommet : une plaque est vissée en haut du "
    "poteau par quatre vis, et la sirène est posée dessus ; une cote donne la hauteur du poteau, 3 mètres. Solution 3, bras "
    "en équerre : un bras horizontal de 50 centimètres sort du poteau, renforcé par une jambe de force en biais ; la sirène "
    "est accrochée sous le bout du bras. Dans les trois croquis, le pavillon de la sirène est tourné vers la droite.")


def croquis_boitier(ident, titre, desc, complet=False):
    """Le croquis coté du boîtier de la station. Incomplet pour l'exercice 5 ; `complet` ajoute en rouge ce qui manquait.
    Les deux versions sont le même dessin, trait pour trait (même graine)."""
    W, H = 640, 470
    c = Crayon(113, amp=1.1)
    h = []
    face = [(140, 150), (404, 150), (404, 326), (140, 326)]
    dessus = [(140, 150), (404, 150), (451, 103), (187, 103)]
    cote_d = [(404, 150), (451, 103), (451, 279), (404, 326)]
    h.append(c.trait(dessus, ferme=True, ep=3.2, rempli="#eef1f5"))
    h.append(c.trait(cote_d, ferme=True, ep=3.2, rempli="#dde3ea"))
    h.append(c.trait(face, ferme=True, ep=3.4, rempli="#f6f8fb"))
    h.append(c.trait([(140, 164), (404, 164), (451, 117)], ep=1.8, double=False))
    for (x, y) in ((165, 141), (398, 141), (193, 112), (426, 112)):
        h.append(c.rond(x, y, 5, 3, ep=1.6, double=False, rempli="#ffffff"))
    # le trou du câble, caché dessous (pointillés), et le câble
    h.append(c.rond(216, 302, 9, 5, ep=1.8, double=False, tirets="4 3"))
    h.append(c.trait([(216, 302), (216, 326)], ep=2.4, double=False, tirets="4 3"))
    h.append(c.trait([(216, 326), (222, 352), (210, 384), (218, 420), (212, 462)], ep=2.8, double=False))
    # titre et cotes présentes
    h.append(ecrit(20, 28, "Boîtier de la station — croquis coté", taille=16, gras=True))
    h.append(ecrit(20, 50, "cotes en mm", taille=14))
    h.append(cote(c, 110, 150, 110, 326, "80", attaches=[(138, 150, 102, 150), (138, 326, 102, 326)], tx=100, ty=238, ancre="end"))
    h.append(cote(c, 187, 78, 451, 78, "120", attaches=[(187, 101, 187, 70), (451, 101, 451, 70)], tx=319, ty=64))
    h.append(ecrit(478, 96, ["couvercle fixé", "par 4 vis de 4 mm"], taille=14))
    h.append(fil(c, 474, 100, 429, 112))
    h.append(ecrit(20, 398, ["trou pour le câble,", "sur le dessous"], taille=14))
    h.append(fil(c, 150, 392, 208, 306))
    if complet:
        h.append(ecrit(620, 28, "en rouge : ce qui manquait", taille=14, coul=ROUGE, gras=True, ancre="end"))
        h.append(cote(c, 414, 336, 461, 289, "60", attaches=[(406, 328, 418, 340), (453, 281, 465, 293)], tx=452, ty=328,
                      ancre="start"))
        h.append(ecrit(478, 200, ["matériau :", "polycarbonate,", "parois de 3 mm"], taille=14, coul=ROUGE, gras=True))
        h.append(fil(c, 474, 204, 440, 212, coul=ROUGE))
        h.append(ecrit(546, 344, "vue de dessous", taille=14, coul=ROUGE, gras=True, ancre="middle"))
        h.append(c.trait([(480, 358), (612, 358), (612, 424), (480, 424)], ferme=True, ep=2.6, coul=ROUGE, double=False))
        h.append(c.rond(524, 391, 7, ep=2.2, coul=ROUGE, double=False))
        h.append(ecrit(538, 391, "Ø 12", taille=14, coul=ROUGE, gras=True))
        h.append(cote(c, 480, 442, 524, 442, "40", attaches=[(480, 426, 480, 450), (524, 400, 524, 450)], tx=502, ty=458))
    return croquis_svg(ident, W, H, titre, desc, "".join(h))


BOITIER = croquis_boitier(
    "cq-boitier", "Croquis coté du boîtier de la station, à vérifier",
    "Croquis coté, à main levée, d'un boîtier en forme de pavé, dessiné en perspective : on voit sa face avant, son dessus "
    "et son côté droit. Titre : boîtier de la station, croquis coté ; cotes en millimètres. Deux cotes seulement : la "
    "longueur, 120, et la hauteur, 80. Aucune cote sur la profondeur. Une légende : couvercle fixé par 4 vis de 4 "
    "millimètres. Une autre : trou pour le câble, sur le dessous — le trou est dessiné en pointillés, car on ne voit pas "
    "le dessous ; un câble en sort vers le bas. Aucun matériau n'est écrit.")

BOITIER_COMPLET = croquis_boitier(
    "cq-boitier-c", "Le croquis coté du boîtier, complété",
    "Le même croquis coté du boîtier, avec en rouge ce qui manquait : la cote de profondeur, 60 ; le matériau, "
    "polycarbonate, avec des parois de 3 millimètres ; et une vue de dessous, qui montre le trou du câble, de diamètre 12, "
    "placé à 40 millimètres du bord gauche.", complet=True)


def quatre_vues(ident, titre, desc):
    """La même station d'alerte, montrée de quatre façons, numérotées sans être nommées (exercice 6)."""
    W, H = 760, 310
    c = Crayon(131)
    h = []
    for k in (1, 2, 3):
        h.append(c.trait([(190 * k, 14), (190 * k, 296)], ep=1.4, double=False, coul="#b9b2a0", tirets="6 6"))
    for k in range(4):
        h.append(pastille(190 * k + 24, 26, str(k + 1), r=14, taille=15))
    # ① un croquis
    ox = 0
    h.append(c.trait([(ox + 14, 290), (ox + 100, 292), (ox + 176, 289)], ep=2.4, double=False))
    h.append(c.trait([(ox + 80, 290), (ox + 80, 92), (ox + 96, 92), (ox + 96, 290)], ep=2.8, rempli="#e3e7ec"))
    h.append(c.trait([(ox + 76, 145), (ox + 106, 145), (ox + 106, 155), (ox + 76, 155)], ferme=True, ep=2.2, double=False))
    h.append(_sirene(c, ox + 128, 150))
    h.append(c.fleche(ox + 30, 70, ox + 80, 70, ep=3.4, pointe=13))
    h.append(ecrit(ox + 55, 56, "vent", taille=13, coul=ROUGE, gras=True, ancre="middle"))
    h.append(ecrit(ox + 150, 206, "sirène", taille=13, ancre="middle"))
    h.append(fil(c, ox + 150, 196, ox + 152, 172))
    h.append(cote(c, ox + 80, 250, ox + 96, 250, "Ø 60", tx=ox + 74, ty=250, ancre="end", taille=13))
    # ② un schéma électrique : des symboles, des traits droits
    ox = 190
    L = '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>'
    for seg in ((ox + 40, 110, ox + 80, 110), (ox + 112, 110, ox + 150, 110), (ox + 150, 110, ox + 150, 166),
                (ox + 150, 196, ox + 150, 250), (ox + 150, 250, ox + 98, 250), (ox + 86, 250, ox + 40, 250),
                (ox + 40, 250, ox + 40, 110)):
        h.append(L % (seg + (ENCRE,)))
    h.append('<circle cx="%.1f" cy="110" r="3" fill="%s"/><circle cx="%.1f" cy="110" r="3" fill="%s"/>' % (ox + 80, ENCRE, ox + 112, ENCRE))
    h.append(L % (ox + 80, 110, ox + 108, 94, ENCRE))
    h.append(L % (ox + 86, 234, ox + 86, 266, ENCRE))
    h.append('<line x1="%.1f" y1="242" x2="%.1f" y2="258" stroke="%s" stroke-width="5"/>' % (ox + 98, ox + 98, ENCRE))
    h.append('<rect x="%.1f" y="166" width="20" height="30" fill="#ffffff" stroke="%s" stroke-width="2.2"/>' % (ox + 140, ENCRE))
    h.append('<path d="M%.1f,172 L%.1f,160 L%.1f,202 L%.1f,190 Z" fill="#ffffff" stroke="%s" stroke-width="2.2"/>'
             % (ox + 160, ox + 176, ox + 176, ox + 160, ENCRE))
    h.append(ecrit(ox + 96, 82, "interrupteur", taille=13, ancre="middle"))
    h.append(ecrit(ox + 92, 282, "batterie 12 V", taille=13, ancre="middle"))
    h.append(ecrit(ox + 134, 214, "sirène", taille=13, ancre="end"))
    # ③ une modélisation en 3D : des arêtes nettes, des faces ombrées, les trois axes
    ox = 380
    def p(x, y):
        return "%.1f,%.1f" % (ox + x, y)
    O, A, B, C_ = (95, 200), (147, 230), (121, 245), (69, 215)
    def haut(q):
        return (q[0], q[1] - 40)
    faces = [([haut(O), haut(A), haut(B), haut(C_)], "#e8eef6"), ([haut(C_), haut(B), B, C_], "#c9d6e6"),
             ([haut(B), haut(A), A, B], "#a9bcd4")]
    for pts, coul in faces:
        h.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.8" stroke-linejoin="round"/>'
                 % (" ".join(p(*q) for q in pts), coul, ENCRE))
    h.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.2"/>'
             % (" ".join(p(*q) for q in [(69, 181), (121, 211), (147, 196)]), ENCRE))
    h.append('<rect x="%.1f" y="60" width="160" height="214" rx="6" fill="none" stroke="#8a97ad" stroke-width="1.4"/>' % (ox + 15))
    h.append('<rect x="%.1f" y="60" width="160" height="16" rx="6" fill="#d5dbe5"/>' % (ox + 15))
    for i, (dx, dy, coul, lettre) in enumerate(((28, 16, "#b3261e", "x"), (-28, 16, "#16753a", "y"), (0, -32, "#1f5fbf", "z"))):
        h.append('<line x1="%.1f" y1="258" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (ox + 44, ox + 44 + dx * 0.8, 258 + dy * 0.8, coul))
        h.append(ecrit(ox + 44 + dx, 258 + dy, lettre, taille=12, coul=coul, gras=True, ancre="middle", halo=False))
    # ④ un graphique
    ox = 570
    h.append(L % (ox + 40, 250, ox + 40, 92, ENCRE))
    h.append(L % (ox + 40, 250, ox + 176, 250, ENCRE))
    h.append('<path d="M%.1f,86 l-5,10 h10 z M%.1f,250 l-10,-5 v10 z" fill="%s"/>' % (ox + 40, ox + 182, ENCRE))
    h.append('<line x1="%.1f" y1="154" x2="%.1f" y2="154" stroke="%s" stroke-width="1.6" stroke-dasharray="6 5"/>' % (ox + 40, ox + 176, ROUGE))
    h.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>'
             % (" ".join("%.1f,%.1f" % (ox + x, y) for x, y in ((40, 232), (58, 228), (78, 218), (98, 204), (118, 178),
                                                                    (138, 146), (158, 124), (172, 116))), "#1f5fbf"))
    h.append(ecrit(ox + 46, 84, "vent (km/h)", taille=12.5))
    h.append(ecrit(ox + 34, 154, "90", taille=12, ancre="end", coul=ROUGE))
    h.append(ecrit(ox + 34, 250, "0", taille=12, ancre="end"))
    h.append(ecrit(ox + 44, 266, "18 h", taille=12, ancre="middle"))
    h.append(ecrit(ox + 108, 266, "minuit", taille=12, ancre="middle"))
    h.append(ecrit(ox + 170, 266, "6 h", taille=12, ancre="middle"))
    h.append(ecrit(ox + 108, 286, "heure de la nuit", taille=12, ancre="middle", italique=True))
    return croquis_svg(ident, W, H, titre, desc, "".join(h))


QUATRE = quatre_vues(
    "cq-quatre", "La station d'alerte, montrée de quatre façons",
    "Quatre dessins numérotés de 1 à 4, côte à côte, sans leur nom. Dessin 1 : à main levée, le poteau, la sirène fixée "
    "par un collier, une flèche rouge marquée vent, une légende « sirène » et une cote « diamètre 60 ». Dessin 2 : des "
    "traits droits et des symboles reliés en boucle — une batterie de 12 volts, un interrupteur ouvert, une sirène. "
    "Dessin 3 : un boîtier en volume, aux arêtes nettes et aux faces ombrées, dans une fenêtre d'ordinateur, avec trois "
    "petits axes notés x, y et z. Dessin 4 : deux axes ; en vertical, le vent en kilomètres par heure ; en horizontal, "
    "l'heure de la nuit, de 18 heures à 6 heures ; une courbe qui monte et dépasse une ligne pointillée marquée 90.")
