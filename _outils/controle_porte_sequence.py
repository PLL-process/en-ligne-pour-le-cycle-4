# -*- coding: utf-8 -*-
"""controle_porte_sequence.py — la séquence est la porte de ses pages (règle d'or n°351).

LE CONSTAT
----------
Le TP « Algorigrammes de domotique » vivait dans le dossier `4e_C6.2`, à côté de la séquence du jardin connecté, et
aucune page de cette séquence ne le reliait : on n'y arrivait que par l'index du site (audit en 12 axes du
20/11/2026 ; lien posé par la PR #841). `controle_atteignabilite.py` le disait atteignable, et il l'était — depuis
l'accueil. Mais l'élève travaille dans sa séquence, pas dans l'index ; et le 08/11/2026 Pascal disait ne plus
retrouver le TP des variables (`3e_C9.1/vittascience_variables.html`) : il n'est relié par aucune page de sa séquence.
Mesuré le 21/11/2026 sur `main` (d7dc83c) : 14 ateliers, TP ou activités dans un dossier de séquence, qu'aucune page
`sequence*.html` du dossier ne relie.

LA RÈGLE
--------
Une page d'élève rangée dans le dossier d'une séquence (atelier, TP, activité) s'ouvre depuis cette séquence : un lien
(`href`) ou un cadre (`src`) dans une page `sequence*.html` du même dossier, à l'endroit où elle sert. L'index peut la
lister en plus ; il ne la remplace pas.

CE QU'IL LIT
------------
Chaque dossier des trois thèmes qui contient au moins une page `sequence*.html` ; dans ce dossier, chaque autre page
.html, sauf celles que la séquence relie déjà par construction ou qui ne sont pas pour l'élève : `qcm*`, `lexique*`,
`*synthese*`, `fiche*`, `rapport*`, `evaluation*`.

RÉFÉRENCE (règle n°273 : nommée, datée, ne peut que rétrécir)
-----------------------------------------------------------
Les 14 pages relevées le 21/11/2026. Une page de la référence qui devient reliée est annoncée « à retirer » ; une
page NOUVELLE sans porte fait sortir à 1.

Sortie : 0 aucune page nouvelle sans porte · 1 au moins une · 2 EN PANNE (aucun dossier de séquence lu, n°299).
Usage : python3 _outils/controle_porte_sequence.py [--muet]
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "_exports", "_generation"}
HORS_PORTE = re.compile(r"^(qcm|lexique|fiche|rapport|evaluation)|synthese", re.I)

#: pages sans porte relevées le 21/11/2026 (main d7dc83c) — ne peut que rétrécir (n°273).
REFERENCE = {
    "theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.2/activite_crcn_donnees_freinage_5e_C1.2.html",
    "theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.2/atelier_diagramme_fast.html",
    "theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/3e/3e_C2.1/atelier_diagramme_cas_utilisation.html",
    "theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/atelier_croquis.html",
    "theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/4e/4e_C2.1/atelier_diagramme_cas_utilisation.html",
    "theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/5e/5e_C2.1/atelier_diagramme_cas_utilisation.html",
    "theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/5e/5e_C2.1/atelier_diagramme_pieuvre.html",
    "theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/3e/3e_C3.1/atelier_bete_a_cornes.html",
    "theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/4e/4e_C3.1/atelier_bete_a_cornes.html",
    "theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/5e/5e_C4.1/atelier_diagramme_fast.html",
    "theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/atelier_C7.1_planification_taches.html",
    "theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/atelier_C7.1_planification_taches.html",
    "theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/atelier_C7.1_planification_taches.html",
    "theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/vittascience_variables.html",
}


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
            for nom in pages:
                if nom in sequences or HORS_PORTE.search(nom):
                    continue
                if not re.search(r"""(?:href|src)\s*=\s*["'](?:\./)?""" + re.escape(nom) + r"""(?:[#?"'])""", texte):
                    sans_porte.append(os.path.relpath(os.path.join(dossier, nom), racine).replace(os.sep, "/"))
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
        print("✘ une page d'élève rangée dans le dossier d'une séquence s'ouvre depuis cette séquence — règle d'or n°351")
        return 1
    print("✅ aucune page nouvelle sans porte" + (f" (reste {len(sans_porte)} à relier, liste REFERENCE)" if sans_porte else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
