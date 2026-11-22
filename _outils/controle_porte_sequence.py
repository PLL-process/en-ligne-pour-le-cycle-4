# -*- coding: utf-8 -*-
"""controle_porte_sequence.py — la séquence est la porte de ses pages (règle d'or n°366).

LE CONSTAT
----------
Le TP « Algorigrammes de domotique » vivait dans le dossier `4e_C6.2`, à côté de la séquence du jardin connecté, et
aucune page de cette séquence ne le reliait : on n'y arrivait que par l'index du site (audit en 12 axes du
20/11/2026 ; lien posé par la PR #841). `controle_atteignabilite.py` le disait atteignable, et il l'était — depuis
l'accueil. Mais l'élève travaille dans sa séquence, pas dans l'index ; et le 08/11/2026 Pascal disait ne plus
retrouver le TP des variables (`3e_C9.1/vittascience_variables.html`) : il n'est relié par aucune page de sa séquence.
Mesuré le 21/11/2026 sur `main` (d7dc83c) : 14 pages. **Corrigé le 21/11/2026 au soir** : 11 étaient de faux positifs.
Dix sont des PAGES-POINTEURS (n°83) : une carte et un bouton vers l'atelier commun (`ateliers-representations/…`,
`atelier-planification/…`), atelier que la séquence relie déjà ou incruste ; une est un renvoi (« Ressource déplacée » :
le TP des variables de 3e_C9.1 a été refondu DANS sa séquence). Restent 3 pages vraiment sans porte.

LA RÈGLE
--------
Une page d'élève rangée dans le dossier d'une séquence (atelier, TP, activité) s'ouvre depuis cette séquence : un lien
(`href`) ou un cadre (`src`) dans une page `sequence*.html` du même dossier, à l'endroit où elle sert. L'index peut la
lister en plus ; il ne la remplace pas.

Une page-pointeur a sa porte quand la séquence relie la page que vise son bouton (`class="btn"`). Un renvoi (page
« déplacée » ou « refondue », ou `<meta http-equiv="refresh">`) n'en demande pas : il ne fait que renvoyer.

CE QU'IL LIT
------------
Chaque dossier des trois thèmes qui contient au moins une page `sequence*.html` ; dans ce dossier, chaque autre page
.html, sauf celles que la séquence relie déjà par construction ou qui ne sont pas pour l'élève : `qcm*`, `lexique*`,
`*synthese*`, `fiche*`, `rapport*`, `evaluation*`.

RÉFÉRENCE (règle n°273 : nommée, datée, ne peut que rétrécir)
-----------------------------------------------------------
Les 14 pages relevées le 21/11/2026 ; 3 après le tri du soir (11 faux positifs) ; **vide le 22/11/2026** : Pascal a
choisi de relier les trois dernières en activité facultative (« 1a », PR #862). Toute page sans porte fait maintenant
sortir à 1. Une page de la référence qui devient reliée est annoncée « à retirer ».

Sortie : 0 aucune page nouvelle sans porte · 1 au moins une · 2 EN PANNE (aucun dossier de séquence lu, n°299).
Usage : python3 _outils/controle_porte_sequence.py [--muet]
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "_exports", "_generation"}
HORS_PORTE = re.compile(r"^(qcm|lexique|fiche|rapport|evaluation)|synthese", re.I)

#: pages sans porte connues — vide depuis le 22/11/2026 (PR #862) ; ne peut que le rester (n°273).
#: 14 pages le 21/11/2026 (main d7dc83c), 3 après le tri du soir, puis reliées à leur séquence sur décision de Pascal.
REFERENCE = set()


RENVOI = re.compile(r"http-equiv\s*=\s*[\"']refresh|Ressource\s+d[ée]plac[ée]e|a\s+[ée]t[ée]\s+refondue", re.I)


def liens(chemin, texte=None):
    """Les chemins (normalisés) que la page relie par `href` ou `src`."""
    if texte is None:
        texte = open(chemin, encoding="utf-8", errors="replace").read()
    d = os.path.dirname(chemin)
    return {os.path.normpath(os.path.join(d, h)) for h in re.findall(r"""(?:href|src)\s*=\s*["']([^"'#?]+)""", texte)
            if not h.startswith(("http:", "https:", "mailto:", "data:", "javascript:", "//"))}


def boutons(chemin, texte):
    """Les pages que visent les boutons (`class="btn"`) d'une page-pointeur."""
    d = os.path.dirname(chemin)
    cibles = set()
    for balise in re.findall(r"<a\b[^>]*>", texte):
        if re.search(r"""class\s*=\s*["'][^"']*\bbtn\b""", balise):
            m = re.search(r"""href\s*=\s*["']([^"'#?]+)""", balise)
            if m:
                cibles.add(os.path.normpath(os.path.join(d, m.group(1))))
    return cibles


def mesurer(racine=RACINE):
    dossiers, sans_porte = 0, []
    for theme in sorted(d for d in os.listdir(racine) if d.startswith("theme-")):
        for dossier, sous, noms in os.walk(os.path.join(racine, theme)):
            sous[:] = sorted(d for d in sous if d not in IGNORES and not d.startswith((".", "_")))
            pages = sorted(n for n in noms if n.lower().endswith(".html"))
            sequences = [n for n in pages if n.lower().startswith("sequence")]
            if not sequences:
                continue
            dossiers += 1
            texte = "".join(open(os.path.join(dossier, s), encoding="utf-8", errors="replace").read() for s in sequences)
            relies = set().union(*(liens(os.path.join(dossier, s)) for s in sequences))
            for nom in pages:
                if nom in sequences or HORS_PORTE.search(nom):
                    continue
                if re.search(r"""(?:href|src)\s*=\s*["'](?:\./)?""" + re.escape(nom) + r"""(?:[#?"'])""", texte):
                    continue
                chemin = os.path.join(dossier, nom)
                page = open(chemin, encoding="utf-8", errors="replace").read()
                if RENVOI.search(page):
                    continue                                   # un renvoi ne demande pas de porte
                if boutons(chemin, page) & relies:
                    continue                                   # page-pointeur : la séquence relie déjà ce qu'elle vise
                sans_porte.append(os.path.relpath(chemin, racine).replace(os.sep, "/"))
    return dossiers, sans_porte


def main(argv):
    muet = "--muet" in argv
    dossiers, sans_porte = mesurer()
    if not dossiers:
        print("⛔ EN PANNE : aucun dossier de séquence lu (n°299).")
        return 2
    nouvelles = [p for p in sans_porte if p not in REFERENCE]
    if not muet:
        for p in nouvelles:
            print(f"✘ {p} — aucune page sequence*.html de son dossier ne la relie")
        for p in sorted(REFERENCE - set(sans_porte)):
            print(f"ℹ {p} — a maintenant sa porte : à retirer de REFERENCE (n°273)")
    print(f"{dossiers} dossier(s) de séquence lus · {len(sans_porte)} page(s) sans porte, dont {len(sans_porte) - len(nouvelles)} connue(s) au 21/11/2026 · {len(nouvelles)} nouvelle(s)")
    if nouvelles:
        print("✘ une page d'élève rangée dans le dossier d'une séquence s'ouvre depuis cette séquence — règle d'or n°366")
        return 1
    print("✅ aucune page nouvelle sans porte" + (f" (reste {len(sans_porte)} à relier, liste REFERENCE)" if sans_porte else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
