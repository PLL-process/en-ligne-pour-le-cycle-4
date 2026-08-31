# Rapport de tests — Lot 4e_C6.1 · C6.3 « Ajuster le programme du jardin »

**Environnement réel d'exécution** : Chromium (Playwright), viewport mobile 390×844,
pages chargées en `file://` (mode hors ligne — polices Google absentes, filtrées comme
attendu). Suite : `tests_lot11.js` — 23 tests, **tous réellement exécutés** le 24/07/2026.

> **Ce script n'est pas dans le dépôt et n'y a jamais été commité** — les coches ci-dessous disent ce qui a été observé ce jour-là, elles ne sont pas rejouables aujourd'hui (règle d'or n°259, relevé du 31/08/2026 par `_outils/controle_rapports_tests.py`). La suite reste à écrire.

**Résultat : 23 / 23 réussis · aucune erreur JavaScript · aucune requête locale échouée.**

## Séquence (15 tests)

| # | Test | Résultat |
|---|---|---|
| 1 | Chargement, titre « Ajuster le programme du jardin » + sous-titre en tête (règle d'or n°4 §1) | ✅ |
| 2 | Badges des 2 codes 4e_C6.1 / 4e_C6.3 | ✅ |
| 3 | Onglets séances : bascule vers S2 fonctionnelle | ✅ |
| 4 | Activité 1 : 5/5 (anomalies + causes logicielles) | ✅ |
| 5 | Activité 2 : 5/5 (algorithme corrigé : hystérésis + plage horaire) | ✅ |
| 6 | Vérificateur 3 SANS scénarios joués : refus + rappel du banc (verrou actif) | ✅ |
| 7 | Banc de test : ordre LIBRE accepté (scénario 2 joué en premier → 1/4) | ✅ |
| 8 | Banc : les 4 scénarios joués → programme validé en simulation + verrou `__exp.scen` | ✅ |
| 9 | Activité 3 : 6/6 (verdicts + sauvegarde + non-régression) avec verrou | ✅ |
| 10 | Activité 4 : 4/4 (transfert lampadaire) | ✅ |
| 11 | Barre de progression : 4/4 activités validées + coches des 2 onglets | ✅ |
| 12 | Sauvegarde localStorage puis rechargement : état intégralement restauré (verrou compris) | ✅ |
| 13 | Blocs règle d'or n°4 (« Prêt·e » + « Bonus ») après le bilan, avant le pied de page, UN SEUL bouton QCM | ✅ |
| 14 | Tous les liens internes (dont LOT 10, 4e_C6.2 et 4e_C4.1) pointent vers des fichiers existants | ✅ |
| 15 | Les 3 SVG référencés existent sur le disque | ✅ |

## QCM (8 tests)

| # | Test | Résultat |
|---|---|---|
| 16 | Chargement, titre « Ajuster le programme du jardin », 30 questions annoncées | ✅ |
| 17 | Banque : 30 questions exactement, 15 par code | ✅ |
| 18 | Répartition des bonnes réponses A/B/C/D = 8/7/7/8 (graine 57, `_outils/fix_r.js`) et `d[r]` vide pour chaque question | ✅ |
| 19 | 3 questions illustrées (règle images v2) | ✅ |
| 20 | Chaque question : 4 options, explication, exemple, erreur, « à retenir », 3 distracteurs expliqués | ✅ |
| 21 | Une partie démarre et une réponse se joue réellement (correction affichée) | ✅ |
| 22 | Clé localStorage `qcm_4e_C6.1-C6.3_ajuster_programme_jardin` | ✅ |
| 23 | Lien de retour vers la séquence valide | ✅ |

## Limites du rapport

Tests exécutés uniquement dans l'environnement ci-dessus (Chromium/Playwright).
Aucune compatibilité non testée n'est revendiquée (autres navigateurs : non testés).
La version 🅰 (programme réel Vittascience/mBlock + maquette) relève de l'enseignant
et n'est pas testable ici. La séquence modèle 4e_C6.2 n'a pas été modifiée et n'entre
pas dans le périmètre de ce rapport.
