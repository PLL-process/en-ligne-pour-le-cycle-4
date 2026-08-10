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

