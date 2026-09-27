#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verif_chaine.py — une page engendrée doit être ce que le générateur produit.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le 27/09/2026, les trois pages de cet atelier (5e, 4e, 3e) se sont révélées
en avance de QUATRE campagnes menées directement sur le HTML publié, jamais
reportées dans `_generation/build_atelier.py` :

  · le CSS d'impression du 02/09/2026 (fond blanc, couleurs conservées) ;
  · la règle d'or n°92, l'agrandisseur d'images (loupe) ;
  · la règle d'or n°303, un lien qui se lit, à l'écran comme sur le papier ;
  · la section « Les traces à garder » (liens vers les synthèses).

Régénérer effaçait les quatre en silence — 564 lignes de contenu perdues par
parcours. Exactement le trou que `verif_chaine.py` referme pour
`atelier-cao` depuis le 30 août 2026 : une chaîne de production qui existe
sur le papier et plus dans les faits.

CE QUE CE CONTRÔLE FAIT
------------------------
Il mesure l'empreinte des trois pages, relance `_generation/build_atelier.py`
pour de vrai, puis mesure à nouveau. Une empreinte qui change dit qu'au moins
une page, avant ce contrôle, N'ÉTAIT PAS ce que `_corrige_calcule.json` et le
générateur produisent.

CE QUI DIFFÈRE DE `atelier-cao/verif_chaine.py`
------------------------------------------------
Cet atelier n'a ni scénario par page ni option `--sortie=` : un seul jeu de
données partagé produit les trois parcours en une seule exécution, aux trois
emplacements réels — il n'y a pas d'autre mode. Le contrôle ne peut donc pas
comparer sans écrire ; mais régénérer EST la réparation (même principe que
pour la CAO : « une page qui diffère se répare en régénérant, PAS en la
modifiant »), donc un écart détecté ici est déjà corrigé sur le disque quand
ce script le signale — il ne reste qu'à relire le diff et committer.

Usage : python3 verif_chaine.py
Sortie : 0 si les trois pages étaient déjà exactement ce que le générateur
         produit, 1 si au moins une différait (elle est alors déjà réécrite).
"""
import hashlib
import pathlib
import subprocess
import sys

A = pathlib.Path(__file__).resolve().parent
GENERATEUR = A / "_generation" / "build_atelier.py"
DONNEES = A / "_corrige_calcule.json"
NIVEAUX = ("5e", "4e", "3e")


def empreinte(chemin):
    """Les seize premiers hexadécimaux du SHA-256, ou None si le fichier manque."""
    return hashlib.sha256(chemin.read_bytes()).hexdigest()[:16] if chemin.exists() else None


def main():
    if not DONNEES.exists():
        print("⛔ %s est introuvable — rien à vérifier." % DONNEES.name)
        return 1

    pages = {n: A / ("atelier_%s_C7.1_planification_taches.html" % n) for n in NIVEAUX}
    avant = {n: empreinte(p) for n, p in pages.items()}

    r = subprocess.run([sys.executable, str(GENERATEUR)],
                       capture_output=True, text=True, cwd=str(GENERATEUR.parent))
    if r.returncode != 0:
        print("⛔ le générateur a refusé de tourner :\n%s" % (r.stdout + r.stderr).strip())
        return 1

    apres = {n: empreinte(p) for n, p in pages.items()}
    ecarts = [n for n in NIVEAUX if avant[n] != apres[n]]

    print("%d parcours régénéré(s) et comparé(s) par empreinte · %d écart(s) : %s"
          % (len(NIVEAUX), len(ecarts), ", ".join(ecarts) or "aucun"))

    if ecarts:
        print("⛔ %d parcours ne correspondaient PAS à ce que le générateur "
              "produit à partir de %s." % (len(ecarts), DONNEES.name))
        print("     La régénération qui vient d'avoir lieu les a DÉJÀ réécrits "
              "sur le disque : relire le diff (`git diff -- %s`), pas le "
              "modifier à la main, puis committer." % pages[ecarts[0]].name)
        return 1

    print("✅ chaque page est exactement ce que %s et le générateur produisent"
          % DONNEES.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
