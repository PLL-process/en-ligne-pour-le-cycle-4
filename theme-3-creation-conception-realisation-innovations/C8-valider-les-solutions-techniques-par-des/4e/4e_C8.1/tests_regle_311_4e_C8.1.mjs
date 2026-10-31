/* Banc de la règle d'or n°311 pour 4e_C8.1 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Pilote du passage à onglets des séquences du thème 3 qui n'en avaient pas (31/10/2026) : trois séances, l'ouverture dans le
   volet « 📖 Rappel » dès la séance 2. Un outil n'est pas du décor : le sélecteur de parcours, ses deux zones role=status, la
   progression et « 🗺 Où j'en suis » servent aux séances 2 et 3 ; ils restent hors du volet.
   Le lien direct #act3 (améliorations) ouvre la séance 3, ouverture repliée.
   Usage : node tests_regle_311_4e_C8.1.mjs [--captures <dossier>] */
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_4e_C8_jardin-validation.html',
  code: '4e_C8.1',
  champ: '#hypothese',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'act3',
  panneauSN: 's3',
  outils: ['.choix-parcours-boutons', '#parcoursNote', '#savedNote', '.progress-wrap', '#taches'],
});
