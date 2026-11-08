# -*- coding: utf-8 -*-
"""Les dessins des ateliers : SVG originaux (CC0), écrits par programme.

Un seul générateur par famille de schéma, pour que la version « à compléter »
et la version « corrigée » soient le MÊME dessin, case pour case : l'élève qui
ouvre la correction retrouve son schéma au même endroit.

Chaque fonction rend une chaîne SVG complète, avec <title> et <desc>.
Les cases « vivantes » (que la page remplit pendant que l'élève choisit) sont
des <text id="…" data-car data-lignes> : le moteur de la page y écrit le texte.
"""
import html
import math

ENCRE = "#1b2438"
GRIS = "#5b6b86"
FOND = "#fbfcff"
POLICE = "font-family=\"'Segoe UI',system-ui,Arial,sans-serif\""

# Familles d'interacteurs : une couleur ET un mot, jamais la couleur seule.
FAMILLES = {
    "usager": ("#1f5fbf", "#e7f0ff", "un usager"),
    "donnee": ("#7a3fc7", "#f2eaff", "une donnée"),
    "objet": ("#b35c00", "#fff1df", "un autre objet"),
    "environnement": ("#16753a", "#e3f6e9", "l'environnement"),
    "neutre": ("#3d4b66", "#ffffff", ""),
    "vide": ("#8a97ad", "#f4f6fb", ""),
}


def e(s):
    return html.escape(str(s), quote=True)


def couper(texte, car):
    mots, lignes, cour = str(texte).split(), [], ""
    for m in mots:
        essai = (cour + " " + m).strip()
        if len(essai) > car and cour:
            lignes.append(cour)
            cour = m
        else:
            cour = essai
    if cour:
        lignes.append(cour)
    return lignes or [""]


def texte(x, y, contenu, car=22, taille=15, gras=False, couleur=ENCRE, ancre="middle",
          ident=None, lignes_max=3, vide="…", italique=False, interligne=1.15, prefixe=""):
    """Un bloc de texte centré verticalement sur y (plusieurs lignes)."""
    lignes = couper(contenu, car) if contenu else couper(vide, car)
    lignes = lignes[:lignes_max]
    attrs = ['x="%.1f"' % x, 'y="%.1f"' % y, 'font-size="%s"' % taille, 'fill="%s"' % couleur,
             'text-anchor="%s"' % ancre, 'dominant-baseline="middle"']
    if gras:
        attrs.append('font-weight="700"')
    if italique:
        attrs.append('font-style="italic"')
    if ident:
        attrs += ['id="%s"' % ident, 'data-car="%d"' % car, 'data-lignes="%d"' % lignes_max,
                  'data-vide="%s"' % e(vide), 'data-interligne="%s"' % interligne]
        if prefixe:
            attrs.append('data-prefixe="%s"' % e(prefixe))
    debut = -((len(lignes) - 1) / 2) * interligne
    tsp = []
    for i, l in enumerate(lignes):
        tsp.append('<tspan x="%.1f" dy="%.2fem">%s</tspan>' % (x, debut if i == 0 else interligne, e(l)))
    return "<text %s>%s</text>" % (" ".join(attrs), "".join(tsp))


def _legende_unites(dessin):
    """Règle d'or n°312 : une unité écrite dans le dessin sans son nom reçoit la ligne « Unités : V (volts) »
    sous le dessin (outil commun `_outils/legende_unites.py`, qui ne touche à rien d'autre)."""
    import pathlib
    import sys
    outils = str(pathlib.Path(__file__).resolve().parents[3] / "_outils")
    if outils not in sys.path:
        sys.path.insert(0, outils)
    import legende_unites
    return legende_unites.poser(dessin)


def svg(largeur, hauteur, titre, desc, corps, classe="schema", ident=None):
    return _legende_unites(_svg(largeur, hauteur, titre, desc, corps, classe, ident))


def _svg(largeur, hauteur, titre, desc, corps, classe="schema", ident=None):
    i = (' id="%s"' % ident) if ident else ""
    if classe == "schema" and largeur <= 560:
        classe = "schema etroit"   # sur téléphone, un schéma étroit n'est pas élargi à 560 px
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" class="%s"%s role="img" '
            'aria-labelledby="%s-t %s-d" %s>'
            '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>'
            '<rect x="0" y="0" width="%d" height="%d" fill="%s"/>%s</svg>'
            % (largeur, hauteur, largeur, hauteur, classe, i, ident or "s", ident or "s", POLICE,
               ident or "s", e(titre), ident or "s", e(desc), largeur, hauteur, FOND, corps))


def fleche_def(ident="pointe", couleur=ENCRE):
    # Pointe en unités utilisateur : sa taille ne dépend pas de l'épaisseur du trait.
    return ('<defs><marker id="%s" viewBox="0 0 12 10" refX="11" refY="5" markerWidth="12" '
            'markerHeight="10" markerUnits="userSpaceOnUse" orient="auto-start-reverse">'
            '<path d="M0,0 L12,5 L0,10 z" fill="%s"/></marker></defs>' % (ident, couleur))


# ─────────────────────────────────────────────────────────────────────────────
# Diagramme des interacteurs extérieurs (diagramme pieuvre)
# ─────────────────────────────────────────────────────────────────────────────
def pieuvre(ident, objet, bulles, titre, desc, liens_fc=(), liens_fp=(), largeur=800, hauteur=500,
            montrer_famille=False, rotation=0):
    """bulles : liste de dicts {nom, famille, vivant(id ou None), vide(str)}.
    liens_fc : [(index_bulle, "FC1")] trait objet–bulle étiqueté.
    liens_fp : [(i, j, "FP1")] courbe bulle–objet–bulle étiquetée.
    rotation : décalage (degrés) de la première bulle, depuis le haut, dans le sens des aiguilles d'une montre.
    Pour qu'une FP se lise comme un U (la corne de la bête à cornes), ses deux interacteurs sont VOISINS sur le cercle."""
    cx, cy = largeur / 2, hauteur / 2 + 6
    rx, ry = largeur * 0.36, hauteur * 0.36
    n = len(bulles)
    pos = []
    for k in range(n):
        a = -math.pi / 2 + math.radians(rotation) + 2 * math.pi * k / n
        pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    # Chaque interacteur est une ELLIPSE (convention du diagramme pieuvre), comme l'objet au centre.
    BRX = 100                                         # demi-largeur d'une bulle
    bry = 44 if montrer_famille else 35               # demi-hauteur (plus haute quand la famille s'écrit dessous)
    ORX, ORY = 106, 52                                # l'ellipse de l'objet

    def dans_bulle(x, y, dx, dy, marge=7):
        """Le point (x+dx, y+dy), ramené dans l'ellipse de la bulle centrée en (x, y) s'il en sort."""
        r = math.hypot(dx / (BRX - marge), dy / (bry - marge))
        return (x + dx / r, y + dy / r) if r > 1 else (x + dx, y + dy)

    def controle_fp(x1, y1, x2, y2):
        """Point de contrôle (Bézier quadratique) d'une FP. La courbe ENTRE dans l'ellipse de l'objet et y plonge, comme
        un U, jusqu'au point p situé à mi-chemin entre son centre et son bord, du côté des deux interacteurs (le nom de
        l'objet s'écarte de l'autre côté) : elle se lit « passer par l'objet ». Une quadratique passe à t = 0,5 par
        (P1 + 2q + P2) / 4 : pour qu'elle passe par p, q = 2·p − m, m étant le milieu des deux interacteurs."""
        mx_, my_ = (x1 + x2) / 2, (y1 + y2) / 2
        ux, uy = mx_ - cx, my_ - cy
        d = math.hypot(ux, uy)
        ux, uy = (ux / d, uy / d) if d > 1 else (0.0, -1.0)
        bord = 1 / math.hypot(ux / ORX, uy / ORY)     # rayon de l'ellipse de l'objet dans cette direction
        px_, py_ = cx + ux * 0.52 * bord, cy + uy * 0.52 * bord
        return 2 * px_ - mx_, 2 * py_ - my_

    nb_fp = {}
    for (i, j, _l) in liens_fp:
        nb_fp[i] = nb_fp.get(i, 0) + 1
        nb_fp[j] = nb_fp.get(j, 0) + 1

    def bouts_fp(i, j):
        """Les deux extrémités d'une FP. Quand un interacteur porte plusieurs FP, chacune part de la moitié de sa bulle
        tournée vers son autre interacteur : les courbes ne se superposent pas en sortant de la bulle."""
        (x1, y1), (x2, y2) = pos[i], pos[j]
        d = math.hypot(x2 - x1, y2 - y1) or 1
        vx, vy = (x2 - x1) / d, (y2 - y1) / d
        if nb_fp.get(i, 0) > 1:
            x1, y1 = dans_bulle(x1, y1, 48 * vx, 48 * vy)
        if nb_fp.get(j, 0) > 1:
            x2, y2 = dans_bulle(x2, y2, -48 * vx, -48 * vy)
        return x1, y1, x2, y2

    def point_fp(i, j, t):
        x1, y1, x2, y2 = bouts_fp(i, j)
        qx, qy = controle_fp(x1, y1, x2, y2)
        u = 1 - t
        return u * u * x1 + 2 * u * t * qx + t * t * x2, u * u * y1 + 2 * u * t * qy + t * t * y2, t

    CONTOUR = [(math.cos(2 * math.pi * k / 96), math.sin(2 * math.pi * k / 96)) for k in range(96)]

    def air_ellipse(px, py, ecx, ecy, erx, ery):
        """L'air entre une étiquette (46 × 24, centrée en (px, py)) et le bord d'une ellipse ; négatif si elles se
        chevauchent (un coin de l'étiquette dans l'ellipse, ou un point du bord dans l'étiquette)."""
        coins = [(px + sx * 23, py + sy * 12) for sx in (-1, 1) for sy in (-1, 1)] + [(px, py)]
        if any(((qx - ecx) / erx) ** 2 + ((qy - ecy) / ery) ** 2 <= 1 for (qx, qy) in coins):
            return -1
        best = 99
        for (c, s_) in CONTOUR:
            qx, qy = ecx + erx * c, ecy + ery * s_
            dx, dy = max(abs(qx - px) - 23, 0), max(abs(qy - py) - 12, 0)
            if dx == 0 and dy == 0:
                return -1
            best = min(best, math.hypot(dx, dy))
        return best

    def sens_fp(x1, y1, x2, y2):
        ux, uy = (x1 + x2) / 2 - cx, (y1 + y2) / 2 - cy
        d = math.hypot(ux, uy)
        return (ux / d, uy / d) if d > 1 else (0.0, -1.0)

    def sortie(px, py, dx, dy, ecx, ecy, erx, ery):
        """Le paramètre t où la demi-droite (px, py) + t·(dx, dy) sort de l'ellipse de centre (ecx, ecy)."""
        dedans = lambda t: ((px + t * dx - ecx) / erx) ** 2 + ((py + t * dy - ecy) / ery) ** 2 <= 1
        if not dedans(0):
            return 0.0
        lo, hi = 0.0, 1.0
        for _ in range(40):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if dedans(m) else (lo, m)
        return lo

    def milieu_visible(x0, y0, x1, y1, bulle):
        """Le milieu du segment (x0, y0) → (x1, y1) hors de l'ellipse de l'objet et hors de la bulle d'arrivée."""
        dx, dy = x1 - x0, y1 - y0
        t0 = sortie(x0, y0, dx, dy, cx, cy, ORX, ORY)                       # sortie de l'objet
        t1 = 1 - sortie(x1, y1, -dx, -dy, bulle[0], bulle[1], BRX, bry)    # entrée dans la bulle
        t = (t0 + t1) / 2 if t1 > t0 else 0.5
        return x0 + t * dx, y0 + t * dy

    corps = [fleche_def(ident + "-pt")]
    # Traits d'abord (sous les bulles)
    etiquettes = []
    # Les traits simples (relation) ne se dessinent que si le schéma ne distingue pas FP et FC.
    if not liens_fc and not liens_fp:
        for k, (x, y) in enumerate(pos):
            corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
                         % (x, y, cx, cy, "#9aa8c2"))
    # Bulles où arrive une FP : la FC qui y va aussi est décalée, pour ne pas se confondre avec la courbe.
    arrivees_fp = {}
    for (i, j, _l) in liens_fp:
        for k, t in ((j, 0.9), (i, 0.1)):
            arrivees_fp[k] = point_fp(i, j, t)[:2]
    for (k, lab) in liens_fc:
        x, y = pos[k]
        x0, y0 = cx, cy
        if k in arrivees_fp:
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy) or 1
            px, py = -dy / d, dx / d
            ax, ay = arrivees_fp[k]
            signe = -1 if (ax - x) * px + (ay - y) * py > 0 else 1
            x, y = dans_bulle(x, y, signe * 62 * px, signe * 62 * py)   # l'extrémité reste dans la bulle
            x0, y0 = cx + signe * 26 * px, cy + signe * 26 * py
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#b3261e" stroke-width="3.2"/>'
                     % (x, y, x0, y0))
        # Règle d'or n°315 : l'étiquette se pose au milieu de la partie VISIBLE du trait — entre le bord de l'ellipse de
        # l'objet et le bord de la bulle —, pour ne toucher ni l'une ni l'autre.
        mx, my = milieu_visible(x0, y0, x, y, pos[k])
        etiquettes.append((mx, my, lab, "#b3261e"))
    # L'objet au centre, puis les courbes des FP PAR-DESSUS : on voit le trait entrer dans l'ellipse et en ressortir.
    corps.append('<ellipse cx="%.1f" cy="%.1f" rx="%d" ry="%d" fill="#ffffff" stroke="%s" stroke-width="3"/>'
                 % (cx, cy, ORX, ORY, ENCRE))
    for (i, j, lab) in liens_fp:
        x1, y1, x2, y2 = bouts_fp(i, j)
        qx, qy = controle_fp(x1, y1, x2, y2)
        corps.append('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#1f5fbf" '
                     'stroke-width="3.2" stroke-linecap="round"/>' % (x1, y1, qx, qy, x2, y2))
        # étiquette vers les quatre cinquièmes de la courbe, côté de la seconde bulle — sauf si elle y toucherait
        # l'étiquette d'une FC, l'ellipse de l'objet ou une bulle (n°315 : 16 unités d'air) : on la fait glisser le long
        # de la courbe, au plus près de 0,80.
        def air(px, py):
            gaps = [max(abs(px - ex) - 46, abs(py - ey) - 24) for (ex, ey, _l, _c) in etiquettes]
            gaps.append(air_ellipse(px, py, cx, cy, ORX, ORY))
            gaps += [air_ellipse(px, py, bx, by, BRX, bry) for (bx, by) in pos]
            return min(gaps)
        choix = sorted((point_fp(i, j, t / 100) for t in range(50, 97, 2)),
                       key=lambda q: abs(q[2] - 0.80))
        ex_, ey_, _t = next((q for q in choix if air(q[0], q[1]) >= 16),
                            max(choix, key=lambda q: air(q[0], q[1])))
        etiquettes.append((ex_, ey_, lab, "#1f5fbf"))
    # Le nom de l'objet s'écarte un peu du côté où plongent les FP, pour que la courbe ne le touche pas.
    sx = sum(sens_fp(*bouts_fp(i, j))[0] for (i, j, _l) in liens_fp)
    sy = sum(sens_fp(*bouts_fp(i, j))[1] for (i, j, _l) in liens_fp)
    ds = math.hypot(sx, sy)
    tx, ty = (cx - 16 * sx / ds, cy - 13 * sy / ds) if ds > 0.3 else (cx, cy)
    corps.append(texte(tx, ty, objet, car=16, taille=19, gras=True))
    # Les bulles : une ellipse par interacteur
    for k, b in enumerate(bulles):
        x, y = pos[k]
        fam = b.get("famille", "neutre")
        trait, fond_b, mot = FAMILLES.get(fam, FAMILLES["neutre"])
        tirets = ' stroke-dasharray="7 5"' if fam == "vide" else ""
        corps.append('<ellipse cx="%.1f" cy="%.1f" rx="%d" ry="%d" fill="%s" stroke="%s" '
                     'stroke-width="2.4"%s/>' % (x, y, BRX, bry, fond_b, trait, tirets))
        if b.get("vivant"):
            corps.append(texte(x, y - (10 if montrer_famille and mot else 0), b.get("nom", ""), car=19, taille=14.5,
                               gras=True, ident=b["vivant"], lignes_max=2, vide=b.get("vide", "…"),
                               prefixe=b.get("prefixe", "")))
        else:
            corps.append(texte(x, y - (10 if montrer_famille and mot else 0), b.get("nom", ""), car=19,
                               taille=14.5, gras=True, lignes_max=2))
        if b.get("repere"):   # pastille posée sur le bord haut-gauche de l'ellipse
            bx_, by_ = x - BRX * 0.707, y - bry * 0.707
            corps.append('<circle cx="%.1f" cy="%.1f" r="12" fill="%s"/>' % (bx_, by_, trait))
            corps.append(texte(bx_, by_, b["repere"], taille=13, gras=True, couleur="#ffffff", car=3))
        if montrer_famille and mot:
            corps.append(texte(x, y + 22, mot, car=30, taille=12, couleur=trait, italique=True, lignes_max=1))
    for (mx, my, lab, coul) in etiquettes:
        corps.append('<rect x="%.1f" y="%.1f" width="46" height="24" rx="6" fill="#ffffff" stroke="%s"/>'
                     % (mx - 23, my - 12, coul))
        corps.append(texte(mx, my, lab, taille=13, gras=True, couleur=coul, car=6))
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


# ─────────────────────────────────────────────────────────────────────────────
# Le besoin (bête à cornes) — EXACTEMENT le modèle de Pascal (04/11/2026)
# ─────────────────────────────────────────────────────────────────────────────
# « La bête à cornes doit être exactement comme mon modèle. » Le dessin ci-dessous est le GABARIT mesuré au pixel sur
# son modèle, dans son cadre viewBox="50 150 960 570" : les positions, les tailles, les couleurs, l'italique, les
# pointillés, la corne qui croise le haut du produit, la flèche qui part en courbe. Toute bête à cornes du dépôt est ce
# dessin, à n'importe quelle taille d'affichage.
#   - LES FORMES ne bougent jamais et ne changent jamais de taille, quel que soit le texte : les deux ellipses du haut
#     (centres 350 et 825,5 ; 134 × 59,5), l'ellipse du produit (583, 476 ; 122 × 73), le rectangle (250, 573 ;
#     732 × 132, coins droits). Fonds blancs, contours bleu foncé #1f3864.
#   - LA CORNE (bleu #2e75b6) est tracée APRÈS le produit : elle passe sur son haut, en le croisant, comme sur le
#     modèle. C'est l'exception voulue à la règle n°315 (« rien ne se touche ») : la corne est un trait sans pointe,
#     elle ne porte aucun texte.
#   - LA FLÈCHE (même bleu) part de la corne à droite, s'incurve, puis descend droite jusqu'au rectangle, la pointe sur
#     son bord haut.
#   - LES QUESTIONS, en italique, gris très foncé, au-dessus des ellipses, et « Dans quel but ? » au-dessus du
#     rectangle, à gauche. La formulation du modèle (« Sur quoi agit-il ? »), avec la typographie juste.
#   - UNE CASE VIDE porte sa ligne pointillée ; le produit vide dit « Nom du / produit », en italique, sur deux lignes.
#   - UNE CASE REMPLIE : le texte remplace les pointillés, centré, sur deux lignes au plus. S'il est long, c'est la
#     TAILLE DU TEXTE qui baisse, jamais la forme. Le nom du produit reste en italique.
#   - Pas de titre dans le dessin : la page a déjà le sien.
# Une case « vivante » (la page y écrit le choix de l'élève, par kit.js) a une taille fixe, calculée pour deux lignes de
# `car` caractères : kit.js ne mesure pas le texte ; au-delà, il coupe la seconde ligne par « … » (le champ garde tout).
BAC_VIEWBOX = (50, 150, 960, 570)
BAC_CONTOUR = "#1f3864"
BAC_BLEU = "#2e75b6"
BAC_TEXTE = "#2b2b2b"
BAC_POLICE = "Calibri, Carlito, 'Segoe UI', Arial, sans-serif"
QUESTIONS_BAC = ("À qui le produit rend-il service ?", "Sur quoi agit-il ?", "Dans quel but ?")
#: les formes du gabarit — ("ellipse", cx, cy, rx, ry) ou ("rect", x, y, largeur, hauteur)
BAC_FORMES = {
    "a_qui": ("ellipse", 350, 284.5, 134, 59.5),
    "sur_quoi": ("ellipse", 825.5, 284.5, 133.5, 59.5),
    "objet": ("ellipse", 583, 476, 122, 73),
    "but": ("rect", 250, 573, 732, 132),
}
#: les lignes pointillées des cases vides : (x1, x2, y)
BAC_POINTILLES = {"a_qui": (234, 466, 286), "sur_quoi": (710, 942, 286), "but": (268, 964, 641)}
#: les questions : (x, y de la ligne de base, ancre)
#: la taille des quatre libellés fixes (les trois questions, « Nom du / produit ») : celle du modèle, mesurée sur ses
#: encres (« À qui le produit rend-il service ? » couvre x 77 à 559, comme le modèle) ; les réponses écrites dans les
#: formes restent à 31 au plus
BAC_TAILLE_LIBELLE = 38
BAC_QUESTIONS_XY = ((318, 191, "middle"), (845, 191, "middle"), (222, 560, "start"))
#: « Nom du / produit » : les deux lignes de base, centrées dans l'ellipse du produit comme sur le modèle
BAC_NOM_VIDE_Y = (470, 517)
BAC_CORNE = "M388,341 C440,398 520,424 590,421 C660,418 742,392 795,342"
BAC_FLECHE = "M792,344 C764,366 750,388 750,414 L750,568"
#: taille et coupe d'une case vivante : (taille du texte, caractères par ligne)
BAC_VIVANT = {"a_qui": (27, 13), "sur_quoi": (27, 13), "objet": (26, 13), "but": (26, 50)}

# Avances de Carlito (métrique de Calibri), en millièmes d'em, romain et italique confondus (la plus large des deux).
_CAR_CHASSE = (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
               'àâäçéèêëîïôöùûüÿœæÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸŒÆ’‘«»…–—°€')
_CHASSE = (226, 326, 401, 498, 507, 715, 682, 221, 303, 303, 498, 498, 250, 306, 252, 388, 507, 507, 507, 507, 507, 507,
           507, 507, 507, 507, 268, 268, 498, 498, 498, 463, 894, 579, 544, 533, 615, 488, 459, 631, 623, 252, 319, 520,
           420, 855, 646, 662, 517, 673, 543, 459, 487, 642, 567, 890, 519, 487, 468, 307, 386, 307, 498, 498, 291, 514,
           525, 423, 525, 498, 305, 514, 525, 229, 239, 455, 229, 799, 525, 527, 525, 525, 349, 391, 335, 525, 452, 715,
           433, 453, 395, 314, 460, 314, 498, 514, 514, 514, 423, 498, 498, 498, 498, 229, 229, 527, 527, 525, 525, 525,
           453, 850, 773, 579, 579, 579, 533, 488, 488, 488, 488, 252, 252, 662, 662, 642, 642, 642, 487, 867, 763, 250,
           250, 512, 512, 690, 498, 905, 339, 507)
CHASSE_CARLITO = dict(zip(_CAR_CHASSE, _CHASSE))
#: une police de repli (Segoe UI, Arial) est plus large que Calibri de 8 à 13 % : le texte doit tenir aussi avec elle
MARGE_REPLI = 1.12


def largeur_bac(s, taille):
    """La largeur d'une ligne, en unités du dessin (Calibri, avec la marge d'une police de repli)."""
    return sum(CHASSE_CARLITO.get(c, 520) for c in str(s)) * taille / 1000 * MARGE_REPLI


def _deux_lignes(texte):
    """La coupe en deux lignes la plus équilibrée (la ligne la plus longue la plus courte possible)."""
    mots = str(texte).split()
    if len(mots) < 2:
        return [" ".join(mots)]
    meilleur = None
    for i in range(1, len(mots)):
        l = [" ".join(mots[:i]), " ".join(mots[i:])]
        m = max(largeur_bac(x, 1) for x in l)
        if meilleur is None or m < meilleur[0]:
            meilleur = (m, l)
    return meilleur[1]


def _tient(lignes, taille, forme, interligne=1.2):
    """Le bloc de texte, centré dans la forme, y tient-il avec de l'air (n°315) ?"""
    n, L = len(lignes), interligne * taille
    if forme[0] == "rect":
        _, x, y, w, h = forme
        return all(largeur_bac(l, taille) <= w - 48 for l in lignes) and n * L + 0.1 * taille <= h - 24
    _, cx, cy, rx, ry = forme
    for i, l in enumerate(lignes):
        dy = abs((i - (n - 1) / 2) * L) + 0.55 * taille + 4
        dx = largeur_bac(l, taille) / 2 + 10
        if (dx / rx) ** 2 + (dy / ry) ** 2 > 1:
            return False
    return True


def ajuster_bac(texte, cle, tmax=30, tmin=16):
    """La plus grande taille (de tmax à tmin) où le texte tient dans sa forme, sur une ligne ou deux.
    Rend (taille, lignes). Un texte trop long pour deux lignes à tmin est une erreur de rédaction."""
    forme = BAC_FORMES[cle]
    t = tmax
    while t >= tmin:
        for lignes in ([str(texte).strip()], _deux_lignes(texte)):
            if _tient(lignes, t, forme):
                return t, lignes
        t -= 0.5
    raise ValueError("bête à cornes : « %s » ne tient pas dans la case %s, même en %s" % (texte, cle, tmin))


def _texte_bac(x, y, lignes, taille, italique=False, ident=None, car=None, vide=" ", interligne=1.2):
    """Un texte centré sur (x, y), une ou deux lignes. Avec `ident`, une case vivante : kit.js y écrit (data-car,
    data-lignes), et pose la classe « rempli » dès qu'il y a une réponse."""
    attrs = ['x="%s"' % _n(x), 'y="%s"' % _n(y), 'font-size="%s"' % _n(taille), 'fill="%s"' % BAC_TEXTE,
             'text-anchor="middle"', 'dominant-baseline="middle"']
    if italique:
        attrs.append('font-style="italic"')
    if ident:
        attrs += ['id="%s"' % ident, 'data-car="%d"' % car, 'data-lignes="2"', 'data-vide="%s"' % e(vide),
                  'data-interligne="%s"' % interligne]
    debut = -((len(lignes) - 1) / 2) * interligne
    tsp = ''.join('<tspan x="%s" dy="%.2fem">%s</tspan>' % (_n(x), debut if i == 0 else interligne, e(l))
                  for i, l in enumerate(lignes))
    return "<text %s>%s</text>" % (" ".join(attrs), tsp)


def _n(v):
    """Un nombre écrit court : 350, 284.5."""
    return ("%.2f" % v).rstrip("0").rstrip(".")


def _pointilles_bac(cle, classe="bac-pointilles"):
    x1, x2, y = BAC_POINTILLES[cle]
    return ('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.5" stroke-dasharray="2 3"/>'
            % (classe, _n(x1), _n(y), _n(x2), _n(y), BAC_CONTOUR))


def _forme_bac(cle):
    f = BAC_FORMES[cle]
    if f[0] == "rect":
        return ('<rect x="%s" y="%s" width="%s" height="%s" fill="#fff" stroke="%s" stroke-width="3"/>'
                % (_n(f[1]), _n(f[2]), _n(f[3]), _n(f[4]), BAC_CONTOUR))
    return ('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#fff" stroke="%s" stroke-width="3"/>'
            % (_n(f[1]), _n(f[2]), _n(f[3]), _n(f[4]), BAC_CONTOUR))


def _centre_bac(cle):
    f = BAC_FORMES[cle]
    if f[0] == "rect":
        return f[1] + f[3] / 2, f[2] + f[4] / 2
    return f[1], f[2]


def _case_bac(cle, val, v, italique=False):
    """Le contenu d'une case : pointillés (vide), case vivante (pointillés qui s'effacent), ou texte ajusté."""
    x, y = _centre_bac(cle)
    if cle in v:
        t, car = BAC_VIVANT[cle]
        vide = "Nom du produit" if cle == "objet" else " "
        h = _texte_bac(x, y, ["Nom du", "produit"] if cle == "objet" else [""], t, italique=italique, ident=v[cle],
                       car=car, vide=vide)
        return h + ("" if cle == "objet" else _pointilles_bac(cle))
    if not str(val or "").strip():
        if cle == "objet":   # le produit vide : « Nom du / produit », comme sur le modèle
            return ('<text x="583" y="%d" text-anchor="middle" font-size="%d" font-style="italic" fill="%s">Nom du</text>'
                    '<text x="583" y="%d" text-anchor="middle" font-size="%d" font-style="italic" fill="%s">produit</text>'
                    % (BAC_NOM_VIDE_Y[0], BAC_TAILLE_LIBELLE, BAC_TEXTE, BAC_NOM_VIDE_Y[1], BAC_TAILLE_LIBELLE, BAC_TEXTE))
        return _pointilles_bac(cle)
    t, lignes = ajuster_bac(val, cle, tmax=31 if cle == "objet" else 30)
    return _texte_bac(x, y, lignes, t, italique=italique)


def dessin_bac(ident, a_qui, sur_quoi, objet, but, vivants=None, questions=QUESTIONS_BAC):
    """Le gabarit, dans ses propres unités (cadre 50 150 960 570), avec ses textes. Rend la liste des éléments SVG ;
    la pointe de la flèche est le marqueur « <ident>-pb » (voir defs_bac)."""
    v = vivants or {}
    c = []
    for (x, y, ancre), q in zip(BAC_QUESTIONS_XY[:2], questions[:2]):
        c.append('<text x="%s" y="%s" text-anchor="%s" font-size="%d" font-style="italic" fill="%s">%s</text>'
                 % (_n(x), _n(y), ancre, BAC_TAILLE_LIBELLE, BAC_TEXTE, e(q)))
    for cle, val in (("a_qui", a_qui), ("sur_quoi", sur_quoi)):
        c.append(_forme_bac(cle))
        c.append(_case_bac(cle, val, v))
    c.append(_forme_bac("objet"))
    c.append(_case_bac("objet", objet, v, italique=True))
    # la corne, APRÈS le produit : elle passe sur son haut
    c.append('<path d="%s" fill="none" stroke="%s" stroke-width="3"/>' % (BAC_CORNE, BAC_BLEU))
    c.append('<path d="%s" fill="none" stroke="%s" stroke-width="3" marker-end="url(#%s-pb)"/>' % (BAC_FLECHE, BAC_BLEU, ident))
    x, y, ancre = BAC_QUESTIONS_XY[2]
    c.append('<text x="%s" y="%s" font-size="%d" font-style="italic" fill="%s">%s</text>'
             % (_n(x), _n(y), BAC_TAILLE_LIBELLE, BAC_TEXTE, e(questions[2])))
    c.append(_forme_bac("but"))
    c.append(_case_bac("but", but, v))
    return c


def defs_bac(ident):
    """La pointe de la flèche, en unités du dessin (sa taille ne dépend pas de l'épaisseur du trait)."""
    return ('<defs><marker id="%s-pb" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="12" markerHeight="12" '
            'markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L11,6 L1,11 z" fill="%s"/></marker></defs>'
            % (ident, BAC_BLEU))


def _style_vivant(ident):
    """La ligne pointillée s'efface quand la page écrit la réponse (kit.js pose la classe « rempli » sur le texte)."""
    return '<style>#%s text.rempli+.bac-pointilles{display:none}</style>' % ident


def bete_a_cornes(ident, a_qui, sur_quoi, objet, but, titre, desc, vivants=None, largeur=None, hauteur=None):
    """Le gabarit de Pascal, avec ses textes. vivants : {"a_qui": id, "sur_quoi": id, "objet": id, "but": id} pour les
    cases que la page remplit. `largeur` et `hauteur` sont ignorés : le cadre est celui du gabarit, 960 × 570."""
    x0, y0, w, h = BAC_VIEWBOX
    corps = [defs_bac(ident)]
    if vivants:
        corps.append(_style_vivant(ident))
    corps += dessin_bac(ident, a_qui, sur_quoi, objet, but, vivants=vivants)
    dessin = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d" width="%d" height="%d" class="schema" id="%s" '
              'role="img" aria-labelledby="%s-t %s-d" font-family="%s"><title id="%s-t">%s</title><desc id="%s-d">%s</desc>'
              '<rect x="%d" y="%d" width="%d" height="%d" fill="#fff"/>%s</svg>'
              % (x0, y0, w, h, w, h, ident, ident, ident, e(BAC_POLICE), ident, e(titre), ident, e(desc),
                 x0, y0, w, h, "".join(corps)))
    return _legende_unites(dessin)


# ─────────────────────────────────────────────────────────────────────────────
# Le dessin de référence (Pascal, 04/11/2026 : « Les mots de cette représentation devront être utilisés plusieurs
# fois, ce sont des références. ») : le gabarit, rempli avec les mots de la méthode APTE. On n'en prend que les mots :
# la forme reste le gabarit de la n°318, sans titre dans le dessin (le titre est posé au-dessus, par la page).
# ─────────────────────────────────────────────────────────────────────────────
#: les mots de référence, case par case : à qui ? sur quoi ? le produit, dans quel but ?
MOTS_REFERENCE_BAC = {"a_qui": "Utilisateur", "sur_quoi": "Matière d'œuvre", "objet": "Produit", "but": "Fonction"}
TITRE_REFERENCE_BAC = "La bête à cornes (méthode APTE)"
APTE_DEVELOPPE = "APplication aux Techniques d'Entreprise"
DESC_REFERENCE_BAC = ("Le gabarit de la bête à cornes, rempli avec ses mots de référence. En haut à gauche, sous la question "
                      "« À qui le produit rend-il service ? », l'ellipse dit : Utilisateur. En haut à droite, sous « Sur quoi "
                      "agit-il ? », l'ellipse dit : Matière d'œuvre. Au centre, plus bas, l'ellipse dit : Produit ; la corne "
                      "part de l'ellipse de gauche, passe sur le haut du produit et remonte à l'ellipse de droite. De là, une "
                      "flèche descend vers le rectangle « Dans quel but ? », qui dit : Fonction.")


def bete_a_cornes_reference(ident="bc-ref"):
    """Le dessin de référence : le gabarit et ses mots de référence (Utilisateur, Matière d'œuvre, Produit, Fonction)."""
    m = MOTS_REFERENCE_BAC
    s = bete_a_cornes(ident, m["a_qui"], m["sur_quoi"], m["objet"], m["but"],
                      TITRE_REFERENCE_BAC + " : les mots de référence", DESC_REFERENCE_BAC)
    # « etroit » : sur un téléphone, le dessin se réduit à la largeur de l'écran (kit.css), sans défilement de côté —
    # quatre mots courts y restent lisibles. Le style en ligne sert aux pages écrites à la main (carte, séquences), qui
    # n'ont pas la feuille des ateliers.
    return s.replace('class="schema"', 'class="schema etroit" style="display:block;width:100%;max-width:820px;'
                     'height:auto;margin:0 auto"', 1)


def figure_reference_bac(ident="bc-ref", legende=None, apte=True, classe="figure bac-reference"):
    """Le dessin de référence dans une page, sous son titre « La bête à cornes (méthode APTE) ».
    `apte` : développer le sigle (n°313) — à la première apparition d'APTE dans la page. `legende` : la phrase sous le
    titre (par défaut, les quatre mots et ce qu'ils nomment)."""
    titre = ("La bête à cornes (méthode APTE, <i>APplication aux Techniques d'Entreprise</i>)" if apte
             else TITRE_REFERENCE_BAC)
    if legende is None:
        # un mot de référence par ligne (08/11/2026, skill texte-clair-et-aere : la légende faisait 41 mots d'un tenant)
        legende = ("Ses quatre mots de référence, les mêmes pour tous les objets&nbsp;:<br>• l'<b>utilisateur</b>&nbsp;: à qui le "
                   "produit rend service&nbsp;;<br>• la <b>matière d'œuvre</b>&nbsp;: ce sur quoi il agit&nbsp;;<br>• le "
                   "<b>produit</b>&nbsp;;<br>• la <b>fonction</b>&nbsp;: la fonction d'usage, dans quel but il existe.")
    return ('<figure class="%s"><figcaption><b class="bac-ref-titre">%s</b><br>%s</figcaption>%s</figure>'
            % (classe, titre, legende, bete_a_cornes_reference(ident)))


def bete_vers_pieuvre(ident, a_qui, sur_quoi, objet, but, fp, fc, titre, desc, largeur=900, hauteur=420):
    """La même liaison, deux fois : la corne de la bête à cornes (à qui → par l'objet → sur quoi) devient la
    fonction principale FP1 du diagramme pieuvre. Repères ①②③ sur les deux schémas, légende en mots.
    La moitié gauche est le gabarit, mis à l'échelle ; ses repères sont posés À CÔTÉ des questions, jamais sur une
    forme. La corne et la FP1 ont le même bleu (#2e75b6), pour que l'œil les relie."""
    BLEU, ROUGE, VIO = BAC_BLEU, "#b3261e", "#6d3fb5"
    corps = [defs_bac(ident), fleche_def(ident + "-pg", GRIS)]

    def badge(x, y, n):
        corps.append('<circle cx="%.1f" cy="%.1f" r="13" fill="%s"/>' % (x, y, VIO))
        corps.append(texte(x, y, n, taille=14, gras=True, couleur="#ffffff", car=3))

    # ── À gauche : le gabarit, à l'échelle k, son coin haut-gauche (50, 150) en (X0, Y0) ──
    # 35 à gauche : la place du repère ①, devant une question de 38 unités mesurée avec la police de repli
    X0, Y0, k = 35, 32, 0.39
    gx = lambda x: X0 + (x - BAC_VIEWBOX[0]) * k   # noqa: E731
    gy = lambda y: Y0 + (y - BAC_VIEWBOX[1]) * k   # noqa: E731
    corps.append(texte(gx(530), 22, "La bête à cornes", taille=15, gras=True, car=30))
    corps.append('<g transform="translate(%.2f %.2f) scale(%s) translate(%d %d)" font-family="%s">'
                 % (X0, Y0, k, -BAC_VIEWBOX[0], -BAC_VIEWBOX[1], e(BAC_POLICE)))
    corps += dessin_bac(ident, a_qui, sur_quoi, objet, but)
    corps.append('</g>')
    # les repères, à gauche de chaque question, à 6 unités de son premier mot ; la question mesurée avec la police de repli
    for i, n in enumerate("123"):
        x, y, ancre = BAC_QUESTIONS_XY[i]
        l = largeur_bac(QUESTIONS_BAC[i], BAC_TAILLE_LIBELLE)
        debut = x - l / 2 if ancre == "middle" else x
        badge(gx(debut) - 6 - 13, gy(y - 10), n)
    # ── Au milieu : « devient » ──
    corps.append('<line x1="418" y1="176" x2="474" y2="176" stroke="%s" stroke-width="3" marker-end="url(#%s-pg)"/>' % (GRIS, ident))
    corps.append(texte(446, 156, "devient", taille=14, italique=True, couleur=GRIS, car=10))
    # ── À droite : le diagramme pieuvre ──
    corps.append(texte(690, 22, "Le diagramme pieuvre", taille=15, gras=True, car=30))
    (x1, y1), (x2, y2), (cx, cy) = (565, 80), (815, 80), (690, 200)
    # La courbe ENTRE dans l'ellipse de l'objet et y plonge en U, au-dessus de son nom (même forme que la corne) :
    # elle passe, à t = 0,5, par le point visé p ; le point de contrôle vaut donc 2·p − milieu(bulles).
    orx, ory = 96, 40
    px_, py_ = cx, cy - 0.74 * ory
    qx, qy = 2 * px_ - (x1 + x2) / 2, 2 * py_ - (y1 + y2) / 2
    corps.append('<line x1="752" y1="186" x2="848" y2="100" stroke="%s" stroke-width="3.4"/>' % ROUGE)
    corps.append('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="#ffffff" stroke="%s" stroke-width="2.6"/>'
                 % (cx, cy, orx, ory, ENCRE))
    corps.append('<path d="M%d,%d Q%.1f,%.1f %d,%d" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round"/>'
                 % (x1, y1, qx, qy, x2, y2, BLEU))
    corps.append(texte(cx, cy + 8, objet, car=18, taille=15, gras=True, lignes_max=2))
    for (bx, by, val) in ((x1, y1, a_qui), (x2, y2, sur_quoi)):   # les interacteurs : des ellipses
        corps.append('<ellipse cx="%d" cy="%d" rx="80" ry="27" fill="#e8f0ff" stroke="%s" stroke-width="2.2"/>' % (bx, by, BLEU))
        corps.append(texte(bx, by, val, car=17, taille=14.5, gras=True, lignes_max=2))
    for (ex, ey, lab, coul) in ((748, 136, "FP1", BLEU), (838, 146, "FC1", ROUGE)):
        corps.append('<rect x="%d" y="%d" width="50" height="26" rx="6" fill="#ffffff" stroke="%s"/>' % (ex - 25, ey - 13, coul))
        corps.append(texte(ex, ey, lab, taille=14, gras=True, couleur=coul, car=6))
    # la phrase de la FP1, dans le bleu de la corne, sur fond blanc (contraste 4,8 : 1)
    corps.append('<rect x="500" y="262" width="380" height="48" rx="10" fill="#ffffff" stroke="%s" stroke-width="2.2"/>' % BLEU)
    corps.append(texte(690, 286, "FP1 : " + fp, car=46, taille=14, gras=True, couleur=BLEU, lignes_max=2))
    corps.append('<rect x="500" y="330" width="380" height="40" rx="10" fill="#fdeceb" stroke="%s" stroke-width="2"/>' % ROUGE)
    corps.append(texte(690, 350, "FC1 : " + fc, car=50, taille=14, gras=True, couleur=ROUGE, lignes_max=2))
    corps.append(texte(690, 394, "Au bout de la FP1, le même élément porte souvent aussi la FC1.", taille=14, italique=True,
                       couleur=GRIS, car=70, lignes_max=1))
    badge(x1 - 57, y1 - 19, "1"); badge(x2 - 57, y2 - 19, "2"); badge(500, 262, "3")
    # ── Légende, en mots, sous la bête à cornes ──
    bas = gy(BAC_VIEWBOX[1] + BAC_VIEWBOX[3])
    for k_, ligne in enumerate(["① « à qui ? » → la bulle d'où part la FP1",
                                "② « sur quoi ? » → la bulle où arrive la FP1",
                                "③ « dans quel but ? » → la phrase de la FP1"]):
        corps.append(texte(30, bas + 28 + 24 * k_, ligne, ancre="start", taille=14, car=60, couleur=ENCRE, lignes_max=1))
    return svg(largeur, max(hauteur, int(math.ceil(bas + 28 + 48 + 22))), titre, desc, "".join(corps), ident=ident)


# ─────────────────────────────────────────────────────────────────────────────
# FAST : de la fonction d'usage aux solutions techniques
# ─────────────────────────────────────────────────────────────────────────────
def fast(ident, fonction_usage, branches, titre, desc, largeur=820, vivants=None, ligne=72):
    """branches : [(fonction_technique, [solutions...])]. Une branche à deux solutions
    est une alternative (« ou »). vivants : {(i, 'ft') : id, (i, j) : id}."""
    v = vivants or {}
    lignes = sum(max(1, len(s)) for _, s in branches)
    hauteur = 110 + lignes * ligne
    corps = [fleche_def(ident + "-pt")]
    # Les deux sens de lecture
    corps.append('<line x1="300" y1="30" x2="40" y2="30" stroke="%s" stroke-width="2.2" marker-end="url(#%s-pt)"/>' % (GRIS, ident))
    corps.append(texte(170, 48, "POURQUOI ?", taille=13, gras=True, couleur=GRIS, car=20))
    corps.append('<line x1="520" y1="30" x2="780" y2="30" stroke="%s" stroke-width="2.2" marker-end="url(#%s-pt)"/>' % (GRIS, ident))
    corps.append(texte(650, 48, "COMMENT ?", taille=13, gras=True, couleur=GRIS, car=20))
    corps.append(texte(115, 78, "Fonction d'usage", taille=12.5, couleur=GRIS, italique=True, car=30))
    corps.append(texte(400, 78, "Fonctions techniques", taille=12.5, couleur=GRIS, italique=True, car=30))
    corps.append(texte(690, 78, "Solutions techniques", taille=12.5, couleur=GRIS, italique=True, car=30))
    y0 = 100
    centres = []
    y = y0
    for i, (ft, sols) in enumerate(branches):
        h = max(1, len(sols)) * ligne
        centres.append(y + h / 2)
        y += h
    fu_y = (centres[0] + centres[-1]) / 2
    corps.append('<rect x="20" y="%.1f" width="190" height="64" rx="8" fill="#fff8e6" stroke="#a06a00" stroke-width="2.6"/>' % (fu_y - 32))
    corps.append(texte(115, fu_y, fonction_usage, car=20, taille=14.5, gras=True, lignes_max=3))
    # bus vertical
    corps.append('<line x1="210" y1="%.1f" x2="240" y2="%.1f" stroke="%s" stroke-width="2.2"/>' % (fu_y, fu_y, ENCRE))
    corps.append('<line x1="240" y1="%.1f" x2="240" y2="%.1f" stroke="%s" stroke-width="2.2"/>' % (centres[0], centres[-1], ENCRE))
    y = y0
    for i, (ft, sols) in enumerate(branches):
        cyb = centres[i]
        corps.append('<line x1="240" y1="%.1f" x2="270" y2="%.1f" stroke="%s" stroke-width="2.2"/>' % (cyb, cyb, ENCRE))
        tir = ' stroke-dasharray="7 5"' if (i, "ft") in v else ""
        corps.append('<rect x="270" y="%.1f" width="260" height="54" rx="6" fill="#eef4ff" stroke="#1f5fbf" stroke-width="2.4"%s/>' % (cyb - 27, tir))
        corps.append(texte(400, cyb, ft, car=30, taille=14, gras=True, ident=v.get((i, "ft")), lignes_max=2))
        n = max(1, len(sols))
        for j, s in enumerate(sols or [""]):
            sy = y + ligne * j + ligne / 2
            corps.append('<path d="M530,%.1f H555 V%.1f H585" fill="none" stroke="%s" stroke-width="2.2"/>' % (cyb, sy, ENCRE))
            tir = ' stroke-dasharray="7 5"' if (i, j) in v else ""
            corps.append('<rect x="585" y="%.1f" width="220" height="54" rx="6" fill="#e3f6e9" stroke="#16753a" stroke-width="2.4"%s/>' % (sy - 27, tir))
            corps.append(texte(695, sy, s, car=25, taille=14, gras=True, ident=v.get((i, j)), lignes_max=2))
            if n > 1 and j < n - 1:
                corps.append(texte(570, sy + ligne / 2, "ou", taille=12.5, italique=True, couleur="#16753a", car=4))
        y += n * ligne
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


# ─────────────────────────────────────────────────────────────────────────────
# Diagramme des exigences (SysML)
# ─────────────────────────────────────────────────────────────────────────────
def exigence_bloc(x, y, nom, ide, txt, l=250, h=118, vivants=None, stereotype="requirement", couleur="#1f5fbf"):
    v = vivants or {}
    p = ['<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="4" fill="#ffffff" stroke="%s" stroke-width="2.2"/>' % (x, y, l, h, couleur),
         '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>' % (x, y + 42, x + l, y + 42, couleur),
         texte(x + l / 2, y + 13, "«" + stereotype + "»", taille=11.5, couleur=GRIS, car=40),
         texte(x + l / 2, y + 30, nom, taille=14, gras=True, car=int(l / 8.5), lignes_max=1, ident=v.get("nom")),
         texte(x + 10, y + 56, "Id = " + ide, taille=12.5, ancre="start", car=40, couleur=GRIS)]
    p.append(texte(x + l / 2, y + 86, txt, taille=12.5, car=int(l / 7.2), lignes_max=3, ident=v.get("texte")))
    return "".join(p)


def exigences(ident, blocs, titre, desc, contient=(), relations=(), largeur=820, hauteur=480):
    """blocs : {cle: dict(x, y, nom, id, texte, vivants, stereotype, couleur, l, h)}.
    contient : [(parent, enfant)] — trait avec ⊕ côté parent.
    relations : [(source, cible, "verify"|"satisfy")] — flèche en tirets."""
    corps = [fleche_def(ident + "-pt", GRIS)]
    def centre_haut(b): return (b["x"] + b.get("l", 250) / 2, b["y"])
    def centre_bas(b): return (b["x"] + b.get("l", 250) / 2, b["y"] + b.get("h", 118))
    for (p, c) in contient:
        bp, bc = blocs[p], blocs[c]
        (x1, y1), (x2, y2) = centre_bas(bp), centre_haut(bc)
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (x1, y1 + 9, x2, y2, ENCRE))
        corps.append('<circle cx="%.1f" cy="%.1f" r="9" fill="#ffffff" stroke="%s" stroke-width="2"/>' % (x1, y1 + 9, ENCRE))
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (x1 - 6, y1 + 9, x1 + 6, y1 + 9, ENCRE))
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (x1, y1 + 3, x1, y1 + 15, ENCRE))
    # Règle d'or n°315 : les flèches d'une même source partent de points ÉCARTÉS sur son bord (elles ne convergent pas
    # en un point), et chaque mot «satisfy» / «verify» se pose À CÔTÉ de sa flèche, là où il ne touche ni une autre
    # flèche, ni un bloc, ni un autre mot.
    traits = []
    for (s, c, genre) in relations:
        bs, bc = blocs[s], blocs[c]
        x2, y2 = bc["x"] + bc.get("l", 250) / 2, bc["y"] + bc.get("h", 118)
        y1 = bs["y"]
        if bs["y"] < bc["y"]:
            y1, y2 = bs["y"] + bs.get("h", 118), bc["y"]
        traits.append([s, x2, y1, x2, y2, genre])
    for s in {t[0] for t in traits}:
        miens = sorted((t for t in traits if t[0] == s), key=lambda t: t[3])
        bs = blocs[s]
        for k, t in enumerate(miens):
            t[1] = bs["x"] + bs.get("l", 250) * (k + 1) / (len(miens) + 1)
    segments = [(t[1], t[2], t[3], t[4]) for t in traits]
    for (p, c) in contient:
        (xa, ya), (xb, yb) = centre_bas(blocs[p]), centre_haut(blocs[c])
        segments.append((xa, ya, xb, yb))
    obstacles = [(b["x"], b["y"], b["x"] + b.get("l", 250), b["y"] + b.get("h", 118)) for b in blocs.values()]

    def air_rect(r, q):
        dx = max(q[0] - r[2], r[0] - q[2], 0)
        dy = max(q[1] - r[3], r[1] - q[3], 0)
        return -1 if dx == 0 and dy == 0 else math.hypot(dx, dy)

    def air_segment(r, sg):
        best = 99
        for k in range(41):
            px, py = sg[0] + (sg[2] - sg[0]) * k / 40, sg[1] + (sg[3] - sg[1]) * k / 40
            dx, dy = max(r[0] - px, px - r[2], 0), max(r[1] - py, py - r[3], 0)
            if dx == 0 and dy == 0:
                return -1
            best = min(best, math.hypot(dx, dy))
        return best

    for (s, x1, y1, x2, y2, genre) in traits:
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2" stroke-dasharray="8 6" marker-end="url(#%s-pt)"/>' % (x1, y1, x2, y2, GRIS, ident))
        mot = "«" + genre + "»"
        W, H = len(mot) * 6.8, 16
        d = math.hypot(x2 - x1, y2 - y1) or 1
        nx, ny = -(y2 - y1) / d, (x2 - x1) / d
        ecart = W / 2 * abs(nx) + H / 2 * abs(ny) + 7
        candidats = []
        for t in (0.5, 0.45, 0.55, 0.4, 0.6, 0.35, 0.65, 0.3, 0.7, 0.25, 0.75):
            for cote in (1, -1):
                mx = x1 + (x2 - x1) * t + cote * ecart * nx
                my = y1 + (y2 - y1) * t + cote * ecart * ny
                r = (mx - W / 2, my - H / 2, mx + W / 2, my + H / 2)
                if r[0] < 4 or r[2] > largeur - 4 or r[1] < 4 or r[3] > hauteur - 4:
                    continue
                autres = [sg for sg in segments if sg != (x1, y1, x2, y2)]
                air = min([air_segment(r, sg) for sg in autres] + [air_rect(r, o) for o in obstacles] + [99])
                candidats.append((min(air, 16), -abs(t - 0.5), mx, my, r))
        if candidats:
            _a, _t, mx, my, r = max(candidats, key=lambda q: (q[0], q[1]))
        else:
            mx, my = (x1 + x2) / 2 + 8 + W / 2, (y1 + y2) / 2
            r = (mx - W / 2, my - H / 2, mx + W / 2, my + H / 2)
        obstacles.append(r)
        corps.append(texte(mx, my, mot, taille=12, couleur=GRIS, car=20))
    for b in blocs.values():
        corps.append(exigence_bloc(b["x"], b["y"], b["nom"], b["id"], b["texte"], l=b.get("l", 250), h=b.get("h", 118),
                                   vivants=b.get("vivants"), stereotype=b.get("stereotype", "requirement"),
                                   couleur=b.get("couleur", "#1f5fbf")))
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


# ─────────────────────────────────────────────────────────────────────────────
# Diagramme de cas d'utilisation (SysML)
# ─────────────────────────────────────────────────────────────────────────────
def acteur(x, y, nom, couleur=ENCRE, ident=None):
    p = ['<circle cx="%.1f" cy="%.1f" r="13" fill="#ffffff" stroke="%s" stroke-width="2.4"/>' % (x, y - 44, couleur),
         '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.4"/>' % (x, y - 31, x, y + 6, couleur),
         '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.4"/>' % (x - 20, y - 18, x + 20, y - 18, couleur),
         '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.4"/>' % (x, y + 6, x - 16, y + 30, couleur),
         '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.4"/>' % (x, y + 6, x + 16, y + 30, couleur),
         texte(x, y + 50, nom, taille=13.5, gras=True, car=16, lignes_max=2, ident=ident)]
    return "".join(p)


def cas_utilisation(ident, systeme, acteurs, cas, liens, titre, desc, largeur=820, hauteur=None,
                    vivants=None, acteurs_dans=None):
    """acteurs : [(cle, nom, 'g'|'d')] ; cas : [(cle, libellé)] ; liens : [(cle_acteur, cle_cas)].
    vivants : {cle : id} pour un cas ou un acteur à remplir.
    acteurs_dans : clés d'acteurs dessinés (à tort) DANS le système — pour un exercice d'erreurs."""
    v = vivants or {}
    dedans = set(acteurs_dans or ())
    n = len(cas)
    pas = 74
    hauteur = hauteur or max(380, 150 + n * pas)
    bx, bw = 240, largeur - 480
    corps = ['<rect x="%d" y="30" width="%d" height="%d" rx="6" fill="#ffffff" stroke="%s" stroke-width="2.4"/>' % (bx, bw, hauteur - 50, ENCRE),
             texte(bx + bw / 2, 52, systeme, taille=15, gras=True, car=40, lignes_max=1)]
    pos_cas = {}
    haut, bas = 100, hauteur - 60
    for i, (k, lib) in enumerate(cas):
        cy = (haut + bas) / 2 if n == 1 else haut + i * (bas - haut) / (n - 1)
        pos_cas[k] = (bx + bw / 2, cy)
    gauche = [a for a in acteurs if a[2] == "g"]
    droite = [a for a in acteurs if a[2] == "d"]
    pos_act = {}
    for groupe, x in ((gauche, 110), (droite, largeur - 110)):
        for i, (k, nom, _) in enumerate(groupe):
            y = 60 + (hauteur - 80) / (len(groupe) + 1) * (i + 1)
            pos_act[k] = (bx + 70 if k in dedans and x < largeur / 2 else (bx + bw - 70 if k in dedans else x), y)
    for (a, c) in liens:
        (x1, y1), (x2, y2) = pos_act[a], pos_cas[c]
        gauche_vers_droite = x1 < x2
        x1b = x1 + (26 if gauche_vers_droite else -26)
        x2b = x2 - 112 if gauche_vers_droite else x2 + 112
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (x1b, y1 - 18, x2b, y2, ENCRE))
    for k, lib in cas:
        x, y = pos_cas[k]
        tir = ' stroke-dasharray="7 5"' if k in v else ""
        corps.append('<ellipse cx="%.1f" cy="%.1f" rx="112" ry="29" fill="#eef4ff" stroke="#1f5fbf" stroke-width="2.4"%s/>' % (x, y, tir))
        corps.append(texte(x, y, lib, taille=13.5, gras=True, car=24, lignes_max=2, ident=v.get(k)))
    for k, nom, _ in acteurs:
        x, y = pos_act[k]
        corps.append(acteur(x, y, nom, ident=v.get(k)))
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


# ─────────────────────────────────────────────────────────────────────────────
# Carte mentale
# ─────────────────────────────────────────────────────────────────────────────
COULEURS_BRANCHES = ["#1f5fbf", "#b35c00", "#16753a", "#7a3fc7", "#b3261e", "#0f7c8c"]


# Règle d'or n°315 : deux feuilles d'une branche ne se touchent pas — 38 unités de haut, 18 d'air entre elles.
PAS_FEUILLE = 56


def carte_mentale(ident, centre, branches, titre, desc, largeur=960, hauteur=None, vivants=None):
    """branches : [(nom, [feuilles])], réparties à droite puis à gauche du centre.
    vivants : {(i,'b'): id, (i,j): id, 'centre': id}."""
    v = vivants or {}
    n = len(branches)
    droite = list(range(0, (n + 1) // 2))
    gauche = list(range((n + 1) // 2, n))
    def hauteur_cote(idx):
        return sum(max(1, len(branches[i][1])) * PAS_FEUILLE + 24 for i in idx)
    hauteur = hauteur or max(420, max(hauteur_cote(droite), hauteur_cote(gauche)) + 60)
    cx, cy = largeur / 2, hauteur / 2
    corps = []
    for cote, idx in ((1, droite), (-1, gauche)):
        y = (hauteur - hauteur_cote(idx)) / 2 + 12
        for i in idx:
            nom, feuilles = branches[i]
            coul = COULEURS_BRANCHES[i % len(COULEURS_BRANCHES)]
            h = max(1, len(feuilles)) * PAS_FEUILLE + 24
            by = y + h / 2 - 12
            bx = cx + cote * 185
            corps.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
                         % (cx + cote * 80, cy, cx + cote * 140, cy, bx - cote * 120, by, bx - cote * 78, by, coul))
            for j, f in enumerate(feuilles):
                fy = y + j * PAS_FEUILLE + 11
                fx = cx + cote * 375
                corps.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.4"/>'
                             % (bx + cote * 78, by, bx + cote * 100, by, fx - cote * 100, fy, fx - cote * 78, fy, coul))
                tir = ' stroke-dasharray="6 4"' if (i, j) in v else ""
                corps.append('<rect x="%.1f" y="%.1f" width="156" height="38" rx="19" fill="#ffffff" stroke="%s" stroke-width="1.8"%s/>' % (fx - 78, fy - 19, coul, tir))
                corps.append(texte(fx, fy, f, taille=12.5, car=22, lignes_max=2, ident=v.get((i, j))))
            tir = ' stroke-dasharray="6 4"' if (i, "b") in v else ""
            corps.append('<rect x="%.1f" y="%.1f" width="156" height="44" rx="10" fill="#ffffff" stroke="%s" stroke-width="2.6"%s/>' % (bx - 78, by - 22, coul, tir))
            corps.append(texte(bx, by, nom, taille=14.5, gras=True, couleur=coul, car=18, lignes_max=2, ident=v.get((i, "b"))))
            y += h
    corps.append('<ellipse cx="%.1f" cy="%.1f" rx="96" ry="44" fill="#fff8e6" stroke="#a06a00" stroke-width="3"/>' % (cx, cy))
    corps.append(texte(cx, cy, centre, taille=15.5, gras=True, car=16, lignes_max=3, ident=v.get("centre")))
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)
