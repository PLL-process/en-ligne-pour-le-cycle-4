# -*- coding: utf-8 -*-
"""Chaque synthèse élève et chaque lexique porte le mode lecture, celui de la source, une fois.

    python3 _outils/controle_mode_lecture.py [racine] [--detail]

Le mode lecture (« une partie par écran », 25/11/2026) est le pendant du mode mission pour les documents qui se
lisent : la synthèse élève, le lexique. Demande de Pascal du 25/11/2026 : « que le mode mission soit pour tous les
documents élèves » ; une synthèse ne se joue pas, elle se lit — sur un téléphone, 8 000 px de haut d'un seul tenant.
Source unique : `_outils/mode_lecture/` (lecture.css, lecture.js), posée par `poser.py` ou par le générateur de la
page (`generer_lexique.py`).

DOCUMENT À LIRE (ce que le contrôle lit)
---------------------------------------
Sous `theme-*`, hors archive et hors `_generation/`, une page dont le nom commence par `synthese_eleve` ou `lexique`.
La synthèse du professeur n'en est pas un.

IL REFUSE
---------
  L1  un document à lire sans le bloc — sauf une page dispensée, raison écrite (`SANS_LECTURE`) ;
  L2  une page qui porte deux blocs ;
  L3  une page dont le bloc n'est pas celui de la source (relancer `mode_lecture/poser.py`, ou le générateur) ;
  L4  une dispense périmée : la page dispensée porte le bloc, ou n'existe plus.

CE QU'IL NE VOIT PAS — et qui le voit
-------------------------------------
Il lit le source : il ne dit pas que le découpage est bon, ni même qu'il y en a un. Une page d'une seule partie (un
lexique d'une seule compétence, un tableau) porte le bloc et s'ouvre telle quelle : le mode n'y fait rien.
`mode_lecture/banc_lecture.mjs` joue chaque page dans un navigateur d'élève, partie par partie, et refuse une partie
vide, un défilement de côté, du texte perdu, un lien d'ancre qui ne mène nulle part, une fiche papier amputée.

Sortie : 0 rien à refuser · 1 au moins un refus · 2 aucun document lu (règle d'or n°299).
"""
import importlib.util
import os
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("poser_lecture", ICI / "mode_lecture" / "poser.py")
poser_lecture = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser_lecture)
EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation", "_outils"}
A_LIRE = re.compile(r"^(synthese_eleve|lexique)", re.I)

#: Les pages dispensées : la fin de leur chemin → la raison, lue par qui se demande pourquoi.
SANS_LECTURE = {}


def documents(racine):
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [s for s in sous if s not in EXCLUS and not s.startswith(".banc")]
        for f in fichiers:
            if f.lower().endswith(".html") and A_LIRE.match(f):
                yield os.path.join(dossier, f)


def sorte(nom):
    return "lexique" if nom.lower().startswith("lexique") else "synthese"


def dispense(chemin):
    c = chemin.replace(os.sep, "/")
    for fin, raison in SANS_LECTURE.items():
        if c.endswith("/" + fin) or c == fin:
            return fin, raison
    return None, None


def main(argv):
    detail = "--detail" in argv
    args = [a for a in argv if not a.startswith("--")]
    racine = args[0] if args else "."
    lus = 0
    par_sorte = {}
    refus, dispenses, vues = [], [], set()
    source = poser_lecture.bloc()
    for chemin in sorted(documents(racine)):
        try:
            html = pathlib.Path(chemin).read_text(encoding="utf-8")
        except OSError:
            continue
        lus += 1
        blocs = poser_lecture.blocs_de(html)
        fin, raison = dispense(chemin)
        if fin:
            vues.add(fin)
            if blocs:
                refus.append((chemin, "L4", "dispense périmée : la page porte le mode lecture (retirer sa ligne de SANS_LECTURE)"))
            else:
                dispenses.append((chemin, raison))
            continue
        if not blocs:
            refus.append((chemin, "L1", "document à lire sans le mode lecture (mode_lecture/poser.py, ou le générateur de la page)"))
            continue
        s = sorte(os.path.basename(chemin))
        par_sorte[s] = par_sorte.get(s, 0) + 1
        if len(blocs) > 1:
            refus.append((chemin, "L2", "%d blocs du mode lecture" % len(blocs)))
        elif blocs[0] != source:
            refus.append((chemin, "L3", "bloc différent de la source (relancer _outils/mode_lecture/poser.py, ou le générateur)"))
    if lus == 0:
        print("⛔ EN PANNE — aucun document à lire sous %s. Ce contrôle n'a RIEN vérifié (règle d'or n°299)." % racine)
        return 2
    if os.path.abspath(racine) == str(ICI.parent):
        for fin in SANS_LECTURE:
            if fin not in vues:
                refus.append((fin, "L4", "dispense périmée : la page n'existe plus (retirer sa ligne de SANS_LECTURE)"))
    for chemin, code, quoi in refus:
        print("✘ %s  %s\n     %s" % (code, chemin, quoi))
    if detail:
        for chemin, raison in dispenses:
            print("· dispensée : %s — %s" % (chemin, raison))
    avec = sum(par_sorte.values())
    print("%d document(s) à lire · %d portent le mode lecture (%s) · %d dispense(s) · %d refus"
          % (lus, avec, ", ".join("%d %s" % (n, s) for s, n in sorted(par_sorte.items())), len(dispenses), len(refus)))
    if refus:
        return 1
    print("✅ chaque synthèse élève et chaque lexique porte le mode lecture, celui de la source, une fois")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
