# -*- coding: utf-8 -*-
"""generer.py — le vélo-cargo S1 de 5e_C3.1 en 3D, pour la vue que l'élève fait tourner (skill
threejs-objet-3d-pedagogique). À exécuter DANS Blender (5.1), par le connecteur : SORTIE = <dossier> ; exec(open(<ce fichier>).read()) ;
print(construire()) — écrit SORTIE/velo_cargo.glb ; puis menage().

Un modèle simplifié, dessiné pour la séquence (aucune marque, aucun modèle réel, n°1) : formes simples, une pièce = un
objet nommé (la page y accroche ses pastilles), matières NON métalliques (un métal sort noir dans three.js sans carte
d'environnement). Couleurs de la chaîne d'énergie de la séquence (n°120, n°310) : STOCKER la batterie (jaune),
DISTRIBUER le contrôleur de puissance (cyan), CONVERTIR le moteur dans le moyeu arrière (violet), câbles de l'énergie
électrique (orange). Le cadre est en aluminium (gris clair), comme le dit le tableau des trois solutions.

Les pastilles de la page se posent sur des objets vides « repere_<pièce> », placés ici du côté +Y de Blender (celui du
contrôleur et des câbles, que la vue de départ montre) : sans eux, la pastille du cadre tombait sur le bac.

Règles du skill blender-visualisation-pedagogique : préfixe tp_ sur la scène, une scène à soi, ménage à la fin, la
scène de Pascal jamais touchée.
"""
import math
import os
import bpy
from mathutils import Vector

SCENE = "tp_velo_cargo_3d"
CREES = []                          # les maillages créés ici (une jointure en laisse d'orphelins)
SORTIE = globals().get("SORTIE") or os.path.dirname(os.path.abspath(globals().get("__file__", ".")))

COULEURS = {                      # sRGB, celles du site
    "batterie": "#ffd66b", "controleur": "#61dafb", "moteur": "#c68ef2", "cable": "#ffb454",
    "cadre": "#b8c4d6", "pneu": "#2b3142", "jante": "#8d98ab", "bac": "#5b7bd5", "colis": "#d9a066",
    "selle": "#1f2633", "guidon": "#1f2633", "pedalier": "#6f7a8c",
}


def lineaire(hexa):
    """sRGB → linéaire : Blender et le glTF stockent la couleur de base en linéaire ; three.js la rend en sRGB."""
    c = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c] + [1.0]


def matiere(nom):
    m = bpy.data.materials.get("tp_" + nom) or bpy.data.materials.new("tp_" + nom)
    m.use_nodes = True
    p = m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value = lineaire(COULEURS[nom])
    p.inputs["Metallic"].default_value = 0.0
    p.inputs["Roughness"].default_value = 0.6
    return m


def menage():
    """Retire ce que ce script a créé (scène tp_…, matières tp_…), rien d'autre."""
    sc = bpy.data.scenes.get(SCENE)
    maillages = []
    if sc:
        for o in list(sc.objects):
            if o.type == "MESH":
                maillages.append(o.data)
            bpy.data.objects.remove(o, do_unlink=True)
        bpy.data.scenes.remove(sc)
    for me in maillages + CREES:               # seulement les maillages de NOS objets, jamais ceux du fichier de Pascal
        try:
            if me.users == 0:
                bpy.data.meshes.remove(me)
        except ReferenceError:                 # déjà retiré
            pass
    CREES.clear()
    for m in [m for m in bpy.data.materials if m.name.startswith("tp_")]:
        bpy.data.materials.remove(m)


def poser(obj, nom, couleur):
    obj.name = nom
    obj.data.name = nom
    obj.data.materials.clear()
    obj.data.materials.append(matiere(couleur))
    CREES.append(obj.data)
    return obj


def tube(a, b, r, nom, couleur, faces=12):
    a, b = Vector(a), Vector(b)
    d = b - a
    bpy.ops.mesh.primitive_cylinder_add(vertices=faces, radius=r, depth=d.length, location=(a + b) / 2)
    o = bpy.context.active_object
    o.rotation_mode = "QUATERNION"
    o.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(d.normalized())
    return poser(o, nom, couleur)


def boite(centre, taille, nom, couleur):
    bpy.ops.mesh.primitive_cube_add(size=1, location=centre)
    o = bpy.context.active_object
    o.scale = taille
    return poser(o, nom, couleur)


def joindre(objets, nom):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objets:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objets[0]
    bpy.ops.object.join()
    o = bpy.context.active_object
    o.name = nom
    o.data.name = nom
    return o


def roue(x, r, nom):
    y = 0.0
    bpy.ops.mesh.primitive_torus_add(major_radius=r - 0.025, minor_radius=0.025, major_segments=36, minor_segments=10,
                                     location=(x, y, r), rotation=(math.pi / 2, 0, 0))
    pneu = poser(bpy.context.active_object, nom + "_pneu", "pneu")
    bpy.ops.mesh.primitive_torus_add(major_radius=r - 0.06, minor_radius=0.01, major_segments=36, minor_segments=6,
                                     location=(x, y, r), rotation=(math.pi / 2, 0, 0))
    jante = poser(bpy.context.active_object, nom + "_jante", "jante")
    rayons = [tube((x, y, r), (x + (r - 0.07) * math.cos(k * math.pi / 8), y, r + (r - 0.07) * math.sin(k * math.pi / 8)),
                   0.004, nom + "_rayon", "jante", 4) for k in range(16)]
    return joindre([pneu, jante] + rayons, nom)


def repere(nom, ou):
    """Objet vide exporté comme nœud glTF : la page y pose la pastille de la pièce (repere_<pièce>)."""
    bpy.ops.object.empty_add(type="PLAIN_AXES", radius=0.02, location=ou)
    o = bpy.context.active_object
    o.name = "repere_" + nom
    return o


def construire():
    menage()
    precedente = bpy.context.window.scene
    sc = bpy.data.scenes.new(SCENE)
    bpy.context.window.scene = sc            # les opérateurs ajoutent à la scène de la fenêtre (piège de Blender 5.1)
    R_AR, R_AV = 0.34, 0.28                  # roue arrière, roue avant (plus petite, sous le bac)
    X_AR, X_AV = 0.0, 1.95
    pedalier = Vector((0.55, 0, 0.30))
    selle = Vector((0.40, 0, 0.92))
    tete_haut, tete_bas = Vector((1.38, 0, 1.02)), Vector((1.45, 0, 0.80))
    moyeu_ar, moyeu_av = Vector((X_AR, 0, R_AR)), Vector((X_AV, 0, R_AV))

    roue(X_AR, R_AR, "roue_arriere")
    roue(X_AV, R_AV, "roue_avant")

    # le cadre, en aluminium : un seul objet « cadre »
    t = []
    t.append(tube(selle - Vector((0, 0, 0.06)), pedalier, 0.022, "c1", "cadre"))                    # tube de selle
    t.append(tube(selle - Vector((0, 0, 0.12)), tete_haut, 0.022, "c2", "cadre"))                   # tube supérieur
    t.append(tube(pedalier, Vector((1.0, 0, 0.42)), 0.028, "c3", "cadre"))                          # tube diagonal
    t.append(tube(Vector((1.0, 0, 0.42)), Vector((1.70, 0, 0.42)), 0.028, "c4", "cadre"))           # longeron sous le bac
    t.append(tube(Vector((1.0, 0, 0.42)), tete_bas, 0.022, "c5", "cadre"))                          # vers la direction
    t.append(tube(tete_bas, tete_haut, 0.03, "c6", "cadre"))                                        # douille de direction
    for dy in (-0.06, 0.06):
        t.append(tube(pedalier + Vector((0, dy, 0)), moyeu_ar + Vector((0, dy, 0)), 0.014, "c7", "cadre"))  # bases
        t.append(tube(selle + Vector((0, dy, -0.14)), moyeu_ar + Vector((0, dy, 0)), 0.012, "c8", "cadre"))  # haubans
        t.append(tube(Vector((1.70, dy, 0.42)), moyeu_av + Vector((0, dy, 0)), 0.014, "c9", "cadre"))       # fourche avant
    cadre = joindre(t, "cadre")

    # le porte-bagages arrière, et la batterie SOUS sa plaque (texte de la séquence)
    pb = [boite((-0.02, 0, 0.84), (0.50, 0.16, 0.012), "pb1", "cadre")]
    for dy in (-0.075, 0.075):
        pb.append(tube((0.22, dy, 0.84), (0.0, dy, R_AR), 0.008, "pb2", "cadre"))
        pb.append(tube((-0.26, dy, 0.84), (0.0, dy, R_AR), 0.008, "pb3", "cadre"))
        pb.append(tube((0.22, dy, 0.84), (0.33, dy, 0.80), 0.008, "pb4", "cadre"))
    joindre(pb, "porte_bagages")
    boite((-0.02, 0, 0.79), (0.32, 0.11, 0.07), "batterie", "batterie")

    # le contrôleur de puissance, sur le tube de selle, et les câbles (énergie électrique)
    boite((0.49, 0.045, 0.56), (0.07, 0.035, 0.11), "controleur", "controleur")
    joindre([tube((0.10, 0.05, 0.76), (0.47, 0.05, 0.62), 0.007, "k1", "cable"),
             tube((0.49, 0.05, 0.50), (0.30, 0.07, 0.36), 0.007, "k2", "cable"),
             tube((0.30, 0.07, 0.36), (0.05, 0.07, R_AR + 0.02), 0.007, "k3", "cable")], "cable")

    # le moteur dans le moyeu arrière
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.085, depth=0.07, location=moyeu_ar, rotation=(math.pi / 2, 0, 0))
    poser(bpy.context.active_object, "moteur", "moteur")

    # le bac avant et son colis, la selle, le guidon, le pédalier
    bac = [boite((1.35, 0, 0.47), (0.62, 0.46, 0.02), "b0", "bac")]
    for (cx, cy, sx, sy) in ((1.35, -0.23, 0.62, 0.02), (1.35, 0.23, 0.62, 0.02), (1.045, 0, 0.02, 0.46), (1.655, 0, 0.02, 0.46)):
        bac.append(boite((cx, cy, 0.62), (sx, sy, 0.30), "b1", "bac"))
    joindre(bac, "bac")
    boite((1.30, 0.02, 0.60), (0.30, 0.26, 0.24), "colis", "colis")
    boite((selle.x - 0.02, 0, selle.z + 0.02), (0.24, 0.12, 0.05), "selle", "selle")
    joindre([tube(tete_haut, tete_haut + Vector((-0.05, 0, 0.12)), 0.014, "g1", "guidon"),
             tube(tete_haut + Vector((-0.10, -0.28, 0.13)), tete_haut + Vector((-0.10, 0.28, 0.13)), 0.014, "g2", "guidon")], "guidon")
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.09, depth=0.012, location=pedalier + Vector((0, 0.07, 0)), rotation=(math.pi / 2, 0, 0))
    plateau = poser(bpy.context.active_object, "plateau", "pedalier")
    joindre([plateau,
             tube(pedalier + Vector((0, 0.09, 0)), pedalier + Vector((0.12, 0.09, -0.12)), 0.012, "m1", "pedalier"),
             tube(pedalier + Vector((0, -0.09, 0)), pedalier + Vector((-0.12, -0.09, 0.12)), 0.012, "m2", "pedalier")], "pedalier")

    # les repères des pastilles, côté +Y, sur une face visible de chaque pièce
    repere("batterie", (-0.02, 0.06, 0.79))                  # flanc de la batterie, sous le porte-bagages
    repere("controleur", (0.49, 0.066, 0.56))                # face du boîtier
    repere("moteur", (0.0, 0.09, R_AR))                      # devant le moyeu, hors des bases et des haubans (y 0,06) qui le cachaient
    repere("cadre", (0.89, 0.025, 0.91))                     # milieu du tube supérieur

    # le sol de la scène est à z = 0 ; l'objet est centré sur x pour que la vue tourne autour de lui
    for o in sc.objects:
        o.location.x -= 0.95
    bpy.ops.object.select_all(action="DESELECT")
    chemin = os.path.join(SORTIE, "velo_cargo.glb")
    bpy.ops.export_scene.gltf(filepath=chemin, export_format="GLB", use_active_scene=True, export_apply=True,
                              export_yup=True, export_materials="EXPORT", export_cameras=False, export_lights=False,
                              export_texcoords=False)   # pas de texture : les coordonnées UV pèseraient un quart du fichier
    noms = sorted(o.name for o in sc.objects)
    bpy.context.window.scene = precedente   # rendre sa scène à la fenêtre de Pascal
    return chemin, os.path.getsize(chemin), noms

