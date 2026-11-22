# -*- coding: utf-8 -*-
"""controle_date_locale.py — la date du jour est celle du poste (règle d'or n°365).

LE CONSTAT
----------
Le bilan du TP « Algorigrammes de domotique » (4e_C6.2) prenait la date du jour par
`new Date().toISOString().slice(0, 10)`. `toISOString()` rend l'heure UNIVERSELLE : en Martinique (UTC−4), à partir
de 20 h, elle est déjà au lendemain. Un élève qui finissait son TP à la maison après le dîner imprimait un bilan daté
du jour suivant, et son code de validation, calculé sur cette date, ne correspondait plus à celle que l'enseignant
saisissait (audit en 12 axes du 20/11/2026, corrigé par la PR #841). Le même geste, recopié d'une page à l'autre,
fausse toute trace datée : bilan, fiche Pronote, nom de fichier téléchargé.

LA RÈGLE
--------
La date du jour se construit avec l'heure du poste (`getFullYear()`, `getMonth() + 1`, `getDate()`), et s'affiche à
l'élève au format jj/mm/aaaa. Un horodatage complet (`toISOString()` gardé tel quel, avec son heure et son « Z ») reste
permis : il ne prétend pas dire « aujourd'hui ».

CE QU'IL CHERCHE
----------------
Dans les .html et .js du site (hors `_archive-anciennes-versions`, `_outils`, `node_modules`), une date du jour tirée
de l'heure universelle : `toISOString()` ou `toJSON()` suivi de `.slice(0, 10)`, `.substring(0, 10)`,
`.substr(0, 10)` ou `.split('T')[0]`.

RÉFÉRENCE (règle n°273)
-----------------------
Aucune page connue au 21/11/2026 (`main` à d7dc83c, après la PR #841). La liste REFERENCE est vide ; elle ne peut que
le rester ou rétrécir.

Sortie : 0 aucune date UTC prise pour la date du jour · 1 au moins une · 2 EN PANNE (aucun fichier lu, n°299).
Usage : python3 _outils/controle_date_locale.py [chemins…] [--muet]
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "_exports"}
MOTIF = re.compile(
    r"\.to(?:ISOString|JSON)\(\)\s*\.\s*(?:slice\(\s*0\s*,\s*10\s*\)|substr(?:ing)?\(\s*0\s*,\s*10\s*\)"
    r"|split\(\s*['\"]T['\"]\s*\)\s*\[\s*0\s*\])"
)
#: fichier → motif daté. Vide au 21/11/2026 ; ne peut que rester vide ou rétrécir (n°273).
REFERENCE = {}


def fichiers(departs):
    for depart in departs:
        if os.path.isfile(depart):
            yield depart
            continue
        for dossier, sous, noms in os.walk(depart):
            sous[:] = sorted(d for d in sous if d not in IGNORES and not d.startswith("."))
            for nom in sorted(noms):
                if nom.endswith((".html", ".js")):
                    yield os.path.join(dossier, nom)


def main(argv):
    muet = "--muet" in argv
    departs = [a for a in argv if not a.startswith("--")] or [RACINE]
    lus, trouves = 0, []
    for chemin in fichiers(departs):
        try:
            texte = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        lus += 1
        rel = os.path.relpath(chemin, RACINE)
        for m in MOTIF.finditer(texte):
            ligne = texte.count("\n", 0, m.start()) + 1
            trouves.append((rel, ligne, m.group(0)))
    if not lus:
        print("⛔ EN PANNE : aucun fichier lu (n°299).")
        return 2
    nouveaux = [t for t in trouves if t[0] not in REFERENCE]
    if not muet:
        for rel, ligne, quoi in trouves:
            marque = "✘" if rel not in REFERENCE else "·"
            print(f"{marque} {rel}:{ligne} — date du jour prise en heure universelle : {quoi}")
        for rel in sorted(set(REFERENCE) - {t[0] for t in trouves}):
            print(f"ℹ {rel} — n'a plus de date UTC : à retirer de REFERENCE (n°273)")
    print(f"{lus} fichier(s) lus · {len(trouves)} date(s) du jour prise(s) en heure universelle · {len(nouveaux)} hors référence")
    if nouveaux:
        print("✘ la date du jour se construit avec l'heure du poste (getFullYear, getMonth + 1, getDate) — règle d'or n°365")
        return 1
    print("✅ chaque date du jour est celle du poste")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
