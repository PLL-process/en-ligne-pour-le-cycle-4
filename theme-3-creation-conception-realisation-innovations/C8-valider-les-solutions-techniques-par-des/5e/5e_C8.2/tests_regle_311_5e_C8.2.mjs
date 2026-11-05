/* Banc de la règle d'or n°311 pour 5e_C8.2 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 : la page d'un seul tenant passe à deux séances à onglets, l'ouverture
   dans le volet « 📖 Rappel » dès la séance 2. Le banc d'essai ne sert qu'à la séance 1 (activités 0 et 2) : il y reste, dans
   l'activité 0. Restent hors du volet, à chaque séance, la barre d'outils et le bandeau de navigation (accueil, lexique).
   Le lien direct #act3 (décider, et le justifier) ouvre la séance 2, ouverture repliée.
   Usage : node tests_regle_311_5e_C8.2.mjs [--captures <dossier>] */
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_5e_C8.2_patere-du-hall.html',
  code: '5e_C8.2',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'act3',
  panneauSN: 's2',
  outils: ['.toolbar', '#navharm'],
});
