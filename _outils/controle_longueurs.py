# -*- coding: utf-8 -*-
"""controle_longueurs.py — la bonne réponse se devine-t-elle à sa longueur ?

Défaut classique du QCM rédigé à la main : on soigne la bonne réponse — nuancée,
complète, précise — et on expédie les distracteurs en quatre mots. L'élève qui ne
sait rien coche la plus longue et s'en tire très bien. Le QCM mesure alors
l'habileté au QCM, pas la technologie.

Deux mesures par banque :

  - **détachées** : questions où la bonne réponse s'écarte de plus de 8 caractères
    du peloton des distracteurs, dans un sens ou dans l'autre. C'est l'écart
    VISIBLE — le seul qui soit exploitable par un élève. Être la plus courte de
    deux caractères ne se remarque pas ; le rang seul n'est donc pas un critère.
  - **écart moyen** : bonne réponse moins moyenne des distracteurs, en caractères.
    Proche de zéro = la longueur ne dit rien.

Seuil retenu : au-delà de **15 % de questions détachées**, la banque est signalée.
Le hasard en produit environ 0 à 7 % dans les QCM anciens du dépôt.

Règle d'or n°198 : dans un QCM, la bonne réponse ne doit pas se reconnaître sans
lire la question. Un distracteur bâclé est une réponse offerte.

Les **billets d'entrée** au gabarit commun (règle d'or n°26, #530 : `<section id="billet">` dans une page de
séquence, deux ou trois questions, la liste `var BONNES` dans son script) sont mesurés de la même façon, sans « je ne
sais pas encore ». Un billet est court : une seule question détachée suffit à le signaler (28/10/2026). Les billets
plus anciens, écrits comme l'activité 0 de leur page avec leur propre moteur, ne sont pas lus ici.

Usage : python3 _outils/controle_longueurs.py [chemin]
"""

import html
import json
import os
import re
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

ECART_VISIBLE = 8      # caractères : en deçà, aucun élève ne fait la différence
SEUIL_ALERTE = 0.15    # part de questions détachées au-delà de laquelle on signale


def banques(racine):
    for dossier, _, fichiers in os.walk(racine):
        if "_archive" in dossier:
            continue
        for f in sorted(fichiers):
            if re.match(r"qcm.*\.html$", f, re.I):
                yield os.path.join(dossier, f)


def mesurer(chemin):
    with open(chemin, encoding="utf-8", errors="ignore") as fh:
        t = fh.read()
    m = re.search(r"const QUESTIONS\s*=\s*\[", t)
    if not m:
        return None
    seg = t[m.end():]
    detachees, ecarts, plus_longues = 0, [], 0
    for oraw, r in re.findall(r"o:\s*(\[[^\]]*\])\s*,\s*r:\s*(\d)", seg):
        try:
            o = json.loads(oraw)
        except ValueError:
            continue
        if len(o) != 4:
            continue
        r = int(r)
        L = [len(x) for x in o]
        bonne, autres = L[r], [x for i, x in enumerate(L) if i != r]
        ecarts.append(bonne - sum(autres) / 3)
        if bonne > max(autres) + ECART_VISIBLE or bonne < min(autres) - ECART_VISIBLE:
            detachees += 1
        if bonne == max(L):
            plus_longues += 1
    if not ecarts:
        return None
    return dict(fichier=os.path.basename(chemin), questions=len(ecarts),
                detachees=detachees, plus_longues=plus_longues,
                ecart=sum(ecarts) / len(ecarts))


INCONNU = "je ne sais pas encore"


def pages_a_billet(racine):
    for dossier, _, fichiers in os.walk(racine):
        if "_archive" in dossier or "node_modules" in dossier:
            continue
        for f in sorted(fichiers):
            if f.endswith(".html") and not re.match(r"qcm", f, re.I):
                yield os.path.join(dossier, f)


def mesurer_billet(chemin):
    """Questions détachées d'un billet d'entrée : [(rang, longueur de la juste, longueurs des autres)]."""
    with open(chemin, encoding="utf-8", errors="ignore") as fh:
        t = fh.read()
    if 'id="billet"' not in t:
        return None
    m = re.search(r"var BONNES = (\[.*?\]);", t)
    if not m:
        return None
    bonnes = json.loads(m.group(1))
    sortie = []
    for i, bonne in enumerate(bonnes, 1):
        g = re.search(r'<fieldset class="qcm-groupe" id="be_%d">(.*?)</fieldset>' % i, t, re.S)
        if not g:
            continue
        o = [html.unescape(re.sub(r"<[^>]+>", "", x)) for x in re.findall(r"<label[^>]*>(.*?)</label>", g.group(1), re.S)]
        o = [x for x in o if x != INCONNU]
        if bonne not in o:
            continue
        b = len(bonne)
        autres = [len(x) for x in o if x != bonne]
        if autres and (b > max(autres) + ECART_VISIBLE or b < min(autres) - ECART_VISIBLE):
            sortie.append((i, b, autres))
    return os.path.relpath(chemin), len(bonnes), sortie


def main(argv):
    racine = argv[1] if len(argv) > 1 else RACINE
    mesures = [m for m in (mesurer(p) for p in banques(racine)) if m]
    if not mesures:
        print("Aucune banque de questions trouvée sous %s" % racine)
        return 0

    print("%-56s %-5s %-13s %-9s %s" % ("QCM", "q", "détachées", "+longues", "écart moyen"))
    print("─" * 104)
    signales = []
    for m in sorted(mesures, key=lambda x: -x["detachees"] / x["questions"]):
        part = m["detachees"] / m["questions"]
        if part > SEUIL_ALERTE:
            signales.append(m)
        print("%-56s %-5d %-13s %-9d %+.1f" % (
            m["fichier"][:54], m["questions"],
            "%d (%.0f %%)" % (m["detachees"], 100 * part), m["plus_longues"], m["ecart"]))

    print()
    print("%d banques mesurées · seuil d'alerte : %.0f %% de questions détachées"
          % (len(mesures), 100 * SEUIL_ALERTE))

    billets = [b for b in (mesurer_billet(p) for p in pages_a_billet(racine)) if b]
    billets_signales = [b for b in billets if b[2]]
    print("%d billets d'entrée mesurés (%d questions) · seuil : aucune question détachée"
          % (len(billets), sum(b[1] for b in billets)))
    if billets_signales:
        print("\n⛔ %d billet(s) d'entrée où la longueur trahit la bonne réponse :" % len(billets_signales))
        for chemin, n, det in billets_signales:
            print("     %s" % chemin)
            for i, b, autres in det:
                print("        question %d : la juste fait %d caractères, les autres %s" % (i, b, autres))
    if signales or billets_signales:
        if signales:
            print("\n⛔ %d banque(s) où la longueur trahit la bonne réponse :" % len(signales))
        for m in signales:
            print("     %-52s %d/%d détachées, écart moyen %+.1f caractères"
                  % (m["fichier"][:50], m["detachees"], m["questions"], m["ecart"]))
        print("   Un élève qui coche la réponse la plus longue s'en tire sans lire la question.")
        return 1
    print("Aucune banque signalée.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
