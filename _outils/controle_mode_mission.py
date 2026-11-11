# -*- coding: utf-8 -*-
"""Le mode mission posé dans une page est celui de la source, une fois.

    python3 _outils/controle_mode_mission.py [racine]

Le mode mission (« un exercice à la fois », décision de Pascal du 11/11/2026) est une source unique,
`_outils/mode_mission/` (mission.css, mission.js), posée dans les pages par `poser.py`. Ce contrôle lit toutes
les séquences et refuse :
  · une page qui porte deux blocs ;
  · une page dont le bloc n'est pas celui de la source (une correction faite à la source doit arriver partout :
    relancer `poser.py` sur la page).
Il ne demande pas encore que toutes les séquences le portent : le pilote est le lampadaire de 5e (voir
`docs/mode-mission/PLAN.md`). Il dit combien le portent.

Sortie 0 si rien à refuser, 1 sinon, 2 si aucune séquence n'a pu être lue (règle d'or n°299 : un contrôle qui
n'a rien lu ne dit pas « tout va bien »).
"""
import importlib.util
import os
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("poser_mission", ICI / "mode_mission" / "poser.py")
poser_mission = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser_mission)
EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation", "_outils"}


def sequences(racine):
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [s for s in sous if s not in EXCLUS and not s.startswith(".banc")]
        for f in fichiers:
            if f.lower().endswith(".html") and f.lower().startswith("sequence"):
                yield os.path.join(dossier, f)


def main(argv):
    racine = argv[0] if argv else "."
    lues = avec = 0
    refus = []
    source = poser_mission.bloc()
    for chemin in sorted(sequences(racine)):
        try:
            html = pathlib.Path(chemin).read_text(encoding="utf-8")
        except OSError:
            continue
        lues += 1
        blocs = poser_mission.blocs_de(html)
        if not blocs:
            continue
        avec += 1
        if len(blocs) > 1:
            refus.append((chemin, "%d blocs du mode mission" % len(blocs)))
        elif blocs[0] != source:
            refus.append((chemin, "bloc différent de la source (relancer _outils/mode_mission/poser.py)"))
    if lues == 0:
        print("⛔ EN PANNE — aucune séquence lue sous %s. Ce contrôle n'a RIEN vérifié (règle d'or n°299)." % racine)
        return 2
    for chemin, quoi in refus:
        print("✘ %s : %s" % (chemin, quoi))
    print("%d séquence(s) lue(s) · %d portent le mode mission · %d refus" % (lues, avec, len(refus)))
    if refus:
        return 1
    print("✅ chaque page qui porte le mode mission porte celui de la source, une fois")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
