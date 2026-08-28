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

Usage : python3 _outils/controle_longueurs.py [chemin]
"""

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
