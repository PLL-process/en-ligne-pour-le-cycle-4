# -*- coding: utf-8 -*-
"""Une seule source pour les animations pas à pas : le lecteur commun, à jour, dans chaque page qui anime.

    python3 _outils/controle_lecteur_pas_a_pas.py [racine]

Sortie 0 : chaque page qui porte une animation pas à pas (un bloc d'id « …-pas-a-pas ») utilise le lecteur
           commun (`data-lpp-racine` et l'appel `LecteurPasAPas(`), et porte son bloc une fois, identique à
           la source `_outils/lecteur_pas_a_pas/` ; aucune page n'appelle le lecteur sans le porter.
Sortie 1 : une page refusée, nommée, avec la raison.
Sortie 2 : aucune page lue (règle n°299 : un contrôle qui n'a rien vérifié est en panne).

Pourquoi : décision 4b de Pascal (25/10/2026). Trois animations avaient chacune leur copie du lecteur
(Herschel, vélo-cargo, trois principes), et chaque copie dérivait. Une correction faite à la source doit
arriver dans toutes les pages : `poser.py` la pose, ce contrôle refuse une page qui a gardé l'ancienne.

Ce qu'il NE vérifie PAS : que l'animation se joue bien (bancs des lots, au navigateur), ni la justesse des
phrases et des dessins. Les archives (`_archive-anciennes-versions/`) ne sont pas lues.
"""
import importlib.util
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("poser_lpp", ICI / "lecteur_pas_a_pas" / "poser.py")
poser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser)

ANIMATION = re.compile(r'id="[a-z0-9-]+-pas-a-pas"')


def defauts(html):
    d = []
    blocs = poser.blocs_de(html)
    anime = bool(ANIMATION.search(html))
    appelle = "LecteurPasAPas(" in html.replace("window.LecteurPasAPas", "").replace("function LecteurPasAPas(", "")
    if len(blocs) > 1:
        d.append("%d blocs du lecteur" % len(blocs))
    if blocs and blocs[0] != poser.bloc():
        d.append("bloc du lecteur différent de la source (relancer poser.py)")
    if appelle and not blocs:
        d.append("appelle LecteurPasAPas sans porter le lecteur")
    if anime and not appelle:
        d.append("animation pas à pas qui n'utilise pas le lecteur commun")
    return d, anime or bool(blocs)


def main(racine="."):
    pages = [p for p in sorted(pathlib.Path(racine).rglob("*.html"))
             if "_archive-anciennes-versions" not in p.parts and ".git" not in p.parts]
    if not pages:
        print("⛔ aucune page lue sous %s : rien n'a été vérifié" % racine)
        return 2
    refus, concernees = [], 0
    for p in pages:
        d, concernee = defauts(p.read_text(encoding="utf-8", errors="replace"))
        concernees += concernee
        if d:
            refus.append((p, d))
    print("%d page(s) lues · %d avec une animation pas à pas ou le lecteur" % (len(pages), concernees))
    for p, d in refus:
        print("  ✘ %s — %s" % (p, " ; ".join(d)))
    print("""
PÉRIMÈTRE : pages .html hors archives. Vérifié : le lecteur commun est utilisé par chaque animation
pas à pas, posé une fois, identique à la source. NON vu : le jeu de l'animation (bancs des lots).""")
    if refus:
        return 1
    print("✅ chaque animation pas à pas utilise le lecteur commun, à jour")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
