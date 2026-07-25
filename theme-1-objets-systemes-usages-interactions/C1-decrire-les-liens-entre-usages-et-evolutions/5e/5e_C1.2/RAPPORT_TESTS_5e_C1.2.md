# Rapport de tests — lot 5e_C1.2

Date : 25 juillet 2026

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

La liste complète des fichiers modifiés dans la PR #51 a été récupérée une nouvelle fois via l’API GitHub. Les neuf chemins modifiés sont tous situés dans `theme-1-objets-systemes-usages-interactions/.../5e/5e_C1.2/` :

1. `FICHE_PEDAGOGIQUE_5e_C1.2.md` ;
2. `JOURNAL_LOT_5e_C1.2.md` ;
3. `MANIFESTE_LOT_5e_C1.2.json` ;
4. `MANIFESTE_LOT_5e_C1.2.md` ;
5. `MIGRATION_QCM_5e_C1.2.md` ;
6. `RAPPORT_TESTS_5e_C1.2.md` ;
7. `qcm_principes_techniques.html` ;
8. `synthese_eleve_5e_C1.2.html` ;
9. `synthese_professeur_5e_C1.2.html`.

Résultat : aucune modification détectée dans les Thèmes 2 ou 3, dans `.github/` ou dans `_outils/`.

### Recontrôle de périmètre GitHub exécuté le 25 juillet 2026

- la liste des fichiers modifiés de la PR #51 a été récupérée de nouveau via l’API GitHub après la reprise de connexion ;
- le total reste de neuf fichiers ;
- les neuf chemins correspondent exactement à la liste ci-dessus ;
- aucun fichier racine, aucun fichier des Thèmes 2 ou 3, aucun fichier de `.github/` et aucun script de `_outils/` n’apparaît dans le diff ;
- la PR reste déclarée fusionnable par GitHub au moment du contrôle.

Résultat : le périmètre du lot reste strictement conforme après reprise des travaux.

### Validation structurée du manifeste — 25 juillet 2026

- le fichier `MANIFESTE_LOT_5e_C1.2.json` a été relu et décodé via l’API GitHub sans erreur de structure ;
- les champs obligatoires du lot ont été vérifiés : code, niveau, thème, compétence, séquence, QCM, synthèses, règles, périmètre et tests ;
- l’entrée préparée pour `nouveautes.json` cible uniquement `5e_C1.2`, le Thème 1 et les chemins du dossier dédié ;
- les étapes restantes sont explicitement conservées dans le manifeste et ne sont pas déclarées terminées.

### Manifeste de livraison

- un manifeste consolidé du lot a été créé ;
- il inventorie les ressources, les règles appliquées, le périmètre et les étapes restantes ;
- une version JSON structurée et un journal local de lot ont été ajoutés pour préparer l’intégration dans les fichiers racine ;
- la règle d’or n°6 est explicitement déclarée non applicable à cette séquence, car aucune activité ne demande de tracer ou recopier les deux chaînes.

### Paquet pédagogique

- synthèse élève créée ;
- synthèse professeur créée ;
- fiche pédagogique créée ;
- QCM séparé de 24 questions migré ;
- registre `SOURCES_MEDIAS.md` présent ;
- manifeste Markdown et manifeste JSON créés ;
- journal local de lot créé.

### Recontrôle automatisé du diff — 25 juillet 2026

- la liste des fichiers de la PR #51 a été interrogée une nouvelle fois par l’API GitHub ;
- neuf fichiers sont toujours présents dans le diff ;
- les neuf chemins appartiennent exclusivement au dossier `5e_C1.2` du Thème 1 ;
- aucune dérive vers les Thèmes 2 ou 3, `.github/`, `_outils/` ou un fichier partagé racine n’a été détectée ;
- ce contrôle a été ajouté au rapport dans le commit `test(theme1): consigner le recontrôle de périmètre de la PR 51`.

### Reprise de travail après interruption réseau — 25 juillet 2026

- la PR #51 a été réinterrogée après rétablissement de la connexion ;
- GitHub retourne toujours exactement neuf fichiers modifiés ;
- chaque chemin est strictement contenu dans le dossier `5e_C1.2` du Thème 1 ;
- aucun fichier des Thèmes 2 et 3, aucun fichier de `.github/`, aucun script de `_outils/` et aucun fichier racine partagé n’est présent dans le diff ;
- le contrôle a été effectué via l’API GitHub, sans dépendre du poste local de Pascal.

Résultat : la reprise n’a introduit aucune dérive de périmètre et le lot peut poursuivre sa finalisation sur la même branche.

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
