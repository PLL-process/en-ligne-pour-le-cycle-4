# 3e_C7.4 — La station doit tenir 72 heures sans secteur

> **Choisir une source d'énergie pour un OST.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D3 · D4 · D5

➡ **[Ouvrir la séquence](sequence_3e_C7.4_energie-de-la-station.html)** — 2 séances de 90 min (1 h 30), banc d'énergie intégré, hors ligne, sans
installation ni compte.

---

## Ce que le lot fait

Le verbe du code est **choisir une source pour un OST** — sans liste fermée, sans
grille fournie. Le lot pose donc un objet réel, une contrainte réelle, et un avis à signer.

**Le pivot :** la station est alimentée par le secteur, et le réseau tombe exactement au
moment où elle sert. La réponse attendue n'est pas UNE source, c'est une **architecture** :
qui alimente d'habitude, qui prend le relais, qui recharge.

**La contre-intuition à faire vivre :** « un panneau solaire, c'est autonome ». Sous un
cyclone, un panneau récolte moins d'un dixième de sa production — et une plaque plate à 180 km/h
s'arrache. Le panneau ne *tient* pas : il *recharge*.

**Et la spirale se referme :** deux accus donnent 18,8 Wh pour 18,12 exigés, soit 3,8 % de
marge. C'est le bois qui cassait à 41 kg pour 40 en 5<sup>e</sup> et le mât recalé pour 1,1 mm en
3<sup>e</sup>. **Tout juste n'est pas assez**, trois fois, sur trois objets sans rapport.


## La spirale C7.4

| Niveau | Ce qu'on demande | Ce qu'on donne |
|---|---|---|
| 5<sup>e</sup> | choisir une source pour l'indicateur du hall | une liste de cinq sources, et le lieu |
| 4<sup>e</sup> | comparer les sources du jardin connecté | les critères à identifier, une grille à remplir |
| 3<sup>e</sup> | choisir la source de la station d'alerte | rien — un objet réel et un avis à signer |

## Le banc d'énergie

Original, écrit pour ces trois lots, en HTML et JavaScript, sans dépendance et sans réseau.
Il fait, sous les yeux de l'élève, les deux multiplications et la division qu'un technicien fait
sur un coin de table — et il permet d'**éteindre** un consommateur pour voir ce qu'il pesait.

Ce montage consomme **6,04 Wh par jour**. Toutes les valeurs sont calculées par
[`energie.py`](energie.py) : courants constructeur usuels, capacités réelles du commerce,
rendement d'un régulateur linéaire = V<sub>sortie</sub> ÷ V<sub>entrée</sub>, ensoleillement de
la Martinique à 5,3 heures équivalent plein soleil par jour avec 30 % de pertes de chaîne.

## Sécurité

Très basse tension **5 V** partout. Le « secteur » est un **adaptateur USB fermé** — jamais la
prise, jamais le câble. Côté élève, il n'y a que du 5 V. C'est la règle de la skill
`arduino-grove-college`, et la fiche pédagogique détaille en outre lesquels de ses 20 éléments
sont tenus ici et lesquels sont **sans objet**, puisque rien n'est programmé dans ce lot.

## Tests

**36 / 36** sur la séquence, **26 / 26** sur le QCM, rejouables : les deux scripts et le jeu de
réponses sont livrés dans le dossier. Voir [`rapport_tests_3e_C7.4.md`](rapport_tests_3e_C7.4.md).

## Fichiers

| Fichier | Contenu |
|---|---|
| [`sequence_3e_C7.4_energie-de-la-station.html`](sequence_3e_C7.4_energie-de-la-station.html) | 6 activités chronométrées, banc intégré |
| [`qcm_3e_C7.4_energie-de-la-station.html`](qcm_3e_C7.4_energie-de-la-station.html) | 30 q · 90 réfutations · 3e_C7.4 ×20, 3e_C3.2 ×10 |
| [`lexique_3e_C7.4.html`](lexique_3e_C7.4.html) | 30 notions, générées depuis le QCM du lot |
| [`synthese_eleve_3e_C7.4.html`](synthese_eleve_3e_C7.4.html) | à imprimer, lisible en noir et blanc |
| [`synthese_professeur_3e_C7.4.html`](synthese_professeur_3e_C7.4.html) | pari didactique, limites, repères LSU |
| [`fiche_pedagogique_3e_C7.4.md`](fiche_pedagogique_3e_C7.4.md) | déroulé, valeurs, différenciation, skill |
| [`matrice_couverture_3e_C7.4.csv`](matrice_couverture_3e_C7.4.csv) | notion → activité → production → questions |
| [`rapport_tests_3e_C7.4.md`](rapport_tests_3e_C7.4.md) | la sortie des deux suites, telle quelle |
| [`energie.py`](energie.py) | recalcule toutes les valeurs du banc |
