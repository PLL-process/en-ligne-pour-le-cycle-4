# Relevé des captures à prendre — TP 3e « Le boîtier étanche »

Sept images de résultat. Deux d'entre elles demandent une attention particulière :
`tp3e_R3_rainure.png` est un **gros plan** — la gorge fait 1 mm de large, elle est invisible
sur une vue d'ensemble — et `tp3e_R6_assemblage_coupe.png` est une **vue en coupe**, la seule
qui montre l'espace laissé au joint entre la nervure et le fond de la gorge.

Toutes les images vont dans `Images/`, avec **exactement** le nom indiqué.

| Nom du fichier | Nature | Moment | Ce qu'il faut voir |
|---|---|---|---|
| `tp3e_R1_bloc.png` | résultat du palier | palier 2 — La boîte pleine — le geste de base | Un pavé plein de 80 sur 60 sur 35 millimètres, vu en perspective. |
| `tp3e_R2_coque.png` | résultat du palier | palier 3 — La coque — évider sans creuser | Le boîtier évidé, ouvert vers le haut, parois de 2 millimètres, vu en perspective légèrement de dessus. |
| `tp3e_R3_rainure.png` | résultat du palier | palier 4 — La rainure du joint — là où l'eau s'arrête | Le bord supérieur du boîtier, vu de dessus en gros plan : une gorge continue court tout autour, à mi-largeur du bord. |
| `tp3e_R4_passage_cable.png` | résultat du palier | palier 5 — Le passage du câble — le vrai point faible | Le boîtier vu de trois quarts : un trou de 12 millimètres traverse une paroi latérale en partie basse, son bord extérieur adouci. |
| `tp3e_R5_couvercle.png` | résultat du palier | palier 6 — Le couvercle — une pièce qui en épouse une autre | Le couvercle vu de dessous : une plaque de 80 sur 60 avec une nervure continue de 1 millimètre qui en fait le tour. |
| `tp3e_R6_assemblage_coupe.png` | résultat du palier | palier 7 — L'assemblage — là où les deux pièces se rencontrent | Vue en coupe de l'assemblage : le couvercle posé sur le boîtier, sa nervure engagée dans la gorge, un espace visible entre les deux pour le joint. |
| `tp3e_R7_boitier_fini.png` | résultat du palier | palier 8 — 🎁 Ton boîtier, dehors pour de bon | Le boîtier terminé, coloré, couvercle légèrement soulevé pour montrer la gorge et l'intérieur. |

## Les deux images qui manquent encore (relevé du 26/11/2026)

`verif_guidage.py` (n°77) le dit : les paliers 1 et 8 n'ont **aucune** image de résultat. Ce sont deux captures
d'**interface**, pas des rendus de pièce : elles demandent un poste en français, connecté au compte Onshape.

| Nom du fichier | Nature | Palier | Ce qu'il faut voir |
|---|---|---|---|
| `tp3e_R0_onglet_boitier.png` | capture d'interface | 1 — Ranger avant de commencer | Le bas de l'écran Onshape : l'onglet renommé **Boitier**, et en haut à gauche le nom du document `Boitier capteur — Camille` (prénom d'exemple, annoncé comme tel). |
| `tp3e_R8_retrouve.png` | capture d'interface | 8 — Emporter son travail | La page **Documents**, bande **Ouvert en dernier par moi** : le document `Boitier capteur - CD` (initiales d'exemple) y figure, avec sa vignette. C'est la preuve que le travail se retrouve. |

Une fois prises : les déclarer au scénario (`image_resultat` des paliers 1 et 8), relancer le générateur, puis
`verif_guidage.py` — le n°77 ne doit plus rien refuser.

## Comment cadrer

Pour une **capture d'interface** : serré sur le panneau et la zone concernée, jamais tout
l'écran. Une capture pleine résolution d'un écran 4K rend le bouton illisible au
vidéoprojecteur. L'interface doit être **en français** (règle d'or n°70), et toute valeur
lisible dans l'image est annoncée comme exemple dans le texte (n°75).

Pour une **image de résultat** : vue d'ensemble en perspective, pièce entière, fond neutre.
L'élève doit pouvoir comparer d'un coup d'œil, sans chercher.

## Ce que ce relevé sert aussi à faire

Prendre ces images, c'est **dérouler le TP**. Si à un moment tu ne sais pas quoi cliquer,
note-le : c'est là qu'un élève lèvera la main, et c'est le seul chiffre qui compte.

## Une fois les images en place

```bash
python3 _generation/build_tp.py scenarios/tp_3e_boitier_etanche.json
python3 verif_guidage.py tp_3e_boitier_etanche.html
```

Le générateur signale toute image annoncée mais absente, et la règle n°77 refuse le TP
tant qu'il en manque.
