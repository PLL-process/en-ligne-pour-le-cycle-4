# -*- coding: utf-8 -*-
"""Le banc des matériaux — on pose des exigences, et le banc dit qui tombe et pourquoi.

Un tableau de caractéristiques n'apprend rien : il se lit, il ne se manipule pas.
Le banc rend trois choses manipulables, et chacune correspond à une erreur qu'on
fait vraiment :

  · **le seuil** — on peut le déplacer, et voir un matériau passer de recalé à
    retenu. Un seuil n'est pas une propriété du matériau : c'est une décision ;
  · **le critère lui-même** — on peut le RETIRER (règle d'or n°213). Le nombre de
    matériaux retenus change, et l'élève voit que « le meilleur matériau » n'existe
    pas : il n'existe que le meilleur pour les critères qu'on a gardés ;
  · **la durée** — le coût d'achat et le coût sur quinze ans ne classent pas les
    matériaux dans le même ordre, parce qu'ils ne durent pas le même temps.

Le banc ne note pas, ne pondère pas et ne conseille pas. Il élimine, et il dit
sur quel critère — parce qu'**un seuil n'est pas une note** : un matériau qui
échoue à un seuil de sécurité n'arrive pas troisième, il est écarté.
"""

CSS = """
/* ── Banc des matériaux — original, CC0 ─────────────────────────────────── */
.bancm{background:#0a1b3d;border:1px solid var(--border);border-radius:12px;padding:14px;margin:12px 0}
table.mat{width:100%;border-collapse:collapse;font-size:.85em;margin:8px 0}
table.mat th,table.mat td{border:1px solid var(--border);padding:5px 7px;text-align:right}
table.mat th{background:#173666;color:var(--hl);text-align:center;font-size:.95em}
table.mat td.nom{text-align:left;width:31%}
table.mat td.ver{text-align:left;width:24%;font-size:.94em}
table.mat tr.ok td{background:rgba(34,197,94,.10)}
table.mat tr.ok td.ver{color:var(--ok);font-weight:600}
table.mat tr.ko td{color:var(--sub)}
table.mat tr.ko td.ver{color:var(--err)}
table.mat td.faute{color:var(--err);font-weight:600}
table.exig{width:100%;border-collapse:collapse;font-size:.88em;margin:8px 0}
table.exig th,table.exig td{border:1px solid var(--border);padding:5px 8px;text-align:left}
table.exig th{background:#173666;color:var(--hl)}
table.exig td.ck{width:34px;text-align:center}
table.exig td input[type=checkbox]{width:17px;height:17px;accent-color:#61dafb}
table.exig td.sv{width:118px}
table.exig td.sv input{width:100%;padding:3px 6px;font-size:.92em;text-align:right}
table.exig tr.off td:not(.ck){color:var(--sub);text-decoration:line-through}
table.exig td.pq{font-size:.9em;color:var(--sub)}
.compteur{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}
.jauge{flex:1;min-width:180px;background:#132c58;border:1px solid var(--border);border-radius:10px;padding:9px 11px}
.jauge b{display:block;font-size:1.5em;color:var(--hl);font-variant-numeric:tabular-nums}
.jauge span{font-size:.8em;color:var(--sub)}
.jauge.zero b{color:var(--err)}
.jauge.un b{color:var(--warn)}
.jauge.plus b{color:var(--ok)}
.bancm-cmd{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0}
.bancm-cmd label{font-size:.9em;color:var(--sub)}
.bancm-cmd select{width:auto;min-width:150px}
.verdict{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.85em;background:#050f24;border:1px solid var(--border);border-radius:9px;padding:9px 11px;max-height:160px;overflow-y:auto}
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


def html(titre, exigences, colonnes, duree=None, extra=""):
    """exigences : [(cle, libellé, unité, sens, valeur, pourquoi)]"""
    lignes_ex = "\n".join(
        '      <tr id="ex_%s"><td class="ck"><input type="checkbox" id="on_%s" checked></td>'
        '<td>%s</td><td>%s</td><td class="sv"><input type="text" inputmode="decimal" '
        'id="sv_%s" value="%s" aria-label="Seuil de %s"></td><td class="pq">%s</td></tr>'
        % (c, c, lib, sens, c, str(val).replace(".", ","), lib, pq)
        for c, lib, u, sens, val, pq in exigences)
    entetes = "".join("<th>%s<br><small>%s</small></th>" % (lib, u) for lib, u in colonnes)
    # La masse a déjà sa colonne quand « masse de la pièce » est une exigence.
    # L'écrire deux fois n'est pas un doublon d'affichage : c'est un tableau qui
    # dit deux fois la même mesure sous deux en-têtes différentes, et l'élève
    # cherche alors ce qui les distingue. Il n'y a rien à trouver.
    masse_a_part = "" if any(c == "masse_max" for c, *_ in exigences) \
        else "<th>Masse<br><small>kg</small></th>"
    bloc_duree = ""
    if duree:
        bloc_duree = ('    <div class="bancm-cmd"><label for="duree">Comparer les coûts sur :</label>\n'
                      '      <select id="duree">\n%s\n      </select></div>\n'
                      % "\n".join('        <option value="%d">%s</option>' % (a, t) for a, t in duree))
    return """
  <div class="bancm">
    <p style="font-size:.92em;color:var(--sub);margin:0 0 8px"><b>%s</b></p>

    <p style="font-size:.9em;color:var(--sub);margin:8px 0 2px">Les exigences du cahier des
    charges. Décoche pour <b>retirer</b> un critère, ou change un seuil.</p>
    <table class="exig">
      <tr><th></th><th>Critère</th><th>Sens</th><th>Seuil</th><th>Pourquoi ce seuil</th></tr>
%s
    </table>
%s
    <div class="compteur">
      <div class="jauge" id="jRet"><b id="nRet">—</b><span>matériau(x) retenu(s)</span></div>
      <div class="jauge" id="jMoins"><b id="nMoins">—</b><span>le moins cher des retenus</span></div>
    </div>

    <table class="mat" id="tab">
      <tr><th>Matériau</th>%s%s<th>Coût<br><small>€</small></th><th>Verdict</th></tr>
    </table>

    <div class="bancm-cmd">
      <button class="btn" id="evaluer" type="button">⚖ Évaluer les candidats</button>
      <button class="btn" id="reinit" type="button">↺ Remettre le cahier des charges</button>
    </div>
    <div class="verdict" id="verdict"><div>Aucun essai. Règle les exigences, puis évalue.</div></div>
%s
  </div>
""" % (titre, lignes_ex, bloc_duree, entetes, masse_a_part, extra)


JS = """
/* ── banc des matériaux ─────────────────────────────────────────────────── */
const MATS = __MATS__;        /* [{cle, nom, val:{critere:…}, masse, cout, uv, note}] */
const EXIG = __EXIG__;        /* [{cle, lib, unite, sens, defaut}] */
const COLS = __COLS__;        /* [critères affichés en colonnes] */

function seuil(c){
  const e = document.getElementById("sv_" + c);
  const v = parseFloat((e.value || "").replace(",", "."));
  return isNaN(v) ? null : v;
}
function actif(c){ return document.getElementById("on_" + c).checked; }
function annees(){
  const e = document.getElementById("duree");
  return e ? parseInt(e.value, 10) : 0;
}
function coutSur(m){
  const a = annees();
  if(!a) return [m.cout, 1];
  const n = Math.max(1, Math.ceil(a / m.uv));
  return [m.cout * n, n];
}
function vg(x, d){ return x.toFixed(d).replace(".", ","); }

/* Le nombre de décimales n'est pas une préférence d'écriture : c'est ce qui
   décide si l'élève VOIT la différence. Le boîtier de 3e pèse 0,545 kg en PVC
   et 0,557 kg en aluminium — arrondis au dixième, ils affichent 0,5 et 0,6, et
   la page raconte alors le contraire de ce qu'elle démontre. On règle donc la
   précision sur l'ordre de grandeur de l'objet, une fois, pour tout le tableau. */
const DEC_C = Math.max.apply(null, MATS.map(m => m.cout)) < 40 ? 2 : 0;
const DEC_M = Math.max.apply(null, MATS.map(m => m.masse)) < 10 ? 3 : 1;
/* Quand « masse de la pièce » est une exigence, elle a déjà sa colonne. */
const MASSE_A_PART = COLS.indexOf("masse_max") < 0;

function juge(m){
  const rates = [];
  EXIG.forEach(e => {
    if(!actif(e.cle)) return;
    const s = seuil(e.cle);
    if(s === null) return;
    const v = m.val[e.cle];
    const ok = e.sens === "au plus" ? v <= s : v >= s;
    if(!ok) rates.push(e.lib.toLowerCase());
  });
  return rates;
}

/* `geste` : vrai quand la mise à jour vient d'une action de l'élève. Faux à
   l'ouverture de la page. Un verrou expérientiel que l'état initial suffit à
   ouvrir n'est pas un verrou — le boîtier de 3e ne retient AUCUN matériau tel
   qu'il est écrit, et « avoir vu zéro » s'obtiendrait alors sans rien faire. */
function majBanc(geste){
  EXIG.forEach(e =>
    document.getElementById("ex_" + e.cle).classList.toggle("off", !actif(e.cle)));
  const t = document.getElementById("tab");
  while(t.rows.length > 1) t.deleteRow(1);
  let retenus = [], moins = null;
  MATS.forEach(m => {
    const rates = juge(m), ok = rates.length === 0;
    const [c, n] = coutSur(m);
    if(ok){ retenus.push(m); if(moins === null || c < moins[0]) moins = [c, m]; }
    const tr = t.insertRow();
    tr.className = ok ? "ok" : "ko";
    const cel = x => { const d = tr.insertCell(); d.innerHTML = x; return d; };
    cel("<b>" + m.nom + "</b>").className = "nom";
    COLS.forEach(c2 => {
      const e = EXIG.find(x => x.cle === c2);
      const d = cel(vg(m.val[c2], c2 === "masse_max" ? DEC_M : 0));
      if(e && actif(c2) && rates.includes(e.lib.toLowerCase())) d.className = "faute";
    });
    if(MASSE_A_PART) cel(vg(m.masse, DEC_M));
    cel(n > 1 ? vg(c, DEC_C) + " <small>(" + n + "×)</small>" : vg(c, DEC_C));
    cel(ok ? "✔ retenu" : "✘ " + rates.join(", ")).className = "ver";
  });
  const j = document.getElementById("jRet");
  document.getElementById("nRet").textContent = retenus.length;
  j.classList.toggle("zero", retenus.length === 0);
  j.classList.toggle("un", retenus.length === 1);
  j.classList.toggle("plus", retenus.length > 1);
  document.getElementById("nMoins").textContent =
    moins ? vg(moins[0], DEC_C) + " €" : "—";
  document.getElementById("jMoins").classList.toggle("zero", !moins);

  if(geste){
    if(retenus.length === 0) window.__exp.zero = true;
    if(retenus.length === 1) window.__exp.unSeul = true;
    if(EXIG.some(e => !actif(e.cle))) window.__exp.retireCritere = true;
    if(annees() > 0) window.__exp.duree = true;
  }
  save();
  return retenus;
}

function ligne(cls, txt){
  const v = document.getElementById("verdict");
  if(v.dataset.vide !== "non"){ v.innerHTML = ""; v.dataset.vide = "non"; }
  const d = document.createElement("div");
  d.className = cls; d.textContent = txt;
  v.appendChild(d); v.scrollTop = v.scrollHeight;
}

document.getElementById("evaluer").addEventListener("click", () => {
  const r = majBanc(true);
  window.__exp.evalue = true;
  if(!r.length){
    ligne("ko", "Aucun matériau ne tient ce cahier des charges. Ce n'est pas une panne du banc : "
        + "c'est un résultat. Il faut changer une exigence, ou changer l'objet.");
  } else if(r.length === 1){
    ligne("wa", "Un seul candidat tient : " + r[0].nom + ". Un choix sans alternative n'est pas "
        + "un choix — vérifie qu'aucun seuil n'est plus sévère que nécessaire.");
  } else {
    const l = r.map(m => m.nom + " (" + vg(coutSur(m)[0], DEC_C) + " €)").join(" · ");
    ligne("ok", r.length + " candidats tiennent : " + l);
  }
  save();
});
document.getElementById("reinit").addEventListener("click", () => {
  EXIG.forEach(e => {
    document.getElementById("on_" + e.cle).checked = true;
    document.getElementById("sv_" + e.cle).value = String(e.defaut).replace(".", ",");
  });
  const d = document.getElementById("duree");
  if(d) d.value = d.options[0].value;
  majBanc(true);
  ligne("wa", "Cahier des charges remis tel qu'il est écrit.");
});
EXIG.forEach(e => {
  document.getElementById("on_" + e.cle).addEventListener("change", () => majBanc(true));
  document.getElementById("sv_" + e.cle).addEventListener("input", () => majBanc(true));
});
if(document.getElementById("duree"))
  document.getElementById("duree").addEventListener("change", () => majBanc(true));
/* Pas d'appel à majBanc() ici : il enregistre, et il tournerait AVANT restore()
   (règle d'or n°221). Le squelette restaure d'abord, puis met à jour. */
__JS_EN_PLUS__
"""
