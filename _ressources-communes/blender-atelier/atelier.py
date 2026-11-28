# -*- coding: utf-8 -*-
"""atelier.py — l'outillage commun des films en 3D du dépôt (Blender ≥ 5.0, moteur EEVEE).

Ce module ne dessine aucun objet : il fournit ce que le script `generer.py` d'un lot emploie pour construire ses scènes
de zéro (skill du dépôt `blender-visualisation-pedagogique`) :

  · couleurs du schéma (`hexa`), formes simples (`m_boite`, `m_cyl`, `m_sphere`, `m_disque`, `m_tore`, `m_anneau`,
    `m_arc`, `tige`, `tuyau`, `fil`), matières (`matiere`, `aplat`), clés d'animation (`cle`, `interpoler`) ;
  · `Atelier` : une scène à soi, son fond (sombre pour l'écran, clair pour l'impression), sa caméra, ses lumières,
    ses pastilles numérotées ;
  · `rendre_image`, `rendre_film` : la dernière image et le film maître ;
  · `menage` : retire ce que le script a créé, et rien d'autre (tout porte le préfixe `PRE`).

    import atelier as A
    A.PRE = "fr_"                    # le préfixe du lot
    at = A.Atelier("patins", "sombre") ; … ; A.rendre_image(at.sc, chemin)

Né du premier lot (5e_C1.1, les trois appareils de Chengdu, 26/11/2026), dont le script garde sa propre copie de ces
fonctions : il a été vérifié tel quel, et sera branché ici le jour où ses films seront refaits.
Vérifié avec Blender 5.1.1 le 26/11/2026. Trois pièges de cette version sont écrits dans le skill.
"""
import math
import os
import random
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

FPS, FIN = 24, 108                      # 4,5 s : l'étape la plus courte dure 4,6 s en mode « Regarder »
LARG, HAUT = 960, 676                   # le rapport du dessin de l'animation (480 × 337,4)
FOND = {"sombre": "#071633", "clair": "#f3f6fb"}
PRE = "at_"                             # préfixe de tout ce que le script crée ; le script du lot pose le sien
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


def _adoucir(me):
    """Normales vers l'extérieur, faces lissées, arêtes vives gardées : pour une maille écrite sommet par sommet."""
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    lisser(bm)
    bm.to_mesh(me)
    bm.free()
    me.update()
    return me


def m_anneau(nom, r_ext, r_int, largeur, n=96):
    """Un anneau à section rectangulaire, d'axe Z : jante, disque, tambour."""
    sommets, faces = [], []
    for i in range(n):
        a = 2 * math.pi * i / n
        c, s = math.cos(a), math.sin(a)
        for r, z in ((r_ext, largeur / 2), (r_ext, -largeur / 2), (r_int, -largeur / 2), (r_int, largeur / 2)):
            sommets.append((r * c, r * s, z))
    for i in range(n):
        j = (i + 1) % n
        for k in range(4):
            faces.append((4 * i + k, 4 * j + k, 4 * j + (k + 1) % 4, 4 * i + (k + 1) % 4))
    me = bpy.data.meshes.new(PRE + nom)
    me.from_pydata(sommets, [], faces)
    return _adoucir(me)


def m_arc(nom, r_ext, r_int, largeur, debut, fin, n=24):
    """Un secteur d'anneau, d'axe Z, de l'angle `debut` à l'angle `fin` (radians) : mâchoire, garniture."""
    sommets, faces = [], []
    for i in range(n + 1):
        a = debut + (fin - debut) * i / n
        c, s = math.cos(a), math.sin(a)
        for r, z in ((r_ext, largeur / 2), (r_ext, -largeur / 2), (r_int, -largeur / 2), (r_int, largeur / 2)):
            sommets.append((r * c, r * s, z))
    for i in range(n):
        for k in range(4):
            faces.append((4 * i + k, 4 * (i + 1) + k, 4 * (i + 1) + (k + 1) % 4, 4 * i + (k + 1) % 4))
    faces.append((3, 2, 1, 0))
    faces.append((4 * n, 4 * n + 1, 4 * n + 2, 4 * n + 3))
    me = bpy.data.meshes.new(PRE + nom)
    me.from_pydata(sommets, [], faces)
    return _adoucir(me)


def tige(at, nom, a, b, rayon, mat, n=12, parent=None):
    """Un cylindre fin d'un point à un autre : rayon de roue, câble, durite."""
    a, b = Vector(a), Vector(b)
    o = at.objet(nom, m_cyl(nom, rayon, (b - a).length, n), (a + b) / 2, mat=mat, parent=parent)
    o.rotation_euler = (b - a).to_track_quat('Z', 'Y').to_euler()
    return o


def tuyau(at, nom, points, rayon, mat, parent=None):
    """Un tube souple qui passe par des points : gaine de câble, durite."""
    cu = bpy.data.curves.new(PRE + nom, 'CURVE')
    cu.dimensions = '3D'
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(points) - 1)
    for bp, p in zip(sp.bezier_points, points):
        bp.co = p
        bp.handle_left_type = bp.handle_right_type = 'AUTO'
    cu.resolution_u, cu.bevel_depth, cu.bevel_resolution, cu.use_fill_caps = 16, rayon, 4, True
    return at.objet(nom, cu, mat=mat, parent=parent)


def m_fil(nom, r, n=10):
    """Un cylindre de longueur 1, le long de +Y, qui part de l'origine : la contrainte « Stretch To » l'étire."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=n, radius1=r, radius2=r, depth=1.0)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(-math.pi / 2, 3, 'X'))
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0.5, 0))
    return _maille(nom, bm)


def fil(at, nom, depart, cible, rayon, mat):
    """Un fil tendu d'un point fixe à un objet qui bouge : il le suit, sans clé d'animation."""
    o = at.objet(nom, m_fil(nom, rayon), depart, mat=mat)
    c = o.constraints.new('STRETCH_TO')
    c.target, c.rest_length, c.volume = cible, 1.0, 'NO_VOLUME'
    return o


def couper(cam, point):
    """Vue en coupe sans rien découper : le plan de coupe avant de la caméra passe par `point`."""
    axe = cam.rotation_euler.to_quaternion() @ Vector((0, 0, -1))     # la caméra n'a pas de parent : sa pose suffit
    cam.data.clip_start = max(0.001, (Vector(point) - cam.location).dot(axe))


def projeter(sc, cam, point):
    """Où un point de la scène tombe dans l'image rendue, en pixels (origine en haut à gauche)."""
    from bpy_extras.object_utils import world_to_camera_view
    p = world_to_camera_view(sc, cam, Vector(point))
    return [round(p.x * sc.render.resolution_x, 1), round((1 - p.y) * sc.render.resolution_y, 1)]


# ───────────────────────────── rendre ─────────────────────────────
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
