#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verif_chaine.py — un TP engendré doit être ce que son scénario produit.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le manifeste de l'atelier déclare une chaîne de production : un générateur, des
scénarios, et une **empreinte** par scénario. Le 30 août 2026, on a mesuré :

  · **trois empreintes sur quatre étaient fausses** — les scénarios avaient été
    modifiés sans que personne les recalcule ;
  · **les trois pages avaient été modifiées à la main**, après coup, pour y
    poser un bandeau d'entrée. Régénérer aurait effacé le bandeau sans
    prévenir ;
  · deux pages étaient en retard d'une amélioration du générateur (un bloc de
    style ajouté depuis) : elles n'étaient plus ce que la chaîne produit.

Autrement dit, la chaîne existait sur le papier et plus dans les faits. Une
empreinte que personne ne vérifie n'est pas une empreinte, c'est une décoration
(règle d'or n°190, sur un autre objet).

CE QUE CE CONTRÔLE FAIT
-----------------------
Pour chaque scénario, il rejoue le générateur **dans un fichier temporaire** et
compare, octet par octet, avec la page présente sur le disque. Puis il recalcule
l'empreinte du scénario et la confronte à celle du manifeste.

Il ne répare rien : `--empreintes` recalcule et réécrit les empreintes du
manifeste, et c'est le seul geste d'écriture qu'il connaisse.

CE QU'IL NE FAIT PAS
--------------------
`_MODELE.json` n'est pas engendrable : son `retour_sequence` est un gabarit
(`../<niveau>/<code>/…`) et le générateur refuse — à juste titre. Le contrôle
l'écarte, le dit, et vérifie quand même son empreinte.

Usage : python3 verif_chaine.py [--empreintes]
Sortie : 0 si la chaîne dit vrai, 1 sinon.
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

A = pathlib.Path(__file__).resolve().parent
MANIFESTE = A / "manifest_cao.json"
GENERATEUR = A / "_generation" / "build_tp.py"


def empreinte(chemin):
    """L'empreinte d'un scénario : les seize premiers hexadécimaux de son SHA-256."""
    return hashlib.sha256(chemin.read_bytes()).hexdigest()[:16]


def engendrable(scenario):
    """Un scénario dont le retour de séquence est un gabarit ne s'engendre pas."""
    s = json.loads(scenario.read_text(encoding="utf-8"))
    return "<" not in str(s.get("retour_sequence", "")), s


def main(ecrire=False):
    manifeste = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    declarees = manifeste.get("empreintes", {})
    scenarios = sorted((A / "scenarios").glob("*.json"))
    ecarts, ecartes, calculees = [], [], {}

    for scenario in scenarios:
        nom = scenario.name
        calculees[nom] = empreinte(scenario)
        if nom not in declarees:
            ecarts.append("%s : absent du manifeste" % nom)
        elif declarees[nom] != calculees[nom]:
            ecarts.append("%s : empreinte déclarée %s, mesurée %s"
                          % (nom, declarees[nom], calculees[nom]))

        ok, s = engendrable(scenario)
        if not ok:
            ecartes.append(nom)
            continue
        page = A / s["fichier_sortie"]
        if not page.exists():
            ecarts.append("%s : la page %s n'existe pas" % (nom, s["fichier_sortie"]))
            continue
        with tempfile.TemporaryDirectory() as tmp:
            temoin = pathlib.Path(tmp) / s["fichier_sortie"]
            r = subprocess.run([sys.executable, str(GENERATEUR), str(scenario),
                                "--sortie=%s" % temoin], capture_output=True, text=True)
            if r.returncode != 0 or not temoin.exists():
                ecarts.append("%s : le générateur refuse — %s"
                              % (nom, (r.stdout + r.stderr).strip().splitlines()[:1]))
                continue
            if temoin.read_bytes() != page.read_bytes():
                ecarts.append("%s : la page sur le disque n'est PAS ce que le scénario "
                              "produit (%s)" % (nom, s["fichier_sortie"]))

    print("%d scénario(s) · %d engendré(s) et comparé(s) · %d écarté(s) : %s"
          % (len(scenarios), len(scenarios) - len(ecartes), len(ecartes),
             ", ".join(ecartes) or "aucun"))
    if ecartes:
        print("     (un scénario écarté porte un « retour_sequence » de gabarit : il ne "
              "s'engendre pas, et son empreinte est vérifiée quand même)")

    if ecrire:
        manifeste["empreintes"] = {n: calculees[n] for n in sorted(calculees)}
        MANIFESTE.write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")
        print("✍ empreintes recalculées dans %s" % MANIFESTE.name)
        return 0

    if ecarts:
        print("⛔ %d écart(s) — la chaîne de production ne décrit plus les fichiers :"
              % len(ecarts))
        for e in ecarts:
            print("     " + e)
        print("     `python3 verif_chaine.py --empreintes` recalcule les empreintes ; "
              "une page qui diffère se répare en régénérant, PAS en la modifiant.")
        return 1
    print("✅ chaque page est exactement ce que son scénario produit, et chaque "
          "empreinte dit vrai")
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--empreintes" in sys.argv))
