# -*- coding: utf-8 -*-
"""controle_echantillonnage.py — combien de questions par compétence ?

Un QCM peut **mobiliser** une compétence sans l'**évaluer**. La distinction n'est
pas rhétorique : en dessous de cinq questions, un score par code n'est plus une
mesure, c'est un tirage. Sur quatre questions, un élève qui en sait la moitié
obtient 2/4 ou 4/4 selon lesquelles il connaît — et l'écart part au LSU.

L'audit externe ChatGPT du Thème 2 le formulait ainsi : « certaines compétences
ne disposent que de quatre questions » et « quatre questions sont trop peu
fiables pour valider isolément une compétence ». Vérifié : c'est exact, et ce
script dit exactement où.

Ce contrôle **n'interdit rien**. Un code peu échantillonné est légitime : il
signale un appui, un rappel, un pont vers un autre lot. Ce qui ne l'est pas,
c'est de reporter son score au LSU comme s'il valait celui du code principal.
Le script sépare donc, pour chaque banque, les codes **évaluables** de ceux qui
sont seulement **mobilisés**.

Seuil : **5 questions**. En dessous, on cite le code en appui ; on ne conclut pas.

Règle d'or n°202 : un QCM peut mobiliser une compétence sans l'évaluer.

Usage : python3 _outils/controle_echantillonnage.py [chemin]
"""

import collections
import os
import re
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

SEUIL_EVALUABLE = 5


def banques(racine):
    for dossier, _, fichiers in os.walk(racine):
        if "_archive" in dossier:
            continue
        for f in sorted(fichiers):
            if re.match(r"qcm.*\.html$", f, re.I):
                yield os.path.join(dossier, f)


#: tout code du programme cité dans un libellé — « 4e_C4.1 · C4.2 » en compte deux.
#: On cherche « C4.1 », pas « 4e_C4.1 » : le préfixe de niveau n'est écrit qu'une
#: fois quand le libellé énumère plusieurs codes de la même famille.
CODE_CITE = re.compile(r"C\d\.\d")


def libelles(t):
    """Ce que la banque dit de ses propres clés (COMP_LABELS)."""
    m = re.search(r"const COMP_LABELS\s*=\s*\{(.*?)\};", t, re.S)
    if not m:
        return {}
    return dict(re.findall(r'"([^"]+)"\s*:\s*"((?:[^"\\]|\\.)*)"', m.group(1)))


def mesurer(chemin):
    with open(chemin, encoding="utf-8", errors="ignore") as fh:
        t = fh.read()
    m = re.search(r"const QUESTIONS\s*=\s*\[", t)
    if not m:
        return None
    codes = collections.Counter(re.findall(r'\bc:"([^"]+)"', t[m.end():]))
    if not codes:
        return None

    # Douze banques du dépôt regroupent leurs questions sous une clé maison
    # (EN, ID, RES, CAP…) dont le LIBELLÉ nomme les codes du programme couverts.
    # Compter ces clés comme des compétences serait compter une convention
    # d'écriture, pas une chose (règle n°184) : une clé qui recouvre deux codes
    # n'est pas un code sous-échantillonné, c'est un groupe.
    lab = libelles(t)
    groupes = {cle: len(CODE_CITE.findall(lab.get(cle, ""))) > 1 for cle in codes}

    return dict(fichier=os.path.basename(chemin), codes=codes,
                total=sum(codes.values()), groupes=groupes, libelles=lab)


def main(argv):
    racine = argv[1] if len(argv) > 1 else RACINE
    mesures = [m for m in (mesurer(p) for p in banques(racine)) if m]
    if not mesures:
        print("Aucune banque de questions trouvée sous %s" % racine)
        return 0

    signalees = []
    print("%-52s %-6s %-28s %s" % ("QCM", "q", "codes évaluables (≥ 5 q.)", "codes seulement mobilisés"))
    print("─" * 118)
    for m in sorted(mesures, key=lambda x: x["fichier"]):
        eval_ = {c: n for c, n in sorted(m["codes"].items()) if n >= SEUIL_EVALUABLE}
        mob = {c: n for c, n in sorted(m["codes"].items())
               if n < SEUIL_EVALUABLE and not m["groupes"].get(c)}
        if mob:
            signalees.append((m, mob))
        print("%-52s %-6d %-28s %s" % (
            m["fichier"][:50], m["total"],
            ", ".join("%s:%d" % kv for kv in eval_.items())[:26] or "—",
            ", ".join("%s:%d" % kv for kv in mob.items()) or "—"))

    print()
    print("%d banques · seuil : %d questions pour qu'un code soit évaluable seul"
          % (len(mesures), SEUIL_EVALUABLE))
    if signalees:
        print("\n%d banque(s) portant au moins un code sous le seuil :" % len(signalees))
        for m, mob in signalees:
            print("     %-50s %s" % (m["fichier"][:48], ", ".join("%s (%d q.)" % kv for kv in mob.items())))
        print("   Ces codes se citent en appui dans la fiche du lot. Ils ne se reportent pas")
        print("   seuls au LSU : le score d'un code à 4 questions n'est pas une mesure.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
