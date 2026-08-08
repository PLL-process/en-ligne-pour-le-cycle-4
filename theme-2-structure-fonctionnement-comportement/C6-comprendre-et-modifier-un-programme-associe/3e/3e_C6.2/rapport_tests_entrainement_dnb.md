# Rapport de tests — Entraînement DNB « algorigrammes »

**Date** 08/08/2026 · **Agent** Fable (Thème 2) · **Branche** `fable/theme-2/entrainement-dnb-algorigrammes`

Ce rapport ne déclare **que des tests réellement exécutés** :

```
python3 tests_entrainement_dnb.py     # depuis ce dossier, Playwright + Chromium
```

## Résultat : 21 / 21 tests passés

| Test exécuté | Résultat |
|---|---|
| aucune erreur JavaScript au chargement | ✅ passé |
| 30 exercices présents | ✅ passé |
| chaque exercice propose 4 options plus le choix vide | ✅ passé |
| chaque liste déroulante porte une étiquette (n°34) | ✅ passé |
| chaque exercice a 2 aides et 1 correction | ✅ passé |
| chaque correction réfute les 3 distracteurs | ✅ passé |
| corrections repliées au chargement | ✅ passé |
| images avec alternative textuelle de plus de 40 caractères | ✅ passé |
| bandeau de tâches affiché (n°30) | ✅ passé |
| bonnes réponses réparties sur les 4 positions (8/8/7/7) | ✅ passé |
| manche 1 : score parfait reconnu | ✅ passé |
| progression mise à jour après vérification | ✅ passé |
| bandeau coché après validation | ✅ passé |
| manche 2 : les exercices sans réponse sont signalés | ✅ passé |
| mode essentiel masque corrections et rappel de cours (n°29) | ✅ passé |
| mode essentiel laisse les exercices et les aides | ✅ passé |
| réponses et progression restaurées après rechargement | ✅ passé |
| les 4 onglets affichent leur bandeau | ✅ passé |
| pas de défilement horizontal à 1280 px | ✅ passé |
| pas de défilement horizontal à 420 px | ✅ passé |
| liens internes vers les séquences présents | ✅ passé |

## Deux défauts trouvés par les tests, et corrigés

**La répartition des bonnes réponses.** Le premier tirage aléatoire plaçait **15 bonnes réponses
sur 30 en position C**. Un élève qui répond C au hasard aurait eu la moyenne sans rien lire. Le
générateur applique désormais une répartition déterministe — 8 / 8 / 7 / 7 — comme le fait
`_outils/fix_r.js` pour les QCM. Le test vérifie que les quatre positions sont servies.

**Un test qui mentait, pas la page.** Le contrôle « le mode essentiel laisse les exercices
visibles » échouait : il interrogeait le premier exercice de la page, qui appartient à la manche 1
— masquée puisque le test venait de basculer sur la manche 2. Le test cible maintenant le panneau
actif. La page, elle, était correcte.

## Ce que la suite ne couvre pas

Le rendu à l'impression A4, le contraste mesuré point par point, la lecture par un vrai lecteur
d'écran et le zoom navigateur à 200 % **n'ont pas été vérifiés automatiquement**. Ils sont donc
déclarés **non vérifiés**, et non « conformes ».

## Vérificateur des règles d'or

La page n'est pas nommée `sequence_*.html` : elle n'entre donc pas dans le champ de
`_outils/verif_regles_audit.py`, qui audite les séquences. Les règles applicables ont été tenues à
l'écriture et vérifiées par la suite ci-dessus : n°29 (mode essentiel), n°30 (bandeau), n°33
(aération), n°34 (étiquettes, alternatives, absence de défilement horizontal).

La règle n°31 (version étayée) est **sans objet** : la page ne demande aucune production écrite,
toutes les réponses se font par liste déroulante — un choix assumé pour les élèves DYS, hérité de
la méthode du dépôt.

## L'ancienne banque, laissée en place

`sequence_algorigrammes_dnb.html` et `qcm_algorigrammes_dnb.html` ne sont **pas modifiés ni
déplacés**. Quatorze fichiers du dépôt y font référence, dont la séquence 3e_C6.1 et plusieurs
fichiers générés : les déplacer casserait ces liens et dépasserait le périmètre de ce lot.

Conséquence assumée : l'ancienne banque reste signalée sans mode essentiel, et c'est **le dernier
manquement mécanique du Thème 2**. Son archivage relève d'une décision de gouvernance, pas d'un
correctif technique.
