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


def svg(largeur, hauteur, titre, desc, corps, classe="schema", ident=None):
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
            montrer_famille=False):
    """bulles : liste de dicts {nom, famille, vivant(id ou None), vide(str)}.
    liens_fc : [(index_bulle, "FC1")] trait objet–bulle étiqueté.
    liens_fp : [(i, j, "FP1")] courbe bulle–objet–bulle étiquetée."""
    cx, cy = largeur / 2, hauteur / 2 + 6
    rx, ry = largeur * 0.36, hauteur * 0.36
    n = len(bulles)
    pos = []
    for k in range(n):
        a = -math.pi / 2 + 2 * math.pi * k / n
        pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
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
        (x1, y1), (x2, y2) = pos[i], pos[j]
        qx, qy = 2 * cx - (x1 + x2) / 2, 2 * cy - (y1 + y2) / 2
        for k, t in ((j, 0.9), (i, 0.1)):
            arrivees_fp[k] = ((1 - t) ** 2 * x1 + 2 * (1 - t) * t * qx + t ** 2 * x2,
                              (1 - t) ** 2 * y1 + 2 * (1 - t) * t * qy + t ** 2 * y2)
    for (k, lab) in liens_fc:
        x, y = pos[k]
        x0, y0, fx = cx, cy, 0.55
        if k in arrivees_fp:
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy) or 1
            px, py = -dy / d, dx / d
            ax, ay = arrivees_fp[k]
            signe = -1 if (ax - x) * px + (ay - y) * py > 0 else 1
            hb_ = 78 if montrer_famille else 64
            x = min(max(x + signe * 62 * px, x - 80), x + 80)   # l'extrémité reste dans la bulle
            y = min(max(y + signe * 62 * py, y - hb_ / 2 + 6), y + hb_ / 2 - 6)
            x0, y0 = cx + signe * 26 * px, cy + signe * 26 * py
            fx = 0.42
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#b3261e" stroke-width="3.2"/>'
                     % (x, y, x0, y0))
        mx, my = (x * fx + x0 * (1 - fx)), (y * fx + y0 * (1 - fx))
        etiquettes.append((mx, my, lab, "#b3261e"))
    for (i, j, lab) in liens_fp:
        (x1, y1), (x2, y2) = pos[i], pos[j]
        # Le point de contrôle est choisi pour que la courbe PASSE par le centre de l'objet.
        qx, qy = 2 * cx - (x1 + x2) / 2, 2 * cy - (y1 + y2) / 2
        corps.append('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#1f5fbf" '
                     'stroke-width="3.2"/>' % (x1, y1, qx, qy, x2, y2))
        # étiquette au quart de la courbe, côté de la seconde bulle
        t = 0.80
        ex_ = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * qx + t ** 2 * x2
        ey_ = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * qy + t ** 2 * y2
        etiquettes.append((ex_, ey_, lab, "#1f5fbf"))
    # L'objet au centre
    corps.append('<ellipse cx="%.1f" cy="%.1f" rx="98" ry="46" fill="#ffffff" stroke="%s" stroke-width="3"/>'
                 % (cx, cy, ENCRE))
    corps.append(texte(cx, cy, objet, car=16, taille=19, gras=True))
    # Les bulles
    for k, b in enumerate(bulles):
        x, y = pos[k]
        fam = b.get("famille", "neutre")
        trait, fond_b, mot = FAMILLES.get(fam, FAMILLES["neutre"])
        tirets = ' stroke-dasharray="7 5"' if fam == "vide" else ""
        hb = 78 if (montrer_famille and mot) else 64
        corps.append('<rect x="%.1f" y="%.1f" width="186" height="%d" rx="30" fill="%s" stroke="%s" '
                     'stroke-width="2.4"%s/>' % (x - 93, y - hb / 2, hb, fond_b, trait, tirets))
        if b.get("vivant"):
            corps.append(texte(x, y - (10 if montrer_famille and mot else 0), b.get("nom", ""), car=19, taille=14.5,
                               gras=True, ident=b["vivant"], lignes_max=2, vide=b.get("vide", "…"),
                               prefixe=b.get("prefixe", "")))
        else:
            corps.append(texte(x, y - (10 if montrer_famille and mot else 0), b.get("nom", ""), car=19,
                               taille=14.5, gras=True, lignes_max=2))
        if b.get("repere"):
            corps.append('<circle cx="%.1f" cy="%.1f" r="12" fill="%s"/>' % (x - 88, y - 28, trait))
            corps.append(texte(x - 88, y - 28, b["repere"], taille=13, gras=True, couleur="#ffffff", car=3))
        if montrer_famille and mot:
            corps.append(texte(x, y + 22, mot, car=30, taille=12, couleur=trait, italique=True, lignes_max=1))
    for (mx, my, lab, coul) in etiquettes:
        corps.append('<rect x="%.1f" y="%.1f" width="46" height="24" rx="6" fill="#ffffff" stroke="%s"/>'
                     % (mx - 23, my - 12, coul))
        corps.append(texte(mx, my, lab, taille=13, gras=True, couleur=coul, car=6))
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


# ─────────────────────────────────────────────────────────────────────────────
# Le besoin (bête à cornes)
# ─────────────────────────────────────────────────────────────────────────────
def bete_a_cornes(ident, a_qui, sur_quoi, objet, but, titre, desc, vivants=None, largeur=780, hauteur=470):
    """vivants : dict {"a_qui": id, "sur_quoi": id, "objet": id, "but": id} pour les cases à remplir."""
    v = vivants or {}
    corps = [fleche_def(ident + "-pt")]
    q = dict(couleur=GRIS, taille=13.5, italique=True, car=40)
    # Questions au-dessus des cases
    corps.append(texte(175, 34, "À qui le produit rend-il service ?", **q))
    corps.append(texte(605, 34, "Sur quoi le produit agit-il ?", **q))
    for (x0, cle, val) in ((40, "a_qui", a_qui), (470, "sur_quoi", sur_quoi)):
        tirets = ' stroke-dasharray="7 5"' if cle in v else ""
        corps.append('<rect x="%d" y="52" width="270" height="74" rx="12" fill="#ffffff" stroke="%s" '
                     'stroke-width="2.4"%s/>' % (x0, ENCRE, tirets))
        corps.append(texte(x0 + 135, 89, val, car=26, taille=16, gras=True, ident=v.get(cle), lignes_max=3))
    # La corne : un U qui part des deux cases et passe sous le produit
    corps.append('<path d="M175,126 C175,330 605,330 605,126" fill="none" stroke="%s" stroke-width="5" '
                 'stroke-linecap="round"/>' % ENCRE)
    # Le produit
    tirets = ' stroke-dasharray="7 5"' if "objet" in v else ""
    corps.append('<ellipse cx="390" cy="200" rx="130" ry="40" fill="#eef4ff" stroke="%s" stroke-width="3"%s/>'
                 % (ENCRE, tirets))
    corps.append(texte(390, 200, objet, car=20, taille=18, gras=True, ident=v.get("objet"), lignes_max=2))
    # Flèche vers le but
    corps.append('<line x1="390" y1="279" x2="390" y2="340" stroke="%s" stroke-width="3" marker-end="url(#%s-pt)"/>'
                 % (ENCRE, ident))
    corps.append(texte(390, 356, "Dans quel but ?", **q))
    tirets = ' stroke-dasharray="7 5"' if "but" in v else ""
    corps.append('<rect x="120" y="372" width="540" height="80" rx="12" fill="#fff8e6" stroke="%s" '
                 'stroke-width="2.4"%s/>' % ("#a06a00", tirets))
    corps.append(texte(390, 412, but, car=52, taille=16, gras=True, ident=v.get("but"), lignes_max=3))
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


def bete_vers_pieuvre(ident, a_qui, sur_quoi, objet, but, fp, fc, titre, desc, largeur=900, hauteur=420):
    """La même liaison, deux fois : la corne de la bête à cornes (à qui → par l'objet → sur quoi) devient la
    fonction principale FP1 du diagramme pieuvre. Repères ①②③ sur les deux schémas, légende en mots."""
    BLEU, ROUGE, VIO = "#1f5fbf", "#b3261e", "#6d3fb5"
    corps = [fleche_def(ident + "-pt"), fleche_def(ident + "-pg", GRIS)]

    def badge(x, y, n):
        corps.append('<circle cx="%d" cy="%d" r="13" fill="%s"/>' % (x, y, VIO))
        corps.append(texte(x, y, n, taille=14, gras=True, couleur="#ffffff", car=3))

    q = dict(couleur=GRIS, taille=12.5, italique=True, car=30)
    # ── À gauche : la bête à cornes ──
    corps.append(texte(210, 22, "La bête à cornes", taille=15, gras=True, car=30))
    corps.append(texte(110, 44, "À qui rend-il service ?", **q))
    corps.append(texte(310, 44, "Sur quoi agit-il ?", **q))
    for (x0, val) in ((30, a_qui), (230, sur_quoi)):
        corps.append('<rect x="%d" y="56" width="160" height="48" rx="10" fill="#ffffff" stroke="%s" stroke-width="2.2"/>' % (x0, ENCRE))
        corps.append(texte(x0 + 80, 80, val, car=18, taille=14.5, gras=True, lignes_max=2))
    corps.append('<path d="M110,104 C110,250 310,250 310,104" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round"/>' % BLEU)
    corps.append('<ellipse cx="210" cy="170" rx="92" ry="30" fill="#eef4ff" stroke="%s" stroke-width="2.6"/>' % ENCRE)
    corps.append(texte(210, 170, objet, car=18, taille=15, gras=True, lignes_max=2))
    corps.append('<line x1="210" y1="215" x2="210" y2="252" stroke="%s" stroke-width="2.6" marker-end="url(#%s-pt)"/>' % (ENCRE, ident))
    corps.append(texte(210, 266, "Dans quel but ?", **q))
    corps.append('<rect x="40" y="280" width="340" height="48" rx="10" fill="#fff8e6" stroke="#a06a00" stroke-width="2.2"/>')
    corps.append(texte(210, 304, but, car=40, taille=14.5, gras=True, lignes_max=2))
    badge(30, 56, "1"); badge(230, 56, "2"); badge(40, 280, "3")
    # ── Au milieu : « devient » ──
    corps.append('<line x1="418" y1="176" x2="474" y2="176" stroke="%s" stroke-width="3" marker-end="url(#%s-pg)"/>' % (GRIS, ident))
    corps.append(texte(446, 158, "devient", taille=12.5, italique=True, couleur=GRIS, car=10))
    # ── À droite : le diagramme pieuvre ──
    corps.append(texte(690, 22, "Le diagramme pieuvre", taille=15, gras=True, car=30))
    (x1, y1), (x2, y2), (cx, cy) = (565, 80), (815, 80), (690, 196)
    # point de contrôle choisi pour que la courbe PASSE par le centre de l'objet : la même forme que la corne
    qx, qy = 2 * cx - (x1 + x2) / 2, 2 * cy - (y1 + y2) / 2
    corps.append('<path d="M%d,%d Q%.1f,%.1f %d,%d" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round"/>'
                 % (x1, y1, qx, qy, x2, y2, BLEU))
    corps.append('<line x1="752" y1="186" x2="848" y2="100" stroke="%s" stroke-width="3.4"/>' % ROUGE)
    corps.append('<ellipse cx="%d" cy="%d" rx="92" ry="30" fill="#ffffff" stroke="%s" stroke-width="2.6"/>' % (cx, cy, ENCRE))
    corps.append(texte(cx, cy, objet, car=18, taille=15, gras=True, lignes_max=2))
    for (bx, by, val) in ((x1, y1, a_qui), (x2, y2, sur_quoi)):
        corps.append('<rect x="%d" y="%d" width="150" height="48" rx="22" fill="#e8f0ff" stroke="%s" stroke-width="2.2"/>' % (bx - 75, by - 24, BLEU))
        corps.append(texte(bx, by, val, car=17, taille=14.5, gras=True, lignes_max=2))
    for (ex, ey, lab, coul) in ((748, 140, "FP1", BLEU), (838, 146, "FC1", ROUGE)):
        corps.append('<rect x="%d" y="%d" width="44" height="22" rx="6" fill="#ffffff" stroke="%s"/>' % (ex - 22, ey - 11, coul))
        corps.append(texte(ex, ey, lab, taille=12.5, gras=True, couleur=coul, car=6))
    corps.append('<rect x="500" y="262" width="380" height="48" rx="10" fill="#e8f0ff" stroke="%s" stroke-width="2.2"/>' % BLEU)
    corps.append(texte(690, 286, "FP1 : " + fp, car=46, taille=14, gras=True, couleur=BLEU, lignes_max=2))
    corps.append('<rect x="500" y="320" width="380" height="40" rx="10" fill="#fdeceb" stroke="%s" stroke-width="2"/>' % ROUGE)
    corps.append(texte(690, 340, "FC1 : " + fc, car=50, taille=13, gras=True, couleur=ROUGE, lignes_max=2))
    corps.append(texte(690, 384, "Au bout de la FP1, le même élément porte souvent aussi la FC1.", taille=12.5, italique=True,
                       couleur=GRIS, car=70, lignes_max=1))
    badge(x1 - 75, y1 - 24, "1"); badge(x2 - 75, y2 - 24, "2"); badge(500, 262, "3")
    # ── Légende, en mots ──
    for k, ligne in enumerate(["① « à qui ? » → la bulle d'où part la FP1",
                               "② « sur quoi ? » → la bulle où arrive la FP1",
                               "③ « dans quel but ? » → la phrase de la FP1"]):
        corps.append(texte(30, 352 + 22 * k, ligne, ancre="start", taille=13, car=60, couleur=ENCRE, lignes_max=1))
    return svg(largeur, hauteur, titre, desc, "".join(corps), ident=ident)


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
    for (s, c, genre) in relations:
        bs, bc = blocs[s], blocs[c]
        x1, y1 = bs["x"] + bs.get("l", 250) / 2, bs["y"]
        x2, y2 = bc["x"] + bc.get("l", 250) / 2, bc["y"] + bc.get("h", 118)
        if bs["y"] < bc["y"]:
            y1, y2 = bs["y"] + bs.get("h", 118), bc["y"]
        corps.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2" stroke-dasharray="8 6" marker-end="url(#%s-pt)"/>' % (x1, y1, x2, y2, GRIS, ident))
        corps.append(texte((x1 + x2) / 2 + 8, (y1 + y2) / 2, "«" + genre + "»", taille=12, couleur=GRIS, ancre="start", car=20))
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


def carte_mentale(ident, centre, branches, titre, desc, largeur=960, hauteur=None, vivants=None):
    """branches : [(nom, [feuilles])], réparties à droite puis à gauche du centre.
    vivants : {(i,'b'): id, (i,j): id, 'centre': id}."""
    v = vivants or {}
    n = len(branches)
    droite = list(range(0, (n + 1) // 2))
    gauche = list(range((n + 1) // 2, n))
    def hauteur_cote(idx):
        return sum(max(1, len(branches[i][1])) * 46 + 24 for i in idx)
    hauteur = hauteur or max(420, max(hauteur_cote(droite), hauteur_cote(gauche)) + 60)
    cx, cy = largeur / 2, hauteur / 2
    corps = []
    for cote, idx in ((1, droite), (-1, gauche)):
        y = (hauteur - hauteur_cote(idx)) / 2 + 12
        for i in idx:
            nom, feuilles = branches[i]
            coul = COULEURS_BRANCHES[i % len(COULEURS_BRANCHES)]
            h = max(1, len(feuilles)) * 46 + 24
            by = y + h / 2 - 12
            bx = cx + cote * 185
            corps.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
                         % (cx + cote * 80, cy, cx + cote * 140, cy, bx - cote * 120, by, bx - cote * 78, by, coul))
            for j, f in enumerate(feuilles):
                fy = y + j * 46 + 11
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
