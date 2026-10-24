/* Banc de la règle d'or n°311 pour 4e_C4.7 — voir banc_regle_311_theme2.mjs (relais du thème 2 vers le banc commun du thème 1).
   Usage : node tests_regle_311_4e_C4.7.mjs [--captures <dossier>] */
import { lancerBanc311Theme2 } from '../../../banc_regle_311_theme2.mjs';

await lancerBanc311Theme2({
  dossier: import.meta.dirname,
  page: 'sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html',
  code: '4e_C4.7',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'fb0',
  ancreSN: 'fb5',
  panneauSN: 'seance4',
});
