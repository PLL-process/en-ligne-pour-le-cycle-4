# -*- coding: utf-8 -*-
"""Assemble le QCM de l'atelier C7.1 à partir du gabarit maison et de `q.py`.

Une seule source de vérité pour les questions (`q.py`), un seul générateur
(ce fichier) — règle d'or n°38. Le moteur du QCM (barème, minuteur, modes,
sauvegarde) n'est pas recopié à la main : il est repris tel quel du gabarit,
seuls le bloc `const QUESTIONS` et les libellés propres au lot sont remplacés.

Règle d'or n°51 — ce que l'élève voit en premier se vérifie en premier : le
gabarit vient d'un lot de Thème 1 ; son `<h1>`, son sous-titre et ses badges
AFFICHÉS parlent de Shenzhen. Ce générateur les remplace, puis REFUSE d'écrire
s'il en reste la moindre trace.

Ici les « compétences » du filtre ne sont pas trois codes différents mais les
trois NIVEAUX du même code C7.1 : la notion est unique, c'est le verbe qui
change (règle d'or n°65).

Usage :
    python3 build_qcm.py <gabarit.html> <sortie.html>
puis  node _outils/fix_r.js <sortie.html> 617
"""

import json
import re
import sys

import q as banque

GRAINE = 617
ORDRE = ("expl", "ex", "err")

JALONS = {
    0: "/* ═══ 5e — SUIVRE un processus avec des tâches identifiées ═══ */",
    10: "/* ═══ 4e — ORGANISER un processus avec des tâches identifiées ═══ */",
    20: "/* ═══ 3e — ÉLABORER un processus avec des tâches identifiées ═══ */",
}


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

    lignes = ["const QUESTIONS = ["]
    for i, o in enumerate(banque.Q):
        if i in JALONS:
            lignes.append(JALONS[i])
        lignes.append(bloc_question(o) + ("," if i < len(banque.Q) - 1 else ""))
    lignes.append("];")

    ancien = re.search(r"const QUESTIONS = \[.*?\n\];", s, re.S)
    if not ancien:
        raise SystemExit("Bloc QUESTIONS introuvable dans le gabarit.")
    s = s[:ancien.start()] + "\n".join(lignes) + s[ancien.end():]

    nb_img = sum(1 for x in banque.Q if "img" in x)
    remplacements = [
        ("/* Banque de questions — Shenzhen 3e : 30 questions "
         "(C3.1 : 8 · C3.3 : 8 · C3.4 : 7 · C3.2 : 7) */",
         "/* Banque de questions — Atelier de planification des tâches, C7.1 : 30 questions "
         "(5e : 10 · 4e : 10 · 3e : 10), dont %d illustrées par de vraies captures de "
         "GanttProject en français. Toutes les valeurs numériques viennent du corrigé calculé "
         "par _verifier_planning.py. */" % nb_img),

        ('const KEY="qcm_3e_C3.1-C3.4_shenzhen";', 'const KEY="qcm_C7.1_planification_taches";'),

        ("""const COMP_LABELS={
  "C3.1":"3e_C3.1 — Établir une liste d'objets ou systèmes techniques possibles",
  "C3.3":"3e_C3.3 — Évaluer les solutions selon des exigences ou critères identifiés",
  "C3.4":"3e_C3.4 — Définir et mettre en œuvre un protocole de mesure",
  "C3.2":"3e_C3.2 — Choisir et argumenter en tenant compte du cycle de vie et des trois piliers" };""",
         # Règle d'or n°42 : formulations recopiées du référentiel, pas résumées.
         """const COMP_LABELS={
  "5e":"5e_C7.1 — Suivre un processus de réalisation d\\u2019un objet avec des tâches identifiées.",
  "4e":"4e_C7.1 — Organiser un processus de réalisation d\\u2019un objet avec des tâches identifiées.",
  "3e":"3e_C7.1 — Élaborer un processus de réalisation d\\u2019un objet avec des tâches identifiées." };"""),

        ("<title>Thème 1 · 3e — QCM : Shenzhen, comment refroidir un local qui surchauffe ? "
         "(3e_C3.1 à C3.4)</title>",
         "<title>Thème 3 · 5e-4e-3e — QCM : le diagramme de planification des tâches (C7.1)</title>"),

        ("<h1>Thème 1 · 3e — QCM : Shenzhen, comment refroidir un local qui surchauffe ?</h1>",
         "<h1>Thème 3 — QCM : le diagramme de planification des tâches</h1>"),

        ('<p class="subtitle">Caractériser et choisir une solution (3e_C3.1 à C3.4) — protocole '
         "de mesure, évaluation des solutions et cycle de vie</p>",
         '<p class="subtitle">Tâches, durée, contraintes entre tâches — et la seule chaîne qui '
         "décide de la date de fin. Suivre en 5e, organiser en 4e, élaborer en 3e (C7.1)</p>"),

        ('<span class="badge niveau">3e</span>',
         '<span class="badge niveau">5e · 4e · 3e</span>'),
        ('<span class="badge code">3e_C3.1</span><span class="badge code">3e_C3.2</span>'
         '<span class="badge code">3e_C3.3</span><span class="badge code">3e_C3.4</span>',
         '<span class="badge code">C7.1</span>'),

        ("30 questions · 1 illustrée · chaque distracteur réfuté",
         "30 questions · %d illustrées · chaque distracteur réfuté" % nb_img),

        ("""      <option value="C3.1">3e_C3.1 — Établir une liste de solutions possibles</option>
      <option value="C3.3">3e_C3.3 — Évaluer selon des exigences identifiées</option>
      <option value="C3.4">3e_C3.4 — Définir et mettre en œuvre un protocole</option>
      <option value="C3.2">3e_C3.2 — Choisir et argumenter sur les trois piliers</option>""",
         """      <option value="5e">5e — Suivre un processus avec des tâches identifiées</option>
      <option value="4e">4e — Organiser un processus avec des tâches identifiées</option>
      <option value="3e">3e — Élaborer un processus avec des tâches identifiées</option>"""),

        ("QCM d’entraînement 3e_C3.1 à C3.4 · Thème 1",
         "QCM d’entraînement C7.1 · Thème 3"),
    ]
    for avant, apres in remplacements:
        if s.count(avant) != 1:
            raise SystemExit("Motif absent ou ambigu dans le gabarit :\n%r" % avant[:90])
        s = s.replace(avant, apres)

    s = s.replace("sequence_3e_C3.1-C3.4_shenzhen.html",
                  "atelier_C7.1_planification_taches.html")
    s = s.replace("../../../../index.html", "../../../index.html")
    s = s.replace("⬅ Revenir à la séquence", "⬅ Revenir à l'atelier")
    s = s.replace("← Séquence", "← Atelier")
    s = s.replace("séquence associée", "atelier associé")

    # ── Contrôles avant écriture ────────────────────────────────────────────
    for reste in ("Shenzhen", "SOS serre", "Packet Tracer", "surchauffe ?", "Martinique — 4e"):
        if reste in s:
            raise SystemExit("Reste du gabarit d'origine non remplacé : %r" % reste)
    restes = re.findall(r"\b[345]e_C3\.\d\b|\"C3\.\d\"", s)
    if restes:
        raise SystemExit("Restes du gabarit 3e non remplacés : %s" % sorted(set(restes)))
    for niv in ("5e", "4e", "3e"):
        if s.count('"%s"' % niv) < 2:
            raise SystemExit("Le niveau %s n'apparaît pas assez : filtre ou questions manquants." % niv)

    # Écriture seulement une fois tout le travail fait.
    open(sortie, "w", encoding="utf-8").write(s)
    print("QCM écrit : %s (%d questions, %d illustrées)" % (sortie, len(banque.Q), nb_img))
    print("Étape suivante : node _outils/fix_r.js %s %d" % (sortie, GRAINE))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    construire(sys.argv[1], sys.argv[2])
