/* Banc de la règle d'or n°311 pour 4e_C1.4 — voir banc_regle_311.mjs (modèle : le pilote 5e_C3.1).
   Usage : node tests_regle_311_4e_C1.4.mjs [--captures <dossier>] */
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

await lancerBanc311({
  dossier: import.meta.dirname,
  page: 'sequence-cybersecurite-protection-donnees.html',
  code: '4e_C1.4',
  champ: '#pbm',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'bloc1-risques',
  ancreSN: 'bloc5-traces',
  panneauSN: 's3',
});
