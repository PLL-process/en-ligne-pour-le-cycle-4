# -*- coding: utf-8 -*-
"""Assemble le QCM 4e_C2.1 · C2.2 à partir du gabarit maison et de `q.py`.

Une seule source de vérité pour les questions (`q.py`), un seul générateur
(ce fichier) — règle d'or n°38. Le moteur du QCM (barème, minuteur, modes,
sauvegarde) n'est pas recopié à la main : il est repris tel quel du gabarit,
seuls le bloc `const QUESTIONS` et les libellés propres au lot sont remplacés.

Ce générateur ajoute en outre le câblage de la **règle d'or n°45** : le QCM
lit `#codes=C2.1` dans l'adresse et s'ouvre alors sur la révision ciblée de
ces seules compétences. La séquence pose ce fragment quand l'élève n'a validé
qu'une partie des activités.

Usage :
    python3 build_qcm.py <gabarit.html> <sortie.html>
puis  node _outils/fix_r.js <sortie.html> 421
"""

import json
import re
import sys

import q as banque

GRAINE = 421

ORDRE = ("expl", "ex", "err")

# Règle d'or n°45 — l'entraînement s'ouvre sur ce qui a été fait.
# Le fragment est ajouté à la fin du moteur : il ne touche à rien, il ne fait
# que préselectionner un mode déjà existant du gabarit.
OUVERTURE_CIBLEE = """
/* ══════ Règle d'or n°45 — ouvrir sur ce que l'élève a déjà travaillé ══════ */
/* La séquence appelle ce QCM avec #codes=C2.1 quand une seule compétence a été
   travaillée. On bascule alors en révision ciblée sur ces codes-là. L'élève
   garde l'accès au parcours complet : on choisit ce qu'on lui propose EN
   PREMIER, on ne lui interdit rien. */
(function ouvrirSurLesCodesDemandes(){
  const m = (location.hash||"").match(/codes=([A-Za-z0-9.,]+)/);
  if(!m) return;
  const voulus = m[1].split(",").filter(c => QUESTIONS.some(q => q.c === c));
  if(!voulus.length || voulus.length === new Set(QUESTIONS.map(q=>q.c)).size) return;
  const sel = document.getElementById("selComp");
  if(sel){ sel.value = voulus[0]; }
  setMode("cible");
  const hote = document.getElementById("porteeCiblee");
  if(hote){
    hote.hidden = false;
    hote.innerHTML = "🎯 Tu arrives depuis la séquence : ce QCM s'ouvre sur <b>" +
      voulus.join(" et ") + "</b>, c'est-à-dire sur ce que tu as déjà travaillé. " +
      "Pour t'entraîner sur les 30 questions, choisis <b>« Parcours complet »</b> ci-dessus.";
  }
})();
"""


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
              "/* ═══ 4e_C2.1 — décrire l'expérience de l'utilisateur ═══ */"]
    for i, o in enumerate(banque.Q):
        if i == 15:
            lignes.append("/* ═══ 4e_C2.2 — repérer et expliquer les contraintes et exigences ═══ */")
        lignes.append(bloc_question(o) + ("," if i < len(banque.Q) - 1 else ""))
    lignes.append("];")

    ancien = re.search(r"const QUESTIONS = \[.*?\n\];", s, re.S)
    if not ancien:
        raise SystemExit("Bloc QUESTIONS introuvable dans le gabarit.")
    s = s[:ancien.start()] + "\n".join(lignes) + s[ancien.end():]

    remplacements = [
        ("/* Banque de questions — Shenzhen 3e : 30 questions "
         "(C3.1 : 8 · C3.3 : 8 · C3.4 : 7 · C3.2 : 7) */",
         "/* Banque de questions — Hangzhou 4e : 30 questions "
         "(4e_C2.1 : 15 · 4e_C2.2 : 15), dont 5 illustrées */"),
        ('const KEY="qcm_3e_C3.1-C3.4_shenzhen";', 'const KEY="qcm_4e_C2_hangzhou";'),
        ("""const COMP_LABELS={
  "C3.1":"3e_C3.1 — Établir une liste d'objets ou systèmes techniques possibles",
  "C3.3":"3e_C3.3 — Évaluer les solutions selon des exigences ou critères identifiés",
  "C3.4":"3e_C3.4 — Définir et mettre en œuvre un protocole de mesure",
  "C3.2":"3e_C3.2 — Choisir et argumenter en tenant compte du cycle de vie et des trois piliers" };""",
         """const COMP_LABELS={
  "C2.1":"4e_C2.1 — Décrire l'expérience de l'utilisateur, du langage naturel aux schémas, graphiques et algorithmes",
  "C2.2":"4e_C2.2 — Repérer et expliquer les contraintes et exigences prises en compte" };"""),
        ("<title>Thème 1 · 3e — QCM : Shenzhen, comment refroidir un local qui surchauffe ? "
         "(3e_C3.1 à C3.4)</title>",
         "<title>Thème 1 · 4e — QCM : Hangzhou, ce que vit l'usager devant la borne "
         "(4e_C2.1 · C2.2)</title>"),
        ('<span class="badge niveau">3e</span>', '<span class="badge niveau">4e</span>'),
        ('<span class="badge code">3e_C3.1</span><span class="badge code">3e_C3.2</span>'
         '<span class="badge code">3e_C3.3</span><span class="badge code">3e_C3.4</span>',
         '<span class="badge code">4e_C2.1</span><span class="badge code">4e_C2.2</span>'),
        ("30 questions · 1 illustrée · chaque distracteur réfuté",
         "30 questions · 5 illustrées · chaque distracteur réfuté"),
        ("""      <option value="C3.1">3e_C3.1 — Établir une liste de solutions possibles</option>
      <option value="C3.3">3e_C3.3 — Évaluer selon des exigences identifiées</option>
      <option value="C3.4">3e_C3.4 — Définir et mettre en œuvre un protocole</option>
      <option value="C3.2">3e_C3.2 — Choisir et argumenter sur les trois piliers</option>""",
         """      <option value="C2.1">4e_C2.1 — Décrire l'expérience de l'utilisateur</option>
      <option value="C2.2">4e_C2.2 — Repérer et expliquer les exigences</option>"""),
        ("QCM d’entraînement 3e_C3.1 à C3.4 · Thème 1",
         "QCM d’entraînement 4e_C2.1 · C2.2 · Thème 1"),
    ]
    for avant, apres in remplacements:
        if s.count(avant) != 1:
            raise SystemExit("Motif absent ou ambigu dans le gabarit :\n%r" % avant[:70])
        s = s.replace(avant, apres)

    s = s.replace("sequence_3e_C3.1-C3.4_shenzhen.html", "sequence_4e_C2_hangzhou_borne.html")

    # zone d'accueil de la règle n°45, juste après les modes
    ancre = '<p style="text-align:center"><a href="sequence_4e_C2_hangzhou_borne.html">'
    if s.count(ancre) != 1:
        raise SystemExit("Ancre du bandeau de portée introuvable.")
    s = s.replace(ancre,
                  '<p class="portee-ciblee" id="porteeCiblee" hidden role="status"></p>\n' + ancre)

    # le fragment de la règle n°45, à la toute fin du moteur
    if s.count("\n</script>") < 1:
        raise SystemExit("Fin de script introuvable.")
    i = s.rfind("\n</script>")
    s = s[:i] + "\n" + OUVERTURE_CIBLEE + s[i:]

    # un peu de style pour le bandeau
    s = s.replace("  .q-comp{",
                  "  .portee-ciblee{max-width:880px;margin:0 auto 12px;padding:9px 14px;"
                  "border:1px solid var(--head);border-radius:10px;background:#2b1a3f;"
                  "font-size:.85em;color:var(--text)}\n  .q-comp{")

    reste = re.findall(r"\b3e_C3\.\d\b|\bC3\.\d\b", s)
    if reste:
        raise SystemExit("Restes du gabarit 3e non remplacés : %s" % sorted(set(reste)))


    # Le gabarit vient d'un lot de Thème 2 : son <h1> et son sous-titre AFFICHÉS
    # parlaient de « SOS serre » et de Packet Tracer. Six QCM de Thème 1 les ont
    # portés jusqu'en production, parce que les générateurs remplaçaient le
    # <title> de l'onglet — que personne ne lit — et pas le titre de la page.
    # Ce garde-fou refuse désormais toute trace du lot d'origine.
    for _reste in ("SOS serre", "Packet Tracer", "Adresse IP fixe"):
        if _reste in s:
            raise SystemExit("Reste du gabarit d'origine non remplacé : %r" % _reste)

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
