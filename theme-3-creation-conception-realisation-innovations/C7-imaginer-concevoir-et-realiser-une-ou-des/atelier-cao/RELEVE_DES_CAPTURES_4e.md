# Relevé des captures à prendre — TP 4e « Le dé sur son socle »

Sept images de résultat, aucune capture d'interface pour l'instant : les gestes de 4e
réutilisent des panneaux déjà montrés en 5e. Les sept se produisent **par l'API Onshape**,
sans intervention humaine — voir le mode opératoire n°2.

Toutes les images vont dans `Images/`, avec **exactement** le nom indiqué.

| Nom du fichier | Nature | Moment | Ce qu'il faut voir |
|---|---|---|---|
| `tp4e_R1_profil.png` | résultat du palier | palier 2 — Le profil du socle — une moitié suffit | Le profil du socle : un rectangle noir de 70 mm sur 35 mm, posé contre une ligne de construction verticale en pointillés. |
| `tp4e_R2_socle_brut.png` | résultat du palier | palier 3 — La révolution — faire tourner le profil | Le socle brut : un cylindre gris de 140 mm de diamètre et 35 mm de haut, vu en perspective. |
| `tp4e_R3_socle_moulure.png` | résultat du palier | palier 4 — La moulure — ce qui fait « romain » | Le socle mouluré : les arêtes du haut et du bas sont arrondies, celle du haut plus franchement que celle du bas. |
| `tp4e_R4_deux_pieces.png` | résultat du palier | palier 5 — Le dé — celui de l'an dernier | Deux onglets en bas de l'écran : Socle et De, chacun contenant sa pièce. |
| `tp4e_R5_assemblage_libre.png` | résultat du palier | palier 6 — L'assemblage — mettre les deux pièces ensemble | L'assemblage : le socle au centre, fixé, et le dé posé à côté, dans le vide, sans contrainte. |
| `tp4e_R6_de_centre.png` | résultat du palier | palier 7 — Les contraintes — centrer sans viser | Le dé posé bien au centre du socle mouluré, vu en perspective : les débords sont égaux tout autour. |
| `tp4e_R7_presse_papier.png` | résultat du palier | palier 8 — 🎁 Ton presse-papier, et pas celui du voisin | Le presse-papier terminé : le dé coloré posé au centre du socle mouluré couleur pierre. |

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
python3 _generation/build_tp.py scenarios/tp_4e_socle_assemblage.json
python3 verif_guidage.py tp_4e_socle_assemblage.html
```

Le générateur signale toute image annoncée mais absente, et la règle n°77 refuse le TP
tant qu'il en manque.
