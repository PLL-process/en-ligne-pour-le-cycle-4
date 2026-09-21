/* audit_cloture_sequence.mjs — par quoi une séquence se termine-t-elle ?
 *
 * LE CONSTAT QUI A DONNÉ CET AUDIT
 * --------------------------------
 * Deux constats de classe, tenus par Pascal et mesurés ici :
 *
 *   1. Un « 🎁 Bonus » se place APRÈS le bilan « 📍 Je me positionne ». L'élève
 *      a donc fait son auto-positionnement — le geste qui clôt une séquence —
 *      et on lui redemande du travail ensuite.
 *   2. Ce Bonus ne porte AUCUN champ de réponse. On ne peut que le lire. Un
 *      bonus qu'on ne peut que lire n'est pas un bonus, c'est un paragraphe.
 *
 * Et l'autre moitié du problème, qui ne se voit pas en regardant les séquences
 * fautives : les séquences qui n'ont AUCUN bilan. Elles ne se terminent alors
 * par rien du tout.
 *
 * CE QUE CET OUTIL MESURE, ET CE QU'IL NE MESURE PAS
 * --------------------------------------------------
 * Il MESURE ce qui se compte : la présence du bilan, la présence du Bonus, leur
 * ORDRE dans le document, le nombre de champs de réponse du Bonus, la présence
 * d'un bloc de corrigé à l'intérieur, et la position du renvoi vers le QCM.
 *
 * Il ne mesure PAS, et ne le prétend pas : la QUALITÉ d'un corrigé — qu'il
 * traite vraiment la question posée, qu'il soit juste, qu'il soit utile. Cela se
 * lit, et un contrôle qui prétendrait l'établir mentirait. De même, il ne juge
 * pas si le contenu d'un bilan est un vrai bilan.
 *
 * COMMENT LE BILAN EST RECONNU
 * ----------------------------
 * À son LIBELLÉ (trois marques : un titre, un conteneur `autopos`, la phrase
 * portée par un champ) OU à sa FONCTION (un groupe de choix dont le sujet est un
 * code du référentiel). Le libellé seul en manquait une sur soixante — une
 * séquence qui titre « Bilan » et fait faire un vrai auto-positionnement.
 *
 * Usage :
 *   node _outils/audit_cloture_sequence.mjs            # rapport complet
 *   node _outils/audit_cloture_sequence.mjs --muet     # synthèse seule
 *   node _outils/audit_cloture_sequence.mjs --csv      # + audit_cloture_sequence.csv
 *   node _outils/audit_cloture_sequence.mjs <racine>   # restreindre le balayage
 *
 * Sortie : 0 la mesure a eu lieu · 2 elle n'a RIEN pu analyser (règle d'or n°299).
 * Cet audit ne REFUSE rien : il mesure. Il n'a donc pas de code 1.
 */
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const DEPOT = path.dirname(ICI);
const ECARTES = /_archive-anciennes-versions|[/\\]\.git|[/\\]node_modules/;
const SEQUENCE = /^sequence[_-].*\.html$|^sequence\.html$/i;

const muet = process.argv.includes('--muet');
const veutCsv = process.argv.includes('--csv');
const cible = process.argv.slice(2).find((a) => !a.startsWith('--'));
const RACINE = cible ? path.resolve(DEPOT, cible) : DEPOT;

const premiereLigne = (e) => String(e && e.message).split(/\r?\n/)[0].slice(0, 120);

/** Règle d'or n°299 : un contrôle qui n'a rien analysé est en panne. */
function enPanne(motif) {
  console.error(`⛔ EN PANNE — ${motif}`);
  console.error("     Cet audit n'a RIEN mesuré ; ne le lisez pas comme un résultat (règle d'or n°299).");
  process.exit(2);
}

function fichiers(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (ECARTES.test(p)) continue;
    if (e.isDirectory()) fichiers(p, a);
    else if (SEQUENCE.test(e.name)) a.push(p);
  }
  return a;
}

function situer(rel) {
  return {
    theme: (rel.match(/theme-(\d)/) || [, '?'])[1],
    niveau: (rel.match(/[/\\]([345]e)[/\\]/) || [, '?'])[1],
    lot: (rel.match(/[/\\]([345]e_C[\d.]+)[/\\]/) || [, '?'])[1],
  };
}

const MESURER = () => {
  /* Tous les panneaux ouverts : un bloc dans un onglet fermé existe autant que
     les autres, et le compter absent donnerait un chiffre faux. */
  for (const p of document.querySelectorAll('.seance-panel')) p.classList.add('active');
  for (const d of document.querySelectorAll('details')) d.open = true;

  const tous = [...document.querySelectorAll('body *')];
  const rang = (el) => tous.indexOf(el);

  /* ── le bilan : le bloc « Je me positionne » ─────────────────────────────
     La phrase ne vit pas toujours dans un titre : selon les lots elle est portée
     par un <h3>, par le <legend> d'un groupe de positionnement, ou par le
     <label> d'un champ. On cherche donc l'élément le PLUS INTÉRIEUR qui la
     porte — chercher un titre seul en manquait dix-neuf sur trente et un. */
  const PHRASE = /je me positionne|auto[- ]?positionnement|je me situe|bilan personnel/i;
  /* La phrase peut vivre dans un attribut, pas seulement dans le texte : un lot
     titre « 🙋 Bilan personnel » et ne dit « auto-positionnement » que dans les
     `aria-label` de ses champs. Le texte seul le manquait. */
  const texteEtAttributs = (e) => (e.textContent || '') + ' '
    + [...e.querySelectorAll('[aria-label]')].map((x) => x.getAttribute('aria-label')).join(' ');
  /* Trois marques possibles, cherchées dans cet ordre : un TITRE qui annonce le
     positionnement, un conteneur de classe `autopos`, ou la phrase portée par un
     <legend>/<label> de champ. La première seule en manquait vingt : plusieurs
     lots titrent « Mon auto-positionnement », et l'un d'eux ne porte la phrase
     que dans l'invite de ses listes. */
  let titreBilan = tous.find((e) => /^H[1-4]$/.test(e.tagName) && PHRASE.test(e.textContent || ''));
  let marqueBilan = titreBilan ? 'titre' : '';
  if (!titreBilan) {
    titreBilan = document.querySelector('.autopos, #autopos, [class*="auto-position"]');
    if (titreBilan) marqueBilan = 'conteneur autopos';
  }
  if (!titreBilan) {
    const porteurs = tous.filter((e) => PHRASE.test(texteEtAttributs(e)));
    titreBilan = porteurs.find((e) => ![...e.children].some((c) => PHRASE.test(texteEtAttributs(c))));
    if (titreBilan) marqueBilan = 'phrase dans un champ';
  }

  /* ── quatrième marque : le bilan reconnu à sa FONCTION ────────────────────
     Les trois marques ci-dessus cherchent toutes un LIBELLÉ. Une séquence qui
     titre simplement « Bilan » et fait faire un vrai auto-positionnement leur
     échappe : `4e_C1.1-C1.3_tsinghua_feux` porte trois groupes de
     positionnement, un par code, douze niveaux à choisir, et les trois marques
     la déclaraient sans bilan.

     La fonction d'un bilan : l'élève s'y situe sur les compétences de la
     séquence. Mécaniquement — un groupe de choix mutuellement exclusifs dont
     l'intitulé a pour SUJET un code du référentiel, offrant au moins trois
     options. Aucun mot d'échelle n'entre ici : ni « maîtrise », ni
     « je sais », ni un émoji. Une échelle écrite autrement resterait vue.

     Le code doit être le SUJET, pas une mention au passage : deux questions de
     contenu du dépôt citent un code dans leur énoncé — « Le banc de 3e_C8.2
     retenait déjà celui-là », « En 4e_C7, tu as choisi un matériau ». Elles
     créeraient un bilan fantôme. D'où le `(?!\s*[,\w])` : dans un
     auto-positionnement, le code est suivi d'un tiret, d'un deux-points, d'une
     parenthèse ou de la fin ; dans une question, d'une virgule ou d'un verbe.
     Et le `(?![\d.])` ferme le code : sans lui « 3e_C8.2 retenait » se lirait
     « 3e_C8 » suivi d'un point. */
  const SUJET_CODE = /\b[345]e_C\d+(?:\.\d+)?(?![\d.])(?:\s*[·,]\s*C\d+(?:\.\d+)?(?![\d.]))*(?!\s*[,\w])/;
  const intituleDuGroupe = (g) => {
    if (g.tagName === 'FIELDSET') return (g.querySelector('legend')?.textContent || '');
    const aria = g.getAttribute('aria-label');
    if (aria) return aria;
    return (g.labels && g.labels.length) ? (g.labels[0].textContent || '') : '';
  };
  const positionnements = [...document.querySelectorAll('fieldset, select')].filter((g) => {
    const options = g.tagName === 'FIELDSET'
      ? g.querySelectorAll('input[type=radio]').length
      : g.querySelectorAll('option').length;
    return options >= 3 && SUJET_CODE.test(intituleDuGroupe(g).replace(/\s+/g, ' ').trim());
  });
  if (!titreBilan && positionnements.length) {
    titreBilan = positionnements[0];
    marqueBilan = `fonction (${positionnements.length} code(s))`;
  }

  /* ── le Bonus : la section dont le titre porte « Bonus » ────────────────── */
  const titreBonus = tous.find((e) => /^H[1-4]$/.test(e.tagName)
    && /\bbonus\b/i.test(e.textContent || ''));
  /* Le bloc du Bonus est le PARENT DIRECT de son titre — `section.card` dans la
     plupart des lots, `div.bloc-bonus` dans d'autres. Remonter jusqu'à la
     `<section>` la plus proche attribuait au Bonus tous les champs de la
     section qui l'accueille, renvoi au QCM compris : quinze champs comptés là
     où le Bonus n'en porte aucun. */
  const sectionBonus = titreBonus ? titreBonus.parentElement : null;

  /* ── le renvoi vers le QCM ──────────────────────────────────────────────── */
  const lienQcm = document.querySelector('#lienQcm')
    || [...document.querySelectorAll('a[href]')].find((a) => /qcm.*\.html$/i.test(a.getAttribute('href') || ''));

  /* ── les champs de réponse du Bonus ─────────────────────────────────────── */
  let champsBonus = 0, detailChamps = {};
  let corrigeBonus = false;
  if (sectionBonus) {
    const compte = (sel) => sectionBonus.querySelectorAll(sel).length;
    detailChamps = {
      textarea: compte('textarea'),
      /* les champs de saisie, boutons et cases de navigation exclus */
      input: [...sectionBonus.querySelectorAll('input')]
        .filter((i) => !/^(button|submit|reset|hidden)$/.test(i.type)).length,
      select: compte('select'),
      groupe: compte('fieldset.qcm-groupe'),
    };
    champsBonus = detailChamps.textarea + detailChamps.input + detailChamps.select + detailChamps.groupe;

    /* un corrigé : un bloc replié dont le résumé parle de corrigé, ou une zone
       de classe « correction » à l'intérieur du Bonus */
    corrigeBonus = [...sectionBonus.querySelectorAll('summary')]
      .some((s) => /corrig|solution|r[ée]ponse attendue/i.test(s.textContent || ''))
      || sectionBonus.querySelector('.correction') !== null;
  }

  const rBilan = titreBilan ? rang(titreBilan) : -1;
  const rBonus = titreBonus ? rang(titreBonus) : -1;
  const rQcm = lienQcm ? rang(lienQcm) : -1;

  return {
    bilan: !!titreBilan,
    marqueBilan,
    titreBilanTexte: titreBilan ? (titreBilan.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 50) : '',
    bonus: !!titreBonus,
    titreBonusTexte: titreBonus ? (titreBonus.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 50) : '',
    lienQcm: !!lienQcm,
    rBilan, rBonus, rQcm,
    bonusApresBilan: rBilan >= 0 && rBonus >= 0 ? rBonus > rBilan : null,
    qcmApresBilan: rBilan >= 0 && rQcm >= 0 ? rQcm > rBilan : null,
    champsBonus, detailChamps, corrigeBonus,
    /* le bilan porte-t-il lui-même de quoi se positionner ? */
    champsBilan: titreBilan
      ? (() => {
        const sec = titreBilan.closest('section, article, div.card') || titreBilan.parentElement;
        return sec ? sec.querySelectorAll('textarea, fieldset.qcm-groupe, select').length : 0;
      })()
      : 0,
  };
};

/* ════════════════════════════════════════════════════════════════════════════ */

let liste;
try { liste = fichiers(RACINE); }
catch (e) { enPanne(`racine impossible à parcourir (${RACINE}) : ${premiereLigne(e)}`); }
if (!liste.length) enPanne(`aucune séquence sous ${RACINE}`);

let navigateur;
try { navigateur = await chromium.launch(); }
catch (e) { enPanne(`le navigateur ne démarre pas : ${premiereLigne(e)}`); }

const lignes = [];
const illisibles = [];
for (const f of liste) {
  const rel = path.relative(DEPOT, f).replace(/\\/g, '/');
  const p = await navigateur.newPage({ viewport: { width: 1280, height: 900 } });
  try {
    await p.goto(pathToFileURL(f).href, { waitUntil: 'load' });
    await p.waitForTimeout(110);
    lignes.push({ rel, ...situer(rel), ...(await p.evaluate(MESURER)) });
  } catch (e) {
    illisibles.push({ rel, erreur: premiereLigne(e) });
  }
  await p.close();
}
await navigateur.close();

if (!lignes.length) enPanne(`${liste.length} fichier(s) ouverts, aucune séquence mesurée`);

/* ════════════════════════════════════════════════════════════════════════════
   Le rapport
   ════════════════════════════════════════════════════════════════════════════ */

const avecBilan = lignes.filter((l) => l.bilan);
const sansBilan = lignes.filter((l) => !l.bilan);
const avecBonus = lignes.filter((l) => l.bonus);
const bonusApres = lignes.filter((l) => l.bonusApresBilan === true);
const bonusMuet = avecBonus.filter((l) => l.champsBonus === 0);
const bonusSansCorrige = avecBonus.filter((l) => !l.corrigeBonus);
const qcmAvantBilan = lignes.filter((l) => l.qcmApresBilan === false);

console.log(`${lignes.length} séquence(s) analysées · ${illisibles.length} illisible(s)`);
console.log('     NON MESURÉ : la QUALITÉ d\'un corrigé — qu\'il traite la question posée, qu\'il');
console.log('     soit juste, qu\'il soit utile. Cela se lit. Cet audit constate la PRÉSENCE d\'un');
console.log('     bloc de corrigé, et rien de plus ; de même il ne juge pas le contenu d\'un bilan.');

console.log('\n═══ 1. CE QUI TERMINE UNE SÉQUENCE ═══');
console.log(`  ${avecBilan.length} / ${lignes.length} portent un bilan (libellé ou fonction)`);
console.log(`  ${sansBilan.length} / ${lignes.length} n'en portent AUCUN — elles ne se terminent par rien`);
console.log(`  ${avecBonus.length} / ${lignes.length} portent un Bonus`);
console.log(`  ${bonusApres.length} ont leur Bonus APRÈS le bilan — du travail demandé après la clôture`);
console.log(`  ${bonusMuet.length} / ${avecBonus.length} Bonus ne portent AUCUN champ de réponse — on ne peut que les lire`);
console.log(`  ${bonusSansCorrige.length} / ${avecBonus.length} Bonus n'ont aucun bloc de corrigé`);
console.log(`  ${qcmAvantBilan.length} renvoient vers le QCM AVANT le bilan`);

if (!muet) {
  console.log('\n═══ 2. LE DÉTAIL, LOT PAR LOT ═══');
  console.log('     « ordre » = position du Bonus par rapport au bilan · « champs » = champs de');
  console.log('     réponse dans le Bonus · « corrigé » = un bloc de corrigé y est présent.');
  for (const theme of ['1', '2', '3', '?']) {
    const duTheme = lignes.filter((l) => l.theme === theme);
    if (!duTheme.length) continue;
    console.log(`\n  ── Thème ${theme} — ${duTheme.length} séquence(s)`);
    console.log(`  ${'lot'.padEnd(10)}${'bilan'.padStart(7)}${'bonus'.padStart(7)}${'ordre'.padStart(14)}`
      + `${'champs'.padStart(8)}${'corrigé'.padStart(9)}   fichier`);
    for (const l of duTheme.slice().sort((a, b) => a.lot.localeCompare(b.lot))) {
      const ordre = !l.bonus ? '—'
        : l.bilan ? (l.bonusApresBilan ? 'APRÈS bilan' : 'avant bilan') : '(pas de bilan)';
      console.log(`  ${l.lot.padEnd(10)}${(l.bilan ? 'oui' : 'NON').padStart(7)}`
        + `${(l.bonus ? 'oui' : '—').padStart(7)}${ordre.padStart(14)}`
        + `${(l.bonus ? String(l.champsBonus) : '—').padStart(8)}`
        + `${(l.bonus ? (l.corrigeBonus ? 'oui' : 'NON') : '—').padStart(9)}   ${l.rel.split('/').pop()}`);
    }
  }

  console.log('\n═══ 3. LES SÉQUENCES SANS AUCUN BILAN ═══');
  console.log(`  ${sansBilan.length} séquence(s). C'est l'autre moitié du problème : elles ne se`);
  console.log('  terminent par rien, et aucun auto-positionnement n\'y est demandé.');
  for (const theme of ['1', '2', '3', '?']) {
    const l = sansBilan.filter((x) => x.theme === theme);
    if (!l.length) continue;
    console.log(`\n  Thème ${theme} — ${l.length} :`);
    for (const x of l.sort((a, b) => a.lot.localeCompare(b.lot))) {
      console.log(`     ${x.lot.padEnd(10)} ${x.bonus ? 'porte un Bonus' : 'sans Bonus'}   ${x.rel.split('/').pop()}`);
    }
  }
}

/* ── Synthèse ─────────────────────────────────────────────────────────────── */
console.log('\n═══ SYNTHÈSE ═══');
console.log(`  1. ${avecBilan.length} séquences sur ${lignes.length} portent un bilan ; `
  + `${sansBilan.length} n'en ont pas du tout.`);
console.log(`  2. Sur les ${avecBonus.length} séquences à Bonus, ${bonusApres.length} le placent APRÈS le bilan, `
  + `${bonusMuet.length} ne lui donnent aucun champ de réponse,`);
console.log(`     et ${bonusSansCorrige.length} n'y mettent aucun corrigé.`);
const aRegler = lignes.filter((l) => !l.bilan || l.bonusApresBilan === true
  || (l.bonus && l.champsBonus === 0) || (l.bonus && !l.corrigeBonus) || l.qcmApresBilan === false);
console.log(`  3. ${aRegler.length} séquence(s) sur ${lignes.length} sont concernées par au moins un de ces défauts.`);

if (illisibles.length) {
  console.log(`\n⚠ ${illisibles.length} fichier(s) illisible(s) :`);
  for (const i of illisibles) console.log(`  ${i.rel} — ${i.erreur}`);
}

if (veutCsv) {
  const entete = 'fichier;theme;niveau;lot;bilan;marque_bilan;bonus;bonus_apres_bilan;champs_bonus;'
    + 'textarea;input;select;groupe;corrige_bonus;lien_qcm;qcm_apres_bilan;champs_bilan';
  const corps = lignes.map((l) => [l.rel, l.theme, l.niveau, l.lot, l.bilan, l.marqueBilan || '', l.bonus,
    l.bonusApresBilan, l.champsBonus, l.detailChamps.textarea || 0, l.detailChamps.input || 0,
    l.detailChamps.select || 0, l.detailChamps.groupe || 0, l.corrigeBonus, l.lienQcm,
    l.qcmApresBilan, l.champsBilan].join(';'));
  const dest = path.join(ICI, 'audit_cloture_sequence.csv');
  fs.writeFileSync(dest, [entete, ...corps].join('\n') + '\n', 'utf-8');
  console.log(`\nCSV écrit : ${path.relative(DEPOT, dest).replace(/\\/g, '/')}`);
}

console.log('\n✅ mesure terminée — cet audit ne refuse rien, il rapporte.');
process.exit(0);
