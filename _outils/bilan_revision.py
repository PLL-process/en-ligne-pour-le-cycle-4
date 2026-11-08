#!/usr/bin/env python3
"""bilan_revision.py — où en est chaque séquence de la révision des trois thèmes (08/11/2026).

Pascal, le 08/11/2026 : « une révision des 3 thèmes s'impose… depuis longtemps cela me paraissait une charge
cognitive ». Décision : une PASSE COMPLÈTE PAR SÉQUENCE (skill `revision-sequence`), dans l'ordre des classeurs de
progression, au lieu de vagues règle par règle.

Pour chaque page de séquence (les pages d'une séquence éclatée comptent sous leur page tout-en-un), l'outil mesure
ce qui, dans la page, alourdit la lecture de l'élève :
  mots       longueur de la page lue par l'élève (texte visible, scripts et styles retirés) ;
  regles     ✘ de `verif_regles_audit.py` sur la page (n°23, 29, 30, 31, 34, 300, 301, 304…) ;
  menus      questions posées par une liste déroulante (n°300 : à convertir en boutons) ;
  aeration   écarts de `audit_aeration.py` (légendes et corrections d'un seul tenant) ;
et lit dans `docs/revision/SUIVI_REVISION.md` l'état de la passe (à faire, en cours, livrée #PR, fusionnée).

Usage : python3 _outils/bilan_revision.py            le tableau, dans l'ordre de passage
        python3 _outils/bilan_revision.py --md       le même, en Markdown (pour le rapport du dimanche)
Une page est « propre » quand regles, menus et aeration sont à zéro.
"""
import glob
import html
import os
import re
import subprocess
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(DEPOT, "_outils"))
import audit_aeration  # noqa: E402

# l'ordre de passage : les classeurs de progression (période, puis ligne), les trois niveaux entrelacés, ce qui passe en
# classe le plus tôt d'abord ; puis les séquences hors classeur. Une séquence est désignée par le dossier de sa page.
ORDRE = [
    # P2 (novembre - décembre)
    "5e_C1.5", "5e_C1.3", "4e_C1.1", "4e_C1.4", "3e_C1.5", "3e_C2.1",
    # P2/P3
    "5e_C1.1", "5e_C1.2", "5e_C3.1", "4e_C2.1", "4e_C3.1", "3e_C4.1", "3e_C4.3",
    # P3, P3/P4
    "5e_C2.1", "4e_C4.1", "4e_C4.1_book-train", "3e_C4.7", "3e_C4.8", "3e_C5.1", "3e_C6.1", "3e_C6.2",
    # P4
    "5e_C4.1", "5e_C6.1", "4e_C5.1", "4e_C6.1", "4e_C6.2", "3e_C9.1", "3e_C7.1",
    # P4/P5, P5 : les projets et leurs séquences de compétence
    "5e_C5.1", "4e_C4.7", "5e_C4.7",
    "3e_C7.3", "3e_C7.4", "3e_C7.5", "3e_C7.7", "3e_C7.8", "3e_C8.1", "3e_C8.2", "3e_C9.2",
    "4e_C7.1", "4e_C7.3", "4e_C7.4", "4e_C7.5", "4e_C7.7", "4e_C7.8", "4e_C8.1", "4e_C9.1",
    "5e_C7.1", "5e_C7.3", "5e_C7.4", "5e_C7.5", "5e_C8.1", "5e_C8.2", "5e_C9.1",
    # hors classeur (lignes sans séance en 3e : sujets de remplacement, DNB)
    "3e_C1.1", "3e_C3.1",
]


def pages():
    out = {}
    for p in glob.glob(os.path.join(DEPOT, "theme-*/**/sequence*.html"), recursive=True):
        rel = os.path.relpath(p, DEPOT)
        if "_archive" in rel or re.search(r"station_[1-4]_", rel):
            continue
        out[os.path.basename(os.path.dirname(rel))] = rel
    return out


def regles_par_page():
    r = subprocess.run([sys.executable, os.path.join(DEPOT, "_outils/verif_regles_audit.py")], capture_output=True,
                       text=True, cwd=DEPOT)
    par, cour = {}, None
    for ligne in r.stdout.splitlines():
        m = re.search(r"(theme-\S+\.html)", ligne)
        if m and "✘" not in ligne:
            cour = m.group(1)
            par.setdefault(cour, [])
        elif cour and "✘" in ligne:
            n = re.search(r"n°(\d+)", ligne)
            menus = re.search(r"(\d+) question\(s\) posée\(s\) par une liste", ligne)
            par[cour].append((n.group(1) if n else "?", int(menus.group(1)) if menus else 0))
    return par


def mots(rel):
    s = open(os.path.join(DEPOT, rel), encoding="utf-8", errors="ignore").read()
    s = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", s, flags=re.S | re.I)
    return len(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())


def suivi():
    f = os.path.join(DEPOT, "docs/revision/SUIVI_REVISION.md")
    etat = {}
    if os.path.exists(f):
        for ligne in open(f, encoding="utf-8"):
            m = re.match(r"\|\s*\d+\s*\|\s*`?([345]e_C[\w.\-]+)`?\s*\|.*\|\s*([^|]+?)\s*\|\s*$", ligne)
            if m:
                etat[m.group(1)] = m.group(2)
    return etat


def main():
    md = "--md" in sys.argv
    pg, regles, etat = pages(), regles_par_page(), suivi()
    ordre = ORDRE + sorted(k for k in pg if k not in ORDRE)
    lignes, propres = [], 0
    for i, code in enumerate(ordre, 1):
        if code not in pg:
            continue
        rel = pg[code]
        r = regles.get(rel, [])
        n_menus = sum(m for _, m in r)
        n_regles = len(r)
        aer = len(audit_aeration.mesurer(os.path.join(DEPOT, rel)))
        ok = n_regles == 0 and aer == 0
        propres += ok
        lignes.append((i, code, mots(rel), n_regles, n_menus, aer, etat.get(code, "à faire"), ok))
    if md:
        print("| N° | Séquence | Mots | ✘ règles | Menus n°300 | Aération | État |")
        print("|---|---|---|---|---|---|---|")
        for i, code, w, nr, nm, a, e, ok in lignes:
            print("| %d | `%s` | %d | %d | %d | %d | %s |" % (i, code, w, nr, nm, a, e))
    else:
        for i, code, w, nr, nm, a, e, ok in lignes:
            print("%2d %-20s %6d mots · %2d ✘ règles · %3d menus · %3d aération · %s%s" % (i, code, w, nr, nm, a, e,
                                                                                         " ✅" if ok else ""))
    print("%d séquence(s) lues · %d propre(s) (0 ✘ de règle, 0 écart d'aération)" % (len(lignes), propres))
    return 0 if lignes else 2


if __name__ == "__main__":
    sys.exit(main())
