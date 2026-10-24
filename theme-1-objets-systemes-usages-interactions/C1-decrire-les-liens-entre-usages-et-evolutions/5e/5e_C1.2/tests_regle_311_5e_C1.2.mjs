/* Banc de la règle d'or n°311 pour 5e_C1.2 — voir banc_regle_311.mjs (modèle : le pilote 5e_C3.1).
   Quatre séances depuis le 24/10/2026 : la dernière (s4) porte les activités 4 et 5 et la clôture.
   Usage : node tests_regle_311_5e_C1.2.mjs [--captures <dossier>] */
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

await lancerBanc311({
  dossier: import.meta.dirname,
  page: 'sequence_5e_C1.2_sainte_luce_freinage.html',
  code: '5e_C1.2',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'be_1__1',
  ancreSN: 'a5_1__1',
  panneauSN: 's4',
});
