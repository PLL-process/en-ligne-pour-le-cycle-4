# -*- coding: utf-8 -*-
"""controle_regle4.py — les deux blocs qui closent une séquence.

LA RÈGLE
--------
Règle d'or n°4 §4, énoncée par Pascal le 24/07/2026 : le bloc « 🧠 Prêt·e à
t'entraîner ? » et le bloc « 🎁 Bonus (facultatif — hors parcours obligatoire) »
**closent la séquence : après le bilan, avant le pied de page**. Un seul bouton
QCM dans toute la page.

Pascal l'a redemandée le 31/08/2026 : « la partie bonus et les QCM à la dernière
page ou à la dernière étape ». Ce fichier mesure ce qu'il demande.

CINQ FOIS FAUX AVANT D'ÊTRE JUSTE
---------------------------------
Ce contrôle a accusé **cinq fois** des pages conformes avant de dire vrai, et
chaque garde-fou ci-dessous vient d'une de ces erreurs. Aucune des cinq n'était
un défaut du dépôt : toutes étaient un défaut de la mesure (règle d'or n°270 —
un test qui échoue accuse d'abord la page ; commence par vérifier qu'il sait la
lire).

1. **L'apostrophe.** Il cherchait « t'entraîner » avec l'apostrophe droite ;
   `5e_C1.3` écrit la sienne avec l'apostrophe typographique. Les deux graphies
   sont désormais acceptées.
2. **L'emoji partagé.** Il prenait tout 🎁 pour le bloc Bonus. Les TP de
   l'atelier CAO finissent par un *palier récompense* « 🎁 Ton boîtier, dehors
   pour de bon » qui fait partie du parcours, et n'est pas le bloc.
3. **L'aparté du professeur.** `3e_C9.2` porte un `<details class="prof">` dont
   le résumé reprend mot pour mot « 🎁 Bonus (facultatif — hors parcours
   obligatoire) » pour parler d'ArduBlock au professeur. Un bloc annoncé dans un
   `<summary>` n'est pas le bloc de l'élève.
4. **La fenêtre trop courte.** Il ne cherchait la mention « Page N sur M » que
   dans les 20 000 premiers octets. Les quatre stations de `3e_C9.2` la portent
   à l'octet 20 826 : les trois premières étaient accusées d'un manque qui est
   leur définition même. Il lit maintenant la page entière — c'est possible sans
   risque, la mesure ayant montré que chaque page ne la porte qu'une fois, et
   que la barre de navigation écrit « Page 2 », jamais « Page 2 sur 4 ».
5bis. **Trop indulgent, une fois.** Les cinq erreurs ci-dessus accusaient à tort ;
   celle-ci laissait passer. Il ne comptait que les liens QCM portant `class="btn"`,
   et les quatre TP de l'atelier CAO en portaient un **second**, en texte courant,
   au premier quart de la page. C'est le navigateur qui l'a vu, pas ce fichier. Un
   lien vers un QCM avant la région finale est désormais un écart, quelle que soit
   son apparence — c'est la demande de Pascal, mot pour mot : « à la dernière page
   ou à la dernière étape ». Deux liens **tous deux** dans la région finale ne le
   sont pas : `4e_C2.1` et `4e_C4.1` les portent à 69 % et 73 %, et cela va.
5. **La balise au milieu du titre.** `3e_C1.1` écrit
   `🎁 Bonus <span style="…">(facultatif — …)</span>` : le mot et sa parenthèse
   sont séparés par une balise. Le motif traverse désormais les balises et les
   espaces insécables — et rien d'autre.

CE QU'IL ÉCARTE, ET POURQUOI
----------------------------
**Les pages-pointeurs** (moins de 6 Ko) : `3e_C7.2/tp_3e_boitier_etanche.html`
et ses semblables renvoient vers le TP réel de l'atelier. Ce sont des panneaux
indicateurs, pas des séquences.

**Les étapes d'une séquence en plusieurs pages** : une page qui déclare
elle-même « Page 2 sur 4 » est une étape. Lui poser le bloc QCM mettrait
l'entraînement avant la fin — exactement ce que Pascal reprochait le 30/08 :
« le QCM est proposé presque sur toutes les pages, alors que toutes les
compétences ne sont pas atteintes ».

**Les exceptions nommées**, listées dans TOLEREES avec leur raison.

Usage :
    python3 _outils/controle_regle4.py           # rapport complet
    python3 _outils/controle_regle4.py --muet    # seulement les écarts
Sortie : 0 si toute séquence close par les deux blocs, 1 sinon.
"""

import glob
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

#: en dessous, une page qui renvoie ailleurs plutôt qu'une séquence
POINTEUR = 6000

#: la « région finale » d'une page, en pourcentage de sa longueur. Ce n'est pas
#: une mesure fine — c'est un seuil grossier qui sépare « au début, avant d'avoir
#: rien fait » de « à la fin, une fois le parcours accompli ».
FIN = 55

#: une page qui déclare elle-même n'être qu'une étape d'une séquence plus longue.
#: On lit la page entière : les quatre stations de `3e_C9.2` portent la mention à
#: l'octet 20 826, et une fenêtre plus courte les accusait toutes les trois.
ETAPE = re.compile(r"Page\s+(\d+)\s+sur\s+(\d+)", re.I)

TOLEREES = {
    "theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-"
    "une-ou-des/atelier-cao/tp_modele_demonstration.html":
        "modèle de TP destiné à l'enseignant (« Modèle de TP de prise en main ») : "
        "il montre la forme d'un TP, il n'en est pas un, et aucun QCM ne lui correspond.",
}

#: les DEUX apostrophes, droite et typographique
PRET = re.compile(r"Pr[êe]t(?:·|&middot;|&#183;)?e?\s*(?:&nbsp;|\s)*[àa]\s*t['’]entra", re.I)
#: « Bonus (facultatif » — le titre peut porter une balise entre les deux mots :
#: `3e_C1.1` met sa parenthèse dans un <span>. On traverse balises et espaces,
#: et rien d'autre : un « Bonus » suivi trois paragraphes plus loin d'un
#: « (facultatif » ne serait pas ce titre.
BONUS = re.compile(r"Bonus(?:\s|&nbsp;|<[^>]{0,120}>)*\(facultatif", re.I)
LIEN_QCM = re.compile(r'<a\b[^>]*href="[^"]*qcm[^"]*\.html"[^>]*>', re.I)
NAV = re.compile(r"<nav\b[^>]*>.*?</nav>", re.I | re.S)
BOUTON = re.compile(r'class="[^"]*\b(btn|button)\b', re.I)


def pages(racine):
    motifs = ("**/sequence*.html", "**/tp_*.html", "**/atelier_*.html")
    vus = set()
    for m in motifs:
        for f in glob.glob(os.path.join(racine, m), recursive=True):
            if any(e in f for e in ECARTES):
                continue
            vus.add(f)
    return sorted(vus)


def bloc_bonus_de_leleve(texte):
    """Le bloc Bonus de la règle n°4 — pas un aparté annoncé dans un <summary>."""
    for m in BONUS.finditer(texte):
        avant = texte.rfind("<", 0, m.start())
        balise = texte[avant:avant + 9].lower() if avant >= 0 else ""
        if balise.startswith("<summary"):
            continue
        return True
    return False


def juger(chemin):
    """(conforme, famille, détail) — `conforme` vaut None si la page est écartée."""
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    rel = os.path.relpath(chemin, DEPOT).replace(os.sep, "/")
    if rel in TOLEREES:
        return None, "tolérée par déclaration", TOLEREES[rel]
    if os.path.getsize(chemin) < POINTEUR:
        return None, "page-pointeur", ("%d octets : elle renvoie vers la ressource réelle"
                                       % os.path.getsize(chemin))
    e = ETAPE.search(re.sub(r"<[^>]+>", " ", texte))
    if e and e.group(1) != e.group(2):
        return None, "étape d'une séquence en plusieurs pages", ("elle se déclare « page %s sur "
                                                                 "%s »" % e.groups())
    navs = [(m.start(), m.end()) for m in NAV.finditer(texte)]
    liens = [m for m in LIEN_QCM.finditer(texte)
             if not any(a <= m.start() < b for a, b in navs)]
    boutons = [m for m in liens if BOUTON.search(m.group(0))]
    pos = [round(100 * m.start() / len(texte)) for m in boutons]
    tot = [round(100 * m.start() / len(texte)) for m in liens]
    manques = []
    if not PRET.search(texte):
        manques.append("pas de bloc « Prêt·e à t'entraîner »")
    if not bloc_bonus_de_leleve(texte):
        manques.append("pas de bloc « Bonus » pour l'élève")
    if len(boutons) == 0:
        manques.append("aucun bouton QCM hors de la barre de navigation")
    elif len(boutons) > 1:
        manques.append("%d boutons QCM au lieu d'un seul" % len(boutons))
    elif pos[0] < FIN:
        manques.append("le bouton QCM est à %d %% de la page, pas à la fin" % pos[0])
    tot_avant = [p for p in tot if p < FIN]
    if tot_avant:
        manques.append("%d lien(s) vers un QCM avant la région finale (à %s %% de la page)"
                       % (len(tot_avant), ", ".join(str(p) for p in tot_avant)))
    return (not manques), "", " · ".join(manques)


def main(muet=False):
    conformes, ecartees, ecarts = 0, [], []
    for f in pages(DEPOT):
        verdict, famille, detail = juger(f)
        rel = os.path.relpath(f, DEPOT)
        if verdict is None:
            ecartees.append((rel, famille, detail))
        elif verdict:
            conformes += 1
        else:
            ecarts.append((rel, detail))
    if not muet:
        print("%d page(s) jugées · %d conformes · %d écart(s) · %d écartée(s), chacune pour une "
              "raison écrite" % (conformes + len(ecarts), conformes, len(ecarts), len(ecartees)))
        raisons = {}
        for _, famille, _d in ecartees:
            raisons[famille] = raisons.get(famille, 0) + 1
        for r, n in sorted(raisons.items(), key=lambda x: -x[1]):
            print("     %2d × %s" % (n, r))
        print("     NON LU : ce que le bloc CONTIENT — qu'un défi bonus soit ouvert et sans\n"
              "     vérificateur se lit, se juge, et ne se mesure pas.")
    if ecarts:
        print("\n⛔ %d page(s) ne closent pas sur les deux blocs (règle n°4 §4) :" % len(ecarts))
        for rel, d in ecarts:
            print("  %s\n     %s" % (rel, d))
        return 1
    print("\n✅ toute séquence close par « Prêt·e à t'entraîner » puis « Bonus », un seul bouton QCM")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))

