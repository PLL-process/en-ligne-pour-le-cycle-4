# -*- coding: utf-8 -*-
"""Chaque page élève porte le mode mission, celui de la source, une fois.

    python3 _outils/controle_mode_mission.py [racine] [--detail]

Le mode mission (« un exercice à la fois », décision de Pascal du 11/11/2026) est une source unique,
`_outils/mode_mission/` (mission.css, mission.js), posée dans les pages par `poser.py` ou par le générateur de la page.

Historique : le 25/11/2026 (« que le mode mission soit pour tous les documents élèves »), ce contrôle s'est mis à
**exiger** le bloc dans les documents qui se jouent (séquences, ateliers, TP, cahiers, activités, entraînement), avec
des panneaux et cinq dispenses. **Le 26/11/2026, Pascal : « tout doit être en mode mission »** — les panneaux, les
cinq pages dispensées, les synthèses élève et les lexiques (qui avaient la veille leur « mode lecture », retiré ce
jour-là), la carte des représentations. Les QCM gardent leur moteur (sa réponse du même jour).

CE QUI EST LU
-------------
Toute page `.html` sous `theme-*`, hors archive et hors `_generation/`. Elle doit porter le bloc, SAUF si elle est
d'une de ces sortes (`HORS_MISSION`, chacune avec sa raison) :
  · un QCM (`qcm_*`, `miniquiz_*`) — son propre moteur, une question à la fois, score et « Mes erreurs » ;
  · un document pour l'enseignant (`synthese_professeur*`, `fiche_*` de l'atelier CAO pour les collègues) ;
  · une figure interactive montrée DANS un écran de sa séquence (`*_en_pieces.html`, `freins_iso.html`, en cadre) ;
  · une page de renvoi (`<meta http-equiv="refresh">`) : elle n'est jamais lue, elle mène à la page qui l'a remplacée.

IL REFUSE
---------
  M1  une page élève sans le bloc (poser.py, ou le générateur de la page) ;
  M2  une page qui porte deux blocs ;
  M3  une page dont le bloc n'est pas celui de la source (relancer `poser.py`, ou le générateur de la page) ;
  M5  une page qui porte encore le bloc du mode lecture (retiré le 26/11/2026 : `poser.py` le remplace).

Ce contrôle lit le source : il ne dit pas que le découpage est bon. `mode_mission/banc_generique.mjs` joue chaque page
qui porte le bloc, écran par écran ; `mode_mission/banc_lecture.mjs` joue les documents à lire (synthèses, lexiques).

Sortie : 0 rien à refuser · 1 au moins un refus · 2 aucune page lue (règle d'or n°299).
"""
import importlib.util
import os
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("poser_mission", ICI / "mode_mission" / "poser.py")
poser_mission = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser_mission)
EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation", "_outils"}
_LECTURE_RE = re.compile(r"<!-- mode-lecture [^ ]+ : début.*?<!-- mode-lecture [^ ]+ : fin -->", re.S)

#: Les sortes de pages qui ne portent pas le mode : motif du nom de fichier → raison.
HORS_MISSION = [
    (re.compile(r"^(qcm|miniquiz)", re.I), "QCM : son propre moteur, une question à la fois (Pascal, 26/11/2026 : « garder leur moteur »)"),
    (re.compile(r"^(synthese_professeur|fiche_)", re.I), "document pour l'enseignant"),
    (re.compile(r"(_en_pieces|^freins_iso)\.html$", re.I), "figure interactive, montrée dans un écran de sa séquence (cadre)"),
]


def documents(racine):
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [s for s in sous if s not in EXCLUS and not s.startswith(".banc")]
        if not os.path.relpath(dossier, racine).replace(os.sep, "/").startswith("theme-"):
            continue
        for f in fichiers:
            if f.lower().endswith(".html"):
                yield os.path.join(dossier, f)


_RENVOI = re.compile(r"<meta[^>]+http-equiv=[\"']?refresh", re.I)


def hors_mission(nom, html=""):
    for motif, raison in HORS_MISSION:
        if motif.search(nom):
            return raison
    if _RENVOI.search(html):
        return "page de renvoi, qui mène à la page qui l'a remplacée"
    return None


def sorte(nom):
    m = re.match(r"(sequence|atelier|tp_|cahier|activite|entrainement|synthese_eleve|lexique)", nom, re.I)
    return m.group(1).lower().rstrip("_") if m else "autre"


def main(argv):
    detail = "--detail" in argv
    args = [a for a in argv if not a.startswith("--")]
    racine = args[0] if args else "."
    lus = 0
    par_sorte = {}
    refus, hors = [], {}
    source = poser_mission.bloc()
    for chemin in sorted(documents(racine)):
        try:
            html = pathlib.Path(chemin).read_text(encoding="utf-8")
        except OSError:
            continue
        nom = os.path.basename(chemin)
        raison = hors_mission(nom, html)
        if raison:
            hors.setdefault(raison, []).append(chemin)
            continue
        lus += 1
        blocs = poser_mission.blocs_de(html)
        if _LECTURE_RE.search(html):
            refus.append((chemin, "M5", "porte encore le mode lecture, retiré le 26/11/2026 (relancer _outils/mode_mission/poser.py)"))
        if not blocs:
            refus.append((chemin, "M1", "page élève sans le mode mission (poser.py, ou le générateur de la page)"))
            continue
        s = sorte(nom)
        par_sorte[s] = par_sorte.get(s, 0) + 1
        if len(blocs) > 1:
            refus.append((chemin, "M2", "%d blocs du mode mission" % len(blocs)))
        elif blocs[0] != source:
            refus.append((chemin, "M3", "bloc différent de la source (relancer _outils/mode_mission/poser.py, ou le générateur)"))
    if lus == 0:
        print("⛔ EN PANNE — aucune page élève lue sous %s. Ce contrôle n'a RIEN vérifié (règle d'or n°299)." % racine)
        return 2
    for chemin, code, quoi in refus:
        print("✘ %s  %s\n     %s" % (code, chemin, quoi))
    if detail:
        for raison, pages in hors.items():
            print("· hors mission — %s : %d page(s)" % (raison, len(pages)))
            for c in pages:
                print("     %s" % c)
    avec = sum(par_sorte.values())
    print("%d page(s) élève lue(s) · %d portent le mode mission (%s) · hors mission : %s · %d refus"
          % (lus, avec, ", ".join("%d %s" % (n, s) for s, n in sorted(par_sorte.items())),
             ", ".join("%d %s" % (len(v), r.split(" :")[0].split(",")[0]) for r, v in hors.items()) or "aucune", len(refus)))
    if refus:
        return 1
    print("✅ chaque page élève porte le mode mission, celui de la source, une fois")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
