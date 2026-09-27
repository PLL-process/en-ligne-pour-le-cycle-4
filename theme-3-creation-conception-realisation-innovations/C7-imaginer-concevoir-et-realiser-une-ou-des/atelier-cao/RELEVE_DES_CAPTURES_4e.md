# Relevé des captures — TP 4e « Le dé sur sa pointe »

Le TP a été réécrit le 27/09/2026 d'après le modèle de référence du professeur
(document Onshape « de-4e-GJEP-dore »). Les captures déjà prises pour l'ancien TP sont
réutilisées quand le geste est le même ; **25 captures restent à prendre**, en déroulant le TP
dans un document neuf « Dé sur sa pointe — Camille », interface française, thème sombre.

Toutes vont dans `Images/`, avec **exactement** le nom indiqué. Les gestes marqués VERIF dans
le scénario (polygone circonscrit, arc, Dériver, rotation de Transformer, Booléen) sont à
confirmer à l'écran : si le libellé diffère, on corrige le scénario, pas la capture.

## À prendre

| Nom du fichier | Palier | Le geste qui l'amène | Ce qu'il faut voir |
|---|---|---|---|
| `dsp_01_document_neuf.png` | Séance 1 · Ranger avant de commencer | Écris Dé sur sa pointe — TON NOM, puis valide avec Créer. | Le document « Dé sur sa pointe — Camille » ouvert, vide. |
| `dsp_02_variable_studio_vide.png` | Séance 1 · Le nombre d'or dans une boîte à variables | En bas, clique sur le +, puis sur Créer un Variable Studio. Renomme l'onglet Nombre d'or. | Le Variable Studio vide, prêt à recevoir des variables. |
| `dsp_03_variable_phi.png` | Séance 1 · Le nombre d'or dans une boîte à variables | Crée la variable phi et donne-lui pour valeur (1 + sqrt(5)) / 2. | La variable phi avec la formule (1 + sqrt(5)) / 2 et sa valeur 1,618. |
| `dsp_04_variables_toutes.png` | Séance 1 · Le nombre d'or dans une boîte à variables | Crée de la même façon, dans cet ordre, les variables suivantes : M = 89 mm · C = #M / #phi | Le Variable Studio rempli : phi, M, C, Hsocle, Rsocle, Rde, penetr et leurs valeurs. |
| `dsp_05_octogone_trace.png` | Séance 1 · La plinthe octogonale | Ouvre la flèche de l'outil polygone et choisis le polygone circonscrit (VERIF nom exact).  | L'octogone régulier tracé autour de l'origine, son cercle de construction à l'intérieur. |
| `dsp_06_octogone_cote.png` | Séance 1 · La plinthe octogonale | Avec l'outil Cote (touche d), cote le diamètre du cercle de construction et tape #M. | L'octogone coté #M, entièrement blanc. |
| `dsp_07_extruder_plinthe.png` | Séance 1 · La plinthe octogonale | Valide l'esquisse. Clique sur Extruder, choisis Nouveau, profondeur #Hsocle, et clique sur | Le panneau Extruder : Nouveau, profondeur #Hsocle, direction vers le bas, et l'aperçu de la dalle. |
| `dsp_R1_plinthe.png` | Séance 1 · La plinthe octogonale | — résultat du palier — | La plinthe : une dalle octogonale régulière, vue en perspective. |
| `dsp_08_profil_moulure.png` | Séance 1 · Le profil de la moulure | À droite de l'axe, trace le contour avec l'outil Ligne et deux Arcs (VERIF outil arc centr | Le profil de la moulure coté : 35, 19, et les deux arcs de rayon 5 et 3, contre l'axe de construction. |
| `dsp_R2_profil.png` | Séance 1 · Le profil de la moulure | — résultat du palier — | Le profil de la moulure entièrement blanc, posé contre l'axe, au-dessus de la plinthe. |
| `dsp_09_pivoter_moulure.png` | Séance 1 · Faire tourner la moulure, adoucir la plinthe | Valide l'esquisse, clique sur Pivoter, choisis Ajouter, sélectionne l'intérieur du profil  | Le panneau Pivoter en mode Ajouter, et l'aperçu du corps mouluré sur la plinthe. |
| `dsp_10_conge_plinthe.png` | Séance 1 · Faire tourner la moulure, adoucir la plinthe | Clique sur Congé, sélectionne les huit arêtes verticales de la plinthe et tape #Rsocle pou | Le panneau Congé, rayon #Rsocle, les huit arêtes verticales de la plinthe sélectionnées. |
| `dsp_R3_socle.png` | Séance 1 · Faire tourner la moulure, adoucir la plinthe | — résultat du palier — | Le socle fini : plinthe octogonale aux angles arrondis, surmontée du corps mouluré. |
| `dsp_11_deriver_de.png` | Séance 2 · Faire venir le dé | Reviens dans l'onglet Presse-papier. Clique sur Dériver (VERIF nom et emplacement de l'out | Le dé dérivé dans le Presse-papier, centré sur l'origine, traversant le socle. |
| `dsp_R4_de_centre.png` | Séance 2 · Faire venir le dé | — résultat du palier — | Le dé à calottes, centré sur l'origine, qui traverse le socle. |
| `dsp_12_esquisse_axes.png` | Séance 2 · Mettre le dé sur sa pointe | Crée une Esquisse sur le plan Top et trace deux lignes passant par l'origine : une horizon | Deux lignes perpendiculaires se croisant à l'origine, sur le plan Top. |
| `dsp_13_rotation_45.png` | Séance 2 · Mettre le dé sur sa pointe | Clique sur Transformer, choisis le type rotation (VERIF libellé), sélectionne le dé, puis  | Le panneau Transformer en rotation, angle 45, et le dé posé sur une arête. |
| `dsp_14_rotation_35.png` | Séance 2 · Mettre le dé sur sa pointe | Ajoute un second Transformer en rotation, sur le dé, autour de la ligne verticale, angle 3 | Le second Transformer, angle 35.2644, et le dé dressé sur sa pointe. |
| `dsp_R5_de_pointe.png` | Séance 2 · Mettre le dé sur sa pointe | — résultat du palier — | Le dé dressé sur un de ses coins, vu de face : il est symétrique de part et d'autre de l'axe. |
| `dsp_15_translation.png` | Séance 2 · Poser le dé sur le socle | Ajoute un Transformer, type Translater en XYZ, sur le dé. Laisse X et Y à 0, et dans Z tap | Le panneau Transformer, Translater en XYZ, la formule dans Z, et le dé posé sur le socle. |
| `dsp_R6_de_pose.png` | Séance 2 · Poser le dé sur le socle | — résultat du palier — | Le dé posé sur sa pointe au sommet du socle mouluré, vu de face. |
| `dsp_16_booleen_empreinte.png` | Séance 2 · Creuser l'empreinte | Clique sur Booléen (VERIF), choisis Soustraire. Dans Outils, le dé ; dans Cibles, le socle | Le panneau Booléen en Soustraire : outils le dé, cibles le socle, décalage 0.25, garder les outils. |
| `dsp_17_empreinte_vue.png` | Séance 2 · Creuser l'empreinte | Masque le dé (clic droit, Masquer) pour regarder le creux, puis réaffiche-le. | Le socle seul, dé masqué : le creux laissé par la pointe du dé. |
| `dsp_R7_empreinte.png` | Séance 2 · Creuser l'empreinte | — résultat du palier — | Le socle vu de dessus, dé masqué : l'empreinte de la pointe au centre. |
| `dsp_R9_presse_papier.png` | 🎁 Séance 3 · Ton presse-papier, et pas celui du voisin | — résultat du palier — | Le presse-papier fini : le dé doré posé sur sa pointe, au sommet du socle octogonal couleur pierre. |

## Déjà en place (réutilisées de l'ancien TP)

- `tp4e_01_menu_creer.png` — Séance 1 · Ranger avant de commencer
- `tp4e_04_onglet_menu.png` — Séance 1 · Ranger avant de commencer
- `tp4e_05_esquisse_plan.png` — Séance 1 · La plinthe octogonale
- `tp4e_06_plan_front.png` — Séance 1 · Le profil de la moulure
- `tp4e_08_bouton_construction.png` — Séance 1 · Le profil de la moulure
- `tp4e_14_bouton_pivoter.png` — Séance 1 · Faire tourner la moulure, adoucir la plinthe
- `tp4e_18_bouton_conge.png` — Séance 1 · Faire tourner la moulure, adoucir la plinthe
- `tp4e_22_menu_plus.png` — Séance 2 · Faire venir le dé
- `tp4e_32_menu_exporter.png` — Séance 3 · Emporter son travail : exporter, retrouver
- `tp4e_34_liste_formats.png` — Séance 3 · Emporter son travail : exporter, retrouver
- `tp4e_35_options_export.png` — Séance 3 · Emporter son travail : exporter, retrouver
- `tp4e_R8_export_stl.png` — Séance 3 · Emporter son travail : exporter, retrouver
- `tp4e_42_apparence_de.png` — 🎁 Séance 3 · Ton presse-papier, et pas celui du voisin
- `tp4e_38_unites_gramme.png` — 🎁 Séance 3 · Ton presse-papier, et pas celui du voisin
- `tp4e_36_materiau_bronze.png` — 🎁 Séance 3 · Ton presse-papier, et pas celui du voisin
- `tp4e_39_masse_socle_bronze.png` — 🎁 Séance 3 · Ton presse-papier, et pas celui du voisin

## Valeurs à retrouver à l'écran

- Variables : φ ≈ 1,618 ; C ≈ 55,005 mm ; Hsocle ≈ 12,985 mm ; Rsocle = penetr ≈ 4,960 mm ; Rde ≈ 8,025 mm.
- Octogone : 89 mm sur plats, côté ≈ 36,87 mm.
- Rotations : 45°, puis 35,2644° ; translation Z ≈ 55,80 mm.
- Empreinte : ≈ 558,5 mm³ sans jeu (un peu plus avec 0,25 mm).

## Une fois les images en place

```bash
python3 _generation/build_tp.py scenarios/tp_4e_socle_assemblage.json
python3 verif_guidage.py tp_4e_socle_assemblage.html
```
