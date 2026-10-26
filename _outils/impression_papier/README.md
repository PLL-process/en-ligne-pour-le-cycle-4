# Fiche papier — impression des séquences

**Demande de Pascal, 25/10/2026** : « imprimer en PDF : les consignes ne sont pas vues parce que la police et sa
couleur est trop claire. Cela fait beaucoup de pages » ; « rendre ces impressions en PDF ultra premium et moins
longues ». Prototype sur le jardin (4e_C8.1 : 16 pages → 7), jugé par Pascal : « la qualité d'impression que tu donnes
là est super, bravo ». Décisions : **1a** la fiche papier sur les 60 séquences, avec un contrôle qui refuse un texte trop
pâle sur le papier ; **2a** on imprime la fiche élève (ce qui ne sert qu'à l'écran disparaît) ; séquences à onglets :
**1a** on imprime **la séance affichée**. Branche transversale `fable/impression-papier`.

Ce qui reste ouvert : « Mode essentiel : ON » par défaut (décision 3, non tranchée).

## Plan et avancement

- [x] 0. Branche et plan (ce fichier).
- [ ] 1. Relevé de la structure des 60 séquences (squelette n°306, onglets de séances, ce qui ne sert qu'à l'écran).
- [ ] 2. Source unique : `papier.css`, `papier.js`, `poser.py` ; contrôle `_outils/controle_impression_papier.py` + tests.
- [ ] 3. Pose sur les 60 séquences ; générateurs qui écrivent des séquences mis à jour.
- [ ] 4. `controle_impression.mjs` : sur une page qui porte la fiche papier, un texte sous 4,5 : 1 sur fond clair est refusé.
- [ ] 5. Banc au navigateur : pages avant / après, aucun champ d'écran imprimé, aucune erreur JavaScript, écran inchangé
      (captures comparées), planches de toutes les fiches regardées.
- [ ] 6. Journal, nouveautés, skills, audit et index, contrôles du dépôt contre `main`, PR.

Chaque étape finie est poussée sur la branche. Pour reprendre : lire ce fichier, puis `git log` de la branche.
