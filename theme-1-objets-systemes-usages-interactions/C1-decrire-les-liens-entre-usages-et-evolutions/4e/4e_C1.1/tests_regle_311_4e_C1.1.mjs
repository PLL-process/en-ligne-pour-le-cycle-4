/* Banc de la règle d'or n°311 pour 4e_C1.1 — voir banc_regle_311.mjs (modèle : le pilote 5e_C3.1).
   Usage : node tests_regle_311_4e_C1.1.mjs [--captures <dossier>] */
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

await lancerBanc311({
  dossier: import.meta.dirname,
  page: 'sequence_4e_C1.1-C1.3_tsinghua_feux.html',
  code: '4e_C1.1',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'be_1__1',
  ancreSN: 'activite-5',   // la séance 5 (24/10/2026) est désormais la dernière : elle porte la clôture
  panneauSN: 's5',
});
