# -*- coding: utf-8 -*-
"""controle_banque_qcm.py — la ligne « Banque : … » d'un QCM dit ce que le QCM contient.

LE CONSTAT
----------
Chaque QCM ouvre son tableau de questions par un commentaire de bilan :
    /* Banque : 30 questions (10 4e_C8.1 + 10 4e_C8.2 + 10 4e_C8.3), 3 illustrees … */
Le 31/08/2026, en câblant les schémas de `4e_C4.7`, ce commentaire s'est révélé faux
dans les trois QCM du lot. Mesuré le 09/09 sur les 62 QCM qui en portent un :
**35 des 37 lignes courtes étaient fausses** — 22 d'entre elles répétaient mot pour
mot « 10 4e_C8.1 + 10 4e_C8.2 + 10 4e_C8.3, 3 illustrees » dans des QCM de 5e_C7.2,
3e_C8.2 ou 4e_C7.6 qui n'ont ni ces codes ni une seule image. Un gabarit copié,
jamais relu. Et 3 des 25 lignes longues disaient « Sainte-Luce 5e, seul code 5e_C1.2 »
en tête de QCM de 3e_C1.5, 4e_C1.4 et 5e_C1.3.

Un commentaire qui ment est pire qu'aucun : le prochain lecteur le croit.

CE QU'IL MESURE
---------------
Pour chaque QCM portant une ligne « Banque », il compte ce que le tableau QUESTIONS
contient vraiment — nombre de questions, répartition par champ `c`, nombre de `img:` —
et le compare à ce que la ligne annonce :

  · « N questions » : N doit être le nombre réel ;
  · « (k1 A + k2 B …) » ou « A : k1 · B : k2 » ou « seul code A » : chaque code
    annoncé doit exister avec cet effectif, et aucun code réel ne doit manquer.
    Un code s'écrit avec ou sans niveau (« 4e_C8.1 » ≡ « C8.1 ») ;
  · « i illustrée(s) » : i doit être le nombre réel de questions avec image.

Ce qu'il ne lit pas : une ligne qui n'annonce aucun chiffre n'est pas jugée ; un QCM
sans ligne « Banque » non plus (il n'en est pas obligé — il ne doit juste pas mentir).

Usage :
    python3 _outils/controle_banque_qcm.py           # rapport complet
    python3 _outils/controle_banque_qcm.py --muet    # seulement les refus
Sortie : 0 si chaque ligne « Banque » dit vrai, 1 sinon.
"""

import collections
import glob
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

BANQUE = re.compile(r"/\*\s*Banque\b(.*?)\*/", re.S)
CODE = r"(?:[345]e_)?(?:C\d\.\d|CRCN\s*[\d./]+|[A-Z]{2,4}|[345]e)"
#: des majuscules qui ne sont pas des codes de question
IGNORES = {"QCM", "DNB", "DOC", "SVG", "PNG", "HTML"}


def pages(racine):
    return sorted(f for f in glob.glob(os.path.join(racine, "**", "qcm*.html"), recursive=True)
                  if not any(e in f for e in ECARTES))


def norm(code):
    code = code.strip().rstrip(",;.")
    return re.sub(r"^[345]e_", "", code)


def est_code(c):
    return bool(re.match(r"(?:C\d\.\d|CRCN)", c))


def reel(texte):
    """(n, Counter des `c`, nb d'images) lus dans le tableau QUESTIONS."""
    deb = texte.find("QUESTIONS")
    if deb < 0:
        return None
    corps = texte[deb:]
    fin = corps.find("\n];")
    corps = corps[:fin] if fin > 0 else corps
    codes = re.findall(r'\{\s*c\s*:\s*"([^"]+)"', corps)
    images = len(re.findall(r"\bimg\s*:\s*\{", corps))
    return len(codes), collections.Counter(norm(c) for c in codes), images


def annonce(com):
    """Ce que la ligne promet : (n, Counter des codes ou None, images ou None)."""
    com = re.sub(r"\s+", " ", com)
    # ce qui est cité entre guillemets est un rappel (l'ancienne ligne, par exemple), pas une promesse
    com = re.sub(r"«[^»]*»", " ", com)
    m = re.search(r"(\d+)\s+questions", com)
    n = int(m.group(1)) if m else None
    m = re.search(r"(\d+)\s+illustr", com)
    images = int(m.group(1)) if m else None
    # les deux totaux sont lus ; on les retire pour ne pas les prendre pour des codes
    com = re.sub(r"\d+\s+questions?", " ", com)
    com = re.sub(r"\d+\s+illustr\w*", " ", com)
    codes = collections.Counter()
    seul = re.search(r"seul code\s+(" + CODE + ")", com)
    if seul:
        codes[norm(seul.group(1))] = n or 0
    else:
        for k, c in re.findall(r"(?<![\d.])(\d+)\s+(?:sur\s+)?(" + CODE + r")(?![\w.])", com):
            if c not in IGNORES:
                codes[norm(c)] += int(k)
        for c, k in re.findall(r"(?<![\w.])(" + CODE + r")\s*:\s*(\d+)(?![\d])", com):
            if c not in IGNORES:
                codes[norm(c)] += int(k)
    return n, (codes if codes else None), images


def juger(chemin):
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    m = BANQUE.search(texte)
    if not m:
        return None
    r = reel(texte)
    if r is None:
        return ["ligne « Banque » sans tableau QUESTIONS lisible"]
    n, codes, images = r
    an_n, an_codes, an_images = annonce(m.group(1))
    if an_n is None and an_codes is None and an_images is None:
        return None
    ecarts = []
    if an_n is not None and an_n != n:
        ecarts.append("annonce %d questions, en contient %d" % (an_n, n))
    if an_codes is not None:
        # un QCM range ses questions soit par CODE de compétence (C7.3), soit par
        # CATÉGORIE (ELA, SIM…). On compare ce qui est du même genre que le réel ; les
        # codes cités en marge d'un QCM à catégories sont une intention, pas un compte.
        genre = est_code(next(iter(codes), ""))
        an_codes = collections.Counter({c: k for c, k in an_codes.items() if est_code(c) == genre})
    if an_codes and an_codes != codes:
        ecarts.append("annonce %s, contient %s" % (
            " + ".join("%d %s" % (k, c) for c, k in an_codes.items()),
            " + ".join("%d %s" % (k, c) for c, k in codes.items())))
    if an_images is not None and an_images != images:
        ecarts.append("annonce %d illustrée(s), en contient %d" % (an_images, images))
    return ecarts


def main(muet=False):
    lus, ecarts = 0, []
    for f in pages(DEPOT):
        r = juger(f)
        if r is None:
            continue
        lus += 1
        if r:
            ecarts.append((os.path.relpath(f, DEPOT).replace(os.sep, "/"), r))
    if not muet:
        print("%d QCM portent une ligne « Banque » chiffrée · %d disent faux" % (lus, len(ecarts)))
        print("     NON LU : qu'une question soit bien de la compétence qu'elle déclare —\n"
              "     cela se lit, question par question.")
    if ecarts:
        print("\n⛔ %d ligne(s) « Banque » mentent sur le QCM qu'elles ouvrent :" % len(ecarts))
        for rel, es in ecarts:
            print("  %s" % rel)
            for e in es:
                print("     · %s" % e)
        return 1
    print("\n✅ chaque ligne « Banque » dit ce que son QCM contient")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
