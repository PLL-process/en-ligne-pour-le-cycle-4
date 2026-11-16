// La fiche A4 du lampadaire (format « drawing », skill « anatomy » de Pascal) : node <kit>/scripts/print.mjs fiche.mjs --format drawing --png
// Copiée à côté de la page claire par `node build.mjs --light` ; les mots viennent de la séquence 5e_C4.1.
const piece = (id) => `[data-piece="${id}"]`;
export default {
  page: "lampadaire_en_pieces-clair.html",
  out: "lampadaire_fiche",
  layers: ".iso-stage svg",
  strip: [".num"],
  reduced: true,
  views: {
    ferme: {},
    ouvert: { actions: [["click", "[data-ouvrir]"], ["wait", 400]], reset: [["click", "[data-ouvrir]"], ["wait", 400]] },
  },
  name: "Lampadaire de la cour",
  kicker: "Dessin expliqué · 5e_C4.1",
  title: "Le lampadaire de la cour, pièce par pièce",
  number: "5e_C4.1",
  question: "Qui fait quoi dans le lampadaire ?",
  lead: "Il n'est relié à aucun câble du secteur : un panneau solaire et une batterie lui suffisent, en très basse tension.",
  spec: [
    ["Énergie", "le soleil, stockée dans la batterie"],
    ["Tension", "très basse tension"],
    ["Jour (80 lux)", "LED éteinte"],
    ["Nuit (10 lux)", "LED en veille, faible"],
    ["Passage", "pleine puissance, environ 5 s"],
  ],
  parts: [
    { id: "panneau", name: "Panneau solaire", say: "capte la lumière, la change en énergie électrique", select: piece("panneau") },
    { id: "tete", name: "Bloc de LED", say: "change l'énergie électrique en lumière", select: piece("tete") },
    { id: "luminosite", name: "Capteur de luminosité", say: "dit à la carte s'il fait nuit", select: piece("luminosite") },
    { id: "bras", name: "Bras", say: "porte la tête au-dessus de l'allée", select: piece("bras") },
    { id: "pir", name: "Détecteur de mouvement", say: "repère qu'une personne passe", select: piece("pir") },
    { id: "mat", name: "Mât", say: "porte tout en hauteur", select: piece("mat") },
    { id: "coffret", name: "Coffret", say: "abrite la batterie et la carte de la pluie", select: piece("coffret") },
    { id: "batterie", name: "Batterie", say: "stocke l'énergie pour la nuit", select: piece("batterie") },
    { id: "regulateur", name: "Régulateur de charge", say: "gère la charge de la batterie", select: piece("regulateur") },
    { id: "carte", name: "Carte programmable", say: "décide quand et comment allumer", select: piece("carte") },
    { id: "interrupteur", name: "Interrupteur commandé", say: "laisse passer l'énergie vers la LED", select: piece("interrupteur") },
    { id: "cable", name: "Câble", say: "relie le coffret à la tête", select: piece("cable") },
    { id: "socle", name: "Socle de béton", say: "tient le mât debout", select: piece("socle") },
  ],
  main: { view: "ouvert" },
  inset: { label: "Fermé", view: "ferme" },
  steps: [
    { view: "ouvert", title: "Le jour : charger", text: "Le panneau capte la lumière ; le régulateur charge la batterie.", focus: ["panneau", "regulateur", "batterie"] },
    { view: "ouvert", title: "La nuit : en veille", text: "Le capteur dit qu'il fait nuit ; la carte allume la LED, faible.", focus: ["luminosite", "carte", "interrupteur", "tete"] },
    { view: "ouvert", title: "Un passage : pleine puissance", text: "Le détecteur voit quelqu'un ; la carte pousse la LED à fond.", focus: ["pir", "carte", "interrupteur", "tete"] },
  ],
};
