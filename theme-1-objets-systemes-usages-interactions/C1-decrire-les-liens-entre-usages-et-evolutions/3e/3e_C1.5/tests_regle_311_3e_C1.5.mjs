/* Banc de la règle d'or n°311 pour 3e_C1.5 — voir banc_regle_311.mjs (modèle : le pilote 5e_C3.1).
   Usage : node tests_regle_311_3e_C1.5.mjs [--captures <dossier>] */
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

await lancerBanc311({
  dossier: import.meta.dirname,
  page: 'sequence-numerique-societe-economie-environnement-sante.html',
  code: '3e_C1.5',
  champ: '#auto_15',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'goodrep',
  ancreSN: 'impact-env',
  panneauSN: 's3',
  boutonSauvegarde: 'button[onclick="saveProgress4()"]',
});
