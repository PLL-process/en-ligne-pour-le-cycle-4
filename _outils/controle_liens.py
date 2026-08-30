#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""controle_liens.py — un lien qui ne mène nulle part apprend à ne plus cliquer.

LE CONSTAT QUI A DONNÉ CET OUTIL
--------------------------------
Les quatre synthèses des lots `5e_C8.1` et `3e_C8.1`, livrées les 30 et 31 août
2026, portaient **seize liens cassés** — la totalité de leur barre de navigation.
Aucun ne menait nulle part : ni l'accueil, ni la séquence, ni le QCM, ni le
lexique.

La cause est bête et se reproduira : la barre a été recopiée depuis une page qui
vit **à la racine du dossier du lot**, alors que les synthèses vivent un cran
plus bas, dans `Synthèses/`. Toutes les adresses relatives étaient donc courtes
d'un niveau. À la lecture, rien ne se voit — un lien cassé ressemble exactement à
un lien juste.

Trente-neuf autres lots portaient les mêmes barres, justes. C'est ce qui rend le
défaut invisible : il n'apparaît qu'au moment où on déplace une page d'un
dossier, et le reste du dépôt continue de fonctionner.

CE QUE CE CONTRÔLE FAIT
-----------------------
Il ouvre chaque page du dépôt, relève chaque adresse **locale** qu'elle contient
(`href` et `src` en HTML, `[texte](adresse)` en Markdown), et vérifie que le
fichier visé existe réellement sur le disque, depuis le dossier de la page qui
le cite.

CE QU'IL NE FAIT PAS — ET IL LE DIT
-----------------------------------
Règle d'or n°242 : un instrument ne prouve une absence que là où il a regardé.
Règle d'or n°248 : un contrôle neuf qui trouve beaucoup de fautes a d'abord tort.
Cette première version en a trouvé 21 ; **cinq n'en étaient pas**, et elles
disent où un lecteur naïf se trompe :

  · une adresse **en commentaire** n'est pas un lien. Deux pages proposent au
    professeur d'insérer sa propre photo, dans un bloc `<!-- … -->` prêt à
    décommenter. Le navigateur ne la charge pas ; le contrôle ne doit pas la
    réclamer.
  · une adresse **fabriquée à l'exécution** n'est pas un chemin. `src="${q.img}"`
    à l'intérieur d'un script n'existe qu'une fois la page vivante.

Le contrôle laisse donc de côté : les commentaires, le contenu des balises
`<script>` et `<style>`, les blocs de code Markdown, et toute adresse qui porte
une marque de gabarit (`${…}`, `{{…}}`). Il laisse aussi de côté :

  · les **ancres** (`#partie-2`) : il vérifie le fichier, pas l'identifiant à
    l'intérieur ;
  · les **adresses distantes** : un lien vers `https://…` n'est pas de son
    ressort, et le dépôt doit rester lisible hors ligne de toute façon ;
  · `_archive-anciennes-versions/` (des versions gelées, dont les liens pointent
    volontairement vers un état passé) et les gabarits de `_outils/` (dont les
    adresses sont des marques à remplacer).

Tout cela est **compté et affiché** à chaque exécution : un contrôle qui écarte
des fichiers sans le dire ment sur son périmètre.

Usage : python3 _outils/controle_liens.py [--tout]
        --tout : n'écarte plus rien, et montre aussi l'archive et les gabarits.
Sortie : 0 si aucun lien cassé dans le périmètre, 1 sinon.
"""
import os
import pathlib
import re
import sys

DEPOT = pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent

#: ce qu'on ne regarde pas, et pourquoi — affiché à chaque exécution
ECARTES = [
    ("_archive-anciennes-versions/", "versions gelées : leurs liens décrivent un état passé"),
    ("_outils/dnb_gabarit.html", "gabarit : ses adresses sont des marques à remplacer"),
]

DISTANT = re.compile(r"^(https?:|mailto:|tel:|data:|javascript:|//)", re.I)
HTML = re.compile(r'(?:href|src)\s*=\s*"([^"]*)"', re.I)
MARKDOWN = re.compile(r"\[[^\]]*\]\(([^)\s]+)")
GABARIT = re.compile(r"\$\{|\{\{|%\(|<%")

#: ce qu'on retire du texte AVANT d'y chercher des adresses
MUETS = [
    (re.compile(r"<!--.*?-->", re.S), "commentaires HTML"),
    (re.compile(r"<(script|style)\b.*?</\1\s*>", re.S | re.I), "balises <script> et <style>"),
]
MUETS_MD = [
    (re.compile(r"^```.*?^```", re.S | re.M), "blocs de code Markdown"),
    (re.compile(r"`[^`\n]*`"), "code en ligne Markdown"),
]


def taire(texte, suffixe):
    """Le texte débarrassé de ce qu'un navigateur ne suit pas.

    Renvoie (texte, nombre de zones tues). Les zones sont remplacées par un
    espace plutôt que supprimées : on ne recolle pas deux morceaux qui ne se
    touchaient pas.
    """
    tues = 0
    for motif, _quoi in (MUETS_MD if suffixe == ".md" else MUETS):
        texte, n = motif.subn(" ", texte)
        tues += n
    return texte, tues


def adresses(texte, suffixe):
    """Les adresses citées par une page, dans l'ordre où elles s'y trouvent."""
    motif = MARKDOWN if suffixe == ".md" else HTML
    return [m.group(1) for m in motif.finditer(texte)]


def locale(adresse):
    """Cette adresse désigne-t-elle un fichier du dépôt, ici et maintenant ?"""
    a = adresse.strip()
    return (bool(a) and not a.startswith("#") and not DISTANT.match(a)
            and not GABARIT.search(a))


def cible(page, adresse):
    """Le chemin visé, ancre et paramètres retirés — tel qu'un navigateur le lit."""
    chemin = adresse.split("#")[0].split("?")[0]
    if not chemin:
        return None
    from urllib.parse import unquote
    return (page.parent / unquote(chemin)).resolve()


def ecarte(relatif):
    for prefixe, _pourquoi in ECARTES:
        if relatif.startswith(prefixe):
            return True
    return False


def parcourir(racine=DEPOT, tout=False):
    """(liens vérifiés, liens cassés, pages écartées, zones tues)."""
    verifies, casses, pages_ecartees, tues = 0, [], 0, 0
    for page in sorted(racine.rglob("*")):
        if page.is_dir() or page.suffix.lower() not in (".html", ".md"):
            continue
        relatif = str(page.relative_to(racine)).replace(os.sep, "/")
        if ".git/" in relatif or relatif.startswith(".git"):
            continue
        if not tout and ecarte(relatif):
            pages_ecartees += 1
            continue
        try:
            texte = page.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        suffixe = page.suffix.lower()
        texte, n = taire(texte, suffixe)
        tues += n
        for a in adresses(texte, suffixe):
            if not locale(a):
                continue
            verifies += 1
            c = cible(page, a)
            if c is None or not c.exists():
                casses.append((relatif, a))
    return verifies, casses, pages_ecartees, tues


def main(tout=False):
    verifies, casses, pages_ecartees, tues = parcourir(tout=tout)
    print("%d adresses locales vérifiées · %d cassée(s)" % (verifies, len(casses)))
    print("%d zone(s) tue(s) avant lecture : %s — un navigateur ne les suit pas."
          % (tues, ", ".join(quoi for _m, quoi in MUETS + MUETS_MD)))
    if not tout:
        print("%d page(s) volontairement hors périmètre :" % pages_ecartees)
        for prefixe, pourquoi in ECARTES:
            print("     %-38s %s" % (prefixe, pourquoi))
        print("     (les ancres `#…` ne sont pas suivies, aucune adresse distante n'est "
              "testée, et une adresse de gabarit `${…}` n'est pas un chemin)")
    if not casses:
        print("✅ aucun lien mort dans le périmètre regardé")
        return 0
    par_page = {}
    for page, a in casses:
        par_page.setdefault(page, []).append(a)
    print("⛔ %d lien(s) mort(s) dans %d page(s) :" % (len(casses), len(par_page)))
    for page in sorted(par_page):
        print("   %s" % page)
        for a in par_page[page]:
            print("       → %s" % a)
    return 1


if __name__ == "__main__":
    raise SystemExit(main("--tout" in sys.argv))
