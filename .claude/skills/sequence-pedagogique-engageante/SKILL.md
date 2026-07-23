---
name: sequence-pedagogique-engageante
description: Construire une séquence de technologie cycle 4 conforme au gabarit du dépôt (modèle « Jardin connecté » 4e_C6.2 amélioré). À utiliser pour toute création ou refonte de séquence, avant d'écrire la moindre ligne de HTML.
---

# Séquence pédagogique engageante (gabarit du dépôt)

## Référence

`theme-2-…/4e/4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html`
= gabarit minimal. Les améliorations obligatoires par rapport à ce modèle :
note /20 à pondération paramétrable (constantes JS nommées), sauvegarde locale +
exports, séparation élève/professeur/inspection, `SOURCES_MEDIAS.md`,
navigation clavier complète, étiquetage des versions A/B/C.

## Structure obligatoire (ordre)

1. **Identification** : titre engageant, niveau, thème, compétence + code
   principal, compétences associées, durée, nb séances, prérequis, matériel,
   logiciels, modalités, version/date.
2. **Situation déclenchante** : concrète, crédible, sans solution donnée,
   illustrée (SVG original de préférence). Contextes à privilégier quand
   pertinents (jamais plaqués) : le collège, Sainte-Luce, Fort-de-France, la
   Martinique, cyclones, solaire, eau, agriculture, objets connectés,
   cybersécurité, robotique, réparation, mobilités, réseaux.
3. **Problématique** ouverte + un problème intermédiaire par séance.
4. **Mission** explicite + production attendue nommée.
5. **Référentiel** : compétence officielle, code, associées, connaissances,
   capacité observable, niveau de maîtrise, socle, CRCN, EDD (± EMI/EMC/orientation).
6. **Déroulement** par séance : question directrice, durée, objectif,
   organisation, matériel, consignes, activités alternées (observation →
   investigation → manipulation/simulation → conception → test → argumentation),
   productions intermédiaires, aides, correction, critères de réussite, transition.
7. **Démarche de projet** (12 étapes : besoin → bilan réflexif) selon le thème.
8. **Synthèse** courte : notions, vocabulaire (mots-clés FR + EN : capteur—sensor,
   actionneur—actuator, réseau—network, donnée—data, boucle—loop…), schéma,
   exemple, erreurs fréquentes, lien vers la séquence suivante.
9. **Différenciation** : aides niveau 1 et 2, fiche guidée, standard,
   approfondissement, sans matériel, simulation, adaptations EBEP. Les aides
   guident sans faire à la place.
10. **Encadré « Choix de l'outil »** + versions A (matériel réel) / B
    (simulation) / C (sans matériel) pour toute séquence matérielle.
11. **Interdisciplinarité** (facultatif, type EPI).

## Interdits

- Recopier un contenu, exercice ou illustration Nathan ou d'un autre éditeur.
- Contexte local artificiel ; questions piège ; humiliation en cas d'erreur ;
  stéréotypes ; matériel non confirmé présenté comme disponible.
- Publier une correction sommative dans une page publique.

## Critères de réussite

- Chaque rubrique 1→10 présente et réellement remplie (pas de section vide).
- Faisable dans un collège : durée réaliste, matériel de
  `inventaire_materiel.csv` ou alternative B/C.
- Cohérence problématique ↔ activités ↔ évaluation vérifiable en relisant
  uniquement ces trois sections.

## Règle d'or « Trois façons de vivre la séquence » (décision Pascal, 23/07/2026 — à entériner au Conseil du 28/07)

Toute séquence mettant en jeu du matériel, un logiciel ou une manipulation
propose — quand c'est possible — un encadré visuel « 🔀 Trois façons de vivre
la séquence » avec trois cartes :

- **🅰 Matériel réel** : la manipulation authentique (matériel confirmé du
  labo, sécurité TBT, protocole) ; tout matériel non confirmé est marqué
  « MATÉRIEL À CONFIRMER — prévoir une alternative par simulation » ;
- **🅱 Simulation / logiciel** : l'équivalent numérique (VittaScience, Filius,
  mBlock, FreeCAD…), gratuit et sans compte obligatoire de préférence ;
- **🅲 Sans matériel** : tout est dans la page (simulateurs HTML intégrés,
  données enregistrées, gabarits imprimables) — AUCUN élève n'est pénalisé
  par l'absence de matériel, y compris à la maison.

Les trois versions visent les MÊMES objectifs d'apprentissage : la version 🅲
n'est jamais un lot de consolation, c'est un chemin complet. L'encadré se place
après « Choix de l'outil », avant les séances (modèle : séquences du Thème 2,
ex. 3e_C4.3 « Station d'alerte cyclonique »). Si une séquence est entièrement
débranchée par nature, l'encadré peut être omis — le signaler dans la fiche
pédagogique.
