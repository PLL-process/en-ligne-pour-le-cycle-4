/* Banc de la règle d'or n°311 pour 3e_C3.1 — voir banc_regle_311.mjs (modèle : le pilote 5e_C3.1).
   Usage : node tests_regle_311_3e_C3.1.mjs [--captures <dossier>] */
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

await lancerBanc311({
  dossier: import.meta.dirname,
  page: 'sequence_3e_C3.1-C3.4_shenzhen.html',
  code: '3e_C3.1',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'be_1__1',
  ancreSN: 'roles-3e_C3-1',
  panneauSN: 's4',
});
