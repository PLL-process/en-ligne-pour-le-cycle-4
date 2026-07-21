# Standard obligatoire — éditeur de code pédagogique

## Décision de Pascal

La séquence `5e_C1.3–C1.4 — Systèmes d’information et gestion des données` doit offrir pour son programme Python la même qualité de présentation et d’utilisation que l’environnement apprécié dans le Jardin connecté.

Ce standard doit ensuite être appliqué à toutes les séquences qui demandent de lire, compléter, commenter ou modifier un programme.

## Problème constaté

Le programme Python de la séquence 5e est actuellement affiché dans un bloc statique `<pre><code>`. L’élève doit copier le contenu vers un compilateur extérieur pour le modifier ou le tester.

Cette présentation ne permet pas directement :

- la numérotation des lignes ;
- la coloration syntaxique ;
- l’édition confortable ;
- la sauvegarde locale ;
- la copie en un clic ;
- l’identification rapide des lignes à commenter ou corriger.

## Composant attendu

Créer un composant réutilisable appelé provisoirement `CodeLab Techno`.

Il doit fonctionner sans compte, sans envoi de données personnelles et sans dépendance indispensable à un service extérieur.

### Fonctions obligatoires

1. **Coloration syntaxique** adaptée au langage affiché : Python, Arduino/C++, JavaScript ou pseudo-code.
2. **Numéros de lignes** dans une gouttière stable, synchronisée avec le défilement.
3. **Édition directe** du programme par l’élève.
4. Police monospace lisible, de type Fira Code avec solution locale de repli.
5. Bouton `Copier le programme`.
6. Bouton `Réinitialiser le programme` avec confirmation.
7. Boutons `A−` et `A+` pour ajuster la taille du texte.
8. Option `Retour à la ligne` activable ou désactivable.
9. Bouton `Plein écran` ou mode agrandi.
10. Indication permanente du langage et du nombre de lignes.
11. Navigation clavier complète et focus visible.
12. Respect de `prefers-reduced-motion`.
13. Affichage adapté à l’ordinateur, la tablette et le téléphone.
14. Fonctionnement hors connexion une fois la page chargée.
15. Sauvegarde automatique locale avec bouton `Effacer ma sauvegarde`.

### Fonctions pédagogiques

- surligner temporairement une ligne citée dans une consigne ;
- permettre à l’enseignant d’indiquer des lignes à observer, compléter ou commenter ;
- conserver les commentaires écrits par l’élève ;
- proposer `Voir un indice` puis une correction exhaustive ;
- afficher une comparaison claire entre la version initiale et la version de l’élève lorsqu’elle apporte une vraie aide ;
- ne jamais remplacer l’explication pédagogique par un simple message d’erreur technique.

### Test du programme

Le fonctionnement principal ne doit pas dépendre d’un compilateur en ligne. Deux niveaux sont prévus :

- **niveau minimal obligatoire** : modifier, sauvegarder, copier puis ouvrir un outil de test recommandé ;
- **niveau enrichi facultatif** : exécution locale sécurisée lorsque le langage et le poids technique le permettent, avec console de sortie séparée.

Les liens vers Programiz ou d’autres compilateurs restent des solutions complémentaires, clairement signalées comme services externes.

## Application immédiate à la séquence 5e_C1.3–C1.4

Le programme de gestion des prêts de livres doit devenir éditable dans la page.

L’élève doit pouvoir :

1. lire le programme avec coloration et numéros de lignes ;
2. ajouter un commentaire sur chaque instruction importante ;
3. compléter ou modifier la fonction `emprunter()` ;
4. sauvegarder son travail localement ;
5. copier le programme pour le tester ;
6. comparer ensuite avec une correction détaillée et commentée ligne par ligne.

## Cohérence avec le Jardin connecté

Les deux séquences doivent partager :

- la même famille de couleurs ;
- la même police de code ;
- les mêmes boutons et pictogrammes ;
- les mêmes règles de numérotation, de sauvegarde et d’accessibilité ;
- un composant commun plutôt que deux implémentations indépendantes.

## Améliorations proposées

- repérage visuel des lignes modifiées ;
- compteur de commentaires ajoutés par l’élève ;
- bouton `Aller à la prochaine ligne à compléter` ;
- indicateur `Travail sauvegardé sur cet appareil` ;
- export du code en fichier `.py` ou `.ino` ;
- possibilité d’importer un fichier compatible sans l’envoyer sur un serveur ;
- mode clair/sombre propre à l’éditeur, sans modifier toute la page.

## Tests bloquants

- numéros de lignes exacts après ajout ou suppression d’une ligne ;
- synchronisation du défilement entre la gouttière et le texte ;
- coloration qui ne modifie jamais le code saisi ;
- sauvegarde et reprise fiables ;
- réinitialisation sûre ;
- copie conforme du programme ;
- absence d’erreur JavaScript ;
- fonctionnement au clavier et sur écran tactile ;
- aucune donnée envoyée à un tiers ;
- aucune dépendance distante bloquante ;
- lisibilité lorsque la réduction des mouvements est activée.

## Gouvernance

Cette évolution doit être réalisée sur une branche dédiée et présentée dans une Pull Request en brouillon. Fable produit le composant et l’intègre aux deux séquences de référence. ChatGPT contrôle l’accessibilité, la sauvegarde, la fidélité du code, les tests et la cohérence pédagogique. Pascal teste uniquement les deux pages de référence avant généralisation.
