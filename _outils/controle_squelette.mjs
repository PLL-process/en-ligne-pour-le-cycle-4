/**
 * controle_squelette.mjs — règle d'or n°306, « la clé de voûte » :
 * L'ARCHITECTURE D'UNE SÉQUENCE SE VÉRIFIE DANS CE QUE VOIT L'ÉLÈVE.
 *
 * LE CONSTAT
 * ----------
 * Le 21/09/2026, Pascal essaie `3e_C1.1` en classe : dès la séance 1, sous l'activité 1,
 * s'affichent le Bonus, le Bilan et « Je me positionne » sur C1.3-C1.4 — pas encore
 * travaillés. L'ordre DANS LE FICHIER était juste, et tous nos contrôles étaient verts :
 * ils lisaient la source, l'élève lit l'écran. Les blocs de clôture étaient écrits après
 * la fermeture des panneaux de séance, donc visibles à tous les onglets. Corrigé en #418.
 *
 * LA RÈGLE — un squelette unique, qui réunit les n°301, 302 et 304
 *   OUVERTURE, visible dès le premier écran : 🔄 Avant de commencer → situation →
 *     problématique → hypothèse de départ → référentiel « Je serai capable de… » →
 *     billet d'entrée.
 *   SÉANCES : chacune porte ses activités.
 *   CLÔTURE, visible SEULEMENT à la dernière séance : Bonus → Bilan (retour à
 *     l'hypothèse, métacognition, « Je me positionne ») → renvoi au QCM. La
 *     métacognition PEUT s'intituler « Comment j'ai travaillé » ; elle n'y est pas obligée.
 *   Page à onglets : la clôture est dans le dernier panneau de séance (ou un onglet final
 *   dédié), jamais hors des panneaux. On ne se positionne pas avant d'avoir travaillé.
 *
 * CE QUI EST MESURÉ — dans Chromium, onglet par onglet
 * ----------------------------------------------------
 * Chaque bloc est reconnu par sa FONCTION, pas par un libellé exact (leçon des n°301 et
 * 304 : quatre comptes par libellé se sont trompés dans ce dépôt) :
 *   · Bonus : un titre h2/h3 « bonus » qui OUVRE son bloc (le h4 « 💡 Bonus » posé au
 *     milieu d'un exercice de 3e_C1.5 n'en est pas un — il a trompé audit_cloture) ;
 *   · positionnement : un groupe de choix (≥ 3 options) dont l'intitulé porte un code du
 *     référentiel, ou un titre « Je me positionne / auto-positionnement / je me situe » ;
 *   · Bilan : un titre « bilan » ;
 *   · métacognition : une FONCTION, pas un titre (correction du 22/09/2026) — dans le
 *     bilan, une question sur la démarche de l'élève : ce qui l'a surpris, où il a hésité
 *     ou failli se tromper, ce qui lui a coûté un effort, l'aide qu'il a prise, ce qu'il
 *     referait autrement, ce qu'il doit encore revoir. Adressée à lui (« as-tu hésité ? »)
 *     ou dite par lui (« je dois encore revoir ____ »). Le titre « Comment j'ai travaillé »
 *     est un signe parmi d'autres. Exclus : le retour à l'hypothèse, les questions de
 *     contenu, les options d'une échelle de positionnement ;
 *   · renvoi au QCM : un lien vers une page qcm du dossier, ou « Prêt·e à t'entraîner ».
 * Pour chaque état (page ouverte, puis chaque onglet cliqué) : quels blocs sont VISIBLES,
 * et à quelle hauteur. Méthode b, confrontée : le panneau DOM qui contient chaque bloc.
 *
 * DÉFAUTS (chacun refuse la séquence)
 *   D1  un bloc de clôture est visible à une séance qui n'est pas la dernière ;
 *   D2  un bloc de clôture n'est pas visible à la dernière séance ;
 *   D3  à l'écran de clôture, l'ordre n'est pas Bonus → Bilan → QCM ;
 *   D4  un bloc d'ouverture présent n'est pas visible au premier écran ;
 *   D5  page à onglets : un élément visible — titre, paragraphe, champ, bouton — est placé
 *       APRÈS la barre d'onglets et n'est contenu dans AUCUN panneau (22/09/2026). Il se
 *       montre donc à toutes les séances. Jugé par le CONTENEUR, jamais par le titre : D1-D3
 *       reconnaissent la clôture à ses titres, et une « Autoévaluation », une « Synthèse »
 *       ou une séance 1 dont le panneau se ferme trop tôt (4e_C1.4, balises déséquilibrées)
 *       leur échappaient — sixième confusion étiquette / fonction dans ce dépôt.
 *       Exceptions, par conteneur, et rien d'autre :
 *         · #tachesBandeau, section#taches — le tableau de bord des tâches (n°30) : il
 *           SITUE l'élève dans la séquence, il est fait pour être vu à chaque séance ;
 *         · .seance-avis — l'avis « ce bloc est hors parcours », qui accompagne l'onglet ;
 *         · footer — le pied de page (crédits, licence), qui n'est pas du contenu de séance.
 *       Rapport : par page, les titres de ce qui fuit (à défaut, le premier texte).
 * SIGNALÉ, non refusé (« à rédiger », pour la révision) : Bonus sans champ ou sans
 * corrigé, bilan sans retour à l'hypothèse, sans métacognition, sans
 * positionnement ; ordre des blocs d'ouverture différent du squelette.
 *
 * CE QUE CE CONTRÔLE NE VOIT PAS
 *   · une séquence ÉCLATÉE en plusieurs pages (la station 3e_C9.2 : quatre fichiers liés) :
 *     chaque page est jugée seule, comme une page sans onglet ;
 *   · un bloc écrit sous un titre qui ne dit pas sa fonction et sans groupe de choix codé ;
 *   · la QUALITÉ d'un corrigé, la pertinence d'un positionnement ;
 *   · ce qu'un script affiche seulement après un geste (une activité validée).
 *
 * Usage : node _outils/controle_squelette.mjs [--json] [chemin]
 * Sortie : 0 aucune séquence refusée · 1 au moins une · 2 rien vérifié (en panne).
 */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
export const DEPOT = path.dirname(ICI);
const MOTIF = /^sequence(?:[_-].*)?\.html$/i;

export function sequences(depart) {
  const abs = path.resolve(depart);
  if (!fs.statSync(abs).isDirectory()) return [abs];
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const c = path.join(d, e.name);
      if (e.isDirectory()) { if (!e.name.startsWith('.') && e.name !== '_archive-anciennes-versions' && e.name !== 'node_modules' && e.name !== '_outils') marcher(c); }
      else if (MOTIF.test(e.name)) out.push(c);
    }
  })(abs);
  return out.sort();
}

/** Relevé, dans la page, de chaque bloc des deux familles. Exécuté dans le navigateur. */
function releverBlocs() {
  const vis = (e) => !!e && (e.offsetParent !== null || e.getClientRects().length > 0) && getComputedStyle(e).visibility !== 'hidden';
  const y = (e) => Math.round(e.getBoundingClientRect().top + scrollY);
  const conteneur = (e) => e.closest('section, article, .card, details, .activite') || e.parentElement;
  const premierTitre = (h) => { const c = conteneur(h); return c && c.querySelector('h1,h2,h3,h4,summary') === h; };
  const titres = [...document.querySelectorAll('h1, h2, h3, h4')];
  const texte = (e) => (e.textContent || '').replace(/\s+/g, ' ').trim();
  const panneau = (e) => { const p = e.closest('.seance-panel, [role="tabpanel"]'); return p ? (p.id || '(panneau sans id)') : null; };
  const blocs = [];
  const ajouter = (famille, type, el) => { if (el) blocs.push({ famille, type, el }); };

  // ── clôture ──
  // un h2 « Bonus » est toujours le Bonus ; un h3, seulement s'il ouvre son bloc. Exiger
  // « ouvre son bloc » du h2 aussi manquait le Bonus de book-train, posé à même le panneau.
  titres.filter((h) => /\bbonus\b/i.test(texte(h)) && (/^h2$/i.test(h.tagName) || (/^h3$/i.test(h.tagName) && premierTitre(h)))).forEach((h) => ajouter('cloture', 'Bonus', h));
  titres.filter((h) => /\bbilan\b/i.test(texte(h)) && !/billet/i.test(texte(h))).forEach((h) => ajouter('cloture', 'Bilan', h));
  titres.filter((h) => /comment j.ai travaill/i.test(texte(h))).forEach((h) => ajouter('cloture', 'Comment j\'ai travaillé', h));
  titres.filter((h) => /je me positionne|auto[-\s]?positionnement|je me situe/i.test(texte(h))).forEach((h) => ajouter('cloture', 'Je me positionne', h));
  const CODE = /\b(?:[345]e_)?C\d{1,2}\.\d{1,2}\b/;
  for (const g of document.querySelectorAll('fieldset, select')) {
    const opts = g.tagName === 'FIELDSET' ? g.querySelectorAll('input[type=radio]').length : g.querySelectorAll('option').length;
    let intitule = g.tagName === 'FIELDSET' ? texte(g.querySelector('legend') || document.createElement('i'))
      : (g.getAttribute('aria-label') || (g.id && texte(document.querySelector(`label[for="${g.id}"]`) || document.createElement('i'))) || '');
    // Deux écritures du positionnement, reconnues à leur fonction :
    //  · l'intitulé a pour SUJET un code, et les options forment une échelle (leçon de la n°301) ;
    //  · sans code : le groupe dit « je me positionne », ou au moins trois options SONT une
    //    échelle (« Je sais… », « Je ne sais pas encore… », 🔴🟠🟢⭐). Exiger le code manquait
    //    les bilans personnels des C7/C8 (« — je me positionne — » suivi de quatre « Je sais… »).
    const options = g.tagName === 'FIELDSET' ? [...g.querySelectorAll('label, .qcm-option')].map(texte) : [...g.querySelectorAll('option')].map(texte);
    const echelle = options.filter((o) => /^(?:[🔴🟠🟢⭐]|je sais|je ne sais|je lis|je suis capable|ma[iî]trise|pas encore)/iu.test(o)).length;
    if (opts >= 3 && ((CODE.test(intitule.slice(0, 40)) && /ma[iî]trise|je sais|pas encore|🔴|🟠|🟢|⭐|acquis/i.test(texte(g)))
      || /je me positionne|je me situe/i.test(texte(g)) || echelle >= 3)) ajouter('cloture', 'Je me positionne', g);
  }
  const lienQcm = [...document.querySelectorAll('a[href]')].filter((a) => /(^|\/)qcm[_-][^/]*\.html/i.test(a.getAttribute('href')) && !/^https?:/i.test(a.getAttribute('href')));
  titres.filter((h) => /prêt·?e? à t.entraîner/i.test(texte(h))).forEach((h) => ajouter('cloture', 'QCM', h));
  lienQcm.filter((a) => !a.closest('nav, #navharm, .toolbar, header')).forEach((a) => ajouter('cloture', 'QCM', a));

  // ── ouverture ──
  ajouter('ouverture', '🔄 Avant de commencer', document.querySelector('.rappel-spiralaire')
    || titres.find((h) => /[\u{1F504}\u{1F501}]/u.test(texte(h)) && /avant de commencer|déjà|d.où tu viens/i.test(texte(h))));
  ajouter('ouverture', 'situation', titres.find((h) => /situation/i.test(texte(h)) && !/transfert/i.test(texte(h))));
  ajouter('ouverture', 'problématique', titres.find((h) => /problématique/i.test(texte(h))));
  ajouter('ouverture', 'hypothèse', titres.find((h) => /hypothèse/i.test(texte(h)) && !/bilan/i.test(texte(h))) || [...document.querySelectorAll('label, legend, summary')].find((h) => /hypothèse de départ/i.test(texte(h))));
  ajouter('ouverture', 'référentiel', titres.find((h) => /référentiel|je serai capable|ce que dit le programme/i.test(texte(h))));
  ajouter('ouverture', 'billet d\'entrée', titres.find((h) => /billet d.entrée|passeport/i.test(texte(h))));

  // ── « à rédiger » : ce que contient la clôture ──
  const bonusH = blocs.find((b) => b.type === 'Bonus');
  const bonusC = bonusH && conteneur(bonusH.el);
  const bilanH = blocs.find((b) => b.type === 'Bilan') || blocs.find((b) => b.type === 'Je me positionne');
  const bilanC = bilanH && (bilanH.el.closest('section, article, .card') || conteneur(bilanH.el));
  // ── La MÉTACOGNITION, reconnue à sa fonction ──
  // Une question du bilan, adressée à l'élève, qui porte sur SA DÉMARCHE : ce qui l'a
  // surpris, où il a hésité ou failli se tromper, ce qui lui a coûté un effort, l'aide qu'il a
  // prise, ce qu'il referait autrement. Le titre « Comment j'ai travaillé » en est un signe
  // parmi d'autres, pas la condition : l'exiger comptait 54 bilans « sans métacognition »,
  // dont 4e_C1.1, qui demande « Quel chiffre t'a le plus surpris, et pourquoi ? ».
  // Exclus : le retour à l'hypothèse (compté à part), les questions de contenu, et les
  // options d'une échelle de positionnement (elles décrivent un niveau, elles ne questionnent pas).
  const DEMARCHE = /surpris|étonn|hésit|failli|difficile|difficulté|effort|bloqu|coincé|t.en es-tu sorti|t.y es-tu pris|aide as-tu|quelle aide|t.a aidé|t.a servi|autrement|recommen[cç]|referais|changerais|commencerais|trompé|ton erreur|tes erreurs|piège|chang\S* (?:mon |ton |d.)avis|ta méthode|ta démarche|ta façon de (?:travailler|chercher|réfléchir|raisonner|procéder|t.y prendre|faire)|stratégie|prochaine fois|retiens pour|encore revoir|n.arrive pas encore|t.a appris que/i;
  // l'élève parle de lui (« je dois encore revoir », « m'a surpris ») ou on lui parle (« as-tu hésité ? »)
  const A_TOI = /\b(?:tu|te|toi|ton|ta|tes|je|me|moi|mon|mes)\b|\b[tjm]['’]|-tu\b/i;
  const metacognition = [];
  if (bilanC) {
    for (const e of bilanC.querySelectorAll('label, legend, h3, h4, p, li, summary')) {
      if (e.closest('fieldset.qcm-groupe, select, .qcm-option, option')) continue;
      const t = texte(e);
      if (t.length < 12 || t.length > 320 || /hypothèse/i.test(t)) continue;
      if (DEMARCHE.test(t) && A_TOI.test(t) && (/\?/.test(t) || e.tagName === 'LABEL' || /_{3,}|:\s*$/.test(t))) metacognition.push(t.slice(0, 110));
    }
  }
  const metaTitre = blocs.some((b) => b.type === 'Comment j\'ai travaillé');
  const contenu = {
    bonus: !!bonusH,
    bonusChamps: !!bonusC && bonusC.querySelectorAll('textarea, input:not([type=button]):not([type=submit]), select').length > 0,
    bonusCorrige: !!bonusC && [...bonusC.querySelectorAll('details, summary, .corrige-bonus, .correction')].some((d) => /corrig|correction/i.test(texte(d).slice(0, 80)) || d.matches('.corrige-bonus, .correction')),
    bilan: !!bilanH,
    retourHypothese: !!bilanC && (/hypothèse/i.test(texte(bilanC)) || !!bilanC.querySelector('#rappelHyp, [id*="Hyp"], [id*="hyp"]')),
    metacognition: metaTitre || metacognition.length > 0,
    metaTitre,
    metaQuestions: [...new Set(metacognition)].slice(0, 4),
    positionnement: blocs.some((b) => b.type === 'Je me positionne'),
    qcm: blocs.some((b) => b.type === 'QCM'),
  };
  const pv = [...document.querySelectorAll('.seance-panel, [role="tabpanel"]')].find((x) => vis(x));
  // ── D5 : ce qui, après la barre d'onglets, n'est dans aucun panneau ──
  // Jugé par le conteneur. Les exceptions sont listées dans l'en-tête, et nulle part ailleurs.
  const EXCEPTIONS = '#tachesBandeau, section#taches, .seance-avis, footer';
  const onglet1 = document.querySelector('button.seance-tab, [role="tab"]:not(a), button[data-panel]');
  const barre = onglet1 && (onglet1.closest('.seance-tabs, [role="tablist"], #seances') || onglet1.parentElement);
  const fuites = [];
  if (barre) {
    for (const e of document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, input, textarea, select, button')) {
      if (!(barre.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) || barre.contains(e)) continue;
      if (e.closest('.seance-panel, [role="tabpanel"]') || e.closest(EXCEPTIONS)) continue;
      if (e.matches('input[type=hidden]') || !vis(e)) continue;
      if (!/^(INPUT|TEXTAREA|SELECT)$/.test(e.tagName) && !texte(e)) continue;
      fuites.push({ titre: /^H\d$/.test(e.tagName), txt: texte(e).slice(0, 60) || `${e.tagName.toLowerCase()}${e.id ? '#' + e.id : ''}` });
    }
  }
  return {
    fuites: { n: fuites.length, titres: [...new Set(fuites.filter((f) => f.titre).map((f) => f.txt))], premier: fuites.length ? fuites[0].txt : null },
    panneauVisible: pv ? (pv.id || '(sans id)') : null,
    blocs: blocs.map((b) => ({ famille: b.famille, type: b.type, visible: vis(b.el), y: vis(b.el) ? y(b.el) : null, panneau: panneau(b.el) })),
    contenu,
  };
}

const RANG = { Bonus: 0, Bilan: 1, 'Comment j\'ai travaillé': 1, 'Je me positionne': 1, QCM: 2 };
const ORDRE_OUV = ['🔄 Avant de commencer', 'situation', 'problématique', 'hypothèse', 'référentiel', 'billet d\'entrée'];

/** Juge une séquence ouverte dans `ctx`. Exporté pour le banc. */
export async function juger(ctx, fichier) {
  const p = await ctx.newPage();
  const erreurs = [];
  p.on('pageerror', (e) => erreurs.push(String(e.message).slice(0, 100)));
  p.on('dialog', (d) => d.dismiss().catch(() => {}));
  await p.goto(pathToFileURL(fichier).href, { waitUntil: 'load', timeout: 30000 });
  await p.evaluate(() => { try { localStorage.clear(); } catch {} });
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(120);
  const onglets = await p.$$eval('button.seance-tab, [role="tab"]:not(a), button[data-panel]', (l) => [...new Set(l)].map((t, i) => ({
    i, libelle: (t.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40), hors: t.classList.contains('hors') || /hors parcours/i.test(t.textContent || '') })));
  const initial = await p.evaluate(releverBlocs);
  const etats = [];
  if (onglets.length) {
    const handles = await p.$$('button.seance-tab, [role="tab"]:not(a), button[data-panel]');
    const vus = new Set();
    for (let i = 0; i < handles.length; i++) {
      const h = handles[i];
      const id = await h.evaluate((t) => t.outerHTML.slice(0, 120));
      if (vus.has(id)) continue; vus.add(id);
      try { await h.click({ timeout: 2000 }); } catch { continue; }
      await p.waitForTimeout(80);
      etats.push({ onglet: onglets[i], releve: await p.evaluate(releverBlocs) });
    }
  }
  await p.close();

  const defauts = [], signales = [], methodeB = [];
  const cl = (r) => r.blocs.filter((b) => b.famille === 'cloture');
  const types = (l) => [...new Set(l.map((b) => b.type))];
  if (etats.length) {
    const seances = etats.filter((e) => !e.onglet.hors);
    const derniere = seances[seances.length - 1];
    for (const e of etats) {
      if (e === derniere) continue;
      const visibles = cl(e.releve).filter((b) => b.visible);
      if (visibles.length) defauts.push({ code: 'D1', dit: `onglet « ${e.onglet.libelle} » : ${types(visibles).join(', ')} déjà visible(s)` });
    }
    if (derniere) {
      const absents = cl(derniere.releve).filter((b) => !b.visible);
      if (absents.length) defauts.push({ code: 'D2', dit: `dernière séance « ${derniere.onglet.libelle} » : ${types(absents).join(', ')} invisible(s)` });
      const ordre = cl(derniere.releve).filter((b) => b.visible).sort((a, b) => a.y - b.y);
      const faute = ordre.find((b, i) => i && RANG[b.type] < RANG[ordre[i - 1].type]);
      if (faute) defauts.push({ code: 'D3', dit: `ordre à l'écran : ${types(ordre).join(' → ')}` });
      // méthode b : où le DOM range chaque bloc
      const panneaux = new Set(cl(derniere.releve).map((b) => b.panneau));
      const horsPanneau = cl(derniere.releve).filter((b) => b.panneau === null);
      methodeB.push(horsPanneau.length ? `hors panneau : ${types(horsPanneau).join(', ')}` : `dans le(s) panneau(x) ${[...panneaux].join(', ')}`);
    }
    // l'ouverture, au premier écran
    const ouvCachee = initial.blocs.filter((b) => b.famille === 'ouverture' && !b.visible);
    if (ouvCachee.length) defauts.push({ code: 'D4', dit: `ouverture absente du premier écran : ${types(ouvCachee).join(', ')}` });
    // D5 : visible hors de tout panneau, dans l'un au moins des états (page ouverte, chaque onglet)
    const tous = [initial, ...etats.map((e) => e.releve)].map((r) => r.fuites).filter((f) => f.n);
    if (tous.length) {
      const pire = tous.reduce((a, b) => (b.n > a.n ? b : a));
      const titres = [...new Set(tous.flatMap((f) => f.titres))];
      defauts.push({ code: 'D5', dit: `${pire.n} élément(s) visibles hors de tout panneau — ${titres.length ? titres.slice(0, 8).map((t) => `« ${t} »`).join(', ') + (titres.length > 8 ? ` (+${titres.length - 8})` : '') : `sans titre : « ${pire.premier} »`}` });
    }
  } else {
    const ordre = cl(initial).filter((b) => b.visible).sort((a, b) => a.y - b.y);
    const faute = ordre.find((b, i) => i && RANG[b.type] < RANG[ordre[i - 1].type]);
    if (faute) defauts.push({ code: 'D3', dit: `ordre à l'écran : ${types(ordre).join(' → ')}` });
    const ouvCachee = initial.blocs.filter((b) => b.famille === 'ouverture' && !b.visible);
    if (ouvCachee.length) defauts.push({ code: 'D4', dit: `ouverture invisible au chargement : ${types(ouvCachee).join(', ')}` });
    methodeB.push('sans onglets');
  }
  const ouv = initial.blocs.filter((b) => b.famille === 'ouverture' && b.visible).sort((a, b) => a.y - b.y).map((b) => b.type);
  const attendu = ORDRE_OUV.filter((t) => ouv.includes(t));
  if (ouv.join('|') !== attendu.join('|')) signales.push(`ouverture dans l'ordre ${ouv.join(' → ')}`);
  const c = initial.contenu;
  const aRediger = [];
  if (!c.bonus) aRediger.push('Bonus absent');
  else { if (!c.bonusChamps) aRediger.push('Bonus sans champ'); if (!c.bonusCorrige) aRediger.push('Bonus sans corrigé'); }
  if (!c.bilan && !c.positionnement) aRediger.push('bilan absent');
  else { if (!c.retourHypothese) aRediger.push('bilan sans retour à l\'hypothèse'); if (!c.metacognition) aRediger.push('pas de métacognition'); if (!c.positionnement) aRediger.push('pas de positionnement'); }
  if (!c.qcm) aRediger.push('pas de renvoi au QCM');
  const derniereS = etats.filter((e) => !e.onglet.hors).pop();
  const meta = { titre: c.metaTitre, questions: c.metaQuestions };
  return { meta, onglets: onglets.length, panneauDernier: derniereS ? derniereS.releve.panneauVisible : null, derniere: etats.length ? (etats.filter((e) => !e.onglet.hors).pop()?.onglet.libelle || '') : '', defauts, signales, aRediger, methodeB: methodeB.join(' ; '), erreurs };
}

export async function main(argv = []) {
  const json = argv.includes('--json');
  const cible = argv.find((a) => !a.startsWith('--'));
  let liste;
  try { liste = sequences(cible || DEPOT); }
  catch (e) { console.error(`⛔ EN PANNE : impossible de parcourir ${cible || DEPOT} — ${String(e).slice(0, 90)}\n     Rien n'a été vérifié. Ce n'est pas un succès.`); return 2; }
  if (!liste.length) { console.error(`⛔ EN PANNE : aucune séquence sous ${cible || DEPOT} (sequence_*.html, sequence-*.html, sequence.html).\n     Rien n'a été vérifié. Ce n'est pas un succès.`); return 2; }
  const nav = await chromium.launch();
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const rapports = [];
  for (const f of liste) {
    const rel = path.relative(DEPOT, f).split(path.sep).join('/');
    try { rapports.push({ rel, ...(await juger(ctx, f)) }); }
    catch (e) { rapports.push({ rel, panne: String(e).slice(0, 100), defauts: [{ code: 'P', dit: 'page illisible dans le navigateur' }], signales: [], aRediger: [] }); }
  }
  await nav.close();
  if (!rapports.some((r) => !r.panne)) { console.error(`⛔ EN PANNE : ${liste.length} séquence(s), aucune ouverte dans le navigateur.`); return 2; }
  const refusees = rapports.filter((r) => r.defauts.length);
  if (json) { console.log(JSON.stringify(rapports, null, 1)); return refusees.length ? 1 : 0; }
  const aOnglets = rapports.filter((r) => r.onglets).length;
  console.log(`${rapports.length} séquence(s) ouvertes onglet par onglet · ${aOnglets} à onglets · ${rapports.length - aOnglets} sans · ${refusees.length} refusée(s)`);
  for (const code of ['D1', 'D2', 'D3', 'D4', 'D5']) {
    const n = rapports.filter((r) => r.defauts.some((d) => d.code === code)).length;
    console.log(`     ${code} ${{ D1: 'clôture visible avant la dernière séance', D2: 'clôture invisible à la dernière séance', D3: 'ordre de clôture à l\'écran', D4: 'ouverture absente du premier écran', D5: 'visible hors de tout panneau de séance' }[code]} : ${n}`);
  }
  for (const r of refusees) {
    console.log(`\n  ✘ ${r.rel}`);
    for (const d of r.defauts) console.log(`     ${d.code} ${d.dit}`);
    if (r.methodeB) console.log(`     (DOM : ${r.methodeB})`);
  }
  console.log(`\n     NON VU : une séquence éclatée en plusieurs pages (chaque page jugée seule) ; un bloc`
    + `\n     dont le titre ne dit pas la fonction ; la qualité d'un corrigé ; ce qu'un geste affiche.`);
  if (refusees.length) return 1;
  console.log('\n✅ chaque séquence montre son ouverture au premier écran et sa clôture à la dernière séance, dans l\'ordre');
  return 0;
}

export function lanceDirectement(url, argv1) { return !!argv1 && path.resolve(fileURLToPath(url)) === path.resolve(argv1); }
if (lanceDirectement(import.meta.url, process.argv[1])) process.exit(await main(process.argv.slice(2)));
