# -*- coding: utf-8 -*-
"""Engendre les trois films « en 3D » de l'animation des trois principes (5e_C1.1, bloc #trois-principes-pas-a-pas) :
P1 lumière, P2 pesée, P3 rayonnement. Chaque scène est construite par ce script, de zéro : aucun fichier .blend,
aucun modèle ni texture venu d'ailleurs (skill du dépôt `blender-visualisation-pedagogique`).

    blender -b -P generer.py -- --sortie DOSSIER                 # les trois appareils : images fixes et films maîtres
    blender -b -P generer.py -- --sortie DOSSIER --appareils p1  # un seul
    blender -b -P generer.py -- --sortie DOSSIER --sans-film     # les images fixes seulement

Dans un Blender ouvert (connecteur) : exécuter ce fichier, puis appeler tout("DOSSIER").

CE QUI SORT, par appareil (p1_lumiere, p2_pesee, p3_rayonnement)
  <nom>_sombre.png   la dernière image, fond de la page (#071633) : l'image complète, affiche du film (n°176)
  <nom>_clair.png    la même sur fond clair, pour l'impression (n°102)
  <nom>_maitre.mp4   le film maître, 4,5 s, 24 images/s, 960 × 676, presque sans perte ;
                     assembler.sh en tire le film léger de la page

CE QUE LES FILMS RESPECTENT
  · les couleurs du schéma (n°120) : lumière #ffd08a, poussière #9bbefc, capteur #61dafb, filtre #f4f6fb,
    dépôt #4b5a78, pompe #81fba1, source #ffb454, rayonnement #c68ef2 ;
  · les mots du schéma (n°348) : les pastilles numérotées renvoient à la légende écrite dans la page ;
  · ce sont des MODÈLES SIMPLIFIÉS, pas des photos : les grains sont grossis, le rayonnement est dessiné.
    La page le dit sous chaque film.

Blender 5.x, moteur EEVEE (une carte graphique est nécessaire). Vérifié avec Blender 5.1.1 le 26/11/2026.
"""
import math
import os
import random
import sys

import bmesh
import bpy
from mathutils import Vector

FPS, FIN = 24, 108                      # 4,5 s : l'étape la plus courte dure 4,6 s en mode « Regarder »
LARG, HAUT = 960, 676                   # le rapport du dessin de l'animation (480 × 337,4)
FOND = {"sombre": "#071633", "clair": "#f3f6fb"}
PRE = "tp_"                             # préfixe de tout ce que le script crée : rien d'autre n'est touché
NOMS = {"p1": "p1_lumiere", "p2": "p2_pesee", "p3": "p3_rayonnement"}
PASTILLES = 82                          # image où les pastilles numérotées apparaissent


# ───────────────────────────── outils ─────────────────────────────
def lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def hexa(h, a=1.0):
    h = h.lstrip("#")
    return (lin(int(h[0:2], 16) / 255), lin(int(h[2:4], 16) / 255), lin(int(h[4:6], 16) / 255), a)


def menage():
    """Retire ce qu'une exécution précédente a laissé (scènes et données au préfixe PRE)."""
    for sc in [s for s in bpy.data.scenes if s.name.startswith(PRE)]:
        for o in list(sc.objects):
            bpy.data.objects.remove(o, do_unlink=True)
        bpy.data.scenes.remove(sc)
    for famille in (bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.materials, bpy.data.lights,
                    bpy.data.cameras, bpy.data.worlds, bpy.data.actions):
        for bloc in [b for b in famille if b.name.startswith(PRE) and b.users == 0]:
            famille.remove(bloc)


def lisser(bm, angle=math.radians(35)):
    for f in bm.faces:
        f.smooth = True
    for e in bm.edges:
        if len(e.link_faces) == 2 and e.calc_face_angle(0) > angle:
            e.smooth = False


def _maille(nom, bm):
    me = bpy.data.meshes.new(PRE + nom)
    lisser(bm)
    bm.to_mesh(me)
    bm.free()
    return me


def m_boite(nom, dx, dy, dz, biseau=0.02):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=(dx, dy, dz), verts=bm.verts)
    if biseau:
        bmesh.ops.bevel(bm, geom=list(bm.edges), offset=min(biseau, 0.45 * min(dx, dy, dz)), segments=3,
                        profile=0.5, affect='EDGES')
    return _maille(nom, bm)


def m_cyl(nom, r, h, n=48, bouts=True):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=bouts, cap_tris=False, segments=n, radius1=r, radius2=r, depth=h)
    return _maille(nom, bm)


def m_sphere(nom, r, u=24, v=12):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=u, v_segments=v, radius=r)
    return _maille(nom, bm)


def m_disque(nom, r, n=48):
    bm = bmesh.new()
    bmesh.ops.create_circle(bm, cap_ends=True, segments=n, radius=r)
    return _maille(nom, bm)


def m_tore(nom, grand, petit, n=48, m=12):
    sommets, faces = [], []
    for i in range(n):
        a = 2 * math.pi * i / n
        for j in range(m):
            b = 2 * math.pi * j / m
            rr = grand + petit * math.cos(b)
            sommets.append((rr * math.cos(a), rr * math.sin(a), petit * math.sin(b)))
    for i in range(n):
        for j in range(m):
            faces.append((i * m + j, ((i + 1) % n) * m + j, ((i + 1) % n) * m + (j + 1) % m, i * m + (j + 1) % m))
    me = bpy.data.meshes.new(PRE + nom)
    me.from_pydata(sommets, [], faces)
    for p in me.polygons:
        p.use_smooth = True
    me.update()
    return me


def bsdf(mat):
    return next(n for n in mat.node_tree.nodes if n.bl_idname == "ShaderNodeBsdfPrincipled")


def matiere(nom, couleur, rug=0.5, metal=0.0, emis=None, force=0.0, alpha=1.0, mode=None):
    m = bpy.data.materials.new(PRE + nom)
    b = bsdf(m)
    b.inputs["Base Color"].default_value = hexa(couleur)
    b.inputs["Roughness"].default_value = rug
    b.inputs["Metallic"].default_value = metal
    if emis:
        b.inputs["Emission Color"].default_value = hexa(emis)
        b.inputs["Emission Strength"].default_value = force
    b.inputs["Alpha"].default_value = alpha
    if mode:
        m.surface_render_method = mode
    m.diffuse_color = hexa(couleur)
    return m


def aplat(nom, couleur):
    """Une couleur exacte, sans ombre ni reflet : pour les pastilles et leurs chiffres."""
    m = bpy.data.materials.new(PRE + nom)
    t = m.node_tree
    for n in list(t.nodes):
        if n.bl_idname == "ShaderNodeBsdfPrincipled":
            t.nodes.remove(n)
    sortie = next(n for n in t.nodes if n.bl_idname == "ShaderNodeOutputMaterial")
    e = t.nodes.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = hexa(couleur)
    e.inputs["Strength"].default_value = 1.0
    t.links.new(e.outputs[0], sortie.inputs["Surface"])
    m.diffuse_color = hexa(couleur)
    return m


def courbes(bloc):
    ad = getattr(bloc, "animation_data", None)
    if not ad or not ad.action:
        return []
    act = ad.action
    if hasattr(act, "layers"):                       # Blender ≥ 4.4 : couches, bandes, sacs de canaux
        return [fc for couche in act.layers for bande in couche.strips for sac in bande.channelbags
                for fc in sac.fcurves]
    return list(act.fcurves)


def interpoler(bloc, mode, chemin=None):
    for fc in courbes(bloc):
        if chemin is None or fc.data_path == chemin:
            for k in fc.keyframe_points:
                k.interpolation = mode


def cle(cible, chemin, image, valeur):
    setattr(cible, chemin, valeur)
    cible.keyframe_insert(chemin, frame=image)


def viser(objet, cible):
    objet.rotation_euler = (Vector(cible) - objet.location).to_track_quat('-Z', 'Y').to_euler()


class Atelier:
    """Une scène et ce qu'il faut pour y poser des objets."""

    def __init__(self, cle_appareil, fond):
        self.fond = fond
        self.sc = bpy.data.scenes.new(PRE + cle_appareil + "_" + fond)
        sc = self.sc
        monde = bpy.data.worlds.new(PRE + "monde_" + cle_appareil + "_" + fond)
        ciel = next(n for n in monde.node_tree.nodes if n.bl_idname == "ShaderNodeBackground")
        ciel.inputs["Color"].default_value = hexa(FOND[fond])
        ciel.inputs["Strength"].default_value = 1.0
        if fond == "clair":
            t = monde.node_tree
            sortie = next(n for n in t.nodes if n.bl_idname == "ShaderNodeOutputWorld")
            chemin = t.nodes.new("ShaderNodeLightPath")
            ambiance = t.nodes.new("ShaderNodeBackground")
            ambiance.inputs["Color"].default_value = hexa("#aab4c6")
            ambiance.inputs["Strength"].default_value = 0.3
            melange = t.nodes.new("ShaderNodeMixShader")
            t.links.new(chemin.outputs["Is Camera Ray"], melange.inputs[0])
            t.links.new(ambiance.outputs[0], melange.inputs[1])
            t.links.new(ciel.outputs[0], melange.inputs[2])
            t.links.new(melange.outputs[0], sortie.inputs["Surface"])
        sc.world = monde
        r = sc.render
        r.engine = 'BLENDER_EEVEE'
        r.resolution_x, r.resolution_y, r.resolution_percentage = LARG, HAUT, 100
        r.fps = FPS
        r.film_transparent = False
        sc.frame_start, sc.frame_end = 1, FIN
        try:
            sc.view_settings.view_transform = 'Standard'      # les couleurs du schéma, telles quelles
            sc.view_settings.look = 'None'
        except TypeError:
            pass
        sc.eevee.taa_render_samples = 48
        self.police = None
        for f in ("segoeuib.ttf", "arialbd.ttf"):
            p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", f)
            if os.path.exists(p):
                self.police = bpy.data.fonts.load(p, check_existing=True)
                break
        clair = fond == "clair"
        self.m_pastille = aplat("pastille", "#0b1b39" if clair else "#ffffff")
        self.m_bord = aplat("pastille_bord", "#ffffff" if clair else "#0b1b39")
        self.m_chiffre = aplat("chiffre", "#ffffff" if clair else "#0b1b39")
        self.cam = None

    def objet(self, nom, donnees, loc=(0, 0, 0), rot=(0, 0, 0), mat=None, parent=None, ombre=True):
        o = bpy.data.objects.new(PRE + nom, donnees)
        o.location, o.rotation_euler = loc, rot
        if mat is not None and donnees is not None and hasattr(donnees, "materials"):
            donnees.materials.append(mat)
        self.sc.collection.objects.link(o)
        if parent is not None:
            o.parent = parent
        if not ombre:
            o.visible_shadow = False
        return o

    def camera(self, loc, cible, focale=50):
        cam = bpy.data.cameras.new(PRE + "camera")
        cam.lens = focale
        o = self.objet("camera", cam, loc)
        viser(o, cible)
        self.sc.camera = self.cam = o
        return o

    def lumiere(self, nom, loc, watts, taille=4.0, cible=(0, 0, 0), couleur="#ffffff"):
        l = bpy.data.lights.new(PRE + nom, 'AREA')
        l.energy, l.size, l.color = watts, taille, hexa(couleur)[:3]
        o = self.objet(nom, l, loc)
        viser(o, cible)
        return o

    def trois_points(self, cible=(0, 0, 0), k=1.0):
        self.lumiere("cle", (-2.6, -4.6, 3.4), 480 * k, cible=cible)
        self.lumiere("appoint", (3.2, -4.0, 0.6), 150 * k, cible=cible)
        self.lumiere("contre", (0.6, 3.2, 3.6), 300 * k, cible=cible)

    def pastille(self, n, loc, debut=PASTILLES):
        """Un disque numéroté, face à la caméra : il renvoie à la légende écrite dans la page."""
        vide = self.objet("pastille%d" % n, None, loc)
        vide.rotation_euler = self.cam.rotation_euler
        self.objet("pastille%d_bord" % n, m_disque("pastille_bord", 0.162), (0, 0, 0), mat=self.m_bord,
                   parent=vide, ombre=False)
        self.objet("pastille%d_fond" % n, m_disque("pastille_fond", 0.138), (0, 0, 0.004), mat=self.m_pastille,
                   parent=vide, ombre=False)
        txt = bpy.data.curves.new(PRE + "chiffre%d" % n, 'FONT')
        txt.body, txt.align_x, txt.align_y, txt.size = str(n), 'CENTER', 'CENTER', 0.215
        if self.police:
            txt.font = self.police
        self.objet("pastille%d_chiffre" % n, txt, (0, -0.006, 0.008), mat=self.m_chiffre, parent=vide, ombre=False)
        d = debut + 3 * (n - 1)
        k = (Vector(loc) - self.cam.location).length / 5.4       # même taille à l'image, près ou loin
        cle(vide, "scale", 1, (0.001, 0.001, 0.001))
        cle(vide, "scale", d, (0.001, 0.001, 0.001))
        cle(vide, "scale", d + 6, (1.12 * k, 1.12 * k, 1.12 * k))
        cle(vide, "scale", d + 9, (k, k, k))
        return vide

    def grains(self, nom, combien, rayon=0.02, couleur="#9bbefc", mat=None):
        maille = m_sphere(nom, rayon, 12, 6)
        maille.materials.append(mat or matiere(nom, couleur, rug=0.6, emis=couleur, force=0.35))
        return [self.objet("%s%02d" % (nom, i), maille) for i in range(combien)]


# ───────────────────────────── P1 : observer la lumière ─────────────────────────────
def p1(at):
    L, P, H, e = 1.7, 0.55, 1.15, 0.04
    zf = 0.14                                                   # hauteur du faisceau
    coque = matiere("p1_coque", "#d5dbe6", rug=0.45)
    dedans = matiere("p1_dedans", "#0e2247", rug=0.85)
    metal = matiere("p1_metal", "#7b8594", rug=0.5, metal=0.6)
    # le boîtier : cinq panneaux et leur doublure sombre, la façade à part
    for nom, d, loc in (("fond", (L, e, H), (0, P / 2, 0)), ("gauche", (e, P, H), (-L / 2, 0, 0)),
                        ("droite", (e, P, H), (L / 2, 0, 0)), ("haut", (L + e, P + e, e), (0, 0, H / 2)),
                        ("bas", (L + e, P + e, e), (0, 0, -H / 2))):
        at.objet("p1_" + nom, m_boite("p1_" + nom, *d), loc, mat=coque)
    for nom, d, loc in (("fond", (L - e, 0.008, H - e), (0, P / 2 - e / 2 - 0.006, 0)),
                        ("gauche", (0.008, P - e, H - e), (-L / 2 + e / 2 + 0.006, 0, 0)),
                        ("droite", (0.008, P - e, H - e), (L / 2 - e / 2 - 0.006, 0, 0)),
                        ("haut", (L - e, P - e, 0.008), (0, 0, H / 2 - e / 2 - 0.006)),
                        ("bas", (L - e, P - e, 0.008), (0, 0, -H / 2 + e / 2 + 0.006))):
        at.objet("p1_doublure_" + nom, m_boite("p1_doublure_" + nom, *d, biseau=0), loc, mat=dedans)
    # la façade et ses ouïes : opaques au début, puis on voit à travers
    facade = matiere("p1_facade", "#d5dbe6", rug=0.45, mode='DITHERED')
    ouies = matiere("p1_ouies", "#39424f", rug=0.7, mode='DITHERED')
    at.objet("p1_facade", m_boite("p1_facade", L + e, e, H + e), (0, -P / 2, 0), mat=facade, ombre=False)
    for i in range(9):
        at.objet("p1_ouie%d" % i, m_boite("p1_ouie", 0.5, 0.014, 0.03, biseau=0.004),
                 (0.42, -P / 2 - e / 2 - 0.004, -0.32 + i * 0.08), mat=ouies, ombre=False)
    for m in (facade, ouies):
        a = bsdf(m).inputs["Alpha"]
        for image, v in ((1, 1.0), (16, 1.0), (40, 0.0)):
            a.default_value = v
            a.keyframe_insert("default_value", frame=image)
    # le poteau de la cour, les colliers, l'antenne, l'entrée et la sortie d'air
    at.objet("p1_poteau", m_cyl("p1_poteau", 0.14, 8.0), (-L / 2 - 0.17, 0.12, 0), mat=metal)
    for z in (-0.38, 0.38):
        at.objet("p1_collier", m_boite("p1_collier", 0.5, 0.36, 0.06, biseau=0.01), (-L / 2 - 0.14, 0.1, z), mat=metal)
    noir = matiere("p1_noir", "#16181d", rug=0.5)
    at.objet("p1_antenne", m_cyl("p1_antenne", 0.022, 0.42, 16), (-0.55, 0.05, H / 2 + 0.23), mat=noir)
    at.objet("p1_antenne_pied", m_cyl("p1_antenne_pied", 0.04, 0.06, 16), (-0.55, 0.05, H / 2 + 0.04), mat=noir)
    for nom, z in (("entree", H / 2 + 0.09), ("sortie", -H / 2 - 0.09)):
        at.objet("p1_" + nom, m_cyl("p1_" + nom, 0.15, 0.16), (0, 0, z), mat=coque)
        at.objet("p1_" + nom + "_trou", m_cyl("p1_trou", 0.12, 0.165), (0, 0, z + (0.004 if z > 0 else -0.004)), mat=dedans)
    # la lampe, son faisceau, le piège à lumière
    allume = None
    xl = -L / 2 + e + 0.11
    at.objet("p1_lampe_boite", m_boite("p1_lampe_boite", 0.2, 0.2, 0.22), (xl, 0, zf), mat=matiere("p1_lampe_boite", "#2f4f8f", rug=0.5))
    m_lampe = matiere("p1_lampe", "#ffd08a", rug=0.3, emis="#ffd08a", force=0.15)
    at.objet("p1_lampe", m_sphere("p1_lampe", 0.05), (xl + 0.105, 0, zf), mat=m_lampe, ombre=False)
    x0, x1 = xl + 0.14, L / 2 - e - 0.1
    m_fx = matiere("p1_faisceau", "#000000", rug=1.0, emis="#ffd08a", force=5.0, mode='BLENDED')
    m_fx.use_backface_culling = True
    t = m_fx.node_tree
    allume = t.nodes.new("ShaderNodeValue")
    allume.label = "lampe allumée"
    coord = t.nodes.new("ShaderNodeTexCoord")
    sep = t.nodes.new("ShaderNodeSeparateXYZ")
    t.links.new(coord.outputs["Object"], sep.inputs[0])
    long = t.nodes.new("ShaderNodeMapRange")                    # fort près de la lampe, plus faible au bout
    long.inputs["From Min"].default_value, long.inputs["From Max"].default_value = -(x1 - x0) / 2, (x1 - x0) / 2
    long.inputs["To Min"].default_value, long.inputs["To Max"].default_value = 0.4, 0.95
    t.links.new(sep.outputs["Z"], long.inputs["Value"])
    face = t.nodes.new("ShaderNodeLayerWeight")
    face.inputs["Blend"].default_value = 0.35
    bord = t.nodes.new("ShaderNodeMath")                        # doux sur les bords du cylindre
    bord.operation = 'SUBTRACT'
    bord.inputs[0].default_value = 1.0
    t.links.new(face.outputs["Facing"], bord.inputs[1])
    p1x = t.nodes.new("ShaderNodeMath")
    p1x.operation = 'MULTIPLY'
    t.links.new(long.outputs[0], p1x.inputs[0])
    t.links.new(bord.outputs[0], p1x.inputs[1])
    p2x = t.nodes.new("ShaderNodeMath")
    p2x.operation = 'MULTIPLY'
    t.links.new(p1x.outputs[0], p2x.inputs[0])
    t.links.new(allume.outputs[0], p2x.inputs[1])
    t.links.new(p2x.outputs[0], bsdf(m_fx).inputs["Alpha"])
    at.objet("p1_faisceau", m_cyl("p1_faisceau", 0.05, x1 - x0, 32, bouts=False), ((x0 + x1) / 2, 0, zf),
             rot=(0, -math.pi / 2, 0), mat=m_fx, ombre=False)
    at.objet("p1_piege", m_boite("p1_piege", 0.1, 0.24, 0.28), (L / 2 - e - 0.05, 0, zf), mat=matiere("p1_piege", "#1a2a44", rug=0.9))
    lueur = bpy.data.lights.new(PRE + "p1_lueur", 'POINT')
    lueur.color, lueur.shadow_soft_size = hexa("#ffd08a")[:3], 0.06
    o_lueur = at.objet("p1_lueur", lueur, (xl + 0.2, -0.05, zf))
    force_lampe = bsdf(m_lampe).inputs["Emission Strength"]
    for image, v in ((1, 0.0), (40, 0.0), (52, 1.0)):
        allume.outputs[0].default_value = v
        allume.outputs[0].keyframe_insert("default_value", frame=image)
        force_lampe.default_value = 0.15 + 7.0 * v
        force_lampe.keyframe_insert("default_value", frame=image)
        lueur.energy = 14.0 * v
        lueur.keyframe_insert("energy", frame=image)
    # le capteur, sur le côté, sous le faisceau
    at.objet("p1_capteur", m_boite("p1_capteur", 0.42, 0.24, 0.15), (0.42, 0, -0.34), mat=matiere("p1_capteur", "#61dafb", rug=0.4))
    lentille = at.objet("p1_lentille", m_sphere("p1_lentille", 0.1), (0.42, 0, -0.265),
                        mat=matiere("p1_lentille", "#bfefff", rug=0.15, emis="#61dafb", force=0.6))
    lentille.scale = (1, 1, 0.4)
    # l'air et ses grains : chacun brille, avec un éclat, là où il traverse le faisceau
    at.camera((1.05, -4.15, 1.38), (-0.06, 0, 0.0))

    def allumee(t):
        v = t.nodes.new("ShaderNodeValue")
        v.label = "lampe allumée"
        for image, x in ((1, 0.0), (40, 0.0), (52, 1.0)):
            v.outputs[0].default_value = x
            v.outputs[0].keyframe_insert("default_value", frame=image)
        return v.outputs[0]

    def dans_le_faisceau(t, position):
        """1 quand le point est dans le faisceau, 0 dehors (distance à l'axe du faisceau)."""
        sep = t.nodes.new("ShaderNodeSeparateXYZ")
        t.links.new(position, sep.inputs[0])
        dz = t.nodes.new("ShaderNodeMath")
        dz.operation = 'SUBTRACT'
        dz.inputs[1].default_value = zf
        t.links.new(sep.outputs["Z"], dz.inputs[0])
        comb = t.nodes.new("ShaderNodeCombineXYZ")
        t.links.new(sep.outputs["Y"], comb.inputs["Y"])
        t.links.new(dz.outputs[0], comb.inputs["Z"])
        dist = t.nodes.new("ShaderNodeVectorMath")
        dist.operation = 'LENGTH'
        t.links.new(comb.outputs[0], dist.inputs[0])
        dans = t.nodes.new("ShaderNodeMapRange")
        dans.interpolation_type = 'SMOOTHSTEP'
        dans.inputs["From Min"].default_value, dans.inputs["From Max"].default_value = 0.05, 0.085
        dans.inputs["To Min"].default_value, dans.inputs["To Max"].default_value = 1.0, 0.0
        t.links.new(dist.outputs["Value"], dans.inputs["Value"])
        fois = t.nodes.new("ShaderNodeMath")
        fois.operation = 'MULTIPLY'
        t.links.new(dans.outputs[0], fois.inputs[0])
        t.links.new(allumee(t), fois.inputs[1])
        return fois.outputs[0]

    m_grain = matiere("p1_grain", "#9bbefc", rug=0.6, emis="#fff6d8", force=0.0)
    t = m_grain.node_tree
    geo = t.nodes.new("ShaderNodeNewGeometry")
    force = t.nodes.new("ShaderNodeMath")
    force.operation = 'MULTIPLY_ADD'                            # presque rien dehors, 20 dans le faisceau
    force.inputs[1].default_value, force.inputs[2].default_value = 20.0, 0.05
    t.links.new(dans_le_faisceau(t, geo.outputs["Position"]), force.inputs[0])
    t.links.new(force.outputs[0], bsdf(m_grain).inputs["Emission Strength"])
    m_eclat = matiere("p1_eclat", "#000000", rug=1.0, emis="#ffe9b0", force=9.0, mode='BLENDED')
    t = m_eclat.node_tree
    info = t.nodes.new("ShaderNodeObjectInfo")
    coord = t.nodes.new("ShaderNodeTexCoord")
    rayon = t.nodes.new("ShaderNodeVectorMath")
    rayon.operation = 'LENGTH'
    t.links.new(coord.outputs["Object"], rayon.inputs[0])
    rond = t.nodes.new("ShaderNodeMapRange")                    # plein au centre, rien au bord du disque
    rond.inputs["From Min"].default_value, rond.inputs["From Max"].default_value = 0.0, 0.085
    rond.inputs["To Min"].default_value, rond.inputs["To Max"].default_value = 1.0, 0.0
    t.links.new(rayon.outputs["Value"], rond.inputs["Value"])
    doux = t.nodes.new("ShaderNodeMath")
    doux.operation = 'POWER'
    doux.inputs[1].default_value = 2.2
    t.links.new(rond.outputs[0], doux.inputs[0])
    opaque = t.nodes.new("ShaderNodeMath")
    opaque.operation = 'MULTIPLY'
    t.links.new(doux.outputs[0], opaque.inputs[0])
    t.links.new(dans_le_faisceau(t, info.outputs["Location"]), opaque.inputs[1])
    t.links.new(opaque.outputs[0], bsdf(m_eclat).inputs["Alpha"])
    disque = m_disque("p1_eclat", 0.085, 24)
    disque.materials.append(m_eclat)
    vers_camera = (at.cam.location - Vector((0, 0, zf))).normalized() * 0.03
    alea = random.Random(511)
    haut, bas, pas = 1.6, -1.55, 0.034                          # 0,034 par image : 0,8 unité par seconde
    for i, g in enumerate(at.grains("p1_grain", 60, 0.017, mat=m_grain)):
        g.location.x, g.location.y = alea.uniform(-0.105, 0.105), alea.uniform(-0.1, 0.1)
        phase = alea.uniform(0, haut - bas)
        z = lambda f: haut - ((f * pas + phase) % (haut - bas))
        for f in range(1, FIN + 1):
            saut = f > 1 and z(f) > z(f - 1)
            if f in (1, FIN) or saut or (f < FIN and z(f + 1) > z(f)):
                g.location.z = z(f)
                g.keyframe_insert("location", index=2, frame=f)
        interpoler(g, 'LINEAR')
        e = at.objet("p1_eclat%02d" % i, disque, tuple(vers_camera), parent=g, ombre=False)
        e.rotation_euler = at.cam.rotation_euler
    at.trois_points()
    at.pastille(1, (xl - 0.02, -0.34, zf + 0.33))
    at.pastille(2, (0.46, -0.34, zf + 0.25))
    at.pastille(3, (-0.36, -0.34, -0.22))
    at.pastille(4, (0.72, -0.3, -0.08))


# ───────────────────────────── P2 : peser un filtre ─────────────────────────────
def p2(at):
    couche = (0, math.pi / 2, 0)                                # un cylindre couché le long de X
    sombre = matiere("p2_socle", "#18294a", rug=0.7)
    metal = matiere("p2_metal", "#7b8594", rug=0.5, metal=0.6)
    vert = matiere("p2_vert", "#4fae7a", rug=0.45)
    at.objet("p2_socle", m_boite("p2_socle", 3.2, 1.0, 0.07), (0.15, 0, -0.62), mat=sombre)
    for x in (-0.85, 0.75):
        at.objet("p2_support", m_boite("p2_support", 0.08, 0.5, 0.3), (x, 0, -0.45), mat=metal)
    verre = matiere("p2_verre", "#cfeede", rug=0.12, alpha=0.15, mode='BLENDED')
    verre.use_backface_culling = False
    x0, x1 = -1.25, 1.1
    at.objet("p2_tube", m_cyl("p2_tube", 0.3, x1 - x0, 64, bouts=False), ((x0 + x1) / 2, 0, 0), rot=couche, mat=verre, ombre=False)
    for nom, x in (("bride_entree", x0), ("bride_sortie", x1)):
        at.objet("p2_" + nom, m_tore("p2_bride", 0.3, 0.03), (x, 0, 0), rot=couche, mat=vert)
    # le filtre : blanc au début, gris de poussière à la fin
    xf = -0.2
    m_filtre = matiere("p2_filtre", "#f4f6fb", rug=0.9)
    at.objet("p2_filtre", m_cyl("p2_filtre", 0.285, 0.035, 64), (xf, 0, 0), rot=couche, mat=m_filtre)
    at.objet("p2_porte_filtre", m_tore("p2_porte_filtre", 0.3, 0.04), (xf, 0, 0), rot=couche, mat=matiere("p2_porte_filtre", "#22355e", rug=0.5))
    teinte = bsdf(m_filtre).inputs["Base Color"]
    propre, sale = Vector(hexa("#f4f6fb")), Vector(hexa("#4b5a78"))
    for image, part in ((1, 0.0), (14, 0.0), (100, 0.82)):
        teinte.default_value = propre.lerp(sale, part)
        teinte.keyframe_insert("default_value", frame=image)
    # la pompe : une hélice dans le tube, son moteur au bout
    at.objet("p2_moteur", m_cyl("p2_moteur", 0.34, 0.5, 48), (x1 + 0.28, 0, 0), rot=couche, mat=matiere("p2_moteur", "#17603a", rug=0.5))
    xh = 0.72
    at.objet("p2_axe", m_cyl("p2_axe", 0.025, x1 - xh, 16), ((xh + x1) / 2, 0, 0), rot=couche, mat=metal)
    helice = at.objet("p2_helice", None, (xh, 0, 0))
    pale = matiere("p2_pale", "#81fba1", rug=0.4)
    at.objet("p2_moyeu", m_sphere("p2_moyeu", 0.065), (0, 0, 0), mat=pale, parent=helice)
    for i in range(3):
        a = i * 2 * math.pi / 3
        o = at.objet("p2_pale%d" % i, m_boite("p2_pale", 0.02, 0.1, 0.2, biseau=0.008),
                     (0, -0.15 * math.sin(a), 0.15 * math.cos(a)), rot=(a, 0, 0), mat=pale, parent=helice)
        o.rotation_euler.rotate_axis('Z', math.radians(28))     # des pales inclinées, comme un ventilateur
    cle(helice, "rotation_euler", 1, (0, 0, 0))
    cle(helice, "rotation_euler", FIN, (2 * math.pi * 5, 0, 0))
    interpoler(helice, 'LINEAR')
    # l'air aspiré : chaque grain file vers le filtre et s'y arrête
    alea = random.Random(512)
    pas = 0.046
    for g in at.grains("p2_grain", 44, 0.024):
        r, a = 0.24 * math.sqrt(alea.random()), alea.uniform(0, 2 * math.pi)
        arrivee = alea.uniform(10, 150)
        g.location = (xf - 0.03 - pas * (arrivee - 1), r * math.cos(a), r * math.sin(a))
        g.keyframe_insert("location", index=0, frame=1)
        g.location.x = xf - 0.03
        g.keyframe_insert("location", index=0, frame=arrivee)
        interpoler(g, 'LINEAR')
    at.camera((-2.75, -3.6, 1.2), (0.12, 0, -0.2))
    at.trois_points(k=1.1)
    at.pastille(1, (x0 - 0.2, -0.4, 0.56))
    at.pastille(2, (xf, -0.4, 0.6))
    at.pastille(3, (xh + 0.1, -0.4, 0.62))


# ───────────────────────────── P3 : freiner un rayonnement ─────────────────────────────
def p3(at):
    sombre = matiere("p3_socle", "#18294a", rug=0.7)
    metal = matiere("p3_metal", "#7b8594", rug=0.5, metal=0.6)
    at.objet("p3_socle", m_boite("p3_socle", 3.4, 1.2, 0.07), (0, 0.1, -1.05), mat=sombre)
    at.objet("p3_colonne", m_boite("p3_colonne", 0.14, 0.14, 2.2), (0, 0.55, 0.05), mat=metal)
    for z in (0.92, -0.74):
        at.objet("p3_bras", m_boite("p3_bras", 0.1, 0.56, 0.08, biseau=0.01), (0, 0.28, z), mat=metal)
    # la source scellée, dans sa capsule
    at.objet("p3_source", m_cyl("p3_source", 0.17, 0.34, 40), (0, 0, 0.8), mat=matiere("p3_source", "#3a2a10", rug=0.5))
    ambre = matiere("p3_ambre", "#ffb454", rug=0.4, emis="#ffb454", force=0.8)
    for z in (0.64, 0.96):
        at.objet("p3_anneau", m_tore("p3_anneau", 0.172, 0.022, 40), (0, 0, z), mat=ambre)
    # la bande de papier filtre, entre ses deux rouleaux
    at.objet("p3_bande", m_boite("p3_bande", 2.6, 0.46, 0.014, biseau=0), (0, 0, 0), mat=matiere("p3_bande", "#dfe6f2", rug=0.95))
    rouleau = matiere("p3_rouleau", "#1a2a44", rug=0.6)
    lisere = matiere("p3_lisere", "#9bbefc", rug=0.5)
    for x in (-1.3, 1.3):
        at.objet("p3_rouleau", m_cyl("p3_rouleau", 0.2, 0.56, 40), (x, 0, -0.207), rot=(math.pi / 2, 0, 0), mat=rouleau)
        for y in (-0.28, 0.28):
            at.objet("p3_lisere", m_tore("p3_lisere", 0.2, 0.018, 40), (x, y, -0.207), rot=(math.pi / 2, 0, 0), mat=lisere)
        at.objet("p3_pied", m_boite("p3_pied", 0.1, 0.1, 0.62), (x, 0.36, -0.7), mat=metal)
        at.objet("p3_essieu", m_cyl("p3_essieu", 0.03, 0.8, 16), (x, 0.08, -0.207), rot=(math.pi / 2, 0, 0), mat=metal)
    # le compteur, sous la bande
    at.objet("p3_compteur", m_boite("p3_compteur", 0.5, 0.42, 0.26), (0, 0, -0.72), mat=matiere("p3_compteur", "#61dafb", rug=0.4))
    at.objet("p3_fenetre", m_cyl("p3_fenetre", 0.15, 0.02, 40), (0, 0, -0.585), mat=matiere("p3_fenetre", "#bfefff", rug=0.15, emis="#61dafb", force=0.5))
    # l'air arrive par une buse et dépose sa poussière
    bouche, depart = Vector((-0.3, 0, 0.2)), Vector((-2.3, 0, 1.49))   # le tuyau sort du cadre
    axe = bouche - depart
    cachette = bouche - axe.normalized() * 0.45                 # dans le tuyau, avant de sortir
    buse = at.objet("p3_buse", m_cyl("p3_buse", 0.075, axe.length, 32), (depart + bouche) / 2, mat=matiere("p3_buse", "#b8c7e6", rug=0.4))
    buse.rotation_euler = axe.to_track_quat('Z', 'Y').to_euler()
    m_tache = matiere("p3_tache", "#4b5a78", rug=0.95, mode='DITHERED')
    tache = at.objet("p3_tache", m_disque("p3_tache", 0.2), (0, 0, 0.0085), mat=m_tache, ombre=False)
    a = bsdf(m_tache).inputs["Alpha"]
    for image, v in ((1, 0.0), (28, 0.0), (100, 0.96)):
        a.default_value = v
        a.keyframe_insert("default_value", frame=image)
    cle(tache, "scale", 28, (0.55, 0.55, 1))
    cle(tache, "scale", 100, (1, 1, 1))
    alea = random.Random(513)
    for i, g in enumerate(at.grains("p3_grain", 26, 0.022)):
        r, ang = 0.15 * math.sqrt(alea.random()), alea.uniform(0, 2 * math.pi)
        depart_f = 24 + i * 3.1
        cle(g, "location", 1, tuple(cachette))
        cle(g, "location", depart_f, tuple(cachette))
        cle(g, "location", depart_f + 6, tuple(bouche))
        cle(g, "location", depart_f + 11, (r * math.cos(ang), r * math.sin(ang), 0.02))
        interpoler(g, 'LINEAR')
    # le rayonnement, dessiné en points : beaucoup traversent au début, peu à la fin
    m_beta = aplat("p3_beta", "#c68ef2")
    cache, pas = (0.001, 0.001, 0.001), 0.055
    for i, g in enumerate(at.grains("p3_beta", 70, 0.028, mat=m_beta)):
        r, ang = 0.085 * math.sqrt(alea.random()), alea.uniform(0, 2 * math.pi)
        x, y = r * math.cos(ang), r * math.sin(ang)
        depart_f = 4 + i * 1.5
        bande_f = depart_f + (0.6 - 0.02) / pas
        chance = 0.92 if bande_f < 34 else max(0.2, 0.92 - 0.72 * (bande_f - 34) / 60)
        passe = (i * 0.618034) % 1.0 < chance
        fin_f = bande_f + (0.57 / pas if passe else 0)
        cle(g, "location", depart_f, (x, y, 0.6))
        cle(g, "location", fin_f, (x, y, -0.57 if passe else 0.02))
        cle(g, "scale", 1, cache)
        cle(g, "scale", depart_f - 1, cache)
        cle(g, "scale", depart_f, (1, 1, 1))
        cle(g, "scale", fin_f, (1, 1, 1))
        cle(g, "scale", fin_f + 1, cache)
        interpoler(g, 'LINEAR', "location")
        interpoler(g, 'CONSTANT', "scale")
    at.camera((1.7, -5.2, 2.5), (0, 0, -0.1))
    at.trois_points(k=0.9)
    at.pastille(1, (0.44, -0.3, 0.92))
    at.pastille(2, (-0.9, -0.36, 0.2))
    at.pastille(3, (0.5, -0.36, 0.16))
    at.pastille(4, (0.52, -0.36, -0.62))


APPAREILS = {"p1": p1, "p2": p2, "p3": p3}


# ───────────────────────────── construire, rendre ─────────────────────────────
def construire(cle_appareil, fond="sombre"):
    at = Atelier(cle_appareil, fond)
    APPAREILS[cle_appareil](at)
    at.sc.frame_set(FIN)
    return at.sc


def activer(sc, image=None):
    """`render.render(scene=…)` recopie l'image courante de la scène de la fenêtre dans la scène rendue :
    on met donc notre scène dans la fenêtre, et la même image partout, avant de rendre."""
    gestion = bpy.context.window_manager
    fenetre = bpy.context.window or (gestion.windows[0] if gestion.windows else None)
    if fenetre is not None:
        fenetre.scene = sc
    if image is not None:
        sc.frame_set(image)
        autre = bpy.context.scene
        if autre is not None and autre != sc:
            autre.frame_current = image


def rendre_image(sc, chemin, image=FIN):
    r, ims = sc.render, sc.render.image_settings
    if hasattr(ims, "media_type"):
        ims.media_type = 'IMAGE'
    ims.file_format, ims.color_mode = 'PNG', 'RGB'
    r.filepath = chemin
    activer(sc, image)
    bpy.ops.render.render(write_still=True, scene=sc.name)
    return chemin


def regler_film(sc, chemin):
    r, ims = sc.render, sc.render.image_settings
    if hasattr(ims, "media_type"):
        ims.media_type = 'VIDEO'
    ims.file_format = 'FFMPEG'
    f = r.ffmpeg
    f.format, f.codec, f.constant_rate_factor, f.ffmpeg_preset = 'MPEG4', 'H264', 'PERC_LOSSLESS', 'GOOD'
    f.audio_codec, f.gopsize = 'NONE', 12
    r.use_file_extension = False
    r.filepath = chemin


def rendre_film(sc, chemin):
    regler_film(sc, chemin)
    activer(sc)
    bpy.ops.render.render(animation=True, scene=sc.name)
    return chemin


def tout(sortie, appareils=("p1", "p2", "p3"), film=True):
    os.makedirs(sortie, exist_ok=True)
    menage()
    faits = []
    for k in appareils:
        nom = NOMS[k]
        sc = construire(k, "sombre")
        faits.append(rendre_image(sc, os.path.join(sortie, nom + "_sombre.png")))
        if film:
            faits.append(rendre_film(sc, os.path.join(sortie, nom + "_maitre.mp4")))
        faits.append(rendre_image(construire(k, "clair"), os.path.join(sortie, nom + "_clair.png")))
    return faits


if __name__ == "__main__" and "--" in sys.argv:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--appareils", nargs="+", default=["p1", "p2", "p3"], choices=sorted(APPAREILS))
    ap.add_argument("--sans-film", action="store_true")
    args = ap.parse_args(sys.argv[sys.argv.index("--") + 1:])
    for chemin in tout(args.sortie, args.appareils, film=not args.sans_film):
        print("écrit :", chemin)
