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


def _figure(svg_txt, legende, description=None):
    """Une figure posée dans un texte (consigne, correction), avec sa description en mots — même forme que les documents."""
    h = '<figure class="figure">%s<figcaption>%s</figcaption></figure>' % (svg_txt, legende)
    if description:
        h += '<details class="description"><summary>📝 Ce que montre le croquis, en mots</summary>%s</details>' % description
    return h


# ─────────────────────────────────────────────────────────────────────────────
# 4e — du témoignage au croquis (4e_C2.1), proposer par un croquis coté (4e_C7.2)
# ─────────────────────────────────────────────────────────────────────────────
TEMOIN_INES = ("<p><b>Inès&nbsp;:</b> « J'approche ma carte du lecteur, sous l'écran. La borne bipe et le voyant passe au vert. "
               "Là, je tire le vélo en arrière, vers moi, pour le sortir de la pince. La première fois, j'ai poussé au lieu "
               "de tirer&nbsp;: rien ne bougeait, j'ai cru que c'était cassé&nbsp;! »</p>")

E1 = dict(
    id="e1", titre="Du témoignage au croquis : lequel est le bon ?", code="4e_C2.1", duree=10,
    objectif="relier ce que raconte un usager à un croquis, dire ce qui ne va pas dans un croquis, et retrouver ce qui fait "
             "un croquis réussi.",
    production="le choix du bon croquis, la raison des deux autres, et les règles d'un croquis réussi.",
    mots=[("croquis", "un dessin rapide, fait à main levée, qui montre l'essentiel. On dit souvent « croquis à main levée »."),
          ("à main levée", "sans règle ni compas : le crayon suit la main. Les traits peuvent trembler, ce n'est pas un défaut."),
          ("légende", "quelques mots écrits à côté du dessin, reliés par un trait à ce qu'ils nomment."),
          ("flèche de mouvement", "une flèche qui montre un geste ou un déplacement, et son sens : on tire, on pousse, on tourne…"),
          ("témoignage", "ce qu'une personne raconte, avec ses mots, de ce qu'elle a fait et ressenti."),
          ("lecteur de carte", "la zone de la borne contre laquelle on pose sa carte pour être reconnu."),
          ("voyant", "une petite lampe qui s'allume pour donner une information (vert : c'est bon).")],
    intro="<p>Sur le front de mer, une <b>borne</b> prête des vélos. Inès raconte comment elle en prend un&nbsp;:</p>" + TEMOIN_INES +
          "<p>Trois élèves ont fait un <b>croquis</b> de ce témoignage.</p>"
          + _figure(BORNE_A, "Croquis A.", "<p>Inès est debout à côté de la borne ; le vélo est tenu par sa roue avant dans une "
                    "pince. Légende 1 : je pose ma carte sur le lecteur. Légende 2 : la borne bipe, le voyant passe au vert. "
                    "Légende 3, en rouge, au-dessus d'une flèche rouge qui part du vélo et s'éloigne de la borne : je tire le "
                    "vélo en arrière, vers moi.</p>")
          + _figure(BORNE_B, "Croquis B.", "<p>Le même dessin que le A, avec les mêmes légendes 1 et 2. Seule la flèche rouge "
                    "change : elle va vers la borne. Légende 3 : je pousse le vélo vers la borne.</p>")
          + _figure(BORNE_C, "Croquis C.", "<p>La borne ouverte, vue de l'intérieur, sans personne : une carte électronique, "
                    "l'antenne du lecteur, des fils, le verrou de la pince qui tient la roue avant, le câble d'alimentation. Une "
                    "petite flèche rouge : le verrou recule.</p>"),
    consigne="<p>Un <b>croquis</b> — on dit souvent <b>croquis à main levée</b> — est un dessin rapide qui montre l'essentiel. "
             "Ses <b>légendes</b> sont des mots reliés au dessin par un trait ; une <b>flèche de mouvement</b> montre un geste et "
             "son sens.</p>"
             "<p><b>Choisis le croquis qui montre comment on sort un vélo de la borne, comme Inès le raconte.</b> Puis <b>dis ce "
             "qui ne va pas</b> dans les deux autres, et <b>coche ce qui rend le bon croquis réussi</b>.</p>",
    critere="tu choisis le bon croquis, tu donnes la bonne raison pour chacun des deux autres, et tu coches les quatre règles "
            "d'un croquis réussi — et rien d'autre.",
    widgets=[dict(type="choix", name="bon",
                  legende="Quel croquis montre comment on sort un vélo de la borne, comme Inès le raconte&nbsp;?",
                  options=[("A", "Le croquis A."), ("B", "Le croquis B."), ("C", "Le croquis C."),
                           ("aucun", "Aucun des trois&nbsp;: il faudrait une photo.")],
                  bonne="A",
                  retours={"A": "Oui : la carte sur le lecteur, le bip et le voyant, puis la flèche qui tire le vélo en arrière, "
                                "dans l'ordre du témoignage.",
                           "B": "Le croquis B montre bien un moment du témoignage, mais c'est l'erreur de la première fois : sa "
                                "flèche pousse le vélo vers la borne.",
                           "C": "Le croquis C montre l'intérieur de la borne : on n'y voit ni Inès, ni son geste.",
                           "aucun": "Une photo montrerait tout, même l'inutile. Un croquis choisit ce qu'il montre : ici, le geste "
                                    "et son sens."}),
             dict(type="classer", name="defaut",
                  categories=[("sens", "sa flèche montre le contraire du bon geste"),
                              ("dedans", "il montre l'intérieur de l'objet, sans l'usager ni son geste"),
                              ("legende", "il n'a aucune légende"),
                              ("rien", "rien&nbsp;: il correspond aussi au témoignage")],
                  items=[("Croquis B — ce qui ne va pas", "sens",
                          "Croquis B : regarde le sens de la flèche rouge, puis relis la fin du témoignage."),
                         ("Croquis C — ce qui ne va pas", "dedans", "Croquis C : cherche Inès et son geste.")]),
             dict(type="cases", name="regles", legende="Le croquis A est réussi. Coche ce qui le rend réussi.",
                  options=[("legendes", "des légendes, chacune reliée par un trait à ce qu'elle nomme"),
                           ("numeros", "des numéros qui donnent l'ordre des étapes, comme dans le témoignage"),
                           ("fleche", "une flèche de mouvement en rouge, avec ce qu'elle veut dire écrit à côté"),
                           ("formes", "des formes simples&nbsp;: des rectangles, des ronds, un bonhomme"),
                           ("regle", "des traits bien droits, tracés à la règle"),
                           ("echelle", "des proportions exactes&nbsp;: la borne, le vélo et Inès sont à l'échelle"),
                           ("couleurs", "beaucoup de couleurs, pour que ce soit beau"),
                           ("interieur", "l'intérieur de la borne, pour être complet")],
                  bonnes=["legendes", "numeros", "fleche", "formes"],
                  retours={"regle": "Les traits du croquis A tremblent, et il est réussi quand même : un croquis se fait à main levée.",
                           "echelle": "Dans le croquis A, rien n'est à l'échelle — et on comprend tout. Un croquis n'a pas besoin "
                                      "des vraies proportions.",
                           "couleurs": "Le croquis A n'a presque que du noir et un peu de rouge, doublé de mots : la couleur ne "
                                       "fait pas la réussite.",
                           "interieur": "L'intérieur de la borne n'aide pas à comprendre le geste d'Inès : un croquis choisit ce "
                                        "qu'il montre."},
                  indice="Pour chaque proposition, demande-toi : est-ce que le croquis A l'a vraiment ? Et est-ce que cela aide "
                         "à comprendre le geste ?")],
    aides=["<p>Relis le témoignage et repère les verbes d'action&nbsp;: <i>approcher</i> la carte, la borne <i>bipe</i>, "
           "<i>tirer</i> le vélo. Cherche ces trois moments dans chaque croquis. Pour la flèche, demande-toi&nbsp;: <b>vers où va le "
           "vélo&nbsp;?</b></p>",
           "<p>Le témoignage → trois moments → la carte sur le lecteur, puis le bip et le voyant, puis <b>tirer</b> le vélo en "
           "arrière.<br>"
           "A → la carte ✔ → le bip ✔ → la flèche s'éloigne de la borne ✔ → c'est le bon.<br>"
           "B → la carte ✔ → le bip ✔ → la flèche va vers la borne ✘ → c'est l'erreur de la première fois.<br>"
           "C → ni Inès, ni geste ✘ → il montre comment la borne est faite, pas ce que vit l'usager.</p>"
           "<p><b>Ce qui fait réussir A</b> → des légendes reliées, des numéros dans l'ordre, une flèche expliquée, des formes "
           "simples. Pas la règle, pas l'échelle, pas les couleurs.</p>"],
    jumeau=dict(consigne="Hugo raconte&nbsp;: « Je glisse mon ticket dans la fente, la barrière se lève, j'avance. » Un croquis "
                         "montre la barrière levée et une flèche qui fait <b>reculer</b> la voiture, sans aucune légende. Qu'est-ce "
                         "qui ne va pas, et comment le corriger&nbsp;?",
                correction="La <b>flèche de mouvement</b> va dans le mauvais sens&nbsp;: Hugo <b>avance</b>. On la retourne, vers la "
                           "barrière levée. Il manque aussi les <b>légendes</b>&nbsp;: « ticket dans la fente », relié à la fente par "
                           "un trait, et « j'avance » à côté de la flèche."),
    correction=[
        "<b>Le témoignage, en trois moments&nbsp;:</b> la carte sur le lecteur → le bip et le voyant vert → tirer le vélo en arrière, vers soi.",
        "<b>Croquis A</b> → la carte ✔ → le bip et le voyant ✔ → la flèche rouge s'éloigne de la borne ✔ → <b>il correspond au témoignage</b>",
        "<b>Croquis B</b> → la carte ✔ → le bip ✔ → la flèche va <b>vers</b> la borne ✘ → il montre l'erreur de la première fois "
        "(« j'ai poussé »), pas le geste qui marche",
        "<b>Croquis C</b> → l'intérieur de la borne (carte électronique, antenne, verrou) → <b>ni Inès, ni son geste</b> ✘ → il dit "
        "comment la borne fonctionne, pas ce que vit l'usager",
        "« Aucun, il faudrait une photo » ne tient pas&nbsp;: une photo montre tout, même l'inutile&nbsp;; le croquis A garde "
        "l'essentiel et le rend lisible.",
        "Pour B et C, « aucune légende » est faux (ils en ont), et « rien » aussi&nbsp;: B inverse le geste, C ne le montre pas.",
        "<b>Ce qui rend A réussi&nbsp;:</b> des légendes reliées par un trait ✔ → des numéros dans l'ordre ✔ → une flèche de "
        "mouvement expliquée ✔ → des formes simples ✔",
        "<b>Ce qui ne compte pas&nbsp;:</b> des traits droits, l'échelle → un croquis se fait à main levée ✘ → les couleurs et "
        "l'intérieur de la borne → ils n'aident pas à comprendre le geste ✘",
        ("conclusion", "Un croquis d'usage montre <b>la personne, l'objet et le geste</b>, dans l'ordre où l'usager le vit. On le "
                       "juge à ce qu'il fait comprendre, pas à sa beauté."),
    ],
    retenir="un croquis <b>choisit</b> ce qu'il montre&nbsp;: pour l'expérience d'un usager, la personne, l'objet et le geste, "
            "avec des légendes et une flèche de mouvement dans le bon sens.",
    piege="choisir le croquis le plus « technique » (l'intérieur de la borne) ou le plus soigné, au lieu de celui qui montre ce "
          "que vit l'usager.",
)

E2 = dict(
    id="e2", titre="Dessiner le geste de la gardienne", code="4e_C2.1", duree=12,
    objectif="passer d'un témoignage, écrit en langage naturel, à un croquis qui montre le geste de l'usager et ce qu'il ressent.",
    production="un croquis légendé du réglage de l'heure d'arrosage, relu avec la liste.",
    mots=[("langage naturel", "la langue de tous les jours, celle qu'on parle et qu'on écrit — par opposition aux schémas, aux "
           "graphiques et aux algorithmes."),
          ("ressenti", "ce que la personne éprouve en utilisant l'objet&nbsp;: gêne, fatigue, surprise, plaisir…"),
          ("facilité d'usage", "le fait qu'un objet se serve sans effort, sans erreur et sans perdre de temps."),
          ("bulle", "dans un croquis, comme en bande dessinée&nbsp;: ce que la personne dit, pense ou ressent."),
          ("reflet", "la lumière du soleil renvoyée par l'écran, qui empêche de lire."),
          ("en visière", "la main posée au-dessus des yeux, pour faire de l'ombre.")],
    intro="<p>Le jardin partagé du collège a un <b>système d'arrosage connecté</b>. Mme Joseph, la gardienne, raconte comment elle "
          "règle l'heure d'arrosage sur le boîtier&nbsp;:</p>"
          "<p><b>Mme Joseph&nbsp;:</b> « En fin d'après-midi, j'ouvre le petit capot du boîtier. L'écran affiche 6:00, mais je veux "
          "arroser à 18:00, quand il fait moins chaud. J'appuie sur le bouton +&nbsp;: chaque appui avance d'une demi-heure, alors "
          "j'appuie, j'appuie… vingt-quatre fois&nbsp;! Puis j'appuie sur OK, et le boîtier bipe deux fois. Le pire, c'est le "
          "soleil&nbsp;: il se reflète sur l'écran, je dois mettre ma main en visière pour lire. »</p>",
    consigne="<p>Ce témoignage est écrit en <b>langage naturel</b>&nbsp;: les mots de tous les jours. Ton travail&nbsp;: le traduire "
             "en un <b>croquis</b> — un dessin rapide, à main levée — que l'on comprendrait sans lire le texte.</p>"
             "<p><b>Coche d'abord ce que ton croquis doit montrer.</b> Puis <b>dessine-le</b> dans la zone de dessin (au doigt, au "
             "stylet ou à la souris)&nbsp;: des <b>légendes</b> (des mots reliés au dessin par un trait), une <b>flèche de "
             "mouvement</b> pour le geste, une <b>bulle</b> pour ce que ressent Mme Joseph. Pas besoin de savoir « bien » "
             "dessiner&nbsp;: un rond pour la tête, un rectangle pour le boîtier suffisent. <b>Relis-le enfin avec la liste.</b></p>",
    critere="tu coches les cinq éléments utiles et seulement eux&nbsp;; ton croquis montre la personne, le boîtier, le geste par "
            "une flèche, au moins deux légendes, et ce que la gardienne voit ou ressent.",
    widgets=[dict(type="cases", name="montrer", legende="Dans le témoignage, qu'est-ce que ton croquis doit montrer&nbsp;?",
                  options=[("personne", "Mme Joseph, ou au moins sa main et sa tête"),
                           ("boitier", "le boîtier, avec son écran et ses boutons"),
                           ("geste", "le geste&nbsp;: appuyer sur +, plusieurs fois"),
                           ("voit", "ce qu'elle voit&nbsp;: l'écran qui passe de 6:00 à 18:00"),
                           ("ressent", "ce qu'elle ressent&nbsp;: le reflet du soleil qui l'empêche de lire"),
                           ("circuit", "les fils et la carte électronique, à l'intérieur du boîtier"),
                           ("cuve", "la cuve d'eau de pluie, au fond du jardin"),
                           ("prix", "la marque et le prix du boîtier")],
                  bonnes=["personne", "boitier", "geste", "voit", "ressent"],
                  retours={"circuit": "Mme Joseph ne voit pas l'intérieur du boîtier : pour son expérience, il ne compte pas.",
                           "cuve": "La cuve sert à l'arrosage, mais elle ne joue aucun rôle dans le geste du réglage.",
                           "prix": "Le prix ne se dessine pas, et il ne dit rien du geste ni du ressenti."},
                  indice="Garde ce que Mme Joseph fait, voit et ressent pendant le réglage ; laisse ce qu'elle ne voit pas ou "
                         "qui ne joue pas dans le geste."),
             dict(type="croquis", name="croquis", label="Mon croquis&nbsp;: Mme Joseph règle l'heure d'arrosage",
                  checklist=["la personne (Mme Joseph, ou au moins sa main et sa tête)",
                             "l'objet&nbsp;: le boîtier, avec son écran et ses boutons",
                             "le geste, montré par une flèche de mouvement",
                             "au moins deux légendes, chacune reliée par un trait",
                             "ce que la personne voit ou ressent (une bulle, un mot, un signe)"],
                  minTraits=6,
                  vide="Ton croquis est encore presque vide : commence par les grandes formes — un rectangle pour le boîtier, "
                       "un rond pour la tête.")],
    aides=["<p>Commence par les grandes formes&nbsp;: un rectangle pour le boîtier, trois ronds pour les boutons, un rond pour la "
           "tête de Mme Joseph. Ajoute le geste (une flèche vers le bouton +), puis les mots. Le témoignage a trois parties&nbsp;: "
           "ce qu'elle <b>fait</b>, ce qu'elle <b>voit</b>, ce qu'elle <b>ressent</b>.</p>",
           "<p>Ce qu'elle fait → appuyer 24 fois sur + → une flèche rouge vers le bouton, et « × 24 ».<br>"
           "Ce qu'elle voit → l'écran → une légende « 6:00 → 18:00 ».<br>"
           "Ce qu'elle ressent → le soleil sur l'écran → une bulle « je ne vois rien&nbsp;! », ou une main en visière.<br>"
           "Ce qu'on laisse de côté → l'intérieur du boîtier, la cuve, le prix&nbsp;: ils ne disent rien de son expérience.</p>"],
    jumeau=dict(consigne="Léo raconte&nbsp;: « Pour recharger ma trottinette, je soulève le cache en caoutchouc, je branche le "
                         "chargeur, et le voyant devient orange. Le cache est si dur que je me casse un ongle à chaque fois. » "
                         "Décris en mots le croquis que tu ferais&nbsp;: ce qu'on voit, les légendes, la flèche, la bulle.",
                correction="La <b>personne</b> (au moins sa main) et la <b>trottinette</b>, avec son cache et sa prise&nbsp;; une "
                           "<b>flèche</b> qui soulève le cache, une autre qui enfonce le chargeur&nbsp;; des <b>légendes</b> « cache "
                           "en caoutchouc », « voyant orange »&nbsp;; une <b>bulle</b> « aïe, mon ongle&nbsp;! » pour le ressenti. "
                           "Le moteur et la batterie, à l'intérieur, n'y sont pas."),
    correction=[
        _figure(GARDIENNE, "Un croquis possible. Le tien peut être très différent&nbsp;: ce qui compte, c'est que les cinq "
                "éléments y soient.", "<p>Le boîtier sur son piquet, un écran qui affiche 18:00 et trois boutons. La main de "
                "la gardienne appuie sur le bouton plus ; une flèche rouge marquée « fois 24 ». À droite, sa tête, une main "
                "en visière, et une bulle : « Le soleil sur l'écran : je ne vois presque rien ! ». Le soleil se reflète sur "
                "l'écran. Légendes : l'écran passe de 6:00 à 18:00 ; le bouton plus, une demi-heure par appui.</p>"),
        "<b>À montrer</b> → la personne, le boîtier, le geste, ce qu'elle voit, ce qu'elle ressent → les cinq viennent du témoignage",
        "<b>À laisser de côté</b> → l'intérieur du boîtier (elle ne le voit pas) → la cuve (elle ne joue pas dans le réglage) → "
        "le prix (il ne se dessine pas)",
        "<b>Le geste</b> → appuyer sur + → une flèche rouge vers le bouton, et « × 24 »&nbsp;: de 6:00 à 18:00, cela fait 12 "
        "heures, soit 24 demi-heures, donc 24 appuis",
        "<b>Ce qu'elle voit</b> → une légende « l'écran passe de 6:00 à 18:00 », reliée à l'écran par un trait",
        "<b>Ce qu'elle ressent</b> → une bulle « je ne vois presque rien&nbsp;! », ou la main en visière et les rayons du soleil "
        "sur l'écran",
        "<b>Deux légendes au moins</b> → « bouton + », « écran »… → chacune reliée par un trait à ce qu'elle nomme",
        "<b>Ce que le croquis fait voir</b> → 24 appuis, c'est long → l'écran se lit mal au soleil → deux pistes pour "
        "améliorer le boîtier&nbsp;: un bouton qui avance d'une heure, un écran qui ne reflète pas",
        ("conclusion", "Le croquis garde du témoignage ce que vit l'usager — ce qu'il <b>fait</b>, <b>voit</b> et <b>ressent</b> — "
                       "et laisse le reste. De ce croquis, on passera ensuite à un schéma ou à un algorithme du réglage."),
    ],
    retenir="pour passer du témoignage au croquis, on cherche ce que la personne <b>fait</b>, <b>voit</b> et <b>ressent</b>&nbsp;: "
            "le geste devient une flèche, ce qu'elle voit une légende, le ressenti une bulle.",
    piege="dessiner l'objet seul, sans la personne ni son geste&nbsp;: on obtient un dessin du boîtier, pas l'expérience de la "
          "gardienne.",
)

E3 = dict(
    id="e3", titre="Proposer par un croquis coté : le support du capteur", code="4e_C7.2", duree=15,
    objectif="proposer une pièce nouvelle par un croquis coté&nbsp;: sa forme, comment elle tient, ses dimensions, son matériau, "
             "son montage.",
    production="un croquis coté du support du capteur, relu avec la liste, et sa description en deux phrases.",
    mots=[("croquis coté", "un croquis qui porte des cotes&nbsp;: on peut fabriquer la pièce à partir de lui."),
          ("cote", "une dimension écrite sur le croquis&nbsp;: une ligne avec une pointe à chaque bout, et un nombre avec son "
           "unité (ou une seule mention « cotes en mm » pour tout le croquis)."),
          ("capteur d'humidité", "la pièce à deux pointes que l'on plante dans la terre&nbsp;: elle mesure si la terre est sèche "
           "ou mouillée."),
          ("flèche de montage", "une flèche qui montre dans quel sens on met la pièce en place."),
          ("matériau", "ce dans quoi la pièce est faite&nbsp;: bois, plastique, métal…"),
          ("PLA (acide polylactique)", "le plastique le plus courant des imprimantes 3D, fabriqué à partir de plantes comme le maïs."),
          ("3D (trois dimensions)", "en volume&nbsp;: avec une longueur, une largeur et une hauteur."),
          ("jeu", "le petit espace laissé entre deux pièces pour qu'elles s'emboîtent sans forcer.")],
    documents=[dict(svg=CAPTEUR, legende="Le croquis coté du capteur d'humidité et du bord du bac (cotes en mm).",
                    description="<ul><li><b>Le capteur, de face</b> — longueur totale 100 mm&nbsp;; largeur 20 mm&nbsp;; la tête, en "
                                "haut, mesure 25 mm&nbsp;; les 60 derniers millimètres des pointes sont à enfoncer dans la terre.</li>"
                                "<li><b>Le capteur, de côté</b> — la tête a 8 mm d'épaisseur. La tête (l'électronique) doit rester "
                                "au sec.</li>"
                                "<li><b>Le bord du bac, en coupe</b> — une planche de pin de 22 mm d'épaisseur&nbsp;; la terre arrive "
                                "40 mm sous le haut de la planche.</li></ul>")],
    intro="<p>Le système d'arrosage n'arrose que si la terre est sèche&nbsp;: il lit un <b>capteur d'humidité</b> planté dans le "
          "bac. Mais le capteur bouge — un coup d'arrosoir, un coup de pied — et ses mesures deviennent fausses. On veut "
          "<b>ajouter une fonction</b> au jardin&nbsp;: <b>tenir le capteur droit, à la bonne profondeur, sans qu'il bouge</b>.</p>",
    consigne="<p>Tu vas <b>proposer une solution par un croquis coté</b>&nbsp;: un croquis qui porte des <b>cotes</b> — des dimensions, "
             "avec leur unité — pour qu'on puisse fabriquer la pièce. Tu inventes la pièce&nbsp;: un crochet, une pince, un piquet… "
             "à toi de voir.</p>"
             "<p><b>Coche d'abord les règles justes du croquis coté.</b> Puis <b>dessine ta pièce</b>&nbsp;: comment elle tient au "
             "bac, au moins une cote, le matériau écrit, et une <b>flèche de montage</b> (le sens dans lequel on la met en place). "
             "<b>Décris-la enfin en deux phrases.</b></p>",
    critere="tu coches les trois règles justes&nbsp;; ton croquis montre la pièce, comment elle tient, une cote, le matériau et la "
            "flèche de montage&nbsp;; ta description dit comment la pièce tient, donne une dimension avec son unité et nomme le "
            "matériau.",
    widgets=[dict(type="cases", name="regles", legende="Les règles du croquis coté&nbsp;: coche les phrases justes.",
                  options=[("unite", "Une cote s'écrit avec son unité — ou une seule mention « cotes en mm » pour tout le croquis."),
                           ("sans_unite", "Une cote peut s'écrire sans unité&nbsp;: celui qui fabrique devinera."),
                           ("main", "Un croquis coté se trace à main levée&nbsp;: ce sont les cotes qui donnent les vraies dimensions."),
                           ("regle", "Un croquis coté se trace à la règle et à l'échelle, sinon ses cotes sont fausses."),
                           ("materiau", "Le matériau s'écrit sur le croquis, dans une légende."),
                           ("plus_tard", "Le matériau ne s'écrit jamais sur un croquis&nbsp;: on le choisit après la fabrication.")],
                  bonnes=["unite", "main", "materiau"],
                  retours={"sans_unite": "« 22 », c'est 22 mm ou 22 cm ? Sans unité, la pièce peut sortir dix fois trop grande.",
                           "regle": "Le croquis du capteur est à main levée, et ses cotes sont justes : le dessin donne la forme, "
                                    "les cotes donnent les dimensions.",
                           "plus_tard": "On choisit le matériau AVANT de fabriquer : il décide de la machine (imprimante 3D, "
                                        "scie…) et de la tenue à l'eau."},
                  indice="Les règles vont par deux : pour chaque paire, une seule phrase est juste."),
             dict(type="croquis", name="croquis", label="Mon croquis coté&nbsp;: le support du capteur d'humidité",
                  checklist=["la pièce que j'invente, en entier",
                             "comment elle tient au bac (crochet, pince, vis, piquet…)",
                             "au moins une cote, avec son unité",
                             "le matériau, écrit dans une légende",
                             "la flèche de montage&nbsp;: dans quel sens on la met en place"],
                  minTraits=6,
                  vide="Ton croquis est encore presque vide : dessine d'abord le bord du bac (un rectangle), puis ta pièce."),
             dict(type="texte", name="desc", lignes=3,
                  label="Décris ta pièce en deux phrases&nbsp;: comment elle tient, et pourquoi le capteur ne bouge plus.",
                  criteres=[dict(label="tu dis comment la pièce tient au bac ou dans la terre",
                                 motifs=["croch", "pince", "clip", r"\bvis", "viss", "serr", "encoch", "fente", "accroch", "coinc",
                                         "enfonc", "emboit", "plant", "pique", "colle", "aimant", "bord", "glisse", "fourreau",
                                         "attache"],
                                 manque="Dis comment ta pièce TIENT : elle s'accroche au bord ? elle se plante ? elle se visse ?"),
                            dict(label="tu donnes une dimension, avec son unité",
                                 motifs=[r"\d+([,.]\d+)?\s*(mm|cm|millim|centim)"],
                                 manque="Donne au moins une dimension, avec son unité : « 24 mm », « 5 cm »…"),
                            dict(label="tu nommes le matériau",
                                 motifs=[r"\bpla\b", "plastique", "bois", "alumin", "metal", "acier", "inox", "caoutchouc",
                                         "bambou", r"\bfer\b", r"\bpvc\b"],
                                 manque="Nomme le matériau de ta pièce : plastique (PLA), bois, aluminium…")],
                  etayage=["Ma pièce est un … en … (matériau), qui tient au bac par …",
                           "Le capteur ne bouge plus parce que … ; la cote la plus importante est … mm."],
                  exemple="Ma pièce est un crochet en PLA qui s'accroche sur le bord du bac : son ouverture mesure 24 mm, pour "
                          "une planche de 22 mm. Le capteur glisse dans une fente du bras, il est serré et ne bouge plus quand "
                          "on arrose.")],
    aides=["<p>Pars des données du croquis coté&nbsp;: la planche fait 22 mm, la tête du capteur 20 mm sur 8 mm. Ta pièce doit "
           "faire deux choses&nbsp;: <b>tenir au bac</b>, et <b>tenir le capteur</b>. Dessine d'abord le bord du bac (un rectangle), "
           "puis ta pièce par-dessus.</p>",
           "<p>Tenir au bac → par exemple un crochet qui coiffe la planche → son ouverture&nbsp;: 22 mm, plus un peu de jeu → 24 mm.<br>"
           "Tenir le capteur → un bras au-dessus de la terre, avec une fente à la taille de la tête → 20 × 8 mm, donc une fente de "
           "21 × 9 mm.<br>"
           "Le matériau → la pièce reste dehors, sous l'arrosage → du PLA, du bois traité, de l'aluminium.<br>"
           "La flèche de montage → le crochet s'enfile de haut en bas, puis le capteur glisse dans la fente.</p>"],
    jumeau=dict(consigne="Mme Joseph veut accrocher son tuyau d'arrosage, enroulé, au poteau du jardin — un poteau carré de 70 mm "
                         "de côté. Décris en mots le croquis coté de ta pièce&nbsp;: sa forme, comment elle tient, une cote, le "
                         "matériau, la flèche de montage.",
                correction="Par exemple&nbsp;: une <b>équerre en aluminium</b>, vissée sur le poteau par deux vis, avec un bras de "
                           "<b>15 cm</b> sur lequel on pose le tuyau enroulé&nbsp;; une <b>flèche</b> montre que le tuyau se pose "
                           "par-dessus. Autre réponse juste&nbsp;: un collier en acier inox, de 70 mm de côté à l'intérieur, serré "
                           "autour du poteau."),
    correction=[
        _figure(SUPPORT, "Un croquis possible. D'autres solutions sont justes&nbsp;: un piquet planté à côté du capteur, une pince "
                "sur le bord…", "<p>Le bord du bac en coupe et la terre. Un crochet en PLA, imprimé en 3D, coiffe la planche : "
                "ouverture 24 pour une planche de 22. Un bras de 55 au-dessus de la terre se termine par un fourreau percé d'une "
                "fente de 21 sur 9, où le capteur est glissé : la tête dans le fourreau, les pointes dans la terre. Deux flèches "
                "de montage : d'abord on enfile le crochet sur le bord, vers le bas ; puis le capteur glisse dans la fente.</p>"),
        "<b>Les règles justes</b> → une cote a son unité ✔ → le croquis coté se trace à main levée, les cotes donnent les "
        "dimensions ✔ → le matériau s'écrit sur le croquis ✔",
        "<b>Les règles fausses</b> → « sans unité »&nbsp;: 22 mm ou 22 cm&nbsp;? ✘ → « à la règle et à l'échelle »&nbsp;: le croquis du "
        "capteur est à main levée, et ses cotes sont justes ✘ → « le matériau après »&nbsp;: il décide de la machine et de la "
        "tenue à l'eau, on le choisit avant ✘",
        "<b>Tenir au bac</b> → un crochet qui coiffe le bord → ouverture <b>24 mm</b> pour une planche de 22 mm (2 mm de jeu pour "
        "l'enfiler)",
        "<b>Tenir le capteur</b> → un bras au-dessus de la terre, terminé par une fente de <b>21 × 9 mm</b> pour une tête de "
        "20 × 8 mm → le capteur est serré, il ne bouge plus",
        "<b>La bonne profondeur</b> → la terre est 40 mm sous le haut de la planche, le capteur mesure 100 mm → si sa tête est au "
        "niveau du haut de la planche, 100 − 40 = <b>60 mm</b> de pointes plongent dans la terre, et la tête reste au sec",
        "<b>Le matériau</b> → du PLA, imprimé en 3D&nbsp;: il ne rouille pas et ne pourrit pas sous l'arrosage",
        "<b>Le montage</b> → d'abord on enfile le crochet sur le bord, vers le bas → puis on glisse le capteur dans la fente",
        "<b>Une description attendue&nbsp;:</b> « Ma pièce est un crochet en PLA qui coiffe le bord du bac&nbsp;; son ouverture mesure "
        "24 mm. Le capteur glisse dans une fente de 21 mm&nbsp;: il est serré et ne bouge plus quand on arrose. »",
        ("conclusion", "Un croquis coté suffit pour proposer et fabriquer une pièce simple&nbsp;: la forme à main levée, les "
                       "<b>cotes</b> avec leur unité, le <b>matériau</b>, et la <b>flèche de montage</b>."),
    ],
    retenir="un <b>croquis coté</b> permet de fabriquer&nbsp;: la forme à main levée, des <b>cotes</b> avec leur unité, le "
            "<b>matériau</b> écrit, et une flèche qui dit comment on monte la pièce.",
    piege="oublier l'unité des cotes, ou croire qu'un croquis coté doit être tracé à la règle&nbsp;: ce sont les cotes, pas le "
          "trait, qui donnent les dimensions.",
)

# ─────────────────────────────────────────────────────────────────────────────
# 3e — proposer plusieurs solutions, lire un croquis coté, choisir sa représentation (3e_C7.2)
# ─────────────────────────────────────────────────────────────────────────────
E4 = dict(
    id="e4", titre="Trois croquis rapides pour fixer la sirène", code="3e_C7.2", duree=13,
    objectif="proposer plusieurs solutions vraiment différentes par des croquis rapides, puis en choisir une avec des raisons.",
    production="trois croquis légendés dans la même zone de dessin, et le choix argumenté de l'un d'eux.",
    mots=[("solution", "une façon de répondre au besoin. Deux solutions sont vraiment différentes quand leur principe change, "
           "pas seulement un détail."),
          ("principe", "l'idée qui fait marcher la solution&nbsp;: serrer autour du poteau, poser dessus, accrocher à un bras…"),
          ("variante", "la même solution avec un détail changé (une vis de plus, une autre couleur)."),
          ("rafale", "un coup de vent brutal et court, plus fort que le vent moyen."),
          ("galvanisé", "recouvert de zinc pour ne pas rouiller."),
          ("collier", "un anneau en deux parties qui serre autour d'un tube, fermé par des boulons."),
          ("platine", "une plaque fixée au bout d'un tube, sur laquelle on visse autre chose."),
          ("Ø", "le symbole du diamètre&nbsp;: la largeur d'un rond, mesurée en passant par son centre.")],
    intro="<p>La <b>station d'alerte cyclonique</b> du collège doit faire entendre sa sirène dans tout le quartier. Il faut fixer la "
          "sirène sur le poteau de la station. Le cahier des charges dit&nbsp;:</p>"
          "<ul><li><b>Le poteau</b>&nbsp;: un tube d'acier galvanisé de 60 mm de diamètre et de 3 m de haut.</li>"
          "<li><b>La sirène</b>&nbsp;: elle pèse 4 kg, et son pavillon doit être tourné vers les maisons.</li>"
          "<li><b>Le vent</b>&nbsp;: la fixation doit tenir face aux rafales d'un cyclone, jusqu'à 250 km/h, et se démonter pour "
          "l'entretien.</li>"
          "<li><b>L'air salé</b>&nbsp;: la station est près de la mer, rien ne doit rouiller.</li></ul>",
    consigne="<p>Avant de choisir, on cherche <b>plusieurs solutions</b>. Une solution est <b>vraiment différente</b> d'une autre quand "
             "son <b>principe</b> change (serrer autour du poteau, poser dessus, accrocher à un bras…), pas quand on ajoute une vis.</p>"
             "<p><b>Dessine trois croquis rapides</b>, côte à côte dans la zone de dessin, numérotés 1, 2 et 3 — environ trois minutes "
             "chacun. Sur chacun, au moins une <b>légende</b>, et une <b>flèche</b> qui montre d'où vient le vent&nbsp;; sur l'un d'eux "
             "au moins, une <b>cote</b>. Puis <b>dis laquelle tu gardes, et pourquoi</b>.</p>",
    critere="trois solutions de principes différents, numérotées et légendées, une flèche pour le vent, une cote&nbsp;; un choix "
            "qui nomme la solution gardée et donne deux raisons, dont une liée au vent.",
    widgets=[dict(type="croquis", name="trois", label="Mes trois croquis rapides&nbsp;: fixer la sirène sur le poteau",
                  checklist=["trois solutions de principes vraiment différents, numérotées 1, 2, 3",
                             "chacune a au moins une légende",
                             "une flèche montre d'où vient le vent",
                             "au moins une cote, avec son unité"],
                  minTraits=12,
                  vide="Il faut trois croquis : pour chacun, deux traits pour le poteau, un cornet pour la sirène, puis la "
                       "fixation."),
             dict(type="texte", name="choix", lignes=3,
                  label="Laquelle gardes-tu&nbsp;? Donne deux raisons, dont une liée au vent.",
                  criteres=[dict(label="tu dis quelle solution tu gardes",
                                 motifs=[r"\b(solution|croquis|numero)\s*(n°\s*)?[123]\b", r"\b[123]\b",
                                         r"\b(premiere|deuxieme|seconde|troisieme)\b", "collier", "platine", "potence",
                                         "hauban", r"\bbras\b", "equerre", "sangle", "plaque", "cerclage"],
                                 manque="Dis quelle solution tu gardes : son numéro, ou son nom (collier, platine, bras…)."),
                            dict(label="une raison est liée au vent", motifs=["vent", "rafale", "cyclone", "arrach", "souffl",
                                                                               "tempete", "ouragan"],
                                 manque="Donne une raison liée au vent : pourquoi ta fixation tiendra-t-elle sous les rafales ?"),
                            dict(label="une deuxième raison (démontage, rouille, montage, son, coût…)",
                                 motifs=["demont", "entretien", "rouill", r"\bsel\b", r"\bsale\b", "corros", "inox", "galvanis",
                                         "prix", "cout", "cher", "poids", "leger", "lourd", "montage", "monter", "install",
                                         "simple", "facile", "rapide", r"\bson\b", "maison", "entend", "orient", "fabriqu",
                                         "outil", r"\bcle\b"],
                                 manque="Ajoute une deuxième raison, prise dans le cahier des charges : le démontage, la rouille, "
                                        "le son vers les maisons…")],
                  etayage=["Je garde la solution … (le …), parce que face au vent …",
                           "Deuxième raison : …"],
                  exemple="Je garde la solution 1, le collier serré par deux boulons : la sirène reste près du poteau, donc le "
                          "vent du cyclone ne peut pas l'arracher. Et on la démonte avec une seule clé pour l'entretien.")],
    aides=["<p>Trois principes pour démarrer&nbsp;: <b>serrer</b> quelque chose autour du poteau&nbsp;; <b>poser</b> la sirène sur le "
           "haut du poteau&nbsp;; <b>accrocher</b> la sirène au bout d'un bras. Dessine vite&nbsp;: un poteau, ce sont deux traits&nbsp;; "
           "une sirène, un cornet. Trois minutes par croquis, pas plus.</p>",
           "<p>Pour comparer, reprends le cahier des charges ligne par ligne.<br>"
           "Le vent → la sirène offre une prise au vent → plus elle est loin du poteau, plus elle force sur la fixation → un bras "
           "long est risqué, un collier serré près du poteau tient mieux.<br>"
           "Le démontage → des boulons ou des vis, pas de soudure.<br>"
           "Le sel → de l'acier galvanisé ou inoxydable.<br>"
           "Ton choix → la solution qui répond au plus de lignes, avec deux raisons écrites.</p>"],
    jumeau=dict(consigne="Il faut aussi fixer le petit panneau solaire de la station sur le même poteau. Donne trois principes de "
                         "fixation vraiment différents, en une ligne chacun, et dis lequel tu gardes.",
                correction="Par exemple&nbsp;: un <b>collier</b> serré autour du poteau, avec une équerre inclinée&nbsp;; une "
                           "<b>platine</b> au sommet du poteau, le panneau posé dessus&nbsp;; un <b>cadre au sol</b>, à côté du "
                           "poteau. On peut garder le collier&nbsp;: le panneau reste près du poteau, le vent a peu de prise, et il "
                           "se démonte avec une clé. Les deux autres choix sont justes aussi, s'ils sont argumentés."),
    correction=[
        _figure(SIRENE, "Trois croquis possibles, de trois principes différents. Les tiens peuvent être autres.",
                "<p>Solution 1, collier serré : la sirène est tenue sur le côté du poteau par deux colliers à boulons ; cote : "
                "diamètre du poteau 60. Solution 2, platine au sommet : une plaque vissée en haut du poteau, la sirène posée "
                "dessus ; cote : hauteur du poteau 3 m. Solution 3, bras en équerre : un bras de 50 cm renforcé par une jambe de "
                "force, la sirène accrochée sous son bout. Chaque croquis a une flèche rouge marquée vent.</p>"),
        "<b>Solution 1, le collier serré</b> → principe&nbsp;: serrer autour du poteau → la sirène reste tout près du poteau → le "
        "vent a peu de prise sur la fixation → elle se démonte avec une clé",
        "<b>Solution 2, la platine au sommet</b> → principe&nbsp;: poser sur le haut du poteau → solide, et la sirène domine le "
        "quartier → mais tout l'effort du vent passe par quatre vis",
        "<b>Solution 3, le bras en équerre</b> → principe&nbsp;: accrocher au bout d'un bras → la sirène s'éloigne du poteau → le "
        "vent force beaucoup plus sur la fixation&nbsp;: il faut une jambe de force",
        "<b>Trois croquis qui n'en font qu'un</b> → un collier, puis un collier à trois boulons, puis un collier peint → c'est une "
        "seule solution et ses variantes, pas trois solutions",
        "<b>Le vent, la cote, les légendes</b> → la flèche « vent » dit contre quoi la fixation doit tenir → une cote (Ø 60, 3 m, "
        "50 cm) donne une dimension → les légendes nomment les pièces",
        "<b>Un choix attendu&nbsp;:</b> « Je garde la solution 1, le collier serré par deux boulons&nbsp;: la sirène reste près du "
        "poteau, donc le vent du cyclone ne peut pas l'arracher. Et on la démonte avec une seule clé pour l'entretien. »",
        ("conclusion", "Proposer, en 3e, c'est faire <b>plusieurs croquis rapides, de principes différents</b>, les comparer avec "
                       "le cahier des charges, puis choisir en disant pourquoi. D'autres choix sont justes s'ils sont argumentés."),
    ],
    retenir="on ne choisit bien qu'entre <b>plusieurs</b> solutions&nbsp;: des croquis rapides, de principes vraiment différents, "
            "comparés ligne par ligne avec le cahier des charges.",
    piege="dessiner trois fois la même solution avec un détail en plus&nbsp;: ce sont des variantes, pas trois solutions.",
)

E5 = dict(
    id="e5", titre="Lire un croquis coté : peut-on fabriquer ce boîtier ?", code="3e_C7.2", duree=10,
    objectif="lire un croquis coté et repérer ce qui manque pour fabriquer la pièce.",
    production="la réponse à « est-ce que ça rentre&nbsp;? », la liste des manques, et un message au dessinateur.",
    mots=[("perçage", "un trou fait dans une pièce&nbsp;; pour le fabriquer, il faut son diamètre et sa place."),
          ("vue", "la façon dont on regarde la pièce pour la dessiner&nbsp;: de face, de dessus, de dessous, en perspective…"),
          ("perspective", "un dessin qui montre plusieurs faces à la fois, pour donner l'idée du volume."),
          ("pointillés", "dans un dessin technique, un trait en pointillés montre ce qui est caché derrière une face."),
          ("coffret", "la petite armoire fixée au poteau, où l'on range le boîtier pour le protéger."),
          ("polycarbonate", "un plastique très résistant aux chocs et au soleil.")],
    documents=[dict(svg=BOITIER, legende="Le croquis coté du boîtier de la station, envoyé par le dessinateur.",
                    description="<ul><li><b>Ce qu'on voit</b> — un boîtier en forme de pavé, en perspective&nbsp;: la face avant, "
                                "le dessus, le côté droit.</li>"
                                "<li><b>Ce qui est écrit</b> — le titre&nbsp;; « cotes en mm »&nbsp;; la longueur, 120&nbsp;; la hauteur, "
                                "80&nbsp;; « couvercle fixé par 4 vis de 4 mm »&nbsp;; « trou pour le câble, sur le dessous ».</li>"
                                "<li><b>Le trou du câble</b> — dessiné en pointillés, car le dessous ne se voit pas&nbsp;; un câble "
                                "en sort vers le bas.</li></ul>")],
    intro="<p>Le dessinateur de l'équipe a fait le <b>croquis coté</b> du boîtier qui protégera la carte électronique de la station. "
          "Avant de lancer la fabrication, tu le vérifies&nbsp;: celui qui fabrique ne doit avoir <b>aucune question à poser</b>.</p>",
    consigne="<p>Pour fabriquer une pièce, il faut trouver sur son croquis coté <b>toutes ses dimensions</b> (longueur, hauteur, "
             "profondeur), leur <b>unité</b>, le <b>matériau</b>, et chaque <b>perçage</b> — un trou&nbsp;: son diamètre et sa place —, "
             "sur une <b>vue</b> qui le montre.</p>"
             "<p><b>Réponds d'abord&nbsp;: le boîtier entre-t-il dans le coffret&nbsp;?</b> Puis <b>coche tout ce qui manque</b> pour le "
             "fabriquer, et <b>écris le message</b> que tu envoies au dessinateur.</p>",
    critere="tu vois qu'on ne peut pas savoir si le boîtier entre, tu coches les quatre manques et rien d'autre, et ton message "
            "demande la profondeur et un autre manque, par des questions précises.",
    widgets=[dict(type="choix", name="rentre",
                  legende="Le boîtier doit entrer dans le coffret du poteau, dont l'intérieur mesure 130 × 90 × 70 mm. Avec ce "
                          "croquis, peut-on savoir s'il entre&nbsp;?",
                  options=[("non", "Non&nbsp;: la profondeur n'est pas cotée, on ne peut pas comparer la troisième dimension."),
                           ("oui", "Oui&nbsp;: 120 mm est plus petit que 130 mm, et 80 mm plus petit que 90 mm."),
                           ("trop", "Non&nbsp;: il est trop grand, car 120 mm et 80 mm, cela fait 200 mm."),
                           ("jamais", "Non&nbsp;: un croquis à main levée ne donne jamais de dimensions fiables.")],
                  bonne="non",
                  retours={"non": "Oui : 120 < 130 et 80 < 90, mais la profondeur n'est écrite nulle part. On ne peut pas conclure.",
                           "oui": "Deux dimensions sur trois seulement : la profondeur n'est pas cotée. Si elle dépasse 70 mm, le "
                                  "boîtier n'entre pas.",
                           "trop": "On compare chaque dimension à celle du coffret qui lui fait face ; on n'additionne pas une "
                                   "longueur et une hauteur.",
                           "jamais": "Les cotes sont fiables même sur un croquis à main levée : 120 et 80 sont de vraies "
                                     "dimensions. Le problème, c'est celle qui manque."}),
             dict(type="cases", name="manques", legende="Qu'est-ce qui manque pour fabriquer ce boîtier&nbsp;?",
                  options=[("profondeur", "la profondeur du boîtier (une cote)"),
                           ("materiau", "le matériau"),
                           ("diametre", "le diamètre du trou du câble"),
                           ("vue", "une vue du dessous, qui montre où est ce trou"),
                           ("unite", "l'unité des cotes"),
                           ("hauteur", "la hauteur du boîtier"),
                           ("regle", "des traits tracés à la règle"),
                           ("ombres", "des ombres et des couleurs, pour faire plus vrai")],
                  bonnes=["profondeur", "materiau", "diametre", "vue"],
                  retours={"unite": "Elle y est : « cotes en mm », sous le titre.",
                           "hauteur": "Elle y est : 80, sur le côté gauche.",
                           "regle": "La main levée ne gêne pas la fabrication : ce sont les cotes qui donnent les dimensions.",
                           "ombres": "Des ombres ne donnent aucune dimension : elles n'aident pas à fabriquer."},
                  indice="Fais comme celui qui fabrique : pour chaque face, « quelle longueur ? » ; pour le trou, « quel diamètre, "
                         "et où ? » ; et « en quoi ? »."),
             dict(type="texte", name="message", lignes=4,
                  label="Écris ton message au dessinateur&nbsp;: au moins deux manques, chacun avec une question précise.",
                  criteres=[dict(label="tu demandes la profondeur", motifs=["profond", "epaisseur du boitier", "troisieme dimension"],
                                 manque="Demande la cote qui manque : la profondeur du boîtier."),
                            dict(label="tu demandes un autre manque (le matériau, le trou du câble, une vue du dessous)",
                                 motifs=["materiau", "matiere", "plastique", r"\bmetal", r"\btrou", "percage", "diametre", "dessous",
                                         r"\bvue\b"],
                                 manque="Demande un deuxième manque : le matériau, le diamètre du trou, une vue du dessous."),
                            dict(label="tu poses des questions précises",
                                 motifs=[r"\?", r"\bquel", "combien", "peux-tu", "pourrais", "indique", "ajoute", "precise",
                                         "merci de"],
                                 manque="Pose de vraies questions : « Quelle est… ? », « Peux-tu ajouter… ? »")],
                  etayage=["Bonjour ! Quelle est la … du boîtier, en mm ?",
                           "Peux-tu aussi ajouter … ?"],
                  exemple="Bonjour ! Quelle est la profondeur du boîtier, en mm ? Quel matériau as-tu choisi ? Et peux-tu ajouter "
                          "une vue du dessous, avec le diamètre et la place du trou du câble ?")],
    aides=["<p>Fais comme celui qui fabrique&nbsp;: pour chaque face, demande-toi « quelle longueur&nbsp;? ». Pour le trou&nbsp;: "
           "« quel diamètre&nbsp;? où exactement&nbsp;? ». Puis cherche le mot qui dit en quoi est le boîtier.</p>",
           "<p>Longueur → 120 ✔. Hauteur → 80 ✔. Profondeur → aucune cote ✘ → impossible de savoir si le boîtier entre (il "
           "faudrait moins de 70 mm).<br>"
           "Unité → « cotes en mm » ✔. Matériau → écrit nulle part ✘.<br>"
           "Le trou du câble → en pointillés, car il est dessous, caché → ni son diamètre, ni sa place ✘ → il faut une vue du "
           "dessous ✘.<br>"
           "Les traits à main levée, l'absence d'ombres → ils ne gênent pas la fabrication.</p>"],
    jumeau=dict(consigne="Le croquis coté d'une étagère indique&nbsp;: « longueur 80 cm, profondeur 25 cm, planche de pin ». "
                         "Qu'est-ce qui manque pour la fabriquer et la fixer au mur&nbsp;?",
                correction="Il manque l'<b>épaisseur</b> de la planche et, pour la fixer, les <b>perçages</b>&nbsp;: leur diamètre "
                           "et leur place. L'unité et le matériau, eux, y sont."),
    correction=[
        _figure(BOITIER_COMPLET, "Le croquis complété&nbsp;: en rouge, ce qui manquait.",
                "<p>Le même croquis, avec en rouge : la cote de profondeur, 60 ; le matériau, polycarbonate, parois de 3 mm ; "
                "une vue de dessous qui montre le trou du câble, de diamètre 12, à 40 mm du bord gauche.</p>"),
        "<b>Est-ce que ça rentre&nbsp;?</b> → 120 < 130 ✔ → 80 < 90 ✔ → la profondeur&nbsp;? pas de cote → <b>on ne peut pas savoir</b>",
        "Les trois autres réponses ne tiennent pas&nbsp;: « oui » oublie la troisième dimension&nbsp;; on n'additionne pas une "
        "longueur et une hauteur&nbsp;; les cotes d'un croquis à main levée sont fiables.",
        "<b>Ce qui manque</b> → la profondeur → le matériau → le diamètre du trou du câble → une vue du dessous, qui montre où "
        "est ce trou",
        "<b>Ce qui y est déjà</b> → l'unité (« cotes en mm ») → la longueur, 120 → la hauteur, 80 → le titre",
        "<b>Ce qui ne manque pas</b> → des traits à la règle, des ombres → ils ne donnent aucune dimension",
        "<b>Une fois complété</b> → profondeur 60 → 120 < 130, 80 < 90, 60 < 70 → <b>le boîtier entre</b>, avec 10 mm de marge "
        "dans chaque direction",
        "<b>Un message attendu&nbsp;:</b> « Quelle est la profondeur du boîtier, en mm&nbsp;? Quel matériau as-tu choisi&nbsp;? Peux-tu "
        "ajouter une vue du dessous, avec le diamètre et la place du trou du câble&nbsp;? »",
        ("conclusion", "Un croquis coté est bon quand celui qui fabrique n'a <b>aucune question à poser</b>&nbsp;: toutes les "
                       "dimensions, leur unité, le matériau, et chaque perçage sur une vue qui le montre."),
    ],
    retenir="pour fabriquer, un croquis coté doit donner <b>les trois dimensions</b>, leur <b>unité</b>, le <b>matériau</b> et "
            "chaque <b>perçage</b> (diamètre et place), sur une vue qui le montre.",
    piege="conclure « ça rentre » en ne comparant que les dimensions écrites&nbsp;: une cote qui manque empêche de conclure.",
)

REPRESENTATIONS = [("croquis", "un croquis"), ("schema", "un schéma"), ("graphique", "un graphique"),
                   ("algorithme", "un algorithme"), ("modelisation", "une modélisation 3D")]

E6 = dict(
    id="e6", titre="Du croquis au schéma ou à la modélisation", code="3e_C7.2", duree=12,
    objectif="reconnaître les modes de représentation d'un même objet, et choisir le bon selon ce que l'on veut faire.",
    production="le nom des quatre vues, le bon choix pour cinq besoins, et une explication écrite.",
    mots=[("schéma", "un dessin normé&nbsp;: des symboles que tout le monde lit de la même façon, reliés par des traits droits. Il "
           "montre comment c'est relié, pas à quoi cela ressemble."),
          ("normé", "qui suit une règle commune, la même pour tous&nbsp;: un symbole normé se lit pareil partout."),
          ("graphique", "des axes et une courbe&nbsp;: comment une grandeur change, par exemple au fil du temps."),
          ("algorithme", "une suite d'instructions dans l'ordre, avec des conditions (si… alors… sinon…)."),
          ("modélisation 3D", "la pièce dessinée en volume dans un logiciel, avec ses dimensions exactes&nbsp;; une machine peut la "
           "fabriquer à partir du fichier."),
          ("simulation", "faire « fonctionner » un modèle dans un logiciel, pour prévoir comment l'objet se comportera."),
          ("prototype", "un premier exemplaire, fabriqué pour essayer la solution en vrai.")],
    documents=[dict(svg=QUATRE, legende="La station d'alerte, montrée de quatre façons.",
                    description="<ul><li><b>Vue 1</b> — à main levée&nbsp;: le poteau, la sirène tenue par un collier, une flèche "
                                "rouge « vent », une légende, une cote « Ø 60 ».</li>"
                                "<li><b>Vue 2</b> — des traits droits et des symboles reliés en boucle&nbsp;: une batterie de 12 V, un "
                                "interrupteur ouvert, une sirène.</li>"
                                "<li><b>Vue 3</b> — un boîtier en volume, aux arêtes nettes et aux faces ombrées, dans une fenêtre "
                                "d'ordinateur, avec trois petits axes x, y, z.</li>"
                                "<li><b>Vue 4</b> — deux axes, le vent en km/h et l'heure de la nuit&nbsp;; une courbe qui monte et "
                                "dépasse une ligne pointillée marquée 90.</li></ul>")],
    intro="<p>Le programme de technologie cite cinq façons de représenter une solution&nbsp;: le <b>croquis</b>, le <b>schéma</b>, le "
          "<b>graphique</b>, l'<b>algorithme</b> et la <b>modélisation</b>. Chacune répond à une question différente.</p>",
    consigne="<p>Un <b>croquis</b> se fait vite, à main levée, pour montrer une idée. Un <b>schéma</b> utilise des symboles "
             "<b>normés</b> (les mêmes pour tous) pour montrer comment c'est relié. Un <b>graphique</b> montre comment une grandeur "
             "change. Un <b>algorithme</b> dit l'ordre des actions. Une <b>modélisation 3D</b> donne la forme exacte, en volume, "
             "dans un logiciel.</p>"
             "<p><b>Nomme chacune des quatre vues de la station.</b> Puis <b>choisis la représentation qui convient à chaque "
             "besoin</b>, et <b>explique</b> pourquoi on n'envoie pas le croquis directement à l'imprimante 3D.</p>",
    critere="neuf réponses justes, et une explication qui parle des dimensions exactes et du fichier dont la machine a besoin.",
    widgets=[dict(type="classer", name="vues", categories=REPRESENTATIONS,
                  items=[("Vue 1", "croquis", "Vue 1 : le trait tremble, il y a des légendes et une flèche — un dessin fait vite, à main levée."),
                         ("Vue 2", "schema", "Vue 2 : des symboles reliés par des traits droits — on voit comment c'est relié."),
                         ("Vue 3", "modelisation", "Vue 3 : un volume aux arêtes nettes, trois axes, une fenêtre de logiciel."),
                         ("Vue 4", "graphique", "Vue 4 : deux axes et une courbe — une grandeur qui change avec l'heure.")]),
             dict(type="classer", name="besoins", categories=REPRESENTATIONS,
                  items=[("En réunion, tu as vingt secondes pour montrer ton idée de fixation", "croquis",
                          "Vingt secondes : il faut dessiner vite, à main levée."),
                         ("Fabriquer le support de la sirène à l'imprimante 3D", "modelisation",
                          "La machine a besoin de la forme exacte, en volume, dans un fichier."),
                         ("Expliquer à l'électricien comment brancher la sirène sur la batterie", "schema",
                          "Brancher : on veut voir comment c'est relié, avec des symboles que l'électricien connaît."),
                         ("Montrer comment le vent a forci pendant la nuit", "graphique",
                          "Une grandeur qui change avec le temps : des axes et une courbe."),
                         ("Dire ce que fait la station quand le vent dépasse 90 km/h", "algorithme",
                          "« Si… alors… » : l'ordre des actions, avec une condition.")]),
             dict(type="texte", name="pourquoi", lignes=3,
                  label="Pourquoi n'envoie-t-on pas le croquis directement à l'imprimante 3D&nbsp;?",
                  criteres=[dict(label="tu parles des dimensions&nbsp;: le croquis n'est pas exact, ou ne les donne pas toutes",
                                 motifs=["cote", "dimension", "mesure", "precis", "exact", "echelle", "main levee", "approximati",
                                         r"\bdroit", "tremble", "taille"],
                                 manque="Que manque-t-il au croquis pour une machine ? Pense aux dimensions et à la précision du trait."),
                            dict(label="tu dis ce qu'il faut à la machine&nbsp;: un fichier, une modélisation dans un logiciel",
                                 motifs=["fichier", "modele", "modelis", "logiciel", "numerique", "ordinateur", "volume"],
                                 manque="Dis ce que la machine lit : un fichier, fait dans un logiciel de modélisation.")],
                  etayage=["Le croquis est fait à main levée : …",
                           "L'imprimante, elle, a besoin de …"],
                  exemple="Le croquis est fait à main levée : son trait n'est pas exact et il ne donne pas toutes les dimensions. "
                          "L'imprimante a besoin d'un fichier fait dans un logiciel de modélisation, avec la forme exacte en volume.")],
    aides=["<p>Pour les vues, cherche les indices&nbsp;: un trait qui tremble, des symboles, des axes, un volume dans une fenêtre "
           "d'ordinateur. Pour les besoins, demande-toi chaque fois&nbsp;: <b>je veux montrer quoi&nbsp;?</b> Une idée, des liaisons, "
           "une évolution, un ordre d'actions, une forme exacte&nbsp;?</p>",
           "<p>Vite, pour une idée → croquis.<br>"
           "Précisément, pour câbler → schéma.<br>"
           "Une grandeur qui change → graphique.<br>"
           "Si… alors… → algorithme.<br>"
           "La forme exacte, pour une machine → modélisation 3D.<br>"
           "Le croquis est le <b>premier</b> geste&nbsp;: on le reprend en schéma ou en modélisation quand il faut de la précision.</p>"],
    jumeau=dict(consigne="Pour le système d'arrosage du jardin&nbsp;: montrer à un camarade, en une minute, où placer le "
                         "capteur&nbsp;; brancher la pompe sur la carte&nbsp;; vérifier si la terre s'est asséchée pendant la semaine. "
                         "Quelle représentation pour chacun&nbsp;?",
                correction="Placer le capteur, en une minute → un <b>croquis</b> (vite, pour une idée). Brancher la pompe → un "
                           "<b>schéma</b> (comment c'est relié). L'humidité pendant la semaine → un <b>graphique</b> (une grandeur au "
                           "fil des jours)."),
    correction=[
        "<b>Vue 1</b> → trait à main levée, légendes, flèche « vent », cote → <b>un croquis</b>",
        "<b>Vue 2</b> → des symboles (batterie, interrupteur, sirène) reliés par des traits droits → <b>un schéma</b> électrique",
        "<b>Vue 3</b> → un volume aux arêtes nettes, trois axes x, y, z, une fenêtre de logiciel → <b>une modélisation 3D</b>",
        "<b>Vue 4</b> → deux axes, une courbe, un seuil à 90 km/h → <b>un graphique</b>",
        "Aucune vue n'est un algorithme&nbsp;: il faudrait une suite d'instructions, par exemple « si le vent dépasse 90 km/h, alors "
        "déclencher la sirène, sinon attendre ».",
        "<b>Vingt secondes en réunion</b> → vite, une idée → <b>croquis</b>",
        "<b>L'imprimante 3D</b> → la forme exacte, dans un fichier → <b>modélisation 3D</b>",
        "<b>Brancher la sirène</b> → comment c'est relié, en symboles normés → <b>schéma</b>",
        "<b>Le vent pendant la nuit</b> → une grandeur qui change avec le temps → <b>graphique</b>",
        "<b>Au-delà de 90 km/h</b> → si… alors… → <b>algorithme</b>",
        "<b>Modéliser n'est pas simuler</b> → la modélisation donne la forme, à quoi la pièce ressemble → une <b>simulation</b> fait "
        "« fonctionner » ce modèle pour prévoir son comportement&nbsp;: tiendra-t-il à 250 km/h&nbsp;?",
        "<b>Une explication attendue&nbsp;:</b> « Le croquis est à main levée&nbsp;: son trait n'est pas exact et il ne donne pas "
        "toutes les dimensions. L'imprimante a besoin d'un fichier fait dans un logiciel de modélisation, avec la forme exacte "
        "en volume. »",
        ("conclusion", "Du croquis au prototype&nbsp;: <b>croquis</b> (l'idée, vite) → <b>croquis coté</b> (les dimensions) → "
                       "<b>modélisation 3D</b> (la forme exacte) → <b>prototype</b>. Le schéma, le graphique et l'algorithme disent "
                       "le reste&nbsp;: les liaisons, ce qui change, l'ordre des actions."),
    ],
    retenir="chaque représentation répond à une question&nbsp;: le <b>croquis</b> montre vite une idée, le <b>schéma</b> les "
            "liaisons, le <b>graphique</b> une évolution, l'<b>algorithme</b> l'ordre des actions, la <b>modélisation 3D</b> la "
            "forme exacte pour fabriquer.",
    piege="croire qu'un schéma ou une modélisation « remplace » le croquis&nbsp;: le croquis vient d'abord, pour trouver l'idée&nbsp;; "
          "les autres la précisent.",
)

# ─────────────────────────────────────────────────────────────────────────────
# Le cours de chaque niveau
# ─────────────────────────────────────────────────────────────────────────────
COURS = {
    "4e": (
        "<h3>Un croquis, c'est quoi&nbsp;?</h3>"
        "<ul><li>Un <b>croquis</b> — souvent appelé <b>croquis à main levée</b> — est un dessin <b>rapide</b>, fait <b>sans règle</b>, "
        "qui montre <b>l'essentiel</b>.</li>"
        "<li>Il <b>choisit</b> ce qu'il montre&nbsp;: ce qui sert à comprendre, rien de plus.</li>"
        "<li><b>Pas besoin de savoir « bien » dessiner</b>&nbsp;: un rond pour une tête, un rectangle pour une boîte suffisent. Un "
        "croquis se juge à ce qu'il fait comprendre, pas à sa beauté.</li></ul>"
        "<h3>Les outils du croquis</h3>"
        '<div class="defile"><table><tr><th scope="col">Outil</th><th scope="col">À quoi il sert</th><th scope="col">Exemple</th></tr>'
        "<tr><td>la légende</td><td>nommer une partie&nbsp;: quelques mots, reliés au dessin par un trait</td><td>« bouton + »</td></tr>"
        "<tr><td>la flèche de mouvement</td><td>montrer un geste ou un déplacement, et son sens</td><td>une flèche rouge&nbsp;: « je "
        "tire le vélo vers moi »</td></tr>"
        "<tr><td>les numéros</td><td>donner l'ordre des étapes</td><td>la carte, puis le bip, puis tirer le vélo</td></tr>"
        "<tr><td>la bulle</td><td>dire ce que la personne voit, entend ou ressent</td><td>« je ne vois presque rien&nbsp;! »</td></tr>"
        "<tr><td>la cote</td><td>donner une dimension, avec son unité</td><td>« 24 », et « cotes en mm »</td></tr></table></div>"
        "<h3>Du témoignage au croquis&nbsp;: l'expérience de l'usager</h3>"
        "<ul><li>On part de ce que dit l'usager, en <b>langage naturel</b>&nbsp;: ses mots à lui.</li>"
        "<li>On y cherche ce qu'il <b>fait</b> (le geste → une flèche), ce qu'il <b>voit</b> (→ une légende) et ce qu'il "
        "<b>ressent</b> (→ une bulle).</li>"
        "<li>Plusieurs croquis numérotés, qui racontent un usage étape par étape, forment un <b>storyboard</b>.</li>"
        "<li>Le croquis prépare la suite&nbsp;: un <b>schéma</b>, un <b>graphique</b> ou un <b>algorithme</b> du même usage.</li></ul>"
        "<h3>Proposer une pièce&nbsp;: le croquis coté</h3>"
        "<ul><li>Pour ajouter une fonction à un objet, on dessine la pièce que l'on invente.</li>"
        "<li>Un <b>croquis coté</b> porte la forme (à main levée), les <b>cotes</b> (des dimensions avec leur unité), le "
        "<b>matériau</b> et une <b>flèche de montage</b>.</li>"
        "<li>Le trait peut trembler&nbsp;: ce sont les cotes, pas le dessin, qui donnent les vraies dimensions.</li></ul>"
        "<h3>Relire son croquis</h3>"
        "<ul><li><b>Croquis d'usage</b>&nbsp;: la personne, l'objet, le geste par une flèche, au moins deux légendes, le ressenti.</li>"
        "<li><b>Croquis de solution</b>&nbsp;: la pièce, comment elle tient, au moins une cote, le matériau, la flèche de montage.</li></ul>"),
    "3e": (
        "<h3>Proposer plusieurs solutions</h3>"
        "<ul><li>Avant de choisir, on cherche <b>plusieurs</b> solutions&nbsp;: des <b>croquis rapides</b>, quelques minutes chacun.</li>"
        "<li>Deux solutions sont <b>vraiment différentes</b> quand leur <b>principe</b> change (serrer, poser, accrocher…), pas quand on "
        "ajoute une vis&nbsp;: sinon, ce sont des <b>variantes</b>.</li>"
        "<li>On les compare avec le <b>cahier des charges</b>, ligne par ligne, puis on choisit en donnant ses raisons.</li></ul>"
        "<h3>Lire un croquis coté</h3>"
        "<ul><li>Celui qui fabrique doit y trouver, sans poser de question&nbsp;: les <b>trois dimensions</b>, leur <b>unité</b>, le "
        "<b>matériau</b>, chaque <b>perçage</b> (diamètre et place).</li>"
        "<li>Chaque détail doit être sur une <b>vue</b> qui le montre&nbsp;; un trait en <b>pointillés</b> montre ce qui est caché.</li>"
        "<li><b>« Est-ce que ça rentre&nbsp;? »</b>&nbsp;: on compare chaque dimension à la place disponible, une à une. Une cote qui "
        "manque empêche de conclure.</li></ul>"
        "<h3>Cinq façons de représenter une solution</h3>"
        '<div class="defile"><table><tr><th scope="col">Façon</th><th scope="col">Ce qu\'elle montre</th>'
        '<th scope="col">Quand s\'en servir</th></tr>'
        "<tr><td>croquis</td><td>une idée, à main levée</td><td>vite, pour chercher et montrer</td></tr>"
        "<tr><td>schéma</td><td>les liaisons, avec des symboles normés</td><td>précisément, pour câbler ou expliquer un principe</td></tr>"
        "<tr><td>graphique</td><td>une grandeur qui change</td><td>pour suivre une mesure dans le temps</td></tr>"
        "<tr><td>algorithme</td><td>l'ordre des actions, avec des conditions</td><td>pour programmer</td></tr>"
        "<tr><td>modélisation 3D</td><td>la forme exacte, en volume</td><td>pour fabriquer avec une machine</td></tr></table></div>"
        "<h3>Modéliser, simuler, fabriquer</h3>"
        "<ul><li><b>Modéliser</b>, c'est représenter la <b>forme</b> et la structure de l'objet&nbsp;: à quoi il ressemble.</li>"
        "<li><b>Simuler</b>, c'est faire « fonctionner » ce modèle dans un logiciel&nbsp;: comment il se comportera (tiendra-t-il au "
        "vent&nbsp;?). On ne simule qu'un objet déjà modélisé.</li>"
        "<li><b>L'ordre</b>&nbsp;: croquis → croquis coté → modélisation 3D, et simulation → prototype.</li></ul>"),
}

# ─────────────────────────────────────────────────────────────────────────────
# Les deux niveaux
# ─────────────────────────────────────────────────────────────────────────────
NIVEAUX = {
    "4e": dict(
        codes=["4e_C2.1", "4e_C7.2"],
        mission="Passer de ce que dit un usager au croquis qui le montre, puis proposer une pièce nouvelle par un croquis coté.",
        avant=[("Je sais légender un dessin&nbsp;: écrire le nom d'une partie et la relier au dessin par un trait.",
                "cycle 3 — sciences et technologie", "@synthese#les-mots", "les mots de l'atelier, dans la synthèse (2 minutes)"),
               ("Je sais décrire un geste avec des mots précis&nbsp;: qui fait quoi, avec quoi, dans quel ordre.",
                "cycle 3 — français, sciences et technologie", "@synthese#les-mots",
                "les mots de l'atelier, dans la synthèse (2 minutes)")],
        situation_titre="Un dessin rapide, qui dit l'essentiel",
        situation="<p>Pour raconter ce que vit un usager, ou pour proposer une pièce, on n'attend pas d'avoir un logiciel&nbsp;: on "
                  "prend un crayon. Le programme de technologie appelle ce dessin le <b>croquis</b>&nbsp;; dans les ateliers, on dit "
                  "souvent <b>croquis à main levée</b> — sans règle, en quelques minutes. Quand plusieurs croquis numérotés racontent "
                  "un usage étape par étape, on parle de <b>storyboard</b>.</p>"
                  "<p><b>Dans cet atelier</b>, tu passes du témoignage d'un usager au croquis — à une borne de vélos, puis devant le "
                  "boîtier du jardin connecté du collège —, et tu proposes une pièce nouvelle pour le jardin par un <b>croquis "
                  "coté</b>.</p>",
        question="Comment montrer, en quelques minutes et sans savoir « bien » dessiner, ce que vit un usager ou la pièce que l'on "
                 "invente&nbsp;?",
        hypothese_amorces=["Je pense qu'un bon croquis doit surtout…", "Pour montrer un geste, je dessinerais…",
                           "Pour qu'on puisse fabriquer ma pièce, il faudrait écrire…"],
        exercices=[E1, E2, E3],
        a_retenir="<ul><li>Un <b>croquis</b> — un <b>croquis à main levée</b> — est un dessin rapide qui <b>choisit</b> ce qu'il "
                  "montre. Pas besoin de savoir bien dessiner&nbsp;: il doit être lisible.</li>"
                  "<li>Pour décrire l'<b>expérience d'un usager</b>, on part de ses mots&nbsp;: ce qu'il fait devient une <b>flèche de "
                  "mouvement</b>, ce qu'il voit une <b>légende</b>, ce qu'il ressent une <b>bulle</b>. Une suite de croquis numérotés "
                  "est un <b>storyboard</b>.</li>"
                  "<li>Pour <b>proposer une pièce</b>, on fait un <b>croquis coté</b>&nbsp;: la forme, les cotes avec leur unité, le "
                  "matériau, la flèche de montage.</li></ul>",
        bonus=[dict(titre="Le storyboard de la première fois",
                    consigne="<p>Raconte en <b>trois croquis numérotés</b> — un <b>storyboard</b> — la première fois d'Inès à la "
                             "borne&nbsp;: elle pousse le vélo, rien ne bouge, elle comprend qu'il faut tirer. Décris en mots ce que "
                             "montre chaque case.</p>",
                    correction=["<b>Case 1</b> → Inès pousse le vélo vers la borne → une flèche rouge vers la borne",
                                "<b>Case 2</b> → rien ne bouge → une bulle « c'est cassé&nbsp;? », un point d'interrogation",
                                "<b>Case 3</b> → elle tire le vélo en arrière → une flèche rouge qui s'éloigne de la borne, une "
                                "bulle « ah, ça sort&nbsp;! »",
                                ("conclusion", "Un storyboard montre un usage dans le temps&nbsp;; ici, il fait voir un défaut de la "
                                               "borne&nbsp;: rien n'indique dans quel sens tirer.")]),
               dict(titre="L'étiquette sans phrase",
                    consigne="<p>Le collège veut coller sur le boîtier du jardin une étiquette qui explique le réglage <b>sans aucune "
                             "phrase</b>, par un petit croquis seulement. Que dessines-tu&nbsp;?</p>",
                    correction=["<b>Le boîtier</b> → l'écran et ses trois boutons",
                                "<b>Une flèche</b> sur le bouton + → « × 2 = 1 h », pour dire qu'un appui avance d'une demi-heure",
                                "<b>Une deuxième flèche</b> sur OK → deux petits arcs, pour le bip",
                                ("conclusion", "Un croquis bien choisi se comprend sans lire&nbsp;: c'est pour cela qu'on en trouve "
                                               "sur les notices.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre ce qu'il faut montrer et ce qu'on peut laisser de côté, ou sur l'unité "
                      "d'une cote. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
    "3e": dict(
        codes=["3e_C7.2"],
        mission="Proposer plusieurs solutions par des croquis rapides, vérifier un croquis coté, puis choisir quand passer au schéma "
                "ou à la modélisation.",
        avant=[("Je sais faire un croquis d'usage&nbsp;: la personne, l'objet, le geste par une flèche, des légendes.",
                "4e_C2.1", "@niveau:4e#cq_4e_e1", "l'atelier de 4e, exercices 1 et 2 (22 minutes)"),
               ("Je sais proposer une pièce par un croquis coté&nbsp;: des cotes avec leur unité, le matériau, la flèche de montage.",
                "4e_C7.2", "@niveau:4e#cq_4e_e3", "l'atelier de 4e, exercice 3 (15 minutes)")],
        situation_titre="Chercher, puis préciser",
        situation="<p>En 3e, on conçoit un objet nouveau&nbsp;: la <b>station d'alerte cyclonique</b> du collège. Le premier geste reste "
                  "le <b>croquis</b> — un croquis à main levée, rapide — pour chercher <b>plusieurs</b> solutions et en discuter. "
                  "Ensuite seulement, on précise&nbsp;: un croquis coté pour fabriquer, un schéma pour câbler, une modélisation 3D "
                  "pour une machine.</p>",
        question="Comment passer d'une idée dessinée en trois minutes à une pièce que l'on peut fabriquer&nbsp;?",
        hypothese_amorces=["Je pense qu'il faut d'abord…, puis…", "Pour choisir entre plusieurs idées, je…",
                           "Un croquis ne suffit plus quand…"],
        exercices=[E4, E5, E6],
        a_retenir="<ul><li>On propose <b>plusieurs</b> solutions par des croquis rapides, de <b>principes différents</b>, puis on "
                  "choisit avec le cahier des charges.</li>"
                  "<li>Un croquis coté permet de fabriquer s'il donne les <b>trois dimensions</b>, leur <b>unité</b>, le "
                  "<b>matériau</b> et chaque <b>perçage</b>, sur une vue qui le montre.</li>"
                  "<li>Le croquis est le <b>premier</b> geste&nbsp;: le <b>schéma</b> montre les liaisons, le <b>graphique</b> une "
                  "évolution, l'<b>algorithme</b> l'ordre des actions, la <b>modélisation 3D</b> la forme exacte pour fabriquer.</li></ul>",
        bonus=[dict(titre="Est-ce que ça rentre, avec le câble&nbsp;?",
                    consigne="<p>Le boîtier complété mesure 120 × 80 × 60 mm. Le coffret du poteau mesure, à l'intérieur, 130 × 90 × "
                             "70 mm. Mais le passe-câble dépasse de 15 mm sous le boîtier. Le boîtier entre-t-il encore, et dans quel "
                             "sens&nbsp;?</p>",
                    correction=["<b>Debout</b> → hauteur 80 + 15 = 95 mm, pour 90 mm de place ✘",
                                "<b>Couché sur le côté</b> → le passe-câble s'ajoute à la longueur&nbsp;: 120 + 15 = 135 mm, pour 130 mm ✘",
                                "<b>Couché sur le dos</b> → il s'ajoute à la profondeur&nbsp;: 60 + 15 = 75 mm, pour 70 mm ✘",
                                ("conclusion", "Dans aucun sens&nbsp;: il ne reste que 10 mm de marge dans chaque direction, moins que les "
                                               "15 mm du passe-câble. Il faut un coffret plus grand ou un passe-câble coudé — une "
                                               "dimension oubliée, et la pièce ne rentre plus.")]),
               dict(titre="Modéliser ou simuler&nbsp;?",
                    consigne="<p>Avant de fabriquer le bras de la solution 3, l'équipe veut savoir s'il tiendra sous des rafales de "
                             "250 km/h. Faut-il modéliser, simuler, ou les deux&nbsp;? Dans quel ordre&nbsp;?</p>",
                    correction=["<b>Modéliser d'abord</b> → dessiner le bras en 3D, avec ses dimensions exactes et son matériau",
                                "<b>Simuler ensuite</b> → le logiciel applique au modèle l'effort du vent, et montre où il plie",
                                "<b>Essayer enfin</b> → sur un prototype, si la simulation est bonne",
                                ("conclusion", "Modéliser, c'est la forme&nbsp;; simuler, c'est le comportement. On ne simule qu'un "
                                               "objet déjà modélisé.")])],
        metacognition="Où as-tu hésité&nbsp;? Par exemple entre deux solutions qui n'étaient que des variantes, ou entre un schéma et "
                      "une modélisation. Qu'est-ce que tu dois encore revoir, et comment&nbsp;?",
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# Ce que le reste du site lit de cet atelier
# ─────────────────────────────────────────────────────────────────────────────
MODULE = "croquis"
NOM_PANNEAU = "croquis"
PANNEAU_TEXTE = {
    "4e": "Le <b>croquis</b> — souvent appelé <b>croquis à main levée</b> — en 4e&nbsp;: tu passes du témoignage d'un usager au croquis "
          "qui le montre (une borne de vélos, le boîtier du jardin), puis tu proposes par un <b>croquis coté</b> une pièce qui tient "
          "le capteur d'humidité du jardin.",
    "3e": "Le <b>croquis</b> — souvent appelé <b>croquis à main levée</b> — en 3e&nbsp;: tu proposes trois solutions pour fixer la "
          "sirène de la station d'alerte, tu vérifies un croquis coté avant fabrication, puis tu choisis quand passer au schéma ou "
          "à la modélisation.",
}
IMAGES = {
    "croquis_borne_A.svg": BORNE_A,
    "croquis_borne_B.svg": BORNE_B,
    "croquis_borne_C.svg": BORNE_C,
    "croquis_gardienne_reglage.svg": GARDIENNE,
    "croquis_cote_capteur_humidite.svg": CAPTEUR,
    "croquis_support_capteur.svg": SUPPORT,
    "croquis_sirene_trois_solutions.svg": SIRENE,
    "croquis_cote_boitier_incomplet.svg": BOITIER,
    "croquis_cote_boitier_complete.svg": BOITIER_COMPLET,
    "station_quatre_representations.svg": QUATRE,
}
ROLES_IMAGES = {
    "croquis_borne_A.svg": "4e, exercice 1 et QCM : le croquis qui correspond au témoignage",
    "croquis_borne_B.svg": "4e, exercice 1 et QCM : le croquis à la flèche inversée",
    "croquis_borne_C.svg": "4e, exercice 1 et QCM : le croquis de l'intérieur de la borne, sans usager",
    "croquis_gardienne_reglage.svg": "4e, correction de l'exercice 2, synthèse et QCM : un croquis d'usage possible",
    "croquis_cote_capteur_humidite.svg": "4e, exercice 3 et QCM : les données cotées du capteur et du bac",
    "croquis_support_capteur.svg": "4e, correction de l'exercice 3 : un croquis coté possible du support",
    "croquis_sirene_trois_solutions.svg": "3e, correction de l'exercice 4 et QCM : trois solutions de principes différents",
    "croquis_cote_boitier_incomplet.svg": "3e, exercice 5 et QCM : le croquis coté à vérifier",
    "croquis_cote_boitier_complete.svg": "3e, correction de l'exercice 5 et synthèse : le croquis coté complété",
    "station_quatre_representations.svg": "3e, exercice 6 et QCM : la même station en quatre représentations",
}
SCHEMAS_SYNTHESE = {"4e": GARDIENNE, "3e": BOITIER_COMPLET}
VOCAB_EN = [("croquis", "sketch"), ("à main levée", "freehand"), ("légende", "label"), ("flèche", "arrow"),
            ("cote", "dimension"), ("croquis coté", "dimensioned sketch"), ("storyboard", "storyboard"),
            ("schéma", "diagram"), ("modélisation 3D", "3D modelling"), ("prototype", "prototype")]
VERBES = {"5e": "pas d'exercice de croquis&nbsp;: le programme ne le nomme qu'en 4e et en 3e. En 5e, l'élève légende déjà des "
                "dessins, sans que le croquis soit travaillé pour lui-même.",
          "4e": "<b>passer</b> du témoignage d'un usager au croquis (4e_C2.1), puis <b>proposer</b> une pièce par un croquis coté "
                "(4e_C7.2)",
          "3e": "<b>proposer plusieurs</b> solutions par des croquis rapides, <b>lire</b> un croquis coté, puis <b>choisir</b> quand "
                "passer au schéma ou à la modélisation (3e_C7.2)"}
CHAINE = ("<p><b>Du langage naturel aux schémas</b> (analyse de l'usage, C2)&nbsp;: témoignage → <b>croquis d'usage</b> → schéma, "
          "graphique, algorithme.</p>"
          "<p><b>Premier geste de la conception</b> (C7)&nbsp;: <b>croquis</b> (plusieurs idées) → <b>croquis coté</b> → schéma → "
          "modélisation 3D (et simulation) → prototype.</p>"
          "<p>Cet atelier fait la jonction&nbsp;: il suit l'analyse du besoin et des contraintes (bête à cornes, pieuvre, exigences) "
          "et précède la modélisation et le prototypage du thème 3 (C7).</p>")
NOTES_PROF = ("<ul><li>Plan du 24/10/2026&nbsp;: six exercices — en 4e, deux pour 4e_C2.1 (lire, puis dessiner un croquis d'usage) et "
              "un pour 4e_C7.2 (proposer par un croquis coté)&nbsp;; en 3e, trois pour 3e_C7.2 (proposer plusieurs solutions, lire un "
              "croquis coté, choisir sa représentation). Pas de 5e&nbsp;: le programme ne nomme le croquis qu'en 4e et en 3e.</li>"
              "<li>Ce qui ne refait pas le thème 3&nbsp;: la séquence de 4e « jardin — conception » demande deux supports (poteau ou "
              "potence) et un choix par deux critères&nbsp;; ici, le croquis d'usage (C2.1) et le croquis coté d'une autre pièce, le "
              "support du capteur. En 3e, la séquence du capteur de confort fabrique un boîtier étanche&nbsp;; ici, on <i>lit</i> le "
              "croquis coté d'un boîtier avant fabrication.</li>"
              "<li>Le croquis à l'écran&nbsp;: une zone de dessin par exercice (crayon, trait épais, crayon rouge pour les cotes et les "
              "flèches, gomme, annuler, effacer), une description en mots pour qui ne peut pas dessiner, et une liste de relecture "
              "que l'élève coche. La page ne juge pas le dessin&nbsp;: elle vérifie qu'il existe (quelques traits, ou une description) "
              "et que la relecture est faite. Le jugement reste au professeur&nbsp;; d'où la correction illustrée d'un croquis possible.</li>"
              "<li>Exercice 4&nbsp;: les trois croquis se font dans une seule zone (une zone par exercice). Sur un téléphone, la zone "
              "est étroite&nbsp;: conseiller la tablette, ou le papier puis la description en mots.</li>"
              "<li>Inspiration&nbsp;: mécaniques relevées dans les inventaires de lecture du cahier « 123 Techno » (Bordas 2021) — "
              "retrouver les règles d'un croquis réussi à partir d'un bon exemple, paires de règles contraires à cocher, image à "
              "erreurs (ici, un croquis coté incomplet), « est-ce que ça rentre&nbsp;? » à partir de cotes, un même objet sous "
              "plusieurs représentations, « rapidement → croquis, précisément → schéma », modéliser n'est pas simuler. Tout est "
              "transposé à nos objets et réécrit&nbsp;; aucun énoncé, aucune image de l'éditeur.</li>"
              "<li>Écarts de l'éditeur non repris&nbsp;: schéma « normé » dessiné en perspective et en couleurs, symbole non normalisé. "
              "Le schéma de l'exercice 6 est en noir, à traits droits, chaque symbole nommé.</li>"
              "<li>Les chiffres (250 km/h, 4 kg, toutes les dimensions) viennent d'un cahier des charges imaginé&nbsp;; aucune donnée "
              "réelle n'est citée.</li></ul>")
DEUX_NOMS = ("Dans le programme de technologie, ce dessin s'appelle simplement le <b>croquis</b>. Dans les ateliers et les bureaux "
             "d'études, on dit souvent <b>croquis à main levée</b>&nbsp;: dessiné sans règle, en quelques minutes. Un croquis qui porte "
             "des dimensions est un <b>croquis coté</b>&nbsp;; une suite de croquis numérotés qui raconte un usage est un "
             "<b>storyboard</b>. Si tu rencontres l'un de ces noms, tu sauras que c'est la même famille de dessins.")
QCM_SOUS_TITRE = ("Du témoignage de l'usager au croquis, proposer une pièce par un croquis coté (4e) ; plusieurs solutions en "
                  "croquis rapides, lire un croquis coté, choisir entre croquis, schéma et modélisation (3e)")
