#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit les deux synthèses manquantes de 4e_C6.2 — « Le jardin connecté s'arrose ».

Le lot portait déjà séquence, QCM, fiche, matrice et rapport de tests. Il lui
manquait les deux synthèses, et c'est la seule pièce qui l'empêchait d'être
« complet et validable ».

RIEN N'EST INVENTÉ ICI. Chaque encadré de la synthèse élève reprend un « à
retenir » de la banque de QCM du lot, mot pour mot ou resserré, et la trace
écrite de la séquence. Une synthèse qui dirait autre chose que la séquence
serait un troisième document à maintenir, et il divergerait au premier
ajustement.

Usage : python3 synth62.py
"""
import pathlib

DOS = pathlib.Path(__file__).parent
CODE = "4e_C6.2"
SEQ = "sequence-jardin-connecte-arrosage-automatique.html"
QCM = "qcm_4e_C6.2_arrosage_automatique.html"

CSS = """
body{font-family:system-ui,sans-serif;max-width:740px;margin:24px auto;padding:0 16px;line-height:1.55;color:#1a1a1a}
h1{color:#1d4e89}h2{color:#2966b1;border-bottom:2px solid #e0e8f5;padding-bottom:4px}
.box{background:#f0f6ff;border-left:4px solid #1d4e89;padding:12px 16px;margin:12px 0;border-radius:0 8px 8px 0}
.limite{background:#fdeff1;border-left:4px solid #b0344b}
table{width:100%;border-collapse:collapse;margin:12px 0;font-size:.93em}
th,td{border:1px solid #b9cbe4;padding:7px 9px;text-align:left}th{background:#e8f0fb;color:#1d4e89}
code{background:#eef3fa;padding:1px 5px;border-radius:4px;font-size:.92em}
ul{padding-left:1.2em}footer{margin-top:32px;font-size:.85em;color:#666}
#navharm{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px;padding:0}#navharm a{padding:5px 11px;border:1.5px solid #b9cbe4;border-radius:999px;background:#f0f7ff;color:#1d4e89;font-size:.88em;text-decoration:none;line-height:1.2}#navharm a:hover{border-color:#1d4e89}@media print{#navharm{display:none}}"""

NAV = ('<nav id="navharm" aria-label="Navigation du site">'
       '<a href="../../../../index.html">⌂ Accueil</a>'
       '<a href="%s">← Séquence</a><a href="%s">🧠 QCM</a>'
       '<a href="lexique_%s.html">📖 Lexique</a></nav>' % (SEQ, QCM, CODE))


def page(titre, corps, pied):
    return ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            "<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n%s\n%s\n"
            "<footer>%s</footer>\n</body>\n</html>\n" % (titre, CSS, NAV, corps, pied))


ELEVE = [
 ("Les deux chaînes du jardin", """Un système automatisé enchaîne <b>deux circuits</b>. La
  <b>chaîne d'information</b> : le capteur <em>acquiert</em> une donnée brute, le programme la
  <em>traite</em> — conversion, comparaison au seuil —, l'écran <em>communique</em>. La <b>chaîne
  d'énergie</b> : l'alimentation fournit, le relais distribue, la pompe convertit en action.
  Elles se rencontrent à la pompe, là où une décision devient un effet."""),
 ("L'instruction conditionnelle", """<code>SI … ALORS … SINON</code> : la machine choisit selon
  que la condition est vraie ou fausse. Et <b>une condition dit ce qu'elle fait dans les deux
  cas</b> — pas seulement quand elle est vraie. Sur l'algorigramme, le <b>losange</b> est le test
  à deux sorties, le <b>rectangle</b> une action."""),
 ("Le sens de la comparaison", """On arrose quand l'humidité est <b>inférieure</b> au seuil.
  Écrire la comparaison à l'envers ne provoque aucune erreur : le programme s'exécute très bien,
  et il arrose exactement quand il ne faut pas."""),
 ("Un seuil est un paramètre", """Une valeur <b>réglable sans réécrire le programme</b>. C'est
  pour cela qu'on la range en haut, avec un nom : on change le réglage sans toucher à la
  logique."""),
 ("Un mauvais seuil ne casse rien", """Trop bas, on arrose <b>trop tard</b> et la plante a soif.
  Trop haut, on <b>gaspille</b>. Dans les deux cas le programme fonctionne parfaitement — il fait
  mal le travail, et c'est bien plus difficile à voir qu'une panne."""),
 ("La boucle et la condition", """La <b>boucle</b> répète, la <b>condition</b> choisit. Un
  système qui surveille a besoin des deux : relire la mesure sans arrêt ne sert à rien si
  personne ne décide, et décider une seule fois ne surveille rien."""),
 ("Prédire avant d'exécuter", """On écrit ce qu'on <em>attend</em>, puis on exécute, puis on
  compare. <b>C'est l'écart qui enseigne, pas le résultat.</b> Une colonne ATTENDU remplie après
  coup n'apprend rien à personne."""),
 ("Le cas frontière", """L'essai <b>exactement au seuil</b> est le seul qui distingue
  <code>&lt;</code> de <code>&lt;=</code>. Un banc de tests sans cas frontière ne prouve pas
  grand-chose."""),
 ("Ce qu'un test prouve", """Un test prouve <b>un comportement dans un cas</b>. Il ne prouve
  <b>jamais l'absence de défaut</b>. Et une exécution simulée prouve la logique — elle ne prouve
  pas le montage."""),
 ("Compléter n'est pas programmer", """Compléter, c'est <b>ajouter la pièce manquante</b> à un
  programme fourni, puis le prouver à l'exécution. C'est un geste précis, et il a ses règles :
  une instruction qui utilise une valeur vient <b>après</b> celle qui la produit."""),
 ("ET restreint, OU élargit", """Ajouter une seconde condition avec <b>ET</b> réduit les cas où
  l'on arrose : les deux doivent être vraies. Avec <b>OU</b>, on les élargit. Le mot change le
  comportement autant que les valeurs."""),
 ("Une preuve se revérifie", """Une preuve est <b>quelque chose qu'un autre peut aller
  revérifier</b> : un banc de tests écrit, des valeurs relevées, un cahier des charges en regard.
  « Ça marche » n'est pas une preuve — c'est un souvenir."""),
]

PROF_PARI = """<p>Le verbe du code est <b>compléter</b>, et le mot qui décide est
<em>fourni</em> : le programme existe, il tourne, et il lui manque une pièce. Le pari du lot est
qu'un élève de 4<sup>e</sup> comprend mieux une instruction conditionnelle en la <b>posant dans
un programme qui marche</b> qu'en l'écrivant sur une page blanche.</p>
<p>Le moment qui porte la séance est le <b>cas frontière</b> — l'essai exactement au seuil. C'est
le seul qui distingue <code>&lt;</code> de <code>&lt;=</code>, et c'est celui que personne
n'écrit spontanément. Il oblige à remplir la colonne ATTENDU <em>avant</em> d'exécuter, sans quoi
l'essai ne prouve rien.</p>
<p><b>La difficulté la plus intéressante</b> est ailleurs : un mauvais seuil ne casse rien. Le
programme s'exécute, la pompe tourne, et le jardin est mal arrosé. C'est un défaut de
<em>réglage</em>, pas de code — et il faut un banc de tests, pas un débogueur, pour le voir.</p>"""

PROF_CAPABLE = [
 "lire une instruction conditionnelle et dire ce qu'elle fait dans les deux cas",
 "compléter la condition d'un programme fourni, en blocs puis en Python",
 "distinguer un paramètre réglable d'une valeur écrite dans la logique",
 "expliquer ce qu'un seuil trop bas et un seuil trop haut produisent, séparément",
 "construire un banc de tests comportant un cas frontière, ATTENDU rempli d'avance",
 "dire ce qu'un test au vert prouve, et ce qu'il ne prouve pas",
 "justifier par écrit le seuil retenu, avec des valeurs relevées",
]

PROF_LIMITES = [
 "<b>Le programme n'est pas écrit de zéro.</b> Il est fourni, remis en ordre puis complété — "
 "écrire un programme entier relève de <code>4e_C9.3</code>. La séquence le dit à l'élève.",
 "<b>L'exécution est simulée dans l'éditeur embarqué.</b> Elle prouve la logique, pas le "
 "montage : la version avec la carte, le capteur en terre et le relais fait foi, et c'est elle "
 "qui révèle les défauts d'énergie.",
 "<b>Le QCM du lot déborde sur quatre autres codes</b> — C4.1, C4.4, C4.5 et C1.4 — avec deux à "
 "cinq questions chacun. C'est trop peu pour les évaluer : ils sont <em>mobilisés</em>, pas "
 "mesurés, et seul <code>4e_C6.2</code> (16 questions) est au-dessus du seuil d'évaluabilité.",
 "<b>Le choix du seuil n'est pas tranché par la séquence.</b> C'est volontaire : l'élève doit "
 "l'argumenter, et deux valeurs différentes bien justifiées valent mieux qu'une valeur juste "
 "recopiée.",
]

PROF_LSU = [
 ("🔴 Insuffisante", "exécute le programme sans savoir ce que la condition décide"),
 ("🟠 Fragile", "complète la condition si on lui rappelle le sens de la comparaison"),
 ("🟢 Satisfaisante", "complète, exécute, et prouve par un banc de tests avec cas frontière"),
 ("⭐ Très bonne", "et justifie le seuil retenu par des valeurs relevées"),
]


def main():
    DOS.mkdir(parents=True, exist_ok=True)
    corps = "\n".join('<h2>%s</h2>\n<div class="box"><p>%s</p></div>' % (t, x) for t, x in ELEVE)
    (DOS / ("synthese_eleve_%s.html" % CODE)).write_text(page(
        "Synthèse élève — Le jardin connecté s'arrose (%s)" % CODE,
        "<h1>💧 Le jardin connecté s'arrose — ce qu'il faut retenir</h1>\n"
        '<p style="color:#555">Thème 2 · 4<sup>e</sup> — %s. Imprimable en noir et blanc, '
        "lisible hors ligne.</p>\n%s" % (CODE, corps),
        "Synthèse élève — %s. Programme 2024, Thème 2." % CODE), encoding="utf-8")

    cap = "\n".join("<li>%s</li>" % x for x in PROF_CAPABLE)
    lim = "\n".join('<div class="box limite"><p>%s</p></div>' % x for x in PROF_LIMITES)
    lsu = "\n".join("<tr><td>%s</td><td>%s</td></tr>" % k for k in PROF_LSU)
    (DOS / ("synthese_professeur_%s.html" % CODE)).write_text(page(
        "Synthèse professeur — Le jardin connecté s'arrose (%s)" % CODE,
        "<h1>💧 Le jardin connecté s'arrose — synthèse professeur</h1>\n"
        "<h2>Le pari de la séquence</h2>\n%s\n"
        "<h2>Ce que l'élève sait faire à la fin</h2>\n<ul>\n%s\n</ul>\n"
        "<h2>Ce que la séquence ne fait pas — et pourquoi</h2>\n%s\n"
        "<h2>Positionnement (LSU)</h2>\n"
        "<table><tr><th>Maîtrise</th><th>Ce qu'on observe</th></tr>\n%s\n</table>\n"
        "<h2>Durée</h2>\n<p><b>3 séances de 55 min</b> — découverte, consolidation, "
        "validation. Le bandeau de la séquence l'annonce, et "
        "<code>_outils/mesurer_temps_seances.py</code> le vérifie.</p>\n"
        "<h2>D'où vient cette synthèse</h2>\n<p>Chaque encadré de la synthèse élève reprend un "
        "« à retenir » de la banque de QCM de ce lot, ou la trace écrite de la séquence. "
        "<b>Rien n'y est ajouté.</b> Une synthèse qui dirait autre chose que la séquence serait "
        "un troisième document à maintenir, et il divergerait au premier ajustement.</p>"
        % (PROF_PARI, cap, lim, lsu),
        "Synthèse professeur — %s. Programme 2024, Thème 2." % CODE), encoding="utf-8")
    print("écrit : synthese_eleve_%s.html (%d encadrés) et synthese_professeur_%s.html"
          % (CODE, len(ELEVE), CODE))


if __name__ == "__main__":
    main()
