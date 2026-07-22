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

## Déclenchement après publication

Le badge ne doit jamais être déclenché par la simple création d’une branche, d’un commit ou d’une Pull Request en brouillon.

Une entrée devient visible sur la page d’accueil uniquement lorsque le lot correspondant a été fusionné dans `main` et que GitHub Pages a publié la nouvelle version.

Le processus de publication doit alors :

1. ajouter ou actualiser automatiquement l’entrée du code concerné dans `nouveautes.json` ;
2. enregistrer la date réelle de publication ;
3. régénérer l’index ;
4. vérifier que le code exact est visible avec son badge ;
5. vérifier que les liens vers la séquence et son QCM fonctionnent ;
6. fournir à Pascal l’ancre directe vers ce code.

Une ressource profondément remaniée peut recevoir le badge `NEW`, même si son fichier existait déjà. Le type de nouveauté doit alors être indiqué par une donnée `nature` :

- `nouvelle_ressource` ;
- `refonte_majeure` ;
- `qcm_nouveau` ;
- `correction_importante`.

Pour le lot de modernisation actuel, `5e_C1.1` devra apparaître avec `nature: refonte_majeure` après publication, accompagné des liens vers la séquence et le QCM.

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
- `nature` (`nouvelle_ressource`, `refonte_majeure`, `qcm_nouveau`, `correction_importante`) ;
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
- tests automatiques couvrant la date, l’ancre, l’ouverture des sections, les liens séquence/QCM et l’absence de faux badge avant fusion.

## Gouvernance

Cette fonctionnalité appartient à la Vague 0 « Fondation — tableau de bord ». Elle doit être développée sur une branche distincte et présentée dans une Pull Request en brouillon. Elle ne doit être ajoutée ni à la Pull Request du LOT 0 ni aux branches pédagogiques. Les lots pédagogiques ne font qu’annoncer les codes à marquer ; le tableau de bord applique réellement le badge après publication.