# Rapport de tests — lot Hangzhou 4e_C2.1 · C2.2

**Date** 8 août 2026 · **Suite** `tests_4e_C2.1-C2.2_hangzhou.py` (Playwright, Chromium 1280×900)
**Résultat** **60 / 60 tests passés**

Ce rapport ne mentionne que des tests **réellement exécutés**. La suite est livrée avec le lot :
elle se relance depuis le dossier du lot par `python3 tests_4e_C2.1-C2.2_hangzhou.py`.

## Les données (5 tests)

C'est nouveau dans ce dépôt : la suite **vérifie les chiffres que la séquence affirme**, en relisant
les CSV. Si quelqu'un régénère les données sans refaire les corrigés, le test tombe.

| Ce qui a été vérifié | Résultat |
|---|---|
| 30 retraits × 5 étapes = 150 lignes | ✔ |
| « choisir » est bien la plus longue en moyenne (40 s) | ✔ |
| « déverrouiller » : 29 s de moyenne, **83 s au maximum** | ✔ |
| 9 reprises sur 30 à l'étape déverrouiller | ✔ |
| 12 verbatims, les 5 étapes représentées | ✔ |

## La séquence (32 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| Aucune erreur JavaScript au chargement ni pendant le parcours | ✔ |
| Hors ligne intégral : aucune ressource distante (n°40) | ✔ |
| Lien d'accueil résolu sur le fichier réel (n°11) | ✔ |
| Bandeau de tâches affiché et mis à jour par séance (n°30) | ✔ |
| 8 zones de rédaction, 8 versions étayées (n°31) | ✔ |
| Chaque champ porte une étiquette ou un `aria-label` (n°34) | ✔ |
| Les trois figures sont chargées, alternative longue (n°1) | ✔ |
| Le compteur annonce 4 activités et en compte 4 (n°39) | ✔ |
| Billet d'entrée : oriente sans note, hors progression (n°26) | ✔ |
| Mode essentiel, rappel d'hypothèse, sauvegarde restaurée | ✔ |
| Blocs « Prêt·e à t'entraîner » et « Bonus », **un seul** bouton QCM (n°4) | ✔ |

**Les quatre verrous de production, testés dans les deux sens :**

| Verrou | Refus vérifié | Validation vérifiée |
|---|---|---|
| Activité 1 — le relevé | un relevé **sans code de verbatim** est refusé | ✔ |
| Activité 2 — le graphique | dix valeurs et une lecture nommant les deux étapes exigées | ✔ |
| Activité 3 — l'algorigramme | un algorigramme **sans sortie d'échec** est refusé | ✔ |
| Activité 4 — les exigences | quatre exigences **d'une seule famille** sont refusées | ✔ |

## Les trois règles neuves (9 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| **n°43** — le corrigé du graphique est présent **et replié** | ✔ |
| **n°43** — le bloc Bonus porte un corrigé, qui traite les trois défis | ✔ |
| **n°44** — aucun badge ni bouton sans infobulle (0 élément nu) | ✔ |
| **n°44** — la légende des badges est lisible **sans survol** | ✔ |
| **n°44** — le mode essentiel est expliqué en clair | ✔ |
| **n°45** — au départ, le bouton vise le parcours complet | ✔ |
| **n°45** — après l'activité 1, il vise `#codes=C2.1` et annonce 15 questions | ✔ |
| **n°45** — les deux compétences faites, retour au parcours complet | ✔ |
| **n°45** — le QCM ouvert sur `#codes=C2.1` propose **15 questions du seul C2.1** | ✔ |

Les quatre arrivées possibles du QCM ont été ouvertes une par une, dans des contextes de navigateur
séparés : `#codes=C2.1`, `#codes=C2.2`, les deux codes, et sans ancre.

## Le QCM (8 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| Aucune erreur JavaScript | ✔ |
| 30 questions, 15 par code | ✔ |
| Bonnes réponses réparties A/B/C/D = **8 / 7 / 7 / 8** (graine 421) | ✔ |
| 5 questions illustrées | ✔ |
| Aucune réfutation de 20 caractères ou moins ; `d[r]` vide partout | ✔ |
| Explication, exemple, erreur classique et à-retenir sur chaque question | ✔ |
| Parcours complet : les 30 bonnes réponses acceptées | ✔ |
| Bilan par compétence affiché avec les deux codes | ✔ |

## Les synthèses (6 tests)

Élève et professeur : aucune erreur JavaScript, figures référencées au bon nombre (3 et 0), et
**tous les liens de navigation résolus sur des fichiers existants**.

## Un test rouge, et qui avait tort

Le contrôle « le corrigé du Bonus traite les trois défis » a d'abord échoué. Le corrigé était bien
là : le test lisait `inner_text` sur un `<details>` **replié**, qui n'expose que son `summary`.

C'est la **quatrième fois** que ce piège se présente dans ce dépôt. Le réflexe est désormais acquis
— chercher lequel des deux a tort avant de toucher au contenu — mais le piège, lui, ne s'use pas.
Le test lit maintenant `textContent`, et un commentaire dans le fichier dit pourquoi.

## Ce qui n'a pas été testé

- L'impression A4 : les feuilles `@media print` viennent du gabarit maison, mais aucune sortie
  papier n'a été produite ni relue.
- Un vrai lecteur d'écran : les `aria-label`, `title`, `aria-describedby` et les `desc` SVG sont en
  place et vérifiés dans le DOM, mais aucun test avec NVDA ou VoiceOver n'a été mené.
- Le comportement des **infobulles sur tablette** : c'est précisément parce qu'on ne peut pas s'y
  fier que la règle n°44 impose une mention en clair — mais la mention, elle, a été vérifiée.
- La séquence sur mobile réel : seule la fenêtre 1280×900 a été utilisée.
