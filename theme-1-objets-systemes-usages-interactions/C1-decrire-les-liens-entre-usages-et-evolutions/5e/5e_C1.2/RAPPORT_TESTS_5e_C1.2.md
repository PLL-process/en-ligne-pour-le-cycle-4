# Rapport de tests — lot 5e_C1.2

Date : 24 juillet 2026

## Contrôles réellement exécutés

Les fichiers ont été relus depuis la branche GitHub après chaque mise à jour.

### Séquence élève

- titre avec emoji présent ;
- sous-titre de mission immédiatement après le titre ;
- situation déclenchante et problématique présentes ;
- trois activités distinctes et progressives ;
- chaque activité comprend consigne, production attendue, aide, correction ou exemple de correction et erreur fréquente ;
- bilan placé avant les blocs de fin ;
- un seul bouton « Ouvrir le QCM d’entraînement » ;
- bloc QCM placé après le bilan ;
- bloc bonus facultatif placé après le QCM ;
- deux images SVG avec textes alternatifs ;
- liens relatifs vers les deux images et le QCM vérifiés statiquement.

### QCM migré vers le moteur commun

- en-tête standard vérifié : titre, sous-titre, badges niveau/code/nombre de questions et lien de retour ;
- quatre champs d’identité présents : Nom, Prénom, Classe, Date ;
- carte « Ma progression » avec les sept compteurs permanents ;
- minuteur avec démarrage, pause et option sans minuteur ;
- quatre modes de travail : complet, 10 questions, erreurs, questions marquées ;
- grille de navigation, marquage « À revoir », validation et bilan final présents ;
- banque de 24 questions vérifiée statiquement ;
- chaque question contient une explication, un exemple, une erreur fréquente et un « À retenir » ;
- sauvegarde locale et reprise présentes dans le code ;
- styles responsive, focus visible et impression A4 présents ;
- l’ancien moteur concurrent a été entièrement remplacé.

### Contrôle d’intégrité complémentaire du 24 juillet 2026

- relecture du QCM directement depuis la branche `codex/theme-1/finaliser-5e-c1-2` ;
- vérification de la présence du lien de retour vers `sequence_5e_C1.2_principes_techniques.html` ;
- vérification de la présence simultanée des 7 compteurs, du minuteur, des 4 modes et de la grille de navigation ;
- vérification que la banque annoncée comporte bien 24 questions et qu’aucun second moteur QCM n’est conservé dans le fichier ;
- vérification du périmètre : les fichiers relus et modifiés restent dans le dossier du Thème 1.

### Contrôle de périmètre GitHub exécuté le 24 juillet 2026

La liste complète des fichiers modifiés dans la PR #51 a été récupérée via l’API GitHub puis contrôlée. Les six chemins modifiés sont tous situés dans `theme-1-objets-systemes-usages-interactions/.../5e/5e_C1.2/` :

1. `FICHE_PEDAGOGIQUE_5e_C1.2.md` ;
2. `MIGRATION_QCM_5e_C1.2.md` ;
3. `RAPPORT_TESTS_5e_C1.2.md` ;
4. `qcm_principes_techniques.html` ;
5. `synthese_eleve_5e_C1.2.html` ;
6. `synthese_professeur_5e_C1.2.html`.

Résultat : aucune modification détectée dans les Thèmes 2 ou 3, dans `.github/` ou dans `_outils/`.

### Paquet pédagogique

- synthèse élève créée ;
- synthèse professeur créée ;
- fiche pédagogique créée ;
- QCM séparé de 24 questions migré ;
- registre `SOURCES_MEDIAS.md` présent.

## Tests non déclarés comme réussis

Les vérifications suivantes restent à exécuter avant de qualifier le paquet de « complet et validable » :

- exécution fonctionnelle réelle dans Chromium, Firefox ou Edge ;
- parcours complet au clavier sans souris ;
- scénarios scriptés tout juste, tout faux et mixte connu ;
- fermeture puis reprise réelle depuis le stockage local ;
- test tactile réel ;
- test d’impression physique ;
- validation des liens sur GitHub Pages après fusion.

Aucun de ces tests n’est déclaré réussi tant qu’il n’a pas été réellement exécuté.
