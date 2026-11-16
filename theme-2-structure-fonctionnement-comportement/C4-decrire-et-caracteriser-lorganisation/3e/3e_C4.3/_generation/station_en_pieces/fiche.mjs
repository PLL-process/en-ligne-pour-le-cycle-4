// La fiche A4 de la station (format « drawing », skill « anatomy » de Pascal) : node <kit>/scripts/print.mjs fiche_station.mjs --format drawing
// Copiée à côté de la page claire par `node build.mjs --light` ; les mots viennent des séquences de la station.
// Comme la figure, elle dit où est chaque pièce, jamais à quoi elle sert dans la chaîne d'information (3e_C4.3, activité 1).
const piece = (id) => `[data-piece="${id}"]`;
export default {
  page: "station_en_pieces-clair.html",
  out: "station_fiche",
  layers: ".iso-stage svg",
  strip: [".num"],
  reduced: true,
  views: {
    ferme: {},
    ouvert: { actions: [["click", "[data-ouvrir]"], ["wait", 400]], reset: [["click", "[data-ouvrir]"], ["wait", 400]] },
  },
  name: "Station d'alerte du collège",
  kicker: "Dessin expliqué · 3e_C4.3",
  title: "La station d'alerte, pièce par pièce",
  number: "3e_C4.3",
  question: "Où est chaque pièce de la station ?",
  lead: "Sur le toit du collège, face à la mer : ce qui doit voir le ciel est en haut du mât, le reste est rangé dans le coffret.",
  spec: [
    ["Lieu", "le toit du collège, face à la mer"],
    ["Elle mesure", "le vent, la pluie, la pression"],
    ["Tension", "12 V (batterie)"],
    ["Pièces", "18, dont 7 dans le coffret"],
  ],
  parts: [
    { id: "anemometre", name: "Anémomètre", say: "trois coupelles, tout en haut", select: piece("anemometre") },
    { id: "girouette", name: "Girouette", say: "à côté de l'anémomètre", select: piece("girouette") },
    { id: "antenne", name: "Antenne radio", say: "la tige fine, au bout du bras", select: piece("antenne") },
    { id: "gyrophare", name: "Gyrophare", say: "au pied de l'antenne", select: piece("gyrophare") },
    { id: "panneau", name: "Panneau solaire", say: "à l'autre bout du bras", select: piece("panneau") },
    { id: "pluviometre", name: "Pluviomètre", say: "un entonnoir sur son bras", select: piece("pluviometre") },
    { id: "sirene", name: "Sirène", say: "tournée vers le quartier", select: piece("sirene") },
    { id: "cable", name: "Câble de la sirène", say: "du coffret à la sirène", select: piece("cable") },
    { id: "coffret", name: "Coffret", say: "fixé au mât, à hauteur de main", select: piece("coffret") },
    { id: "led", name: "LED d'alimentation", say: "sur la porte du coffret", select: "[data-led]" },
    { id: "mat", name: "Mât", say: "vissé sur le toit par sa platine", select: piece("mat") },
    { id: "radio", name: "Module radio", say: "relié à l'antenne", select: piece("radio") },
    { id: "barometre", name: "Baromètre", say: "une petite carte du coffret", select: piece("barometre") },
    { id: "micro", name: "Microcontrôleur", say: "la carte programmable", select: piece("micro") },
    { id: "convertisseur", name: "Convertisseur 12 V → 5 V", say: "à côté du microcontrôleur", select: piece("convertisseur") },
    { id: "fusible", name: "Fusible", say: "dans son porte-fusible", select: piece("fusible") },
    { id: "regulateur", name: "Régulateur de charge", say: "à côté de la batterie", select: piece("regulateur") },
    { id: "batterie", name: "Batterie 12 V", say: "en bas du coffret", select: piece("batterie") },
  ],
  main: { view: "ouvert" },
  inset: { label: "Fermé", view: "ferme" },
  steps: [
    { view: "ouvert", title: "Tout en haut", text: "Rien ne cache le vent ni la pluie à l'anémomètre, à la girouette et au pluviomètre.", focus: ["anemometre", "girouette", "pluviometre"] },
    { view: "ouvert", title: "Sur le bras", text: "Le panneau solaire d'un côté ; le gyrophare et l'antenne de l'autre.", focus: ["panneau", "gyrophare", "antenne"] },
    { view: "ouvert", title: "Dans le coffret", text: "Sept pièces à l'abri, à hauteur de main : la batterie en bas, les cartes au-dessus.", focus: ["radio", "barometre", "micro", "convertisseur", "fusible", "regulateur", "batterie"] },
  ],
};
