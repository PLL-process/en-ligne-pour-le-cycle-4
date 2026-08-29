# -*- coding: utf-8 -*-
"""L'établi Grove — on monte des constituants, et le prototype dit ce qui ne va pas.

Un prototype n'est pas une liste de composants : c'est un assemblage qui doit
tenir quatre fonctions à la fois — **acquérir, traiter, agir, alimenter** — et
qui tombe dès qu'il en manque une. L'établi rend ça manipulable :

  · on choisit un port pour chaque constituant ;
  · on teste, et l'établi ne dit pas « ça ne marche pas », il dit POURQUOI :
    le port n'est pas du bon type, la fonction n'est pas tenue, le budget de
    courant est dépassé, ou le programme lit ailleurs que là où c'est branché ;
  · on peut RETIRER un constituant d'un montage qui marchait et voir ce que ça
    casse (règle d'or n°213 : ce qui fait la découverte, c'est de pouvoir retirer).

Le diagnostic est ordonné du plus grossier au plus fin, comme celui d'un
dépanneur : sans carte, rien ne s'exécute — inutile de parler du port du capteur.
"""

CSS = """
/* ── Établi Grove — original, CC0 ───────────────────────────────────────── */
.etabli{background:#0a1b3d;border:1px solid var(--border);border-radius:12px;padding:14px;margin:12px 0}
.chaine{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:12px}
@media(max-width:620px){.chaine{grid-template-columns:repeat(2,1fr)}}
.fct{background:#132c58;border:1px solid var(--border);border-radius:10px;padding:9px 8px;text-align:center;transition:background .2s,border-color .2s}
.fct b{display:block;font-size:.9em;color:var(--sub)}
.fct span{font-size:.78em;color:var(--sub)}
.fct.tenue{background:#14532d;border-color:var(--ok)}
.fct.tenue b{color:#eafff0}
table.cat{width:100%;border-collapse:collapse;font-size:.88em;margin:8px 0}
table.cat th,table.cat td{border:1px solid var(--border);padding:5px 8px;text-align:left;vertical-align:middle}
table.cat th{background:#173666;color:var(--hl)}
table.cat td.pt{width:150px}
table.cat td.pt select{width:100%;min-width:0;padding:4px 6px;font-size:.92em}
table.cat tr.monte td:not(.pt){color:#fff}
table.cat td.ma{width:70px;text-align:right;color:var(--sub);font-variant-numeric:tabular-nums}
.budget{font-size:.86em;color:var(--sub);margin:4px 0 10px}
.budget b{color:var(--hl)}
.budget.trop b{color:var(--err)}
.etabli-cmd{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0}
.verdict{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.86em;background:#050f24;border:1px solid var(--border);border-radius:9px;padding:9px 11px;max-height:170px;overflow-y:auto}
.verdict div{padding:1px 0}
.verdict .ok{color:var(--ok)}.verdict .ko{color:var(--err)}.verdict .wa{color:var(--warn)}
.prog{font-family:ui-monospace,Menlo,Consolas,monospace;background:#050f24;border:1px solid var(--border);border-radius:9px;padding:10px 12px;font-size:.86em;color:var(--hl);overflow-x:auto;white-space:pre;margin:8px 0}
.prog .cm{color:#7f9cc4}
.symp{background:#3a2a10;border-left:4px solid var(--warn);border-radius:0 8px 8px 0;padding:8px 12px;margin:8px 0;font-size:.92em}
table.releve{width:100%;border-collapse:collapse;font-size:.87em;margin:8px 0}
table.releve th,table.releve td{border:1px solid var(--border);padding:6px 8px;text-align:left}
table.releve th{background:#173666;color:var(--hl)}
table.releve td.num{width:32%}
table.releve td input{padding:4px 8px}
.grille{list-style:none;padding:0;margin:8px 0}
.grille li{border-left:3px solid var(--head);background:rgba(198,142,242,.08);padding:7px 12px;border-radius:0 8px 8px 0;margin:6px 0;font-size:.94em}
"""

FONCTIONS = [("acquerir", "Acquérir", "prendre la mesure"),
             ("traiter", "Traiter", "décider quoi faire"),
             ("agir", "Agir", "produire l'effet"),
             ("alimenter", "Alimenter", "fournir l'énergie")]


def html(titre, constituants, ports, programme="", symptome="", extra=""):
    """constituants : [(id, nom, role)] — le reste (ports admis, mA) est en JS."""
    cases = "\n".join(
        '      <div class="fct" id="f_%s"><b>%s</b><span>%s</span></div>' % f[:3]
        for f in FONCTIONS)
    opts = "".join('<option value="%s">%s</option>' % (p, p) for p in ports)
    lignes = "\n".join(
        '      <tr id="tr_%s"><td><b>%s</b></td><td>%s</td>'
        '<td class="ma" id="ma_%s">—</td>'
        '<td class="pt"><select id="pt_%s" aria-label="Port de %s">'
        '<option value="">— non monté —</option>%s</select></td></tr>'
        % (i, nom, role, i, i, nom, opts)
        for i, nom, role in constituants)
    bloc_prog = ('    <p style="font-size:.9em;color:var(--sub);margin:10px 0 2px">'
                 "Le programme téléversé dans la carte (on ne le modifie pas) :</p>\n"
                 '    <div class="prog">%s</div>\n' % programme) if programme else ""
    bloc_symp = ('    <div class="symp">%s</div>\n' % symptome) if symptome else ""
    return """
  <div class="etabli">
    <p style="font-size:.92em;color:var(--sub);margin:0 0 8px"><b>%s</b></p>
%s
    <div class="chaine">
%s
    </div>

    <table class="cat">
      <tr><th>Constituant</th><th>Ce qu'il fait</th><th>mA</th><th>Port</th></tr>
%s
    </table>
    <p class="budget" id="budget">—</p>
%s
    <div class="etabli-cmd">
      <button class="btn" id="tester" type="button">⚡ Tester le prototype</button>
      <button class="btn" id="demonter" type="button">↺ Tout démonter</button>
    </div>
    <div class="verdict" id="verdict"><div>Aucun essai. Monte les constituants, puis teste.</div></div>
%s
  </div>
""" % (titre, bloc_symp, cases, lignes, bloc_prog, extra)


JS = """
/* ── établi Grove ───────────────────────────────────────────────────────── */
/* CONSTITUANTS : {id, nom, fonction, ports:[types admis], mA, attendu?, cle?} */
const CONST = __CONSTITUANTS__;
const BUDGET = __BUDGET__;          /* mA disponibles sans alimentation externe */
const ATTENDU = __ATTENDU__;        /* {id: "A0"} — ce que le programme lit/écrit */
const OBLIGE = __OBLIGE__;          /* fonctions que ce prototype doit tenir */
const REQUIS = __REQUIS__;          /* {id: raison} — constituants sans lesquels le cahier
                                       des charges n'est pas tenu, même si la fonction l'est */
const MARCHE = __MARCHE__;          /* phrase décrivant le comportement obtenu */
let dejaOk = false;

function typePort(p){
  if(!p) return "";
  if(p === "ALIM EXT") return "ALIM";
  if(p === "SOCLE" || p === "I2C" || p === "UART") return p;
  return p[0];                       /* "A0" → "A", "D4" → "D" */
}
function montes(){
  return CONST.filter(c => document.getElementById("pt_" + c.id).value);
}
function portDe(c){ return document.getElementById("pt_" + c.id).value; }

function majEtabli(){
  const m = montes();
  CONST.forEach(c => {
    const mo = !!portDe(c);
    document.getElementById("tr_" + c.id).classList.toggle("monte", mo);
    document.getElementById("ma_" + c.id).textContent = mo ? c.mA : "—";
  });
  FONCTIONS_ID.forEach(f => {
    const tenue = m.some(c => c.fonction === f);
    document.getElementById("f_" + f).classList.toggle("tenue", tenue);
  });
  const somme = m.reduce((s, c) => s + c.mA, 0);
  const ext = m.some(c => c.fonction === "alimenter" && c.externe);
  const b = document.getElementById("budget");
  b.textContent = "Courant demandé : " + somme + " mA sur " + (ext ? "l'alimentation externe (2000 mA)" : BUDGET + " mA disponibles par l'USB")
    + (somme > (ext ? 2000 : BUDGET) ? " — c'est trop." : "");
  b.classList.toggle("trop", somme > (ext ? 2000 : BUDGET));
  if(m.length) window.__exp.monte = true;
  save();
}

/* Le diagnostic, du plus grossier au plus fin — comme celui d'un dépanneur. */
function diagnostic(){
  const m = montes(), noms = m.map(c => c.id);
  if(!noms.includes("carte"))
    return ["ko", "Rien ne s'exécute : il n'y a pas de carte. Le programme n'a nulle part où tourner.", "sans_carte"];
  if(CONST.some(c => c.id === "shield") && !noms.includes("shield"))
    return ["ko", "Aucun module ne peut être branché : le Base Shield manque. Les connecteurs Grove n'ont pas de prise sur la carte nue.", "sans_shield"];

  for(const c of m){
    const p = portDe(c), t = typePort(p);
    if(c.ports.length && !c.ports.includes(t))
      return ["ko", c.nom + " est sur " + p + ", et il lui faut " + c.ports.map(x => LIBPORT[x] || x).join(" ou ") + ". " + c.pourquoi, "port_" + c.id];
  }
  const doublons = {};
  for(const c of m){ const p = portDe(c);
    if(p !== "ALIM EXT" && p !== "SOCLE" && doublons[p])
      return ["ko", "Deux constituants sur " + p + " : " + doublons[p] + " et " + c.nom + ". Un port ne reçoit qu'un module.", "doublon"];
    doublons[p] = c.nom; }

  /* un constituant qui en exige un autre : la puissance ne se commande pas
     directement depuis une sortie de carte. */
  for(const c of m){
    if(c.exige && !noms.includes(c.exige))
      return ["ko", c.siManque, "exige_" + c.exige];
  }
  for(const f of OBLIGE){
    if(!m.some(c => c.fonction === f))
      return ["ko", "La fonction « " + LIB[f] + " » n'est tenue par aucun constituant. " + MANQUE[f], "fonction_" + f];
  }
  /* la fonction peut être tenue et le cahier des charges non tenu : deux choses
     différentes, et c'est exactement ce qu'un prototype incomplet enseigne. */
  for(const id in REQUIS){
    if(!noms.includes(id)) return ["ko", REQUIS[id], "requis_" + id];
  }
  const somme = m.reduce((s, c) => s + c.mA, 0);
  const ext = m.some(c => c.fonction === "alimenter" && c.externe);
  const dispo = ext ? 2000 : BUDGET;
  if(somme > dispo)
    return ["ko", "Le montage demande " + somme + " mA et n'en a que " + dispo + ". La carte s'effondre et redémarre en boucle : il faut une alimentation externe très basse tension.", "budget"];

  for(const c of m){
    const att = ATTENDU[c.id];
    if(att && portDe(c) !== att)
      return ["ko", "Le programme " + (c.sens || "lit") + " " + att + ", et " + c.nom + " est sur " + portDe(c) + " : l'ordre et la mesure se croisent sans se rencontrer. Le branchement et le programme doivent dire la même chose.", "attendu_" + c.id];
  }
  return ["ok", MARCHE, "ok"];
}

function verdict(cls, txt){
  const v = document.getElementById("verdict");
  if(v.dataset.vide !== "non"){ v.innerHTML = ""; v.dataset.vide = "non"; }
  const d = document.createElement("div");
  d.className = cls;
  d.textContent = (cls === "ok" ? "✔ " : "✘ ") + txt;
  v.appendChild(d); v.scrollTop = v.scrollHeight;
}

document.getElementById("tester").addEventListener("click", () => {
  const [cls, txt, id] = diagnostic();
  verdict(cls, txt);
  window.__exp.teste = true;
  window.__exp["diag_" + id] = true;   /* on a VU ce diagnostic-là, pas un autre */
  if(cls === "ko") window.__exp.panne = true;
  if(cls === "ok"){ window.__exp.ok = true; dejaOk = true; }
  else if(dejaOk) window.__exp.retire = true;
  save();
});
document.getElementById("demonter").addEventListener("click", () => {
  CONST.forEach(c => { document.getElementById("pt_" + c.id).value = ""; });
  majEtabli(); verdict("ko", "Établi vide.");
});
CONST.forEach(c =>
  document.getElementById("pt_" + c.id).addEventListener("change", majEtabli));
/* Pas d'appel à majEtabli() ici : il enregistre, et il tournerait AVANT restore().
   La page écraserait alors sa propre sauvegarde par un établi vide à chaque
   ouverture. C'est le squelette qui appelle restore() puis majEtabli(). */
__JS_EN_PLUS__
"""

PRELUDE = """
const FONCTIONS_ID = ["acquerir","traiter","agir","alimenter"];
const LIB = {acquerir:"Acquérir", traiter:"Traiter", agir:"Agir", alimenter:"Alimenter"};
const LIBPORT = {
  A:"une entrée analogique (A0 à A3)", D:"un port numérique (D2 à D8)",
  I2C:"un port I2C", UART:"le port UART", SOCLE:"une place sur le socle",
  ALIM:"l'alimentation externe"
};
const MANQUE = {
  acquerir:"Sans capteur, le prototype n'a aucune information sur le monde : il ne peut que répéter la même chose.",
  traiter:"Sans carte programmable, personne ne décide : une mesure sans décision ne déclenche rien.",
  agir:"Sans actionneur, la décision reste à l'intérieur : rien ne se passe dans le monde réel.",
  alimenter:"Sans source d'énergie, aucun des trois autres ne fonctionne — c'est la fonction qu'on oublie en dernier et qui arrête tout en premier."
};
"""
