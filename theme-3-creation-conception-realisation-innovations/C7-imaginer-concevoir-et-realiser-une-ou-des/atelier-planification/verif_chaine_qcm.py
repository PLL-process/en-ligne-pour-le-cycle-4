#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verif_chaine_qcm.py — le QCM publié doit être ce que q.py et build_qcm.py produisent.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le 27/09/2026, `qcm_C7.1_planification_taches.html` s'est révélé en avance de
QUATRE campagnes menées directement sur le HTML publié, jamais reportées dans
`q.py` ni dans `_generation/build_qcm.py` :

  · 17 des 30 questions avaient des options reformulées à la main, jamais
    reportées dans `q.py` (source unique de la banque, règle d'or n°38) ;
  · la navigation (bandeau, paragraphe « Revenir », pied de page) ne reliait
    qu'à l'atelier de 5e, jamais aux ateliers de 4e et 3e ni aux trois
    séquences, alors que ce QCM sert les TROIS niveaux ;
  · une fonctionnalité « nuance » (et un champ `err` rendu optionnel) avait
    été ajoutée directement au HTML, absente du moteur que `build_qcm.py`
    recopie du gabarit ;
  · le CSS d'impression du gabarit avait gagné deux sélecteurs
    (`.loupe-cliquable`, `#qImgCap`) depuis la dernière régénération de cette
    page — un retard, pas une régression (même campagne du 02/09/2026 déjà
    rencontrée sur `atelier_*_C7.1_planification_taches.html`, voir
    `verif_chaine.py`).

Exactement le trou que `verif_chaine.py` referme pour `atelier-cao` depuis le
30 août 2026 et pour cet atelier même depuis le 27/09/2026 : une chaîne de
production qui existe sur le papier et plus dans les faits.

CE QUE CE CONTRÔLE FAIT
------------------------
Contrairement à `verif_chaine.py` (ce dossier), `build_qcm.py` accepte déjà un
gabarit et une sortie en arguments : il n'a pas besoin d'écrire aux emplacements
réels pour être rejoué. Ce contrôle profite de cette différence pour suivre le
principe de `atelier-cao/verif_chaine.py` : régénérer dans un dossier
TEMPORAIRE, comparer octet à octet, ne JAMAIS écrire sur la page réelle.

    1. rejoue `build_qcm.py <gabarit Shenzhen> <temp>` ;
    2. rejoue `node _outils/fix_r.js <temp> 617` (même graine que la page
       publiée) ;
    3. compare `<temp>` à `qcm_C7.1_planification_taches.html` octet à octet.

CE QUI DIFFÈRE DE `verif_chaine.py` (LE GÉNÉRATEUR DES ATELIERS)
------------------------------------------------------------------
Ce QCM emprunte son gabarit à un lot totalement différent (Thème 1, Shenzhen) :
si ce gabarit disparaît, change de forme, ou si le moteur qu'il transporte
change de version, ce contrôle le signale au lieu d'écrire une page fausse.

Usage : python3 verif_chaine_qcm.py
Sortie : 0 si la page publiée est exactement ce que q.py, build_qcm.py et
         fix_r.js produisent ensemble, 1 sinon (rien n'est réécrit sur le
         disque : contrairement à verif_chaine.py, une régénération QCM ne
         peut pas se faire en place sans passer par un fichier temporaire).
"""
import pathlib
import subprocess
import sys
import tempfile

A = pathlib.Path(__file__).resolve().parent
DEPOT = A.parent.parent.parent
GENERATEUR = A / "_generation" / "build_qcm.py"
FIX_R = DEPOT / "_outils" / "fix_r.js"
GABARIT = (DEPOT / "theme-1-objets-systemes-usages-interactions" /
           "C3-caracteriser-et-choisir-un-objet-ou-un" / "3e" / "3e_C3.1" /
           "qcm_3e_C3.1-C3.4_shenzhen.html")
PAGE = A / "qcm_C7.1_planification_taches.html"
GRAINE = "617"


def main():
    if not GABARIT.exists():
        print("⛔ le gabarit %s est introuvable — ce QCM en dépend, rien à vérifier."
              % GABARIT.relative_to(DEPOT))
        return 1
    if not PAGE.exists():
        print("⛔ %s est introuvable." % PAGE.name)
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        temoin = pathlib.Path(tmp) / "qcm_temoin.html"

        r = subprocess.run([sys.executable, str(GENERATEUR), str(GABARIT), str(temoin)],
                           capture_output=True, text=True, cwd=str(GENERATEUR.parent))
        if r.returncode != 0 or not temoin.exists():
            print("⛔ build_qcm.py refuse de tourner :\n%s" % (r.stdout + r.stderr).strip())
            return 1

        r = subprocess.run(["node", str(FIX_R), str(temoin), GRAINE],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("⛔ fix_r.js refuse de tourner :\n%s" % (r.stdout + r.stderr).strip())
            return 1

        identiques = temoin.read_bytes() == PAGE.read_bytes()

    if not identiques:
        print("⛔ %s n'est PAS ce que q.py + build_qcm.py + fix_r.js produisent."
              % PAGE.name)
        print("     Contrairement à verif_chaine.py, ceci ne s'auto-répare pas : "
              "régénérer pour de vrai (python3 _generation/build_qcm.py <gabarit> "
              "%s puis node _outils/fix_r.js %s %s depuis la racine du dépôt), "
              "PUIS relire le diff avant de committer." % (PAGE.name, PAGE.name, GRAINE))
        return 1

    print("✅ %s est exactement ce que q.py, build_qcm.py et fix_r.js (graine %s) "
          "produisent à partir du gabarit Shenzhen." % (PAGE.name, GRAINE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
