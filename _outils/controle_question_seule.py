# -*- coding: utf-8 -*-
"""controle_question_seule.py — une question se lit seule (règles d'or n°343, clé de voûte, n°344 et n°345 ; 21/11/2026).

LE CONSTAT
----------
Le 21/11/2026, Pascal demande d'améliorer les séances et les QCM du thème 1 à la lumière de deux « prompts maîtres »
d'audit. Tous les contrôles du dépôt sont verts sur le thème. La lecture question par question des QCM trouve pourtant :
  · « Les cinq étapes » du cycle de vie, dont la bonne réponse n'en cite que quatre (Shanghai) ; « Les six familles »
    d'exigences, dont la bonne réponse n'en cite que cinq (Hangzhou) — des listes raccourcies pour que la bonne réponse
    ne soit plus la plus longue ;
  · « S2 consomme 165 Wh/km, S1 seulement 18 », « Avec les quatre exigences du centre, combien de solutions passent ? »,
    « La solution la plus performante du tableau est aussi… » : l'élève qui révise trois semaines plus tard n'a plus la
    planche, ni le tableau, ni le nom de S1 ;
  · « En 4e à Hangzhou… », « Par rapport à la 5e… » : des renvois à une année que les élèves de Pascal n'ont pas faite
    avec lui (n°304) ;
  · neuf QCM de séquence sur quinze sous les six questions sur document, deux sans aucune ;
  · un billet de sortie (la preuve faite seul, n°330) sur une séquence du thème sur quatorze.
Pascal, le même jour : « ce que les outils ne voient pas, et que la lecture question par question trouve : il faut en
faire des clés de voûte, des règles d'or et des skills ». Cet outil mesure ce qui se lit dans le source ; le skill
`question-qui-se-lit-seule` porte la lecture que l'outil ne fait pas.

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Les QCM du gabarit maison (`qcm*.html` qui portent `const QUESTIONS = [`), hors archive et hors exports ; pour P1, les
pages `sequence*.html` qui portent le mode mission. Une question est lue dans ses champs `n`, `q`, `o`, `r`, `img`.

CE QUI EST MESURÉ
-----------------
Dans chaque question (les « refus » : --strict sort à 1) :
  S1  un code sans son nom — « S1 », « S2 », « P3 » dans l'énoncé ou les propositions, sans document sous la question
      et sans le nom à côté (« le vélo-cargo (S1) », « S2, la fourgonnette ») ;
  S2  un renvoi sans document — « du tableau », « sur le graphique », « dans ce projet », « de la séquence », « dans
      notre travail », « vu en classe » — alors que la question n'affiche aucun document (`img`) ;
  S3  une autre année — « en 5e », « en 4e », « l'an dernier », « au programme de » (n°304, étendue aux questions) ;
  S4  une notion qui souffle — la notion, affichée avec la question (« notion : … »), porte un nombre ou un code
      que seule la bonne réponse reprend (« La compétence CRCN 1.2 » au-dessus de « CRCN 1.2 — Gérer des données ») ;
  E1  une liste tronquée — la notion ou l'énoncé annonce un nombre (« Les cinq étapes ») et la bonne réponse est une
      liste qui n'a pas ce nombre d'éléments (n°344).
Par QCM et par séquence (les « chantiers » : toujours ⚠, jamais un refus) :
  D1  moins de six questions sur document dans un QCM rattaché à une séquence (n°345) ;
  P1  une séquence sans billet de sortie (n°330 : la preuve faite seul, sur un objet nouveau).

NON LU, à lire (skill `question-qui-se-lit-seule`) : qu'une donnée dont dépend la réponse manque à l'énoncé sans qu'un
mot la trahisse (« combien de solutions passent ? ») ; qu'une question évalue bien le code qu'elle porte, et pas le
programme ou une anecdote ; qu'un leurre parle la grandeur de la question (« au gramme près » pour des degrés) ; qu'une
convention de la maison rende un leurre défendable (l'énergie chimique sous la batterie) ; qu'un document affiché donne
la réponse au lieu de la faire trouver.

Usage : python3 _outils/controle_question_seule.py [--strict] [--muet] [--chantiers] [chemin…]
  --chantiers  détaille aussi D1 et P1 (sinon ils ne sont que comptés).
Sortie : 0 (mesure) · 1 au moins un refus (S1 à S4, E1) avec --strict · 2 rien lu (n°299 : un outil qui ne lit rien
est en panne).
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAINE = r'"((?:[^"\\]|\\.)*)"'
NOMBRES = {"deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10}
ANNONCE = re.compile(r"\b(%s)\b(?!\s+(?:fois|sur|à|ou|ans?|jours?|heures?|minutes?|secondes?|mois|essais?|élèves?)\b)"
                     % "|".join(NOMBRES), re.I)
# S1 : une lettre et un ou deux chiffres, seuls (« S1 », « P12 ») ; ni un code de compétence (« C3.1 », « 5e_C3 »),
# ni un format de papier, ni un domaine du socle.
CODE = re.compile(r"(?<![\w.°])([A-Z]\d{1,2})(?![\w.]|\s*:)")
# connus sans leur nom : formats de papier, domaines du socle, classes de flexibilité d'un cahier des charges (F0 à F3,
# vocabulaire enseigné), formules chimiques.
CODES_CONNUS = {"A3", "A4", "A5", "D1", "D2", "D3", "D4", "D5", "F0", "F1", "F2", "F3", "H2", "O2"}
RENVOI = re.compile(
    r"\bdu tableau\b|\ble tableau (?:donne|montre|indique|dit)\b|\bsur (?:le|ce) (?:graphique|schéma)\b"
    r"|\bsur la planche\b|\bci-dess(?:us|ous)\b|\bdans ce projet\b|\b(?:de|dans) la séquence\b"
    r"|\bdans notre (?:travail|étude|séquence|projet)\b|\bvu(?:e|s|es)? en classe\b|\bdans l['’]activité \d", re.I)
ANNEE = re.compile(r"\ben (?:6e|5e|4e|3e|sixième|cinquième|quatrième|troisième)\b|\bl['’]an dernier\b"
                   r"|\bl['’]année dernière\b|\bau programme de\b|\bpar rapport à la (?:6e|5e|4e)\b", re.I)


def net(t: str) -> str:
    t = re.sub(r"<[^>]+>", " ", t).replace("&nbsp;", " ").replace("\\\"", "\"").replace("\\n", " ")
    return re.sub(r"\s+", " ", t).strip()


def questions(chemin: str):
    """Les questions d'un QCM du gabarit maison : [(notion, énoncé, propositions, indice juste, a un document)]."""
    s = open(chemin, encoding="utf-8").read()
    b = re.search(r"const QUESTIONS = \[(.*?)\n\];", s, re.S)
    if not b:
        return None
    sortie = []
    for bloc in re.split(r"\n\s*\{\s*c:", b.group(1))[1:]:
        n = re.search(r"\bn:" + CHAINE, bloc)
        q = re.search(r"\bq:" + CHAINE, bloc)
        o = re.search(r"\bo:\[(.*?)\],\s*r:(\d+)", bloc, re.S)
        if not (q and o):
            continue
        props = [net(x) for x in re.findall(CHAINE, o.group(1))]
        sortie.append((net(n.group(1)) if n else "", net(q.group(1)), props, int(o.group(2)), bool(re.search(r"\bimg:\{", bloc))))
    return sortie


def liste(prop: str):
    """Les éléments d'une proposition écrite comme une liste (« a, b, c et d ») ; [] si ce n'en est pas une."""
    corps = prop.split(":", 1)[1] if ":" in prop else prop
    items = [x.strip() for x in re.split(r",|;|\bet\b", corps) if x.strip()]
    if len(items) >= 3 and all(len(x.split()) <= 4 for x in items):
        return items
    return []


def juger(notion, enonce, props, r, doc):
    """Les refus d'une question : [(code, ce qui est dit)]."""
    ecarts = []
    tout = enonce + " | " + " | ".join(props)
    if not doc:
        codes = []
        for m in CODE.finditer(tout):
            c = m.group(1)
            if c in CODES_CONNUS or c in codes:
                continue
            # nommé à côté : « le vélo-cargo (S1) », ou « S2, la fourgonnette »
            if re.search(r"\w\s*\(%s\)" % re.escape(c), tout) or re.search(r"%s,? (?:le|la|l['’]|les|un|une) " % re.escape(c), tout):
                continue
            codes.append(c)
        if codes:
            ecarts.append(("S1", "« %s » sans son nom, et sans document sous la question" % " », « ".join(codes)))
        m = RENVOI.search(enonce)
        if m:
            ecarts.append(("S2", "« %s » : la question renvoie à un document qu'elle n'affiche pas" % m.group(0)))
    m = ANNEE.search(tout)
    if m:
        ecarts.append(("S3", "« %s » : une autre année, que l'élève n'a peut-être pas faite ici (n°304)" % m.group(0)))
    if 0 <= r < len(props):
        # S4 : la notion s'affiche avec la question (« notion : … ») ; un nombre ou un code qu'elle partage avec la seule
        # bonne réponse la désigne (« La compétence CRCN 1.2 » au-dessus de « CRCN 1.2 — Gérer des données »).
        marques = set(re.findall(r"\d+(?:[.,]\d+)?", notion))
        seules = [m for m in marques if re.search(r"(?<![\d.,])%s(?![\d.,])" % re.escape(m), props[r])
                  and not any(re.search(r"(?<![\d.,])%s(?![\d.,])" % re.escape(m), x) for i, x in enumerate(props) if i != r)]
        if seules:
            ecarts.append(("S4", "la notion affichée « %s » porte « %s », que seule la bonne réponse reprend" % (notion, " », « ".join(seules))))
        tete = props[r].split(":", 1)[0] if ":" in props[r] else ""
        annonces = {NOMBRES[x.lower()] for x in ANNONCE.findall(notion + " " + enonce + " " + tete)}
        items = liste(props[r])
        if annonces and items and len(items) not in annonces:
            ecarts.append(("E1", "%s annoncé(e)s, %d cité(e)s dans la bonne réponse : « %s »"
                           % (" ou ".join(str(a) for a in sorted(annonces)), len(items), props[r][:70])))
    return ecarts


def fichiers(chemins):
    for c in chemins or [DEPOT]:
        if os.path.isfile(c):
            yield c
            continue
        for d, _, fs in os.walk(c):
            dd = d.replace(os.sep, "/")
            if "_archive" in dd or "/." in dd or "node_modules" in dd or "_exports" in dd:
                continue
            for f in sorted(fs):
                if f.endswith(".html") and (f.startswith("qcm") or f.startswith("sequence")):
                    yield os.path.join(d, f)


def main(argv) -> int:
    strict, muet, chantiers = "--strict" in argv, "--muet" in argv, "--chantiers" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    refus, travaux = [], []
    nq = nqcm = nseq = 0
    for p in fichiers(chemins):
        rel = os.path.relpath(p, DEPOT)
        nom = os.path.basename(p)
        if nom.startswith("qcm"):
            qs = questions(p)
            if not qs:
                continue
            nqcm += 1
            nq += len(qs)
            for i, (notion, enonce, props, r, doc) in enumerate(qs, 1):
                for code, dit in juger(notion, enonce, props, r, doc):
                    refus.append((code, rel, "Q%d « %s » — %s" % (i, enonce[:60], dit)))
            docs = sum(1 for q in qs if q[4])
            a_sequence = any(f.startswith("sequence") and f.endswith(".html") for f in os.listdir(os.path.dirname(p)))
            if a_sequence and docs < 6:
                travaux.append(("D1", rel, "%d question(s) sur document sur %d (au moins 6 : n°345)" % (docs, len(qs))))
        else:
            s = open(p, encoding="utf-8").read()
            if "<!-- mode-mission v1 : début" not in s:
                continue
            nseq += 1
            if not re.search(r'id="billetSortie"|[Bb]illet de sortie', s):
                travaux.append(("P1", rel, "aucun billet de sortie : la preuve faite seul manque (n°330)"))
    if not nqcm and not nseq:
        print("✘ rien n'a été lu : aucun QCM du gabarit maison, aucune séquence qui porte le mode mission")
        return 2
    par = defaultdict(int)
    for c, *_ in refus + travaux:
        par[c] += 1
    if not muet:
        for code, ou, dit in refus:
            print("  %s %s %s — %s" % ("✘" if strict else "⚠", code, ou, dit))
        if chantiers:
            for code, ou, dit in travaux:
                print("  ⚠ %s %s — %s" % (code, ou, dit))
    print("%d QCM lus (%d questions), %d séquence(s) · S1 code sans nom : %d · S2 renvoi sans document : %d · "
          "S3 autre année : %d · S4 notion qui souffle : %d · E1 liste tronquée : %d · chantiers : D1 moins de six "
          "questions sur document : %d · P1 séquence sans billet de sortie : %d"
          % (nqcm, nq, nseq, par["S1"], par["S2"], par["S3"], par["S4"], par["E1"], par["D1"], par["P1"]))
    print("     NON LU : une donnée qui manque sans qu'un mot la trahisse, une question hors de sa compétence, un leurre\n"
          "     d'une autre grandeur, un document qui donne la réponse — cela se lit, question par question\n"
          "     (skill `question-qui-se-lit-seule`).")
    if not refus:
        print("✅ aucune question ne renvoie ailleurs, et chaque liste annoncée est citée en entier (règles d'or n°343 et n°344)")
    return 1 if (strict and refus) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
