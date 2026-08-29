# -*- coding: utf-8 -*-
"""Le banc de la publication — on compose un message, et le banc dit ce qu'il révèle.

Une publication ne dit pas seulement ce qu'on a voulu écrire. Elle **révèle** ce
qu'on n'a pas pensé à retirer, et elle **engage** celui qui appuie sur le bouton.
Le banc met les trois colonnes côte à côte :

  · ce que je publie — chaque élément se coche et se DÉCOCHE ;
  · ce qu'un inconnu peut en déduire — et le compte des indices qui mènent
    encore à une personne réelle ;
  · ce que ça engage — droit d'auteur, droit à l'image, donnée personnelle.

Deux distinctions que le banc rend visibles, et qu'aucun cours ne rend évidentes :

1. **une autorisation rend licite, elle ne rend pas anonyme.** Avec l'accord écrit
   de Maël, publier son visage devient légal — et il reste identifiable ;
2. **ce n'est pas un élément qui identifie, c'est leur combinaison.** Retirer le
   visage ne suffit pas si le prénom, le nom du collège et l'heure restent : le
   compteur ne tombe pas à zéro, et il le montre.

Règle d'or n°213 : ce qui fait la découverte, c'est de pouvoir RETIRER un élément
et voir le résultat bouger.
"""

CSS = """
/* ── Banc de la publication — original, CC0 ─────────────────────────────── */
.publi{background:#0a1b3d;border:1px solid var(--border);border-radius:12px;padding:14px;margin:12px 0}
table.elems{width:100%;border-collapse:collapse;font-size:.88em;margin:8px 0}
table.elems th,table.elems td{border:1px solid var(--border);padding:5px 8px;text-align:left}
table.elems th{background:#173666;color:var(--hl)}
table.elems td.ck{width:34px;text-align:center}
table.elems td input[type=checkbox]{width:17px;height:17px;accent-color:#61dafb}
table.elems tr.pris td:not(.ck){color:#fff}
.publi-cmd{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0}
.publi-cmd label{font-size:.9em;color:var(--sub)}
.publi-cmd select{width:auto;min-width:250px}
.compteur{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}
.jauge{flex:1;min-width:190px;background:#132c58;border:1px solid var(--border);border-radius:10px;padding:9px 11px}
.jauge b{display:block;font-size:1.5em;color:var(--hl);font-variant-numeric:tabular-nums}
.jauge span{font-size:.8em;color:var(--sub)}
.jauge.zero b{color:var(--ok)}
.jauge.alerte b{color:var(--err)}
ul.revele{list-style:none;padding:0;margin:8px 0}
ul.revele li{padding:4px 0 4px 24px;position:relative;font-size:.92em}
ul.revele li::before{position:absolute;left:0;font-weight:700}
ul.revele li.vu::before{content:"👁";color:var(--warn)}
ul.revele li.loi::before{content:"⚖";color:var(--err)}
ul.revele li.rien::before{content:"✔";color:var(--ok)}
ul.revele li.rien{color:var(--sub)}
.verdict{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.86em;background:#050f24;border:1px solid var(--border);border-radius:9px;padding:9px 11px;max-height:150px;overflow-y:auto}
.verdict div{padding:1px 0}
.verdict .ok{color:var(--ok)}.verdict .ko{color:var(--err)}.verdict .wa{color:var(--warn)}
table.releve{width:100%;border-collapse:collapse;font-size:.87em;margin:8px 0}
table.releve th,table.releve td{border:1px solid var(--border);padding:6px 8px;text-align:left}
table.releve th{background:#173666;color:var(--hl)}
table.releve td.num{width:32%}
table.releve td input{padding:4px 8px}
.grille{list-style:none;padding:0;margin:8px 0}
.grille li{border-left:3px solid var(--head);background:rgba(198,142,242,.08);padding:7px 12px;border-radius:0 8px 8px 0;margin:6px 0;font-size:.94em}
"""


def html(titre, elements, choix, extra=""):
    """elements : [(id, nom, ce_que_c_est)] ; choix : [(id, label, [options])]"""
    lignes = "\n".join(
        '      <tr id="tr_%s"><td class="ck"><input type="checkbox" id="el_%s"></td>'
        '<td><b>%s</b></td><td>%s</td></tr>' % (i, i, nom, quoi)
        for i, nom, quoi in elements)
    sel = "\n".join(
        '    <div class="publi-cmd"><label for="%s">%s</label>\n'
        '      <select id="%s">\n%s\n      </select></div>'
        % (i, lab, i, "\n".join('        <option>%s</option>' % o for o in opts))
        for i, lab, opts in choix)
    return """
  <div class="publi">
    <p style="font-size:.92em;color:var(--sub);margin:0 0 8px"><b>%s</b></p>

    <table class="elems">
      <tr><th></th><th>Élément</th><th>Ce que c'est</th></tr>
%s
    </table>
%s
    <div class="compteur">
      <div class="jauge" id="jInd"><b id="nInd">0</b><span>indice(s) qui mènent à une personne réelle</span></div>
      <div class="jauge" id="jLoi"><b id="nLoi">0</b><span>règle(s) non respectée(s)</span></div>
    </div>

    <p style="font-size:.9em;color:var(--sub);margin:10px 0 0">Ce qu'un inconnu peut en déduire :</p>
    <ul class="revele" id="revele"></ul>

    <div class="publi-cmd">
      <button class="btn" id="regarder" type="button">🔍 Regarder ce que ça révèle</button>
      <button class="btn" id="publier" type="button">📤 Publier</button>
      <button class="btn" id="vider" type="button">↺ Tout décocher</button>
    </div>
    <div class="verdict" id="verdict"><div>Aucun essai. Compose la publication, puis regarde.</div></div>
%s
  </div>
""" % (titre, lignes, sel, extra)


JS = """
/* ── banc de la publication ─────────────────────────────────────────────── */
/* ELEMENTS : {id, nom, indice, infraction?, leve_par?} */
const ELEMENTS = __ELEMENTS__;
const DEDUCTIONS = __DEDUCTIONS__;   /* {cles:[…], txt} — visible si tout est coché */
const CHOIX = __CHOIX__;             /* {id: {valeur: {infraction?, leve?, note?}}} */
const PUBLIABLE = __PUBLIABLE__;     /* phrase quand la publication est acceptée */

function coches(){
  return ELEMENTS.filter(e => document.getElementById("el_" + e.id).checked);
}
function valeurChoix(id){ const e = document.getElementById(id); return e ? e.value : ""; }

/* Ce qui est levé par un choix (une autorisation, un crédit) : la règle cesse
   d'être enfreinte — et l'indice, lui, reste. Une autorisation rend licite,
   elle ne rend pas anonyme. */
function leves(){
  const s = [];
  for(const id in CHOIX){
    const c = CHOIX[id][valeurChoix(id)];
    if(c && c.leve){ s.push(...c.leve); }
  }
  return s;
}
function infractions(){
  const pris = coches(), l = leves(), out = [];
  pris.forEach(e => {
    if(e.infraction && !l.includes(e.id)) out.push({id:e.id, txt:e.infraction});
  });
  for(const id in CHOIX){
    const c = CHOIX[id][valeurChoix(id)];
    if(c && c.infraction) out.push({id:id, txt:c.infraction});
  }
  return out;
}
function indices(){ return coches().filter(e => e.indice).length; }

/* Un choix non fait n'est pas une faute : c'est une décision qui manque.
   Le banc ne compte donc pas de règle enfreinte tant qu'on n'a rien décidé —
   il refuse simplement de publier, et il dit ce qu'il attend. */
function indecis(){
  const s = [];
  for(const id in CHOIX){
    const v = valeurChoix(id);
    if(v.charAt(0) === "\u2014"){ s.push(CHOIX[id][v] && CHOIX[id][v].manque); }
  }
  return s.filter(Boolean);
}

function majPubli(){
  const pris = coches().map(e => e.id);
  ELEMENTS.forEach(e =>
    document.getElementById("tr_" + e.id).classList.toggle("pris", pris.includes(e.id)));

  const nI = indices(), inf = infractions();
  document.getElementById("nInd").textContent = nI;
  document.getElementById("nLoi").textContent = inf.length;
  document.getElementById("jInd").classList.toggle("zero", nI === 0);
  document.getElementById("jInd").classList.toggle("alerte", nI >= 3);
  document.getElementById("jLoi").classList.toggle("zero", inf.length === 0);
  document.getElementById("jLoi").classList.toggle("alerte", inf.length > 0);

  if(nI === 0) window.__exp.anonyme = true;
  if(inf.length === 0 && !indecis().length && pris.length) window.__exp.legal = true;
  if(pris.length) window.__exp.compose = true;
  save();
}

function regarder(){
  const u = document.getElementById("revele"), pris = coches().map(e => e.id);
  u.innerHTML = "";
  let n = 0;
  DEDUCTIONS.forEach(d => {
    if(d.cles.every(k => pris.includes(k))){
      const li = document.createElement("li");
      li.className = "vu"; li.textContent = d.txt;
      u.appendChild(li); n += 1;
    }
  });
  infractions().forEach(i => {
    const li = document.createElement("li");
    li.className = "loi"; li.textContent = i.txt;
    u.appendChild(li); n += 1;
  });
  for(const id in CHOIX){
    const c = CHOIX[id][valeurChoix(id)];
    if(c && c.note){
      const li = document.createElement("li");
      li.className = "vu"; li.textContent = c.note;
      u.appendChild(li); n += 1;
    }
  }
  if(!n){
    const li = document.createElement("li");
    li.className = "rien";
    li.textContent = "Rien ne permet de remonter à quelqu'un, et aucune règle n'est enfreinte.";
    u.appendChild(li);
  }
  window.__exp.regarde = true;
  save();
}

function ligne(cls, txt){
  const v = document.getElementById("verdict");
  if(v.dataset.vide !== "non"){ v.innerHTML = ""; v.dataset.vide = "non"; }
  const d = document.createElement("div");
  d.className = cls; d.textContent = txt;
  v.appendChild(d); v.scrollTop = v.scrollHeight;
}

document.getElementById("regarder").addEventListener("click", () => {
  regarder();
  ligne("wa", "Relevé fait : " + indices() + " indice(s), " + infractions().length + " règle(s) enfreinte(s).");
});
document.getElementById("publier").addEventListener("click", () => {
  regarder();
  const inf = infractions(), nI = indices();
  const rien = indecis();
  if(!coches().length){
    ligne("ko", "Il n'y a rien à publier : aucun élément n'est coché.");
  } else if(rien.length){
    ligne("wa", "Refusé — " + rien[0]);
    window.__exp.indecis = true;
  } else if(inf.length){
    ligne("ko", "Refusé — " + inf[0].txt + (inf.length > 1 ? " (et " + (inf.length - 1) + " autre(s))" : ""));
    window.__exp.refuse = true;
  } else if(nI > 0){
    ligne("wa", "Publiable, et " + nI + " indice(s) mènent encore à une personne réelle. "
        + "C'est légal, ce n'est pas anodin : demande-toi si c'est nécessaire.");
    window.__exp.publieAvecIndices = true;
  } else {
    ligne("ok", PUBLIABLE);
    window.__exp.publie = true;
  }
  save();
});
document.getElementById("vider").addEventListener("click", () => {
  ELEMENTS.forEach(e => { document.getElementById("el_" + e.id).checked = false; });
  majPubli(); regarder();
  ligne("wa", "Publication vidée.");
});
ELEMENTS.forEach(e =>
  document.getElementById("el_" + e.id).addEventListener("change", () => { majPubli(); regarder(); }));
for(const id in CHOIX){
  const s = document.getElementById(id);
  if(s) s.addEventListener("change", () => { majPubli(); regarder(); });
}
/* Pas d'appel à majPubli() ici : il enregistre, et il tournerait AVANT restore().
   La page écraserait alors sa propre sauvegarde à chaque ouverture (règle n°221). */
__JS_EN_PLUS__
"""
