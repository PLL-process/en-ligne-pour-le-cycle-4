# Rapport de tests — Lot 4e_C5.1 → C5.3 « SOS jardin connecté »

**Environnement réel d'exécution** : Chromium (Playwright), viewport mobile 390×844,
pages chargées en `file://` (mode hors ligne — polices Google absentes, filtrées comme
attendu). Suite : `tests_lot10.js` — 23 tests, **tous réellement exécutés** le 24/07/2026.

**Résultat : 23 / 23 réussis · aucune erreur JavaScript sur les deux pages.**

## Séquence (15 tests)

| # | Test | Résultat |
|---|---|---|
| 1 | Chargement, titre « SOS jardin connecté » + sous-titre en tête (règle d'or n°4 §1) | ✅ |
| 2 | Badges des 3 codes 4e_C5.1 / C5.2 / C5.3 | ✅ |
| 3 | Onglets séances : bascule vers S2 fonctionnelle | ✅ |
| 4 | Poste de diagnostic : test joué trop tôt → remise à zéro (0/6) | ✅ |
| 5 | Diagnostic : les 6 tests dans l'ordre → cause isolée + verrou `__exp.diag` | ✅ |
| 6 | Activité 1 : 8/8 avec verrou de diagnostic actif | ✅ |
| 7 | Simulateur de remplacement : geste joué trop tôt → remise à zéro (0/6) | ✅ |
| 8 | Remplacement : les 6 gestes dans l'ordre, SANS protocole affiché → verrou `__exp.remplace` | ✅ |
| 9 | Activité 2 : 8/8 (ordre construit + questions) avec verrou | ✅ |
| 10 | Activités 3 et 4 : 7/7 et 4/4 | ✅ |
| 11 | Barre de progression : 4/4 activités validées | ✅ |
| 12 | Sauvegarde localStorage puis rechargement : état intégralement restauré (verrous compris) | ✅ |
| 13 | Blocs règle d'or n°4 (« Prêt·e » + « Bonus ») après le bilan, avant le pied de page, UN SEUL bouton QCM | ✅ |
| 14 | Tous les liens internes de la page pointent vers des fichiers existants (synthèses comprises) | ✅ |
| 15 | Les 3 SVG référencés existent sur le disque | ✅ |

## QCM (8 tests)

| # | Test | Résultat |
|---|---|---|
| 16 | Chargement, titre « SOS jardin connecté », 30 questions annoncées | ✅ |
| 17 | Banque : 30 questions exactement, 10 par code | ✅ |
| 18 | Répartition des bonnes réponses A/B/C/D = 8/7/7/8 (graine 42) et `d[r]` vide pour chaque question | ✅ |
| 19 | 3 questions illustrées (règle images v2), fichiers SVG présents | ✅ |
| 20 | Chaque question : 4 options, explication, exemple, erreur, « à retenir », 3 distracteurs expliqués | ✅ |
| 21 | Une partie démarre et une réponse se joue réellement (correction affichée) | ✅ |
| 22 | Clé localStorage `qcm_4e_C5.1-C5.3_depanner_jardin` | ✅ |
| 23 | Lien de retour vers la séquence valide | ✅ |

## Note sur l'outillage

La répartition des bonnes réponses a été produite par `_outils/fix_r.js` (graine 42).
L'outil, cité par la méthode mais absent du dépôt (non commité lors des LOTs 01-09),
a été **recréé et commité dans ce lot** : permutation déterministe mulberry32 +
Fisher-Yates, échange `o[0]↔o[t]` et `d[0]↔d[t]`, quotas 8/7/7/8.

## Limites du rapport

Tests exécutés uniquement dans l'environnement ci-dessus (Chromium/Playwright).
Aucune compatibilité non testée n'est revendiquée (autres navigateurs : non testés).
La version 🅰 (maquette réelle) relève de l'enseignant et n'est pas testable ici.
