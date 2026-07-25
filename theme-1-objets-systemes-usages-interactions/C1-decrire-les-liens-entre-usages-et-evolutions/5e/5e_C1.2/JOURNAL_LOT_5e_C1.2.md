# Journal du lot — 5e_C1.2

Date de consolidation : 25 juillet 2026

## Décisions appliquées

1. Le paquet `5e_C1.2` est une ressource complète distincte : séquence, QCM, synthèses élève et professeur, fiche pédagogique, médias documentés et rapport de tests.
2. La séquence respecte la règle d’or n°4 : titre suivi de la mission, bilan, bloc QCM unique, puis bonus facultatif avant le pied de page.
3. Le QCM historique a été remplacé par l’interface standard commune : identité, sept compteurs de progression, minuteur, modes de travail, navigation, marquage « à revoir », corrections détaillées, reprise et bilan final.
4. L’ancien moteur JavaScript concurrent n’est plus conservé dans la version proposée par la PR #51.
5. La règle d’or n°6 est non applicable : aucune activité ne demande de tracer ou de recopier les deux chaînes.
6. La règle d’or n°7 est appliquée : toute mention CRCN du lot renseigne la compétence exacte, le niveau visé, le repère pour enseigner verbatim, une action observable et une trace produite.
7. Le CRCN retenu est `1.3 — Traiter des données`, niveau 2. Il est exercé dans une activité originale fondée sur un jeu de données entièrement simulées : insertion d’une colonne, saisie, tri, filtre et interprétation.
8. L’ancrage du Thème 1 est ouvert sur Shenzhen 深圳 — *Shēnzhèn*, puis transféré vers Sainte-Luce afin d’interroger la dépendance des choix techniques au territoire.
9. Aucun exercice, tableau ni média du cahier Delagrave n’est reproduit. Seule la logique de progression par niveaux et par actions observables a inspiré une ressource entièrement nouvelle.
10. Aucun contenu des Thèmes 2 et 3, aucun script de `_outils/` et aucun fichier de `.github/` n’est modifié.

## Preuve CRCN du lot

| Exigence | Preuve |
|---|---|
| Compétence exacte | `CRCN 1.3 — Traiter des données` |
| Niveau visé | Niveau 2 |
| Repère verbatim | « Insérer, saisir et trier des données dans un tableur pour les exploiter. » |
| Action observable | Enregistrer le CSV en tableur, insérer une colonne, saisir des priorités, trier et filtrer. |
| Trace produite | Fichier `.ods` ou `.xlsx` transformé et export PDF argumenté. |

Le principe « utiliser un ordinateur n’est pas une compétence » est inscrit explicitement dans l’activité et dans la fiche pédagogique.

## Contrôles statiques réalisés

- situation déclenchante et problématique ;
- trois activités progressives ;
- productions attendues, aides, corrections, exemples et erreurs fréquentes ;
- bouton QCM unique ;
- ordre `Bilan → QCM → Bonus` ;
- chemins relatifs vers les deux SVG, les synthèses et le QCM ;
- présence des 24 questions et de leurs quatre champs pédagogiques de correction ;
- CSV décodé avec 3 lignes de données et 8 colonnes ;
- activité CRCN contenant les cinq mentions obligatoires et un lien relatif vers le CSV.

## Contrôles fonctionnels réalisés

### QCM

Le banc d’essai Chromium headless du 25 juillet 2026 a exécuté **44 contrôles sur 44 avec succès** : chargement, scénarios 20/20, 0/20 et 10/20, compteurs, bilan, minuteur, modes, reprise simulée, clavier, responsive et PDF A4.

### Activité CRCN ajoutée

Le premier passage Chromium a révélé un débordement horizontal de 17 px à 320 px, causé par le nom long du fichier tableur. La feuille de style a été corrigée avec des règles de césure et d’enveloppement.

Le second passage a réussi **16 contrôles sur 16** :

- titre correct ;
- présence de la compétence, du niveau, du repère verbatim, de l’action observable et de la trace ;
- présence du principe anti-CRCN décoratif ;
- lien CSV correct et fichier présent ;
- tableau et correction dépliable présents ;
- aucun débordement à 320, 768 et 1440 px ;
- PDF A4 généré ;
- aucune erreur console.

La politique de sécurité du conteneur bloquant les navigations vers `file://` et `localhost`, les pages ont été chargées dans Chromium par injection contrôlée du contenu HTML. Les liens relatifs ont été contrôlés séparément sur le système de fichiers.

## État de livraison

Le lot est en revalidation après ajout de l’activité CRCN. Il pourra repasser en revue dès que le rapport et le manifeste seront synchronisés et que la garde de périmètre finale sera verte.
