# Rapport de tests — Lot 5e_C5.1 → C5.3 « Dépanner le lampadaire »

**Environnement réel d'exécution** : Chromium (Playwright), viewport mobile 390×844,
pages chargées en `file://` (mode hors ligne — polices Google absentes, filtrées comme
attendu). Suite : `tests_lot08.js` — 22 tests, **tous réellement exécutés** le 24/07/2026.

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
