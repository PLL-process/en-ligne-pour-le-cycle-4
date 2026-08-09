# -*- coding: utf-8 -*-
"""Assemble le QCM 3e_C1.1 à C1.4 à partir du gabarit maison et de `q.py`.

Une seule source de vérité pour les questions (`q.py`), un seul générateur
(ce fichier) — règle d'or n°38. Le moteur du QCM (barème, minuteur, modes,
sauvegarde) n'est pas recopié à la main : il est repris tel quel du gabarit,
seuls le bloc `const QUESTIONS` et les libellés propres au lot sont remplacés.

Deux règles récentes sont câblées ici :

  · **n°45** — l'entraînement s'ouvre sur ce qui a été fait. Ce lot est
    MULTI-CODE : le QCM lit `#codes=C1.2,C1.1` dans l'adresse et se restreint
    aux compétences effectivement travaillées, ou `#depart=court` et s'ouvre
    alors sur le parcours de dix questions.

  · **n°51** — ce que l'élève voit en premier se vérifie en premier. Le
    gabarit vient d'un lot de Thème 2 ; son `<h1>` et son sous-titre AFFICHÉS
    parlaient de « SOS serre » et de Packet Tracer, et six QCM de Thème 1 les
    ont portés jusqu'en production. Ce générateur les remplace, puis REFUSE
    d'écrire s'il en reste la moindre trace.

Usage :
    python3 build_qcm.py <gabarit.html> <sortie.html>
puis  node _outils/fix_r.js <sortie.html> 512
"""

import json
import re
import sys

import q as banque

GRAINE = 731

ORDRE = ("expl", "ex", "err")

# Règle d'or n°45 — l'entraînement s'ouvre sur ce qui a été fait.
# Le fragment est ajouté à la fin du moteur : il ne touche à rien, il ne fait
# que préselectionner des modes déjà existants du gabarit.
OUVERTURE_CIBLEE = """
/* ══════ Règle d'or n°45 — ouvrir sur ce que l'élève a déjà travaillé ══════ */
/* Cette séquence porte SIX codes : la séquence sait lesquels ont été validés et
   les passe dans l'adresse. Deux formes possibles :
     #codes=C1.2,C1.1  → révision ciblée sur ces compétences seulement ;
     #depart=court     → parcours de dix questions, quand rien n'est validé.
   Dans les deux cas on ne fait que préselectionner : le parcours complet reste
   à un clic. On choisit ce qu'on propose EN PREMIER, on n'interdit rien. */
(function ouvrirSurCeQuiAEteFait(){
  const h = location.hash || "";
  const hote = document.getElementById("porteeCiblee");

  const mCodes = h.match(/codes=([A-Za-z0-9.,]+)/);
  if(mCodes){
    const demandes = mCodes[1].split(",").filter(c => COMP_LABELS[c]);
    if(demandes.length){
      /* le gabarit ne sait cibler qu'UNE compétence à la fois. On passe donc par
         setMode("cible") — qui met à jour les boutons, le tableau de bord et le
         sélecteur — puis on ÉLARGIT la sous-liste à la liste demandée. Faire
         l'inverse (écrire etat.sousListe puis appeler une fonction de rendu)
         laissait l'interface annoncer un mode et en afficher un autre. */
      $("selComp").value = demandes[0];
      setMode("cible");
      etat.sousListe = QUESTIONS.map((q,i)=>i).filter(i => demandes.includes(QUESTIONS[i].c));
      etat.courante = etat.sousListe[0];
      rendreTout();
      if(hote){
        hote.hidden = false;
        hote.innerHTML = "🎯 Tu arrives depuis la séquence&nbsp;: ce QCM s'ouvre sur les <b>" +
          etat.sousListe.length + " questions</b> qui portent sur <b>" +
          demandes.join(", ") + "</b> — les compétences que tu as déjà travaillées. " +
          "Pour les 30, choisis <b>« Parcours complet »</b> ci-dessus.";
      }
      return;
    }
  }

  if(/depart=court/.test(h)){
    setMode("dix");
    if(hote){
      hote.hidden = false;
      hote.innerHTML = "🎯 Tu arrives depuis la séquence, qui n'est pas encore commencée&nbsp;: " +
        "ce QCM s'ouvre sur un <b>parcours court de 10 questions</b>, pour te tester sans être " +
        "submergé·e. Pour les 30, choisis <b>« Parcours complet »</b> ci-dessus.";
    }
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


JALONS = {
    0: "/* ═══ C1.1 — Les innovations de rupture ═══ */",
    8: "/* ═══ C1.2 — De la découverte scientifique à ses effets ═══ */",
    15: "/* ═══ C1.3 — L'incidence d'un OST sur la société ═══ */",
    23: "/* ═══ C1.4 — L'incidence des contraintes sociétales sur les OST ═══ */",
}


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

    remplacements = [
        ("/* Banque de questions — Shenzhen 3e : 30 questions "
         "(C3.1 : 8 · C3.3 : 8 · C3.4 : 7 · C3.2 : 7) */",
         "/* Banque de questions — Tsinghua 3e : 30 questions sur les quatre codes "
         "(C1.1 : 8 · C1.2 : 7 · C1.3 : 8 · C1.4 : 7), dont 11 illustrées. Chiffres "
         "publics et sourcés ; les questions touchant aux données du PNUE portent la "
         "discipline de la règle n°68. */"),

        ('const KEY="qcm_3e_C3.1-C3.4_shenzhen";', 'const KEY="qcm_3e_C1_tsinghua";'),

        ("""const COMP_LABELS={
  "C3.1":"3e_C3.1 — Établir une liste d'objets ou systèmes techniques possibles",
  "C3.3":"3e_C3.3 — Évaluer les solutions selon des exigences ou critères identifiés",
  "C3.4":"3e_C3.4 — Définir et mettre en œuvre un protocole de mesure",
  "C3.2":"3e_C3.2 — Choisir et argumenter en tenant compte du cycle de vie et des trois piliers" };""",
         # Règle d'or n°42 : ces formulations sont recopiées du référentiel, pas résumées.
         """const COMP_LABELS={
  "C1.1":"3e_C1.1 — Identifier les innovations de rupture qui sont attachées à l\u2019évolution d\u2019un OST.",
  "C1.2":"3e_C1.2 — Mettre en relation une découverte scientifique avec ses développements technologiques et leurs effets sur la société.",
  "C1.3":"3e_C1.3 — Exprimer dans un argumentaire court l\u2019incidence d\u2019un OST sur la société.",
  "C1.4":"3e_C1.4 — Exprimer dans un argumentaire court l\u2019incidence des contraintes sociétales sur les OST." };"""),

        ("<title>Thème 1 · 3e — QCM : Shenzhen, comment refroidir un local qui surchauffe ? "
         "(3e_C3.1 à C3.4)</title>",
         "<title>Thème 1 · 3e — QCM : Tsinghua, robots, drones et IA face aux feux "
         "(3e_C1.1 à C1.4)</title>"),

        # Règle d'or n°51 — le titre AFFICHÉ, et son sous-titre. C'est ce que l'élève lit.
        ("<h1>Thème 1 · 3e — QCM : Shenzhen, comment refroidir un local qui surchauffe ?</h1>",
         "<h1>Thème 1 · 3e — QCM : Tsinghua, robots, drones et IA face aux feux</h1>"),
        ('<p class="subtitle">Caractériser et choisir une solution (3e_C3.1 à C3.4) — protocole '
         "de mesure, évaluation des solutions et cycle de vie</p>",
         '<p class="subtitle">Deux ruptures, une découverte de 1800, et deux argumentaires '
         "courts — identifier les innovations de rupture (3e_C1.1), relier une découverte à ses "
         "effets (C1.2), dire ce que l'objet change pour la société (C1.3) et ce que la société "
         "oblige l'objet à changer (C1.4)</p>"),

        ('<span class="badge niveau">3e</span>', '<span class="badge niveau">3e</span>'),
        ('<span class="badge code">3e_C3.1</span><span class="badge code">3e_C3.2</span>'
         '<span class="badge code">3e_C3.3</span><span class="badge code">3e_C3.4</span>',
         '<span class="badge code">3e_C1.1</span><span class="badge code">3e_C1.2</span>'
         '<span class="badge code">3e_C1.3</span><span class="badge code">3e_C1.4</span>'),

        ("30 questions · 1 illustrée · chaque distracteur réfuté",
         "30 questions · 11 illustrées · chaque distracteur réfuté"),

        ("""      <option value="C3.1">3e_C3.1 — Établir une liste de solutions possibles</option>
      <option value="C3.3">3e_C3.3 — Évaluer selon des exigences identifiées</option>
      <option value="C3.4">3e_C3.4 — Définir et mettre en œuvre un protocole</option>
      <option value="C3.2">3e_C3.2 — Choisir et argumenter sur les trois piliers</option>""",
         """      <option value="C1.1">3e_C1.1 — Les innovations de rupture</option>
      <option value="C1.2">3e_C1.2 — D'une découverte à ses effets sur la société</option>
      <option value="C1.3">3e_C1.3 — L'incidence d'un OST sur la société</option>
      <option value="C1.4">3e_C1.4 — L'incidence des contraintes sociétales</option>"""),

        ("QCM d’entraînement 3e_C3.1 à C3.4 · Thème 1",
         "QCM d’entraînement 3e_C1.1 à C1.4 · Thème 1"),
    ]
    for avant, apres in remplacements:
        if s.count(avant) != 1:
            raise SystemExit("Motif absent ou ambigu dans le gabarit :\n%r" % avant[:90])
        s = s.replace(avant, apres)

    s = s.replace("sequence_3e_C3.1-C3.4_shenzhen.html",
                  "sequence_3e_C1.1-C1.4_tsinghua_feux.html")

    # zone d'accueil de la règle n°45, juste avant le lien de retour
    ancre = '<p style="text-align:center"><a href="sequence_3e_C1.1-C1.4_tsinghua_feux.html">'
    if s.count(ancre) != 1:
        raise SystemExit("Ancre du bandeau de portée introuvable.")
    s = s.replace(ancre,
                  '<p class="portee-ciblee" id="porteeCiblee" hidden role="status"></p>\n' + ancre)

    # le fragment de la règle n°45, à la toute fin du moteur
    i = s.rfind("\n</script>")
    if i < 0:
        raise SystemExit("Fin de script introuvable.")
    s = s[:i] + "\n" + OUVERTURE_CIBLEE + s[i:]

    # un peu de style pour le bandeau
    s = s.replace("  .q-comp{",
                  "  .portee-ciblee{max-width:880px;margin:0 auto 12px;padding:9px 14px;"
                  "border:1px solid var(--head);border-radius:10px;background:#2b1a3f;"
                  "font-size:.85em;color:var(--text)}\n  .q-comp{")

    # ── Contrôles avant écriture ────────────────────────────────────────────
    # Règle d'or n°51 : le gabarit vient d'un lot de Thème 2. Aucune trace du lot
    # d'origine ne doit survivre — c'est exactement ce qui a échappé six fois.
    for reste in ("SOS serre", "Packet Tracer", "Adresse IP fixe", "Martinique — 4e"):
        if reste in s:
            raise SystemExit("Reste du gabarit d'origine non remplacé : %r" % reste)
    restes = re.findall(r"\b[345]e_C3\.\d\b|\bC3\.\d\b", s)
    if restes:
        raise SystemExit("Restes du gabarit 3e non remplacés : %s" % sorted(set(restes)))
    for code in ("C1.1", "C1.2", "C1.3", "C1.4"):
        if s.count('"%s"' % code) < 2:
            raise SystemExit("Le code %s n'apparaît pas assez : filtre ou questions manquants." % code)

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
