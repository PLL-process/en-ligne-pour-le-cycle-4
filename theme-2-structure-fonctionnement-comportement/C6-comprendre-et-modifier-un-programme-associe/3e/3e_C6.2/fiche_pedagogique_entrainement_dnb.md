# Fiche pédagogique — Entraînement DNB « lire et interpréter un algorigramme »

**Niveau** 3e · **Thème 2** · **Nature** ressource d'entraînement — ce n'est **pas** une séquence
**Format** page autonome, hors ligne, sans compte, sans envoi de données
**Contenu** 30 exercices en 4 manches, corrections qui réfutent chaque réponse fausse

## Ce que cette page est, et ce qu'elle n'est pas

Elle **entraîne** à lire, dérouler et interpréter un algorigramme — ce que demande l'épreuve du
brevet. Elle ne prétend pas couvrir un code du référentiel : pas de situation déclenchante, pas de
mission, pas de production d'élève. C'est assumé, et c'est écrit sur la page elle-même.

Pour **écrire** un algorithme de zéro, la séquence 3e_C6.2 « L'auto-test de la station » reste la
ressource de référence. Pour lire les données d'un programme puis le modifier, c'est 3e_C6.1.

## Pourquoi une réécriture plutôt qu'un rustinage

Le dossier contenait déjà une banque de 30 exercices, héritée d'une organisation antérieure du
dépôt. Elle est bonne sur le fond mais n'est pas bâtie sur le gabarit maison : **aucune sauvegarde
locale**, aucun mode essentiel, aucune barre d'outils, et surtout des corrections qui donnent la
bonne réponse **sans dire pourquoi les trois autres sont fausses**.

Or au brevet, les distracteurs sont conçus pour être plausibles. Un élève qui sait pourquoi B est
faux ne se fera pas prendre par une variante de B. C'est la raison principale de la réécriture :
**la réfutation de chaque distracteur**, sur les trente exercices.

## Les quatre manches

| Manche | Contenu | Exercices |
|---|---|---|
| 1 | Le vocabulaire et les symboles — ce qu'on doit savoir nommer avant de savoir lire | 8 |
| 2 | Lire et dérouler — suivre les flèches, noter ce que devient chaque variable | 8 |
| 3 | Compteurs, tests et cas limites — là où se perdent les points | 6 |
| 4 | Sujets type DNB — des situations complètes, comme à l'épreuve | 8 |

Chaque manche a son propre vérificateur. Le seuil de validation est fixé à trois quarts des
réponses justes : au-dessus, la manche est acquise ; en dessous, le message oriente vers les aides
de niveau 2 plutôt que vers le score.

## Les erreurs que la manche 3 vise explicitement

Ce sont celles qui coûtent le plus de points, et elles reviennent chaque année :

1. **le compteur initialisé dans la boucle** — le programme tourne, ne plante pas, et donne un
   résultat faux ;
2. **le cas qui tombe pile sur le seuil** — tout se joue sur `>` contre `≥` ;
3. **la conclusion placée dans la boucle** — un message par tour au lieu d'un seul ;
4. **la boucle sans progression** — rien ne fait avancer la variable du test ;
5. **la branche par défaut oubliée** — que fait le système quand aucun test n'est vrai ?

## Comment l'utiliser en classe

**En autonomie**, une manche à la fois, avec la consigne explicite d'ouvrir la correction **même
quand la réponse est juste**. C'est là qu'est le travail.

**En remédiation ciblée**, en envoyant un élève sur la manche qui correspond à sa difficulté :
les manches sont indépendantes et la page retient la progression.

**En révision de fin d'année**, la manche 4 seule constitue une séance de trente minutes sur des
situations de type brevet.

La page fonctionne hors ligne : elle peut être copiée sur les postes de la salle, ou distribuée
telle quelle.

## Accessibilité et différenciation

- **Mode essentiel** (règle n°29) : masque le rappel de cours, les corrections et les compléments.
- **Deux niveaux d'aide** avant chaque correction : le premier remet sur la piste, le second
  explique le raisonnement complet. La page dit explicitement que les utiliser n'est pas tricher.
- **Bandeau de tâches** (règle n°30) : l'élève sait dans quelle manche il se trouve.
- Chaque liste déroulante porte une étiquette ; les figures ont une alternative textuelle qui
  décrit le contenu, pas l'apparence ; aucune information n'est portée par la seule couleur.

## Ce qui n'a pas été fait, et pourquoi

Pas de QCM séparé : la page **est** l'entraînement, un QCM ferait doublon.
Pas de synthèse élève ni professeur : le rappel de cours est intégré, et les synthèses de 3e_C6.2
couvrent déjà les mêmes notions.
Pas d'évaluation sommative : ce n'est pas la fonction de cette ressource.
