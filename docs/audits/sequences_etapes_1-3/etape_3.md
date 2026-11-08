# Audit des séquences cycle 4 — Étape 3
Date : 1 novembre 2026

## Périmètre et méthode
Lecture de l'index public https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html . L'accès au dépôt par clonage a échoué (résolution DNS). Aucun test dynamique JavaScript ou navigateur n'a donc été réalisé durant cette étape. Ne pas interpréter les contrôles à faire comme des défauts prouvés.

## Observations vérifiées

### A3-01 — 5e_C1.6 — Traçabilité indirecte
- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html
- Emplacement : Thème 1 > C1 > 5e > 5e_C1.6
- Constat : repère affiché « Couvert par une séquence mutualisée » et « Aucune ressource pédagogique publiée pour ce repère ».
- Gravité : moyenne, défaut de traçabilité directe ; ne prouve pas l'absence d'enseignement.
- Correction : ajouter l'URL de la séquence mutualisée, l'activité précise, la production attendue et son critère de réussite.

### A3-02 — 3e_C1.2 — Traçabilité indirecte
- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html
- Emplacement : Thème 1 > C1 > 3e > 3e_C1.2
- Constat : « Couvert par une séquence mutualisée » mais « Aucune ressource pédagogique publiée pour ce repère ».
- Gravité : moyenne.
- Correction : lien direct vers une activité où l'élève met en relation une découverte scientifique, un développement technologique et des effets sociétaux ; ajouter un critère d'évaluation explicite.

### A3-03 — 3e_C1.4 — Traçabilité indirecte
- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html
- Emplacement : Thème 1 > C1 > 3e > 3e_C1.4
- Constat : « Couvert par une séquence mutualisée » mais « Aucune ressource pédagogique publiée pour ce repère ».
- Gravité : moyenne.
- Correction : lien direct vers la consigne d'argumentaire sur les contraintes sociétales, la production attendue et la grille critériée.

## Plan de tests restant à exécuter
1. Thèmes 2 et 3 : relever les pages réelles, confronter capteurs et seuils aux documents de référence ; distinguer valeurs simulées, mesurées et calibrées.
2. Boutons Vérifier : tester vide, texte arbitraire, réponse exacte, synonyme, casse, accents, espaces, réponse partiellement correcte et injection HTML ; observer la validation effective.
3. Accessibilité : parcours Tab/Maj+Tab/Entrée/Espace, focus visible, libellés, textes alternatifs, contrastes mesurés, zoom 200 %, orientation mobile et tablette.
4. Technique : contrôler chaque URL, fichiers CSV (séparateur, encodage, en-têtes, cohérence), erreurs console, stockage local et fonctionnement en navigation privée/poste partagé.
5. Compétences : produire pour chaque repère une ligne « libellé officiel — séquence URL — paragraphe — activité — trace élève — critère — résultat du contrôle ».

## Limite
Les trois constats ci-dessus concernent uniquement la présentation de l'index. Le code source et le comportement des interfaces n'ont pas été audités dans cette étape.
