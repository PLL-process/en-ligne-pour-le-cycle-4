# -*- coding: utf-8 -*-
"""Assemble le QCM 5e_C2.1 · C2.2 à partir du gabarit maison et de `q.py`.

Une seule source de vérité pour les questions (`q.py`), un seul générateur
(ce fichier) — règle d'or n°38. Le moteur du QCM (barème, minuteur, modes,
sauvegarde) n'est pas recopié à la main : il est repris tel quel du gabarit,
seul le bloc `const QUESTIONS` et les libellés propres au lot sont remplacés.

Usage :
    python3 build_qcm.py <gabarit.html> <sortie.html>
puis  node _outils/fix_r.js <sortie.html> 502
pour répartir les bonnes réponses sur A/B/C/D (elles sont toutes en r:0 ici).
"""

import json
import re
import sys

import q as banque

GRAINE = 502  # rappel : la graine passée à fix_r.js pour ce lot

ORDRE = ("expl", "ex", "err")


def bloc_question(o: dict) -> str:
    p = ["c:" + json.dumps(o["c"], ensure_ascii=False),
         "n:" + json.dumps(o["n"], ensure_ascii=False),
         "q:" + json.dumps(o["q"], ensure_ascii=False)]
    if "img" in o:
        p.append("img:{src:%s,alt:%s}" % (json.dumps(o["img"]["src"], ensure_ascii=False),
                                          json.dumps(o["img"]["alt"], ensure_ascii=False)))
    p.append("o:[%s]" % ",".join(json.dumps(x, ensure_ascii=False) for x in o["o"]))
    p.append("r:0")
    for k in ORDRE:
        p.append("%s:%s" % (k, json.dumps(o[k], ensure_ascii=False)))
    p.append("d:[%s]" % ",".join(json.dumps(x, ensure_ascii=False) for x in o["d"]))
    p.append("ret:" + json.dumps(o["ret"], ensure_ascii=False))
    return "{" + ",\n ".join(p) + "}"


def construire(gabarit: str, sortie: str) -> None:
    s = open(gabarit, encoding="utf-8").read()

    lignes = ["const QUESTIONS = [",
              "/* ═══ 5e_C2.1 — recenser les interacteurs extérieurs ═══ */"]
    for i, o in enumerate(banque.Q):
        if i == 15:
            lignes.append("/* ═══ 5e_C2.2 — repérer et expliquer les choix de conception ═══ */")
        lignes.append(bloc_question(o) + ("," if i < len(banque.Q) - 1 else ""))
    lignes.append("];")

    ancien = re.search(r"const QUESTIONS = \[.*?\n\];", s, re.S)
    if not ancien:
        raise SystemExit("Bloc QUESTIONS introuvable dans le gabarit.")
    s = s[:ancien.start()] + "\n".join(lignes) + s[ancien.end():]

    remplacements = [
        ("/* Banque de questions — Shenzhen 3e : 30 questions "
         "(C3.1 : 8 · C3.3 : 8 · C3.4 : 7 · C3.2 : 7) */",
         "/* Banque de questions — Shenzhen 5e : 30 questions "
         "(5e_C2.1 : 15 · 5e_C2.2 : 15), dont 4 illustrées */"),
        ('const KEY="qcm_3e_C3.1-C3.4_shenzhen";', 'const KEY="qcm_5e_C2_shenzhen";'),
        ("""const COMP_LABELS={
  "C3.1":"3e_C3.1 — Établir une liste d'objets ou systèmes techniques possibles",
  "C3.3":"3e_C3.3 — Évaluer les solutions selon des exigences ou critères identifiés",
  "C3.4":"3e_C3.4 — Définir et mettre en œuvre un protocole de mesure",
  "C3.2":"3e_C3.2 — Choisir et argumenter en tenant compte du cycle de vie et des trois piliers" };""",
         """const COMP_LABELS={
  "C2.1":"5e_C2.1 — Faire la liste des interacteurs extérieurs d'un objet ou système technique",
  "C2.2":"5e_C2.2 — Repérer et expliquer les choix de conception (ergonomie, sécurité, esthétique)" };"""),
        ("<title>Thème 1 · 3e — QCM : Shenzhen, comment refroidir un local qui surchauffe ? "
         "(3e_C3.1 à C3.4)</title>",
         "<title>Thème 1 · 5e — QCM : Shenzhen, la station de vélos et tout ce qui l'entoure "
         "(5e_C2.1 · C2.2)</title>"),
        ('<span class="badge niveau">3e</span>', '<span class="badge niveau">5e</span>'),
        ('<span class="badge code">3e_C3.1</span><span class="badge code">3e_C3.2</span>'
         '<span class="badge code">3e_C3.3</span><span class="badge code">3e_C3.4</span>',
         '<span class="badge code">5e_C2.1</span><span class="badge code">5e_C2.2</span>'),
        ("30 questions · 1 illustrée · chaque distracteur réfuté",
         "30 questions · 4 illustrées · chaque distracteur réfuté"),
        ("""      <option value="C3.1">3e_C3.1 — Établir une liste de solutions possibles</option>
      <option value="C3.3">3e_C3.3 — Évaluer selon des exigences identifiées</option>
      <option value="C3.4">3e_C3.4 — Définir et mettre en œuvre un protocole</option>
      <option value="C3.2">3e_C3.2 — Choisir et argumenter sur les trois piliers</option>""",
         """      <option value="C2.1">5e_C2.1 — Faire la liste des interacteurs extérieurs</option>
      <option value="C2.2">5e_C2.2 — Repérer et expliquer les choix de conception</option>"""),
        ("QCM d’entraînement 3e_C3.1 à C3.4 · Thème 1",
         "QCM d’entraînement 5e_C2.1 · C2.2 · Thème 1"),
    ]
    for avant, apres in remplacements:
        if s.count(avant) != 1:
            raise SystemExit("Motif absent ou ambigu dans le gabarit :\n%r" % avant[:70])
        s = s.replace(avant, apres)

    s = s.replace("sequence_3e_C3.1-C3.4_shenzhen.html",
                  "sequence_5e_C2_shenzhen_station_velos.html")

    reste = re.findall(r"\b3e_C3\.\d\b|\bC3\.\d\b", s)
    if reste:
        raise SystemExit("Restes du gabarit 3e non remplacés : %s" % sorted(set(reste)))

    # Écriture seulement une fois tout le travail fait : ouvrir en 'w' tronque
    # immédiatement, et une erreur survenue après ce point détruirait le fichier.
    open(sortie, "w", encoding="utf-8").write(s)
    print("QCM écrit : %s (%d questions, %d illustrées)"
          % (sortie, len(banque.Q), sum(1 for x in banque.Q if "img" in x)))
    print("Étape suivante : node _outils/fix_r.js %s %d" % (sortie, GRAINE))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    construire(sys.argv[1], sys.argv[2])
