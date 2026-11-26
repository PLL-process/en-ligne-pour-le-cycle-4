# -*- coding: utf-8 -*-
"""Chaque document élève porte le mode mission, celui de la source, une fois.

    python3 _outils/controle_mode_mission.py [racine] [--detail]

Le mode mission (« un exercice à la fois », décision de Pascal du 11/11/2026) est une source unique,
`_outils/mode_mission/` (mission.css, mission.js), posée dans les pages par `poser.py` ou par le générateur de la page.

**Depuis le 25/11/2026** (demande de Pascal : « que le mode mission soit pour tous les documents élèves ») ce contrôle
ne se contente plus de vérifier le bloc là où il est : il **exige** qu'il soit là. Mesure du jour, avant : 60 séquences
sur 60 le portaient, et aucun des 32 autres documents élèves (ateliers, cahiers, TP, activités, entraînement).

DOCUMENT ÉLÈVE (ce que le contrôle lit)
---------------------------------------
Sous `theme-*`, hors archive et hors `_generation/`, une page dont le nom commence par `sequence`, `atelier`, `tp_`,
`cahier`, `activite` ou `entrainement`.

IL REFUSE
---------
  M1  un document élève sans le bloc — sauf un panneau (voir plus bas) ou une page dispensée, raison écrite ;
  M2  une page qui porte deux blocs ;
  M3  une page dont le bloc n'est pas celui de la source (relancer `poser.py`, ou le générateur de la page) ;
  M4  une dispense périmée : la page dispensée porte le bloc, ou n'existe plus.

CE QUI N'EST PAS DEMANDÉ, ET POURQUOI
-------------------------------------
- **Un panneau** : une page de moins de 10 Ko sans aucun champ de réponse, qui renvoie vers l'atelier ou le TP réel
  (les `atelier_*.html` et `tp_*.html` rangés dans le dossier de chaque code servi). Rien à découper.
- **Les dispenses**, une par une, avec leur raison (`SANS_MISSION`).
- **Les QCM** ont leur propre moteur, une question à la fois. **Les synthèses et les lexiques** se lisent ; ils ne se
  jouent pas (un « mode lecture » leur est destiné). **Les vues d'objet** (`*_en_pieces.html`, `freins_iso.html`)
  tiennent en un écran.

Ce contrôle lit le source : il ne dit pas que le découpage est bon. `mode_mission/banc_generique.mjs` joue chaque page
qui porte le bloc, écran par écran, et refuse un écran vide, un défilement de côté, une réponse juste refusée.

Sortie : 0 rien à refuser · 1 au moins un refus · 2 aucun document lu (règle d'or n°299).
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
ELEVE = re.compile(r"^(sequence|atelier|tp_|cahier|activite|entrainement)", re.I)
CHAMP = re.compile(r"<(fieldset|textarea|select)\b|<input\b(?![^>]*type=[\"']?hidden)", re.I)
PANNEAU_MAX = 10000

#: Les pages dispensées : la fin de leur chemin → la raison, lue par qui se demande pourquoi.
SANS_MISSION = {
    "atelier-cao/tp_modele_demonstration.html":
        "modèle de démonstration du format des TP, marqué « Ne pas distribuer aux élèves »",
    "4e_C6.2/tp_algorigrammes_domotique.html":
        "a déjà son pas à pas : six phases, une seule à l'écran, ses propres boutons",
    "4e_C1.3/atelier_bete_a_cornes.html":
        "panneau vers l'atelier du besoin, avec le rappel d'un seul exercice",
    "3e_C3.1/atelier_bete_a_cornes.html":
        "panneau vers l'atelier du besoin, avec le rappel d'un seul exercice",
    "4e_C3.1/atelier_bete_a_cornes.html":
        "panneau vers l'atelier du besoin, avec le rappel d'un seul exercice",
}


def documents(racine):
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [s for s in sous if s not in EXCLUS and not s.startswith(".banc")]
        for f in fichiers:
            if f.lower().endswith(".html") and ELEVE.match(f):
                yield os.path.join(dossier, f)


def sorte(nom):
    return ELEVE.match(nom).group(1).lower().rstrip("_")


def est_panneau(html):
    return len(html.encode("utf-8")) < PANNEAU_MAX and not CHAMP.search(re.sub(r"<script\b.*?</script>", "", html, flags=re.S | re.I))


def dispense(chemin):
    c = chemin.replace(os.sep, "/")
    for fin, raison in SANS_MISSION.items():
        if c.endswith("/" + fin) or c == fin:
            return fin, raison
    return None, None


def main(argv):
    detail = "--detail" in argv
    args = [a for a in argv if not a.startswith("--")]
    racine = args[0] if args else "."
    lus = 0
    par_sorte = {}
    refus, panneaux, dispenses, vues = [], [], [], set()
    source = poser_mission.bloc()
    for chemin in sorted(documents(racine)):
        try:
            html = pathlib.Path(chemin).read_text(encoding="utf-8")
        except OSError:
            continue
        lus += 1
        blocs = poser_mission.blocs_de(html)
        fin, raison = dispense(chemin)
        if fin:
            vues.add(fin)
            if blocs:
                refus.append((chemin, "M4", "dispense périmée : la page porte le mode mission (retirer sa ligne de SANS_MISSION)"))
            else:
                dispenses.append((chemin, raison))
            continue
        if not blocs:
            if est_panneau(html):
                panneaux.append(chemin)
            else:
                refus.append((chemin, "M1", "document élève sans le mode mission (poser.py, ou le générateur de la page)"))
            continue
        s = sorte(os.path.basename(chemin))
        par_sorte[s] = par_sorte.get(s, 0) + 1
        if len(blocs) > 1:
            refus.append((chemin, "M2", "%d blocs du mode mission" % len(blocs)))
        elif blocs[0] != source:
            refus.append((chemin, "M3", "bloc différent de la source (relancer _outils/mode_mission/poser.py, ou le générateur)"))
    if lus == 0:
        print("⛔ EN PANNE — aucun document élève lu sous %s. Ce contrôle n'a RIEN vérifié (règle d'or n°299)." % racine)
        return 2
    if racine in (".", str(ICI.parent)) or os.path.abspath(racine) == str(ICI.parent):
        for fin in SANS_MISSION:
            if fin not in vues:
                refus.append((fin, "M4", "dispense périmée : la page n'existe plus (retirer sa ligne de SANS_MISSION)"))
    for chemin, code, quoi in refus:
        print("✘ %s  %s\n     %s" % (code, chemin, quoi))
    if detail:
        for chemin, raison in dispenses:
            print("· dispensée : %s — %s" % (chemin, raison))
    avec = sum(par_sorte.values())
    print("%d document(s) élève lu(s) · %d portent le mode mission (%s) · %d panneau(x) · %d dispense(s) · %d refus"
          % (lus, avec, ", ".join("%d %s" % (n, s) for s, n in sorted(par_sorte.items())), len(panneaux), len(dispenses), len(refus)))
    if refus:
        return 1
    print("✅ chaque document élève porte le mode mission, celui de la source, une fois")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
