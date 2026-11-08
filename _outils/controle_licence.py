# -*- coding: utf-8 -*-
"""controle_licence.py — chaque page porte la licence du dépôt (règle d'or n°321).

CE QU'IL MESURE
---------------
  · `LICENSE.md` existe à la racine et nomme CC BY-NC-SA 4.0 ;
  · chaque page `.html` publiée (hors `_archive-anciennes-versions`, `.git`, `node_modules`,
    bancs d'essai `.banc-*`) porte la mention de `licence_cc.py`, reconnue par son attribut
    `data-licence="cc-by-nc-sa"` ;
  · un `README.md` racine, s'il existe, porte la mention Markdown.

POURQUOI UN CONTRÔLE ET PAS SEULEMENT UNE INJECTION
---------------------------------------------------
Huit générateurs écrivent des pages complètes (`make_index.py`, `generer_lexique.py`,
`qcm_generator.py`, les `_generation/` des ateliers). Une page régénérée sans la mention
reviendrait nue : ce contrôle le voit, et `--corriger` répare sur place.

Usage : python3 _outils/controle_licence.py [--racine .] [--corriger]
Sortie 0 si tout porte la mention, 1 sinon (avec la liste). Avec `--corriger`, pose la mention
où elle manque, puis mesure à nouveau : sortie 0 si plus rien ne manque.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from licence_cc import porte_mention, injecter, MENTION_MD  # noqa: E402

EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports"}


def pages_html(racine):
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [s for s in sous if s not in EXCLUS and not s.startswith(".banc")]
        for f in fichiers:
            if f.lower().endswith(".html"):
                yield os.path.join(dossier, f)


def mesurer(racine):
    manques = []
    licence = os.path.join(racine, "LICENSE.md")
    if not os.path.isfile(licence):
        manques.append(("LICENSE.md", "absent à la racine"))
    elif "BY-NC-SA 4.0" not in open(licence, encoding="utf-8").read():
        manques.append(("LICENSE.md", "ne nomme pas CC BY-NC-SA 4.0"))
    readme = os.path.join(racine, "README.md")
    if os.path.isfile(readme) and "CC BY-NC-SA 4.0" not in open(readme, encoding="utf-8").read():
        manques.append(("README.md", "sans mention de licence"))
    for p in sorted(pages_html(racine)):
        try:
            t = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            t = open(p, encoding="utf-8", errors="replace").read()
        if not porte_mention(t):
            manques.append((os.path.relpath(p, racine), "page sans mention de licence"))
    return manques


def corriger(racine, manques):
    posees = 0
    for rel, raison in manques:
        if raison != "page sans mention de licence":
            continue
        p = os.path.join(racine, rel)
        t = open(p, encoding="utf-8").read()
        open(p, "w", encoding="utf-8").write(injecter(t))
        posees += 1
    return posees


def main(argv):
    racine = "."
    corrige = False
    i = 0
    while i < len(argv):
        if argv[i] == "--racine":
            racine = argv[i + 1]; i += 2
        elif argv[i] == "--corriger":
            corrige = True; i += 1
        else:
            print("argument inconnu :", argv[i]); return 2
    racine = os.path.abspath(racine)
    manques = mesurer(racine)
    if corrige and manques:
        n = corriger(racine, manques)
        print(f"{n} mention(s) posée(s)")
        manques = mesurer(racine)
    total = sum(1 for _ in pages_html(racine))
    if manques:
        print(f"✘ {len(manques)} manque(s) sur {total} pages :")
        for rel, raison in manques:
            print(f"  - {rel} — {raison}")
        if any(r.startswith("README") for r, _ in manques):
            print("  (README.md est engendré : la mention se pose dans make_index.py —", MENTION_MD[:40], "…)")
        return 1
    print(f"✓ licence : {total} pages portent la mention, LICENSE.md présent")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
