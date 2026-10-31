/* Banc de la règle d'or n°311 pour 4e_C9.1 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Un outil n'est pas du décor : le sélecteur de parcours, ses deux zones role=status, la progression, « 🗺 Où en suis-je ? »
   et « 🧪 Le banc d'essai du jardin » servent aux séances 2 et 3 ; ils restent hors du volet.
   Le lien direct #pompe-pas-a-pas (l'animation pas à pas de la pompe) ouvre la séance 3, ouverture repliée.
   Usage : node tests_regle_311_4e_C9.1.mjs [--captures <dossier>] */
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_4e_C9_jardin-programme.html',
  code: '4e_C9.1',
  champ: '#hyp1',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act1',
  ancreSN: 'pompe-pas-a-pas',
  panneauSN: 's3',
  outils: ['.choix-parcours-boutons', '#parcoursNote', '#savedNote', '.progress-wrap', '#taches', '#bancCard'],
});
