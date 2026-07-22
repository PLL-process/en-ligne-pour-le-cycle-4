# LOT pilote — 5e_C1.3–C1.4

## Éléments réalisés

- séquence élève enrichie et liée au QCM ;
- CodeLab Techno intégré au programme Python : coloration syntaxique, numéros de lignes, édition, sauvegarde locale, copie, taille, retour à la ligne, plein écran et export `.py` ;
- sauvegarde locale des réponses de la séquence ;
- QCM séparé porté à 30 questions, dont 6 consacrées au programme Python ;
- 30 corrections structurées avec bonne réponse, raisonnement, exemple, erreur fréquente, distracteurs et encadré « À retenir » ;
- progression du QCM : répondues, correctes, incorrectes, restantes et barre globale ;
- minuteur avec démarrage, pause, reprise et temps final ;
- navigation directe, filtres, impression, reprise locale et réessai des erreurs ;
- interactions tactiles ajoutées aux classements ;
- parcours de conversions organisé en 10 exercices essentiels et 20 approfondissements ;
- activité sur les mémoires réorganisée en parcours essentiel et approfondissement ;
- mémoire CMOS retirée du classement binaire et expliquée comme cas particulier alimenté par une pile ;
- matrice de couverture notion → activité → questions ;
- synthèse élève ajoutée : `synthese_eleve_5e_C1.3-C1.4.html` ;
- synthèse professeur ajoutée : `synthese_professeur_5e_C1.3-C1.4.html`.

## Contrôles réellement effectués

- contrôle de présence des 30 questions et des 30 entrées de correction lors des passes précédentes ;
- contrôle statique des liens réciproques entre séquence et QCM ;
- contrôle statique des deux synthèses : métadonnée viewport, structure HTML fermée, liens relatifs vers la séquence et le QCM ;
- vérification du périmètre GitHub : aucun fichier du Thème 2 dans la Pull Request ;
- vérification du script de progressivité par relecture statique : ciblage du titre des mémoires, séparation des termes avancés et traitement explicite de CMOS.

## Contrôles encore nécessaires avant fusion

- exécution complète des tests JavaScript dans un navigateur ;
- test réel de sauvegarde et reprise du QCM ;
- test réel du minuteur, de la pause et du réessai ;
- test réel de CodeLab Techno : copie, export, réinitialisation et reprise ;
- test des classements à la souris, au clavier et sur écran tactile ;
- aperçu ordinateur, tablette et téléphone ;
- vérification finale des liens et médias externes.

La tentative d’exécution locale de `node --check` a rencontré une erreur transitoire de l’environnement d’exécution. Elle n’est donc pas comptabilisée comme un test réussi.

## Statut

Le lot reste en Pull Request brouillon. Il ne doit pas être fusionné dans `main` avant la réussite des contrôles fonctionnels ci-dessus.
