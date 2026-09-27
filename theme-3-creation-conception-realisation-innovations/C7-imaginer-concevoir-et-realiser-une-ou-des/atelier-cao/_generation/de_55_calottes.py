#!/usr/bin/env python3
"""de_55_calottes.py — engendre de_55_calottes.step, le dé fourni du TP 4e « Le dé sur sa pointe ».

Toutes les cotes viennent du nombre d'or, comme dans le modèle de référence du professeur
(Variable Studio « Variables phi ») :
  M = 89 mm (nombre de Fibonacci) · C = M/φ ≈ 55,003 mm (arête du dé)
  Rde = C/φ⁴ ≈ 8,025 mm (arêtes arrondies) · dPoint = C/φ⁴ (ouverture d'un point)
  pPoint = C/φ⁷ ≈ 1,894 mm (profondeur) · gPip = C/φ³ ≈ 12,98 mm (demi-pas de la grille)
  calotte : sphère de rayon R = (d²/4 + h²)/2h, centrée à u = R − h au-dessus de la face.
Faces opposées sommant à 7 : +Z 1 · −Z 6 · +X 2 · −X 5 · +Y 3 · −Y 4.
Le dé est CENTRÉ sur l'origine : deux rotations autour d'axes passant par l'origine mettent
sa grande diagonale à la verticale sans le déplacer.

Construit avec le noyau OpenCascade (OCP). Usage : python de_55_calottes.py → ../de_55_calottes.step
"""
import math, pathlib
from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeSphere
from OCP.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCP.TopTools import TopTools_ListOfShape
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCP.TopoDS import TopoDS
from OCP.gp import gp_Pnt
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCP.BRepCheck import BRepCheck_Analyzer

phi = (1 + 5 ** 0.5) / 2
M = 89.0
C = M / phi
Rde = C / phi ** 4
d = C / phi ** 4
h = C / phi ** 7
g = C / phi ** 3
R = (d * d / 4 + h * h) / (2 * h)
u = R - h
a = C / 2

FACES = {   # (normale, axes u et v de la face, points en (u, v))
    1: ((0, 0, 1), (1, 0, 0), (0, 1, 0), [(0, 0)]),
    6: ((0, 0, -1), (1, 0, 0), (0, 1, 0), [(-g, -g), (-g, 0), (-g, g), (g, -g), (g, 0), (g, g)]),
    2: ((1, 0, 0), (0, 1, 0), (0, 0, 1), [(-g, -g), (g, g)]),
    5: ((-1, 0, 0), (0, 1, 0), (0, 0, 1), [(-g, -g), (-g, g), (g, -g), (g, g), (0, 0)]),
    3: ((0, 1, 0), (1, 0, 0), (0, 0, 1), [(-g, -g), (0, 0), (g, g)]),
    4: ((0, -1, 0), (1, 0, 0), (0, 0, 1), [(-g, -g), (-g, g), (g, -g), (g, g)]),
}


def construire():
    cube = BRepPrimAPI_MakeBox(gp_Pnt(-a, -a, -a), C, C, C).Shape()
    f = BRepFilletAPI_MakeFillet(cube)
    ex = TopExp_Explorer(cube, TopAbs_EDGE)
    while ex.More():
        f.Add(Rde, TopoDS.Edge_s(ex.Current()))
        ex.Next()
    f.Build()
    de = f.Shape()
    outils = TopTools_ListOfShape()
    n = 0
    for (nx, ny, nz), U, V, pts in FACES.values():
        for pu, pv in pts:
            c = [pu * U[i] + pv * V[i] + (a + u) * (nx, ny, nz)[i] for i in range(3)]
            outils.Append(BRepPrimAPI_MakeSphere(gp_Pnt(*c), R).Shape())
            n += 1
    cut = BRepAlgoAPI_Cut()
    args = TopTools_ListOfShape(); args.Append(de)
    cut.SetArguments(args); cut.SetTools(outils); cut.Build()
    return cut.Shape(), n


if __name__ == '__main__':
    de, n = construire()
    gp = GProp_GProps(); BRepGProp.VolumeProperties_s(de, gp)
    k = 0; ex = TopExp_Explorer(de, TopAbs_FACE)
    while ex.More(): k += 1; ex.Next()
    out = pathlib.Path(__file__).resolve().parents[1] / 'de_55_calottes.step'
    w = STEPControl_Writer(); w.Transfer(de, STEPControl_AsIs); w.Write(str(out))
    print('points %d · faces %d · volume %.4f mm³ · valide %s · arête %.4f mm'
          % (n, k, gp.Mass(), BRepCheck_Analyzer(de).IsValid(), C))
    print('écrit', out.name, out.stat().st_size, 'octets')
