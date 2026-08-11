# -*- coding: utf-8 -*-
"""Règle d'or n°93 — un TP ne suppose acquis aucun GESTE d'outil.

Cet audit ne juge pas une notion : il cherche, dans toute page qui met un
LOGICIEL entre les mains de l'élève, les quatre gestes sans lesquels une
séance se perd — et qu'aucune progression ne garantit, puisque l'année
précédente n'a pas toujours eu lieu.

    ouvrir · nommer · retrouver · sortir

    python3 audit/audit_gestes.py <racine du dépôt>

CE QUE CET AUDIT SAIT FAIRE
  Repérer les pages qui nomment un logiciel, et y chercher la trace écrite
  de chaque geste. C'est une recherche de MOTS : elle voit qu'on en parle,
  pas qu'on l'explique bien.

CE QU'IL NE SAIT PAS FAIRE, et qu'il ne faut pas lui demander
  Dire si le geste est enseigné de façon auto-suffisante. « Comme en 5e »
  contient le mot et ne vaut rien pour qui n'était pas là — c'est
  précisément ce que la règle n°93 interdit, et seule une lecture humaine
  le voit. Un ✔ ici veut dire « le sujet est abordé », jamais « c'est bon ».
"""
import pathlib
import re
import sys

# Un logiciel = un endroit où l'élève produit un fichier qu'il devra retrouver.
LOGICIELS = {
    "Onshape":       r"Onshape",
    "GanttProject":  r"GanttProject|\.gan\b",
    "Vittascience":  r"Vittascience",
    "Filius":        r"Filius",
    "Packet Tracer": r"Packet\s*Tracer",
    "Scratch":       r"Scratch",
    "Arduino":       r"Arduino|mBlock",
    # « tableur » seul se dit aussi d'un tableau de cours : on exige le
    # signe qu'un ÉLÈVE en manipule un.
    "Tableur":       r"LibreOffice Calc|tableur.{0,40}(ouvr|saisis|classeur|feuille de calcul)",
}

GESTES = {
    "ouvrir":    r"cr[ée]er? (un |le )?(nouveau )?(document|projet|fichier)|nouveau document|ouvrir le logiciel",
    "nommer":    r"nomme|renomme|nom du (document|fichier|projet)|TON NOM|PRENOM",
    "retrouver": r"retrouver (ton|son) (travail|fichier|document)|rouvre|réouvr|la semaine (prochaine|suivante)|enregistr",
    "sortir":    r"export|enregistrer sous|\.stl|\.step|\.png|imprimer|rendre le fichier",
}

IGNORE = re.compile(r"(^|/)(_archive[^/]*|_modele|_generation)/|gabarit", re.I)


def analyser(page: pathlib.Path):
    html = page.read_text(encoding="utf-8", errors="replace")
    texte = re.sub(r"<[^>]+>", " ", html)
    trouves = [n for n, motif in LOGICIELS.items() if re.search(motif, texte, re.I)]
    if not trouves:
        return None
    manques = [g for g, motif in GESTES.items()
               if not re.search(motif, texte, re.I)]
    return trouves, manques


def main(racine):
    pages = [p for p in sorted(pathlib.Path(racine).rglob("*.html"))
             if not IGNORE.search(str(p))]
    concernees, incompletes = 0, []
    for p in pages:
        r = analyser(p)
        if not r:
            continue
        concernees += 1
        logiciels, manques = r
        if manques:
            incompletes.append((p, logiciels, manques))

    print("AUDIT DES GESTES D'OUTIL — règle d'or n°93")
    print("=" * 64)
    print("%d page(s) lue(s), %d mettent un logiciel entre les mains de "
          "l'élève." % (len(pages), concernees))
    print("%d d'entre elles ne parlent pas d'au moins un des quatre gestes.\n"
          % len(incompletes))

    par_manque = {}
    for p, log, manques in incompletes:
        for m in manques:
            par_manque.setdefault(m, []).append(p)
    for geste in GESTES:
        n = len(par_manque.get(geste, []))
        if n:
            print("  %-10s manquant dans %2d page(s)" % (geste, n))

    print("\nLE DÉTAIL, page par page :\n")
    for p, log, manques in incompletes:
        print("  %s" % p)
        print("      logiciel(s) : %s" % ", ".join(log))
        print("      absent      : %s" % ", ".join(manques))

    print("""
PÉRIMÈTRE DE CET AUDIT
  Vérifié mécaniquement : la présence, dans le texte de la page, de mots
  qui parlent d'ouvrir, de nommer, de retrouver et de sortir son travail.
  NON couvert, et c'est l'essentiel : savoir si le geste est expliqué de
  façon AUTO-SUFFISANTE. « Comme tu l'as vu en 5e » satisfait ce script et
  viole la règle n°93. Un ✔ signifie « le sujet est abordé », jamais
  « c'est bien fait ». La relecture se fait à la main, cette liste sert à
  savoir OÙ regarder.""")
    return 1 if incompletes else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
