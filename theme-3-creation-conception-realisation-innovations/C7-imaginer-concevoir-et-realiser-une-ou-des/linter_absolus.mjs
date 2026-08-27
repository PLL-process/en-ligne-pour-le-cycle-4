#!/usr/bin/env node
/* Inventaire des ABSOLUS dans les réfutations et les « à retenir ».
 *
 * POURQUOI CET OUTIL EXISTE
 * -------------------------
 * La relecture d'août 2026 a montré que les erreurs les plus tenaces d'une
 * banque de QCM ne sont pas dans les questions : elles sont dans les phrases
 * qui les entourent. Une réfutation qui, pour écarter une proposition, énonce
 * une loi générale (« l'épaisseur ne change JAMAIS rien ») enseigne une chose
 * fausse à l'élève qui a répondu juste comme à celui qui s'est trompé.
 *
 * CE QUE CET OUTIL NE FAIT PAS
 * ----------------------------
 * Il ne juge pas. Aucun programme ne peut décider si « on ne câble jamais sur
 * le secteur » est une exagération (ce n'en est pas une : c'est une règle de
 * sécurité) ou si « l'épaisseur ne change jamais rien » en est une (c'en est
 * une). Il compte, il liste, et il compare à un inventaire écrit à la main.
 *
 * C'est donc un CLIQUET, pas un correcteur : aucun absolu nouveau ne peut
 * entrer dans une banque sans qu'un humain l'ait ajouté à
 * `absolus_declares.json` avec la raison pour laquelle il y a sa place.
 *
 * Le champ `nuance` est HORS PÉRIMÈTRE, volontairement : c'est le champ dont
 * le rôle est précisément de discuter les absolus, et il en contient donc
 * beaucoup, à dessein.
 *
 * Usage : NODE_PATH=<node_modules> node linter_absolus.mjs [--ecrire]
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const ICI = path.dirname(fileURLToPath(import.meta.url));
const THEME = path.resolve(ICI, "..");
const INVENTAIRE = path.join(ICI, "absolus_declares.json");

export const QCM = [
  "C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/qcm_5e_C7_mini-projet.html",
  "C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/qcm_4e_C7_jardin-conception.html",
  "C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/qcm_4e_C8_jardin-validation.html",
  "C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/qcm_3e_C7_capteur-confort-ny.html",
];

/* Uniquement les tournures qui énoncent une LOI. « aucun » et « seul » sont
   écartés : « la couleur n'a aucune influence sur l'étanchéité » est une
   négation ordinaire, pas une généralisation. */
const MOTS = /\b(toujours|jamais|systématiquement|il suffit de|tous les|dans tous les cas)\b/gi;

export async function inventorier(nav) {
  const trouves = [];
  for (const rel of QCM) {
    const abs = path.join(THEME, rel);
    const ctx = await nav.newContext();
    const page = await ctx.newPage();
    await page.goto(pathToFileURL(abs).href);
    const banque = await page.evaluate(() =>
      QUESTIONS.map(x => ({ d: x.d || [], ret: x.ret || "" })));
    await ctx.close();
    banque.forEach((x, i) => {
      const champs = [["ret", [x.ret]], ["d", x.d]];
      for (const [nom, textes] of champs) {
        textes.forEach((t, k) => {
          for (const m of String(t).matchAll(MOTS)) {
            trouves.push({
              fichier: path.basename(rel),
              question: i + 1,
              champ: nom === "d" ? "d[" + k + "]" : nom,
              mot: m[0].toLowerCase(),
            });
          }
        });
      }
    });
  }
  return trouves;
}

export function clef(x) {
  return [x.fichier, x.question, x.champ, x.mot].join(" · ");
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const nav = await chromium.launch();
  const trouves = await inventorier(nav);
  await nav.close();

  if (process.argv.includes("--ecrire")) {
    const declare = fs.existsSync(INVENTAIRE)
      ? JSON.parse(fs.readFileSync(INVENTAIRE, "utf-8")) : { absolus: [] };
    const raisons = new Map(declare.absolus.map(a => [a.ou, a.raison]));
    const sortie = {
      commentaire: "Inventaire des absolus ASSUMÉS dans les réfutations et les « à retenir ». "
        + "Chaque ligne a été lue par un humain. Un absolu qui n'est pas ici fait échouer les tests : "
        + "c'est voulu — il oblige à décider s'il enseigne une règle, ou s'il exagère.",
      genere_par: "linter_absolus.mjs --ecrire",
      absolus: trouves.map(t => ({ ou: clef(t), raison: raisons.get(clef(t)) || "À JUSTIFIER" })),
    };
    fs.writeFileSync(INVENTAIRE, JSON.stringify(sortie, null, 2) + "\n", "utf-8");
    console.log("inventaire écrit : " + trouves.length + " absolus");
  } else {
    trouves.forEach(t => console.log(clef(t)));
    console.log("\n" + trouves.length + " absolus dans d[] et ret");
  }
}
