# Rapport de tests — lot 5e_C1.3–C1.4

Date : 25 juillet 2026

Branche : `codex/theme-1/conformite-5e-c1-3-c1-4`

## Ressources testées

- `sequence_C1.3-C1.4_SI_gestion_donnees.html`
- `qcm_systemes_information_donnees.html`
- `donnees_velos_hangzhou_simulees.csv`
- trois SVG originaux
- synthèses élève et professeur

## Séquence — 23 contrôles sur 23 réussis

- aucune dépendance CSS, JS ou police externe ;
- titre, mission, situation déclenchante et problématique ;
- trois séances progressives ;
- deux blocs CRCN contenant compétence exacte, niveau, repère verbatim, action observable et trace ;
- principe « utiliser un ordinateur n’est pas une compétence » ;
- règle d’or n°4 : bilan, bloc QCM unique, bonus, pied de page ;
- un seul bouton vers le QCM ;
- liens locaux vers QCM, synthèses, CSV et images ;
- CSV : 8 lignes de données, 7 colonnes ;
- règle de priorité vérifiée : V-104, V-105, V-108 et V-112 ;
- sauvegarde locale des trois réponses textuelles ;
- aucun débordement à 320, 768 et 1440 px ;
- PDF A4 généré : 197 265 octets ;
- aucune erreur console.

## QCM — 35 contrôles sur 35 réussis

- 30 questions et 3 questions illustrées ;
- répartition des bonnes réponses : A 8, B 8, C 7, D 7 ;
- quatre champs d’identité ;
- sept compteurs ;
- cinq modes de travail ;
- grille de 30 questions ;
- minuteur : démarrage, pause et reprise ;
- mode 10 questions ;
- révision ciblée « traitement des données » : 9 questions ;
- mode questions marquées ;
- identité sauvegardée ;
- sélection et validation au clavier ;
- scénario tout juste : 30/30, 20,0/20 ;
- scénario tout faux : 0/30, 0,0/20 ;
- scénario mixte : 15/30, 10,0/20 ;
- réessai des 15 erreurs ;
- bilan sur cinq catégories ;
- corrections détaillées : explication, exemple, erreur fréquente, à retenir ;
- aucun débordement à 320, 768 et 1440 px ;
- PDF A4 généré : 202 680 octets ;
- aucune erreur console.

## Synthèses — 24 contrôles sur 24 réussis

- titre et liens de retour ;
- affichage à 320, 768 et 1440 px ;
- aucun débordement après correction du tableau CRCN de la synthèse élève ;
- aucune erreur console ;
- contenu aligné sur les trois séances, sans ancien développement Python hors parcours.

## Médias

- trois SVG locaux : environ 1,8 à 3,2 Ko ;
- textes alternatifs présents ;
- aucune image externe ;
- retrait des sept PNG lourds et non documentés.

## Contrôles non déclarés comme réussis

- ouverture du CSV dans Excel sur Windows ;
- ouverture du CSV dans LibreOffice Calc sur les postes du collège ;
- essai tactile sur appareil physique ;
- impression sur imprimante physique ;
- validation des liens après publication sur GitHub Pages.

## Conclusion

Le paquet est fonctionnel, accessible et conforme aux règles d’or n°4 et n°7. La règle n°6 n’est pas applicable : aucune consigne ne demande de tracer les chaînes d’information et d’énergie.
