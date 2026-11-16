# -*- coding: utf-8 -*-
"""registre_regles.py — le registre des règles d'or, lu dans le journal.

POURQUOI
--------
La règle n°10 dit que le journal fait foi, et que tout nouveau numéro se prend
dans le « Registre central » en tête de `JOURNAL_DES_DECISIONS.md`. Ce tableau
s'est arrêté au n°21 ; les règles suivantes ont été numérotées dans leurs
entrées. L'audit du 15/11/2026 (#721) en a trouvé la conséquence : **les
numéros n°322 et n°323 ont été attribués deux fois**, le 10/11 (sauvegarde
locale ; place des bonnes réponses) et le 14/11 (audit de `3e_C9.1`). Personne
ne s'est trompé de bonne foi : il n'y avait plus d'endroit où lire le dernier
numéro pris.

Ce fichier remplace la lecture à l'œil par une lecture mécanique du journal :

  · il relève, pour chaque numéro, la PREMIÈRE définition écrite (titre, date
    de l'entrée, ligne) et engendre `docs/REGISTRE_DES_REGLES_OR.md` ;
  · il donne le prochain numéro libre (`--prochain`) ;
  · il signale un numéro DÉFINI DEUX FOIS sous deux titres sans mot commun
    (`--verifier` sort à 1) — le défaut du 14/11, qu'il aurait vu.

CE QU'IL RECONNAÎT COMME UNE DÉFINITION
---------------------------------------
Les formes que le journal emploie réellement (relevées le 15/11/2026), de la
plus sûre à la moins sûre — exergue, puce, phrase :
  « Règle d'or n°91 (clé de voûte) — titre »   « > **Règle d'or n°331 — titre** »
  « ### n°30 — titre »   « - **n°174** — titre »   « **Règle n°22 (…)** : titre »
  « règle d'or n°322 : titre »
Les n°1 à n°21 n'ont leur titre que dans le tableau de tête : il est lu aussi.
Une ligne qui dit « renumérotée n°333 » rattache sa définition au nouveau
numéro : c'est ainsi que le doublon du 14/11 est résolu sans réécrire l'entrée.

CE QU'IL NE VOIT PAS
--------------------
Une règle définie dans une forme qu'il ne connaît pas, ou jamais écrite (le
journal du 13/08 en déclare dix-huit : n°17, n°19, n°156 à n°165…) : elle est
listée « sans définition trouvée », jamais inventée. Le titre retenu est la
première phrase trouvée, coupée à 140 caractères — pas un résumé.

Usage :
    python3 _outils/registre_regles.py              # vérifie : 1 si un numéro est défini deux fois
    python3 _outils/registre_regles.py --ecrire     # vérifie, et écrit docs/REGISTRE_DES_REGLES_OR.md
    python3 _outils/registre_regles.py --prochain   # le prochain numéro libre
Sans option, il n'écrit rien : c'est ainsi que `rapport_audit.py` le lance, sur le dépôt.
Sortie : 0 · 1 doublon · 2 journal illisible ou aucune règle trouvée (règle n°299).
"""

import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNAL = os.path.join(RACINE, "JOURNAL_DES_DECISIONS.md")
SORTIE = os.path.join(RACINE, "docs", "REGISTRE_DES_REGLES_OR.md")

#: une entrée datée du journal : « ## 15/11/2026 — … », « ## 2026-08-08 — … », « ## 8 août 2026 — … »
ENTREE = re.compile(r"^##\s+(.{0,40}?\b(?:\d{1,2}[/ ]\S+[/ ]\d{4}|\d{4}-\d{2}-\d{2}))")
SEP = r"\s*(?:\*\*)?\s*(?:\([^)]{0,40}\))?\s*(?:\*\*)?\s*[—–:]\s*(?:\*\*)?\s*"
FORMES = [
    # « exergue » : une règle qu'on INTRODUIT — un titre d'entrée ou de section, une citation en exergue
    ("exergue", re.compile(r"^(?:#{2,4}\s+|>\s*\*\*)\s*(?:\*\*)?[Rr]ègle d['’]or n°\s?(\d+)" + SEP + r"(.+)")),
    ("exergue", re.compile(r"^#{3,4}\s+n°\s?(\d+)\s*[—–:]\s*(.+)")),
    ("exergue", re.compile(r"^>\s*\*\*Règle d['’]or n°\s?(\d+)\.\*\*\s*(.+)")),       # « > **Règle d'or n°306.** Une séquence… »
    ("exergue", re.compile(r"^#{3,4}\s+Règle d['’]or n°\s?(\d+)\s*()$")),                  # titre seul : l'énoncé est la ligne suivante
    # « puce » : une règle rétablie OU un compte rendu rangé sous son numéro (« - **n°23** — la séance 3… »)
    ("puce", re.compile(r"^-\s+\*\*n°\s?(\d+)\*\*\s*[—–:]\s*(.+)")),
    ("puce", re.compile(r"^-?\s*\*\*Règle n°\s?(\d+)[^*]{0,40}\*\*\s*:\s*(.+)")),
    # « phrase » : la règle nommée au fil d'une phrase, avec son énoncé
    ("phrase", re.compile(r"[Rr]ègle d['’]or n°\s?(\d+)" + SEP + r"(.+)")),
]
RENUMEROTEE = re.compile(r"renumérotée n°\s?(\d+)")
MOTS_VIDES = set("le la les un une des de du d l à au aux et ou en est sont son sa ses se ne pas qui que "
                 "dans sur par pour ce cette il elle on y a".split())


def nettoyer(titre):
    t = re.sub(r"\*?\(renumérotée[^)]*\)\*?", "", titre)
    t = re.sub(r"\*\*|`|«|»|“|”", "", t)
    t = re.sub(r"\s+", " ", t).strip(" .;:—–-")
    return t[:140] + ("…" if len(t) > 140 else "")


def mots(titre):
    return {m for m in re.findall(r"[a-zàâçéèêëîïôûùüœ]{3,}", titre.lower()) if m not in MOTS_VIDES}


def lire(chemin=None):
    """{numéro: [ (force, titre, date, ligne), … ]} dans l'ordre du journal."""
    defs, date = {}, "?"
    with open(chemin or JOURNAL, encoding="utf-8") as f:
        lignes = f.read().split("\n")
    debut = next((i for i, l in enumerate(lignes) if l.startswith("Règle de réservation")), 0)
    for i, l in enumerate(lignes):
        if i < debut:            # le tableau de tête : les n°1 à n°21 n'ont leur titre que là
            m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", l)
            if m:
                defs.setdefault(int(m.group(1)), []).append(("tableau", nettoyer(m.group(2)), "registre de tête", i + 1))
            continue
        m = ENTREE.match(l)
        if m:
            date = m.group(1).strip(" —-")
        for force, motif in FORMES:
            m = motif.search(l)
            if not m:
                continue
            n, titre = int(m.group(1)), nettoyer(m.group(2))
            if not titre:
                suite = next((x for x in lignes[i + 1:i + 4] if x.strip()), "")
                titre = nettoyer(re.sub(r"^[>#\-\s]+", "", suite))
            if len(titre.split()) < 3:
                continue
            r = RENUMEROTEE.search(l)
            if r:
                n = int(r.group(1))
            defs.setdefault(n, []).append((force, titre, date, i + 1))
            break
    return defs


def doublons(defs):
    """Les numéros INTRODUITS une seconde fois (en exergue, dans une autre entrée) sous un titre sans mot commun.

    Une puce « - **n°23** — la séance 3 portait… » n'est pas une seconde définition : le journal range ainsi
    ses comptes rendus sous le numéro de la règle appliquée (essayé le 15/11 : neuf faux doublons sur onze).
    """
    sortie = []
    for n, occ in sorted(defs.items()):
        premiere = occ[0]
        for autre in occ[1:]:
            if autre[0] != "exergue" or autre[2] == premiere[2]:
                continue
            if not (mots(premiere[1]) & mots(autre[1])):
                sortie.append((n, premiere, autre))
                break
    return sortie


def tableau_de_tete(chemin=None):
    """Les numéros réservés dans le tableau de tête (un numéro peut y être réservé avant d'être écrit)."""
    with open(chemin or JOURNAL, encoding="utf-8") as f:
        tete = f.read().split("Règle de réservation")[0]
    return {int(m) for m in re.findall(r"^\|\s*(\d+)\s*\|", tete, re.M)}


def ecrire(defs, dbl):
    nums = sorted(defs)
    haut = max(nums)
    manquent = [n for n in range(1, haut + 1) if n not in defs]
    L = ["# Registre des règles d'or",
         "",
         "> Fichier **engendré** par `python3 _outils/registre_regles.py` à partir de `JOURNAL_DES_DECISIONS.md` "
         "— ne pas l'éditer à la main : le journal fait foi (règle n°10). Le titre est la première définition "
         "trouvée dans le journal, coupée à 140 caractères ; le texte complet est à la ligne indiquée.",
         "",
         "**Prochain numéro libre : n°%d.** Le réserver en tête du lot qui l'introduit (tableau du journal), "
         "puis relancer ce script." % prochain(defs),
         "",
         "%d numéros définis, du n°1 au n°%d." % (len(nums), haut),
         ""]
    if dbl:
        L += ["## ⚠ Numéros définis deux fois", ""]
        for n, a, b in dbl:
            L.append("- **n°%d** — %s (%s, l. %d) **et** %s (%s, l. %d)" % (n, a[1], a[2], a[3], b[1], b[2], b[3]))
        L.append("")
    if manquent:
        L += ["## Sans définition trouvée", "",
              "Numéros cités ou réservés dont le journal n'écrit pas le texte dans une forme reconnue "
              "(certains n'ont jamais été écrits : entrée du 13/08/2026). Rien n'est inventé ici.", "",
              ", ".join("n°%d" % n for n in manquent), ""]
    L += ["## Les règles", "", "| N° | Titre (première définition) | Entrée | Ligne du journal |", "|---|---|---|---|"]
    for n in nums:
        _f, titre, date, ligne = defs[n][0]
        L.append("| %d | %s | %s | %d |" % (n, titre.replace("|", "∣"), date, ligne))
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    with open(SORTIE, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return manquent


def prochain(defs, chemin=None):
    return max(set(defs) | tableau_de_tete(chemin)) + 1


def main(argv):
    if not os.path.exists(JOURNAL):
        print("❌ EN PANNE : journal introuvable (%s)" % JOURNAL)
        return 2
    defs = lire()
    if not defs:
        print("❌ EN PANNE : aucune règle reconnue dans le journal (règle n°299)")
        return 2
    if "--prochain" in argv:
        print("n°%d" % prochain(defs))
        return 0
    dbl = doublons(defs)
    if "--ecrire" in argv:
        manquent = ecrire(defs, dbl)
        print("écrit : %s — %d règles, %d sans définition trouvée, prochain n°%d"
              % (os.path.relpath(SORTIE, RACINE), len(defs), len(manquent), prochain(defs)))
    for n, a, b in dbl:
        print("✘ n°%d défini deux fois : « %s » (%s, l. %d) et « %s » (%s, l. %d)"
              % (n, a[1][:70], a[2], a[3], b[1][:70], b[2], b[3]))
    if dbl:
        print("✘ %d numéro(s) défini(s) deux fois : renuméroter la seconde (« renumérotée n°X » sur sa ligne)" % len(dbl))
        return 1
    print("✅ aucun numéro de règle d'or n'est défini deux fois (%d numéros lus, prochain n°%d)"
          % (len(defs), prochain(defs)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
