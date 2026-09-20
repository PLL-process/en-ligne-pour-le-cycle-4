# -*- coding: utf-8 -*-
"""controle_gestes_outil.py — l'encart « les quatre gestes » nomme l'outil de SA page,
et se place à la porte de l'outil.

LE CONSTAT
----------
Le 08/09/2026, Pascal lit dans `4e_C1.1` : « Ouvre l'éditeur (Arduino ou mBlock) et
crée un nouveau programme. » — dans une séquence qui ne programme rien et ouvre un
CSV dans un tableur. L'encart (règle d'or n°93, les gestes d'outil réenseignés à
chaque niveau) avait été posé le 11/08 par un choix par mots-clés qui lisait aussi
le CODE de la page : le mot « arduino » n'y figurait que dans le vérificateur
JavaScript d'une activité. Mesuré sur les 22 encarts du dépôt : un seul faux.

Le 13/09/2026, seconde mesure : les 22 encarts étaient tous EN TÊTE de page, avant la
situation. Le premier contact de l'élève avec sa séquence était un tutoriel de
logiciel, avant même de savoir quel problème il allait traiter. Règle d'or n°297
complétée ce jour : l'échauffement se place immédiatement avant la première activité
qui ouvre l'outil — on ne s'échauffe pas une heure avant l'effort.

CE QU'IL MESURE
---------------
1. L'OUTIL. Pour chaque page qui porte `<section class="card gestes-outil">`, l'outil
   nommé dans son titre (« les quatre gestes de/du X ») doit apparaître dans le TEXTE
   VISIBLE de la page HORS de l'encart — ni dans un <script>, ni dans un <style>, ni
   dans une balise. Sinon la page est refusée : elle enseigne les gestes d'un outil
   qu'elle n'emploie pas. Les outils connus et les mots qui les trahissent sont dans
   OUTILS. Un outil inconnu est refusé aussi : il faut l'ajouter ici, avec ses mots.

2. LA POSITION. Une activité est un titre <h2> ou <h3> qui porte « Activité n » ou
   « Séance n » (dans le titre, ou dans le cartouche <span class="num"> qui le
   précède) ; son bloc va jusqu'au prochain titre de même niveau ou plus haut. L'encart
   est refusé
     - s'il précède le <h2> de la situation ou de la problématique ;
     - s'il n'est pas COLLÉ à une activité dont le bloc nomme l'outil : entre la fin
       de l'encart et le titre de l'activité suivante, rien de visible sauf le
       cartouche « Activité n » (les balises d'onglet et de carte ne comptent pas).
   Pour Vittascience (OUVRE), nommer ne suffit pas : l'activité doit porter un lien ou un
   cadre vers fr.vittascience.com — cinq pages citent le mot et n'ouvrent que leur
   simulateur intégré.

3. L'OUVERTURE (durci le 13/09/2026, vague 2 étape 1). Si AUCUNE activité de la page
   n'ouvre l'outil, l'encart est REFUSÉ : il enseigne les gestes d'un outil que l'élève
   n'ouvre jamais depuis cette page (règle d'or n°297 : un geste d'outil s'enseigne
   pour être refait seul depuis la page, à la porte de l'outil — pas de porte, pas
   d'encart). Jusqu'à cette date, ces pages étaient seulement signalées : neuf encarts,
   les six du thème 2 retirés le 13/09 (#390), les trois Onshape du thème 3 le 14/09
   (#391) — ces trois-là TOLÉRÉS nommément (TOLERES) le temps de leur PR, puisque la
   garde de périmètre interdit à une branche du thème 3 de toucher `_outils/`. TOLERES
   est vide depuis. Une tolérance devenue sans objet — la page n'a plus d'encart — est
   affichée comme périmée, à retirer.

   NON LU : que l'activité collée soit bien la PREMIÈRE qui OUVRE l'outil. Le script
   distingue une mention d'une ouverture aussi mal qu'un moteur de recherche : dans
   `3e_C4.8`, l'activité 1 montre une capture « construite dans Packet Tracer » et
   l'activité 3 l'ouvre. C'est la mesure à la main, page par page, qui tranche
   (journal du 13/09) ; le script vérifie seulement que l'encart est collé à une
   activité qui parle de l'outil, et après la situation.

Usage :
    python3 _outils/controle_gestes_outil.py           # rapport complet
    python3 _outils/controle_gestes_outil.py --muet    # seulement les refus
Sortie : 0 si chaque encart parle de l'outil de sa page et se tient à sa porte, 1 sinon.
"""

import glob
import html
import os
import re
import sys

import panne

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

ENCART = re.compile(r'<section class="card gestes-outil".*?</section>', re.S)
TITRE = re.compile(r"quatre gestes (?:de |du |d')\s*([^<]+)<", re.I)
TITRES = re.compile(r"<h([23])[^>]*>(.*?)</h\1>", re.S)
SITUATION = re.compile(r"situation|probl[ée]matique", re.I)
NUMERO = re.compile(r"(?:Activit[ée]|S[ée]ance)\s*\d", re.I)

#: l'outil tel que l'encart le nomme → ce que la page doit dire ailleurs
OUTILS = {
    "arduino": r"arduino|mblock|t[ée]l[ée]vers",
    "onshape": r"onshape",
    "packet tracer": r"packet\s*tracer",
    "tableur": r"tableur|libreoffice|\bcalc\b|classeur",
    "vittascience": r"vittascience",   # mention ; l'OUVERTURE, elle, exige un lien (OUVRE)
    "mblock": r"mblock",
    "thonny": r"thonny",
    "freecad": r"freecad",
}


#: pour ces outils, une activité n'« ouvre » pas l'outil en le nommant : il lui faut un lien
#: ou un cadre vers le site. Mesuré le 12/09 : cinq encarts Vittascience sur des pages dont le
#: simulateur est dans la page, et qui ne citent le mot que dans « Choix de l'outil ».
OUVRE = {"vittascience": r'(?:href|src)="https?://fr\.vittascience\.com'}

#: encarts d'un outil que la page n'ouvre pas, tolérés NOMMÉMENT et pour une raison écrite.
#: Vide depuis le 14/09/2026 : les trois encarts Onshape du thème 3, tolérés le temps de leur
#: retrait (#391), ont disparu, et leurs entrées s'affichaient « périmées ». Le mécanisme reste :
#: une prochaine tolérance s'écrit ici, avec sa raison, et s'annonce périmée dès qu'elle ne sert plus.
TOLERES = {}


def pages(racine):
    return sorted(f for f in glob.glob(os.path.join(racine, "**", "*.html"), recursive=True)
                  if not any(e in f for e in ECARTES))


def _texte_visible(fragment):
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<(script|style)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    return html.unescape(re.sub(r"<[^>]+>", " ", fragment))


def _activites(texte, encart):
    """Les titres h2/h3 hors encart : (début, fin, texte, niveau, est_une_activité)."""
    out = []
    for h in TITRES.finditer(texte):
        if encart.start() <= h.start() < encart.end():
            continue
        titre = _texte_visible(h.group(2)).strip()
        cartouche = _texte_visible(texte[max(0, h.start() - 300):h.start()])
        est_act = bool(NUMERO.search(titre)) or bool(re.search(r"(?:Activit[ée]|S[ée]ance)\s*\d\s*$", cartouche.strip()))
        out.append((h.start(), h.end(), titre, int(h.group(1)), est_act))
    return out


def position(texte, encart, outil, motif):
    """None si aucune activité n'ouvre l'outil ; sinon (True, activité collée) ou (False, raison)."""
    titres = _activites(texte, encart)
    ouvre = OUVRE.get(outil, motif)
    nomme = []
    for i, (deb, fin, titre, niveau, est_act) in enumerate(titres):
        if not est_act:
            continue
        # le bloc va jusqu'au prochain titre de même niveau ou plus haut (un <h3> ne clôt pas un <h2>)
        borne = next((t[0] for t in titres[i + 1:] if t[3] <= niveau), len(texte))
        bloc = texte[deb:borne]
        if encart.start() >= deb and encart.start() < borne:
            bloc = bloc.replace(encart.group(0), "")
        if re.search(ouvre, bloc if outil in OUVRE else _texte_visible(bloc), re.I):
            nomme.append((deb, titre))
    if not nomme:
        return None
    sit = next(((deb, titre) for deb, fin, titre, niveau, est_act in titres if not est_act and SITUATION.search(titre)), None)
    if sit and encart.start() < sit[0]:
        return False, "précède la situation « %s »" % sit[1][:60]
    suivant = next(((deb, titre) for deb, fin, titre, niveau, est_act in titres if deb >= encart.end() and est_act), None)
    if suivant is None:
        return False, "aucune activité ne le suit"
    entre = _texte_visible(texte[encart.end():suivant[0]]).strip()
    if not re.fullmatch(r"(?:(?:Activit[ée]|S[ée]ance)\s*\d+)?", entre):
        return False, "n'est pas collé à l'activité « %s » : « %s » s'intercale" % (suivant[1][:50], entre[:60])
    if suivant[0] not in {deb for deb, _ in nomme}:
        return False, "collé à « %s », qui n'ouvre pas l'outil" % suivant[1][:60]
    return True, suivant[1]


def juger(chemin):
    """None si la page n'a pas d'encart ; sinon (outil, nb d'occurrences, motif, position)."""
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    m = ENCART.search(texte)
    if not m:
        return None
    t = TITRE.search(m.group(0))
    outil = t.group(1).strip().lower() if t else ""
    reste = _texte_visible(texte[:m.start()] + texte[m.end():])
    motif = OUTILS.get(outil)
    if motif is None:
        return outil or "(sans titre)", -1, None, None
    return outil, len(re.findall(motif, reste, re.I)), motif, position(texte, m, outil, motif)


def main(muet=False, toleres=None):
    toleres = TOLERES if toleres is None else toleres
    # Règle d'or n°299 : ce qui doit être non nul, c'est le nombre de pages
    # OUVERTES. Zéro encart « les quatre gestes » est un résultat possible et
    # légitime ; zéro page lue est une panne.
    lues = pages(DEPOT)
    if not lues:
        return panne.rien_vu("aucune page .html sous %s" % DEPOT)

    vus, ecarts, signales, avec_encart = 0, [], [], set()
    for f in lues:
        r = juger(f)
        if r is None:
            continue
        vus += 1
        outil, n, motif, pos = r
        rel = os.path.relpath(f, DEPOT).replace(os.sep, "/")
        avec_encart.add(rel)
        if n < 0:
            ecarts.append((rel, "outil « %s » inconnu de OUTILS : ajoute-le avec ses mots" % outil))
        elif n == 0:
            ecarts.append((rel, "l'encart enseigne « %s », et la page ne l'emploie nulle part "
                                "(aucun mot du motif /%s/ hors de l'encart)" % (outil, motif)))
        elif pos is None:
            if rel in toleres:
                signales.append((rel, outil, toleres[rel]))
            else:
                ecarts.append((rel, "l'encart enseigne « %s », et aucune activité de la page n'ouvre "
                                    "cet outil : pas de porte, pas d'encart (règle d'or n°297)" % outil))
        elif pos[0] is False:
            ecarts.append((rel, "l'encart « %s » n'est pas à la porte de l'outil : %s" % (outil, pos[1])))
    perimes = sorted(rel for rel in toleres if rel not in avec_encart)
    if not muet:
        print("%d page(s) lues · %d encart(s) « les quatre gestes » · %d écart(s) · "
              "%d toléré(s) nommément" % (len(lues), vus, len(ecarts), len(signales)))
        print("     NON LU : que les quatre gestes soient JUSTES pour cet outil et cette version —\n"
              "     cela se vérifie devant le logiciel, pas dans un script. Ni que l'activité collée\n"
              "     soit la première qui OUVRE l'outil : le script lit une mention, pas une ouverture.")
        if signales:
            print("\n⚠ %d encart(s) d'un outil que la page n'ouvre pas, TOLÉRÉS nommément (TOLERES) :"
                  % len(signales))
            for rel, outil, raison in signales:
                print("  %s  (%s)\n     %s" % (rel, outil, raison))
        if perimes:
            print("\nℹ %d tolérance(s) périmée(s) — la page n'a plus d'encart, retirer l'entrée de TOLERES :"
                  % len(perimes))
            for rel in perimes:
                print("  %s" % rel)
    if ecarts:
        print("\n⛔ %d encart(s) refusé(s) :" % len(ecarts))
        for rel, d in ecarts:
            print("  %s\n     %s" % (rel, d))
        return 1
    print("\n✅ chaque encart « les quatre gestes » nomme l'outil de sa page et se tient à sa porte")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
