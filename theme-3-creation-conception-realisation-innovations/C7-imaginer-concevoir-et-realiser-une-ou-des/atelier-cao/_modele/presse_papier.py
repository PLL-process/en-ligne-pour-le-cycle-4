# -*- coding: utf-8 -*-
"""Le presse-papier « dé sur socle » — modèle de référence, construit hors navigateur.

Trois cotes commandent tout, comme dans la fonction Onshape :
    D = diamètre du socle, H = hauteur du socle, A = arête du dé.

Le dé est posé sur un de ses angles et CENTRÉ sur l'axe du socle : ce n'est pas
un réglage, c'est une conséquence de la construction (tout est bâti autour de
l'origine, puis pivoté autour de l'axe vertical).

Sortie : un STL prêt à imprimer + trois vues PNG.
"""
import numpy as np
import trimesh
from trimesh.creation import cylinder, box, revolve

D, H, A = 120.0, 30.0, 40.0          # mm — les trois cotes
RP, PROF, ECART = A * 0.10, A * 0.09, A * 0.25   # points : rayon, profondeur, écartement
ENFONCE = A * 0.20                    # de combien le dé s'enfonce dans le socle


def socle_mouluré():
    """Profil (r, z) tourné autour de l'axe : plinthe, tore, listel."""
    r1, r2, r3 = D / 2, D * 0.435, D * 0.385
    h1, h2 = H * 0.34, H * 0.62
    prof = [(0.0, 0.0), (r1, 0.0), (r1, h1 * 0.72)]
    # le quart de rond de la plinthe
    for t in np.linspace(0, np.pi / 2, 14):
        prof.append((r1 - (r1 - r2) * (1 - np.cos(t)), h1 * 0.72 + (h1 * 0.28) * np.sin(t)))
    prof += [(r2, h2 * 0.80)]
    # le congé du listel
    for t in np.linspace(0, np.pi / 2, 14):
        prof.append((r2 - (r2 - r3) * np.sin(t), h2 * 0.80 + (H - h2 * 0.80) * (1 - np.cos(t))))
    prof += [(r3, H), (0.0, H)]
    return revolve(np.array(prof), sections=192)


def points_du_de():
    """Les 21 points, faces opposées sommant à 7, en cylindres à soustraire."""
    plans = {
        0: [(0, 0)],                                                   # 1 → +X
        5: [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)],      # 6 → −X
        1: [(-1, -1), (1, 1)],                                         # 2 → +Y
        4: [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)],               # 5 → −Y
        2: [(-1, -1), (0, 0), (1, 1)],                                 # 3 → +Z
        3: [(-1, -1), (-1, 1), (1, -1), (1, 1)],                       # 4 → −Z
    }
    normales = {0: (1, 0, 0), 5: (-1, 0, 0), 1: (0, 1, 0),
                4: (0, -1, 0), 2: (0, 0, 1), 3: (0, 0, -1)}
    creux = []
    for k, liste in plans.items():
        n = np.array(normales[k], dtype=float)
        for (pu, pv) in liste:
            u, v = pu * ECART, pv * ECART
            c = n * (A / 2)
            libres = [i for i in range(3) if n[i] == 0]
            c[libres[0]] += u
            c[libres[1]] += v
            cyl = cylinder(radius=RP, height=PROF * 2 + 1.0, sections=48)
            # orienter le cylindre selon la normale, puis le poser à cheval sur la face
            cyl.apply_transform(trimesh.geometry.align_vectors([0, 0, 1], n))
            cyl.apply_translation(c)
            creux.append(cyl)
    return creux


def construire():
    base = socle_mouluré()
    de = box(extents=[A, A, A])
    for creux in points_du_de():
        de = de.difference(creux)

    # debout sur un angle : 45° autour de Z, puis atan(√2) autour de Y
    rz = trimesh.transformations.rotation_matrix(np.radians(45), [0, 0, 1])
    ry = trimesh.transformations.rotation_matrix(np.arctan(np.sqrt(2)), [0, 1, 0])
    de.apply_transform(ry @ rz)
    de.apply_translation([0, 0, A * np.sqrt(3) / 2 + H - ENFONCE])

    piece = base.union(de)
    piece.merge_vertices()
    return piece


if __name__ == "__main__":
    p = construire()
    print("étanche :", p.is_watertight, "| volume :", round(p.volume / 1000, 1), "cm³",
          "| hauteur totale :", round(p.bounds[1][2] - p.bounds[0][2], 1), "mm",
          "| Ø :", round(p.bounds[1][0] - p.bounds[0][0], 1), "mm")
    p.export("/home/claude/presse_papier_de_sur_socle.stl")
    print("STL écrit")
