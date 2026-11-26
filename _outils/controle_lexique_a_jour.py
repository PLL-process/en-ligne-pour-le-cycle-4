# -*- coding: utf-8 -*-
"""Chaque lexique engendré est celui que son générateur écrit aujourd'hui.

    python3 _outils/controle_lexique_a_jour.py [racine]

LE CONSTAT (25/11/2026)
-----------------------
Un lexique est tiré mot pour mot des QCM de son lot (`generer_lexique.py`). Le 25/11/2026, la vérification totale a
renommé une notion dans `qcm_5e_C7.4` (question 16) : le lexique du lot est resté sur l'ancien nom, et aucun des
53 contrôles ne le disait — aucun ne rejouait le générateur. L'élève lisait dans le lexique un mot que le QCM
n'employait plus.

CE QU'IL FAIT
-------------
Il lance `generer_lexique.py --verifier` sur chaque dossier du dépôt qui porte un `lexique_*.html` (y compris les lots
sans séquence propre, autour d'un TP mutualisé, que `--tous` ne parcourt pas) : chaque lexique est engendré en mémoire
et comparé, octet pour octet, à la page du dépôt. Rien n'est écrit. Un lexique écrit à la main (`EXCLUS`, dans le
générateur) n'est pas comparé : il est compté.

Sortie : 0 tous à jour · 1 au moins un lexique périmé ou refusé (relancer `generer_lexique.py <dossier du lot>`) ·
2 aucun lexique comparé (règle d'or n°299).
"""
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation", "_outils"}


def main(argv):
    racine = os.path.abspath(argv[0]) if argv else os.path.dirname(ICI)
    lots = set()
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [x for x in sous if x not in EXCLUS and not x.startswith(".")]
        if os.path.relpath(dossier, racine).startswith("theme-") and any(f.startswith("lexique_") and f.endswith(".html") for f in fichiers):
            lots.add(dossier)
    if not lots:
        print("⛔ aucun lexique sous %s : rien n'a été vérifié (règle d'or n°299)" % racine)
        return 2
    r = subprocess.run([sys.executable, os.path.join(ICI, "generer_lexique.py"), "--verifier"] + sorted(lots),
                       capture_output=True, text=True)
    ecrits_main = sum(1 for ligne in r.stdout.splitlines() if "EXCLU —" in ligne)
    for ligne in r.stdout.splitlines():
        if "PÉRIMÉ" in ligne or "REFUSÉ" in ligne or "NON GÉNÉRÉ" in ligne or ligne.startswith(("✅", "⛔")) or "comparé(s)" in ligne or "refusé(s)" in ligne:
            print(ligne)
    print("%d dossier(s) à lexique lus · %d lexique(s) écrit(s) à la main, non comparé(s)" % (len(lots), ecrits_main))
    if r.returncode not in (0, 1, 2):
        print(r.stderr.strip()[-600:])
        print("⛔ le générateur s'est arrêté (sortie %d) : rien n'a été vérifié" % r.returncode)
        return 2
    return r.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
