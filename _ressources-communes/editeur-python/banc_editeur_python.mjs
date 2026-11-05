#!/usr/bin/env node
/* banc_editeur_python.mjs — le banc de l'éditeur Python intégré (editeur-python.js + .css + Skulpt).
 *
 * Il fabrique, dans un dossier temporaire, une page d'essai qui ressemble à une page du dépôt (thème
 * sombre, sauvegarde de tous les champs à « change », restauration par .value), y pose deux éditeurs
 * (un simple, un avec des fonctions simulées), et éprouve ce que l'éditeur promet :
 *   print(3 + 4) et print("3" + "4") ; les erreurs expliquées en français ; input() dans la console,
 *   jamais par une fenêtre ; la boucle sans fin arrêtée ; ⏹ ; la sauvegarde après rechargement ;
 *   ⬇ puis 📂 (même contenu) ; aucune requête réseau ; Skulpt chargé au premier ▶ seulement ;
 *   390 px sans défilement de côté ; cibles de 44 px ; clavier ; l'impression ; sans JavaScript.
 * Aucune page n'est écrite dans le dépôt.
 *
 * Usage : node _ressources-communes/editeur-python/banc_editeur_python.mjs [--captures <dossier>]
 * Sortie : 0 si tout passe, 1 sinon.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const ICI = path.dirname(fileURLToPath(import.meta.url));
const JS = pathToFileURL(path.join(ICI, "editeur-python.js")).href;
const CSS = pathToFileURL(path.join(ICI, "editeur-python.css")).href;
const iCap = process.argv.indexOf("--captures");
const CAP = iCap > 0 ? path.resolve(process.argv[iCap + 1]) : null;
if (CAP) fs.mkdirSync(CAP, { recursive: true });

const TMP = fs.mkdtempSync(path.join(os.tmpdir(), "banc-editeur-py-"));
const PAGE = path.join(TMP, "page_essai.html");
fs.writeFileSync(PAGE, `<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Banc de l'éditeur Python</title>
<link rel="stylesheet" href="${CSS}">
<style>
  :root{--bg:#050f24;--panel:#0d2347;--panel2:#0a1b3d;--border:#274a8a;--text:#e4eaf5;--input-bg:#173666;--input-bd:#2e5d9f;
    --btn:#1d4e89;--btn-h:#2966b1;--hl:#61dafb;--ok:#81fba1;--warn:#ffd66b;--err:#ff7b88}
  *{box-sizing:border-box} body{background:var(--bg);color:var(--text);font-family:system-ui,sans-serif;margin:0;padding:0 16px 40px;line-height:1.55}
  section.card{max-width:940px;margin:16px auto;background:var(--panel);border:1px solid var(--border);border-radius:16px;padding:18px}
  input[type=text],textarea{background:var(--input-bg);border:1px solid var(--input-bd);color:var(--text);border-radius:8px;padding:7px 10px;font-size:.92em;width:100%}
  .btn{background:var(--btn);color:#fff;border:none;border-radius:9px;padding:9px 18px;cursor:pointer;font-weight:600;font-size:.92em}
  @media print{body{background:#fff;color:#111}section.card{background:#fff;border-color:#999}button,.btn{display:none}}
</style></head><body>
<section class="card"><h2>Activité d'essai</h2>
<div class="editeur-py" id="vs1" data-fichier="3e-VARIABLES-TON NOM">
  <label for="py_essai">🐍 Ton programme</label>
  <textarea id="py_essai" class="editeur-py-code" rows="4" wrap="off" spellcheck="false">print(3 + 4)
print("3" + "4")</textarea>
  <p class="editeur-py-vitta">Avec Vittascience (facultatif, Internet) : <a class="btn vs-lien" href="https://fr.vittascience.com/python/?mode=code&amp;console=bottom" target="_blank" rel="noopener">Vittascience, si tu préfères</a></p>
  <p class="editeur-py-sansjs">Les boutons n'apparaissent pas ? Écris ton programme dans la zone ci-dessus.</p>
</div>
<div class="editeur-py" id="vs2" data-fichier="4e-ARROSAGE-TON NOM" data-simulation="carte-simulee">
  <label for="py_sim">🐍 Avec des fonctions simulées</label>
  <textarea id="py_sim" class="editeur-py-code" rows="4" wrap="off" spellcheck="false">h = lire_capteur_pourcent(0)
print("mesure", h)
print(h + "%")</textarea>
</div>
<ol class="gestes-pratique" data-editeur="py_echauf" data-bilan="bilan-echauf">
  <li data-geste="1" data-si-inchange="Change d'abord Camille."><span class="geste-coche">☐</span><span class="geste-texte">1. Écrire et exécuter</span></li>
  <li data-geste="2"><span class="geste-coche">☐</span><span class="geste-texte">2. Nommer</span></li>
  <li data-geste="3"><span class="geste-coche">☐</span><span class="geste-texte">3. Sortir</span></li>
  <li data-geste="4"><span class="geste-coche">☐</span><span class="geste-texte">4. Retrouver</span></li>
</ol>
<p class="gestes-pratique-bilan" id="bilan-echauf" role="status"></p>
<div class="editeur-py editeur-py-essai" id="vsE" data-fichier="5e-HALL-essai-TON NOM">
  <label for="py_echauf">🐍 L'éditeur d'essai</label>
  <textarea id="py_echauf" class="editeur-py-code" rows="3" wrap="off" spellcheck="false">nom = "Camille"
print("Bonjour", nom, "!")</textarea>
</div>
<script type="text/x-python" id="carte-simulee">
mesures = [55, 40, 25]
rang = [0]
def lire_capteur_pourcent(broche):
    rang[0] = rang[0] + 1
    return mesures[(rang[0] - 1) % len(mesures)]
</script>
</section>
<script>
const KEY = "banc_editeur_python";
function save(){ const o = {}; document.querySelectorAll("input, select, textarea").forEach(e => { if(e.id) o[e.id] = e.value; });
  try{ localStorage.setItem(KEY, JSON.stringify(o)); }catch(e){} window.__sauvegardes = (window.__sauvegardes||0) + 1; }
function restore(){ let o; try{ o = JSON.parse(localStorage.getItem(KEY) || "null"); }catch(e){} if(!o) return;
  Object.entries(o).forEach(([id, v]) => { const e = document.getElementById(id); if(e) e.value = v; }); }
document.addEventListener("change", e => { if(e.target.matches("input, select, textarea")) save(); });
restore();
window.__fins = []; document.addEventListener("editeur-py:fin", e => window.__fins.push(e.detail));
</script>
<script src="${JS}" defer></script>
</body></html>
`);
const URL_PAGE = pathToFileURL(PAGE).href;

let nOk = 0, nKo = 0;
function ok(nom, cond, detail = "") {
  if (cond) nOk++; else { nKo++; process.exitCode = 1; }
  console.log((cond ? "✅ " : "❌ ") + nom + (detail ? " — " + detail : ""));
}
const nav = await chromium.launch();
const reseau = [];
const dialogues = [];
async function contexte(opts = {}) {
  const ctx = await nav.newContext({ acceptDownloads: true, viewport: { width: 1280, height: 900 }, ...opts });
  await ctx.route("**/*", (r) => {
    const u = r.request().url();
    if (/^(file|data|blob):/.test(u)) return r.continue();
    reseau.push(u); return r.abort();
  });
  return ctx;
}
async function ouvrir(ctx) {
  const p = await ctx.newPage();
  p.on("dialog", (d) => { dialogues.push(d.type() + " : " + d.message()); d.dismiss().catch(() => {}); });
  p.erreurs = []; p.on("pageerror", (e) => p.erreurs.push(e.message));
  await p.goto(URL_PAGE);
  await p.waitForSelector("#vs1.editeur-py--actif");
  return p;
}
const consoleDe = (p, id) => p.locator(`#${id} .editeur-py-console`).innerText();
async function executer(p, id, attendre = 15000) {
  const n = await p.evaluate(() => window.__fins.length);
  await p.click(`#${id} .editeur-py-executer`);
  await p.waitForFunction((k) => window.__fins.length > k, n, { timeout: attendre });
  return p.evaluate(() => window.__fins[window.__fins.length - 1]);
}
async function ecrireCode(p, id, code) {
  await p.evaluate(([id, c]) => { const t = document.querySelector(`#${id} textarea`); t.value = c; t.dispatchEvent(new Event("input", { bubbles: true })); }, [id, code]);
}
async function capture(p, nom, sel) {
  if (!CAP) return;
  const f = path.join(CAP, nom + ".png");
  if (sel) await p.locator(sel).screenshot({ path: f }); else await p.screenshot({ path: f });
}

const ctx = await contexte();
let p = await ouvrir(ctx);

/* 1. Skulpt n'est pas chargé à l'ouverture */
ok("Skulpt n'est pas chargé à l'ouverture de la page",
   await p.evaluate(() => !window.Sk && !document.querySelector('script[src*="skulpt"]')));
ok("le code de départ est dans la zone, numérotée 1-2",
   (await p.inputValue("#py_essai")) === 'print(3 + 4)\nprint("3" + "4")' &&
   (await p.locator("#vs1 .editeur-py-marge").innerText()).trim() === "1\n2");
await capture(p, "01_vide_1280", "#vs1");

/* 2. print(3 + 4) et print("3" + "4") */
let r = await executer(p, "vs1");
ok('print(3 + 4) → 7 et print("3" + "4") → 34', r.sortie === "7\n34\n" && !r.erreur, JSON.stringify(r.sortie));
ok("la console l'affiche, puis « ✔ Terminé »", /^7\n34\n[\s\S]*✔ Terminé/.test(await consoleDe(p, "vs1")));
ok("Skulpt est chargé au premier ▶ (deux fichiers locaux)",
   await p.evaluate(() => [...document.querySelectorAll('script[src*="skulpt"]')].length === 2 && !!window.Sk));
ok("l'événement editeur-py:fin porte le bloc, le champ et le code",
   r.bloc === "vs1" && r.champ === "py_essai" && /print\(3 \+ 4\)/.test(r.code));
await capture(p, "02_execute_1280", "#vs1");

/* 3. les erreurs, expliquées en français */
const ERREURS = [
  ['print("3" + 4)', 1, /Erreur de type/, /texte \(str\) et un nombre[\s\S]*int\(/, /can only concatenate str \(not "int"\) to str/],
  ['minutes = "21"\nminutes = minutes - 1', 2, /Erreur de type/, /on ne soustrait pas/, /unsupported operand/],
  ['Print("bonjour")', 1, /Nom inconnu/, /« print »/, /NameError/],
  ['print(prix)', 1, /Nom inconnu/, /prix = …\) AVANT/, /NameError/],
  ['x = 5\nif x > 3\n    print(x)', 2, /syntaxe/, /deux-points/, /SyntaxError/],
  ['x = 5\nif x > 3:\nprint(x)', 3, /décalage/, /décalent de 4 espaces/, /SyntaxError/],
  ['x = 5\n    y = 2', 2, /décalage/, /rien ne l'exige/, /SyntaxError/],
  ['x = 3\nif x = 3:\n    print(x)', 2, /syntaxe/, /« == »/, /SyntaxError/],
  ['h = 1\nif h ___ 3:\n    print(h)', 2, /syntaxe/, /trou/, /SyntaxError/],
  ['print("bonjour)', 1, /syntaxe/, /guillemet/, /SyntaxError/],
  ['print((2 + 3)\nprint(1)', 1, /syntaxe/, /parenthèse/, /SyntaxError/],
  ['n = int("douze")', 1, /Valeur impossible/, /« douze »/, /ValueError/],
  ['print(10 / 0)', 1, /Division par zéro/, /divises par zéro/, /ZeroDivisionError: division by zero/],
  ['humidité = 3', 1, /syntaxe/, /accentuée/, /SyntaxError/],
];
for (const [code, ligne, titre, expl, brut] of ERREURS) {
  await ecrireCode(p, "vs1", code);
  r = await executer(p, "vs1");
  const c = await consoleDe(p, "vs1");
  const marque = await p.locator("#vs1 .editeur-py-marge .editeur-py-ko").innerText().catch(() => "");
  ok("erreur expliquée : " + JSON.stringify(code).slice(0, 34),
     r.erreur && r.erreur.ligne === ligne && titre.test(c) && expl.test(c) && brut.test(c) && marque.trim() === String(ligne),
     r.erreur ? "ligne " + r.erreur.ligne + " · " + r.erreur.explication.slice(0, 90) : "pas d'erreur");
  if (code.startsWith('print("3" + 4)')) await capture(p, "03_erreur_1280", "#vs1");
}

/* 4. input() dans la console, jamais par une fenêtre */
await ecrireCode(p, "vs1", 'n = int(input("Combien de minutes ? "))\nprint("Attente :", n * 2, "min")');
const n0 = await p.evaluate(() => window.__fins.length);
await p.click("#vs1 .editeur-py-executer");
await p.waitForSelector("#vs1 .editeur-py-entree-champ", { timeout: 10000 });
ok("input() : l'invite s'écrit dans la console, le champ y apparaît et prend le focus",
   /Combien de minutes \?/.test(await consoleDe(p, "vs1")) &&
   await p.evaluate(() => document.activeElement && document.activeElement.classList.contains("editeur-py-entree-champ")));
await p.waitForTimeout(1200);   // l'attente de l'élève ne compte pas dans la limite de calcul
await p.keyboard.type("21");
await p.keyboard.press("Enter");
await p.waitForFunction((k) => window.__fins.length > k, n0, { timeout: 10000 });
r = await p.evaluate(() => window.__fins[window.__fins.length - 1]);
ok("input() : la réponse 21 donne « Attente : 42 min » ; la console garde l'invite et la réponse",
   r.sortie === "Attente : 42 min\n" && !r.erreur && /Combien de minutes \? 21\nAttente : 42 min/.test(await consoleDe(p, "vs1")), JSON.stringify(r.sortie));
ok("aucune fenêtre (alert, prompt, confirm) n'a été ouverte", dialogues.length === 0, dialogues.join(" | "));

/* 5. la boucle sans fin, arrêtée avec un message clair */
await ecrireCode(p, "vs1", "i = 0\nwhile i < 10:\n    print(\"tour\")\n");
let t0 = Date.now();
r = await executer(p, "vs1", 20000);
ok("une boucle qui affiche sans fin s'arrête (console pleine) avec un message", r.arret === "lignes" && /débordait/.test(await consoleDe(p, "vs1")), (Date.now() - t0) + " ms");
await ecrireCode(p, "vs1", "i = 0\nwhile i < 10:\n    i = i * 1\n");
t0 = Date.now();
r = await executer(p, "vs1", 20000);
const duree = Date.now() - t0;
ok("une boucle sans fin silencieuse est arrêtée au bout de quelques secondes, ligne et explication",
   r.erreur && r.erreur.type === "TimeLimitError" && /Boucle sans fin/.test(await consoleDe(p, "vs1")) && duree < 9000, duree + " ms, " + (r.erreur && r.erreur.explication.slice(0, 60)));

/* 6. ⏹ Arrêter, pendant une attente */
await ecrireCode(p, "vs1", "import time\nwhile True:\n    print(\"mesure\")\n    time.sleep(0.5)\n");
const n1 = await p.evaluate(() => window.__fins.length);
await p.click("#vs1 .editeur-py-executer");
await p.waitForTimeout(1300);
ok("pendant l'exécution, ▶ est grisé et ⏹ disponible",
   await p.evaluate(() => document.querySelector("#vs1 .editeur-py-executer").disabled && !document.querySelector("#vs1 .editeur-py-arreter").disabled));
await p.click("#vs1 .editeur-py-arreter");
await p.waitForFunction((k) => window.__fins.length > k, n1, { timeout: 5000 });
r = await p.evaluate(() => window.__fins[window.__fins.length - 1]);
const lignesAvant = (r.sortie.match(/mesure/g) || []).length;
await p.waitForTimeout(900);
ok("⏹ Arrêter interrompt le programme, même pendant time.sleep, et rien ne s'écrit ensuite",
   r.arret === "bouton" && lignesAvant >= 2 && ((await consoleDe(p, "vs1")).match(/mesure/g) || []).length === lignesAvant, lignesAvant + " mesures");

/* 7. les fonctions simulées : leurs lignes ne décalent pas celles de l'élève */
r = await executer(p, "vs2");
ok("fonctions simulées : la mesure 55 s'affiche, et l'erreur est bien à la ligne 3 de l'élève",
   /^mesure 55\n/.test(r.sortie) && r.erreur && r.erreur.ligne === 3 && r.erreur.type === "TypeError", r.erreur && r.erreur.ligne);

/* 8. l'API sans écran : une vérification qui juge en exécutant */
r = await p.evaluate(() => window.EditeurPython.executer('places = 0\nif places > 0:\n    print("OUVERTE")\nelse:\n    print("FERMÉE")'));
ok("EditeurPython.executer(code) rend la sortie sans toucher à l'écran", r.sortie === "FERMÉE\n" && !r.erreur);
r = await p.evaluate(() => window.EditeurPython.executer('a = input()\nprint(a * 2)', { entrees: ["ab"] }));
ok("EditeurPython.executer(code, {entrees}) répond aux input()", r.sortie === "abab\n", JSON.stringify(r.sortie));

/* 9. le clavier : Tab = 4 espaces, Entrée après « : » décale, Échap libère Tab */
await ecrireCode(p, "vs1", "");
await p.focus("#py_essai");
await p.keyboard.type("if True:");
await p.keyboard.press("Enter");
await p.keyboard.type("print(1)");
await p.keyboard.press("Enter");
await p.keyboard.press("Shift+Tab");
await p.keyboard.type("x = 2");
await p.keyboard.press("Enter");
await p.keyboard.press("Tab");
await p.keyboard.type("y");
ok("clavier : Entrée après « : » décale de 4, Maj+Tab retire, Tab insère 4 espaces",
   (await p.inputValue("#py_essai")) === "if True:\n    print(1)\nx = 2\n    y", JSON.stringify(await p.inputValue("#py_essai")));
await p.keyboard.press("Escape");
await p.keyboard.press("Tab");
ok("clavier : Échap puis Tab fait sortir de la zone", await p.evaluate(() => document.activeElement.id !== "py_essai"));

/* 10. ↺ en deux clics, puis ↶ */
await p.click("#vs1 .editeur-py-depart");
ok("↺ : un premier clic demande confirmation, sans rien effacer", (await p.inputValue("#py_essai")) === "if True:\n    print(1)\nx = 2\n    y");
await p.click("#vs1 .editeur-py-depart");
ok("↺ : le second clic remet le code de départ", (await p.inputValue("#py_essai")) === 'print(3 + 4)\nprint("3" + "4")');
await p.click("#vs1 .editeur-py-annuler");
ok("↶ : le programme d'avant revient", (await p.inputValue("#py_essai")) === "if True:\n    print(1)\nx = 2\n    y");

/* 11. la sauvegarde automatique, après rechargement */
await p.click("#py_essai");
await p.keyboard.press("Control+End");
await p.keyboard.type("\nprint(\"sauvé\")");
await p.waitForTimeout(800);
await p.reload();
await p.waitForSelector("#vs1.editeur-py--actif");
const apres = await p.inputValue("#py_essai");
ok("sauvegarde : le programme tapé revient après rechargement, marge comprise",
   /print\("sauvé"\)$/.test(apres) && (await p.locator("#vs1 .editeur-py-marge").innerText()).trim().split("\n").length === apres.split("\n").length,
   JSON.stringify(apres.slice(-30)));

/* 12. ⬇ puis 📂 : le même contenu */
const CODE = 'nom = "Q"\nprint("Train", nom)  # été, °C\nfor i in range(2):\n    print(i)\n';
await ecrireCode(p, "vs1", CODE);
let rappel = false;
p.once("download", () => { rappel = true; });
await p.click("#vs1 .editeur-py-telecharger");
await p.waitForTimeout(300);
ok("⬇ : tant que « TON NOM » est dans le nom, le premier clic le rappelle (geste 2) sans télécharger",
   !rappel && /TON NOM/.test(await p.locator("#vs1 .editeur-py-etat").innerText()));
await p.fill("#py_essai_nom", "3e-VARIABLES-DUPONT");
const [dl] = await Promise.all([p.waitForEvent("download"), p.click("#vs1 .editeur-py-telecharger")]);
const fichier = path.join(TMP, dl.suggestedFilename());
await dl.saveAs(fichier);
const contenu = fs.readFileSync(fichier, "utf8");
ok("⬇ : le fichier s'appelle 3e-VARIABLES-DUPONT.py et contient le programme (fins de ligne Windows)",
   dl.suggestedFilename() === "3e-VARIABLES-DUPONT.py" && contenu.replace(/\r\n/g, "\n") === CODE, dl.suggestedFilename());
await ecrireCode(p, "vs1", "print('autre chose')");
await p.setInputFiles("#vs1 .editeur-py-choix", fichier);
await p.waitForFunction((c) => document.getElementById("py_essai").value === c, CODE, { timeout: 3000 }).catch(() => {});
ok("📂 : le fichier rouvert redonne exactement le même programme", (await p.inputValue("#py_essai")) === CODE);
ok("📂 : le nom du fichier revient aussi", (await p.inputValue("#py_essai_nom")) === "3e-VARIABLES-DUPONT");
const VITTA = path.join(TMP, "3e-VARIABLES-DUPONT_202694_171953.py");
fs.writeFileSync(VITTA, '"""\nInterface : Python\nNom du projet : 3e-VARIABLES-DUPONT\nMode : code\nProjet généré par Vittascience\n"""\n\nprint(3 + 4)\n');
await p.setInputFiles("#vs1 .editeur-py-choix", VITTA);
await p.waitForTimeout(400);
ok("📂 : un fichier téléchargé de Vittascience s'ouvre, son en-tête retiré", (await p.inputValue("#py_essai")) === "print(3 + 4)\n");
await p.waitForTimeout(700);
await p.reload(); await p.waitForSelector("#vs1.editeur-py--actif");
ok("📂 : le programme ouvert est sauvegardé dans la page", (await p.inputValue("#py_essai")) === "print(3 + 4)\n");

/* 12 bis. l'échauffement : ⬇ et 📂 se signalent, et les quatre gestes se cochent quand ils sont réussis */
const coches = () => p.$$eval("ol.gestes-pratique li", (ls) => ls.map((l) => (l.classList.contains("geste-fait") ? "1" : "0")).join(""));
const bilanE = () => p.locator("#bilan-echauf").innerText();
ok("échauffement : au départ, aucun geste coché, les cases sont ☐", (await coches()) === "0000" &&
   (await p.$$eval("ol.gestes-pratique .geste-coche", (cs) => cs.every((c) => c.textContent === "☐"))));
await executer(p, "vsE");
ok("échauffement : ▶ sur le programme de départ ne coche pas le geste 1, et le dit", (await coches()) === "0000" && /Change d'abord Camille/.test(await bilanE()));
await ecrireCode(p, "vsE", 'nom = "Léa"\nprint("Bonjour", nom, "!")');
await executer(p, "vsE");
ok("échauffement : ▶ sur le programme changé, mené au bout, coche le geste 1", (await coches()) === "1000" && /Geste 1 réussi/.test(await bilanE()));
await ecrireCode(p, "vsE", 'print("Bonjour"');
await executer(p, "vsE");
ok("échauffement : une erreur ne décoche rien et ne coche rien", (await coches()) === "1000");
await ecrireCode(p, "vsE", 'nom = "Léa"\nprint("Bonjour", nom, "!")');
await p.fill("#py_echauf_nom", "5e-HALL-essai-DUPONT");
ok("échauffement : un nom sans « TON NOM » coche le geste 2", (await coches()) === "1100");
const signaux = await p.evaluate(() => { window.__sig = []; ["editeur-py:telecharge", "editeur-py:ouvert"].forEach((t) => document.addEventListener(t, (e) => window.__sig.push(t + " " + e.detail.champ + " " + e.detail.fichier))); return true; });
const [dlE] = await Promise.all([p.waitForEvent("download"), p.click("#vsE .editeur-py-telecharger")]);
const fichierE = path.join(TMP, dlE.suggestedFilename());
await dlE.saveAs(fichierE);
ok("échauffement : ⬇ envoie editeur-py:telecharge (champ, fichier) et coche le geste 3",
   signaux && (await coches()) === "1110" && (await p.evaluate(() => window.__sig.join("|"))) === "editeur-py:telecharge py_echauf 5e-HALL-essai-DUPONT.py");
await p.click("#vsE .editeur-py-depart"); await p.click("#vsE .editeur-py-depart");
ok("échauffement : ↺ (deux clics) remet Camille", /Camille/.test(await p.inputValue("#py_echauf")));
await p.setInputFiles("#vsE .editeur-py-choix", fichierE);
await p.waitForFunction(() => /Léa/.test(document.getElementById("py_echauf").value), null, { timeout: 3000 }).catch(() => {});
ok("échauffement : 📂 envoie editeur-py:ouvert, Léa revient, le geste 4 est coché, et le bilan dit les quatre",
   (await coches()) === "1111" && /Léa/.test(await p.inputValue("#py_echauf")) && /quatre gestes sont faits/.test(await bilanE()) &&
   /editeur-py:ouvert py_echauf 5e-HALL-essai-DUPONT\.py/.test(await p.evaluate(() => window.__sig.join("|"))));
ok("échauffement : les cases cochées passent à ✅", await p.$$eval("ol.gestes-pratique .geste-coche", (cs) => cs.every((c) => c.textContent === "✅")));
await p.waitForTimeout(700);
await p.reload(); await p.waitForSelector("#vs1.editeur-py--actif");
ok("échauffement : après rechargement, les coches restent, et le bilan le dit", (await coches()) === "1111" && /déjà faits/.test(await bilanE()));
ok("les autres éditeurs ne cochent rien : la liste ne suit que son éditeur (data-editeur)",
   await p.evaluate(() => document.querySelectorAll("ol.gestes-pratique--actif").length === 1));

/* 13. accessibilité : console aria-live, cibles de 44 px, champs étiquetés */
const a11y = await p.evaluate(() => {
  const c = document.querySelector("#vs1 .editeur-py-console");
  const petits = [...document.querySelectorAll(".editeur-py .editeur-py-btn, .editeur-py input.editeur-py-nom, .editeur-py a.vs-lien")]
    .filter((b) => b.offsetParent && b.getBoundingClientRect().height < 44).map((b) => b.textContent.trim().slice(0, 20));
  const orphelins = [...document.querySelectorAll(".editeur-py input, .editeur-py textarea")].filter((e) =>
    !(e.id && document.querySelector('label[for="' + e.id + '"]')) && !e.closest("label") && !e.getAttribute("aria-label")).map((e) => e.className);
  return { live: c.getAttribute("aria-live"), role: c.getAttribute("role"), petits, orphelins };
});
ok("la console est une zone aria-live (role=log)", a11y.live === "polite" && a11y.role === "log");
ok("toutes les cibles font au moins 44 px de haut", a11y.petits.length === 0, a11y.petits.join(", "));
ok("tous les champs de l'éditeur ont une étiquette", a11y.orphelins.length === 0, a11y.orphelins.join(", "));

/* 14. 390 px : pas de défilement de côté, même avec une très longue ligne de code */
const ctxm = await contexte({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
const pm = await ouvrir(ctxm);
await ecrireCode(pm, "vs1", 'print("' + "une très longue ligne de texte ".repeat(8) + '")\nprint(3 + 4)');
r = await executer(pm, "vs1");
const debord = await pm.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
const zoneDefile = await pm.evaluate(() => { const t = document.getElementById("py_essai"); return t.scrollWidth > t.clientWidth; });
ok("390 px : la page ne défile pas de côté ; la longue ligne défile dans sa zone", debord <= 0 && zoneDefile, "débord " + debord + " px");
ok("390 px : la console replie la longue sortie", await pm.evaluate(() => { const c = document.querySelector("#vs1 .editeur-py-console"); return c.scrollWidth <= c.clientWidth + 1; }));
ok("390 px : zéro erreur JavaScript", pm.erreurs.length === 0, pm.erreurs.join(" | "));
if (CAP) {
  await ecrireCode(pm, "vs1", 'print(3 + 4)\nprint("3" + "4")\nprint("3" + 4)');
  await executer(pm, "vs1");
  await capture(pm, "04_erreur_390", "#vs1");
}
await ctxm.close();

/* 15. l'impression : le programme écrit et la dernière sortie, ou des lignes vides */
await ecrireCode(p, "vs1", 'print("Train Q", 3, "min")');
await executer(p, "vs1");
await p.emulateMedia({ media: "print" });
const imp = await p.evaluate(() => {
  const vis = (s) => { const e = document.querySelector(s); return !!e && getComputedStyle(e).display !== "none" && e.offsetParent !== null; };
  return { code: document.querySelector("#vs1 .editeur-py-imp-code").innerText, sortie: document.querySelector("#vs1 .editeur-py-imp-sortie").innerText,
    zone: vis("#vs1 .editeur-py-zone"), imp: vis("#vs1 .editeur-py-imp"), boutons: vis("#vs1 .editeur-py-executer"),
    fond: getComputedStyle(document.querySelector("#vs1")).backgroundColor, encre: getComputedStyle(document.querySelector("#vs1 .editeur-py-imp-code")).color };
});
ok("impression : le programme écrit et la dernière sortie, sans boutons ni zone d'écran",
   imp.imp && !imp.zone && !imp.boutons && /print\("Train Q", 3, "min"\)/.test(imp.code) && /Train Q 3 min/.test(imp.sortie), JSON.stringify(imp).slice(0, 160));
ok("impression : encre sombre sur fond blanc", imp.fond === "rgb(255, 255, 255)" && imp.encre === "rgb(17, 17, 17)", imp.fond + " / " + imp.encre);
await p.emulateMedia({ media: "screen" });
await ecrireCode(p, "vs1", "");
await p.emulateMedia({ media: "print" });
ok("impression : sans programme, des lignes vides à remplir",
   await p.evaluate(() => document.querySelector("#vs1 .editeur-py-imp-code").classList.contains("editeur-py-imp-vide")));
await p.emulateMedia({ media: "screen" });
ok("page d'essai : zéro erreur JavaScript", p.erreurs.length === 0, p.erreurs.join(" | "));
await ctx.close();

/* 16. sans JavaScript : la zone (avec le code de départ) et le lien Vittascience restent */
const ctxs = await contexte({ javaScriptEnabled: false });
const ps = await ctxs.newPage();
await ps.goto(URL_PAGE);
ok("sans JavaScript : la zone de code (code de départ) et le lien Vittascience restent utilisables",
   (await ps.inputValue("#py_essai")) === 'print(3 + 4)\nprint("3" + "4")' && (await ps.locator("#vs1 a.vs-lien").isVisible()) &&
   (await ps.locator("#vs1 .editeur-py-sansjs").isVisible()));
await ctxs.close();

/* 17. hors ligne : aucune requête distante pendant tout le banc */
ok("hors ligne : aucune requête vers le réseau pendant tout le banc", reseau.length === 0, reseau.slice(0, 3).join(" | "));

await nav.close();
fs.rmSync(TMP, { recursive: true, force: true });
console.log(`\n${nOk} / ${nOk + nKo} vérifications passées`);
