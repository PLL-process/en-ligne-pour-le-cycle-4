/* Banc de la règle d'or n°311 pour 5e_C7.1 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 (même gabarit) : la page d'un seul tenant passe à trois séances à
   onglets, l'ouverture dans le volet « 📖 Rappel » dès la séance 2. Un outil n'est pas du décor : le sélecteur de parcours, ses
   deux zones role=status, la progression et « 🗺 Où j'en suis » servent à chaque séance ; le simulateur de place sert aux
   séances 1 et 2 (activités 0 et 2) — un seul nœud, que le script range dans la séance ouverte, sous son en-tête. Tous restent
   hors du volet.
   La page ne portait ni la chaîne « rappel-ouverture » ni d'exercice incrusté des ateliers (vérifié le 04/11/2026).
   Le lien direct #act2 (la grille de validation) ouvre la séance 2, ouverture repliée.
   Usage : node tests_regle_311_5e_C7.1.mjs [--captures <dossier>] */
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_5e_C7_mini-projet-objet.html',
  code: '5e_C7.1',
  champ: '#idee0',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'act2',
  panneauSN: 's2',
  outils: ['.toolbar', '.choix-parcours-boutons', '#parcoursNote', '#savedNote', '.progress-wrap', '#taches', '#outilSimu'],
});
