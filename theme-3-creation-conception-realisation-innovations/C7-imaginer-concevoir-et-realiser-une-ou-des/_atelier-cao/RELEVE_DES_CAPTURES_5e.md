# Relevé des captures à prendre — TP 5e « Le dé » (Onshape)

Le texte du TP est écrit et les onze règles de guidage passent au vert. Il manque **les images**,
et elles ne peuvent pas être produites autrement qu'en déroulant le TP : ce sont des captures de
gestes dans la zone de dessin.

**Faire ce relevé, c'est aussi tester le TP.** Si à un moment tu ne sais pas quoi cliquer, note-le :
c'est là qu'un élève lèvera la main, et c'est le seul chiffre qui compte (voir la fin de
`verif_guidage.py`).

Toutes les images vont dans `Images/`, avec **exactement** le nom indiqué.

| Nom du fichier | Palier | Ce qu'il faut avoir à l'écran |
|---|---|---|
| `tp5e_01_creer_document.png` | 1 — Ranger avant de commencer | La fenêtre Nouveau document d'Onshape, avec le champ Nom du document, la zone Étiquettes et le choix de l'emplacement. |
| `tp5e_02_esquisse_plan.png` | 2 — Esquisser le carré | Le panneau Esquisse 1 ouvert, le champ Plan d'esquisse vide, et le message Sélectionnez un plan d'esquisse au centre de la zone graphique. |
| `tp5e_03_rectangle_centre.png` | 2 — Esquisser le carré | Le menu déroulant de l'outil rectangle ouvert, montrant Rectangle par sommet, Rectangle à partir du centre et Rectangle aligné. |
| `tp5e_04_cotation.png` | 2 — Esquisser le carré | La cote en cours de placement sur le côté supérieur du rectangle, avec la case de saisie ouverte affichant une valeur décimale. |
| `tp5e_05_carre_50.png` | 2 — Esquisser le carré | Le carré de 50 mm sur 50 mm, entièrement en noir, avec ses deux cotes affichées. |
| `tp5e_R1_carre.png` | 2 — Esquisser le carré | **Résultat du palier.** Vue en perspective : le carré de 50 mm posé sur le plan horizontal, esquisse validée, aucune matière encore créée. |
| `tp5e_06_extruder.png` | 3 — Donner du volume : l'extrusion | Le panneau Extruder ouvert, avec le champ Profondeur, et l'aperçu du volume qui sort du carré. |
| `tp5e_R2_cube.png` | 3 — Donner du volume : l'extrusion | **Résultat du palier.** Le cube de 50 mm de côté, en perspective, sur les trois plans de référence. |
| `tp5e_07_cercle_cote.png` | 4 — La face du 1 — un cercle et un creux | Le cercle centré sur la face supérieure du cube, avec ses deux cotes de 25 mm depuis les bords. |
| `tp5e_08_enlevement.png` | 4 — La face du 1 — un cercle et un creux | Le panneau Extruder réglé sur Enlever, profondeur 5 mm, avec l'aperçu du creux dans la face supérieure. |
| `tp5e_R3_face1.png` | 4 — La face du 1 — un cercle et un creux | **Résultat du palier.** Le cube avec un unique creux circulaire au centre de sa face supérieure. |
| `tp5e_R4_face6.png` | 5 — La face du 6 | **Résultat du palier.** La face à six creux, en deux colonnes de trois, régulièrement espacés. |
| `tp5e_R5_de_complet.png` | 6 — Les quatre faces qui restent | **Résultat du palier.** Le dé complet en perspective, ses six faces percées, faces opposées sommant à 7. |
| `tp5e_09_conge.png` | 7 — Adoucir : les congés | Le panneau Congé ouvert avec un rayon de 3 mm, plusieurs arêtes du cube sélectionnées et l'aperçu arrondi. |
| `tp5e_R6_conges.png` | 7 — Adoucir : les congés | **Résultat du palier.** Le dé aux douze arêtes arrondies, points bien visibles. |
| `tp5e_R7_de_colore.png` | 8 — 🎁 Ton dé, et pas celui du voisin | **Résultat du palier.** Le dé terminé, coloré, prêt à être exporté. |

## Comment cadrer

Cadre **serré sur ce qui compte** : le panneau et la zone concernée, pas tout l'écran. Une capture
pleine résolution d'un écran 4K rend le bouton illisible sur le vidéoprojecteur.

Pour les images de **résultat**, au contraire : vue d'ensemble en perspective, pièce entière,
fond neutre. L'élève doit pouvoir comparer d'un coup d'œil.

## Une fois les images en place

```bash
python3 _generation/build_tp.py scenarios/tp_5e_de_onshape.json
python3 verif_guidage.py tp_5e_de_onshape.html
```

Le TP se réassemble avec les images, et le vérificateur repasse les onze règles.
