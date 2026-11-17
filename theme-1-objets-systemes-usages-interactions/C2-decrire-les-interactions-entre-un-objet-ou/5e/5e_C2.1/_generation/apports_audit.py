# -*- coding: utf-8 -*-
"""Ce que l'audit « double regard » du 17/11/2026 a ajouté au QCM de 5e_C2.1 — par l'outil commun.

Le QCM de Shenzhen a été le premier à recevoir « Avant de commencer » (règle d'or n°337), les aides progressives et
la révision par pièges (n°339). Le moteur est commun (`_outils/qcm_aides/poser.py`) ; les données du lot sont dans
`../qcm_aides_5e_C2.1.json` (les trois lignes, les six pièges, le message du bilan). `build_qcm.py` appelle
`appliquer` après ses remplacements ; seul : `python3 apports_audit.py <qcm.html>`.
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "..", "..", "..", "..", "_outils", "qcm_aides"))
import poser  # noqa: E402

DONNEES = os.path.join(ICI, "..", "qcm_aides_5e_C2.1.json")


def appliquer(s: str) -> str:
    return poser.appliquer(s, json.load(open(DONNEES, encoding="utf-8")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    f = sys.argv[1]
    t = open(f, encoding="utf-8").read()
    u = appliquer(t)
    if u != t:
        open(f, "w", encoding="utf-8").write(u)
        print("apports de l'audit appliqués :", f)
    else:
        print("déjà appliqués :", f)
