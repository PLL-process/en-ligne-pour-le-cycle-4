# -*- coding: utf-8 -*-
"""Les chaînes à compléter : l'outil commun, à jour, dans chaque page qui pose des étiquettes dans un schéma de chaîne.

    python3 _outils/controle_chaine_a_completer.py [racine]

Sortie 0 : chaque page qui porte une étape `div.cac[data-cac]` porte le bloc de `_outils/chaine_a_completer/` une
           fois, identique à la source ; chaque étape nomme un dessin déclaré dans la page (`CAC_DESSINS.<nom>`) et
           des groupes de boutons radio qui existent, à l'intérieur de l'étape ; aucune page ne porte le bloc sans
           s'en servir.
Sortie 1 : une page refusée, nommée, avec la raison.
Sortie 2 : aucune page lue (règle n°299 : un contrôle qui n'a rien vérifié est en panne).

Pourquoi : demande de Pascal du 15/11/2026. L'élève répondait à beaucoup de questions sur les chaînes d'énergie et
d'information sans avoir le schéma sous les yeux. Les étiquettes se posent maintenant DANS le schéma, qui se bâtit
d'une activité à l'autre. Une correction faite à la source doit arriver dans toutes les pages : `poser.py` la pose,
ce contrôle refuse une page qui a gardé l'ancienne.

Ce qu'il NE vérifie PAS : le jeu au navigateur (bancs des lots, `mode_mission/banc_generique.mjs`), la justesse des
mots et des dessins. Les archives (`_archive-anciennes-versions/`) ne sont pas lues.
"""
import html as H
import importlib.util
import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("poser_cac", ICI / "chaine_a_completer" / "poser.py")
poser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser)

ETAPE = re.compile(r"<div class=\"cac\" data-cac='([^']*)'>(.*?)\n</div>\n</div>", re.S)


def defauts(page):
    d = []
    blocs = poser.blocs_de(page)
    etapes = ETAPE.findall(poser._BLOC_RE.sub("", page))          # le mode d'emploi, dans le bloc, en cite une
    if len(blocs) > 1:
        d.append("%d blocs de l'outil" % len(blocs))
    if blocs and blocs[0] != poser.bloc():
        d.append("bloc de l'outil différent de la source (relancer poser.py)")
    if etapes and not blocs:
        d.append("des étapes de chaîne à compléter sans l'outil")
    if blocs and not etapes:
        d.append("l'outil posé sans aucune étape qui s'en sert")
    for i, (conf, corps) in enumerate(etapes, 1):
        try:
            c = json.loads(H.unescape(conf))
        except ValueError as e:
            d.append("étape %d : data-cac illisible (%s)" % (i, e)); continue
        if not re.search(r"CAC_DESSINS\.%s\s*=" % re.escape(c.get("dessin", "?")), page):
            d.append("étape %d : dessin « %s » non déclaré dans la page" % (i, c.get("dessin")))
        for cle, fid in (c.get("cases") or {}).items():
            if 'id="%s"' % fid not in corps:
                d.append("étape %d : la case %s attend le groupe %s, absent de l'étape" % (i, cle, fid))
        for cle, fid in (c.get("acquis") or {}).items():
            if 'id="%s"' % fid not in page:
                d.append("étape %d : l'acquis %s lit le groupe %s, absent de la page" % (i, cle, fid))
    return d, bool(blocs or etapes)


def main(racine="."):
    pages = [p for p in sorted(pathlib.Path(racine).rglob("*.html"))
             if "_archive-anciennes-versions" not in p.parts and ".git" not in p.parts and "node_modules" not in p.parts]
    if not pages:
        print("⛔ aucune page lue sous %s : rien n'a été vérifié" % racine)
        return 2
    refus, concernees = [], 0
    for p in pages:
        d, concernee = defauts(p.read_text(encoding="utf-8", errors="replace"))
        concernees += concernee
        if d:
            refus.append((p, d))
    print("%d page(s) lues · %d avec une chaîne à compléter" % (len(pages), concernees))
    for p, d in refus:
        print("  ✘ %s — %s" % (p, " ; ".join(d)))
    print("""
PÉRIMÈTRE : pages .html hors archives. Vérifié : l'outil commun posé une fois, identique à la source, dans chaque page
qui pose des étiquettes dans un schéma de chaîne ; chaque étape nomme un dessin déclaré et des groupes qui existent.
NON vu : le jeu au navigateur (bancs des lots, banc générique du mode mission).""")
    if refus:
        return 1
    print("✅ chaque chaîne à compléter utilise l'outil commun, à jour, et ses étapes sont complètes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
