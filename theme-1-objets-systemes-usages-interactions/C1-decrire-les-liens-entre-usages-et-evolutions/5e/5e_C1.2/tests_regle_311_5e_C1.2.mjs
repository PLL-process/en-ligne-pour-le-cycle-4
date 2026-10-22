/* Banc de la règle d'or n°311 pour 5e_C1.2 — voir banc_regle_311.mjs (modèle : le pilote 5e_C3.1).
   Usage : node tests_regle_311_5e_C1.2.mjs [--captures <dossier>] */
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

await lancerBanc311({
  dossier: import.meta.dirname,
  page: 'sequence_5e_C1.2_sainte_luce_freinage.html',
  code: '5e_C1.2',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'be_1__1',
  ancreSN: 'a3_1__1',
  panneauSN: 's3',
});
