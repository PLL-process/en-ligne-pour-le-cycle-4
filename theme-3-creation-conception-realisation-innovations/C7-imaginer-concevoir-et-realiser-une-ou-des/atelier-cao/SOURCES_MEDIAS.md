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
