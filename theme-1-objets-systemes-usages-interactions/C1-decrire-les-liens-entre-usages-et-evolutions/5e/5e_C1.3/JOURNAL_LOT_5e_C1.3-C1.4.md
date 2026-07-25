# Journal du lot — conformité 5e_C1.3–C1.4

Date : 25 juillet 2026

## Décisions

1. Remplacer la ressource historique dépendante de six fichiers `_assets` absents par une séquence HTML autonome.
2. Retenir Hangzhou 杭州 — *Hángzhōu* comme ancrage principal du Thème 1, puis demander un transfert argumenté vers la Martinique.
3. Supprimer les sept PNG lourds et non documentés, remplacés par trois SVG originaux accessibles.
4. Revendiquer uniquement deux compétences CRCN disposant d’une action et d’une trace :
   - 1.2 niveau 2 : arborescence et double sauvegarde → capture + ZIP ;
   - 1.3 niveau 2 : insertion, saisie, tri et filtre → ODS/XLSX + PDF.
5. Retirer les anciens éléments Python, conversions de stockage et domaines CRCN décoratifs qui ne correspondaient plus aux trois séances.
6. Migrer le QCM vers le moteur commun et porter la banque à 30 questions avec réponses équilibrées 8/8/7/7.

## Résultats

- séquence : 23/23 ;
- QCM : 35/35 ;
- synthèses : 24/24 ;
- sept PNG retirés ;
- trois SVG originaux de moins de 4 Ko ;
- aucune modification des Thèmes 2 et 3, de `.github/` ou de `_outils/`.

## Intégration racine

L’entrée de nouveauté est préparée dans `ENTREE_NOUVEAUTES_5e_C1.3-C1.4.json`.

La régénération de l’audit ne doit pas être déclarée réussie tant que le dictionnaire `OVERLAY` de `_outils/build_audit.py` conserve l’ancien diagnostic relatif aux PNG et à l’absence de différenciation. Ce script appartient au périmètre du Thème 2 ; le lot ne le modifie pas.
