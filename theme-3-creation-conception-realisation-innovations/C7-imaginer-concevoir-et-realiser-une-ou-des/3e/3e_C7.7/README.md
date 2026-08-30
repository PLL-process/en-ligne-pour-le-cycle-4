# 🖨 Produire le boîtier — `3e_C7.7`

> Le dessin est juste et la pièce est ratée. Que faut-il corriger — et surtout, que faut-il surtout ne pas toucher ?

**Thème 3 · 3<sup>e</sup> — Choisir les moyens et produire la forme voulue.** · appui `3e_C8.1` · 2 séances de 90 min (160 min d'activités)

➡ **[Ouvrir la séquence](sequence_3e_C7.7_produire-le-boitier.html)** — hors ligne, sans installation ni compte.

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
| [`sequence_3e_C7.7_produire-le-boitier.html`](sequence_3e_C7.7_produire-le-boitier.html) | la séquence élève, hors ligne, avec le banc |
| [`qcm_3e_C7.7_produire-le-boitier.html`](qcm_3e_C7.7_produire-le-boitier.html) | 30 questions — 20 sur `3e_C7.7`, 10 sur `3e_C8.1`, 90 réfutations |
| [`lexique_3e_C7.7.html`](lexique_3e_C7.7.html) | 30 notions, engendrées depuis le QCM |
| [`synthese_eleve_3e_C7.7.html`](synthese_eleve_3e_C7.7.html) | à retenir, imprimable en noir et blanc |
| [`synthese_professeur_3e_C7.7.html`](synthese_professeur_3e_C7.7.html) | le pari, les limites, la grille LSU |
| [`fiche_pedagogique_3e_C7.7.md`](fiche_pedagogique_3e_C7.7.md) | déroulé, versions, sécurité, origine des nombres |
| [`matrice_couverture_3e_C7.7.csv`](matrice_couverture_3e_C7.7.csv) | notion → activité → production → question |
| [`rapport_tests_3e_C7.7.md`](rapport_tests_3e_C7.7.md) | la sortie des deux suites, telle quelle |
| `moyens.py` · `atelier.py` · `tests_3e_C7.7_sequence.mjs` · `tests_3e_C7.7_qcm.mjs` · `reponses_3e_C7.7.json` | de quoi tout rejouer |

**Tests réels : 52/52 sur la séquence, 32/32 sur le QCM.**

## Ancrage

Les deux colonnes qui font le cœur du lot — **tenue au rayonnement solaire** et **tenue au
brouillard salin** — ne figurent dans aucun catalogue générique. Elles éliminent pourtant des
matériaux qu'un tableau écrit sous un climat tempéré retiendrait. C'est la contrainte réelle
d'ici, et elle s'écrit au cahier des charges comme les autres.

## Sécurité

Impression en **local ventilé, capot fermé** : une buse à 240 °C émet des particules
ultrafines, et l'on ne se penche pas au-dessus du plateau. La buse et le plateau restent chauds
longtemps après la fin : on décolle à la spatule, plateau refroidi, jamais aux doigts. Le retrait
des supports se fait **avec des lunettes** — un support arraché part en éclats. Le **PVC** ne
s'imprime pas et ne se découpe pas au laser. La station est alimentée en **très basse tension**,
aucun élève ne manipule le **secteur**, et la pose en tête de mât reste un geste d'agent.
