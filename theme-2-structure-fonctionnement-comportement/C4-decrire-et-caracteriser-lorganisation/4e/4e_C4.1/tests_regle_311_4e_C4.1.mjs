/* Banc de la règle d'or n°311 pour 4e_C4.1 — voir banc_regle_311_theme2.mjs (relais du thème 2 vers le banc commun du thème 1).
   Usage : node tests_regle_311_4e_C4.1.mjs [--captures <dossier>] */
import { lancerBanc311Theme2 } from '../../../banc_regle_311_theme2.mjs';

await lancerBanc311Theme2({
  dossier: import.meta.dirname,
  page: 'sequence_4e_C4.1-C4.9_jardin_connecte.html',
  code: '4e_C4.1',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'billetEntree',
  ancreSN: 'act5',
  panneauSN: 's4',
});
