# -*- coding: utf-8 -*-
"""L'atelier — on pose une forme, et l'atelier dit qui sait la produire, et à quel prix.

Un tableau de machines n'apprend rien : il se lit. L'atelier rend manipulables
les trois choses qui décident vraiment, et chacune correspond à une erreur
qu'on fait vraiment :

  · **le trait de forme** — en 3e, chaque cote du dessin se modifie. Le moyen
    ne change pas : c'est le DESSIN qui vient à sa rencontre. C'est le geste que
    C7.7 demande et que C7.3 ne demandait pas — là on rouvrait le cahier des
    charges, ici on n'y touche pas ;
  · **la quantité** — quatre pièces et trente pièces ne se fabriquent pas par
    le même moyen, et ce n'est pas une question d'intendance : le temps machine
    disponible est une contrainte de fabrication comme l'épaisseur minimale ;
  · **rien du tout** — deux traits n'ont besoin d'aucune correction. Les
    toucher est compté, séparément (règle d'or n°219).

Et l'atelier affiche, pour chaque moyen retenu, **ce qu'il fera du dessin**.
Aucun moyen ne rend la pièce dessinée : le laser élargit de son trait de coupe,
la fraiseuse arrondit les angles internes, l'impression laisse un bourrelet.
Le dessin est ce qu'on a demandé ; la pièce est ce qu'on obtient.
"""

CSS = """
/* ── Atelier des moyens — original, CC0 ─────────────────────────────────── */
.atel{background:#0a1b3d;border:1px solid var(--border);border-radius:12px;padding:14px;margin:12px 0}
table.traits{width:100%;border-collapse:collapse;font-size:.88em;margin:8px 0}
table.traits th,table.traits td{border:1px solid var(--border);padding:5px 8px;text-align:left}
table.traits th{background:#173666;color:var(--hl)}
table.traits td.val{width:120px}
table.traits td.val input{width:100%;padding:3px 6px;font-size:.92em;text-align:right}
table.traits td.pq{font-size:.9em;color:var(--sub)}
table.traits td.etat{width:34px;text-align:center;font-weight:700}
table.traits tr.ko td.etat{color:var(--err)}
table.traits tr.ok td.etat{color:var(--ok)}
table.traits tr.touche td.val input{outline:2px solid var(--warn)}
table.moy{width:100%;border-collapse:collapse;font-size:.85em;margin:8px 0}
table.moy th,table.moy td{border:1px solid var(--border);padding:5px 7px;text-align:left;vertical-align:top}
table.moy th{background:#173666;color:var(--hl);text-align:center}
table.moy td.nom{width:26%}
table.moy td.t{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
table.moy td.hors{color:var(--err)}
table.moy tr.ok td{background:rgba(34,197,94,.10)}
table.moy tr.ok td.ver{color:var(--ok);font-weight:600}
table.moy tr.ko td{color:var(--sub)}
table.moy tr.ko td.ver{color:var(--err)}
table.moy td.emp{font-size:.93em;color:var(--warn)}
.compteur{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}
.jauge{flex:1;min-width:170px;background:#132c58;border:1px solid var(--border);border-radius:10px;padding:9px 11px}
.jauge b{display:block;font-size:1.5em;color:var(--hl);font-variant-numeric:tabular-nums}
.jauge span{font-size:.8em;color:var(--sub)}
.jauge.zero b{color:var(--err)}
.jauge.un b{color:var(--warn)}
.jauge.plus b{color:var(--ok)}
.jauge.bon b{color:var(--ok)}
.atel-cmd{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0}
.atel-cmd label{font-size:.9em;color:var(--sub)}
.atel-cmd select{width:auto;min-width:210px}
.verdict{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.85em;background:#050f24;border:1px solid var(--border);border-radius:9px;padding:9px 11px;max-height:170px;overflow-y:auto}
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


def html(titre, traits, quantites, editable, jauge2, moyen_vise=None, extra=""):
    """traits : [(cle, libellé, valeur affichée, unité, pourquoi)]
       quantites : [(n, texte)] ; editable : les cotes se modifient (3e)
       jauge2 : (id, libellé) de la seconde jauge"""
    lignes = []
    for cle, lib, val, unite, pq in traits:
        champ = ('<input type="text" inputmode="decimal" id="tr_%s" value="%s" '
                 'aria-label="Cote : %s">' % (cle, val, lib)) if editable else \
                ('<b>%s</b> <span style="color:var(--sub)">%s</span>' % (val, unite))
        lignes.append('      <tr id="li_%s"><td class="etat" id="et_%s">·</td><td>%s</td>'
                      '<td class="val">%s</td><td class="pq">%s</td></tr>'
                      % (cle, cle, lib, champ, pq))
    entete_val = "Cote dessinée" if editable else "Valeur"
    legende = ('    <p style="font-size:.88em;color:var(--sub);margin:2px 0 10px">'
               "La colonne de gauche se lit <b>pour %s</b> — le moyen déjà retenu par le "
               "cahier des charges. <b>✘</b> : cette cote est hors de son domaine. "
               "<b>✔</b> : elle passe.</p>\n" % moyen_vise) if moyen_vise else ""
    bloc_q = ('    <div class="atel-cmd"><label for="qte">Nombre de pièces à produire :</label>\n'
              '      <select id="qte">\n%s\n      </select></div>\n'
              % "\n".join('        <option value="%d">%d — %s</option>' % (n, n, t)
                          for n, t in quantites))
    return """
  <div class="atel">
    <p style="font-size:.92em;color:var(--sub);margin:0 0 8px"><b>%s</b></p>

    <p style="font-size:.9em;color:var(--sub);margin:8px 0 2px">%s</p>
    <table class="traits">
      <tr><th></th><th>Ce que le dessin demande</th><th>%s</th><th>Pourquoi</th></tr>
%s
    </table>
%s%s
    <div class="compteur">
      <div class="jauge" id="jRet"><b id="nRet">—</b><span>moyen(s) capable(s) de produire cette forme</span></div>
      <div class="jauge" id="j2"><b id="%s">—</b><span>%s</span></div>
    </div>

    <table class="moy" id="tab">
      <tr><th>Moyen</th><th>Temps machine</th><th>Ce qu'il fera de ton dessin</th><th>Verdict</th></tr>
    </table>

    <div class="atel-cmd">
      <button class="btn" id="evaluer" type="button">🏭 Lancer l'atelier</button>
      <button class="btn" id="reinit" type="button">↺ Remettre le dessin d'origine</button>
    </div>
    <div class="verdict" id="verdict"><div>Aucun essai. Règle le dessin, puis lance l'atelier.</div></div>
%s
  </div>
""" % (titre,
       "Chaque cote se modifie. <b>Le cahier des charges, lui, ne bouge pas</b> : "
       "ni la matière, ni l'encombrement, ni ce que l'objet doit faire."
       if editable else
       "La forme est donnée : elle sort de la modélisation. <b>Tu ne la modifies pas</b> — "
       "tu choisis par quel moyen la produire.",
       entete_val, "\n".join(lignes), legende, bloc_q, jauge2[0], jauge2[1], extra)


JS = """
/* ── l'atelier des moyens ───────────────────────────────────────────────── */
const MOYENS = __MOYENS__;    /* domaine de chaque moyen */
const TRAITS = __TRAITS__;    /* [{cle, lib, valeur, unite, sansCorrection, correction}] */
const PIECE  = __PIECE__;     /* {matiere, etanche, tempsDispo} */
const EDIT   = __EDIT__;      /* les cotes sont-elles modifiables ? */

function vg(x, d){ return x.toFixed(d).replace(".", ","); }
function duree(min){
  min = Math.round(min);
  if(min < 60) return min + " min";
  const h = Math.floor(min / 60), r = min % 60;
  return r === 0 ? h + " h" : h + " h " + (r < 10 ? "0" : "") + r;
}
function cote(t){
  if(!EDIT) return t.valeur;
  const e = document.getElementById("tr_" + t.cle);
  const v = parseFloat((e.value || "").replace(",", "."));
  return isNaN(v) ? t.valeur : v;
}
function quantite(){ return parseInt(document.getElementById("qte").value, 10); }

/* Les règles de domaine. Elles disent POURQUOI, jamais « ça ne marche pas ». */
function tientTrait(m, t, v){
  switch(t.cle){
    case "epaisseur": {
      const s = PIECE.etanche ? m.e_etanche : m.e_min;
      return v >= s ? null
        : "il ne fait pas une paroi " + (PIECE.etanche ? "étanche " : "") + "de moins de " + vg(s, 1) + " mm";
    }
    case "r_int":
      return v >= m.r_int ? null : (m.pourquoiRayon || ("il impose un rayon de " + vg(m.r_int, 1) + " mm aux angles internes"));
    case "surplomb":
      if(m.surplomb === null) return null;
      return v <= m.surplomb ? null
        : "au-delà de " + m.surplomb + "° il faut un support, et le support laisse une surface rugueuse";
    case "res_z":
      return v >= m.res_z ? null
        : "il ne tient pas un détail de moins de " + vg(m.res_z, 2) + " mm dans l'épaisseur";
    case "tol":
      return v >= m.tol ? null : "sa tolérance courante est de " + vg(m.tol, 2) + " mm";
    case "traversant":
      return (m.traversant || !v) ? null : "il ne perce pas";
    case "borgne":
      return (m.borgne || !v) ? null : "il ne fait pas de trou borgne";
  }
  return null;
}

function juge(m){
  const rates = [];
  if(m.matieres.indexOf(PIECE.matiere) < 0) rates.push("il n'accepte pas le " + PIECE.matiere);
  TRAITS.forEach(t => { const r = tientTrait(m, t, cote(t)); if(r) rates.push(r); });
  return rates;
}

/* Combien de cotes ont été touchées alors qu'elles n'en avaient pas besoin ? */
function touchesInutiles(){
  if(!EDIT) return [];
  return TRAITS.filter(t => t.sansCorrection && Math.abs(cote(t) - t.valeur) > 1e-9);
}

function majAtelier(geste){
  const n = quantite();
  /* L'état de chaque trait. Quand le cahier des charges a DÉJÀ retenu un moyen
     — c'est le cas du boîtier, choisi en 3e_C7.3 — la colonne se lit pour lui,
     et pour lui seul : « trois cotes bloquent » n'a de sens que rapporté à une
     machine précise. Sinon, on dit si au moins un moyen sait la produire. */
  const CIBLE = PIECE.moyenVise ? MOYENS.filter(m => m.cle === PIECE.moyenVise)[0] : null;
  TRAITS.forEach(t => {
    const li = document.getElementById("li_" + t.cle), et = document.getElementById("et_" + t.cle);
    let bloque;
    if(CIBLE) bloque = tientTrait(CIBLE, t, cote(t)) !== null;
    else bloque = MOYENS.every(m => tientTrait(m, t, cote(t)) !== null);
    li.classList.toggle("ko", bloque);
    li.classList.toggle("ok", !bloque);
    li.classList.toggle("touche", EDIT && Math.abs(cote(t) - t.valeur) > 1e-9);
    et.textContent = bloque ? "✘" : "✔";
  });

  const tb = document.getElementById("tab");
  while(tb.rows.length > 1) tb.deleteRow(1);
  let retenus = [], dansLesTemps = 0;
  MOYENS.forEach(m => {
    const rates = juge(m), ok = rates.length === 0;
    const t = m.prep + n * m.min_piece, tient = t <= PIECE.tempsDispo;
    if(ok){ retenus.push(m); if(tient) dansLesTemps++; }
    const tr = tb.insertRow();
    tr.className = ok ? "ok" : "ko";
    const cel = x => { const d = tr.insertCell(); d.innerHTML = x; return d; };
    cel("<b>" + m.nom + "</b>").className = "nom";
    const c = cel(duree(t) + (tient ? "" : " <b>✗</b>"));
    c.className = "t" + (tient ? "" : " hors");
    cel(ok ? m.empreinte : "—").className = "emp";
    cel(ok ? "✔ capable" : "✘ " + rates.join(" · ")).className = "ver";
  });

  const jR = document.getElementById("jRet");
  document.getElementById("nRet").textContent = retenus.length;
  jR.classList.toggle("zero", retenus.length === 0);
  jR.classList.toggle("un", retenus.length === 1);
  jR.classList.toggle("plus", retenus.length > 1);

  const j2 = document.getElementById("j2");
  if(EDIT){
    const inut = touchesInutiles().length;
    document.getElementById("nInutile").textContent = inut;
    j2.classList.toggle("zero", inut > 0);
    j2.classList.toggle("bon", inut === 0);
  } else {
    document.getElementById("nDelai").textContent = dansLesTemps;
    j2.classList.toggle("zero", dansLesTemps === 0);
    j2.classList.toggle("un", dansLesTemps === 1);
    j2.classList.toggle("plus", dansLesTemps > 1);
  }

  if(geste){
    if(retenus.length === 0) window.__exp.zero = true;
    if(retenus.length === 1) window.__exp.unSeul = true;
    if(retenus.length > 1) window.__exp.plusieurs = true;
    if(EDIT && TRAITS.some(t => Math.abs(cote(t) - t.valeur) > 1e-9)) window.__exp.corrige = true;
    if(!EDIT && n !== parseInt(document.getElementById("qte").options[0].value, 10))
      window.__exp.quantite = true;
    if(dansLesTemps < retenus.length) window.__exp.horsDelai = true;
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
  const r = majAtelier(true), n = quantite();
  window.__exp.evalue = true;
  if(!r.length){
    ligne("ko", "Aucun moyen de l'atelier ne sait produire cette forme. Ce n'est pas une panne : "
        + "c'est un résultat. Regarde quelles lignes du dessin portent une croix.");
  } else {
    const hors = r.filter(m => m.prep + n * m.min_piece > PIECE.tempsDispo);
    ligne("ok", r.length + " moyen(s) savent la produire : " + r.map(m => m.nom).join(" · "));
    if(hors.length)
      ligne("wa", "Mais pour " + n + " pièces, " + hors.length + " d'entre eux dépassent les "
          + duree(PIECE.tempsDispo) + " de machine disponibles : " + hors.map(m => m.nom).join(" · "));
  }
  if(EDIT){
    const inut = touchesInutiles();
    if(inut.length)
      ligne("wa", inut.length + " cote(s) modifiée(s) sans nécessité : " + inut.map(t => t.lib).join(" · ")
          + ". Elles passaient déjà.");
  }
  save();
});
document.getElementById("reinit").addEventListener("click", () => {
  if(EDIT) TRAITS.forEach(t => {
    document.getElementById("tr_" + t.cle).value = String(t.valeur).replace(".", ",");
  });
  const q = document.getElementById("qte");
  q.value = q.options[0].value;
  majAtelier(true);
  ligne("wa", "Dessin remis tel qu'il sort de la modélisation.");
});
if(EDIT) TRAITS.forEach(t => {
  const e = document.getElementById("tr_" + t.cle);
  if(e) e.addEventListener("input", () => majAtelier(true));
});
document.getElementById("qte").addEventListener("change", () => majAtelier(true));
/* Pas d'appel à majAtelier() ici : il enregistre, et il tournerait AVANT
   restore() (règle d'or n°221). Le squelette restaure d'abord, puis met à jour.
   Et l'appel du squelette ne passe AUCUN geste : un verrou que l'ouverture de
   la page suffit à ouvrir n'est pas un verrou (règle d'or n°226). */
__JS_EN_PLUS__
"""
