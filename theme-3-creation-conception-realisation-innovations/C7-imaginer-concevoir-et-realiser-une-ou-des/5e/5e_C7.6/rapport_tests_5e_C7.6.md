# Rapport de tests — 5e_C7.6

Ce rapport ne déclare que des tests **réellement exécutés**, sous Chromium (Playwright), le
30/08/2026.

## QCM — `tests_5e_C7.6_qcm.mjs`

    node tests_5e_C7.6_qcm.mjs qcm_5e_C7.6_le-de.html "5e_C7.6" "" ../../atelier-cao/tp_5e_de_onshape.html

**31 / 31.** Ce que la suite vérifie :

- chargement sans erreur JavaScript, sans requête échouée, sans boîte modale ;
- 30 questions, 4 options et 3 réfutations chacune, la bonne réponse sans réfutation ;
- tous les champs du gabarit remplis, 30 notions **distinctes**, aucune image héritée ;
- **la répartition par code est mesurée dans la banque**, pas déclarée (30 sur `5e_C7.6`) ;
- chaque code porté dépasse le seuil d'évaluabilité de 5 questions ;
- les bonnes réponses sont réparties sur les quatre positions (8/7/7/8) ;
- **aucune bonne réponse détachée par sa longueur** (écart maximal toléré : 8 caractères) et
  écart moyen sous 5 caractères (mesuré : +2.8 caractère) ;
- une bonne réponse est déclarée correcte, une mauvaise incorrecte, la correction déplie les
  trois réfutations et porte un « à retenir » ;
- les deux confirmations en deux temps, **sans aucune boîte modale** (règle d'or n°188) ;
- 30 bonnes réponses donnent 100 % et la note 20/20 ;
- le lien vers le TP pointe le bon fichier ;
- réponses et progression survivent au rechargement.

## Outils du dépôt passés sur ce lot

| Outil | Résultat |
|---|---|
| `_outils/sans_modale.py` | rien à faire — aucune boîte modale |
| `_outils/fix_r.js` | répartition A/B/C/D = 8/7/7/8, graine 761 |
| `_outils/generer_lexique.py` | 30 notions → `lexique_5e_C7.6.html` |
| `_outils/controle_liens.py` | aucune adresse morte dans les pièces du lot |
| `_outils/controle_couverture.py` | verdict rendu **depuis le dossier de chaque code** (un code peut être cité chez lui et évalué ici) : `5e_C7.6` : ÉVALUÉ 30 question(s) |
| `_outils/controle_formulations.py` | les citations du référentiel sont exactes |

## Ce qui n'est pas testé, et ne peut pas l'être ici

- **Le TP lui-même n'est pas rejoué.** Il vit dans l'atelier CAO et n'a pas été modifié par ce
  lot, à l'exception de l'avertissement de connexion ajouté en tête. La justesse des gestes qu'il
  décrit dépend de l'interface d'Onshape, qui change plusieurs fois par an : elle se constate en
  salle, pas dans un script.
- **Aucun essai en classe.** Le seul critère qui compte pour un TP de prise en main — combien
  d'élèves lèvent la main pour retrouver un bouton — se relève devant les élèves.
