# 🏭 Le support du capteur — `4e_C7.7`

> Le dessin est validé. Comment savoir, avant de lancer la machine, si elle rendra bien la pièce qu'on a dessinée ?

**Thème 3 · 4<sup>e</sup> — Choisir les moyens et produire la forme voulue.** · appui `4e_C4.3` · 2 séances de 55 min (95 min d'activités)

➡ **[Ouvrir la séquence](sequence_4e_C7.7_support-du-capteur.html)** — hors ligne, sans installation ni compte.

## Trois niveaux, trois gestes

Le programme 2024 emploie **la même phrase** en 4<sup>e</sup> et en
3<sup>e</sup> — « Choisir les moyens et produire la forme voulue ». Ce n'est donc pas elle qui
distingue les deux niveaux, c'est le geste :

| Niveau | Formulation officielle | Le geste |
|---|---|---|
| 4<sup>e</sup> | Choisir les moyens et produire la forme voulue | **confronter** — la forme est donnée, deux moyens savent la produire, et aucun ne rend le dessin |
| 3<sup>e</sup> | Choisir les moyens et produire la forme voulue | **corriger** — le moyen est déjà choisi, et c'est le dessin qui doit venir à sa rencontre |

## L'instrument

`atelier.py` engendre un **atelier des moyens**. Il ne classe pas les machines du meilleur au
pire : il dit **lesquelles savent produire CETTE forme-là**, et **ce que chacune en fera**. Deux
idées y sont rendues manipulables, et chacune correspond à une erreur qu'on fait vraiment :

* **un moyen n'a pas de qualité, il a un domaine.** Hors de son domaine il ne fait pas
  « moins bien » : il ne fait pas, ou il fait autre chose. Une fraiseuse ne rate pas un angle
  interne vif — elle le fait rond, parce qu'un outil rond ne peut rien faire d'autre ;
* **tout moyen déforme le dessin, à sa manière, et toujours.** Le laser élargit de son trait de
  coupe, la fraiseuse arrondit les angles internes, l'impression laisse un bourrelet de première
  couche. **Le dessin est ce qu'on a demandé, la pièce est ce qu'on obtient.**

En 4<sup>e</sup>, la forme est figée et c'est la **quantité** qui se règle. En 3<sup>e</sup>,
chaque **cote se modifie** — et une seconde jauge compte celles qu'on a touchées sans nécessité
(règle d'or n°219).

Toutes les valeurs viennent de `moyens.py` : temps, domaines, empreintes et verdicts sont
**calculés**, jamais recopiés. `python3 moyens.py` rejoue les deux tables.

## Ce que contient le dossier

| Fichier | Ce que c'est |
|---|---|
| [`sequence_4e_C7.7_support-du-capteur.html`](sequence_4e_C7.7_support-du-capteur.html) | la séquence élève, hors ligne, avec le banc |
| [`qcm_4e_C7.7_support-du-capteur.html`](qcm_4e_C7.7_support-du-capteur.html) | 30 questions — 20 sur `4e_C7.7`, 10 sur `4e_C4.3`, 90 réfutations |
| [`lexique_4e_C7.7.html`](lexique_4e_C7.7.html) | 30 notions, engendrées depuis le QCM |
| [`synthese_eleve_4e_C7.7.html`](synthese_eleve_4e_C7.7.html) | à retenir, imprimable en noir et blanc |
| [`synthese_professeur_4e_C7.7.html`](synthese_professeur_4e_C7.7.html) | le pari, les limites, la grille LSU |
| [`fiche_pedagogique_4e_C7.7.md`](fiche_pedagogique_4e_C7.7.md) | déroulé, versions, sécurité, origine des nombres |
| [`matrice_couverture_4e_C7.7.csv`](matrice_couverture_4e_C7.7.csv) | notion → activité → production → question |
| [`rapport_tests_4e_C7.7.md`](rapport_tests_4e_C7.7.md) | la sortie des deux suites, telle quelle |
| `moyens.py` · `atelier.py` · `tests_4e_C7.7_sequence.mjs` · `tests_4e_C7.7_qcm.mjs` · `reponses_4e_C7.7.json` | de quoi tout rejouer |

**Tests réels : 38/38 sur la séquence, 32/32 sur le QCM.**

## Ancrage

Les deux colonnes qui font le cœur du lot — **tenue au rayonnement solaire** et **tenue au
brouillard salin** — ne figurent dans aucun catalogue générique. Elles éliminent pourtant des
matériaux qu'un tableau écrit sous un climat tempéré retiendrait. C'est la contrainte réelle
d'ici, et elle s'écrit au cahier des charges comme les autres.

## Sécurité

Le **PVC ne passe jamais à la découpe laser** : chauffé, il dégage du chlorure
d'hydrogène, qui brûle les voies respiratoires et corrode la machine. Le PMMA de ce support, lui,
se découpe très bien — capot fermé, **on ne regarde pas le faisceau**, extraction pendant toute
la découpe et une minute après. À la fraiseuse : **pièce bridée**, lunettes, cheveux attachés,
manches remontées, **aucun gant** — un gant happé entraîne la main. Les copeaux se retirent à la
brosse, broche arrêtée, jamais aux doigts ni à l'air comprimé. Côté électricité, la sonde et la
station du jardin sont en **très basse tension** : aucun élève ne manipule le **secteur**.
