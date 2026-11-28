# -*- coding: utf-8 -*-
"""generer.py — les trois freins de la même roue, en 3D (5e_C1.2, Sainte-Luce).

Construit de zéro, dans Blender (≥ 5.0, moteur EEVEE), trois scènes : la même roue avant dans sa fourche, avec
un frein à patins, un frein à disque, un frein à tambour. Aucun fichier .blend, aucun modèle, aucune texture venus
d'ailleurs (règle d'or n°1) : tout est écrit ici, avec l'outillage commun `_ressources-communes/blender-atelier/`.

Chaque frein est rendu DEUX fois, par deux caméras de la même scène :
  · `large` : la roue entière, son guidon et son levier — pour voir à quelle distance de l'axe ça frotte ;
  · `loupe` : le frein de près, en coupe (le plan de coupe avant de la caméra passe juste devant les pièces) —
    pour voir quelles deux surfaces se touchent.
`habiller.py` assemble ensuite les deux vues, la loupe et les pastilles numérotées ; `assembler.sh` encode.

    blender -b -P generer.py -- --sortie rendus [--freins patins,disque] [--sans-film]

Dans le Blender de Pascal (connecteur) : voir le skill `blender-visualisation-pedagogique`.

Ce que le modèle simplifie (écrit sous le film, dans la page) : l'écart entre les pièces est grossi, la roue a
seize rayons, la couleur orange montre l'endroit qui chauffe.
"""
import importlib
import json
import math
import os
import sys

import bpy
from mathutils import Vector

ICI = os.path.dirname(os.path.abspath(__file__))
for _d in (ICI, os.path.normpath(os.path.join(ICI, *([".."] * 6), "_ressources-communes", "blender-atelier"))):
    if os.path.exists(os.path.join(_d, "atelier.py")) and _d not in sys.path:
        sys.path.insert(0, _d)
import atelier as A  # noqa: E402

A = importlib.reload(A)
A.PRE = "fr_"                            # préfixe de tout ce que ce script crée : rien d'autre n'est touché

FREINS = ("patins", "disque", "tambour")
U = 0.02                                 # 1 cm de vélo = 0,02 unité de Blender
LOUPE = 480                              # côté de l'image de la loupe, en pixels
RAYONS = 16                              # une vraie roue en a 32 ou 36 : à 24 images/s, ils sembleraient reculer
T_SERRE, T_CONTACT, T_ARRET = 22, 36, 74 # on serre le levier · les pièces se touchent · la roue est arrêtée
OMEGA = math.radians(8)                  # vitesse de la roue avant le freinage, par image
ORANGE = "#ff8a3c"                       # l'endroit qui chauffe


def u(x):
    return x * U


def P(x, y, z):
    """Un point en centimètres. X vers l'avant du vélo, Y vers sa gauche (la caméra est à droite), Z vers le haut.
    L'origine est le centre de la roue."""
    return (x * U, y * U, z * U)


def marque(o, passe):
    """Cet objet n'est rendu que dans une des deux vues (« large » ou « loupe »)."""
    o["passe"] = passe
    return o


def angle_roue(i):
    """La roue tourne à vitesse constante, puis ralentit régulièrement du contact à l'arrêt."""
    if i <= T_CONTACT:
        return -OMEGA * (i - 1)
    d = T_ARRET - T_CONTACT
    t = min(i, T_ARRET) - T_CONTACT
    return -OMEGA * (T_CONTACT - 1) - OMEGA * (t - t * t / (2.0 * d))


def serrer(objet, chemin, repos, serre):
    """Une clé au repos jusqu'à T_SERRE, une clé serrée à T_CONTACT : tout ce qui suit le levier."""
    A.cle(objet, chemin, 1, repos)
    A.cle(objet, chemin, T_SERRE, repos)
    A.cle(objet, chemin, T_CONTACT, serre)


def chauffer(mat, force=0.75):
    """La matière devient orange pendant que ça frotte, et le reste : c'est là que la chaleur apparaît."""
    b = A.bsdf(mat)
    b.inputs["Emission Color"].default_value = A.hexa(ORANGE)
    s = b.inputs["Emission Strength"]
    c = b.inputs["Base Color"]
    froid = tuple(c.default_value)
    for image, valeur, teinte in ((1, 0.0, froid), (T_CONTACT, 0.0, froid), (T_ARRET, force, A.hexa("#b8541c"))):
        s.default_value = valeur
        s.keyframe_insert("default_value", frame=image)
        c.default_value = teinte
        c.keyframe_insert("default_value", frame=image)
    ad = mat.node_tree.animation_data
    if ad and ad.action:
        ad.action.name = A.PRE + "chauffe_" + mat.name
    return mat


def matieres():
    m = dict(
        pneu=A.matiere("pneu", "#232833", rug=0.85),
        alu=A.matiere("alu", "#cfd6e2", rug=0.34, metal=0.45),
        acier=A.matiere("acier", "#a9b3c4", rug=0.38, metal=0.45),
        cadre=A.matiere("cadre", "#81aaff", rug=0.42),
        sombre=A.matiere("sombre", "#4a5368", rug=0.6),
        poignee=A.matiere("poignee", "#2a2f3b", rug=0.9),
        pousse=A.matiere("pousse", "#61dafb", rug=0.42, metal=0.2),        # ce qui pousse : bras, étrier, came
        frotte=A.matiere("frotte", "#ff7b88", rug=0.75),                   # ce qui frotte sans tourner
        gaine=A.matiere("gaine", "#ffd66b", rug=0.5),                      # ce qui transmet : gaine, durite
        fil=A.matiere("fil", "#f4f7fb", rug=0.3, metal=0.4),
        cata=A.matiere("cata", "#ffb454", rug=0.4, emis="#ffb454", force=0.5),
        trou=A.matiere("trou", "#39415a", rug=0.7),
        gomme=A.matiere("gomme", "#5a6274", rug=0.85),             # la gomme du pneu, là où il est coupé
        coupe=A.matiere("coupe", "#dfe5ee", rug=0.6, emis="#dfe5ee", force=0.25),   # le métal, là où il est coupé
        machoire=A.matiere("machoire", "#7c879d", rug=0.5, metal=0.2),
    )
    m["piste"] = chauffer(A.matiere("piste", "#cfd6e2", rug=0.34, metal=0.45))   # ce qui tourne ET qui frotte
    return m


# ───────────────────────────── la roue, la fourche, le guidon : les mêmes pour les trois freins
def base(at, m, flasque_cam=(2.7, 3.2), jambe_large=False):
    """Renvoie (roue, fixe) : le repère qui tourne et celui qui ne tourne pas. Dans les deux, le plan de la roue
    est le plan XY et l'axe de la roue est Z, tourné vers la caméra (X reste l'avant, Y devient le haut)."""
    axe = at.objet("axe", None, rot=(math.pi / 2, 0, 0))
    fixe = at.objet("fixe", None, parent=axe)
    roue = at.objet("roue", None, parent=axe)
    at.objet("pneu", A.m_tore("pneu", u(30.6), u(2.2), 96, 16), mat=m["pneu"], parent=roue)
    at.objet("jante", A.m_anneau("jante", u(29.6), u(27.4), u(2.4)), mat=m["alu"], parent=roue)
    at.objet("moyeu", A.m_cyl("moyeu", u(1.3), u(8.6)), mat=m["acier"], parent=roue)
    at.objet("flasque_loin", A.m_cyl("flasque_loin", u(2.9), u(0.5)), (0, 0, -u(3.2)), mat=m["acier"], parent=roue)
    rc, zc = flasque_cam
    at.objet("flasque_cam", A.m_cyl("flasque_cam", u(rc + 0.2), u(0.5)), (0, 0, u(zc)), mat=m["acier"], parent=roue)
    for i in range(RAYONS):
        a = 2 * math.pi * i / RAYONS
        rh, zh = (rc, zc) if i % 2 == 0 else (2.7, -3.2)
        da = 0.5 if (i // 2) % 2 else -0.5
        A.tige(at, "rayon%02d" % i, (u(rh) * math.cos(a + da), u(rh) * math.sin(a + da), u(zh)),
               (u(27.5) * math.cos(a), u(27.5) * math.sin(a), 0), u(0.13), m["acier"], n=8, parent=roue)
    av = 2 * math.pi * 0.5 / RAYONS                                   # la valve, entre deux rayons
    A.tige(at, "valve", (u(27.5) * math.cos(av), u(27.5) * math.sin(av), 0),
           (u(24.4) * math.cos(av), u(24.4) * math.sin(av), 0), u(0.32), m["acier"], n=10, parent=roue)
    ac = 2 * math.pi * 6.5 / RAYONS                                   # le catadioptre : on voit la roue tourner
    at.objet("catadioptre", A.m_boite("catadioptre", u(5.6), u(2.4), u(0.9), biseau=u(0.3)),
             (u(19.5) * math.cos(ac), u(19.5) * math.sin(ac), 0), rot=(0, 0, ac + math.pi / 2), mat=m["cata"],
             parent=roue)
    for i in range(1, A.FIN + 1):
        A.cle(roue, "rotation_euler", i, (0.0, 0.0, angle_roue(i)))
    A.interpoler(roue, 'LINEAR')

    # la fourche : deux fourreaux qui se rapprochent vers le haut, une tête, un pivot
    for s in (-1, 1):
        o = A.tige(at, "fourreau%+d" % s, P(0, s * 7.0, -1.4), P(0, s * 4.6, 39.6), u(1.4), m["cadre"], n=24)
        if s < 0 and jambe_large:
            marque(o, "large")
        o = at.objet("ecrou%+d" % s, A.m_cyl("ecrou", u(1.15), u(0.9), n=6), P(0, s * 8.75, 0),
                     rot=(math.pi / 2, 0, 0), mat=m["acier"])
        if s < 0:
            marque(o, "large")
    marque(A.tige(at, "axe_roue", P(0, -8.6, 0), P(0, 8.6, 0), u(0.55), m["acier"], n=12), "large")
    at.objet("tete", A.m_boite("tete", u(3.8), u(12.4), u(3.2), biseau=u(0.6)), P(0, 0, 40.2), mat=m["cadre"])
    A.tige(at, "pivot", P(0, 0, 41), P(0, 0, 59), u(1.6), m["cadre"], n=20)
    A.tige(at, "potence", P(0, 0, 58), P(0, 0, 66.6), u(2.0), m["sombre"], n=20)
    A.tige(at, "potence_avant", P(0, 0, 65.2), P(8, 0, 67), u(1.5), m["sombre"], n=16)
    A.tige(at, "cintre", P(8, -27, 67), P(8, 27, 67), u(1.1), m["sombre"], n=16)
    for s in (-1, 1):
        A.tige(at, "poignee%+d" % s, P(8, s * 27.3, 67), P(8, s * 15, 67), u(1.65), m["poignee"], n=20)

    # le levier de frein, du côté de la caméra : il pivote vers la poignée
    at.objet("cocotte", A.m_boite("cocotte", u(2.6), u(2.6), u(2.2), biseau=u(0.4)), P(9.7, -13.0, 66.7),
             mat=m["sombre"])
    levier = at.objet("levier", None, P(10.9, -13.6, 66.3))
    A.tige(at, "levier_lame", (u(0.3), -u(0.3), 0), (u(2.6), -u(11.5), -u(0.4)), u(0.55), m["fil"], parent=levier)
    at.objet("levier_bout", A.m_sphere("levier_bout", u(0.85)), (u(2.6), -u(11.5), -u(0.4)), mat=m["fil"],
             parent=levier)
    serrer(levier, "rotation_euler", (0, 0, 0), (0, 0, -math.radians(14)))
    at.reperes["levier"] = (levier, (u(1.6), -u(6.5), 0))
    return roue, fixe


DEPART = P(9.7, -11.5, 66.7)             # là où la gaine (ou la durite) sort du levier


# ───────────────────────────── 1. le frein à patins : deux patins pincent la jante
def patins(at, m):
    roue, fixe = base(at, m)
    at.objet("piste", A.m_anneau("piste", u(29.5), u(27.6), u(2.52)), mat=m["piste"], parent=roue)
    alpha = math.atan(0.6 / 4.0)                                      # l'écart au repos, grossi : 6 mm
    hauts = {}
    for s in (-1, 1):
        A.tige(at, "bossage%+d" % s, P(1.0, s * 5.4, 24.5), P(3.7, s * 4.4, 24.5), u(0.65), m["acier"], n=12)
        bras = at.objet("bras%+d" % s, None, P(3.0, s * 4.3, 24.5))
        at.objet("bras%+d_barre" % s, A.m_boite("bras", u(1.3), u(1.0), u(11.8), biseau=u(0.3)), (0, 0, u(5.3)),
                 mat=m["pousse"], parent=bras)
        A.tige(at, "bras%+d_tenon" % s, (0, -s * u(0.4), u(4.0)), (0, -s * u(1.2), u(4.0)), u(0.45), m["acier"],
               n=10, parent=bras)
        patin = at.objet("patin%+d" % s, A.m_boite("patin", u(6.0), u(1.4), u(1.3), biseau=u(0.2)),
                         (0, -s * u(1.8), u(4.0)), mat=m["frotte"], parent=bras)
        hauts[s] = at.objet("bras%+d_haut" % s, None, (0, 0, u(10.6)), parent=bras)
        serrer(bras, "rotation_euler", (0, 0, 0), (s * alpha, 0, 0))
        if s < 0:
            at.reperes["bras"] = (bras, (0, 0, u(8.6)))
            at.reperes["patin"] = (patin, (u(3.0), 0, 0))
    # la coupe, dans la loupe seulement : le pneu (creux) et la jante, coupés juste devant les patins
    xc = 6.15
    zp, zj0, zj1 = (math.sqrt(r * r - xc * xc) for r in (30.6, 27.4, 29.6))
    for nom, rayon, mat, dx in (("coupe_pneu", 2.2, "gomme", 0.0), ("coupe_air", 1.55, "trou", 0.02)):
        o = at.objet(nom, A.m_disque(nom, u(rayon), 48), P(xc + dx, 0, zp), rot=(0, math.pi / 2, 0), mat=m[mat])
        o.scale = (30.6 / zp, 1, 1)
        marque(o, "loupe")
    marque(at.objet("coupe_jante", A.m_boite("coupe_jante", u(0.04), u(2.4), u(zj1 - zj0), biseau=0),
                    P(xc, 0, (zj0 + zj1) / 2), mat=m["coupe"]), "loupe")
    bout = P(3.0, -6.6, 35.3)                                         # la gaine s'arrête ici, le câble continue
    A.tuyau(at, "gaine", [DEPART, P(8.6, -4.5, 62), P(5.4, -3.4, 50), P(3.4, -7.8, 42), P(3.0, -8.0, 37.2), bout],
            u(0.42), m["gaine"])
    A.fil(at, "cable", bout, hauts[1], u(0.16), m["fil"])
    at.reperes["cable"] = (None, P(5.4, -3.4, 50))
    at.reperes["zone"] = (None, P(3.0, 0, 29.4))
    at.reperes["jante"] = (None, P(6.0, 0, 28.3))
    at.reperes["axe"] = (None, P(0, -8.75, 0))
    loupe = at.camera(P(34, 2.0, 31.6), P(3.0, 0, 29.4), 92)
    A.couper(loupe, P(6.6, 0, 29.4))                                 # juste devant les patins : la jante est coupée
    marque(at.lumiere("loupe", P(30, -22, 44), 3, taille=0.5, cible=P(3, 0, 29)), "loupe")
    return loupe


# ───────────────────────────── 2. le frein à disque : deux plaquettes pincent le disque
PHI = math.radians(155)                  # où l'étrier est posé sur le disque : en haut, vers l'arrière


def disque(at, m):
    roue, fixe = base(at, m)
    yd = 4.9                                                          # le disque, à 4,9 cm du milieu de la roue
    at.objet("disque", A.m_anneau("disque", u(8.0), u(5.6), u(0.4)), (0, 0, u(yd)), mat=m["piste"], parent=roue)
    at.objet("porte_disque", A.m_cyl("porte_disque", u(2.3), u(1.9)), (0, 0, u(yd - 0.85)), mat=m["acier"],
             parent=roue)
    for k in range(6):
        a = 2 * math.pi * k / 6
        at.objet("branche%d" % k, A.m_boite("branche", u(4.2), u(1.0), u(0.36), biseau=u(0.1)),
                 (u(3.9) * math.cos(a), u(3.9) * math.sin(a), u(yd)), rot=(0, 0, a), mat=m["acier"], parent=roue)
    for k in range(12):
        a = 2 * math.pi * (k + 0.5) / 12
        at.objet("trou%02d" % k, A.m_cyl("trou", u(0.5), u(0.44), n=16),
                 (u(6.8) * math.cos(a), u(6.8) * math.sin(a), u(yd)), mat=m["trou"], parent=roue)

    centre = Vector(P(7 * math.cos(PHI), -yd, 7 * math.sin(PHI)))     # le milieu de l'étrier, sur la piste
    rad = Vector((math.cos(PHI), 0, math.sin(PHI)))                   # vers l'extérieur de la roue
    tan = Vector((math.sin(PHI), 0, -math.cos(PHI)))                  # le long du disque
    etrier = at.objet("etrier", None, centre, rot=(0, math.atan2(math.cos(PHI), math.sin(PHI)), 0))
    # dans le repère de l'étrier : X le long du disque, Y en travers (− vers la caméra), Z vers l'extérieur
    at.objet("coque_ext", A.m_boite("coque_ext", u(5.4), u(1.1), u(3.5), biseau=u(0.3)), (0, -u(1.75), -u(0.45)),
             mat=m["pousse"], parent=etrier)
    at.objet("coque_int", A.m_boite("coque_int", u(5.4), u(0.45), u(3.5), biseau=u(0.15)), (0, u(1.42), -u(0.45)),
             mat=m["pousse"], parent=etrier)
    marque(at.objet("pont", A.m_boite("pont", u(5.4), u(3.95), u(1.1), biseau=u(0.3)), (0, -u(0.325), u(1.85)),
                    mat=m["pousse"], parent=etrier), "large")
    for s in (-1, 1):                                                 # −1 : la plaquette du côté de la caméra
        plq = at.objet("plaquette%+d" % s, A.m_boite("plaquette", u(3.4), u(0.6), u(2.4), biseau=u(0.12)),
                       mat=m["frotte"], parent=etrier)
        at.objet("piston%+d" % s, A.m_cyl("piston", u(0.95), u(0.55), n=24), (0, s * u(0.6), 0),
                 rot=(math.pi / 2, 0, 0), mat=m["fil"], parent=plq)
        serrer(plq, "location", (0, s * u(0.95), 0), (0, s * u(0.52), 0))   # l'écart au repos, grossi : 4 mm
        if s < 0:
            at.reperes["plaquette"] = (plq, (-u(1.9), 0, 0))
    A.tige(at, "patte_etrier", tuple(centre + rad * u(-1.0) + Vector((0, -u(2.0), 0))), P(-0.6, -6.9, 6.4), u(0.5),
           m["pousse"], n=10)
    arrivee = centre + rad * u(-0.3) + Vector((0, -u(2.3), 0))        # sur le côté de l'étrier, vers la caméra
    A.tuyau(at, "durite", [DEPART, P(8.6, -5.2, 61.5), P(3.6, -6.4, 44), P(-2.3, -7.4, 30), P(-4.9, -8.6, 15),
                           tuple(arrivee + rad * u(2.4) + Vector((0, -u(1.9), 0))),
                           tuple(arrivee + Vector((0, -u(1.5), 0))), tuple(arrivee)], u(0.42), m["gaine"])
    at.reperes["durite"] = (None, P(-2.3, -7.4, 30))
    at.reperes["etrier"] = (None, tuple(centre + Vector((0, -u(2.3), 0))))
    at.reperes["zone"] = (None, tuple(centre + Vector((0, -u(2.3), 0))))
    at.reperes["disque"] = (None, tuple(centre + tan * u(4.2)))
    at.reperes["axe"] = (None, P(0, -8.75, 0))
    loupe = at.camera(tuple(centre + rad * u(27) + tan * u(2.5)), tuple(centre + tan * u(0.3)), 82)
    A.couper(loupe, tuple(centre + rad * u(1.62)))                    # le pont de l'étrier et le haut de la roue
    marque(at.lumiere("loupe", tuple(centre + rad * u(30) + Vector((0, -u(22), 0))), 3, taille=0.5,
                      cible=tuple(centre)), "loupe")
    return loupe


# ───────────────────────────── 3. le frein à tambour : deux mâchoires s'écartent dans le tambour
def tambour(at, m):
    roue, fixe = base(at, m, flasque_cam=(4.4, 2.7), jambe_large=True)
    zt = 3.9                                                          # le milieu du tambour, vers la caméra
    at.objet("tambour", A.m_anneau("tambour", u(4.3), u(3.5), u(2.0)), (0, 0, u(zt)), mat=m["piste"], parent=roue)
    for k in range(10):                                               # des ailettes : on voit le tambour tourner
        a = 2 * math.pi * k / 10
        at.objet("ailette%d" % k, A.m_boite("ailette", u(0.45), u(0.5), u(1.9), biseau=u(0.1)),
                 (u(4.45) * math.cos(a), u(4.45) * math.sin(a), u(zt)), rot=(0, 0, a), mat=m["acier"], parent=roue)

    # ce qui ne tourne pas : le flasque (ôté dans la loupe), le pivot, les deux mâchoires, la came
    marque(at.objet("flasque", A.m_cyl("flasque", u(4.15), u(0.3), n=64), (0, 0, u(5.35)), mat=m["sombre"],
                    parent=fixe), "large")
    bloc = at.objet("bloc", None, (0, 0, u(4.0)), rot=(0, 0, -math.radians(60)), parent=fixe)   # la came vers l'avant
    at.objet("pivot_machoires", A.m_cyl("pivot_machoires", u(0.45), u(1.7), n=16), (0, -u(2.65), 0),
             mat=m["acier"], parent=bloc)
    delta = math.radians(5.4)
    for s, (d0, f0, d1, f1) in ((1, (-70, 80, -55, 65)), (-1, (100, 250, 115, 235))):
        mach = at.objet("machoire%+d" % s, None, (0, -u(2.65), 0), parent=bloc)
        at.objet("machoire%+d_corps" % s, A.m_arc("machoire", u(2.95), u(2.35), u(1.5), math.radians(d0),
                                                  math.radians(f0)), (0, u(2.65), 0), mat=m["machoire"], parent=mach)
        garn = at.objet("garniture%+d" % s, A.m_arc("garniture", u(3.25), u(2.95), u(1.5), math.radians(d1),
                                                    math.radians(f1)), (0, u(2.65), 0), mat=m["frotte"],
                        parent=mach)
        serrer(mach, "rotation_euler", (0, 0, 0), (0, 0, -s * delta))
        if s > 0:
            at.reperes["machoire"] = (garn, (u(3.1) * math.cos(math.radians(-30)),
                                             u(3.1) * math.sin(math.radians(-30)), u(0.75)))
    came = at.objet("came", None, (0, u(2.35), 0), parent=bloc)
    at.objet("came_corps", A.m_boite("came_corps", u(0.8), u(1.9), u(1.5), biseau=u(0.3)), mat=m["pousse"],
             parent=came)
    marque(at.objet("came_axe", A.m_cyl("came_axe", u(0.4), u(2.3), n=12), (0, 0, u(1.15)), mat=m["acier"],
                    parent=came), "large")
    bielle = marque(at.objet("levier_came", A.m_boite("levier_came", u(6.2), u(1.0), u(0.45), biseau=u(0.2)),
                             mat=m["pousse"], parent=came), "large")
    bielle.rotation_euler = (0, 0, math.radians(45))                  # au repos : vers l'avant, un peu vers le bas
    bielle.location = (u(2.6) * math.cos(math.radians(45)), u(2.6) * math.sin(math.radians(45)), u(1.78))
    bout = at.objet("levier_came_bout", None, (u(5.3) * math.cos(math.radians(45)),
                                               u(5.3) * math.sin(math.radians(45)), u(1.78)), parent=came)
    serrer(came, "rotation_euler", (0, 0, 0), (0, 0, math.radians(50)))
    butee = P(2.5, -6.5, 20.0)                                        # la gaine s'arrête sur la fourche
    marque(at.objet("butee", A.m_boite("butee", u(1.4), u(1.4), u(1.6), biseau=u(0.2)), butee, mat=m["sombre"]),
           "large")
    marque(A.tuyau(at, "gaine", [DEPART, P(8.6, -6.0, 61.5), P(4.2, -6.4, 45), P(2.7, -6.6, 31), butee], u(0.42),
                   m["gaine"]), "large")
    marque(A.fil(at, "cable", butee, bout, u(0.16), m["fil"]), "large")
    at.reperes["cable"] = (None, P(2.7, -6.6, 31))
    at.reperes["levier_came"] = (bout, (-u(1.6), 0, 0))
    at.reperes["zone"] = (None, P(0, -5.5, 0))
    at.reperes["tambour"] = (None, P(3.9 * math.cos(math.radians(200)), -4.9, 3.9 * math.sin(math.radians(200))))
    at.reperes["came"] = (came, (0, 0, u(0.75)))
    at.reperes["axe"] = (None, P(0, -8.75, 0))
    loupe = at.camera(P(0, -27, 0), P(0, -4, 0), 70)
    A.couper(loupe, P(0, -5.05, 0))                                   # le flasque et la fourche sont devant la coupe
    marque(at.lumiere("loupe", P(6, -30, 12), 1.1, taille=0.6, cible=P(0, -4, 0)), "loupe")
    return loupe


CONSTRUIRE = {"patins": patins, "disque": disque, "tambour": tambour}
EXPOSITION = {"patins": -0.35, "disque": -0.15, "tambour": -0.8}       # la loupe est tout près des lumières


# ───────────────────────────── construire, changer de vue, rendre
def construire(frein, fond="sombre"):
    at = A.Atelier(frein, fond)
    at.reperes = {}
    m = matieres()
    loupe = CONSTRUIRE[frein](at, m)
    large = at.camera(P(125, -208, 57), P(0, 0, 17.5), 50)
    large.data.shift_x = 0.232                                        # le vélo à gauche : la loupe viendra à droite
    at.cams = {"large": large, "loupe": loupe}
    at.exposition = {"large": 0.0, "loupe": EXPOSITION[frein]}
    at.trois_points(cible=P(0, 0, 18), k=1.25)
    passe(at, "large")
    return at


def passe(at, nom):
    """Choisit la vue : sa caméra, sa taille d'image, et les objets qui ne sont rendus que dans l'autre."""
    sc = at.sc
    for o in sc.objects:
        cache = o.get("passe") not in (None, nom)
        o.hide_render = o.hide_viewport = cache
    sc.camera = at.cams[nom]
    sc.view_settings.exposure = at.exposition[nom]
    sc.render.resolution_x, sc.render.resolution_y = (A.LARG, A.HAUT) if nom == "large" else (LOUPE, LOUPE)
    return sc


def reperes(at):
    """Où tombent, à la dernière image, les points que les pastilles désignent (en pixels, dans chaque vue)."""
    sc, sortie = at.sc, {}
    for nom in ("large", "loupe"):
        passe(at, nom)
        A.activer(sc, A.FIN)
        bpy.context.view_layer.update()
        sortie[nom] = {}
        for cle, (objet, point) in at.reperes.items():
            monde = objet.matrix_world @ Vector(point) if objet is not None else Vector(point)
            sortie[nom][cle] = A.projeter(sc, at.cams[nom], monde)
    passe(at, "large")
    return sortie


def rendre(at, frein, sortie, vues=("large", "loupe"), film=True, image=True):
    faits = []
    for nom in vues:
        passe(at, nom)
        if image:
            faits.append(A.rendre_image(at.sc, os.path.join(sortie, "%s_%s_%s.png" % (frein, nom, at.fond))))
        if film and at.fond == "sombre":
            faits.append(A.rendre_film(at.sc, os.path.join(sortie, "%s_%s_maitre.mp4" % (frein, nom))))
    passe(at, "large")
    return faits


def tout(sortie, freins=FREINS, film=True):
    os.makedirs(sortie, exist_ok=True)
    A.menage()
    for frein in freins:
        for fond in ("sombre", "clair"):
            at = construire(frein, fond)
            rendre(at, frein, sortie, film=film)
            if fond == "sombre":
                with open(os.path.join(sortie, "%s_reperes.json" % frein), "w", encoding="utf-8") as f:
                    json.dump(reperes(at), f, indent=1, sort_keys=True)
    A.menage()


if __name__ == "__main__":
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    sortie = args[args.index("--sortie") + 1] if "--sortie" in args else os.path.join(ICI, "rendus")
    freins = tuple(args[args.index("--freins") + 1].split(",")) if "--freins" in args else FREINS
    tout(os.path.abspath(sortie), freins, film="--sans-film" not in args)
