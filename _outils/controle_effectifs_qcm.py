# -*- coding: utf-8 -*-
"""controle_effectifs_qcm.py — un QCM doit dire vrai sur sa propre taille.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le 31/08/2026, la banque du lampadaire (`5e_C4.1` → `C4.8`) est passée de **32**
à **36** questions : quatre codes n'en avaient que quatre chacun, sous le seuil
d'évaluabilité, et il leur manquait de vraies notions — pas des questions de
remplissage.

Avant d'écrire la première, on a cherché où le nombre « 32 » était écrit. Il
l'était à **dix endroits**, dans six fichiers :

  · dans la page elle-même, cinq fois — le badge de l'en-tête, le compteur
    « Restantes », le bouton « Parcours complet (32) », le total affiché pendant
    le parcours, le total du bilan — plus le commentaire en tête de banque ;
  · dans la séquence, qui invite à « 32 questions » ;
  · dans le lexique, qui annonce « 32 notions » ;
  · dans la fiche pédagogique et la synthèse professeur, « QCM 32 q (4 par
    code) » ;
  · dans le manifeste du lot, `questions_qcm` et les huit `questions_par_code` ;
  · dans le rapport de tests, et dans `_outils/build_audit.py`, qui le recopie
    dans l'audit.

Aucune de ces dix n'est fausse aujourd'hui — on a vérifié les **65 banques** du
dépôt avant d'écrire ce fichier, et toutes disent vrai. Ce contrôle n'est donc
pas né d'une faute constatée mais d'une faute **imminente** : celle qu'on
allait commettre en changeant une banque et en oubliant trois de ses dix échos
(règle d'or n°261 — corriger l'occurrence qu'on a sous les yeux, c'est croire
qu'il n'y en a qu'une).

CE QU'IL VÉRIFIE
----------------
**1. La page contre elle-même.** Chaque nombre qu'une page de QCM affiche à son
propre sujet doit valoir le nombre d'entrées de sa banque.

**2. Le manifeste du lot contre la banque.** `questions_qcm`, chaque valeur de
`questions_par_code` et `questions_illustrees` sont confrontés au comptage réel —
par étiquette `c:` pour les codes, par bloc `img:{…}` pour les illustrations.

`questions_illustrees` a été ajouté le 31/08/2026 : ce contrôle confrontait déjà
521 nombres auto-déclarés, mais pas celui-là, et **deux** manifestes étaient en
écart — `5e_C6.1` (2 annoncées, 3 dans la banque) et `5e_C2.1` (4 annoncées, 5).

**3. Le lexique contre lui-même.** « N notions » doit valoir le nombre d'entrées
qu'il porte — c'est le seul nombre qu'un lexique affirme.

CE QU'IL NE VÉRIFIE PAS, ET LE DIT
-----------------------------------
Il ne lit **aucune prose libre** : ni la fiche pédagogique, ni la synthèse, ni le
rapport de tests, ni le journal. « QCM 32 q (4 par code) » y est une phrase, pas
un champ, et un contrôle qui prétendrait la lire partout signalerait des
tournures correctes (règles n°242 et n°248). Ces fichiers-là se corrigent à la
main — et la liste ci-dessus dit où regarder.

Il ne juge pas non plus la **qualité** de l'échantillonnage : combien de
questions un code mérite est l'affaire de `controle_echantillonnage.py`.

Usage :
    python3 _outils/controle_effectifs_qcm.py           # rapport complet
    python3 _outils/controle_effectifs_qcm.py --muet    # seulement les écarts
Sortie : 0 si toutes les banques disent vrai sur leur taille, 1 sinon.
"""

import collections
import json
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

#: les cinq endroits où une page de QCM parle de sa propre taille, plus le
#: commentaire de tête. Chaque motif est une convention réelle du dépôt.
AUTO_DECLARATIONS = [
    ("badge de l'en-tête", re.compile(r'badge theme">\s*(\d+)\s*questions', re.I)),
    ("compteur « Restantes »", re.compile(r'id="dRest"[^>]*>(\d+)<')),
    ("bouton « Parcours complet »",
     re.compile(r'data-mode="complet"[^>]*>[^<(]*\((\d+)\)')),
    ("total pendant le parcours", re.compile(r'id="qTot"[^>]*>(\d+)<')),
    ("total du bilan", re.compile(r'id="rTot"[^>]*>(\d+)<')),
    ("commentaire de tête de banque",
     re.compile(r"/\*\s*Banque[^*]{0,120}?(\d+)\s*questions", re.I)),
]

NOTIONS = re.compile(r'class="sub">\s*(\d+)\s*notions', re.I)
ENTREE_LEXIQUE = re.compile(r'<(dt)\b|class="(?:mot|terme)"', re.I)


def banque(texte):
    """Le bloc `const QUESTIONS = [ … ]`, ou None si la page n'en porte pas."""
    i = texte.find("const QUESTIONS")
    if i < 0:
        return None
    j = texte.find("\n];", i)
    return texte[i:j] if j > 0 else None


def comptage(bloc):
    """(nombre total de questions, nombre par étiquette `c:`)."""
    codes = re.findall(r'\{c:"([^"]+)"', bloc)
    return len(codes), collections.Counter(codes)


#: Une question illustrée porte un bloc `img:{src:…}`. Le nombre qu'un manifeste
#: en annonce est un champ, pas une phrase (règle d'or n°264) : il se confronte.
#: Ajouté le 31/08/2026, après DEUX manifestes trouvés en écart — `5e_C6.1`
#: (2 déclarées, 3 dans la banque) et `5e_C2.1` (4 déclarées, 5 dans la banque).
#: Ce contrôle confrontait déjà 521 nombres auto-déclarés, mais pas celui-là.
ILLUSTREE = re.compile(r"\bimg\s*:\s*\{")


def comptage_illustrees(bloc):
    """Le nombre de questions de la banque qui portent une image."""
    return len(ILLUSTREE.findall(bloc))


def pages(racine):
    for dossier, _, fichiers in os.walk(racine):
        if any(e in dossier for e in ECARTES):
            continue
        for f in sorted(fichiers):
            if re.match(r"qcm.*\.html$", f, re.I):
                yield os.path.join(dossier, f)


def manifestes(dossier, banque_nom):
    """Les manifestes qui NOMMENT cette banque dans leur bloc `fichiers`.

    Un manifeste posé dans le même dossier ne parle pas forcément de cette
    banque-là : `4e_C4.7/` en porte quatre, dont trois appartiennent au lot
    « réseaux » et une seule au lot « SOS serre ». Confronter tous les
    manifestes à toutes les banques du dossier produirait neuf faux écarts —
    et un contrôle qui signale du faux finit ignoré (règle d'or n°248). Le
    rattachement est donc **déclaré par le manifeste**, jamais déduit du
    voisinage (règle d'or n°263).
    """
    for f in sorted(os.listdir(dossier)):
        if not re.match(r"manifest.*\.json$", f, re.I):
            continue
        chemin = os.path.join(dossier, f)
        try:
            donnees = json.load(open(chemin, encoding="utf-8")) or {}
        except (ValueError, OSError):
            continue
        fichiers = donnees.get("fichiers")
        if isinstance(fichiers, list):        # certains manifestes listent à plat
            cite = [x for x in fichiers if isinstance(x, str)]
        elif isinstance(fichiers, dict):
            cite = fichiers.get("qcm")
        else:
            cite = None
        cites = cite if isinstance(cite, list) else [cite] if cite else []
        cites = [c for c in cites if re.match(r"qcm.*\.html$", os.path.basename(str(c)), re.I)]
        if any(os.path.basename(str(c)) == banque_nom for c in cites):
            yield chemin, donnees


def juger_page(chemin, ecarts, releve):
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    bloc = banque(texte)
    if bloc is None:
        releve["sans_banque"] += 1
        return
    total, par_code = comptage(bloc)
    if total == 0:
        releve["sans_banque"] += 1
        return
    releve["banques"] += 1
    nom = os.path.relpath(chemin, DEPOT)
    plat = re.sub(r"\s+", " ", texte)

    for quoi, motif in AUTO_DECLARATIONS:
        m = motif.search(plat)
        if not m:
            continue
        releve["declarations"] += 1
        if int(m.group(1)) != total:
            ecarts.append("%s\n     %s annonce %s, la banque en porte %d"
                          % (nom, quoi, m.group(1), total))

    for mf, donnees in manifestes(os.path.dirname(chemin), os.path.basename(chemin)):
        releve["manifestes"] += 1
        contenu = donnees.get("contenu") or {}
        dit = contenu.get("questions_qcm")
        if isinstance(dit, int):
            releve["declarations"] += 1
            if dit != total:
                ecarts.append("%s\n     %s : questions_qcm = %d, la banque en porte %d"
                              % (nom, os.path.basename(mf), dit, total))
        for code, n in (contenu.get("questions_par_code") or {}).items():
            releve["declarations"] += 1
            court = code.split("_")[-1]
            reel = par_code.get(court, par_code.get(code, 0))
            if n != reel:
                ecarts.append("%s\n     %s : questions_par_code[%s] = %s, mesuré %d"
                              % (nom, os.path.basename(mf), code, n, reel))
        illustrees = contenu.get("questions_illustrees")
        if isinstance(illustrees, int):
            releve["declarations"] += 1
            reel = comptage_illustrees(bloc)
            if illustrees != reel:
                ecarts.append("%s\n     %s : questions_illustrees = %d, la banque en porte %d"
                              % (nom, os.path.basename(mf), illustrees, reel))


def juger_lexique(chemin, ecarts, releve):
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    m = NOTIONS.search(re.sub(r"\s+", " ", texte))
    if not m:
        return
    releve["lexiques"] += 1
    releve["declarations"] += 1
    reel = len(ENTREE_LEXIQUE.findall(texte))
    if reel and int(m.group(1)) != reel:
        ecarts.append("%s\n     annonce %s notions, en porte %d"
                      % (os.path.relpath(chemin, DEPOT), m.group(1), reel))


def main(muet=False):
    ecarts = []
    releve = collections.Counter()

    for chemin in pages(DEPOT):
        juger_page(chemin, ecarts, releve)
    for dossier, _, fichiers in os.walk(DEPOT):
        if any(e in dossier for e in ECARTES):
            continue
        for f in sorted(fichiers):
            if re.match(r"lexique.*\.html$", f, re.I):
                juger_lexique(os.path.join(dossier, f), ecarts, releve)

    if not muet:
        print("%d banque(s) de QCM · %d manifeste(s) rattaché(s) par leur bloc « fichiers » · "
              "%d lexique(s)\n%d nombre(s) auto-déclarés confrontés"
              % (releve["banques"], releve["manifestes"], releve["lexiques"],
                 releve["declarations"]))
        print("     (%d page(s) « qcm… » sans bloc `const QUESTIONS` — hors périmètre)"
              % releve["sans_banque"])
        print("     NON LU : fiche pédagogique, synthèses, rapport de tests, journal — un\n"
              "     nombre y est une phrase, pas un champ, et se corrige à la main.")

    if ecarts:
        print("\n⛔ %d écart(s) — une page ne dit pas la vérité sur sa taille :" % len(ecarts))
        for e in ecarts:
            print("  " + e)
        return 1
    print("✅ chaque banque, chaque manifeste et chaque lexique annonce le nombre qu'il porte")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
