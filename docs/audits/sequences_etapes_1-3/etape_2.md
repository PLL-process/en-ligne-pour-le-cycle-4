# Audit des séquences cycle 4 — Étape 2

Date : 1er novembre 2026. Périmètre : examen documentaire de pages publiques, sans exécution instrumentée de navigateur ni accès au code source complet. Les tests non réalisés ne sont pas présentés comme réussis ou échoués.

## Fiche A — Traçabilité des compétences mutualisées
- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html
- Emplacement : thème 2, 4e_C4.2 à C4.6 et 3e_C4.4 à C4.6 ; thème 3, repères mutualisés.
- Constat vérifié : plusieurs repères portent la mention « Couvert par une séquence mutualisée » et simultanément « Aucune ressource pédagogique publiée pour ce repère ».
- Problème : la page d'index ne permet pas de remonter directement de chaque compétence à l'activité, à la production et à l'évaluation correspondantes. Cela ne démontre pas une absence de traitement dans les séquences.
- Priorité : élevée (traçabilité).
- Correction : ajouter un lien profond vers la séquence mutualisée, l'ancre de l'activité, le livrable et le critère observable ; distinguer « mutualisé et accessible » de « à documenter ».

## Fiche B — Jardin connecté, modèle numérique du capteur
- URL : https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html
- Emplacement : activité 3, « Le voyage de la donnée », paragraphes « La mesure brute (612) devient une donnée utile (60 %) » et correction « division par 1023 ».
- Constat vérifié : la page associe 612 à 60 % et mentionne la division par 1023.
- Problème : 612 / 1023 × 100 ≈ 59,82 %, soit 60 % après arrondi ; la conversion nécessite explicitement multiplication par 100 et arrondi. Surtout, ce pourcentage est une normalisation du signal, pas nécessairement une humidité physique étalonnée du sol ; certains capteurs sont inversés et demandent calibration.
- Priorité : élevée (rigueur scientifique).
- Correction : écrire la formule complète et préciser « indice d'humidité simulé, étalonné pour l'exercice », avec deux points de calibration si l'on prétend mesurer l'humidité du sol.

## Fiche C — Jardin connecté, affirmation de sécurité
- Même URL que fiche B.
- Emplacement : séance 4, lexique de l'exercice cahier des charges, entrée « tension d'alimentation ».
- Constat vérifié : la page affirme « 12 V est une très basse tension, sans danger au toucher ».
- Problème : formulation trop absolue : la sécurité dépend également de la source, du courant disponible, de l'humidité, des défauts et de l'installation.
- Priorité : élevée (sécurité).
- Correction : « Dans la maquette pédagogique, utiliser une alimentation 12 V continue adaptée et protégée, sous supervision ; ne jamais intervenir sur une installation sous tension. »

## Fiche D — Jardin connecté, portée de l'évaluation
- Même URL que fiche B.
- Emplacement : activités 1 à 4, critères « 9/9 », « 4/4 », « 3/3 et 6/6 », « 3 pannes et 4/4 ».
- Constat vérifié : la page énonce des scores de réponses et des productions manuscrites.
- Risque à vérifier : le compteur peut valider les réponses sélectionnées sans vérifier le schéma recopié, l'argumentation ou la compréhension. Aucune conclusion sur le JavaScript n'est possible sans exécution.
- Priorité : moyenne.
- Correction : séparer « quiz réussi » et « compétence validée par production », avec grille critériée et contrôle enseignant.

## Fiche E — Jardin connecté, simplification réseau
- Même URL que fiche B.
- Emplacement : activité 4, correction du dépannage réseau.
- Constat vérifié : la règle « IP fixe libre et hors plage DHCP » est présentée comme générale.
- Problème : simplification pédagogique utile, mais une réservation DHCP est également une solution ; hors plage DHCP n'est pas la seule manière de prévenir les conflits.
- Priorité : faible.
- Correction : ajouter une note « autre possibilité : réservation DHCP sur le routeur ».

## Fiche F — Station d'alerte cyclonique : preuves à réunir
- URL thème 2 : https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.3/sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html
- URL thème 3 : https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html
- Constat vérifié : deux séquences distinctes existent, l'une pour la chaîne d'information, l'autre pour la programmation et l'interaction.
- Vérifications restant à exécuter : cohérence des seuils et unités, distinction simulation/alerte officielle, comportement aux valeurs limites, aux capteurs déconnectés et aux données manquantes, traçabilité des compétences C4.3–C4.6, C9.2 et C8.3.
- Priorité : élevée ; statut : test non réalisé.

## Campagne technique à exécuter sur le dépôt cloné
1. Inventorier tous les boutons « Vérifier » et identifier leurs fonctions JavaScript.
2. Pour chaque champ : tester réponse correcte, variante équivalente, casse/accents/espaces, réponse vide, texte arbitraire, HTML, nombres hors plage, valeur limite.
3. Tester la navigation Tab/Shift+Tab/Entrée/Espace, l'affichage du focus, les annonces de résultats et les messages d'erreur.
4. Mesurer les contrastes WCAG AA, contrôler les `alt` et les intitulés des contrôles, le zoom 200 % et les largeurs 320/375/768 px.
5. Vérifier tous les liens HTTP, chemins relatifs, ressources téléchargées, fichiers CSV (encodage, séparateur, colonnes, cohérence), erreurs de console, stockage local et impression.
6. Construire une matrice exhaustive : compétence officielle → URL/ancre → consigne → action élève → production → critère → mode de preuve.

## Limites de cette étape
Audit documentaire partiel : aucun résultat de test de navigateur, de JavaScript, de clavier, de CSV ou de sauvegarde ne peut encore être certifié. Ne pas confondre la présence d'un lien ou d'un fichier de test dans l'index avec son exécution réussie.
