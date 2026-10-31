/* Banc de la règle d'or n°311 pour 3e_C9.2, page tout-en-un (8 séances) — voir banc_regle_311_theme3.mjs (relais du thème 3
   vers le banc commun du thème 1). Les quatre pages découpées restent hors de la règle (pas d'onglets).
   Un outil n'est pas du décor : le lien vers les quatre pages, le sélecteur de parcours, ses deux zones role=status, la
   progression, « 🌀 Le banc d'essai de la station » (séances 3 à 8) et le bandeau des tâches de la séance restent hors du volet.
   Lien direct : #pont-en-h (séance 1), #act7 (séance 8).
   Usage : node tests_regle_311_3e_C9.2.mjs [--captures <dossier>] */
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html',
  code: '3e_C9.2',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'pont-en-h',
  ancreSN: 'act7',
  panneauSN: 's8',
  outils: ['#vers-quatre-pages', '.choix-parcours-boutons', '#parcoursNote', '#savedNote', '.progress-wrap', '#bancCard', '#tachesBandeau'],
});
