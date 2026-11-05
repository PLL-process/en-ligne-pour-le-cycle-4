# Le relais qui claque, vu en coupe

Pascal, le 05/11/2026, sur la situation déclenchante de `4e_C7.4` (« le capteur lit l'humidité, la carte décide, le relais
claque, la pompe arrose ») : « le relais claque, il faudrait vulgariser ou expliquer ce terme ; il manque aussi des images
réalistes ou des schémas ou une animation ».

## Ce que montre la figure

- **L'explication, en mots** : un relais est un interrupteur que la carte actionne toute seule. Le petit courant de la carte
  passe dans une **bobine**, qui devient un **aimant**. L'aimant attire une **lame**, la lame touche un **contact**, et le
  circuit de la pompe se ferme. Ce mouvement fait « clac ». Un **ressort** relève la lame quand l'ordre est coupé.
- **Le schéma, en coupe** :
  - en haut, le chemin de l'ordre (le capteur mesure, la carte décide, le relais distribue, la pompe arrose) ;
  - à gauche, ① le circuit de la carte, où passe un tout petit courant ;
  - au milieu, l'intérieur du relais ;
  - à droite, ② le circuit de la pompe, où passe un courant fort.
- **L'animation** :
  - « La carte envoie l'ordre » : la bobine s'aimante, la lame se ferme, « clac », le courant circule, la pompe tourne ;
  - « La carte coupe l'ordre » : le ressort relève la lame, « clac » ;
  - « Faire battre 6 fois » : la pompe qui s'affole, avec douze clacs ;
  - « Son » : coupé par défaut ; le clac est fabriqué dans la page, sans fichier.
- Le statut (`role="status"`) dit ce qui vient de se passer et compte les clacs. La légende rappelle que **chaque clac use un
  peu les contacts** : un relais s'use au nombre de fois qu'il bascule, pas au nombre d'années.

Sans JavaScript et sur le papier, le schéma reste, au repos, avec son explication ; les boutons n'apparaissent pas. Avec
« réduire les animations », la lame bascule sans mouvement et le courant ne défile pas.

## Les fichiers

| Fichier | Rôle |
|---|---|
| `relais_figure.py` | écrit la figure (HTML + SVG au repos) dans chaque page de sa liste `PAGES`, entre `<!-- relais-anime:debut -->` et `<!-- relais-anime:fin -->` ; sans argument, vérifie que chaque page est à jour |
| `relais-anime.js` | l'animation (boutons, son, compteur) |
| `relais-anime.css` | l'habit (couleurs de la page, 390 px, cibles de 44 px, impression, mouvement réduit) |
| `banc_relais_anime.mjs` | le banc : la figure à jour, l'animation, le son, 390 px, l'impression, sans JavaScript, hors ligne |

## Poser la figure dans une page

1. Ajouter la page et le titre de sa figure à `PAGES`, dans `relais_figure.py`.
2. Dans la page : la marque vide `<!-- relais-anime:debut -->` puis `<!-- relais-anime:fin -->` à l'endroit choisi, la
   feuille de style dans `<head>`, le script avant `</body>` (chemins relatifs vers `_ressources-communes/relais-anime/`).
3. `python3 _ressources-communes/relais-anime/relais_figure.py --ecrire`, puis le banc.

## Les pages, au 05/11/2026

- **`4e_C7.4`** : dans la situation déclenchante. Elle a aussi l'image du jardin dans la cour, sans source d'énergie
  visible, puisque c'est la question de la séquence.
- **`4e_C7.5`** : sous la consigne de sécurité (« le relais doit claquer »).
- **`4e_C9.1`** : dans l'aide de niveau 2 de l'activité 5, la pompe qui s'affole.
- **`4e_C6.1`** : dans la situation déclenchante (« on l'entend claquer depuis la classe » : la pompe qui a démarré 47 fois).

Le dessin est original (règle d'or n°1), sous la licence du dépôt.
