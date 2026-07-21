# Spécification — badge « NEW » du tableau de bord

## Objectif

Permettre à Pascal de retrouver immédiatement une ressource nouvellement publiée depuis l’adresse permanente :

`https://pll-process.github.io/en-ligne-pour-le-cycle-4/`

Le badge doit guider visuellement jusqu’au thème, à la compétence puis à la ressource concernée, sans exiger la consultation d’une Pull Request.

## Comportement attendu

Lorsqu’une nouvelle ressource est publiée :

1. le thème concerné affiche un badge `NEW` ;
2. la compétence concernée affiche également un badge `NEW` ;
3. le code précis, par exemple `3e_C4.3`, affiche un badge `NEW` ;
4. le lien de la nouvelle ressource reçoit une mise en évidence discrète ;
5. le thème et la compétence concernés peuvent être ouverts automatiquement lorsqu’un lien direct avec ancre est utilisé ;
6. le message envoyé à Pascal indique le code, le titre et l’ancre directe.

## Durée d’affichage

Par défaut, le badge reste visible pendant 21 jours après la publication. Cette durée doit être stockée dans une donnée de configuration et non codée en dur dans plusieurs fichiers.

## Animation et accessibilité

- Animation douce de pulsation, jamais un clignotement rapide.
- Respect de `prefers-reduced-motion` : aucune animation pour les utilisateurs ayant demandé la réduction des mouvements.
- Le texte `Nouveau` doit être disponible pour les lecteurs d’écran.
- L’information ne doit pas reposer uniquement sur la couleur.
- Le badge reste lisible en mode sombre, sur mobile et à l’impression.

## Données proposées

Créer un fichier public léger, par exemple `nouveautes.json`, contenant pour chaque publication :

- `code` ;
- `theme` ;
- `competence` ;
- `titre` ;
- `url` ;
- `date_publication` ;
- `type` (`sequence`, `qcm`, `synthese`, `activite`) ;
- `lot`.

Le générateur de l’index doit utiliser ces données pour poser automatiquement les badges. Aucune modification manuelle répétitive de `index.html` ne doit être nécessaire.

## Accès direct

Chaque code doit avoir une ancre stable, par exemple :

`#3e_C4.3`

Le message de publication pourra alors donner un lien du type :

`https://pll-process.github.io/en-ligne-pour-le-cycle-4/#3e_C4.3`

La page doit ouvrir automatiquement le thème et la compétence contenant cette ancre, puis placer la ressource dans la zone visible.

## Critères de réussite

- un badge visible au niveau du thème, de la compétence et du code ;
- accès en un clic à la nouvelle ressource ;
- fonctionnement sur ordinateur, tablette et téléphone ;
- animation désactivable automatiquement ;
- disparition automatique après la durée prévue ;
- aucune dépendance externe nécessaire ;
- aucune donnée personnelle collectée ;
- fonctionnement hors connexion après chargement de la page ;
- tests automatiques couvrant la date, l’ancre, l’ouverture des sections et l’absence de faux badge.

## Gouvernance

Cette fonctionnalité appartient à la Vague 0 « Fondation — tableau de bord ». Elle doit être développée sur une branche distincte et présentée dans une Pull Request en brouillon. Elle ne doit pas être ajoutée à la Pull Request du LOT 0.
