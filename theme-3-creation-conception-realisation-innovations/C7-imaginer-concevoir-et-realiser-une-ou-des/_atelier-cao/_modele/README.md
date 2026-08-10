# Le modèle de référence — presse-papier « dé sur socle »

Ce dossier contient **le modèle du professeur**, pas celui de l'élève.

L'élève, lui, **construit le dé lui-même** dans Onshape, geste après geste, guidé par le TP.
Ce modèle-ci sert à trois choses, et à trois seulement : montrer le résultat visé, imprimer un
exemplaire témoin, et vérifier qu'une cote modifiée donne bien ce qu'on attend.

## Ce qu'il y a ici

| Fichier | Ce que c'est |
|---|---|
| `presse_papier.py` | les 80 lignes qui construisent la pièce, à partir de **trois cotes** |
| `presse_papier_de_sur_socle.stl` | le maillage imprimable, produit par ce script |
| `../Images/presse_papier_vues.png` | trois vues — isométrique, face, dessus |

## Les trois cotes, et rien d'autre

```python
D, H, A = 120.0, 30.0, 40.0    # diamètre du socle, hauteur du socle, arête du dé
```

Tout le reste en découle : le profil mouluré du socle, le rayon et la profondeur des points, leur
écartement, l'enfoncement du dé. Changez `A = 20` et la pièce entière se réajuste — c'est
exactement la démonstration à faire en classe sur la CAO paramétrique.

```bash
python3 presse_papier.py      # → étanche : True | volume : 320.1 cm³ | hauteur : 91.3 mm | Ø : 120.0 mm
```

## Le dé est centré, et il ne peut pas ne pas l'être

Le dé n'est pas *placé* au centre du socle : il est construit **autour de l'origine**, puis pivoté
autour de l'axe vertical (45° puis 54,7356° — l'angle qui met une diagonale de cube à la verticale)
et remonté le long de ce même axe. Aucune étape n'introduit de décalage latéral. Le décentrage
n'est pas corrigé, il est **géométriquement impossible**.

## Les faces opposées font 7

1 en face de 6, 2 en face de 5, 3 en face de 4 — comme sur un vrai dé. Les points sont des
**cylindres soustraits**, pas des sphères : c'est plus fidèle au geste que l'élève apprendra dans
le TP (cercle → enlèvement de matière → congé), et c'est plus propre à imprimer.

## Pourquoi ce modèle n'est pas fait dans Onshape

Onshape reste **le logiciel de la classe** : rien à installer, interface française, comptes
Éducation, ça tourne sur n'importe quel poste du collège. Mais le modèle de référence, lui, se
construit par **script** — c'est reproductible, versionnable, et une cote modifiée se vérifie en
une seconde au lieu de vingt clics.

La règle qui se dégage : *l'élève manipule, le professeur script*. Les deux produisent la même
pièce, et aucun des deux ne fait le travail de l'autre.

## Ce qui n'a pas été vérifié

L'impression réelle. Le maillage est **étanche** (contrôlé), l'orientation d'impression et les
supports nécessaires ne le sont pas — c'est justement l'objet d'une des activités du TP.
