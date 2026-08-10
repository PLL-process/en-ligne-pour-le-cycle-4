# Rapport de tests — lot 3e_C1.1 à C1.4 « Tsinghua »

**Date d'exécution** 9 août 2026 · **Suite** `tests_3e_C1.1-C1.4_tsinghua.py` · **Moteur** Chromium
via Playwright.

**41 contrôles exécutés, 41 verts, aucune erreur JavaScript.**

Ne sont déclarés ici que des tests **réellement exécutés**. Le détail exact figure dans le fichier
de tests, qui est livré avec le lot et rejouable en une commande.

## Séquence — 24 contrôles

| Ce qui est vérifié | Nombre |
|---|---|
| Les six verrous **refusent** une page vide | 6 |
| Les six verrous **s'ouvrent** sur une production complète | 6 |
| Progression : 5 / 5 activités après validation | 1 |
| Cible du bouton d'entraînement aux trois moments (règle n°45) | 2 |
| Sauvegarde locale restaurée après rechargement (texte + progression) | 2 |
| Blocs de la règle n°4 : entraînement, Bonus, **corrigé du Bonus** | 3 |
| Phrase éthique de l'activité 4 **visible et non repliée** (règle n°68) | 1 |
| Carte de référentiel : les quatre formulations | 1 |
| Les trois corrigés graphiques se chargent effectivement | 1 |
| Zéro erreur JavaScript | 1 |

## QCM — 17 contrôles

Titre affiché et sous-titre propres au lot (règle n°51) · aucune trace d'un autre lot ·
30 questions · bonnes réponses réparties sur A/B/C/D · 11 illustrées · chaque distracteur réfuté ·
réfutation vide pour la bonne réponse · explication, exemple, erreur classique et à-retenir sur
chaque question · formulation du référentiel recopiée · ouverture `#depart=court` sur 10 questions ·
bandeau de portée visible · 30 bonnes réponses acceptées · clé de sauvegarde propre au lot ·
les 11 images se chargent · lien de retour vers la séquence · zéro erreur JavaScript.

Vérifié en outre, hors suite : `#codes=C1.1,C1.4` ouvre bien les 15 questions correspondantes
(8 + 7), le filtre propose les quatre codes, et le mode passe à « cible ».

## Vérificateur de règles du dépôt

`python3 _outils/verif_regles_audit.py` sur le dossier du lot : **8 contrôles sur 8**, dont la
règle n°42 — les quatre formulations de la carte sont celles du référentiel — et la n°33, après
correction de deux pavés de plus de 110 mots dans la correction de l'activité 5.

## Ce qui n'a PAS été testé (règle n°47)

- L'exactitude pédagogique des corrigés et des explications : elle relève de la relecture.
- La justesse des chiffres publics cités : elle relève des sources, listées dans
  `SOURCES_DONNEES_IMPACTS_3e.md`. Les tests vérifient que la page les affiche, pas que le
  ministère de l'Intérieur a raison.
- Le rendu à l'impression et l'ergonomie réelle en classe.
- Le comportement sur un navigateur autre que Chromium.

## Défauts trouvés et corrigés pendant les tests

1. **Deux éléments portaient `id="s1"`.** La découpe du gabarit tombait à l'intérieur de la
   structure des séances : le haut se terminait par l'ouverture du panneau `s1`. Le gestionnaire
   d'onglets activait donc le panneau vide, et le vrai restait invisible. Trouvé parce qu'un bouton
   présent dans le DOM refusait d'être cliquable — un contrôle qui porte sur ce qui est **rendu**
   (n°49) voit ce qu'une lecture du source laisse passer.
2. **Deux pavés de 117 et 115 mots** dans la correction de l'activité 5 (n°33). Coupés aux
   frontières de sens, sans être raccourcis : c'est leur longueur qui montre à l'élève ce qu'on
   attend d'un argumentaire.
3. **La séquence annonçait 7 questions illustrées**, la banque en compte 11. Aligné sur le nombre
   calculé depuis la banque (n°54).
