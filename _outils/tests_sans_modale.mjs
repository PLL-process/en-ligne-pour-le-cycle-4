// tests_sans_modale.mjs — le contrôle en navigateur de la règle d'or n°188.
//
// `sans_modale.py --controle` lit le code : il dit qu'aucune boîte n'est ouverte
// et qu'aucune fonction n'est appelée sans exister. Ce script-ci ouvre vraiment
// les pages et clique vraiment, parce qu'une page peut satisfaire la lecture et
// se casser à l'usage.
//
// Ce qu'il vérifie, page par page :
//   1. la page charge sans erreur JS ;
//   2. `demande` existe et se comporte en deux temps DANS CETTE PAGE ;
//   3. le bandeau parle au premier appel (il est créé s'il n'existait pas) ;
//   4. tout bouton destructeur GARDÉ par `demande` ne détruit rien au premier
//      clic — un bouton jamais gardé est signalé, pas compté en échec ;
//   5. aucune boîte modale ne s'ouvre sur tout le parcours.
//
// Usage : NODE_PATH=… node _outils/tests_sans_modale.mjs <fichier.html> […]

import { chromium } from 'playwright';

const fichiers = process.argv.slice(2);
const b = await chromium.launch();
let echecs = 0, total = 0;

for (const f of fichiers) {
  const nom = f.split('/').pop();
  const p = await b.newPage();
  const err = [], dlg = [];
  p.on('pageerror', e => err.push(e.message));
  p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
  p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });
  const T = [];
  const ok = (n, c, d = '') => { T.push({ n, ok: !!c, d }); total++; if (!c) echecs++; };

  try {
    await p.goto('file://' + f, { waitUntil: 'load' });
    await p.waitForTimeout(350);
    ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));

    // le helper lui-même, dans le contexte réel de la page
    const h = await p.evaluate(() => {
      if (typeof demande !== 'function') return { absent: true };
      const un = demande('_essai', 'Message d’essai');
      const z = document.getElementById('savedNote');
      const vu = z ? z.textContent : '';
      const deux = demande('_essai', 'Message d’essai');
      if (z && z.dataset.cree) z.remove();
      return { un, deux, vu };
    });
    ok('`demande` existe', !h.absent);
    ok('premier appel : ne fait rien', h.un === false, String(h.un));
    ok('premier appel : le bandeau parle', (h.vu || '').includes('seconde fois'), (h.vu || '').slice(0, 60));
    ok('second appel : exécute', h.deux === true, String(h.deux));

    // un seul clic sur un bouton destructeur ne doit rien détruire
    const boutons = await p.$$('button, a[role="button"], input[type="button"]');
    let cliques = 0;
    const nonGardes = [];
    for (const el of boutons) {
      const txt = ((await el.textContent()) || '').trim();
      if (!/Effacer|Réinitialiser|Recommencer|Remise à zéro|Tout effacer/i.test(txt)) continue;
      // on n'exige rien d'un bouton que personne n'a jamais gardé : on regarde
      // si CE clic passe par `demande`, et seulement alors on vérifie qu'il
      // n'a rien détruit. Un bouton non gardé est signalé, pas compté en échec.
      const avant = await p.evaluate(() => {
        window.__vus = [];
        const o = window.demande;
        window.demande = function (c, m) { const r = o(c, m); window.__vus.push(r); return r; };
        return JSON.stringify(Object.entries(localStorage).sort());
      });
      // clic direct : ces boutons vivent souvent sur un écran de bilan qui n'est
      // pas affiché. On veut éprouver le gardien, pas la mise en page.
      await el.evaluate(e => e.click()).catch(() => {});
      await p.waitForTimeout(200);
      const apres = await p.evaluate(() => JSON.stringify(Object.entries(localStorage).sort()));
      const vus = await p.evaluate(() => window.__vus || []);
      if (vus.length) {
        ok(`un clic sur « ${txt.slice(0, 28)} » ne détruit rien`, avant === apres);
        ok(`« ${txt.slice(0, 28)} » : le premier clic ne fait qu'annoncer`, vus[0] === false, String(vus[0]));
        cliques++;
      } else {
        nonGardes.push(txt.slice(0, 34));
      }
      // on referme la fenêtre de six secondes au lieu de l'attendre
      await p.evaluate(() => { try { _demandes = {}; } catch (e) {} });
    }
    ok('au moins un bouton gardé trouvé et éprouvé', cliques > 0,
       cliques ? '' : 'non gardés : ' + (nonGardes.join(', ') || 'aucun bouton trouvé'));
    ok('aucune boîte modale sur tout le parcours', dlg.length === 0, dlg.join(' | '));
  } catch (e) {
    ok('la page se laisse éprouver', false, String(e).slice(0, 120));
  }

  const r = T.filter(t => t.ok).length;
  const mauvais = T.filter(t => !t.ok);
  console.log(`${mauvais.length ? '❌' : '✅'} ${nom.padEnd(56).slice(0, 56)} ${r}/${T.length}`);
  mauvais.forEach(t => console.log(`      ↳ ${t.n}${t.d ? ' — ' + t.d : ''}`));
  await p.close();
}

console.log(`\n${total - echecs} / ${total}`);
await b.close();
process.exit(echecs === 0 ? 0 : 1);
