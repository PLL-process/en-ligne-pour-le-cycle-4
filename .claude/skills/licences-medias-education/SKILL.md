---
name: licences-medias-education
description: Choisir, documenter et attribuer correctement chaque média (image, SVG, PDF, vidéo) d'un lot, et tenir SOURCES_MEDIAS.md. À utiliser dès qu'un média entre dans une séquence, sans exception.
---

# Licences des médias éducatifs

Mis à jour le 23/10/2026 (inventaire des skills) : aligné sur le journal jusqu'à la règle d'or n°311.

Le journal (`JOURNAL_DES_DECISIONS.md`) fait foi (règle n°10) : les règles citées ici y sont en entier.

## Ordre de préférence obligatoire

1. SVG original créé pour la séquence (Inkscape ou code) ;
2. photographie personnelle de Pascal ;
3. domaine public ; 4. CC0 ; 5. CC BY ; 6. CC BY-SA.

« Accessible gratuitement » ≠ « librement réutilisable ». Jamais d'image
« trouvée dans Google Images ». Jamais d'illustration de manuel (Nathan ou
autre). Pas de hotlinking : télécharger dans `Images/` quand la licence le
permet. Une photo libre est bienvenue si sa licence est vérifiée à la source,
le fichier téléchargé et l'attribution complète (précision de la règle n°1,
journal du 30/07/2026).

## Documents d'éditeur : un lien, pas une copie

Un document d'éditeur ne se rediffuse pas sans droit établi ; on met un lien vers
l'éditeur. Même gratuit, même téléchargé avec un compte enseignant : le droit de
l'imprimer pour sa classe n'est pas le droit de le publier.

Cas de référence (arbitrage A5, clos le 23/10/2026) : le cahier *Si alors — Cahier
d'activités Pix Collège (2026)* et l'affiche *L'écologie du numérique* (© Delagrave)
étaient versionnés et publiés. Droit non établi : retirés du dépôt ;
`_ressources-communes/README.md` renvoie aux pages de l'éditeur. Citer un ouvrage
comme source d'inspiration reste permis : ce n'est pas le rediffuser.

## SOURCES_MEDIAS.md — une entrée par média

nom du fichier · description · auteur · source · URL de la page source ·
licence · date de consultation · modifications effectuées · attribution à
afficher. Les SVG originaux y figurent aussi (auteur : écosystème
Pascal/Claude, licence choisie par Pascal).

**Capture d'écran** (règle d'or n°94, 21/08/2026) : elle vient du vrai logiciel,
exécuté sur le poste, avec le programme réellement construit. Sa ligne dit
**« Capture d'écran réelle »**, avec le logiciel, la date et le poste. Une
reconstitution se déclare comme telle (image, légende, `alt`), sauf pour des blocs.

**Capture de blocs** (règle d'or n°308, 18/10/2026) : un bloc ne se dessine pas, il
se capture. Fichier `bloc_vitta_*.png`, 300 Ko au plus, `alt` qui dit le programme en
mots, et une ligne « Capture d'écran réelle » dans le `SOURCES_MEDIAS.md` du dossier
ou d'un dossier parent. `_outils/controle_blocs_dessines.py` (critère D3) refuse sinon.
Modèle : `_archive-anciennes-versions/…/3e_C9.1/SOURCES_MEDIAS.md`.

## Exigences par image

- Nom de fichier explicite, taille optimisée (< 300 Ko sauf justification, WebP/PNG selon contenu), légende si informative, version SVG dès que le contenu est schématique.
- **`alt` court, description longue à côté** (règle d'or n°117, 21/08/2026) : l'`alt` dit la fonction de l'image en une phrase ; la description détaillée vit dans un volet dépliable à côté de l'image, ouvert à tous. Chronogrammes, câblages et algorigrammes reçoivent en plus un équivalent en tableau.
- **Agrandissement** (règle d'or n°92, 11/08/2026) : toute image d'une page élève s'agrandit d'un clic ou d'Entrée, et se referme par Échap, sans bibliothèque ni réseau. Outil : `theme-3-creation-conception-realisation-innovations/audit/loupe.py <dossier>` (bloc `loupe-images-v1`). L'agrandissement montre l'`alt` en légende : un `alt` creux se voit. Défaut connu du bloc v1 : un `alt` long fait recouvrir l'image par sa légende (journal du 24/09/2026) ; le bloc corrigé `loupe-images-v2` est prévu, pas encore posé.
- Schémas techniques : scientifiquement justes, symboles compréhensibles, information/énergie/matière/action distinguées, lisibles en niveaux de gris imprimés. Chaîne d'énergie : skill `chaine-energie-fonctionnelle`.

## Contrôles

- `python3 _outils/controle_medias.py` : refuse un média dans un dossier sans `SOURCES_MEDIAS.md`, et une image promise par un manifeste mais absente. Il compte sans refuser les médias non nommés et les images qu'aucune page n'affiche (à trancher, pas à deviner). Il ne juge ni poids, ni format, ni qualité. État au 23/10/2026 : vert ; 20 images orphelines dans 5 lots.
- `python3 _outils/controle_blocs_dessines.py` : captures de blocs (ci-dessus).

## Cas connus du dépôt

- Résolus, vérifiés sur le disque et dans git le 23/10/2026 :
  - `4e_C4.7/Images/*_hd.jpg` (8) et `doc3_schema_parcours.png` (extrait de manuel) : retirés le 31/08/2026 (commit `e1503c8`). Leur retrait, annoncé depuis le 11/08, n'avait pas eu lieu : règle d'or n°276, « une suppression annoncée au passé n'est pas une suppression ». Vérifier sur le disque avant d'écrire « retiré ».
  - `5e_C1.3/Images/image_extraite_01` à `08.png` : PNG lourds à la licence mal documentée, le 08 un extrait de manuel ; retirés (01 à 07 le 25/07/2026 ; 08, oublié, le 31/08/2026, commit `bbd1962`). Le dossier ne porte plus que des SVG.
  - Captures de `3e_C9.1` : documentées (captures réelles du 04/10/2026). Celles de la ressource héritée sont archivées avec elle (`_archive-anciennes-versions/…/3e_C9.1/`), sans licence écrite ; l'archive est hors de `controle_medias.py`.
  - Les SVG originaux de `4e_C4.7`, dessinés pour remplacer ces images tierces, sont de nouveau affichés par les QCM du lot (journal du 02/09/2026, règle d'or n°279) ; `4e_C4.7` est sorti de la liste des orphelines.
  - PDF Delagrave : voir « Documents d'éditeur ». Ils restent dans l'historique git : Pascal a décidé le 24/10/2026 de garder l'historique tel quel (journal, entrée « Décision 1 tranchée »). Ne pas proposer de nouveau de le réécrire, sauf si un ayant droit le demande.
- Encore ouvert : les 20 images orphelines relevées par `controle_medias.py` (5 lots, dont les captures de l'atelier CAO). Chaque lot se tranche dans sa propre PR.

## Critères de réussite

- Chaque média du lot a son entrée SOURCES_MEDIAS.md AVANT la remise ; `controle_medias.py` vert.
- Aucun média `LICENCE À VÉRIFIER` dans un fichier destiné à publication sans signalement explicite dans le rapport de lot.
- Aucun document d'éditeur versionné sans droit de rediffusion écrit.
- Chaque capture d'écran déclarée « Capture d'écran réelle » ; `controle_blocs_dessines.py` sans refus.

## Usage pédagogique des images — RÈGLE v2 (décision Pascal, 22/07/2026 ; règle d'or n°1, en vigueur)

L'image est un outil d'apprentissage à part entière au cycle 4 (double codage
texte+visuel, soutien aux lecteurs fragiles, allophones et profils DYS,
entraînement à la lecture de documents techniques exigée au DNB). Les agents
sont donc ENCOURAGÉS à utiliser des images, selon trois usages :

1. **IMAGE-OBJET** : l'image est ce sur quoi porte la question ou l'activité
   (schéma à compléter, courbe à interpréter, composant à identifier, table à
   lire). Usage prioritaire — dans les QCM, viser 6 à 8 questions illustrées
   (pas nécessairement toutes : l'alternance maintient l'attention).
2. **IMAGE-EXPLICATION** : l'image accompagne une correction ou une synthèse
   pour MONTRER la réponse au lieu de seulement la dire.
3. **IMAGE-CONTEXTE** : une illustration d'ambiance est tolérée en ouverture de
   séquence (situation déclenchante) si elle installe le contexte réel du
   problème — jamais au milieu d'un exercice.

Reste interdit : l'image purement décorative posée à côté d'une question ou
d'un calcul (effet « détail séduisant » : elle détourne l'attention de la
notion) ; l'image qui REMPLACE une explication écrite ; toute image sans alt
pertinent ; les sources illicites (section licences ci-dessus, inchangée).

**Critère de contrôle de fin de lot** : pour chaque image, répondre OUI à au
moins une de ces questions — « l'élève doit-il la LIRE pour répondre ? »,
« aide-t-elle à COMPRENDRE la correction ? », « installe-t-elle le CONTEXTE de
la situation déclenchante ? ». Sinon, l'image est retirée.
