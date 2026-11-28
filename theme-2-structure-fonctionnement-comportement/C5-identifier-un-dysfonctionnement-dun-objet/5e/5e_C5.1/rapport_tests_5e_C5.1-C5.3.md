# Rapport de tests — Lot 5e_C5.1 → C5.3 « Dépanner le lampadaire »

**Environnement réel d'exécution** : Chromium (Playwright), viewport mobile 390×844,
pages chargées en `file://` (mode hors ligne — polices Google absentes, filtrées comme
attendu). Suite : `tests_lot08.js` — 22 tests, **tous réellement exécutés** le 24/07/2026.

> **Ce script n'est pas dans le dépôt et n'y a jamais été commité** (relevé du 31/08/2026 par
> `_outils/controle_rapports_tests.py`).
>
> **Suite du même jour — elle est écrite, et elle est ici.** `tests_5e_C5.1-C5.3.mjs`,
> **26 contrôles**, rejoue les vingt-deux lignes ci-dessous : l'inspecteur visuel cliqué zone
> par zone, le simulateur de réparation conduit étape par étape — y compris une étape jouée
> trop tôt, qui doit tout remettre à zéro —, les quatre activités remplies avec les réponses
> **lues dans la page**, le rechargement verrous compris, puis le QCM ouvert et joué.
>
> ```
> node tests_5e_C5.1-C5.3.mjs      →  26 / 26
> ```
>
> Quatre contrôles s'ajoutent au tableau d'origine : aucun verrou ouvert au chargement
> (n°226), les réponses extraites de la page et non recopiées, les réfutations parallèles
> vérifiées question par question, et l'absence de boîte modale sur tout le parcours.

> **Révision du 14/11/2026** (révision des trois thèmes, ligne 29 du suivi). Les trente questions sont des groupes de
> boutons radio (règle d'or n°300) ; les réponses attendues se lisent dans les tables `ATT1` à `ATT4` de la page. Le banc
> coche les boutons et gagne **quatre contrôles** : aucune liste déroulante et chaque réponse attendue présente une seule
> fois ; la bonne réponse change de place (aucune place n'en porte plus de 40 %) ; en séance 2, le protocole est replié
> pendant qu'on range les étapes et les boutons du simulateur ne sont pas dans l'ordre ; une seule erreur donne 7 / 8, ne
> valide pas l'activité et marque cette seule question « à revoir ».
>
> ```
> node tests_5e_C5.1-C5.3.mjs      →  30 / 30
> node tests_regle_311_5e_C5.1.mjs →  34 / 34
> ```

**Résultat : 22 / 22 réussis · aucune erreur JavaScript sur les deux pages.**

## Séquence (14 tests)

| # | Test | Résultat |
|---|---|---|
| 1 | Chargement, titre « Dépanner » + sous-titre en tête (règle d'or n°4 §1) | ✅ |
| 2 | Badges des 3 codes 5e_C5.1 / C5.2 / C5.3 | ✅ |
| 3 | Onglets séances : bascule vers S2 fonctionnelle | ✅ |
| 4 | Inspecteur visuel : clic des 6 zones → compteur 6/6 + verrou `__exp.inspection` | ✅ |
| 5 | Activité 1 : 8/8 avec verrou d'inspection actif | ✅ |
| 6 | Simulateur de réparation : étape jouée trop tôt → remise à zéro (0/6) | ✅ |
| 7 | Simulateur : les 6 étapes dans l'ordre → « 6/6 RÉPARÉ » + verrou `__exp.repare` | ✅ |
| 8 | Activité 2 : 8/8 (ordre du protocole + questions) avec verrou | ✅ |
| 9 | Activités 3 et 4 : 7/7 et 4/4 | ✅ |
| 10 | Barre de progression : 4/4 activités validées | ✅ |
| 11 | Sauvegarde localStorage puis rechargement : état intégralement restauré (verrous compris) | ✅ |
| 12 | Blocs règle d'or n°4 (« Prêt·e à t'entraîner ? » + « Bonus facultatif ») présents, après le bilan, avant le pied de page | ✅ |
| 13 | Tous les liens internes de la page pointent vers des fichiers existants | ✅ |
| 14 | Les 3 SVG référencés existent sur le disque | ✅ |

## QCM (8 tests)

| # | Test | Résultat |
|---|---|---|
| 15 | Chargement, titre « Dépanner », 30 questions annoncées | ✅ |
| 16 | Banque : 30 questions exactement, 10 par code | ✅ |
| 17 | Répartition des bonnes réponses A/B/C/D = 8/7/7/8 et `d[r]` vide pour chaque question | ✅ |
| 18 | 3 questions illustrées (règle images v2), fichiers SVG présents | ✅ |
| 19 | Chaque question : 4 options, explication, « à retenir », 3 distracteurs expliqués | ✅ |
| 20 | Une partie démarre et une réponse se joue réellement | ✅ |
| 21 | Clé localStorage `qcm_5e_C5.1-C5.3_depanner_lampadaire` | ✅ |
| 22 | Lien de retour vers la séquence valide | ✅ |

## Limites du rapport

Tests exécutés uniquement dans l'environnement ci-dessus (Chromium/Playwright).
Aucune compatibilité non testée n'est revendiquée (autres navigateurs : non testés).
La version 🅰 (maquette réelle) relève de l'enseignant et n'est pas testable ici.

## Reprise du 28/11/2026 — quatre questions sur document de plus, et un billet de sortie (n°345, n°330)

- `node tests_5e_C5.1-C5.3.mjs` : **36 / 36** (six tests neufs : le billet existe à la séance 3, juste avant le Bonus ;
  deux zones gardées, deux versions étayées, deux critères, des contre-exemples, aucun bouton ; la réponse survit au
  rechargement ; au QCM, au moins six questions sur document, chaque document décrit, `documents_qcm.py --verifier` à
  jour). `node tests_regle_311_5e_C5.1.mjs` : **34 / 34**.
- `controle_question_seule.py --strict --chantiers` : tout à 0 (D1 et P1 étaient à 1). `balayer_questions_qcm.mjs
  --apres` : 30 questions, 7 illustrées, 0 écart. Contrôles des QCM (aides comprises), des schémas (0 ✘), de
  l'aération, des règles d'or, du squelette, du mode mission, des liens et des statuts : verts.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.
