# Sources — Atelier CAO (Onshape)

## Les documents qui ont servi de source, et qui ne sont PAS redistribués ici

**Le TP « Dé » de Pascal Gouacide** (SolidWorks, usage en classe). Il a servi de **modèle de
forme** : c'est de lui que sont tirées les règles d'or n°72 à n°82. Aucune de ses phrases n'est
reprise. Il reste sa propriété.

**« Cours de modélisation 3D sur www.Onshape.com »**, Gaëtan Bussy et Hélène Carrel,
FabLab-Neuch et FabLab Ici Autour, septembre 2017, 28 pages. Consulté pour **vérifier des faits**
sur l'interface — les modes de l'outil rectangle et de l'outil cercle, le raccourci clavier qui
oriente le plan face à l'écran, la sortie d'un outil de dessin. Ce document **n'est pas
redistribué** dans le dépôt et aucune de ses images n'est reprise : ses captures datent de 2017 et
sont **en anglais**, alors que l'interface du collège est en français (règle d'or n°70).

C'est un bon manuel de **référence** — un outil par page — là où notre TP est un **parcours guidé**.
Les deux ne se remplacent pas. L'enseignant qui veut la liste complète des fonctions le trouvera
auprès du FabLab-Neuch ; l'élève qui veut construire son dé suit notre TP.

## Ce qui a été vérifié dans ce document, et repris comme fait

- l'outil **rectangle** propose bien « par sommet » et « à partir du centre » ;
- l'outil **cercle** propose « à partir du centre », « par 3 points » et « ellipse » ;
- la touche **N** oriente le plan d'esquisse face à l'écran ;
- **Échap** quitte un outil de dessin resté actif ;
- une **face d'un volume** peut servir de plan d'esquisse.

Ces cinq faits sont désormais dans le TP de 5e, écrits avec nos mots et les libellés français de
l'interface actuelle.

## Les images du dossier

`Images/presse_papier_vues.png` — rendu de notre propre modèle, produit par
`_modele/presse_papier.py`. Original, CC0.

Les seize captures du TP de 5e restent **à produire** : voir `RELEVE_DES_CAPTURES_5e.md`. Elles
devront être prises sur l'interface **française** du poste du collège (règle n°70).

## Images de résultat du TP 5e « Le dé » (10 août 2026)

`Images/tp5e_R2_cube.png` · `tp5e_R3_face1.png` · `tp5e_R4_face6.png` ·
`tp5e_R5_de_complet.png` · `tp5e_R6_conges.png` · `tp5e_R7_de_colore.png`

**Origine** : rendus ombrés produits par l'**API Onshape** (`/shadedviews`) à partir d'un
modèle construit pour ce dépôt — cube de 50 mm, 21 creux Ø 10 profondeur 5, congés 3 mm.
Ce ne sont **pas** des captures d'écran du logiciel : aucune interface, aucun élément
d'habillage Onshape n'y figure. 1600×1200, fond aplati sur blanc.

**Licence** : géométrie et rendus créés pour ce dépôt, réutilisables sous la licence du
dépôt. Le modèle de référence reste ouvert dans le compte Onshape Éducateur de l'auteur.

**Contrôle exécuté** : comptage des cylindres de rayon 5 mm par face relevé sur la pièce
(1 · 6 · 2 · 5 · 3 · 4, paires opposées à 7), recoupé à l'œil sur les six vues
orthogonales ; encombrement 50 × 50 × 50 mm ; volume avant congés 116 753,3 mm³, soit
exactement 125 000 − 21 × π × 5² × 5.

**Non produites par l'API, et non simulées** : `tp5e_R1_carre.png` (esquisse sans matière)
et les neuf captures d'interface `tp5e_01` à `tp5e_09` — elles doivent montrer les panneaux
d'Onshape **en français** (règle d'or n°70).

## Les seize rendus produits le 11 août 2026 (les TP de 5e, 4e et 3e d'alors)

`Images/tp5e_R6_conges.png` · `tp5e_R7_de_colore.png` · `tp4e_R1_profil.png` →
`tp4e_R7_presse_papier.png` · `tp3e_R1_bloc.png` → `tp3e_R7_boitier_fini.png`

**Origine** : rendus ombrés produits par l'**API Onshape** (`/shadedviews`) à partir de modèles
construits pour ce dépôt. Ce ne sont **pas** des captures d'écran du logiciel : aucune interface,
aucun élément d'habillage Onshape n'y figure. Fond aplati sur blanc.

**Licence** : géométrie et rendus créés pour ce dépôt, réutilisables sous sa licence.

**Contrôles exécutés, relevés sur la pièce et non sur l'intention.**
Le dé : 21 creux répartis 1 · 6 · 2 · 5 · 3 · 4, paires opposées à 7, comptés depuis les arêtes
puis recoupés par les 21 tores du congé de 1 mm et par les 21 fonds plans d'aire 78,5398 mm² =
π·5². Volume final 115 482,72 mm³ — le chiffre de 116 753 mm³ noté précédemment était le volume
**avant** congés.
Le socle : Ø 140 × 35, volume 538 783,1401 mm³ = π·70²·35 exactement, avant congés.
Le centrage du dé : écart entre l'axe du socle et le centre du dé = **0,00 mm**, débord 45,00 mm
sur les quatre côtés, base du dé à z = 35,00 = dessus du socle. Le dé est tenu par une contrainte
d'assemblage résolue, pas par des coordonnées saisies.
La coque : 27 552,000000000004 mm³ contre 80·60·35 − 76·56·33 = 27 552 attendus.
La gorge : son fond est **une seule face** de 136,00 mm², exactement l'aire de l'anneau complet —
c'est la preuve qu'elle fait le tour **sans interruption**. Le sommet de nervure est lui aussi une
face unique de 136,00 mm².
Le jeu du joint : fond de gorge z = 33,50, sommet de nervure z = 34,00 → **0,50 mm**.

**Trois limites déclarées.**
`tp3e_R6_assemblage_coupe.png` **n'est pas une coupe des pièces de production** : l'API publique
d'Onshape ne sait pas produire de vue en coupe, et l'on ne peut pas booléiser dans un assemblage.
Les deux pièces ont donc été reconstruites dans un Part Studio dédié, puis un demi-espace
soustrait. L'équivalence est prouvée au volume (boîtier 27 113,413844746257 contre
27 113,41384474628 pour la pièce réelle ; couvercle 14 536,0 des deux côtés), mais c'est une
reconstruction.
`tp4e_R1_profil.png` n'est pas un rendu Onshape : `/shadedviews` ne montre pas les esquisses.
L'image est tracée à partir de l'esquisse réelle lue par l'API — les cotes 70 et 35 et la ligne de
construction y sont — mais son habillage est celui du traceur, pas de l'interface.
`tp3e_R5_couvercle.png` est honnête et peu démonstratif : la nervure de 1 mm est continue et
traçable sur les quatre côtés, mais à l'échelle du couvercle entier elle reste un mince liseré.

**Non produites par l'API, et non simulées** : `tp5e_R1_carre.png` (une esquisse sans matière ne
se rend pas ombrée) et les neuf captures d'interface `tp5e_01` à `tp5e_09`, qui doivent montrer
les panneaux d'Onshape **en français** (règle d'or n°70).


## Le dessin de coupe du TP « Le dé, en mieux » (30 août 2026)

`Images/coupe_calotte_5e.svg`

**Origine** : dessin vectoriel **engendré** par `../5e/5e_C7.2/calotte.py`, fonction
`dessin_coupe()`. Ce n'est ni une capture d'écran ni un rendu : c'est un tracé calculé, où
chaque cote provient du modèle géométrique et non d'un report à la main. Relancer le script
redessine le fichier à l'identique.

**Ce qu'il montre** : la face du 1 en coupe, l'ancien creux (cylindre Ø10 à fond plat, arête
vive) à gauche, la calotte à droite, la bille de Ø20 en pointillés et la hauteur de son centre.

**Contrôles, relevés sur le modèle et non sur l'intention.** Bille Ø20, profondeur 1,5 mm →
centre à 10 − 1,5 = **8,5 mm** au-dessus de la face ; largeur de la calotte
2·√(10² − 8,5²) = **Ø10,54**, soit 0,54 mm de plus que le cylindre qu'elle remplace. Volume
retiré : 67,2 mm³ contre 117,8 mm³ pour le cylindre, **43 % de moins**. Le cylindre ne devient
plus large que la calotte qu'à partir de 0,16 mm de profondeur.

**Licence** : tracé créé pour ce dépôt, réutilisable sous sa licence.

**Limite déclarée** : ce dessin est le **seul** média du quatrième TP, et il sert à trois
paliers sur huit. Les cinq autres n'ont aucune image de résultat — la règle n°77 refuse donc ce
TP, et `RELEVE_DES_CAPTURES_5e-bis.md` dit lesquelles prendre.

## Les 74 captures des quatre TP — famille documentée le 31/08/2026

`_outils/controle_medias.py`, livré le 31/08/2026, relevait que ce dossier portait
**74 fichiers** — 31 Mo — que ce document ne nommait pas un par un. Les voici comme
**famille**, ce qui est la seule façon honnête de parler d'eux : les nommer un par un
donnerait soixante-quatorze lignes identiques, et cacherait la seule question qui compte.

| Préfixe | Nombre | Ce que ce sont |
|---|---|---|
| `p4_…` à `p9_…` | 36 | les captures de gestes, palier par palier, du TP 5e « Le dé » |
| `tp3_…`, `tp4_…`, `tp5e_…` | 36 | les captures des TP 3e, 4e et de la reprise 5e |
| `r2_…` | 2 | deux rendus de résultat |

**Origine** : ce sont des **captures de l'interface d'Onshape**, prises en déroulant les TP sur
un poste dont l'interface est en **français** (règle d'or n°70), et recadrées sur la zone utile.
Elles ne sont ni téléchargées, ni tirées d'un manuel, ni reprises du document FabLab-Neuch cité
plus haut — dont ce fichier explique justement pourquoi il n'est **pas** redistribué.

**La question qui reste, et qu'on ne tranche pas à la place de Pascal.** Une capture d'écran
montre l'interface d'un logiciel tiers. Le geste de l'élève, le modèle, le cadrage et la
légende sont à nous ; les icônes et la disposition d'Onshape sont à Onshape. Publier ces
captures sur un dépôt ouvert relève de l'usage pédagogique, mais **ce n'est pas à un contrôle
automatique d'en décider** — pas plus qu'à l'agent qui écrit cette ligne.

Deux voies, à trancher :

1. **on assume l'usage pédagogique** — c'est la position implicite depuis août 2026, et il
   suffit alors de l'écrire ici noir sur blanc pour que la question soit close ;
2. **on demande à Onshape** — la plupart des éditeurs autorisent explicitement les captures
   à des fins d'enseignement, et une ligne de leur part vaut mieux qu'une présomption.

En attendant, les fichiers restent, leur origine est écrite, et personne ne pourra dire qu'on
ne savait pas.

### L'inventaire, nom par nom
Écrit en toutes lettres pour deux raisons : un contrôle qui vérifie la présence d'un nom ne
peut rien faire d'un préfixe, et une capture ajoutée demain sans sa ligne doit réveiller ce
contrôle. Toutes ont la même origine et la même réserve que ci-dessus.

**TP 5e « Le dé », palier par palier (préfixes p4 à p9)** — 36 fichiers, 24819 Ko :
- `Images/p4_01_esquisse_face.png`
- `Images/p4_01b_face_a_plat.png`
- `Images/p4_01c_vue_normale_touche_N.png`
- `Images/p4_02_outil_cercle.png`
- `Images/p4_02b_cercle_trace.png`
- `Images/p4_03_cote_gauche.png`
- `Images/p4_04_cote_haut.png`
- `Images/p4_05_cote_diametre.png`
- `Images/p4_06_extrudeur.png`
- `Images/p4_07_zone_choisie.png`
- `Images/p4_08_retraite_1mm5.png`
- `Images/p4_08a_erreur_virgule.png`
- `Images/p4_M_mesures_controle.png`
- `Images/p4_R_face1.png`
- `Images/p5_01_face_opposee.png`
- `Images/p5_02_six_cercles.png`
- `Images/p5_03_cotes_posees.png`
- `Images/p5_03a_esquisse_non_resolue.png`
- `Images/p5_04_retraite.png`
- `Images/p5_M_mesures_controle.png`
- `Images/p5_Q2_repetition_lineaire.png`
- `Images/p5_R_face6.png`
- `Images/p6_01_face2_esquisse.png`
- `Images/p6_02_face2_cotes.png`
- `Images/p6_04_face5_cotes.png`
- `Images/p6_R_face2.png`
- `Images/p6_R_face3.png`
- `Images/p6_R_face5.png`
- `Images/p7_01_conge3_selection.png`
- `Images/p7_02_conge3_appercu.png`
- `Images/p7_04_conge1_21aretes.png`
- `Images/p8_01_exportateur_menu.png`
- `Images/p8_03_unites_mm.png`
- `Images/p9_01_modifier_apparence.png`
- `Images/p9_05_masse_bronze.png`
- `Images/p9_06_masse_abs.png`

**Rendus de résultat (préfixe r2)** — 2 fichiers, 1938 Ko :
- `Images/r2_mesure_fond_face1.png`
- `Images/r2_mesure_fond_face3.png`

**TP 3e « Boîtier étanche » (préfixe tp3)** — 3 fichiers, 408 Ko :
- `Images/tp3e_R2_coque.png`
- `Images/tp3e_R3_rainure.png`
- `Images/tp3e_R4_passage_cable.png`

**TP 4e « Socle d'assemblage » (préfixe tp4)** — 5 fichiers, 993 Ko :
- `Images/tp4e_R2_socle_brut.png`
- `Images/tp4e_R3_socle_moulure.png`
- `Images/tp4e_R4_deux_pieces.png`
- `Images/tp4e_R5_assemblage_libre.png`
- `Images/tp4e_R6_de_centre.png`

**TP 5e, reprise (préfixe tp5e)** — 28 fichiers, 2852 Ko :
- `Images/tp5e_01_creer_document.png`
- `Images/tp5e_01b_onglets.png`
- `Images/tp5e_01c_nom_saisi.png`
- `Images/tp5e_02_esquisse_plan.png`
- `Images/tp5e_02b_document_vide.png`
- `Images/tp5e_03_rectangle_centre.png`
- `Images/tp5e_03a_plan_haut.png`
- `Images/tp5e_03b_vue_normale.png`
- `Images/tp5e_03c_rectangle_trace.png`
- `Images/tp5e_04_cotation.png`
- `Images/tp5e_04a_double_clic.png`
- `Images/tp5e_04b_clic_simple.png`
- `Images/tp5e_04c_coche_verte.png`
- `Images/tp5e_05_carre_50.png`
- `Images/tp5e_05a_infobulle_extrudeur.png`
- `Images/tp5e_06_extruder.png`
- `Images/tp5e_06a_panneau_vide.png`
- `Images/tp5e_06b_zone_choisie.png`
- `Images/tp5e_06c_piece_creee.png`
- `Images/tp5e_06d_menu_isometrique.png`
- `Images/tp5e_07_cercle_cote.png`
- `Images/tp5e_08_enlevement.png`
- `Images/tp5e_09_conge.png`
- `Images/tp5e_10_exportateur.png`
- `Images/tp5e_11_formats.png`
- `Images/tp5e_12_export_stl.png`
- `Images/tp5e_13_retrouver.png`
- `Images/tp5e_15_bibliotheque_materiaux.png`
