# Relevé des captures à prendre — TP 5e bis « Le dé, en mieux »

Ce relevé **n'existait pas**. Le TP est né le 30 août 2026 avec ses huit paliers, et l'atelier
a continué d'en annoncer trois, comme au 11 août 2026 : celui-ci n'a jamais été écrit, et ses
images manquantes n'étaient donc réclamées nulle part. Elles le sont ici.

**État mesuré** : **cinq paliers sur huit** n'ont aucune image de résultat, et les trois qui en
ont une portent **le même** dessin — `coupe_calotte_5e.svg`, la coupe engendrée par
`calotte.py`. La règle n°77 refuse ce TP, et elle a raison : un élève qui ne peut pas se
comparer lève la main, et c'est le seul chiffre qui compte.

Toutes les images vont dans `Images/`, avec **exactement** le nom indiqué.

## Les cinq images qui manquent

| Nom du fichier | Nature | Palier | Ce qu'il faut voir |
|---|---|---|---|
| `tp5eb_R1_deux_onglets.png` | capture d'interface | 1 — Ranger avant de commencer | Le bas de l'écran Onshape : **deux onglets** côte à côte, l'original et **Dé v2**, celui de droite actif. C'est la preuve que le témoin n'a pas été écrasé — le geste le plus important du TP, et le moins spectaculaire. |
| `tp5eb_R2_creux_supprime.png` | résultat du palier | 3 — Mettre l'ancien creux de côté | La face du 1 **redevenue lisse**, et à gauche l'arbre des fonctions où la ligne supprimée est **grisée** et non effacée. Les vingt autres creux sont toujours là : c'est voulu, et l'image doit le montrer. |
| `tp5eb_R3_calotte.png` | résultat du palier | 5 — La bille en mode « Retirer » | Le dé en perspective rapprochée sur la face du 1 : un creux **rond**, sans arête vive, le bord descendant en pente douce. À comparer d'un coup d'œil avec `tp5eb_R2`. |
| `tp5eb_R4_mesure_1054.png` | capture d'interface | 6 — Mesurer, comparer, décider | Le coin bas-droit d'Onshape avec la mesure affichée : **10,54**. C'est le chiffre autour duquel tourne toute la décision du palier ; l'élève doit savoir où il s'affiche. |
| `tp5eb_R5_v1_v2.png` | résultat du palier | 8 — 🎁 Deux dés, une seule différence | Les **deux** dés côte à côte, de couleurs différentes, cadrés de trois quarts pour que la face du 1 se voie sur les deux. Une seule différence doit sauter aux yeux ; tout le reste doit être identique. |

Les paliers 2, 4 et 7 gardent le dessin de coupe (`coupe_calotte_5e.svg`) : il explique une
géométrie, ce qu'aucune capture ne ferait mieux. Le palier 7 (exporter les deux STL) n'a pas
besoin d'image — la liste des téléchargements suffit, et son critère de réussite est écrit.

## Comment cadrer

Pour une **capture d'interface** (`R1`, `R4`) : serré sur le panneau et la zone concernée,
jamais tout l'écran. L'interface doit être **en français** (règle d'or n°70), et toute valeur
lisible dans l'image est annoncée comme exemple dans le texte (n°75).

Pour une **image de résultat** (`R2`, `R3`, `R5`) : vue rapprochée sur la face du 1, éclairage
rasant. C'est un creux de 1,5 mm de profond sur un cube de 50 : à contre-jour ou de face, la
calotte et le cylindre se ressemblent — et c'est justement l'argument du palier 6. Il faut donc
le **profil**, pas la vue de face.

## Le mode opératoire, s'il passe par l'API

`tp5eb_R2`, `R3` et `R5` sont des rendus de pièce : l'API Onshape (`/shadedviews`) sait les
produire, comme les seize rendus du 11 août. `R1` et `R4` ne s'obtiennent **pas** par l'API — ce
sont des panneaux du logiciel, et ils demandent un poste en français.

`calotte.py` donne toutes les cotes à reproduire : plan décalé de **8,5 mm**, bille **Ø20**,
mode Retirer, creux résultant **Ø10,54**, profondeur **1,5 mm** identique à celle du cylindre
d'origine.

## Ce que ce relevé sert aussi à faire

Prendre ces images, c'est **dérouler le TP** — et ce TP en a un besoin particulier : ses gestes
Onshape (le plan décalé, la primitive Sphère en mode Retirer) sont écrits **d'après la
documentation**, pas constatés sur poste. C'est la limite déclarée n°5 du manifeste. La séance
de prise de vue est donc aussi la première vérification que les boutons décrits existent, et
qu'ils sont là où le TP les annonce.

Si à un moment tu ne sais pas quoi cliquer, note-le : c'est là qu'un élève lèvera la main.

## Une fois les images en place

```bash
python3 _generation/build_tp.py scenarios/tp_5e_de_calottes.json
python3 verif_guidage.py tp_5e_de_calottes.html
python3 verif_chaine.py
python3 verif_effectifs.py
```

Le générateur signale toute image annoncée mais absente, la règle n°77 refuse le TP tant qu'il
en manque, `verif_chaine.py` vérifie que la page sur le disque est bien ce que le scénario
produit — et `verif_effectifs.py` refuse qu'un TP se retrouve à nouveau sans relevé.
