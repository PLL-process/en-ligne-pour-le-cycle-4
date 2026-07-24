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