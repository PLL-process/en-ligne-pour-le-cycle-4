// Banc générique du mode mission — joue TOUTE séquence qui porte le bloc, écran par écran, à 390 px.
//   node _outils/mode_mission/banc_generique.mjs <sequence.html> [...]      (sans argument : toutes les pages qui portent le bloc)
//   --detail : liste chaque écran
// Pour chaque page : entrer en mission, parcourir chaque séance par « Suivant », répondre juste à chaque écran qui se
// vérifie (les réponses sont lues dans la page, comme le fait le mode), puis revenir à la page complète.
// Refus (sortie 1) : erreur JavaScript, écran vide, défilement de côté, écran qui ne s'accepte pas avec les bonnes
// réponses, bouton de vérification de la page laissé visible dans un écran de question, écran suivant qui ne se
// montre pas depuis son début, page complète non rétablie.
// Signalé sans refus : les réponses attendues qu'aucun écran ne vérifie (elles restent vérifiées par la page).
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const args = process.argv.slice(2), detail = args.includes('--detail');
let pages = args.filter(a => !a.startsWith('--')).map(a => path.resolve(a));
if (!pages.length) {
  const voir = d => fs.readdirSync(d, { withFileTypes: true }).flatMap(e => e.name.startsWith('.') || e.name === 'node_modules' || e.name.startsWith('_archive') ? [] :
    e.isDirectory() ? voir(path.join(d, e.name)) : /^sequence[-_].*\.html$/.test(e.name) ? [path.join(d, e.name)] : []);
  pages = fs.readdirSync(RACINE).filter(n => n.startsWith('theme-')).flatMap(t => voir(path.join(RACINE, t)))
    .filter(f => fs.readFileSync(f, 'utf-8').includes('<!-- mode-mission v1 : début'));
}

const b = await chromium.launch();
let refusTotal = 0;
for (const PAGE of pages) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } }); const p = await ctx.newPage();
  const err = []; p.on('pageerror', e => err.push(e.message));
  const refus = [], notes = [], ecransVus = [];
  await p.goto(pathToFileURL(PAGE).href, { waitUntil: 'load' }); await p.waitForTimeout(350);
  if (!(await p.$('#btnMission'))) { console.log(`❌ ${path.relative(RACINE, PAGE)}\n   · le bouton du mode mission n'apparaît pas (gabarit non reconnu, ou bloc absent)`); refusTotal++; await ctx.close(); continue; }

  // les séances : des panneaux ouverts par des onglets (gabarit commun, Book Train), ou des blocs à la suite dans une
  // page sans onglets — là, c'est le mode qui n'en montre qu'un (`.ms-ici`). Le banc reconnaît le gabarit lui-même.
  const GAB = await p.evaluate(() => document.querySelector('.seance-panel') ? { P: '.seance-panel', T: '.seance-tab', A: 'active', de: 'data-panel' }
    : document.querySelector('section.panneau[role=tabpanel]') ? { P: 'section.panneau[role=tabpanel]', T: '[role=tablist] [role=tab][aria-controls]', A: 'actif', de: 'aria-controls' }
    : { P: '.seance-bloc[id]', T: null, A: 'ms-ici', de: null });
  const ACTIF = `${GAB.P}.${GAB.A}`, CHECK = 'button[data-check], button.verif[data-exo]', MESSAGE = '.feedback, .resultat[id^="res-"]';
  // les réponses que le mode retient, groupe par groupe (la prise `_mission` du bloc)
  const cles = await p.evaluate(GAB => { const M = document.documentElement._mission, o = {};
    document.querySelectorAll(GAB.P).forEach(P => P.querySelectorAll('fieldset.qcm-groupe[id], select[id]:not([data-interface])').forEach(f => { const c = M.cle(f); if (c !== undefined) o[f.id] = c; })); return o; }, GAB);
  // ce que la page cache d'elle-même, séance par séance : la référence pour le retour à la page complète
  const caches = () => p.evaluate(([GAB, ACTIF, CHECK]) => { const o = {};
    const compte = P => [...P.querySelectorAll('.consigne, .exo, fieldset.qcm-groupe, ' + CHECK)].filter(x => !x.offsetParent && !x.closest('details:not([open])')).length;
    if (!GAB.T) { document.querySelectorAll(GAB.P).forEach(P => { o[P.id] = compte(P); }); return o; }
    const onglets = [...document.querySelectorAll(GAB.T)], ouvert = document.querySelector(ACTIF), premier = onglets.find(t => ouvert && t.getAttribute(GAB.de) === ouvert.id) || onglets[0];
    onglets.forEach(t => { t.click(); const P = document.querySelector(ACTIF); o[P.id] = compte(P); });
    premier.click(); return o; }, [GAB, ACTIF, CHECK]);
  const avant = await caches();
  await p.click('#btnMission'); await p.waitForTimeout(250);
  const onglets = await p.evaluate(GAB => GAB.T ? [...document.querySelectorAll(GAB.T)].map(t => t.getAttribute(GAB.de)) : [...document.querySelectorAll(GAB.P)].map(P => P.id), GAB);
  let nEcrans = 0, nVerifies = 0, nEtq = 0, nEcrits = 0, nPage = 0;
  for (const id of onglets) {
    if (GAB.T) await p.evaluate(([GAB, i]) => [...document.querySelectorAll(GAB.T)].find(t => t.getAttribute(GAB.de) === i).click(), [GAB, id]);
    else if (await p.evaluate(([ACTIF, i]) => (document.querySelector(ACTIF) || {}).id !== i, [ACTIF, id])) await p.click('#msSuiv');      // sans onglets : « Séance suivante → » y mène
    await p.waitForTimeout(220);
    if (await p.evaluate(([ACTIF, i]) => (document.querySelector(ACTIF) || {}).id !== i, [ACTIF, id])) { refus.push(`${id} : la séance ne s'ouvre pas`); continue; }
    await p.evaluate(() => { const b = document.querySelector('#msRail [data-k="0"]'); if (b) b.click(); }); await p.waitForTimeout(120);
    for (let garde = 0; garde < 140; garde++) {
      const e = await p.evaluate(([cles, ACTIF, CHECK]) => {
        const P = document.querySelector(ACTIF), vu = x => !!x.offsetParent;
        const rail = [...document.querySelectorAll('#msRail [data-k]')], k = rail.findIndex(x => x.getAttribute('aria-current'));
        const verif = !document.getElementById('msVerif').hidden, exo = verif || !document.getElementById('msVide').hidden;
        const champs = [...P.querySelectorAll('fieldset.qcm-groupe, select[id]:not([data-interface])')].filter(f => vu(f) && !f.classList.contains('ms-origine'));
        const texte = [...P.children].filter(vu).map(c => c.innerText).join(' ').replace(/\s+/g, ' ').trim();
        return { k, n: rail.length, titre: document.getElementById('msOu').childNodes[0].textContent, verif, exo,
          etq: [...P.querySelectorAll('.ms-etq')].filter(vu).length, avecCle: champs.filter(f => cles[f.id] !== undefined && !f.classList.contains('positionnement')).map(f => f.id),
          sansCle: champs.filter(f => cles[f.id] === undefined && !f.classList.contains('positionnement')).map(f => f.id),
          mots: texte ? texte.split(' ').length : 0, medias: [...P.querySelectorAll('img,svg,canvas,video,iframe,textarea,input,select')].filter(vu).length,
          large: document.documentElement.scrollWidth > innerWidth + 1,
          checks: [...P.querySelectorAll(CHECK)].filter(vu).length, suiv: !document.getElementById('msSuiv').hidden,
          ecran: document.documentElement._mission.ecran() };
      }, [cles, ACTIF, CHECK]);
      nEcrans++; const ou = `${id} · écran ${e.k + 1}/${e.n} « ${e.titre.slice(0, 50)} »`;
      if (e.mots < 2 && !e.medias) refus.push(`${ou} : écran vide`);
      if (e.large) refus.push(`${ou} : défilement de côté à 390 px`);
      if (e.exo && e.checks) refus.push(`${ou} : le bouton de vérification de la page est visible dans un écran de question`);
      let issue = '';
      if (e.verif && (e.etq || e.avecCle.length)) {
        // répondre juste, comme un élève qui sait : étiquettes posées une à une, boutons radio cochés
        await p.evaluate(([cles, ACTIF]) => {
          const P = document.querySelector(ACTIF), vu = x => !!x.offsetParent;
          [...P.querySelectorAll('.ms-etq')].filter(vu).forEach(comp => { comp._sets.forEach((f, i) => { const but = cles[f.id]; if (but === undefined) return;
            const lab = [...comp.querySelectorAll('.ms-lab')].find(l => l.textContent === but); if (!lab) return; lab.click(); comp.querySelector(`.ms-case[data-i="${i}"]`).click(); }); });
          [...P.querySelectorAll('fieldset.qcm-groupe, select[id]:not([data-interface])')].filter(f => vu(f) && !f.classList.contains('ms-origine') && cles[f.id] !== undefined && !f.classList.contains('positionnement'))
            .forEach(f => { if (f.tagName === 'SELECT') { f.value = cles[f.id]; f.dispatchEvent(new Event('input', { bubbles: true })); f.dispatchEvent(new Event('change', { bubbles: true })); return; }
              const r = [...f.querySelectorAll('input[type=radio]')].find(x => x.value === cles[f.id]); if (r) r.click(); });
        }, [cles, ACTIF]);
        await p.click('#msVerif'); await p.waitForTimeout(140);
        const r = await p.evaluate(() => { const x = [...document.querySelectorAll('.ms-retour')].find(e => e.offsetParent); return { ok: !!x && x.classList.contains('ok'), texte: x ? x.textContent.slice(0, 90) : '(aucun message)' }; });
        if (r.ok) { nVerifies++; if (e.etq) nEtq++; issue = '✓'; } else { refus.push(`${ou} : les bonnes réponses ne sont pas acceptées — ${r.texte}`); issue = '✗'; await p.waitForTimeout(2100); }
      } else if (e.exo) { nEcrits++; issue = e.verif ? 'vérif. de la page' : 'écrit'; if (e.verif) { await p.click('#msVerif'); await p.waitForTimeout(140); } }
      // à la dernière question d'une zone, c'est la vérification de la page qui parle : son message doit se voir ici
      if (e.verif && e.ecran && e.ecran.dernier && e.ecran.check) {
        const fb = await p.evaluate(([ACTIF, MESSAGE]) => { const P = document.querySelector(ACTIF); return [...P.querySelectorAll(MESSAGE)].filter(x => x.offsetParent && x.textContent.trim()).length; }, [ACTIF, MESSAGE]);
        if (fb) nPage++; else refus.push(`${ou} : dernière question de la zone, mais le message de la vérification de la page ne s'affiche pas`);
        const ko = await p.evaluate(ACTIF => [...document.querySelectorAll(ACTIF + ' .ms-juste')].filter(f => f.classList.contains('ko') || f.classList.contains('faux')).map(f => f.id), ACTIF);
        if (ko.length) refus.push(`${ou} : la page marque fausse une réponse que le mode a acceptée — ${ko.join(', ')}`);
      }
      if (detail) ecransVus.push(`     ${ou} ${e.etq ? '[étiquettes] ' : ''}${e.avecCle.length ? '[' + e.avecCle.length + ' choix] ' : ''}${e.sansCle.length ? '[' + e.sansCle.length + ' sans réponse lue] ' : ''}${issue}`);
      if (e.k >= e.n - 1) break;
      await p.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));          // l'élève a lu l'écran jusqu'en bas
      await p.click('#msSuiv'); await p.waitForTimeout(130);
      const haut = await p.evaluate(ACTIF => Math.round(document.querySelector(ACTIF).getBoundingClientRect().top), ACTIF);
      if (haut < 0 && !refus.some(m => m.includes('depuis son début'))) refus.push(`${ou} : après « Suivant », l'écran suivant n'est pas montré depuis son début (son haut est à ${haut} px)`);
    }
  }
  // ce que le mode n'a vérifié sur aucun écran (la page, elle, le vérifie toujours)
  const hors = await p.evaluate(([cles, GAB]) => Object.keys(cles).filter(id => { const f = document.getElementById(id); return f && f.matches('fieldset.qcm-groupe') && !f.classList.contains('positionnement') && f.closest(GAB.P) && !f.classList.contains('ms-juste'); }), [cles, GAB]);
  if (hors.length) notes.push(`${hors.length} réponse(s) attendue(s) hors des écrans vérifiés (cartes hors activité, Bonus…) : ${hors.slice(0, 8).join(', ')}${hors.length > 8 ? '…' : ''}`);
  await p.click('#msQuitter'); await p.waitForTimeout(200);
  // chaque réponse retenue par le mode doit valoir un point, et un seul, à la vérification de la page
  const croise = await p.evaluate(cles => {
    if (typeof CHECKS === 'undefined') return { sans: true };
    const total = () => Object.keys(CHECKS).reduce((a, n) => { try { return a + (Number(CHECKS[n]().score) || 0); } catch (e) { return a; } }, 0), faux = [];
    Object.keys(cles).forEach(id => { const f = document.getElementById(id); if (!f.classList.contains('ms-juste')) return;
      const lire = () => f.tagName === 'SELECT' ? f.value : (f.querySelector('input[type=radio]:checked') || {}).value || '';
      const mettre = v => { if (f.tagName === 'SELECT') f.value = v || ''; else f.querySelectorAll('input[type=radio]').forEach(r => { r.checked = !!v && r.value === v; }); };
      const garde = lire(); mettre(''); const s0 = total(); mettre(cles[id]); const s1 = total();
      if (s1 !== s0 + 1) faux.push(`${id} (${s0} → ${s1})`); mettre(garde); });
    return { n: Object.keys(cles).filter(id => document.getElementById(id).classList.contains('ms-juste')).length, faux };
  }, cles);
  // le pourquoi des erreurs : jamais sur la bonne réponse ; et combien de mauvaises réponses en ont un
  const pq = await p.evaluate(cles => { let surBonne = [], total = 0, avec = 0;
    Object.keys(cles).forEach(id => { const f = document.getElementById(id), ind = f.hasAttribute('data-indice');
      f.querySelectorAll('input[type=radio]').forEach(r => { if (r.value === cles[id]) { if (r.hasAttribute('data-pourquoi')) surBonne.push(id); return; }
        if (f.classList.contains('qcm-grille')) return; total++; if (ind || r.hasAttribute('data-pourquoi')) avec++; });
      if (f.classList.contains('qcm-grille')) { total++; if (ind) avec++; } });
    return { surBonne, total, avec }; }, cles);
  if (pq.surBonne.length) refus.push(`un « pourquoi » est posé sur la bonne réponse : ${pq.surBonne.join(', ')}`);
  if (pq.avec) notes.push(`pourquoi des erreurs : ${pq.avec} / ${pq.total} (mauvaises propositions et lignes de grille)`);
  if (croise.sans) notes.push('pas de table CHECKS visible : croisement fait sur les marques « ok / ko » que la page pose à sa vérification');
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
