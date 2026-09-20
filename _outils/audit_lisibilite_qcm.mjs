/* audit_lisibilite_qcm.mjs — les propositions qui masquent la question.
 *
 * LE CONSTAT QUI A DONNÉ CET AUDIT
 * --------------------------------
 * Constat de classe, élèves de 3e : en répondant, on perd la question. Le cas
 * s'est produit dans une SÉQUENCE — `3e_C1.1`, séance 1 — et non dans un QCM
 * autonome. C'est ce qui oriente tout l'audit.
 *
 * Une séquence pose ses questions en `<select>`. Une liste déroulante native
 * n'est PAS dessinée dans la page : le système la dessine PAR-DESSUS, ancrée au
 * `<select>`, et elle recouvre ce qui l'entoure — donc l'énoncé, qui le précède
 * immédiatement. Un QCM autonome, lui, pose ses propositions en `<button>` :
 * elles occupent de la place dans le flux, s'enroulent sur plusieurs lignes et
 * POUSSENT le contenu au lieu de le couvrir. Deux formes, deux comportements.
 *
 * Plus une proposition est longue, plus le menu natif est haut, et plus il
 * remonte : la longueur du texte est donc la grandeur à mesurer.
 *
 * CE QUE CET OUTIL MESURE, ET CE QU'IL NE MESURE PAS
 * --------------------------------------------------
 * Il MESURE : le nombre de questions à liste déroulante, la longueur de leur
 * plus longue proposition, l'uniformité du gabarit, la géométrie de la page, et
 * le gabarit des QCM autonomes vers lequel on ira.
 *
 * Il ne SIMULE PAS la liste ouverte et ne prétend pas l'avoir vue. Elle vit hors
 * du DOM : aucun outil de page ne la mesure, Playwright pas davantage. Dessiner
 * un faux menu en HTML pour le mesurer donnerait un chiffre qui ne serait le
 * chiffre de rien. On rapporte la LONGUEUR des propositions, qui commande la
 * hauteur du menu — c'est tout ce qu'on peut établir honnêtement.
 *
 * LA POSITION DU CHAMP : UN CRITÈRE MESURÉ, PUIS ABANDONNÉ
 * --------------------------------------------------------
 * L'hypothèse de départ était géométrique : un `<select>` situé dans le tiers
 * bas de la fenêtre y ouvrirait sa liste vers le haut, par-dessus l'énoncé. Le
 * critère a été mesuré aux deux tailles, et LA MESURE LE TUE — 1 question sur
 * 1 480 sur téléphone, AUCUNE sur le portable de classe. Si la position
 * expliquait quoi que ce soit, le constat de classe serait introuvable.
 *
 * Le chiffre reste calculé et rapporté (section 6), mais comme RÉSULTAT
 * NÉGATIF : il établit qu'aucune règle du dépôt ne devra se fonder sur cette
 * géométrie. La liste native se dessine par-dessus la page quelle que soit la
 * position du champ, dès qu'elle est trop haute pour tenir sous lui ; ce qui
 * commande sa hauteur est le NOMBRE de propositions et la LONGUEUR de leur
 * texte.
 *
 * LES DEUX TAILLES, ET POURQUOI CELLES-LÀ
 * ---------------------------------------
 * Elles font varier la HAUTEUR, qui est ce qui compte ici, non la largeur :
 *   · 390 × 844   téléphone, la taille du constat de départ ;
 *   · 1280 × 720  portable de salle de classe — 720 px de haut, soit MOINS que
 *     le téléphone. C'est le cas défavorable, et le plus fréquent en classe.
 *
 * Usage :
 *   node _outils/audit_lisibilite_qcm.mjs              # rapport complet
 *   node _outils/audit_lisibilite_qcm.mjs --muet       # synthèse seule
 *   node _outils/audit_lisibilite_qcm.mjs --csv        # + audit_lisibilite_qcm.csv
 *   node _outils/audit_lisibilite_qcm.mjs <racine>     # restreindre le balayage
 *
 * Sortie : 0 la mesure a eu lieu · 2 elle n'a RIEN pu analyser (règle d'or n°299).
 * Cet audit ne REFUSE rien : il mesure. Il n'a donc pas de code 1.
 */
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

/* `fileURLToPath`, jamais `new URL(...).pathname` : ce dernier rend « /C:/… »
   sous Windows et fabrique un chemin à deux lettres de lecteur. */
const ICI = path.dirname(fileURLToPath(import.meta.url));
const DEPOT = path.dirname(ICI);

const ECARTES = /_archive-anciennes-versions|[/\\]\.git|[/\\]node_modules/;
const SEQUENCE = /^sequence[_-].*\.html$|^sequence\.html$/i;
const QCM = /^qcm.*\.html$/i;

const SEUILS = [60, 90, 120];
const TAILLES = [
  { nom: '390×844', width: 390, height: 844, quoi: 'téléphone' },
  { nom: '1280×720', width: 1280, height: 720, quoi: 'portable de classe' },
];
/** Le lot sur lequel on chiffre le coût de conversion : celui du constat. */
const TEMOIN = /3e_C1\.1/;

const muet = process.argv.includes('--muet');
const veutCsv = process.argv.includes('--csv');
const cible = process.argv.slice(2).find((a) => !a.startsWith('--'));
const RACINE = cible ? path.resolve(DEPOT, cible) : DEPOT;

const premiereLigne = (e) => String(e && e.message).split(/\r?\n/)[0].slice(0, 120);

/** Règle d'or n°299 : un contrôle qui n'a rien analysé n'est pas vert, il est
 *  en panne. Il le dit sur stderr — donc visible sous `--muet` — et sort à 2. */
function enPanne(motif) {
  console.error(`⛔ EN PANNE — ${motif}`);
  console.error("     Cet audit n'a RIEN mesuré ; ne le lisez pas comme un résultat (règle d'or n°299).");
  process.exit(2);
}

function fichiers(dossier, acc = []) {
  for (const e of fs.readdirSync(dossier, { withFileTypes: true })) {
    const p = path.join(dossier, e.name);
    if (ECARTES.test(p)) continue;
    if (e.isDirectory()) fichiers(p, acc);
    else if (SEQUENCE.test(e.name)) acc.push({ f: p, forme: 'select' });
    else if (QCM.test(e.name)) acc.push({ f: p, forme: 'boutons' });
  }
  return acc;
}

/** Thème et niveau, lus dans le chemin — jamais devinés autrement. */
function situer(rel) {
  return {
    theme: (rel.match(/theme-(\d)/) || [, '?'])[1],
    niveau: (rel.match(/[/\\]([345]e)[/\\]/) || [, '?'])[1],
  };
}

/* ════════════════════════════════════════════════════════════════════════════
   1. LES SÉQUENCES — questions en <select>
   ════════════════════════════════════════════════════════════════════════════ */

const MESURER_SELECTS = () => {
  const out = [];

  const collante = () => {
    let h = 0;
    for (const e of document.querySelectorAll('body *')) {
      const s = getComputedStyle(e);
      if (s.position !== 'sticky' && s.position !== 'fixed') continue;
      const r = e.getBoundingClientRect();
      if (r.height > 0 && r.top <= 1 && r.height < innerHeight / 2) h = Math.max(h, r.height);
    }
    return Math.round(h);
  };
  const hCollante = collante();

  const panneaux = [...document.querySelectorAll('.seance-panel')];
  const selects = [...document.querySelectorAll('select')];

  /* Des formes AUTRES que la liste déroulante, déjà présentes dans les
     séquences : ce sont des précédents, et on les cherche exprès. */
  const autresFormes = {
    radios: document.querySelectorAll('input[type="radio"]').length,
    cases: document.querySelectorAll('input[type="checkbox"]').length,
    boutonsOption: document.querySelectorAll('button.option, .options button').length,
    gabarit: null,
  };
  /* Si une séquence emploie déjà des boutons radio, on relève son gabarit avec
     la même précision que celui des QCM autonomes : c'est un modèle candidat,
     et il vit DÉJÀ dans une séquence — donc avec sa sauvegarde et son banc. */
  const unRadio = document.querySelector('input[type="radio"]');
  if (unRadio) {
    const enveloppe = unRadio.closest('label, div, li') || unRadio.parentElement;
    const etiquette = unRadio.id ? document.querySelector(`label[for="${CSS.escape(unRadio.id)}"]`)
      : (enveloppe ? enveloppe.querySelector('label') : null);
    const ce = enveloppe ? getComputedStyle(enveloppe) : null;
    const groupe = unRadio.name
      ? document.querySelectorAll(`input[type="radio"][name="${CSS.escape(unRadio.name)}"]`).length : 0;
    autresFormes.gabarit = {
      enveloppe: enveloppe ? enveloppe.tagName.toLowerCase() + '.' + (enveloppe.className || '(sans classe)') : '(aucune)',
      disposition: ce ? `${ce.display} · align ${ce.alignItems} · gap ${ce.gap}` : '',
      champ: `input[type=radio]${unRadio.name ? ' name="' + unRadio.name + '"' : ' (SANS name)'}`,
      tailleGroupe: groupe,
      etiquette: etiquette ? etiquette.tagName.toLowerCase() + '.' + (etiquette.className || '(sans classe)') : '(aucune)',
      texte: etiquette ? etiquette.textContent.replace(/\s+/g, ' ').trim().slice(0, 90) : '',
      enroule: etiquette ? getComputedStyle(etiquette).whiteSpace !== 'nowrap' : null,
    };
  }

  for (const sel of selects) {
    const mien = sel.closest('.seance-panel');
    if (mien) for (const p of panneaux) p.classList.toggle('active', p === mien);

    const ouverts = [];
    for (let d = sel.closest('details'); d; d = d.parentElement && d.parentElement.closest('details')) {
      if (!d.open) { d.open = true; ouverts.push(d); }
    }

    /* L'ÉNONCÉ, et par quel gabarit il est rattaché au champ.
       Le balayage a montré que le dépôt n'en connaît pas un mais TROIS : le
       jeter au lieu de le classer ferait disparaître 387 questions du compte. */
    let lab = sel.id ? document.querySelector(`label[for="${CSS.escape(sel.id)}"]`) : null;
    let famille = lab ? 'label-for' : '';
    if (!lab) {
      const bloc = sel.closest('.assoc, p, li, div');
      const l2 = bloc ? bloc.querySelector('label') : null;
      if (l2) { lab = l2; famille = 'label-bloc'; }
    }
    /* 2e gabarit : l'énoncé est un <p>, le champ vit dans un bloc d'exercice. */
    if (!lab) {
      const bloc = sel.closest('.exo, .card, div, td, p');
      let prec = sel.previousElementSibling;
      while (prec && !/^(P|H2|H3|H4|SPAN|LI)$/.test(prec.tagName)) prec = prec.previousElementSibling;
      if (!prec && bloc) prec = bloc.querySelector('p, h3, h4');
      if (prec && prec.textContent.trim().length > 8) { lab = prec; famille = 'enonce-p'; }
    }
    /* 3e gabarit : le champ est EN LIGNE dans un tableau ou une étape, et porte
       lui-même son énoncé en aria-label. Il n'y a alors aucun énoncé au-dessus
       de lui à recouvrir — le risque est d'une autre nature. */
    const aria = sel.getAttribute('aria-label') || '';
    if (!lab && aria) famille = 'aria-en-ligne';
    if (!famille) famille = 'aucun';

    /* Le gabarit est-il celui qu'on croit : « <label> puis <select>, rien entre » ?
       On regarde ce qui sépare réellement les deux nœuds dans le document. */
    let colle = false, separateur = '';
    if (lab) {
      /* On parcourt le document DANS L'ORDRE, de la fin de l'énoncé au début du
         champ, et on retient ce qui occupe réellement de la place. Compter les
         frères de nœud déclarait « autre parent » 162 questions dont l'énoncé
         précède pourtant immédiatement le champ : c'est la mise en page qui
         compte ici, pas la parenté dans l'arbre. */
      const vus = [];
      const marche = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT);
      marche.currentNode = lab;
      let n = marche.nextNode();
      while (n && n !== sel) {
        if (!lab.contains(n) && !n.contains(sel)) {
          const r = n.getBoundingClientRect();
          if (r.height > 2) vus.push(n.tagName.toLowerCase());
        }
        n = marche.nextNode();
      }
      colle = vus.length === 0;
      separateur = vus.slice(0, 4).join(',');
    } else if (aria) {
      /* Champ en ligne : il n'a pas d'énoncé AU-DESSUS de lui, donc la question
         « collé ou non » ne se pose pas. On ne le compte pas comme exception. */
      colle = null; separateur = '(champ en ligne, énoncé porté par aria-label)';
    }

    /* La séance : le panneau, et le libellé de son onglet. */
    const panneau = mien ? mien.id : '';
    const onglet = panneau ? document.getElementById('tab-' + panneau) : null;
    /* `textContent` colle « Séance 4 » et son titre, que le <br> séparait :
       on rend l'espace, sans quoi le rapport écrit « Séance 4Incommensurable ». */
    const seance = onglet
      ? [...onglet.childNodes].map((n) => n.textContent).join(' ').replace(/\s+/g, ' ').trim().slice(0, 44)
      : (panneau || '(hors séance)');

    /* Les propositions : on écarte l'invite « — choisir — », qui n'en est pas une. */
    const props = [...sel.options]
      .filter((o, k) => !(k === 0 && (o.value === '' || /^[—–-]/.test(o.textContent.trim()))))
      .map((o) => o.textContent.replace(/\s+/g, ' ').trim());
    const plusLongue = props.reduce((a, b) => (b.length > a.length ? b : a), '');

    const rs = sel.getBoundingClientRect();
    const visible = rs.width > 0 || rs.height > 0;
    const rl = lab ? lab.getBoundingClientRect() : null;

    /* Une image glissée entre l'énoncé et le <select> ? */
    let image = false;
    const bloc = sel.closest('.assoc, li, p, div');
    if (bloc && rl) {
      for (const img of bloc.querySelectorAll('img, svg, figure')) {
        const ri = img.getBoundingClientRect();
        if (ri.height > 12 && ri.top >= rl.bottom - 2 && ri.bottom <= rs.top + 2) image = true;
      }
    }

    out.push({
      id: sel.id || '(sans id)',
      seance,
      famille,
      sansEnonce: famille === 'aucun',
      invisible: !visible,
      colle,
      separateur,
      enonce: lab ? lab.textContent.replace(/\s+/g, ' ').trim().slice(0, 110)
        : (aria ? aria.replace(/\s+/g, ' ').trim().slice(0, 110) : ''),
      nProps: props.length,
      longueur: plusLongue.length,
      plusLongue: plusLongue.slice(0, 210),
      image,
      etendue: (visible && rl) ? Math.round(rs.bottom - rl.top) : null,
      collante: hCollante,
    });

    for (const d of ouverts) d.open = false;
  }
  return { out, autresFormes };
};

/* ════════════════════════════════════════════════════════════════════════════
   2. LES QCM AUTONOMES — questions à boutons (mesure brève, second plan)
   ════════════════════════════════════════════════════════════════════════════ */

const MESURER_BOUTONS = () => {
  const out = [];
  if (typeof QUESTIONS === 'undefined' || typeof etat === 'undefined'
      || typeof rendreTout !== 'function') return { incompatible: true, out, gabarit: null };

  const collante = () => {
    let h = 0;
    for (const e of document.querySelectorAll('body *')) {
      const s = getComputedStyle(e);
      if (s.position !== 'sticky' && s.position !== 'fixed') continue;
      const r = e.getBoundingClientRect();
      if (r.height > 0 && r.top <= 1 && r.height < innerHeight / 2) h = Math.max(h, r.height);
    }
    return Math.round(h);
  };
  const hCollante = collante();

  for (let i = 0; i < QUESTIONS.length; i++) {
    etat.courante = i;
    if (typeof montrerEcran === 'function') montrerEcran('q');
    rendreTout();
    const txt = document.getElementById('qTexte');
    const opts = document.getElementById('qOptions');
    const fig = document.getElementById('qFigure');
    if (!txt || !opts || !opts.children.length) { out.push({ n: i + 1, incomplet: true }); continue; }

    const dernier = opts.children[opts.children.length - 1];
    const rt = txt.getBoundingClientRect(), rd = dernier.getBoundingClientRect();
    const figVisible = !!(fig && !fig.hidden && fig.getBoundingClientRect().height > 12);
    const textes = [...opts.children].map((b) => b.textContent.replace(/\s+/g, ' ').trim());
    const plusLongue = textes.reduce((a, b) => (b.length > a.length ? b : a), '');

    out.push({
      n: i + 1,
      enonce: txt.textContent.replace(/\s+/g, ' ').trim().slice(0, 110),
      nProps: opts.children.length,
      longueur: plusLongue.length,
      plusLongue: plusLongue.slice(0, 210),
      image: figVisible,
      etendue: Math.round(rd.bottom - rt.top),
      collante: hCollante,
    });
  }

  /* Le gabarit, relevé sur la première question — c'est le modèle vers lequel
     on ira, donc on le décrit par la mesure et non de mémoire. */
  let gabarit = null;
  const opts = document.getElementById('qOptions');
  if (opts && opts.children.length) {
    const b = opts.children[0];
    const cs = getComputedStyle(opts), cb = getComputedStyle(b);
    gabarit = {
      conteneur: opts.tagName.toLowerCase() + '.' + (opts.className || '(sans classe)'),
      roleConteneur: opts.getAttribute('role') || '(aucun)',
      ariaConteneur: opts.getAttribute('aria-label') || '(aucun)',
      dispositionConteneur: `${cs.display} · gap ${cs.gap}`,
      option: b.tagName.toLowerCase() + '.' + (b.className || '(sans classe)'),
      roleOption: b.getAttribute('role') || '(aucun — c\'est un <button> natif)',
      tabindex: b.getAttribute('tabindex') || '(aucun — un <button> est focalisable d\'office)',
      dispositionOption: `${cb.display} · align ${cb.alignItems} · text-align ${cb.textAlign}`,
      enroule: cb.whiteSpace !== 'nowrap',
      interieur: b.innerHTML.replace(/\s+/g, ' ').slice(0, 120),
      focusable: b.tabIndex >= 0,
      desactivable: 'disabled' in b,
    };
  }
  return { incompatible: false, out, gabarit };
};

/* ════════════════════════════════════════════════════════════════════════════
   3. LE COÛT DE CONVERSION, chiffré sur le lot témoin
   ════════════════════════════════════════════════════════════════════════════ */

/** Ce qu'il faudrait toucher pour passer une séquence du `<select>` au bouton.
 *  Tout est LU dans le fichier, rien n'est estimé de mémoire. */
function coutConversion(source, nQuestions, ids, dossier) {
  const lignes = source.split('\n');
  const compte = (re) => (source.match(re) || []).length;

  /* Le banc du lot : ce qu'il faudrait y toucher. On le LIT, on ne le suppose
     pas — la première version de ce rapport affirmait « le banc suit sans
     réécriture », ce qui n'était pas mesuré. */
  const bancs = [];
  try {
    for (const n of fs.readdirSync(dossier)) {
      if (!/^tests?[_-].*\.(py|mjs|js)$/i.test(n)) continue;
      const t = fs.readFileSync(path.join(dossier, n), 'utf-8');
      bancs.push({
        nom: n,
        lignes: t.split('\n').length,
        poseValeur: (t.match(/\.value\s*=/g) || []).length,
        litValeur: (t.match(/\.value\b(?!\s*=)/g) || []).length,
        selectOption: (t.match(/select_option|selectOption/g) || []).length,
        nommeSelect: (t.match(/\bselect\b/gi) || []).length,
      });
    }
  } catch { /* pas de banc à côté : on le dira */ }

  /* La feuille d'impression énumère-t-elle les identifiants à la main ? */
  let idsImprimes = 0, ligneImpression = 0;
  lignes.forEach((l, k) => {
    if (!/@media print/.test(l) && !/#\w+,#\w+/.test(l)) return;
    const trouves = ids.filter((id) => new RegExp('#' + id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b').test(l));
    if (trouves.length > idsImprimes) { idsImprimes = trouves.length; ligneImpression = k + 1; }
  });

  return {
    questions: nQuestions,
    /* la sauvegarde : générique ou nominative ? */
    sauvegardeGenerique: /querySelectorAll\(["']select[^"']*["']\)/.test(source),
    lignesSauvegarde: lignes.filter((l) => /querySelectorAll\(["']select/.test(l)).length,
    /* l'accesseur de valeur, cœur de la vérification */
    accesseurVal: compte(/const val\s*=/g),
    appelsVal: compte(/\bval\(/g),
    lectureValeurDirecte: compte(/\.value\b/g),
    /* l'impression : une énumération d'identifiants écrite à la main */
    idsEnumeresImpression: idsImprimes,
    ligneImpression,
    /* le CSS des listes */
    cssSelect: compte(/(^|[\s,{])select\b[^{]*\{/gm) + compte(/\.assoc\s+option/g),
    /* la TABLE DES RÉPONSES : « identifiant: "texte de la proposition" ».
       C'est le point décisif du chiffrage. Les bonnes réponses sont comparées
       au TEXTE de l'option (`val(id) === v`), pas à un indice : si le nouveau
       champ sait rendre ce même texte, aucune table n'est à réécrire. */
    entreesTable: compte(/\b[a-z][a-z0-9_]*:\s*"/g),
    comparaisonParTexte: /val\([^)]*\)\s*===/.test(source),
    bancs,
  };
}

/* ════════════════════════════════════════════════════════════════════════════
   Le balayage
   ════════════════════════════════════════════════════════════════════════════ */

let liste;
try { liste = fichiers(RACINE); }
catch (e) { enPanne(`racine impossible à parcourir (${RACINE}) : ${premiereLigne(e)}`); }
if (!liste.length) {
  enPanne(`aucune séquence ni QCM sous ${RACINE} `
    + `(attendu : sequence_*.html, sequence-*.html, sequence.html, qcm*.html)`);
}

let navigateur;
try { navigateur = await chromium.launch(); }
catch (e) { enPanne(`le navigateur ne démarre pas : ${premiereLigne(e)}`); }

const parFichier = [];      // une ligne par fichier
const toutesQuestions = []; // une ligne par question (séquences)
const illisibles = [];
let gabaritBoutons = null;
let temoin = null;
const autresFormesTotal = { radios: 0, cases: 0, boutonsOption: 0, fichiers: [] };

for (const { f, forme } of liste) {
  const rel = path.relative(DEPOT, f).replace(/\\/g, '/');
  const ctx = await navigateur.newContext({ viewport: { width: TAILLES[0].width, height: TAILLES[0].height } });
  const page = await ctx.newPage();
  try {
    await page.goto(pathToFileURL(f).href, { waitUntil: 'load' });
    await page.waitForTimeout(130);

    const geo = {};
    let mesures = [], incompatible = false;

    if (forme === 'select') {
      const r1 = await page.evaluate(MESURER_SELECTS);
      mesures = r1.out;
      if (r1.autresFormes.radios || r1.autresFormes.cases || r1.autresFormes.boutonsOption) {
        autresFormesTotal.radios += r1.autresFormes.radios;
        autresFormesTotal.cases += r1.autresFormes.cases;
        autresFormesTotal.boutonsOption += r1.autresFormes.boutonsOption;
        autresFormesTotal.fichiers.push({ rel, ...r1.autresFormes });
        if (r1.autresFormes.gabarit && !autresFormesTotal.gabaritRadio) {
          autresFormesTotal.gabaritRadio = { rel, ...r1.autresFormes.gabarit };
        }
      }
      geo[TAILLES[0].nom] = mesures.filter((m) => m.etendue !== null)
        .filter((m) => m.etendue > (2 / 3) * (TAILLES[0].height - m.collante)).length;
      await page.setViewportSize({ width: TAILLES[1].width, height: TAILLES[1].height });
      await page.waitForTimeout(90);
      const r2 = await page.evaluate(MESURER_SELECTS);
      geo[TAILLES[1].nom] = r2.out.filter((m) => m.etendue !== null)
        .filter((m) => m.etendue > (2 / 3) * (TAILLES[1].height - m.collante)).length;

      if (TEMOIN.test(rel) && !temoin) {
        const src = fs.readFileSync(f, 'utf-8');
        const ids = mesures.map((m) => m.id).filter((i) => i !== '(sans id)');
        temoin = { rel, ...coutConversion(src, mesures.length, ids, path.dirname(f)), octets: src.length };
      }
    } else {
      const r = await page.evaluate(MESURER_BOUTONS);
      mesures = r.out; incompatible = r.incompatible;
      if (r.gabarit && !gabaritBoutons) gabaritBoutons = { rel, ...r.gabarit };
      geo[TAILLES[0].nom] = mesures.filter((m) => typeof m.etendue === 'number')
        .filter((m) => m.etendue > (2 / 3) * (TAILLES[0].height - m.collante)).length;
      await page.setViewportSize({ width: TAILLES[1].width, height: TAILLES[1].height });
      await page.waitForTimeout(90);
      const r2 = await page.evaluate(MESURER_BOUTONS);
      geo[TAILLES[1].nom] = r2.out.filter((m) => typeof m.etendue === 'number')
        .filter((m) => m.etendue > (2 / 3) * (TAILLES[1].height - m.collante)).length;
    }

    const vraies = mesures.filter((m) => !m.sansEnonce && !m.incomplet);
    const parFamille = {};
    for (const m of vraies) if (m.famille) parFamille[m.famille] = (parFamille[m.famille] || 0) + 1;
    for (const m of vraies) if (forme === 'select') toutesQuestions.push({ ...m, rel, ...situer(rel) });

    parFichier.push({
      rel, forme, ...situer(rel), incompatible,
      questions: vraies.length,
      parFamille,
      sansEnonce: mesures.filter((m) => m.sansEnonce).length,
      nonColles: vraies.filter((m) => m.colle === false).length,
      seuils: SEUILS.map((s) => vraies.filter((m) => m.longueur > s).length),
      geo,
    });
  } catch (e) {
    illisibles.push({ rel, erreur: premiereLigne(e) });
  }
  await ctx.close();
}
await navigateur.close();

const totalQuestions = parFichier.reduce((s, r) => s + r.questions, 0);
if (!totalQuestions) enPanne(`${liste.length} fichier(s) ouverts, aucune question mesurée`);

/* ════════════════════════════════════════════════════════════════════════════
   Le rapport
   ════════════════════════════════════════════════════════════════════════════ */

const seq = parFichier.filter((r) => r.forme === 'select');
const qcm = parFichier.filter((r) => r.forme === 'boutons');
const nSeq = seq.reduce((s, r) => s + r.questions, 0);
const nQcm = qcm.reduce((s, r) => s + r.questions, 0);
const pct = (a, b) => (b ? (100 * a / b).toFixed(1) + ' %' : '—');
const somme = (l, i) => l.reduce((s, r) => s + r.seuils[i], 0);

console.log(`${liste.length} fichier(s) analysés — ${seq.length} séquence(s), ${qcm.length} QCM autonome(s) `
  + `· ${nSeq} question(s) à liste déroulante · ${nQcm} question(s) à boutons `
  + `· ${illisibles.length} illisible(s)`);
console.log('     NON MESURÉ : la liste déroulante native OUVERTE. Le système la dessine hors du');
console.log('     DOM ; aucun outil de page ne la voit. Ce qui suit est la LONGUEUR des');
console.log('     propositions et la géométrie qui la rendent dangereuse, pas une simulation.');

/* ── 1. Par niveau et par thème ─────────────────────────────────────────────── */
if (!muet) {
  console.log('\n═══ 1. LES QUESTIONS À LISTE DÉROULANTE — par thème et par niveau ═══');
  console.log('     « > N » = questions dont la PLUS LONGUE proposition dépasse N caractères.');
  console.log(`\n  ${'périmètre'.padEnd(22)}${'fichiers'.padStart(9)}${'questions'.padStart(10)}`
    + SEUILS.map((s) => ('> ' + s).padStart(9)).join(''));
  for (const theme of ['1', '2', '3', '?']) {
    const l = seq.filter((r) => r.theme === theme);
    if (!l.length) continue;
    const q = l.reduce((s, r) => s + r.questions, 0);
    console.log(`  ${('Thème ' + theme).padEnd(22)}${String(l.length).padStart(9)}${String(q).padStart(10)}`
      + SEUILS.map((_, i) => String(somme(l, i)).padStart(9)).join(''));
    for (const niveau of ['3e', '4e', '5e', '?']) {
      const n = l.filter((r) => r.niveau === niveau);
      if (!n.length) continue;
      const qn = n.reduce((s, r) => s + r.questions, 0);
      console.log(`  ${('   ' + niveau).padEnd(22)}${String(n.length).padStart(9)}${String(qn).padStart(10)}`
        + SEUILS.map((_, i) => String(somme(n, i)).padStart(9)).join(''));
    }
  }
  console.log(`  ${'TOTAL'.padEnd(22)}${String(seq.length).padStart(9)}${String(nSeq).padStart(10)}`
    + SEUILS.map((_, i) => String(somme(seq, i)).padStart(9)).join(''));

  console.log('\n  ── Par fichier (les 20 qui portent le plus de questions longues) ──');
  const parLongues = seq.slice().sort((a, b) => b.seuils[0] - a.seuils[0]).slice(0, 20);
  for (const r of parLongues) {
    if (!r.seuils[0]) continue;
    console.log(`  ${String(r.questions).padStart(4)} q · > 60 : ${String(r.seuils[0]).padStart(3)}`
      + ` · > 90 : ${String(r.seuils[1]).padStart(3)} · > 120 : ${String(r.seuils[2]).padStart(3)}  ${r.rel}`);
  }
}

/* ── 2. Les vingt pires ─────────────────────────────────────────────────────── */
console.log('\n═══ 2. LES VINGT PIRES QUESTIONS DU DÉPÔT ═══');
console.log('     Classées par la longueur de leur plus longue proposition.');
const pires = toutesQuestions.slice().sort((a, b) => b.longueur - a.longueur).slice(0, 20);
pires.forEach((p, k) => {
  console.log(`\n  ${String(k + 1).padStart(2)}. ${p.longueur} caractères · ${p.nProps} propositions`
    + `${p.image ? ' · IMAGE intercalée' : ''}`);
  console.log(`      ${p.rel}`);
  console.log(`      séance : ${p.seance} · champ : ${p.id}`);
  console.log(`      énoncé : « ${p.enonce} »`);
  console.log(`      la plus longue : « ${p.plusLongue} »`);
});

/* ── 3. L'uniformité du gabarit ─────────────────────────────────────────────── */
console.log('\n═══ 3. LE GABARIT DES SÉQUENCES EST-IL UNIFORME ? ═══');

const FAMILLES = {
  'label-for': '<label for="id"> puis <select id="id"> — le gabarit de référence',
  'label-bloc': '<label> sans for=, dans le même bloc que le <select>',
  'enonce-p': "l'énoncé est un <p> (ou un titre), pas un <label> — blocs d'exercice",
  'aria-en-ligne': 'champ EN LIGNE (tableau, étape) portant son énoncé en aria-label',
};
const totauxFam = {};
for (const r of parFichier) for (const [k, v] of Object.entries(r.parFamille || {})) totauxFam[k] = (totauxFam[k] || 0) + v;

console.log('  NON : le dépôt emploie plusieurs gabarits, et non un seul.');

/* La séparation qui compte n\'est pas entre gabarits, mais entre les questions que
   cette affaire CONCERNE et celles qu\'elle ne concerne pas. */
const enLigneTotal = totauxFam['aria-en-ligne'] || 0;
const auDessusTotal = toutesQuestions.length - enLigneTotal;
console.log('');
console.log(`  A — énoncé AU-DESSUS du champ ...... ${String(auDessusTotal).padStart(5)} question(s)  CONCERNÉES`);
console.log('      la liste native peut les recouvrir : c\'est le sujet de cet audit.');
console.log(`  B — champ EN LIGNE (aria-label) .... ${String(enLigneTotal).padStart(5)} question(s)  NON CONCERNÉES`);
console.log('      leur énoncé n\'est pas au-dessus d\'eux mais dans leur attribut : il n\'y a RIEN');
console.log('      à recouvrir. Elles vivent en ligne, dans des cellules de tableau et des');
console.log('      étapes d\'algorithme. Elles NE RELÈVENT PAS de cette règle et NE DOIVENT');
console.log('      PAS entrer dans une conversion : un bouton pleine largeur au milieu d\'une');
console.log('      phrase ou dans une cellule casserait la mise en page.');

console.log(`\n  ${'gabarit'.padEnd(16)}${'fam.'.padStart(5)}${'questions'.padStart(11)}   description`);
for (const [k, v] of Object.entries(totauxFam).sort((a, b) => b[1] - a[1])) {
  const fam = k === 'aria-en-ligne' ? 'B' : 'A';
  console.log(`  ${k.padEnd(16)}${fam.padStart(5)}${String(v).padStart(11)}   ${FAMILLES[k] || ''}`);
}
console.log(`  ${'TOTAL'.padEnd(16)}${String(toutesQuestions.length).padStart(10)}`);
const sansEnonceTotal = parFichier.reduce((s, r) => s + r.sansEnonce, 0);
if (sansEnonceTotal) {
  console.log(`  ${sansEnonceTotal} <select> sans énoncé rattachable d'aucune façon — non comptés.`);
}

console.log('\n  ── L\'énoncé est-il COLLÉ au champ ? ──');
const avecEnonceAuDessus = toutesQuestions.filter((q) => q.colle !== null);
const nonColles = avecEnonceAuDessus.filter((q) => q.colle === false);
console.log(`  Sur les ${avecEnonceAuDessus.length} question(s) dont l'énoncé PRÉCÈDE le champ :`);
console.log(`  ${avecEnonceAuDessus.length - nonColles.length} ont l'énoncé immédiatement suivi du champ, rien entre les deux`);
console.log(`  ${nonColles.length} ont quelque chose qui s'intercale.`);
console.log(`  (les ${toutesQuestions.length - avecEnonceAuDessus.length} champs de la famille B sont hors de cette question, par construction)`);
if (nonColles.length) {
  console.log('\n  Ce qui s\'intercale — ce sont peut-être des précédents à suivre :');
  const parSep = new Map();
  for (const q of nonColles) {
    const k = q.separateur || "(rien d'identifiable)";
    if (!parSep.has(k)) parSep.set(k, []);
    parSep.get(k).push(q);
  }
  for (const [sep, qs] of [...parSep].sort((a, b) => b[1].length - a[1].length).slice(0, 8)) {
    console.log(`     « ${sep} » — ${qs.length} question(s)`);
    for (const q of qs.slice(0, 3)) console.log(`        ${q.rel}  ${q.id}  (${q.seance})`);
    if (qs.length > 3) console.log(`        … et ${qs.length - 3} autre(s)`);
  }
}

console.log('\n  ── Une autre forme est-elle DÉJÀ employée dans une séquence ? ──');
if (!autresFormesTotal.fichiers.length) {
  console.log('  Aucune. Pas un seul bouton-réponse, ni radio, ni case à cocher dans les 60');
  console.log('  séquences : la liste déroulante est la forme unique, sans précédent à suivre.');
} else {
  console.log(`  ${autresFormesTotal.radios} radio(s) · ${autresFormesTotal.cases} case(s) à cocher · `
    + `${autresFormesTotal.boutonsOption} bouton(s)-option, sur ${autresFormesTotal.fichiers.length} fichier(s) :`);
  for (const f of autresFormesTotal.fichiers.slice(0, 12)) {
    console.log(`     ${f.rel}\n        ${f.radios} radio · ${f.cases} case · ${f.boutonsOption} bouton-option`);
  }
  if (autresFormesTotal.fichiers.length > 12) {
    console.log(`     … et ${autresFormesTotal.fichiers.length - 12} autre(s) fichier(s)`);
  }
  const g = autresFormesTotal.gabaritRadio;
  if (g) {
    console.log('\n  ── LE SECOND PRÉCÉDENT : des boutons radio, DÉJÀ dans une séquence ──');
    console.log(`  Relevé sur ${g.rel}`);
    console.log(`  · enveloppe      ${g.enveloppe}`);
    console.log(`    disposition    ${g.disposition}`);
    console.log(`  · champ          ${g.champ}`);
    console.log(`    groupe         ${g.tailleGroupe} bouton(s) portant le même name=`);
    console.log(`  · étiquette      ${g.etiquette}`);
    console.log(`    le texte s'enroule sur plusieurs lignes : ${g.enroule ? 'OUI' : 'non'}`);
    console.log(`    exemple        « ${g.texte} »`);
    console.log('  · au clavier     un groupe de boutons radio natifs se parcourt AUX FLÈCHES,');
    console.log('                   compte pour UN seul arrêt de tabulation, et est annoncé');
    console.log('                   comme « choix 2 sur 4 ». C\'est ce que le <select> offre');
    console.log('                   aussi, et ce que les <button> des QCM autonomes n\'offrent');
    console.log('                   PAS. Ce gabarit-ci garde donc la sémantique du <select>');
    console.log('                   tout en occupant le flux au lieu de le recouvrir.');
  }
}

/* ── 4. Le gabarit des QCM autonomes ────────────────────────────────────────── */
console.log('\n═══ 4. LE GABARIT DES QCM AUTONOMES — le modèle vers lequel on irait ═══');
if (!gabaritBoutons) {
  console.log('  Non relevé : aucun QCM autonome n\'a pu être parcouru.');
} else {
  const g = gabaritBoutons;
  console.log(`  Relevé sur ${g.rel}`);
  console.log(`  · conteneur      ${g.conteneur}`);
  console.log(`    role="${g.roleConteneur}"  aria-label="${g.ariaConteneur}"`);
  console.log(`    disposition     ${g.dispositionConteneur}`);
  console.log(`  · une proposition ${g.option}`);
  console.log(`    role            ${g.roleOption}`);
  console.log(`    tabindex        ${g.tabindex}`);
  console.log(`    disposition     ${g.dispositionOption}`);
  console.log(`    le texte s'enroule sur plusieurs lignes : ${g.enroule ? 'OUI' : 'non'}`);
  console.log(`    contenu         ${g.interieur}`);
  console.log('  · au clavier      chaque proposition est un <button> natif : on y arrive à la');
  console.log('                    touche Tab, on la choisit par Entrée ou Espace. Il n\'y a NI');
  console.log('                    role="radiogroup", NI navigation aux flèches : les propositions');
  console.log('                    ne sont donc pas annoncées comme un ensemble de choix exclusifs,');
  console.log('                    et il faut autant de Tab que de propositions pour les passer.');
  console.log('                    C\'est le point à reprendre si l\'on adopte ce gabarit.');
  console.log('  · comportement    les propositions occupent le FLUX : elles poussent le contenu');
  console.log('                    vers le bas et ne recouvrent jamais l\'énoncé. C\'est la');
  console.log('                    différence de fond avec la liste native.');
}

/* ── 5. Le coût de conversion, chiffré sur le lot témoin ────────────────────── */
console.log('\n═══ 5. LE COÛT DE CONVERSION D\'UNE SÉQUENCE TYPE ═══');
if (!temoin) {
  console.log('  Le lot témoin 3e_C1.1 n\'est pas dans le périmètre balayé.');
} else {
  const t = temoin;
  console.log(`  Mesuré sur ${t.rel} (${(t.octets / 1024).toFixed(0)} ko)`);
  console.log(`  · ${t.questions} question(s) à convertir dans ce seul fichier.`);
  console.log(`  · SAUVEGARDE — ${t.sauvegardeGenerique ? 'générique' : 'NOMINATIVE'} : `
    + `${t.lignesSauvegarde} ligne(s) \`querySelectorAll("select,…")\`.`);
  console.log(`    ${t.sauvegardeGenerique
    ? 'Elle balaie les <select> d\'un coup ; il faut lui apprendre à lire un état de'
    : 'Chaque champ y est nommé : le coût est proportionnel au nombre de questions.'}`);
  if (t.sauvegardeGenerique) console.log('    bouton (un attribut, pas un `.value`). Coût : une ligne, une fois par fichier.');
  console.log(`  · VÉRIFICATION — ${t.accesseurVal} accesseur \`val(id)\`, appelé ${t.appelsVal} fois `
    + `· ${t.lectureValeurDirecte} lecture(s) \`.value\` en tout.`);
  console.log('    Tout passe par cet accesseur unique : le convertir suffit à convertir la');
  console.log('    vérification entière. Coût : une fonction, une fois par fichier.');
  console.log(`  · IMPRESSION — la feuille énumère ${t.idsEnumeresImpression} identifiant(s) `
    + `À LA MAIN (ligne ${t.ligneImpression}).`);
  console.log('    C\'est le poste le plus coûteux : cette liste est écrite à la main, fichier par');
  console.log('    fichier, et devra être réécrite en entier à chaque conversion.');
  console.log(`  · CSS — ${t.cssSelect} règle(s) visant \`select\` ou \`.assoc option\` à remplacer.`);
  console.log(`  · TABLE DES RÉPONSES — ${t.entreesTable} entrée(s) « identifiant: "texte" », `
    + `comparées ${t.comparaisonParTexte ? 'PAR LE TEXTE de la proposition' : 'autrement'}.`);
  if (t.comparaisonParTexte) {
    console.log('    C\'est le chiffre qui décide de tout : les bonnes réponses sont comparées au');
    console.log('    TEXTE de l\'option, jamais à un indice. Si le nouveau champ sait rendre ce même');
    console.log('    texte, AUCUNE de ces entrées n\'est à réécrire — ni les contrôles par');
    console.log('    expression régulière qui les accompagnent.');
  }
  if (!t.bancs.length) {
    console.log('  · BANC — aucun fichier de banc trouvé à côté de la séquence.');
  } else {
    for (const b of t.bancs) {
      console.log(`  · BANC ${b.nom} (${b.lignes} lignes)`);
      console.log(`    ${b.poseValeur} écriture(s) \`.value =\` · ${b.litValeur} lecture(s) \`.value\``
        + ` · ${b.selectOption} \`select_option\` · ${b.nommeSelect} mention(s) du mot « select »`);
      console.log(`    ${b.poseValeur ? 'Le banc pose les réponses par `.value` : ce sont CES écritures-là'
        : 'Le banc ne pose aucune valeur : rien à y reprendre de ce côté'}`);
      if (b.poseValeur) console.log('    qu\'il faut convertir, et elles sont peu nombreuses car génériques.');
    }
  }
}

/* ── 6. La géométrie, brièvement ────────────────────────────────────────────── */
console.log('\n═══ 6. RÉSULTAT NÉGATIF — la position du champ ne prédit rien ═══');
console.log('     Hypothèse de départ : un champ situé dans le tiers bas de la fenêtre y ouvre');
console.log('     sa liste vers le haut, donc par-dessus l\'énoncé. Mesurée aux deux tailles,');
console.log('     l\'énoncé calé en haut de la zone utile. Voici le compte.');
let geoTotal = 0;
for (const t of TAILLES) {
  const s = seq.reduce((a, r) => a + (r.geo[t.nom] || 0), 0);
  const b = qcm.reduce((a, r) => a + (r.geo[t.nom] || 0), 0);
  geoTotal += s;
  console.log(`  ${t.nom} (${t.quoi}) — séquences : ${s} / ${nSeq} (${pct(s, nSeq)})`
    + ` · QCM autonomes : ${b} / ${nQcm} (${pct(b, nQcm)})`);
}
console.log('');
console.log(`  LE CRITÈRE EST ABANDONNÉ : ${geoTotal} question(s) sur ${nSeq}, les deux tailles`);
console.log('  réunies. Si la position dans la fenêtre expliquait le défaut, le constat de');
console.log('  classe serait introuvable — or il a bien eu lieu. La liste native se dessine');
console.log('  par-dessus la page QUELLE QUE SOIT la position du champ, dès qu\'elle est trop');
console.log('  haute pour tenir sous lui ; sa hauteur tient au NOMBRE de propositions et à la');
console.log('  LONGUEUR de leur texte, jamais à la mise en page ni à l\'écran.');
console.log('  Conséquence : aucune règle du dépôt ne peut être fondée sur cette géométrie.');

/* ── Synthèse ──────────────────────────────────────────────────────────────── */
console.log('\n═══ SYNTHÈSE ═══');
console.log(`  1. ${nSeq} question(s) à liste déroulante dans ${seq.length} séquence(s) — `
  + `${somme(seq, 0)} dépassent 60 caractères (${pct(somme(seq, 0), nSeq)}), `
  + `${somme(seq, 1)} dépassent 90, ${somme(seq, 2)} dépassent 120.`);
console.log(`  2. Le gabarit n'est PAS uniforme : ${Object.keys(totauxFam).length} formes de rattachement `
  + `énoncé → champ coexistent — ${Object.entries(totauxFam).sort((a, b) => b[1] - a[1])
      .map(([k, v]) => `${k} ${v}`).join(' · ')}.`);
console.log(`     Sur ces ${toutesQuestions.length}, ${auDessusTotal} sont CONCERNÉES (énoncé au-dessus du champ) ;`);
console.log(`     les ${enLigneTotal} champs en ligne à aria-label ne le sont pas — rien à recouvrir,`);
console.log('     et à tenir hors de toute conversion.');
console.log(`  3. Le risque tient à la FORME — ni à la taille d'écran, ni à la position du champ`);
console.log(`     (critère abandonné, section 6) : les propositions d'un QCM autonome s'enroulent`);
console.log(`     et poussent — ${somme(qcm, 0)} y dépassent 60 caractères sans gêner personne —`);
console.log('     tandis que celles d\'une liste native se dessinent par-dessus l\'énoncé.');

if (illisibles.length) {
  console.log(`\n⚠ ${illisibles.length} fichier(s) illisible(s) :`);
  for (const i of illisibles) console.log(`  ${i.rel} — ${i.erreur}`);
}

if (veutCsv) {
  const entete = 'fichier;forme;theme;niveau;questions;sup60;sup90;sup120;non_colles;'
    + TAILLES.map((t) => 'tiers_bas_' + t.nom.replace('×', 'x')).join(';');
  const lignes = parFichier.map((r) => [r.rel, r.forme, r.theme, r.niveau, r.questions,
    ...r.seuils, r.nonColles, ...TAILLES.map((t) => r.geo[t.nom] || 0)].join(';'));
  const dest = path.join(ICI, 'audit_lisibilite_qcm.csv');
  fs.writeFileSync(dest, [entete, ...lignes].join('\n') + '\n', 'utf-8');
  console.log(`\nCSV écrit : ${path.relative(DEPOT, dest).replace(/\\/g, '/')}`);
}

console.log('\n✅ mesure terminée — cet audit ne refuse rien, il rapporte.');
process.exit(0);
