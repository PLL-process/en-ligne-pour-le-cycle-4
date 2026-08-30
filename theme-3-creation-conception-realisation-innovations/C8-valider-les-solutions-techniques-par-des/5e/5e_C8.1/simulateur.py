# -*- coding: utf-8 -*-
"""Le simulateur de la patère — HTML et JS engendrés depuis `patere.py`.

Un seul endroit décide des chiffres : le modèle Python. La page reçoit les
matériaux en JSON, et le banc de tests interroge la page pour vérifier qu'elle
dit exactement ce que le modèle calcule. Aucune valeur n'est recopiée à la
main — c'est la seule façon d'être sûr qu'un chiffre corrigé dans le modèle ne
survive pas, faux, dans la page (règle d'or n°233).
"""

import json

import patere as P

CSS = """
.simu{background:#081733;border:1.5px solid var(--hl);border-radius:12px;padding:16px}
.simu h4{margin:0 0 10px;color:var(--hl);font-size:1em}
.atelier{display:grid;grid-template-columns:minmax(210px,.9fr) minmax(260px,1.1fr);gap:16px;align-items:start}
@media(max-width:660px){.atelier{grid-template-columns:1fr}}
.atelier svg{width:100%;height:auto;background:#081b3a;border-radius:10px}
.cmd{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:8px 0}
.cmd label{font-size:.9em;color:var(--sub)}
.cmd select,.cmd input[type=number]{width:auto;min-width:110px}
.lecture{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:1.1em;color:var(--hl);margin:6px 0 2px}
.lecture b{color:#fff}
.jauge{height:16px;border-radius:8px;background:#0a1b3d;border:1px solid var(--border);overflow:hidden;position:relative}
.jauge>span{display:block;height:100%;width:100%;background:linear-gradient(90deg,#3aa76d,#ffd66b,#ff7b88);clip-path:inset(0 100% 0 0);transition:clip-path .18s}
.jauge>i{position:absolute;top:-3px;bottom:-3px;width:2px;background:#fff;opacity:.85}
table.releve{width:100%;border-collapse:collapse;font-size:.86em;margin:8px 0}
table.releve th,table.releve td{border:1px solid var(--border);padding:6px 8px;text-align:left}
table.releve th{background:#173666;color:var(--hl)}
table.releve tr.ok td{background:rgba(129,251,161,.10)}
table.releve tr.ko td{background:rgba(255,123,136,.10)}
.verdict-ok{color:var(--ok);font-weight:700}
.verdict-non{color:var(--err);font-weight:700}
.ecart{border-left:4px solid var(--warn);background:rgba(255,214,102,.08);padding:9px 13px;border-radius:0 10px 10px 0;margin:10px 0}
"""

#: la patère vue de côté : mur, bras, charge. Original, CC0.
SVG = """
<svg viewBox="0 0 300 210" role="img" aria-labelledby="svgT svgD">
  <title id="svgT">Le crochet du hall vu de côté, et la contrainte dans son bras</title>
  <desc id="svgD">Un mur vertical à gauche. Un bras horizontal de 60 mm part du mur ;
  une charge est suspendue à son extrémité. La couleur du bras montre la contrainte de
  flexion : elle est maximale contre le mur, nulle au bout. Un texte donne la valeur en
  mégapascals et indique si le crochet reste élastique ou plie pour toujours.</desc>
  <defs>
    <linearGradient id="gradC" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ff7b88" id="g0"/>
      <stop offset="55%" stop-color="#ffd66b" id="g1"/>
      <stop offset="100%" stop-color="#3aa76d" id="g2"/>
    </linearGradient>
    <pattern id="mur" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="16" height="16" fill="#12305e"/>
      <path d="M0 8h16M8 0v8M0 16h16" stroke="#274a8a" stroke-width="1.4"/>
    </pattern>
  </defs>
  <rect x="0" y="0" width="60" height="210" fill="url(#mur)"/>
  <line x1="60" y1="0" x2="60" y2="210" stroke="#61dafb" stroke-width="2"/>
  <g id="bras">
    <rect id="brasRect" x="60" y="72" width="180" height="26" rx="4" fill="url(#gradC)"/>
    <rect x="60" y="72" width="180" height="26" rx="4" fill="none" stroke="#0a1b3d" stroke-width="1.5"/>
  </g>
  <path id="crochet" d="M240 98 q22 0 22 26 q0 20 -20 20" fill="none" stroke="#9bbefc" stroke-width="9" stroke-linecap="round"/>
  <g id="sac">
    <path d="M228 150 l30 0 l7 40 l-44 0 z" fill="#2966b1" stroke="#81aaff" stroke-width="2"/>
    <path d="M236 150 q7 -14 14 0" fill="none" stroke="#81aaff" stroke-width="3"/>
  </g>
  <text x="150" y="60" text-anchor="middle" fill="#9bbefc" font-size="12">contrainte maximale contre le mur</text>
  <text x="70" y="120" fill="#ff7b88" font-size="13" id="svgSigma">— MPa</text>
  <text x="150" y="205" text-anchor="middle" fill="#e4eaf5" font-size="13" id="svgEtat">règle le simulateur</text>
</svg>
"""

HTML = """
<div class="simu">
  <h4>🖥️ Le simulateur fourni par le service technique</h4>
  <p style="font-size:.9em;color:var(--sub);margin:0 0 10px">
    Il calcule la contrainte de flexion dans le bras du crochet, et la compare à la
    <b>limite élastique</b> du matériau — la valeur au-delà de laquelle le crochet
    reste tordu même une fois le sac enlevé. Tu ne le programmes pas : tu l'utilises.
  </p>
  <div class="atelier">
    <div>__SVG__</div>
    <div>
      <div class="cmd">
        <label for="mat">Matériau</label>
        <select id="mat">__OPTIONS__</select>
      </div>
      <div class="cmd">
        <label for="charge">Charge suspendue</label>
        <input type="number" id="charge" min="1" max="250" step="1" value="__SERVICE__"> kg
      </div>
      <div class="cmd">
        <button class="btn" id="calculer">▶ Calculer</button>
        <button class="btn" id="ajouter">＋ Reporter dans le tableau</button>
      </div>
      <p class="lecture">contrainte : <b id="lSigma">—</b> · limite élastique : <b id="lLim">—</b></p>
      <p class="lecture">coefficient de sécurité : <b id="lCoef">—</b> (exigé : __COEF__)</p>
      <div class="jauge" aria-hidden="true"><span id="jSigma"></span><i id="jSeuil" style="left:0"></i></div>
      <p id="lVerdict" style="margin:8px 0 0">—</p>
    </div>
  </div>

  <table class="releve" id="tab">
    <thead><tr><th>Matériau</th><th>σ sous __SERVICE__ kg</th><th>limite élastique</th>
      <th>coefficient</th><th>décision</th></tr></thead>
    <tbody><tr><td colspan="5" style="color:var(--sub)">Aucun essai reporté pour l'instant.</td></tr></tbody>
  </table>
  <p class="lecture">essais reportés : <b id="nEssais">0</b> · retenus : <b id="nRetenus">0</b></p>
</div>
"""

JS = """
/* ── le simulateur fourni ────────────────────────────────────────────────
   Les matériaux viennent du modèle Python (patere.py) : aucune valeur n'est
   recopiée ici à la main. */
const MAT = __MATERIAUX__;
const GEO = __GEO__;
const $ = i => document.getElementById(i);
const fr = (x, d) => x.toFixed(d).replace(".", ",");
const releves = {};

function courant(){ return MAT.filter(m => m.nom === $("mat").value)[0]; }

/** Contrainte de flexion, en MPa. Elle ne dépend PAS du matériau : seulement
 *  de la charge et de la forme du bras. C'est le piège n°1 de la séquence. */
function contrainte(kg){ return kg * GEO.g * GEO.L / GEO.module; }

function peindre(m, kg){
  const s = contrainte(kg), k = m.sigma_e / s;
  const part = Math.min(s / m.sigma_e, 1);
  $("jSigma").style.clipPath = "inset(0 " + (100 - part * 100) + "% 0 0)";
  $("jSeuil").style.left = (100 / GEO.coef) + "%";
  $("lSigma").textContent = fr(s, 1) + " MPa";
  $("lLim").textContent = m.sigma_e + " MPa";
  $("lCoef").textContent = fr(k, 1);
  $("svgSigma").textContent = fr(s, 1) + " MPa";
  const ok = k >= GEO.coef;
  $("svgEtat").textContent = s > m.sigma_e
    ? "le crochet plie pour toujours"
    : (ok ? "élastique, avec la marge exigée" : "élastique, mais sans la marge exigée");
  $("svgEtat").setAttribute("fill", ok ? "#81fba1" : "#ff7b88");
  $("lVerdict").innerHTML = ok
    ? '<span class="verdict-ok">✔ retenu — ' + fr(k, 1) + ' ≥ ' + GEO.coef + '</span>'
    : '<span class="verdict-non">✘ écarté — ' + fr(k, 1) + ' &lt; ' + GEO.coef + '</span>';
}

function tableau(){
  const tb = $("tab").tBodies[0];
  const noms = Object.keys(releves);
  if(!noms.length){
    tb.innerHTML = '<tr><td colspan="5" style="color:var(--sub)">Aucun essai reporté pour l\\'instant.</td></tr>';
  } else {
    tb.innerHTML = noms.map(n => {
      const r = releves[n];
      return '<tr class="' + (r.ok ? "ok" : "ko") + '"><td>' + n + '</td><td>' + fr(r.sigma, 1)
        + ' MPa</td><td>' + r.lim + ' MPa</td><td>' + fr(r.k, 1) + '</td><td>'
        + (r.ok ? '<span class="verdict-ok">retenu</span>'
                : '<span class="verdict-non">écarté</span>') + '</td></tr>';
    }).join("");
  }
  $("nEssais").textContent = noms.length;
  $("nRetenus").textContent = noms.filter(n => releves[n].ok).length;
}

$("calculer").addEventListener("click", () => {
  const m = courant(), kg = Math.max(1, +$("charge").value || 1);
  peindre(m, kg);
  /* Un verrou ne s'ouvre que par un geste — jamais au chargement (règle n°226). */
  window.__exp = window.__exp || {};
  window.__exp.simule = true;
  if(save) save();
});

$("ajouter").addEventListener("click", () => {
  const m = courant(), kg = Math.max(1, +$("charge").value || 1);
  peindre(m, kg);
  const s = contrainte(kg), k = m.sigma_e / s;
  releves[m.nom] = {sigma: s, lim: m.sigma_e, k: k, ok: k >= GEO.coef, kg: kg};
  tableau();
  window.__exp = window.__exp || {};
  window.__exp.simule = true;
  if(Object.keys(releves).length >= MAT.length) window.__exp.tous = true;
  if(releves["Bois (pin)"] && !releves["Bois (pin)"].ok) window.__exp.bois = true;
  if(save) save();
});
"""


def bloc(cle_option="mat"):
    """Le fragment HTML du simulateur, prêt à coller dans la séquence."""
    options = "".join('<option>%s</option>' % m.nom for m in P.MATERIAUX)
    return (HTML.replace("__SVG__", SVG.strip())
                .replace("__OPTIONS__", options)
                .replace("__SERVICE__", str(P.CHARGE_SERVICE))
                .replace("__COEF__", str(P.COEF_EXIGE)))


def script():
    """Le JS du simulateur, alimenté par le modèle Python."""
    mats = [dict(nom=m.nom, sigma_e=m.sigma_e, sigma_r=m.sigma_r,
                 prix=m.prix, minutes=m.minutes, humidite=m.humidite)
            for m in P.MATERIAUX]
    geo = dict(L=P.L, module=P.MODULE, g=P.G, coef=P.COEF_EXIGE,
               service=P.CHARGE_SERVICE, nombre=P.NOMBRE)
    return (JS.replace("__MATERIAUX__", json.dumps(mats, ensure_ascii=False))
              .replace("__GEO__", json.dumps(geo)))


if __name__ == "__main__":
    print(bloc()[:400])
    print("…")
    print(script()[:400])
