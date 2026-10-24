/* Banc de la règle d'or n°311 pour 3e_C6.2 — voir banc_regle_311_theme2.mjs (relais du thème 2 vers le banc commun du thème 1).
   Usage : node tests_regle_311_3e_C6.2.mjs [--captures <dossier>] */
import { lancerBanc311Theme2 } from '../../../banc_regle_311_theme2.mjs';

await lancerBanc311Theme2({
  dossier: import.meta.dirname,
  page: 'sequence_3e_C6.2_auto_test_station.html',
  code: '3e_C6.2',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'fb0',
  ancreSN: 'fb5',
  panneauSN: 'seance3',
});
