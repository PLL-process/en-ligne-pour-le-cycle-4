/* Banc de la règle d'or n°311 pour 4e_C6.2 — voir banc_regle_311_theme2.mjs (relais du thème 2 vers le banc commun du thème 1).
   Pas d'hypothèse de départ : le volet s'appelle « 📖 Rappel : la situation », et le banc suit une réponse de la séance 1.
   Usage : node tests_regle_311_4e_C6.2.mjs [--captures <dossier>] */
import { lancerBanc311Theme2 } from '../../../banc_regle_311_theme2.mjs';

await lancerBanc311Theme2({
  dossier: import.meta.dirname,
  page: 'sequence-jardin-connecte-arrosage-automatique.html',
  code: '4e_C6.2',
  champ: '#a1q1',
  choix: true,
  texte: "capteur d'humidité",
  ancreS1: 'a1q1',
  ancreSN: 'a7q1',
  panneauSN: 's3',
});
