/* tests_banc_python.mjs — le banc du petit Python de la page (banc_python.js), sans navigateur.
 *
 * Il éprouve ce qui fonde la règle d'or n°333 (une réussite affichée prouve la production réelle : on compare le comportement, pas le texte) : deux écritures
 * équivalentes donnent les mêmes sorties, un opérateur faux change la sortie à sa frontière, et chaque erreur de
 * Python arrive avec sa ligne. Les critères de recette de l'audit du 21/11/2026 (3e_C6.1) y sont recopiés :
 *   · « Remplacer seulement les guillemets doubles des chaînes par des apostrophes » : même comportement ;
 *   · « Remplacer seulement le test strict du seuil supérieur par un test inclusif » : à 118, le niveau et le
 *     gyrophare changent.
 * Usage : node _outils/banc_python/tests_banc_python.mjs — sortie 0 si tout passe, 1 sinon.
 */
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const ctx = {}; vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(ICI, 'banc_python.js'), 'utf8'), ctx);
const B = ctx.BancPython;

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });

const V2 = `# Station d'alerte cyclonique — programme d'alerte v2
SEUIL_ORANGE = 60
SEUIL_ROUGE = 90
SEUIL_OURAGAN = 118

vent_kmh = lire_capteur("anemometre")
pression_hpa = lire_capteur("barometre")

vigilance = "verte"
sirene_active = False
gyrophare_actif = False

if vent_kmh > SEUIL_OURAGAN:
    vigilance = "violette"
    sirene_active = True
    gyrophare_actif = True
elif vent_kmh > SEUIL_ROUGE:
    vigilance = "rouge"
    sirene_active = True
elif vent_kmh > SEUIL_ORANGE:
    vigilance = "orange"
    gyrophare_actif = True

message = "Vigilance " + vigilance
envoyer(message)
if sirene_active:
    activer_sirene()
if gyrophare_actif:
    activer_gyrophare()`;

function station(code, vent) {
  const s = { sirene: false, gyro: false };
  const r = B.executer(code, {
    fonctions: {
      lire_capteur: a => a[0] === 'anemometre' ? vent : 1013,
      envoyer: () => null,
      activer_sirene: () => { s.sirene = true; },
      activer_gyrophare: () => { s.gyro = true; },
    },
    arites: { lire_capteur: 1, envoyer: 1, activer_sirene: 0, activer_gyrophare: 0 },
  });
  return { r, msg: r.sorties.appels.filter(a => a.nom === 'envoyer').map(a => a.args[0]).join('|'), ...s };
}
const resume = o => o.r.ok ? `${o.msg} · sirène ${o.sirene ? 'oui' : 'non'} · gyro ${o.gyro ? 'oui' : 'non'}` : B.phraseErreur(o.r.erreur);

// 1 · la v2 de la correction, aux dix vents du banc
const attendu = v => { const n = v > 118 ? 'violette' : v > 90 ? 'rouge' : v > 60 ? 'orange' : 'verte';
  return `"Vigilance ${n}" · sirène ${v > 90 ? 'oui' : 'non'} · gyro ${(n === 'orange' || n === 'violette') ? 'oui' : 'non'}`; };
const DIX = [55, 59, 60, 61, 89, 90, 91, 117, 118, 119];
const faux = DIX.filter(v => resume(station(V2, v)) !== attendu(v));
ok('1 · la version 2 donne les sorties du cahier des charges aux dix vents', faux.length === 0, faux.map(v => v + ' → ' + resume(station(V2, v))).join(' ; '));

// 2 · critère de recette de l'audit : apostrophes au lieu de guillemets → mêmes sorties
const apos = V2.replace(/"/g, "'");
ok('2 · apostrophes au lieu de guillemets : mêmes sorties aux dix vents (critère de l\'audit)',
   DIX.every(v => resume(station(apos, v)) === resume(station(V2, v))));

// 3 · critère de recette : >= au seuil supérieur → à 118 le niveau et le gyrophare changent
const large = V2.replace('vent_kmh > SEUIL_OURAGAN', 'vent_kmh >= SEUIL_OURAGAN');
const a118 = station(large, 118);
ok('3 · `>=` au seuil ouragan : à 118, violette et gyrophare actif (critère de l\'audit)',
   a118.msg === '"Vigilance violette"' && a118.gyro && DIX.filter(v => v !== 118).every(v => resume(station(large, v)) === attendu(v)), resume(a118));

// 4 · la trace dit le chemin : à 118, premier test faux, deuxième vrai
const tr = station(V2, 118).r.trace.filter(p => p.t === 'test' && p.n < 25).map(p => B.phraseTrace(p));
ok('4 · trace à 118 : « 118 > 118 → faux », puis « 118 > 90 → vrai »',
   tr.length === 2 && /118 > 118 → faux/.test(tr[0]) && /118 > 90 → vrai/.test(tr[1]), tr.join(' / '));

// 5 · oubli de l'initialisation : NameError à la ligne du if final, pour un vent faible seulement
const sansInit = V2.replace('gyrophare_actif = False\n', '');
const e55 = station(sansInit, 55).r, e61 = station(sansInit, 61).r;
ok('5 · sans « gyrophare_actif = False » : NameError à 55 km/h (ligne du if final), rien à 61 km/h',
   !e55.ok && e55.erreur.type === 'NameError' && e55.erreur.ligne === 27 && e61.ok, B.phraseErreur(e55.erreur));

// 6 · indentation manquante
const ind = V2.replace('if gyrophare_actif:\n    activer_gyrophare()', 'if gyrophare_actif:\nactiver_gyrophare()');
const e6 = B.analyser(ind);
ok('6 · « activer_gyrophare() » sans ses 4 espaces : IndentationError, ligne 29', !e6.ok && e6.erreur.type === 'IndentationError' && e6.erreur.ligne === 29, B.phraseErreur(e6.erreur));

// 7 · indentation en trop
const e7 = B.analyser('x = 1\n    y = 2');
ok('7 · une ligne décalée sans if : IndentationError « unexpected indent »', !e7.ok && /unexpected indent/.test(e7.erreur.message));

// 8 · deux-points manquants, = au lieu de ==, else if
ok('8 · « if x > 1 » sans deux-points : SyntaxError expected \':\'', /expected ':'/.test(B.analyser('x = 2\nif x > 1\n    y = 1').erreur.message));
ok('8 bis · « if x = 1: » : SyntaxError qui propose ==', /==/.test(B.analyser('x = 2\nif x = 1:\n    y = 1').erreur.conseil));
ok('8 ter · « else if » : le conseil dit elif', /elif/.test(B.analyser('x = 2\nif x > 1:\n    y = 1\nelse if x > 0:\n    y = 2').erreur.conseil));

// 9 · types : texte + nombre, comparaison texte / nombre
const e9 = B.executer('a = "Vigilance " + 3');
ok('9 · "texte" + 3 : TypeError « can only concatenate str »', !e9.ok && /concatenate/.test(e9.erreur.message));
const e9b = B.executer('v = "95"\nif v > 90:\n    a = 1');
ok('9 bis · "95" > 90 : TypeError, et le conseil parle de float(…)', !e9b.ok && /float/.test(e9b.erreur.conseil));

// 10 · décimaux et input : le programme du Bonus
const r10 = B.executer('h = float(input("hauteur ? "))\nd = "vert"\nif h > 4:\n    d = "rouge"\nprint("Baignade :", d)', { entrees: ['4.0'] });
ok('10 · float(input()) avec « 4.0 » : 4.0 > 4 est faux, print affiche « Baignade : vert »', r10.ok && r10.sorties.affichages[0] === 'Baignade : vert', JSON.stringify(r10.sorties.affichages));

const r10b = B.executer('h = float(input())', { entrees: ['4,0'] });
ok('10 bis · float(« 4,0 ») : ValueError comme en Python, et le conseil dit d\'écrire 4.0', !r10b.ok && r10b.erreur.type === 'ValueError' && /4\.0/.test(r10b.erreur.conseil), B.phraseErreur(r10b.erreur));

// 11 · comparaisons enchaînées, and/or/not, elif/else
const r11 = B.executer('x = 3\nif 2 < x <= 3 and not x == 4:\n    r = "oui"\nelse:\n    r = "non"');
ok('11 · 2 < x <= 3 and not x == 4 : vrai', r11.ok && r11.variables.r === 'oui');

// 12 · ce que le banc ne sait pas faire, il le dit
const r12 = B.analyser('while True:\n    x = 1');
ok('12 · while : refus nommé « le banc de la page ne sait pas encore exécuter »', !r12.ok && r12.erreur.type === 'NonPrisEnCharge' && /UN passage/.test(r12.erreur.conseil));

// 13 · une fonction inconnue, une fonction mal appelée
const r13 = B.executer('activer_sirène()', { fonctions: { activer_sirene: () => null }, arites: { activer_sirene: 0 } });
ok('13 · fonction mal orthographiée : NameError qui liste les fonctions de la station', !r13.ok && r13.erreur.type === 'NameError' && /activer_sirene/.test(r13.erreur.conseil));
const r13b = B.executer('activer_sirene(1)', { fonctions: { activer_sirene: () => null }, arites: { activer_sirene: 0 } });
ok('13 bis · activer_sirene(1) : TypeError sur le nombre d\'arguments', !r13b.ok && r13b.erreur.type === 'TypeError');

// 14 · commentaires, lignes vides, # dans un texte
const r14 = B.executer('# titre\n\nm = "a # b"   # fin\n');
ok('14 · un # dans un texte n\'est pas un commentaire', r14.ok && r14.variables.m === 'a # b');

// 15 · empreinte : deux textes différents → deux versions
ok('15 · empreinte : la moindre modification change la version', B.empreinte(V2) !== B.empreinte(large) && B.empreinte(V2) === B.empreinte(V2));

// 16 · entiers et décimaux s'affichent comme en Python
const r16 = B.executer('print(4.0, 7 / 2, 7 // 2, 10 / 5)');
ok('16 · print(4.0, 7 / 2, 7 // 2, 10 / 5) → « 4.0 3.5 3 2.0 »', r16.ok && r16.sorties.affichages[0] === '4.0 3.5 3 2.0', r16.sorties.affichages[0]);

// 17 · écritures Python justes que le banc lit (audit Fable du 22/11/2026) : f-string, is, expression conditionnelle, « ; », in
const r17 = B.executer('v = "rouge"\nm = f"Vigilance {v}"\na = True\nb = 1 if a is True else 0; c = "ou" in "rouge"\nd = None\ne = d is None and "x" not in m');
ok('17 · f"…{v}", is True, a if c else b, « ; », in, not in, is None : lus comme Python', r17.ok && r17.variables.m === 'Vigilance rouge' && r17.variables.b === 1 && r17.variables.c === true && r17.variables.e === true, r17.ok ? JSON.stringify(r17.variables) : B.phraseErreur(r17.erreur));

// 18 · ce que le banc ne lit pas n'est JAMAIS une SyntaxError : « limite du banc, pas forcément une erreur »
const nonLus = ['x = [1, 2]', 'f = lambda y: y', 'd = {"a": 1}', 'for i in range(3):\n    pass', 'm = f"{3.14159:.2f}"', 'b = b"ab"', 'if True: x = 1; y = 2'];
const mal = nonLus.map(c => [c, B.executer(c)]).filter(([c, r]) => r.ok || r.erreur.type !== 'NonPrisEnCharge' || !/limite du banc, pas forcément une erreur/.test(B.phraseErreur(r.erreur)));
ok('18 · listes, lambda, { }, for, f-string formatée, b"…", « ; » après if : refus nommés « limite du banc », jamais « SyntaxError »', mal.length === 0, mal.map(([c, r]) => c + ' → ' + (r.ok ? 'ok ?' : B.phraseErreur(r.erreur))).join(' | '));

// 19 · une vraie erreur reste une vraie erreur
const r19 = B.executer('if 3 > 2\n    x = 1');
const r19b = B.executer('x = 1 if True');
ok('19 · « if 3 > 2 » sans deux-points et « 1 if True » sans else restent des SyntaxError', !r19.ok && r19.erreur.type === 'SyntaxError' && !r19b.ok && r19b.erreur.type === 'SyntaxError');

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d && !t.ok ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
process.exit(n === T.length ? 0 : 1);
