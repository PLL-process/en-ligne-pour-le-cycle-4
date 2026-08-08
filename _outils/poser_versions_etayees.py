#!/usr/bin/env python3
"""Pose les blocs « version étayée » (règle d'or n°31) écrits à la main dans amorces.py.

Ce script ne DEVINE rien : il refuse toute zone dont l'amorce n'a pas été écrite.
Le texte vient d'amorces.py, pas d'une extraction automatique — c'est la leçon du
bandeau de tâches (08/08/2026) : mécaniser une règle de forme est facile, mécaniser
une règle de sens ne l'est pas.
"""
import html, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from amorces_versions_etayees import A

CSS = """
  /* Règle d'or n°31 — version étayée : même exigence, obstacle de rédaction en moins */
  details.etayage{margin:8px 0;border:1px solid #3f6bb5;border-left:4px solid #61dafb;
    border-radius:8px;background:rgba(13,35,71,.55);padding:6px 12px}
  details.etayage>summary{cursor:pointer;font-weight:600;color:#61dafb}
  details.etayage p{margin:6px 0}
  details.etayage ul{margin:6px 0;padding-left:22px}
  details.etayage li{margin:5px 0}
  @media print{details.etayage{break-inside:avoid}}
"""

INTRO = ("Le niveau attendu est <b>exactement le même</b> qu'avec la consigne libre&nbsp;: "
         "ces débuts de phrases retirent l'obstacle de la rédaction, pas l'exigence "
         "scientifique. Recopie-les et complète chaque «&nbsp;____&nbsp;».")


def bloc(amorces: list[str]) -> str:
    items = "\n".      join(f"    <li>{html.escape(a)}</li>" for a in amorces)
    return ('\n<details class="etayage">\n'
            '  <summary>🪜 Version étayée — des phrases à compléter</summary>\n'
            f'  <p>{INTRO}</p>\n  <ul>\n{items}\n  </ul>\n</details>')


def traiter(chemin: pathlib.Path, essai: bool) -> int:
    table = A.get(chemin.name)
    if not table:
        print(f"·  {chemin.name} — aucune amorce écrite pour ce fichier, ignoré")
        return 0
    src = chemin.read_text(encoding="utf-8")
    if "etayage" in src:
        print(f"·  {chemin.name} — déjà traité")
        return 0
    poses, sautees = 0, []
    # On parcourt à l'envers pour que les positions restent valides.
    for m in reversed(list(re.finditer(r"<textarea\b[^>]*>.*?</textarea>", src, re.S))):
        ident = re.search(r'\bid="([^"]+)"', m.group(0))
        if not ident:
            continue
        nom = ident.group(1)
        if nom not in table:
            sautees.append(nom)
            continue
        src = src[:m.end()] + bloc(table[nom]) + src[m.end():]
        poses += 1
    if poses and "details.etayage" not in src:
        i = src.rindex("</style>")
        src = src[:i] + CSS + src[i:]
    if poses != len(table):
        print(f"✘  {chemin.name} — {poses} posé(s) pour {len(table)} amorces écrites : "
              f"fichier NON réécrit")
        return 0
    if not essai:
        chemin.write_text(src, encoding="utf-8")
    note = f"  (zones sans amorce, laissées telles quelles : {', '.join(sautees)})" if sautees else ""
    print(f"{'≡' if essai else '✔'}  {chemin.name} — {poses} version(s) étayée(s){note}")
    return poses


def main(argv):
    essai = "--essai" in argv
    racine = pathlib.Path("theme-2-structure-fonctionnement-comportement")
    total = sum(traiter(f, essai) for f in sorted(racine.glob("**/sequence_*.html")))
    print(f"\n{total} version(s) étayée(s) posée(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
