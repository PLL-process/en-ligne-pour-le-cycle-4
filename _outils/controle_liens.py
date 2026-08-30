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
une marque de gabarit (`${…}`, `{{…}}`).

LES ANCRES — l'angle mort de la première version
------------------------------------------------
Elle vérifiait le fichier et s'arrêtait là : `page.html#partie-2` était déclaré
juste tant que `page.html` existait. Or un lien d'ancre morte ne mène pas
« ailleurs », il mène **en haut de la bonne page** — le lecteur croit avoir mal
cliqué et recommence. Le dépôt en compte 48, tous justes à ce jour ; c'est
précisément le moment d'installer le contrôle, pendant qu'il ne dénonce
personne.

Un identifiant est cherché dans le fichier visé **tel qu'il est écrit sur le
disque**, `id="…"` ou `name="…"`. Deux réserves, tenues du côté indulgent :
`#top` est toujours accepté (le navigateur remonte, sans identifiant), et un
identifiant **posé par un script à l'exécution** n'est pas visible ici — le
contrôle ne le réclame que s'il ne le trouve nulle part dans la source. Enfin,
une ancre visant un fichier Markdown n'est pas vérifiée : l'identifiant y est
fabriqué par le rendu, pas écrit dans le texte.

Il laisse aussi de côté :

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


#: `#top` remonte en haut de page sans qu'aucun identifiant existe
ANCRES_TOUJOURS_VALIDES = {"top"}

IDENTIFIANT = r'\b(?:id|name)\s*=\s*["\']%s["\']'


def identifiant_present(chemin, ancre, _cache={}):
    """Le fichier visé porte-t-il cet identifiant, écrit dans sa source ?

    On lit le fichier BRUT, sans rien taire : un identifiant reste un
    identifiant où qu'il se trouve, et mieux vaut se taire à tort que dénoncer
    à tort (règle d'or n°248).
    """
    if ancre in ANCRES_TOUJOURS_VALIDES:
        return True
    cle = str(chemin)
    if cle not in _cache:
        try:
            _cache[cle] = chemin.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            _cache[cle] = ""
    return re.search(IDENTIFIANT % re.escape(ancre), _cache[cle]) is not None


def parcourir(racine=DEPOT, tout=False):
    """Relevé complet : liens, ancres, ce qui a été tu et ce qui a été écarté."""
    releve = dict(verifies=0, casses=[], pages_ecartees=0, tues=0,
                  ancres_verifiees=0, ancres_mortes=[], ancres_non_verifiables=0)
    for page in sorted(racine.rglob("*")):
        if page.is_dir() or page.suffix.lower() not in (".html", ".md"):
            continue
        relatif = str(page.relative_to(racine)).replace(os.sep, "/")
        if ".git/" in relatif or relatif.startswith(".git"):
            continue
        if not tout and ecarte(relatif):
            releve["pages_ecartees"] += 1
            continue
        try:
            texte = page.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        suffixe = page.suffix.lower()
        texte, n = taire(texte, suffixe)
        releve["tues"] += n
        for a in adresses(texte, suffixe):
            ancre = a.split("#", 1)[1] if "#" in a else ""
            if locale(a):
                releve["verifies"] += 1
                c = cible(page, a)
                if c is None or not c.exists():
                    releve["casses"].append((relatif, a))
                    continue
                visee = c
            elif a.strip().startswith("#") and not GABARIT.search(a):
                visee = page          # une ancre dans la page elle-même
            else:
                continue
            if not ancre:
                continue
            if visee.suffix.lower() not in (".html", ".htm"):
                releve["ancres_non_verifiables"] += 1
                continue
            releve["ancres_verifiees"] += 1
            if not identifiant_present(visee, ancre):
                releve["ancres_mortes"].append((relatif, a))
    return releve


def _lister(titre, defauts):
    par_page = {}
    for page, a in defauts:
        par_page.setdefault(page, []).append(a)
    print("⛔ %s — %d dans %d page(s) :" % (titre, len(defauts), len(par_page)))
    for page in sorted(par_page):
        print("   %s" % page)
        for a in par_page[page]:
            print("       → %s" % a)


def main(tout=False):
    r = parcourir(tout=tout)
    print("%d adresses locales vérifiées · %d cassée(s)" % (r["verifies"], len(r["casses"])))
    print("%d ancre(s) vérifiée(s) · %d introuvable(s) · %d non vérifiable(s) (cible non HTML)"
          % (r["ancres_verifiees"], len(r["ancres_mortes"]), r["ancres_non_verifiables"]))
    print("%d zone(s) tue(s) avant lecture : %s — un navigateur ne les suit pas."
          % (r["tues"], ", ".join(quoi for _m, quoi in MUETS + MUETS_MD)))
    if not tout:
        print("%d page(s) volontairement hors périmètre :" % r["pages_ecartees"])
        for prefixe, pourquoi in ECARTES:
            print("     %-38s %s" % (prefixe, pourquoi))
        print("     (aucune adresse distante n'est testée, une adresse de gabarit `${…}` "
              "n'est pas un chemin, et un identifiant posé par un script à l'exécution "
              "n'est pas visible ici)")
    if not r["casses"] and not r["ancres_mortes"]:
        print("✅ aucun lien mort, aucune ancre introuvable dans le périmètre regardé")
        return 0
    if r["casses"]:
        _lister("lien(s) mort(s)", r["casses"])
    if r["ancres_mortes"]:
        _lister("ancre(s) introuvable(s) — la page existe, la section non", r["ancres_mortes"])
    return 1


if __name__ == "__main__":
    raise SystemExit(main("--tout" in sys.argv))
