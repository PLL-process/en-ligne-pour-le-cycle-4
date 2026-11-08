# Audit des séquences élèves — état intermédiaire vérifié

Date : 1er novembre 2026. Site : https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html

> Ce document est une étape de l'audit, et non un audit exhaustif des 60 pages. Les anomalies sont distinguées des points à vérifier.

## Méthode

Contrôle des textes accessibles publiquement, de l'index, des séquences ciblées et de la cohérence des consignes. Les interactions JavaScript, les performances réelles et les lecteurs d'écran restent à tester dans un navigateur.

## A01 — Couverture mutualisée difficile à identifier — priorité moyenne

- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html
- Emplacement : Thème 1 > C1 > 5e_C1.6 ; Thème 1 > C1 > 3e_C1.2 et 3e_C1.4.
- Constat : l'index indique « Couvert par une séquence mutualisée » tout en affichant « Aucune ressource pédagogique publiée pour ce repère ».
- Risque : l'élève ou l'enseignant ne sait pas quelle séquence ouvrir pour travailler précisément cette compétence.
- Correction : ajouter un lien direct vers la séquence mutualisée et vers la séance ou l'activité pertinente, avec une mention « ressource dédiée absente, compétence traitée dans… ».
- Statut : constat textuel confirmé ; réalité de la couverture pédagogique à examiner dans les séquences.

## A02 — Définition de la précision à nuancer — priorité moyenne

- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.1/sequence_5e_C1.1-C1.6_chengdu_air.html
- Emplacement : « Activité 1 — Une fonction, trois principes » > « Les chiffres pour choisir » et « Les mots de la planche ».
- Constat : le tableau donne des pourcentages ±10 %, ±2 %, ±5 %, puis définit « précision (±10 %) » comme un écart possible à la vraie valeur. Dans une activité pédagogique simulée, ces nombres peuvent fonctionner comme hypothèses, mais ne doivent pas être présentés comme performances universelles des technologies.
- Correction : écrire « incertitude supposée pour cet exercice » et distinguer justesse, fidélité et incertitude à un niveau adapté aux élèves.
- Statut : point de rigueur scientifique confirmé dans la formulation ; pas une preuve que les valeurs simulées sont fausses.

## A03 — Contradiction potentielle sur l'entretien du capteur — priorité moyenne

- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.1/sequence_5e_C1.1-C1.6_chengdu_air.html
- Emplacement : « Les chiffres pour choisir » > ligne « Ce qu'il exige », puis « Correction complète » de l'activité 1.
- Constat : le tableau décrit un boîtier fermé que le collège ne peut pas entretenir ; la correction propose néanmoins de « nettoyer » comme solution à la dérive.
- Correction : remplacer par « prévoir le remplacement du module, une maintenance externe ou un contrôle par une mesure de référence » ; ne mentionner le nettoyage que pour un modèle démontable.
- Statut : incohérence textuelle confirmée.

## A04 — Position de l'échauffement tableur — priorité faible

- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.1/sequence_5e_C1.1-C1.6_chengdu_air.html
- Emplacement : « Avant de commencer (échauffement) — les quatre gestes du tableur ».
- Constat : l'échauffement se trouve après l'activité 1 et avant l'activité 2, et non immédiatement après le « Billet d'entrée ». Ce placement est cohérent si l'échauffement prépare spécifiquement l'activité 2 ; son titre général « Avant de commencer » peut toutefois laisser penser qu'il précède toutes les activités.
- Correction : renommer « Avant l'activité 2 — quatre gestes du tableur » ou le déplacer après le billet d'entrée si l'objectif est une préparation générale.
- Statut : emplacement confirmé ; recommandation éditoriale, pas bug.

## A05 — Attention à la sauvegarde locale — priorité moyenne

- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.1/sequence_5e_C1.1-C1.6_chengdu_air.html
- Emplacement : introduction, sous les boutons « Imprimer », « Effacer ma sauvegarde », « Mode essentiel ».
- Constat : les réponses sont annoncées comme conservées dans ce navigateur uniquement. Sur des postes partagés de collège, cette persistance n'est ni une sauvegarde portable ni une protection contre la consultation par un autre utilisateur du même profil.
- Correction : afficher un avertissement explicite « poste partagé », offrir une exportation locale sans données personnelles et vérifier l'effacement complet.
- Statut : risque d'usage identifié ; implémentation technique non encore testée.

## Points restant à auditer

1. Les séquences des thèmes 2 et 3, notamment jardin connecté, capteurs d'humidité et station d'alerte cyclonique.
2. Les boutons « Vérifier » : validation sémantique, tolérance aux réponses justes, impossibilité de réussir avec du texte arbitraire.
3. Navigation clavier, contrastes, textes alternatifs, zoom 200 %, smartphone/tablette.
4. Vérification des liens, des ressources, des CSV, de l'exécution JavaScript et des sauvegardes.
5. Traçabilité de chaque compétence officielle 2024 jusqu'à une production observable et à son critère d'évaluation.

## Synthèse provisoire

Le site affiche un effort pédagogique réel : compétences explicitées, données simulées signalées, différenciation par phrases amorces, corrections et accompagnement pas à pas. Les premiers correctifs portent surtout sur la traçabilité des ressources mutualisées, la cohérence scientifique des explications et l'usage sur les postes partagés. Aucun score global de qualité n'est attribué tant que l'ensemble des séquences et interactions n'a pas été vérifié.
