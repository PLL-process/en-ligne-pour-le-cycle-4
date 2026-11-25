/* banc-eleve v1 : début — source unique : _outils/banc_eleve/banc_eleve.js, posée par poser.py ; ne pas la modifier dans la page */
/* ── banc-eleve (règle d'or n°333, 25/11/2026) : le programme de l'élève est jugé en l'EXÉCUTANT ──────────────────
   Après chaque ▶ Exécuter d'un éditeur nommé dans BANC_ELEVE, la page rejoue le programme sur des entrées choisies
   — sous, sur et au-dessus de chaque seuil (n°351) —, en remplaçant la ligne « nom = … » par la valeur d'essai
   (modèle : 5e_C9.1, avecPlaces), et compare ce qu'il affiche au cahier des charges. Le verdict est gardé avec
   l'empreinte du programme : une frappe qui le change le périme (« à rejouer ») et retire la validation.
   Une limite de l'outil n'est jamais une faute de l'élève : une erreur de Python se dit avec son nom et sa ligne. */
const BE_ARRETE = "⏹ arrêté par le banc";   /* un programme qui ne finit pas : jamais confondu avec une sortie */
function beEmpreinte(t){ let h = 5381; t = String(t || ""); for(let i = 0; i < t.length; i++) h = ((h * 33) ^ t.charCodeAt(i)) >>> 0; return ("0000000" + h.toString(16)).slice(-8); }
function beAvec(code, vals){
  const l = String(code).split("\n");
  Object.keys(vals || {}).forEach(nom => {
    const re = new RegExp("^" + nom + "\\s*=(?!=)"), i = l.findIndex(x => re.test(x));
    if(i >= 0) l[i] = nom + " = " + vals[nom]; else l.unshift(nom + " = " + vals[nom]);
  });
  return l.join("\n");
}
function beCode(bloc){ const t = document.querySelector("#" + bloc + " textarea.editeur-py-code"); return t ? t.value : ""; }
function beLigne(bloc){
  let p = document.getElementById(bloc + "-banc");
  if(!p){
    const b = document.getElementById(bloc); if(!b) return null;
    p = document.createElement("p"); p.id = bloc + "-banc"; p.className = "banc-eleve"; p.setAttribute("aria-live", "polite");
    b.insertAdjacentElement("afterend", p);
  }
  return p;
}
function beJuger(bloc, code){
  const B = BANC_ELEVE[bloc];
  return Promise.all(B.essais.map(e => window.EditeurPython.executer(beAvec(code, e.vals),
      {simulation: e.simulation || B.simulation, limiteActive: 1500, limiteTotale: 3000})
    .then(r => r, err => ({sortie: "", erreur: {titre: "Panne", explication: String(err)}, arret: null}))))
  .then(rs => {
    let n = 0, ecart = null;
    rs.forEach((r, k) => {
      const e = B.essais[k], obtenu = r.erreur ? null : r.arret ? BE_ARRETE : B.lire(r.sortie || "", e);
      if(obtenu === e.attendu) n++; else if(!ecart) ecart = {e, r, obtenu};
    });
    return {n, total: B.essais.length, ecart};
  });
}
/* les espaces insécables : « T = 28 °C » et « 30 < 30 » ne se coupent pas en fin de ligne, « : » ne commence pas une ligne */
function beInsecables(t){
  return t.replace(/ ([=<>!]=?) /g, "\u00a0$1\u00a0").replace(/ (°C|%|h)(?=[\s.,;)]|$)/g, "\u00a0$1")
          .replace(/ ([:;!?»])/g, "\u00a0$1").replace(/« /g, "«\u00a0");
}
function bePhrase(bloc, v){ return beInsecables(bePhraseBrute(bloc, v)); }
function bePhraseBrute(bloc, v){
  const B = BANC_ELEVE[bloc];
  if(v.n === v.total) return "✔ Banc d'essai : " + v.n + " / " + v.total + " essais conformes.\n" + B.resume;
  const e = v.ecart.e, r = v.ecart.r, o = v.ecart.obtenu;
  let obt;
  if(r.erreur) obt = "une erreur" + (r.erreur.titre ? " — " + r.erreur.titre + (r.erreur.ligne ? ", ligne " + r.erreur.ligne : "") : "") +
                     ". Lis l'explication dans la console.";
  else if(o === BE_ARRETE) obt = "le programme ne s'arrête pas : le banc a dû l'arrêter.";
  else if(o === "rien") obt = (B.rien || "rien d'affiché") + ".";
  else obt = B.dire(o) + ".";
  return "✘ Banc d'essai : " + v.n + " / " + v.total + " essais conformes.\nPremier écart — " + e.libelle + ".\n" +
         "Attendu : " + B.dire(e.attendu) + (e.pourquoi ? " (" + e.pourquoi + ")" : "") + ".\nObtenu : " + obt;
}
function beOk(bloc){ const x = window.__exp || {}; return !!x[bloc] && x[bloc + "_emp"] === beEmpreinte(beCode(bloc)); }
function beMsg(bloc){
  const x = window.__exp || {};
  if(x[bloc + "_emp"] && x[bloc + "_emp"] !== beEmpreinte(beCode(bloc)))
    return "↻ À rejouer : ton programme a changé depuis le dernier essai. Clique ▶ Exécuter : la page l'essaie de nouveau.";
  if(x[bloc + "_verdict"] && !x[bloc]) return x[bloc + "_verdict"].replace(/\n/g, " ") + " Corrige ton programme, puis ▶ Exécuter.";
  return BANC_ELEVE[bloc].attente;
}
function beAfficher(bloc){
  const x = window.__exp || {}, p = x[bloc + "_verdict"] ? beLigne(bloc) : document.getElementById(bloc + "-banc");
  if(!p) return;
  if(x[bloc + "_emp"] && x[bloc + "_emp"] !== beEmpreinte(beCode(bloc))){
    p.textContent = "↻ À rejouer : ton programme a changé depuis le dernier essai."; p.className = "banc-eleve"; return;
  }
  p.textContent = x[bloc + "_verdict"] || ""; p.className = "banc-eleve " + (x[bloc] ? "ok" : "ko");
}
document.addEventListener("editeur-py:fin", e => {
  const d = e.detail || {}, B = d.bloc && BANC_ELEVE[d.bloc];
  if(!B || !window.EditeurPython) return;
  const code = beCode(d.bloc), p = beLigne(d.bloc);
  if(p){ p.textContent = "⏳ Banc d'essai : la page essaie ton programme…"; p.className = "banc-eleve"; }
  beJuger(d.bloc, code).then(v => {
    const x = window.__exp;
    x[d.bloc] = v.n === v.total; x[d.bloc + "_emp"] = beEmpreinte(code); x[d.bloc + "_verdict"] = bePhrase(d.bloc, v);
    beAfficher(d.bloc); save();
  });
});
document.addEventListener("input", e => {
  const t = e.target;
  if(!t || !t.matches || !t.matches("textarea.editeur-py-code")) return;
  const b = t.closest(".editeur-py"), bloc = b && b.id, B = bloc && BANC_ELEVE[bloc], x = window.__exp || {};
  if(!B || !x[bloc + "_emp"]) return;
  beAfficher(bloc);
  if(B.retirer && x[bloc] && x[bloc + "_emp"] !== beEmpreinte(t.value)) B.retirer();
});
window.addEventListener("load", () => Object.keys(BANC_ELEVE).forEach(beAfficher));
/* banc-eleve v1 : fin */
