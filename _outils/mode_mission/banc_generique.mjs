// Banc générique du mode mission — joue TOUTE séquence qui porte le bloc, écran par écran, à 390 px.
//   node _outils/mode_mission/banc_generique.mjs <sequence.html> [...]      (sans argument : toutes les pages qui portent le bloc)
//   --detail : liste chaque écran
// Pour chaque page : entrer en mission, parcourir chaque séance par « Suivant », répondre juste à chaque écran qui se
// vérifie (les réponses sont lues dans la page, comme le fait le mode), puis revenir à la page complète.
// Refus (sortie 1) : erreur JavaScript, écran vide, défilement de côté, écran qui ne s'accepte pas avec les bonnes
// réponses, bouton de vérification de la page laissé visible dans un écran de question, page complète non rétablie.
// Signalé sans refus : les réponses attendues qu'aucun écran ne vérifie (elles restent vérifiées par la page).
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const args = process.argv.slice(2), detail = args.includes('--detail');
let pages = args.filter(a => !a.startsWith('--')).map(a => path.resolve(a));
if (!pages.length) {
  const voir = d => fs.readdirSync(d, { withFileTypes: true }).flatMap(e => e.name.startsWith('.') || e.name === 'node_modules' || e.name.startsWith('_archive') ? [] :
    e.isDirectory() ? voir(path.join(d, e.name)) : /^sequence_.*\.html$/.test(e.name) ? [path.join(d, e.name)] : []);
  pages = fs.readdirSync(RACINE).filter(n => n.startsWith('theme-')).flatMap(t => voir(path.join(RACINE, t)))
    .filter(f => fs.readFileSync(f, 'utf-8').includes('<!-- mode-mission v1 : début'));
}

const b = await chromium.launch();
let refusTotal = 0;
for (const PAGE of pages) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } }); const p = await ctx.newPage();
  const err = []; p.on('pageerror', e => err.push(e.message));
  const refus = [], notes = [], ecransVus = [];
  await p.goto('file://' + PAGE, { waitUntil: 'load' }); await p.waitForTimeout(350);
  if (!(await p.$('#btnMission'))) { console.log(`❌ ${path.relative(RACINE, PAGE)}\n   · le bouton du mode mission n'apparaît pas (gabarit non reconnu, ou bloc absent)`); refusTotal++; await ctx.close(); continue; }

  // les réponses que le mode retient, groupe par groupe (la prise `_mission` du bloc)
  const cles = await p.evaluate(() => { const M = document.documentElement._mission, o = {};
    document.querySelectorAll('.seance-panel fieldset.qcm-groupe[id]').forEach(f => { const c = M.cle(f); if (c !== undefined) o[f.id] = c; }); return o; });
  // ce que la page cache d'elle-même, séance par séance : la référence pour le retour à la page complète
  const caches = () => p.evaluate(() => { const o = {}, premier = document.querySelector('.seance-tab.active') || document.querySelector('.seance-tab');
    document.querySelectorAll('.seance-tab').forEach(t => { t.click(); const P = document.querySelector('.seance-panel.active');
      o[P.id] = [...P.querySelectorAll('.consigne, .exo, button[data-check], fieldset.qcm-groupe')].filter(x => !x.offsetParent && !x.closest('details:not([open])')).length; });
    premier.click(); return o; });
  const avant = await caches();
  await p.click('#btnMission'); await p.waitForTimeout(250);
  const onglets = await p.evaluate(() => [...document.querySelectorAll('.seance-tab')].map(t => t.dataset.panel));
  let nEcrans = 0, nVerifies = 0, nEtq = 0, nEcrits = 0, nPage = 0;
  for (const id of onglets) {
    await p.evaluate(i => document.querySelector(`.seance-tab[data-panel="${i}"]`).click(), id); await p.waitForTimeout(220);
    await p.evaluate(() => { const b = document.querySelector('#msRail [data-k="0"]'); if (b) b.click(); }); await p.waitForTimeout(120);
    for (let garde = 0; garde < 140; garde++) {
      const e = await p.evaluate(cles => {
        const P = document.querySelector('.seance-panel.active'), vu = x => !!x.offsetParent;
        const rail = [...document.querySelectorAll('#msRail [data-k]')], k = rail.findIndex(x => x.getAttribute('aria-current'));
        const verif = !document.getElementById('msVerif').hidden, exo = verif || !document.getElementById('msVide').hidden;
        const champs = [...P.querySelectorAll('fieldset.qcm-groupe')].filter(f => vu(f) && !f.classList.contains('ms-origine'));
        const texte = [...P.children].filter(vu).map(c => c.innerText).join(' ').replace(/\s+/g, ' ').trim();
        return { k, n: rail.length, titre: document.getElementById('msOu').childNodes[0].textContent, verif, exo,
          etq: [...P.querySelectorAll('.ms-etq')].filter(vu).length, avecCle: champs.filter(f => cles[f.id] !== undefined && !f.classList.contains('positionnement')).map(f => f.id),
          sansCle: champs.filter(f => cles[f.id] === undefined && !f.classList.contains('positionnement')).map(f => f.id),
          mots: texte ? texte.split(' ').length : 0, medias: [...P.querySelectorAll('img,svg,canvas,video,iframe,textarea,input,select')].filter(vu).length,
          large: document.documentElement.scrollWidth > innerWidth + 1,
          checks: [...P.querySelectorAll('button[data-check]')].filter(vu).length, suiv: !document.getElementById('msSuiv').hidden,
          ecran: document.documentElement._mission.ecran() };
      }, cles);
      nEcrans++; const ou = `${id} · écran ${e.k + 1}/${e.n} « ${e.titre.slice(0, 50)} »`;
      if (e.mots < 2 && !e.medias) refus.push(`${ou} : écran vide`);
      if (e.large) refus.push(`${ou} : défilement de côté à 390 px`);
      if (e.exo && e.checks) refus.push(`${ou} : le bouton de vérification de la page est visible dans un écran de question`);
      let issue = '';
      if (e.verif && (e.etq || e.avecCle.length)) {
        // répondre juste, comme un élève qui sait : étiquettes posées une à une, boutons radio cochés
        await p.evaluate(cles => {
          const P = document.querySelector('.seance-panel.active'), vu = x => !!x.offsetParent;
          [...P.querySelectorAll('.ms-etq')].filter(vu).forEach(comp => { comp._sets.forEach((f, i) => { const but = cles[f.id]; if (but === undefined) return;
            const lab = [...comp.querySelectorAll('.ms-lab')].find(l => l.textContent === but); if (!lab) return; lab.click(); comp.querySelector(`.ms-case[data-i="${i}"]`).click(); }); });
          [...P.querySelectorAll('fieldset.qcm-groupe')].filter(f => vu(f) && !f.classList.contains('ms-origine') && cles[f.id] !== undefined && !f.classList.contains('positionnement'))
            .forEach(f => { const r = [...f.querySelectorAll('input[type=radio]')].find(x => x.value === cles[f.id]); if (r) r.click(); });
        }, cles);
        await p.click('#msVerif'); await p.waitForTimeout(140);
        const r = await p.evaluate(() => { const x = [...document.querySelectorAll('.ms-retour')].find(e => e.offsetParent); return { ok: !!x && x.classList.contains('ok'), texte: x ? x.textContent.slice(0, 90) : '(aucun message)' }; });
        if (r.ok) { nVerifies++; if (e.etq) nEtq++; issue = '✓'; } else { refus.push(`${ou} : les bonnes réponses ne sont pas acceptées — ${r.texte}`); issue = '✗'; await p.waitForTimeout(2100); }
      } else if (e.exo) { nEcrits++; issue = e.verif ? 'vérif. de la page' : 'écrit'; if (e.verif) { await p.click('#msVerif'); await p.waitForTimeout(140); } }
      // à la dernière question d'une zone, c'est la vérification de la page qui parle : son message doit se voir ici
      if (e.verif && e.ecran && e.ecran.dernier && e.ecran.check) {
        const fb = await p.evaluate(() => { const P = document.querySelector('.seance-panel.active'); return [...P.querySelectorAll('.feedback')].filter(x => x.offsetParent && x.textContent.trim()).length; });
        if (fb) nPage++; else refus.push(`${ou} : dernière question de la zone, mais le message de la vérification de la page ne s'affiche pas`);
      }
      if (detail) ecransVus.push(`     ${ou} ${e.etq ? '[étiquettes] ' : ''}${e.avecCle.length ? '[' + e.avecCle.length + ' choix] ' : ''}${e.sansCle.length ? '[' + e.sansCle.length + ' sans réponse lue] ' : ''}${issue}`);
      if (e.k >= e.n - 1) break;
      await p.click('#msSuiv'); await p.waitForTimeout(130);
    }
  }
  // ce que le mode n'a vérifié sur aucun écran (la page, elle, le vérifie toujours)
  const hors = await p.evaluate(cles => Object.keys(cles).filter(id => { const f = document.getElementById(id); return f && f.matches('fieldset.qcm-groupe') && !f.classList.contains('positionnement') && f.closest('.seance-panel') && !f.classList.contains('ms-juste'); }), cles);
  if (hors.length) notes.push(`${hors.length} réponse(s) attendue(s) hors des écrans vérifiés (cartes hors activité, Bonus…) : ${hors.slice(0, 8).join(', ')}${hors.length > 8 ? '…' : ''}`);
  await p.click('#msQuitter'); await p.waitForTimeout(200);
  // chaque réponse retenue par le mode doit valoir un point, et un seul, à la vérification de la page
  const croise = await p.evaluate(cles => {
    if (typeof CHECKS === 'undefined') return { sans: true };
    const total = () => Object.keys(CHECKS).reduce((a, n) => { try { return a + (Number(CHECKS[n]().score) || 0); } catch (e) { return a; } }, 0), faux = [];
    Object.keys(cles).forEach(id => { const f = document.getElementById(id), garde = f.value; f.value = null; const s0 = total(); f.value = cles[id]; const s1 = total();
      if (s1 !== s0 + 1) faux.push(`${id} (${s0} → ${s1})`); f.value = garde; });
    return { n: Object.keys(cles).length, faux };
  }, cles);
  if (croise.sans) notes.push('pas de table CHECKS : les réponses retenues ne sont pas croisées avec la vérification de la page');
  else if (croise.faux.length) refus.push(`${croise.faux.length} réponse(s) retenue(s) par le mode ne valent pas un point à la vérification de la page : ${croise.faux.slice(0, 10).join(', ')}`);
  const sortie = await p.evaluate(() => ({ ms: document.body.classList.contains('ms'), seuls: [...document.querySelectorAll('.ms-seul')].filter(x => x.offsetParent).length }));
  const apres = await caches(), restes = Object.keys(apres).filter(id => apres[id] > avant[id]);
  if (sortie.ms || sortie.seuls || restes.length) refus.push(`retour à la page complète : ${JSON.stringify(sortie)} ; blocs restés cachés dans ${restes.join(', ') || 'aucune séance'}`);
  err.slice(0, 3).forEach(m => refus.push('erreur JavaScript : ' + m.slice(0, 140)));

  console.log(`${refus.length ? '❌' : '✅'} ${path.relative(RACINE, PAGE)}\n   ${onglets.length} séance(s) · ${nEcrans} écrans · ${nVerifies} écrans vérifiés par le mode (dont ${nEtq} à étiquettes) · ${nEcrits} écrans écrits ou vérifiés par la page · ${nPage} vérifications de la page déclenchées · ${Object.keys(cles).length} réponses lues${croise.sans ? '' : ', croisées avec la page'}`);
  refus.forEach(m => console.log('   ✘ ' + m)); notes.forEach(m => console.log('   · ' + m)); ecransVus.forEach(m => console.log(m));
  refusTotal += refus.length; await ctx.close();
}
await b.close();
console.log(refusTotal ? `══ ${refusTotal} refus sur ${pages.length} page(s) ══` : `══ mode mission : ${pages.length} page(s) jouées écran par écran, aucun refus ══`);
process.exit(refusTotal ? 1 : 0);
