/* Banc de la règle d'or n°311 pour 3e_C9.1 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Un outil n'est pas du décor : le sélecteur de parcours, ses deux zones role=status, la progression et « 🗺 Où en suis-je ? »
   servent à chaque séance ; ils restent hors du volet.
   Usage : node tests_regle_311_3e_C9.1.mjs [--captures <dossier>] */
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_3e_C9.1_variables_types_systemes.html',
  code: '3e_C9.1',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act1',
  ancreSN: 'act5',
  panneauSN: 's4',
  outils: ['.choix-parcours-boutons', '#parcoursNote', '#savedNote', '.progress-wrap', '#taches'],
});
