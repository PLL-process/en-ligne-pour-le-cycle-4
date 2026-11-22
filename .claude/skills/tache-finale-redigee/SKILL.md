---
name: tache-finale-redigee
description: Concevoir et poser dans une page du dépôt en-ligne-pour-le-cycle-4 la tâche finale rédigée d'une séquence ou d'un entraînement — un document inédit, quatre questions sans propositions (trajet, cas limite, modification, essai qui distingue), un coup de pouce replié, une correction et une grille à trois critères que l'élève coche lui-même. À utiliser à la fin de toute série de questions à choix, et pour préparer l'écrit du brevet. Règles d'or n°346, 351, 356 et 357.
---

# La tâche finale rédigée

**Règle d'or n°346 (clé de voûte) — Choisir n'est pas expliquer** (Pascal, 21/11/2026). Toute série de questions à
choix se termine par une réponse écrite, sans propositions, sur un document que l'élève n'a jamais vu.

Né de l'audit de l'entraînement DNB de `3e_C6.2` : « je peux reconnaître la bonne explication à l'écran sans parvenir à
l'écrire sur ma copie ». Modèle en place : l'onglet « Épreuve écrite » de
`3e_C6.2/entrainement_dnb_algorigrammes.html` (l'abri à vélos), lien direct `#ep`.

## 1. Le document

- **Un objet inédit**, du collège ou de la commune, jamais celui de la séquence : sinon on mesure la mémoire.
- **Des données, pas le verdict** (n°345, n°348) : entrées nommées, condition dans le losange, sorties, retour.
- **Tout ce dont dépend la réponse est écrit** (n°350) : état de départ, unité, comportement entre deux seuils.
- **Le même document sous la question** (n°331), dans la page et à l'impression.

## 2. Quatre questions graduées

| Question | Ce qu'elle mesure | Exemple (abri à vélos, seuil 80 lux) |
|---|---|---|
| 1. Le trajet | suivre une branche avec une valeur | « À 79 lux avec présence, indique le trajet et justifie la commande. » |
| 2. Le cas limite | lire le signe du comparateur (n°351) | « À 80 lux avec présence, prévois l'état de la lampe. » |
| 3. La modification | changer une condition selon un besoin | « Le besoin change : allumer aussi à 80 lux. Modifie la condition. » |
| 4. L'essai qui distingue | prouver la modification, et ce qui n'a pas changé | « Propose un essai qui vérifie que la présence reste obligatoire. » |

La question 3 fournit le bloc d'origine à part : un élève qui s'est trompé en 1 ou 2 peut encore la traiter.

## 3. Dans la page

- Une zone de texte par question, sauvegardée (n°15) ; aucune proposition visible.
- Une **version étayée** repliée par question (n°31) : des phrases à compléter, pas la réponse.
- **Deux aides repliées avant la correction** (n°367) : un indice, puis la démarche ; elles ne s'impriment pas.
- **Hors de la zone d'un bouton « Vérifier »** : le retrait de validation (n°340, `_outils/retrait_validation.py`)
  regarde tous les champs de l'activité ; un écrit posé dedans retirerait la validation des questions à choix
  (vu sur `3e_C6.1`, 21/11/2026). Le bloc va dans sa propre carte, ou après la fin de l'activité.
- Une **correction** repliée, exhaustive (n°96), qui donne **la phrase de copie** (« ✍️ Sur ta copie, on peut
  écrire… », n°356).
- Une **grille à trois critères** que l'élève coche après avoir lu la correction : suivre la branche, justifier avec
  les données, modifier et vérifier.
- **Aucun bouton qui note** : la page ne juge pas un texte libre (n°340).
- **Chaque sigle écrit en clair** dans le bloc, même s'il est expliqué ailleurs sur la page (TTL, CDI… ; n°44,
  consigne de Pascal du 22/11/2026) ; une lettre de formule aussi (« ρ : la masse volumique de l'air »). Le bandeau dit « réponses écrites, correction
  lue, grille cochée », pas « réussi ».
- La fiche bilan imprimable reprend les réponses écrites (n°358).

## 4. Le brevet, tel qu'il est (n°357)

Les chiffres se citent avec leur source et leur date, et se relisent chaque année. Ceux de l'audit du 21/11/2026, pour
la session 2027 : si la technologie est tirée, 30 minutes environ et 10 points, dont 1 point de maîtrise de la langue
pour toute la copie de technologie ; des exercices indépendants ; peu de QCM. Sources citées par l'audit :
[définition de l'épreuve](https://www.education.gouv.fr/bo/2026/Hebdo4/MENE2623228N) et
[maîtrise de la langue](https://www.education.gouv.fr/bo/2026/Special4/MENE2623195N). Skill `dnb-technologie` pour un
sujet complet.

Jamais « le brevet se joue dans les distracteurs » ; toujours « après avoir choisi, explique ton raisonnement en une ou
deux phrases ».

## 5. Vérifier

```bash
python3 _outils/tests_ecrit_brevet.py <page.html>     # ou --tout : chaque bloc .ecrit-brevet du site
```

Le banc commun joue chaque bloc à 390 px : forme (zones, aucune proposition, étayage, deux aides, correction repliée
avec une phrase de copie par zone, grille), document sous les yeux (n°331), rien de noté (n°340), reprise après
rechargement, lien direct `#id` qui ouvre la séance (n°359), aucune erreur, aucun défilement.

Blocs en place (22/11/2026) : `3e_C6.1` (`#ecritBouee`), `3e_C4.7-C4.8` (`#ecritPont`), `3e_C8.1` (`#ecritPort`,
livré par la PR du thème 3 qui suit). L'épreuve écrite de l'entraînement DNB (`3e_C6.2`, `#ep`) a son propre gabarit
et son banc (`tests_entrainement_dnb.py`), hors de ce banc commun.


- Le banc remplit les quatre zones, recharge, et retrouve les textes et la grille.
- Le banc vérifie qu'aucune zone n'affiche « juste » ou « faux ».
- En classe : comparer trois copies, le score d'une manche à choix et la réponse écrite (n°346). Un élève qui réussit
  les choix et n'écrit pas « 80 < 80 est faux, car < exclut l'égalité » a encore besoin d'un guidage.
