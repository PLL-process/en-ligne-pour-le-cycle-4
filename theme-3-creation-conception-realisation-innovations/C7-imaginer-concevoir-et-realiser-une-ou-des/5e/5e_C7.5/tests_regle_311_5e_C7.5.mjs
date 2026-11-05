/* Banc de la règle d'or n°311 pour 5e_C7.5 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 : la page d'un seul tenant passe à deux séances à onglets, l'ouverture
   dans le volet « 📖 Rappel » dès la séance 2. Un outil n'est pas du décor : l'établi Grove sert aux deux séances (activités 1
   et 2, le Bonus) ; un seul nœud, que le script range dans la séance ouverte, sous son en-tête, hors du volet.
   La barre d'outils (« 🖨 Imprimer / PDF ») est posée par la vague : le banc commun l'exige.
   Le lien direct #act2 (retirer, pour voir) ouvre la séance 2, ouverture repliée.
   Usage : node tests_regle_311_5e_C7.5.mjs [--captures <dossier>] */
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_5e_C7.5_eclairage-du-preau.html',
  code: '5e_C7.5',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'act2',
  panneauSN: 's2',
  outils: ['.toolbar', '#outilEtabli'],
});
