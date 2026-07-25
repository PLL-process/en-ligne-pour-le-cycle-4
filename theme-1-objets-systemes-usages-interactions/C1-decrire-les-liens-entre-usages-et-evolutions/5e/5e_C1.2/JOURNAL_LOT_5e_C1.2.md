# Journal du lot — 5e_C1.2

Date de consolidation : 25 juillet 2026

## Décisions appliquées

1. Le paquet `5e_C1.2` est une ressource complète distincte : séquence, QCM, synthèses élève et professeur, fiche pédagogique, médias documentés et rapport de tests.
2. La séquence respecte la règle d’or n°4 : titre suivi de la mission, bilan, bloc QCM unique, puis bonus facultatif avant le pied de page.
3. Le QCM historique a été remplacé par l’interface standard commune : identité, sept compteurs de progression, minuteur, modes de travail, navigation, marquage « à revoir », corrections détaillées, reprise et bilan final.
4. L’ancien moteur JavaScript concurrent n’est plus conservé dans la version proposée par la PR #51.
5. La règle d’or n°6 est non applicable : aucune activité ne demande de tracer ou de recopier les deux chaînes.
6. Aucun contenu des Thèmes 2 et 3, aucun script de `_outils/` et aucun fichier de `.github/` n’est modifié.

## Contrôles statiques réalisés

- situation déclenchante et problématique ;
- trois activités progressives ;
- productions attendues, aides, corrections, exemples et erreurs fréquentes ;
- bouton QCM unique ;
- ordre `Bilan → QCM → Bonus` ;
- chemins relatifs vers les deux SVG, les synthèses et le QCM ;
- présence des 24 questions et de leurs quatre champs pédagogiques de correction.

## Contrôles fonctionnels réalisés

Le banc d’essai Chromium headless du 25 juillet 2026 a exécuté **44 contrôles sur 44 avec succès** :

- chargement JavaScript ;
- scénarios tout juste, tout faux et mixte connu ;
- calcul des notes 20/20, 0/20 et 10/20 ;
- compteurs et bilan par notion ;
- minuteur, pause et reprise ;
- cinq modes de travail ;
- identité, réponse et marquage restaurés par la logique de reprise ;
- interaction au clavier ;
- affichages 320, 768 et 1440 px sans débordement horizontal ;
- média d’impression et génération PDF A4.

La politique de sécurité du conteneur bloquant les navigations vers `file://` et `localhost`, la reprise a été vérifiée avec une implémentation compatible de `localStorage` injectée dans le banc. L’essai du stockage natif dans Edge reste un contrôle post-publication et n’est pas déclaré réussi.

## État de livraison

Le lot est **prêt pour revue**. Les seuls contrôles restant après fusion sont : essai tactile physique, stockage natif dans Edge ou Firefox, impression physique et validation des liens sur GitHub Pages.
