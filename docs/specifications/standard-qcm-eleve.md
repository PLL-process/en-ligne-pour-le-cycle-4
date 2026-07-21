# Standard obligatoire — QCM HTML d’entraînement pour l’élève

## Principe général

Toute séquence pédagogique publiée dans le dépôt doit être accompagnée d’au moins un **QCM HTML autonome et distinct** de la séquence.

Le QCM est une ressource d’entraînement durable, utilisable notamment à la maison après la séance. Il ne doit pas être fondu dans le fichier de séquence ni disparaître lors d’une fusion de contenus.

Chaque QCM doit rester accessible directement depuis la compétence et depuis le tableau de bord permanent du site.

## Référence fonctionnelle retrouvée

La version archivée `QCM_XXL_40_Reseaux_v2_ex-canonique.html` contenait des fonctions utiles qui ont disparu lors de la fusion vers le QCM XXL de 77 questions :

- barre de progression globale ;
- compteurs `répondues`, `correctes`, `incorrectes`, `non répondues` ;
- minuteur avec démarrage, pause et reprise ;
- correction enrichie après chaque réponse ;
- affichage explicite de la bonne réponse ;
- explication complète repliable ;
- bouton `Réessayer` ;
- résultat final incluant le temps passé.

Ces fonctions doivent être restaurées dans le QCM XXL de 77 questions puis intégrées au générateur commun.

## Tableau de bord élève obligatoire

Le haut de chaque QCM doit afficher une zone compacte et, si possible, fixe lors du défilement :

- nombre total de questions ;
- nombre répondu ;
- nombre correct ;
- nombre incorrect ;
- nombre restant ;
- pourcentage d’avancement ;
- score brut et note sur 20 ;
- minuteur facultatif que l’élève peut mettre en pause ;
- bouton pour reprendre là où il s’était arrêté.

L’information ne doit jamais dépendre uniquement d’une couleur.

## Navigation dans les questions

Pour les QCM de plus de 20 questions, ajouter une grille ou un sommaire cliquable :

- numéro de chaque question ;
- état `non répondue`, `correcte`, `à revoir` ;
- accès direct à la question ;
- filtres `Toutes`, `Non répondues`, `À revoir`, `Correctes` ;
- bouton `Question suivante non répondue`.

## Sauvegarde et reprise

Le QCM doit sauvegarder localement, sans compte et sans serveur :

- identité seulement si l’élève la saisit volontairement ;
- réponses ;
- progression ;
- temps écoulé ;
- questions déjà corrigées ;
- date de la dernière activité.

La sauvegarde doit utiliser `localStorage`, avec un bouton clair `Effacer ma progression`.

Aucune donnée personnelle ne doit être envoyée en ligne.

## Correction exhaustive obligatoire

Après chaque tentative, la correction doit comprendre au minimum :

1. l’indication claire `Correct` ou `À revoir` ;
2. la bonne réponse formulée en toutes lettres ;
3. une explication complète du raisonnement ;
4. un exemple concret lié à la technologie ou à la vie réelle ;
5. l’explication de l’erreur la plus probable ;
6. pour un QCM à choix, une justification courte indiquant pourquoi les autres propositions ne conviennent pas ;
7. un encadré `À retenir` ;
8. un bouton `Réessayer` qui n’ajoute pas plusieurs fois les mêmes points.

Une correction réduite à `Bonne réponse` ou `Mauvaise réponse` est interdite.

## Aides progressives

Chaque question doit proposer, lorsque cela apporte une vraie aide :

- `Indice 1` : rappel très bref ;
- `Indice 2` : démarche ou notion à mobiliser ;
- `Voir le cours` : explication plus complète ;
- la solution seulement après une tentative ou une demande explicite.

L’utilisation d’une aide peut être signalée dans le bilan, mais ne doit pas humilier ni bloquer l’élève.

## Bilan final personnalisé

À la fin, le QCM doit afficher :

- score et note sur 20 ;
- temps passé ;
- taux de réussite ;
- réussite par compétence ou sous-thème ;
- liste des notions maîtrisées ;
- liste des notions à revoir ;
- liens directs vers les questions incorrectes ;
- proposition d’une courte série de rattrapage centrée sur les erreurs ;
- bouton `Recommencer uniquement les questions à revoir` ;
- bouton d’impression ou d’enregistrement en PDF du bilan, sans publier la correction d’une évaluation sommative.

## Modes d’utilisation

Le même moteur doit pouvoir proposer :

- `Entraînement guidé` : correction après chaque question ;
- `Entraînement libre` : l’élève avance dans l’ordre souhaité ;
- `Défi rapide` : sélection aléatoire de 10 questions ;
- `Révision ciblée` : questions d’une compétence choisie ;
- `XXL` : totalité de la banque.

Le mode par défaut reste l’entraînement guidé à domicile.

## Ergonomie et accessibilité

- fonctionnement sur ordinateur, tablette et téléphone ;
- utilisable au clavier ;
- focus visible ;
- textes alternatifs pertinents ;
- contraste suffisant ;
- respect de `prefers-reduced-motion` ;
- aucune animation rapide ou agressive ;
- consignes courtes et vocabulaire adapté au niveau ;
- fonctionnement hors connexion une fois le fichier chargé ;
- aucun CDN indispensable au fonctionnement.

## Règles de qualité des questions

- une seule difficulté principale par question ;
- distracteurs plausibles mais non trompeurs ;
- absence de pièges purement linguistiques ;
- niveau explicitement adapté à la 5e, 4e ou 3e ;
- compétence réellement travaillée et pas seulement affichée ;
- exemples contextualisés, notamment en Martinique lorsque pertinent ;
- nombres, unités, schémas et calculs vérifiés automatiquement ;
- questions sensibles ou ambiguës signalées pour arbitrage.

## Générateur commun

Le standard doit être implanté dans le générateur de QCM du dépôt afin que toutes les ressources bénéficient des mêmes fonctions.

Les données d’une question doivent séparer clairement :

- énoncé ;
- type de réponse ;
- propositions ;
- réponse attendue ;
- compétence ;
- difficulté ;
- indices ;
- correction exhaustive ;
- exemple ;
- erreurs fréquentes ;
- message `À retenir`.

La fusion de deux banques de questions ne doit jamais supprimer les fonctions de l’interface. Des tests de non-régression doivent comparer les capacités fonctionnelles avant et après fusion.

## Tests bloquants

Un QCM n’est pas validable tant que les contrôles suivants ne réussissent pas :

- nombre réel de questions conforme au titre ;
- chaque question possède une réponse attendue ;
- chaque question possède une correction exhaustive ;
- score non cumulable plusieurs fois sur la même question ;
- réinitialisation complète et fiable ;
- sauvegarde/reprise fonctionnelle ;
- progression exacte après réponse, correction, nouvel essai et réinitialisation ;
- absence d’erreur JavaScript ;
- liens et médias disponibles ou solution de repli locale ;
- fonctionnement mobile et clavier ;
- aucune donnée envoyée à un service externe ;
- aucune correction sommative privée publiée.

## Priorité immédiate

1. Restaurer dans le QCM XXL de 77 questions la progression détaillée, le minuteur, le bouton `Réessayer` et les corrections enrichies de la version archivée.
2. Vérifier les 77 corrections et les rendre exhaustives avec exemples.
3. Ajouter la sauvegarde locale, la navigation par numéros et le bilan par compétences.
4. Reporter ces fonctions dans le générateur commun.
5. Régénérer progressivement les QCM existants sans modifier leurs contenus validés sans contrôle.

## Gouvernance

Cette évolution appartient à une branche et une Pull Request distinctes : `draft/standard-qcm-eleve`.

Fable produit et exécute ses tests. ChatGPT contrôle la conformité, la qualité des corrections, les calculs et les régressions. Pascal ne reçoit à tester que le QCM de référence et un petit échantillon des QCM régénérés.