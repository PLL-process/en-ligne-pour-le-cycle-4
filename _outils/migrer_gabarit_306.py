#!/usr/bin/env python3
"""migrer_gabarit_306.py — une page de l'ancien gabarit rejoint le squelette commun.

POURQUOI (V2 de la boucle d'audit, 07/11/2026)
-----------------------------------------------
L'audit a trouvé une famille de dix-neuf pages (3e/4e/5e C7.3 → C7.8, C8.1, C8.2, plus
4e_C6.2 et 5e_C1.5) passées aux onglets le 04/11 mais restées sur l'ancien gabarit :
elles tombent ensemble sur quatre règles d'or — n°29 (pas de mode essentiel), n°30 (pas
de tableau de bord des tâches), n°31 (aucune version étayée), n°34 (champs sans
étiquette) — et portent leurs questions en listes déroulantes (n°300). Ce script fait,
page par page et de façon rejouable, ce que ces cinq règles demandent ; ce qu'il ne sait
pas faire seul (le CONTENU des versions étayées), il le lit dans un fichier JSON écrit à
la main à côté de la page.

CE QU'IL FAIT
-------------
  n°300  chaque <select> qui pose une question (les menus voulus par les n°317/318 sont
         laissés : cahier des charges `…cdcf…`, bête à cornes `bc_…__aqui|…`, `bac_…` ; et
         une LISTE D'INTERFACE — un choix de port sur un établi, 16 entrées identiques
         sur dix champs — marquée `data-interface` dans la page, n'est pas une question :
         la n°300 l'annonçait le 20/09/2026, « elle mérite d'être discutée », décision
         pour Pascal au journal de V2)
         devient un <fieldset class="qcm-groupe" id="X"> : l'énoncé va dans la <legend>
         (un <label for="X"> ou le <p> qui précède immédiatement ; sinon le script
         REFUSE la page et nomme le champ — on ne devine pas un énoncé), chaque
         proposition devient un bouton radio dont la valeur est le TEXTE de la
         proposition, l'invite (« — je choisis — ») disparaît. Le groupe porte sa
         valeur (propriété `value` sur HTMLFieldSetElement.prototype, leçon de la vague
         du 20/09/2026) : `sv()`, `save()`, `restore()` continuent de lire `.value`.
         `save()` apprend à sauvegarder le groupe et non ses boutons ;
         `p.selectedIndex = n` sur #pos (lecture des anciennes réponses) devient le
         n-ième bouton coché.
  n°29   bouton « 🎯 Mode essentiel » dans la barre, CSS `body.essentiel`, bascule
         sauvegardée dans `window.__exp.mode_essentiel`.
  n°30   bandeau #tachesBandeau sous la barre d'onglets : une ligne par activité
         vérifiable, barrée quand elle a été validée (`window.__exp.valides[n]`, posé
         par le vérificateur et sauvegardé avec le reste).
  n°31   après chaque <textarea> de rédaction (hors #hyp, l'hypothèse n'est pas une
         production exigée), un <details class="etayage"> dont les phrases viennent du
         fichier `etayage_<page>.json` : {"id du textarea": ["phrase à compléter…", …]}.
         Sans fichier, ou sans entrée pour un textarea, le script REFUSE la page.
  n°34   chaque <textarea> sans étiquette reçoit un `aria-label` : son placeholder, ou
         le texte du <p> qui précède.

    python3 _outils/migrer_gabarit_306.py <page.html> [--etat]
Il s'arrête sans écrire au premier doute ; il est rejouable (une page déjà migrée ne
bouge plus).
"""
import html as html_mod
import json
import os
import re
import sys

MENU_VOULU_ID = re.compile(r"(?:^|_)cdcf(?:_|$)|^bc_[^\"]*__(?:aqui|surquoi|objet|but)$|^bac_", re.I)

PROTO = """<script>
/* Règle d'or n°300 — le groupe porte sa valeur (vague du 20/09/2026) : tout ce qui
   lisait ou écrivait `champ.value` sur l'ancienne liste déroulante continue de
   fonctionner sur le groupe de boutons radio, sans être touché. */
(function(){
  if (Object.getOwnPropertyDescriptor(HTMLFieldSetElement.prototype, "value")) return;
  Object.defineProperty(HTMLFieldSetElement.prototype, "value", {
    configurable: true,
    get: function(){
      if (!this.classList.contains("qcm-groupe")) return undefined;
      var c = this.querySelector("input[type=radio]:checked");
      return c ? c.value : "";
    },
    set: function(v){
      if (!this.classList.contains("qcm-groupe")) return;
      this.querySelectorAll("input[type=radio]").forEach(function(r){ r.checked = (r.value === v); });
    }
  });
})();
</script>
"""

CSS_QCM = """
  /* Règle d'or n°300 — une question se lit pendant qu'on y répond : groupe de boutons radio */
  .qcm-groupe{margin:10px 0 14px;padding:0 0 0 11px;min-width:0;border:0;
    border-left:3px solid var(--border);border-radius:0;background:none}
  .qcm-groupe legend{display:block;width:100%;padding:0;margin:0 0 6px;font-weight:600}
  .qcm-groupe .qcm-option{display:flex;align-items:flex-start;gap:9px;margin:5px 0;
    padding:7px 9px;border:2px solid transparent;border-radius:9px;background:var(--panel2,#0a1b3d)}
  .qcm-groupe .qcm-option:hover,.qcm-groupe .qcm-option:focus-within{border-color:var(--hl)}
  .qcm-groupe .qcm-option input[type=radio]{width:19px;height:19px;margin:1px 0 0;flex-shrink:0;accent-color:var(--hl)}
  .qcm-groupe .qcm-option label{display:block;margin:0;flex:1;cursor:pointer}
  .qcm-groupe.ok{border-left-color:var(--ok)}.qcm-groupe.ko{border-left-color:var(--err)}
  @media print{.qcm-groupe,.qcm-groupe .qcm-option{background:#fff!important;border-color:#999!important;box-shadow:none!important}
    .qcm-groupe legend,.qcm-groupe .qcm-option label{color:#111!important}}
"""

CSS_306 = """
  /* Règle d'or n°29 — mode essentiel : les corrections et les compléments se masquent, rien ne se perd */
  body.essentiel details.correction,body.essentiel .approfondissement,body.essentiel .bonus-complement{display:none}
  /* Règle d'or n°30 — la barre compte, ce bandeau situe */
  #tachesBandeau{max-width:940px;margin:10px auto 14px;padding:9px 15px;background:var(--panel,#0d2347);
    border:1px solid var(--border);border-radius:10px;font-size:.92em;line-height:1.55}
  #tachesBandeau .tb-titre{font-weight:700;color:var(--hl);display:block;margin-bottom:3px}
  #tachesBandeau ul{list-style:none;margin:0;padding:0}
  #tachesBandeau li.faite{opacity:.6;text-decoration:line-through}
  /* Règle d'or n°31 — version étayée : des phrases à compléter, repliées */
  details.etayage{margin:8px 0 12px;padding:6px 12px;border-left:4px solid var(--hl);border-radius:8px}
  details.etayage summary{cursor:pointer;color:var(--hl);font-weight:600}
  details.etayage ul{margin:6px 0;padding-left:22px}details.etayage li{margin:5px 0}
  @media print{#tachesBandeau{display:none}details.etayage{border-color:#999!important}details.etayage summary{color:#047fa0!important}}
"""

JS_306 = """
/* ══ Règle d'or n°29 — mode essentiel (gabarit commun, V2 du 07/11/2026) ══ */
function majEssentiel(){ const b=$("btnEssentiel"); if(!b) return;
  const on=document.body.classList.contains("essentiel");
  b.textContent = on ? "🎯 Mode essentiel : ON" : "🎯 Mode essentiel : OFF";
  b.setAttribute("aria-pressed", on ? "true" : "false"); }
if($("btnEssentiel")) $("btnEssentiel").addEventListener("click", () => {
  document.body.classList.toggle("essentiel");
  (window.__exp = window.__exp || {})["mode_essentiel"] = document.body.classList.contains("essentiel") ? 1 : 0;
  majEssentiel(); save(); });
/* ══ Règle d'or n°30 — le bandeau des tâches : une ligne par activité, barrée quand elle est validée ══ */
function majBandeau(){ const b=$("tachesBandeau"); if(!b) return; const ul=b.querySelector("ul"); if(!ul) return;
  const v=(window.__exp||{}).valides||{}; let faites=0;
  ul.querySelectorAll("li").forEach(li => { const ok=!!v[li.dataset.check]; li.classList.toggle("faite", ok); if(ok) faites++;
    li.querySelector(".tb-etat").textContent = ok ? "✔" : "○"; });
  const c=b.querySelector(".tb-compte"); if(c) c.textContent = faites + " / " + ul.children.length + " validée(s)"; }
window.__exp = window.__exp || {};
if(window.__exp["mode_essentiel"]) document.body.classList.add("essentiel");
majEssentiel(); majBandeau();
"""


def refus(msg):
    raise SystemExit("REFUS — " + msg)


def texte(h):
    return re.sub(r"\s+", " ", html_mod.unescape(re.sub(r"<[^>]+>", "", h))).strip()


def convertir_selects(t, page):
    """n°300 : chaque <select> qui pose une question devient un groupe de boutons radio."""
    faits, laisses = [], []
    deja = set()
    while True:
        # on recherche À CHAQUE TOUR : les positions bougent après chaque remplacement
        m = None
        for cand in re.finditer(r"<select\b([^>]*)>(.*?)</select>", t, re.S):
            mid = re.search(r'\bid="([^"]+)"', cand.group(1))
            if not mid:
                refus("%s : un <select> sans id (%s…)" % (page, cand.group(1)[:60]))
            if MENU_VOULU_ID.search(mid.group(1)) or "data-interface=" in cand.group(1):
                if mid.group(1) not in deja:
                    laisses.append(mid.group(1)); deja.add(mid.group(1))
                continue
            m = cand
            break
        if m is None:
            break
        attrs, corps = m.group(1), m.group(2)
        sid = re.search(r'\bid="([^"]+)"', attrs).group(1)
        options = re.findall(r"<option\b([^>]*)>(.*?)</option>", corps, re.S)
        # Pas d'invite (aucune <option value="">) : le menu a une valeur dès l'ouverture — c'est une
        # COMMANDE de simulateur (la source d'énergie de 3e_C7.4, le profilé de 3e_C8.2), lue par le
        # code de la page comme une clé, pas une question posée à l'élève. On la laisse, marquée
        # `data-interface="commande"` pour que le contrôle n°300 la compte à part.
        if not any(re.search(r'\bvalue=""', oa) for oa, _ in options):
            t = t[:m.start()] + '<select data-interface="commande"' + attrs + ">" + corps + "</select>" + t[m.end():]
            laisses.append(sid); deja.add(sid)
            continue
        props = []
        for oa, ot in options:
            ov = re.search(r'\bvalue="([^"]*)"', oa)
            if ov is not None and ov.group(1) == "":
                continue                       # l'invite
            val = ov.group(1) if ov else texte(ot)
            props.append((val, re.sub(r"\s+", " ", ot).strip()))
        if not props:
            refus("%s : #%s n'a aucune proposition" % (page, sid))
        # l'énoncé : un <label for=X> n'importe où, sinon le <p> qui précède immédiatement
        enonce, retirer = None, None
        ml = re.search(r'<label\b[^>]*\bfor="%s"[^>]*>(.*?)</label>\s*' % re.escape(sid), t, re.S)
        if ml:
            enonce, retirer = ml.group(1).strip(), ml.group(0)
        else:
            avant = t[:m.start()]
            mp = re.search(r"<p\b([^>]*)>((?:(?!</p>).)*)</p>\s*$", avant, re.S)
            if mp:
                enonce, retirer = mp.group(2).strip(), mp.group(0)
        if not enonce:
            aria = re.search(r'\baria-label="([^"]+)"', attrs)
            if aria:
                enonce = aria.group(1)
            else:
                refus("%s : impossible de lire l'énoncé de #%s (ni <label for>, ni <p> juste avant) — à écrire à la main" % (page, sid))
        lignes = ['<fieldset class="qcm-groupe" id="%s">' % sid, "  <legend>%s</legend>" % enonce]
        for n, (val, lib) in enumerate(props, 1):
            vesc = html_mod.escape(val, quote=True)
            lignes.append('  <div class="qcm-option"><input type="radio" name="%s" id="%s__%d" value="%s"><label for="%s__%d">%s</label></div>'
                          % (sid, sid, n, vesc, sid, n, lib))
        lignes.append("</fieldset>")
        bloc = "\n".join(lignes)
        # remplacer : le select, puis l'énoncé retiré (qui le précède ou vit ailleurs)
        t = t[:m.start()] + "@@SELECT_%s@@" % sid + t[m.end():]
        if retirer:
            if retirer in t[:t.find("@@SELECT_%s@@" % sid)] or ml:
                t = t.replace(retirer, "", 1)
            else:
                refus("%s : énoncé de #%s introuvable au moment de le retirer" % (page, sid))
        t = t.replace("@@SELECT_%s@@" % sid, bloc, 1)
        faits.append((sid, len(props)))
    return t, faits, laisses


def poser_proto_css(t):
    if "HTMLFieldSetElement.prototype" not in t:
        i = t.find("<script")
        t = t[:i] + PROTO + t[i:]
    # la feuille des groupes est reconnue à sa règle d'écran NON limitée à #billet ; une règle
    # d'impression (`.qcm-groupe{border:0!important…}` de la fiche papier) ne compte pas
    if not re.search(r"\n\s*\.qcm-groupe \.qcm-option\{display:flex", t):
        t = t.replace("</style>", CSS_QCM + "</style>", 1)
    if "#tachesBandeau{" not in t:
        t = t.replace("</style>", CSS_306 + "</style>", 1)
    return t


def patcher_save(t, page):
    old = 'document.querySelectorAll("input, select, textarea").forEach(e => {\n    if(!e.id) return;'
    new = ('document.querySelectorAll("input, select, textarea, fieldset.qcm-groupe").forEach(e => {\n    if(!e.id) return;\n'
           '    if(e.type === "radio" && e.closest(".qcm-groupe")) return;   // n°300 : le groupe porte sa valeur, pas ses boutons')
    old2 = 'document.querySelectorAll("input, select, textarea").forEach(e => { if(e.id) o.inputs[e.id] = e.value; });'
    new2 = ('document.querySelectorAll("input, select, textarea, fieldset.qcm-groupe").forEach(e => { if(!e.id) return;\n'
            '    if(e.type === "radio" && e.closest(".qcm-groupe")) return;   // n°300 : le groupe porte sa valeur, pas ses boutons\n'
            '    o.inputs[e.id] = e.value; });')
    if "fieldset.qcm-groupe" in t[t.find("function save("):t.find("function save(") + 600]:
        return t
    if old in t:
        t = t.replace(old, new, 1)
    elif old2 in t:
        t = t.replace(old2, new2, 1)
    else:
        refus("%s : save() n'a pas la forme attendue — à migrer à la main" % page)
    # #pos : les anciennes réponses se relisaient par selectedIndex ; sur un groupe, on coche le n-ième bouton
    t = re.sub(r"p\.selectedIndex = ANCIEN_POS\[vp\];",
               'p.querySelectorAll("input[type=radio]")[ANCIEN_POS[vp]-1].checked = true;', t)
    return t


def poser_essentiel(t, page):
    if 'id="btnEssentiel"' in t:
        return t
    m = re.search(r'<div class="toolbar">(.*?)</div>', t, re.S)
    if not m:
        refus("%s : pas de barre d'outils" % page)
    bouton = ('\n  <button class="btn ghost" id="btnEssentiel" type="button" aria-pressed="false" '
              'title="Masquer les corrections et les compléments, pour ne garder que les consignes et les exercices. Un second clic ramène tout.">🎯 Mode essentiel : OFF</button>\n')
    t = t[:m.end() - 6] + bouton + t[m.end() - 6:]
    return t


def poser_bandeau(t, page):
    if 'id="tachesBandeau"' in t:
        return t
    boutons = re.findall(r'<button class="btn(?: check)?" data-check="([^"]+)"[^>]*>(.*?)</button>', t, re.S)
    if len(boutons) < 2:
        return t
    lis = "".join('    <li data-check="%s"><span class="tb-etat">○</span> %s</li>\n' % (n, texte(lib).replace("✅ ", "")) for n, lib in boutons)
    bandeau = ('<div id="tachesBandeau" aria-live="polite" aria-atomic="true">\n'
               '  <span class="tb-titre">📋 Où j\'en suis <span class="tb-compte"></span></span>\n  <ul>\n' + lis + '  </ul>\n</div>\n')
    m = re.search(r'<(nav|div) class="seance-tabs"[^>]*>.*?</\1>\s*', t, re.S)
    if not m:
        refus("%s : pas de barre d'onglets où accrocher le bandeau" % page)
    t = t[:m.end()] + bandeau + t[m.end():]
    # le vérificateur mémorise la validation
    old = 'fb.className = "feedback show ok";'
    if old not in t:
        refus("%s : le vérificateur n'a pas la forme attendue (feedback show ok)" % page)
    t = t.replace(old, 'fb.className = "feedback show ok"; (window.__exp.valides = window.__exp.valides || {})[n] = 1; majBandeau();', 1)
    return t


def poser_js(t, page):
    if "function majEssentiel(" in t:
        return t
    i = t.find("function save(")
    j = t.find("})();\n</script>", i)
    if j < 0:
        refus("%s : fin du script principal introuvable" % page)
    return t[:j] + JS_306 + t[j:]


def poser_etayage(t, page, chemin_json):
    if not os.path.exists(chemin_json):
        refus("%s : pas de fichier %s pour les versions étayées" % (page, os.path.basename(chemin_json)))
    phrases = json.load(open(chemin_json, encoding="utf-8"))
    faits = []
    # du DERNIER au premier : une insertion ne décale que ce qui suit, jamais ce qui précède
    for m in reversed(list(re.finditer(r"<textarea\b([^>]*)>.*?</textarea>", t, re.S))):
        mid = re.search(r'\bid="([^"]+)"', m.group(1))
        if not mid:
            refus("%s : un <textarea> sans id" % page)
        tid = mid.group(1)
        if tid == "hyp":
            continue
        apres = t[m.end():m.end() + 300]
        if 'class="etayage"' in apres:
            continue
        if tid not in phrases:
            refus("%s : aucune version étayée pour #%s dans %s" % (page, tid, os.path.basename(chemin_json)))
        lis = "".join("<li>« %s »</li>" % html_mod.escape(p, quote=False) for p in phrases[tid])
        bloc = ('\n<details class="etayage"><summary>🪜 Version étayée — des phrases à compléter</summary>'
                '<p>Le niveau attendu est <b>le même</b> : ces phrases donnent le départ, pas la réponse.</p><ul>%s</ul></details>' % lis)
        t = t[:m.end()] + bloc + t[m.end():]
        faits.append(tid)
    return t, faits


def etiqueter_textareas(t, page):
    faits = []
    for m in reversed(list(re.finditer(r"<textarea\b([^>]*)>", t))):   # du dernier au premier, même raison
        attrs = m.group(1)
        mid = re.search(r'\bid="([^"]+)"', attrs)
        if not mid or "aria-label" in attrs or "aria-labelledby" in attrs:
            continue
        tid = mid.group(1)
        if re.search(r'<label\b[^>]*\bfor="%s"' % re.escape(tid), t):
            continue
        ph = re.search(r'\bplaceholder="([^"]+)"', attrs)
        if ph:
            lib = ph.group(1)
        else:
            avant = t[:m.start()]
            mp = re.search(r"<p\b[^>]*>((?:(?!</p>).)*)</p>\s*(?:<[^>]+>\s*)*$", avant, re.S)
            lib = texte(mp.group(1))[:140] if mp else None
        if not lib:
            refus("%s : #%s sans étiquette possible (ni placeholder, ni <p> avant)" % (page, tid))
        t = t[:m.start()] + '<textarea aria-label="%s"%s>' % (html_mod.escape(lib, quote=True), attrs) + t[m.end():]
        faits.append(tid)
    return t, faits


def migrer(chemin, etat):
    page = os.path.basename(chemin)
    t = open(chemin, encoding="utf-8").read()
    t, selects, laisses = convertir_selects(t, page)
    t = poser_proto_css(t)
    t = patcher_save(t, page)
    t = poser_essentiel(t, page)
    t = poser_bandeau(t, page)
    t = poser_js(t, page)
    t, etayes = poser_etayage(t, page, os.path.join(os.path.dirname(chemin), "etayage_%s.json" % re.sub(r"\.html$", "", page)))
    t, etiquetes = etiqueter_textareas(t, page)
    if not etat:
        open(chemin, "w", encoding="utf-8").write(t)
    print("%s %s : %d liste(s) → groupes (%d propositions), %d menu(s) voulu(s) laissé(s), %d version(s) étayée(s), %d étiquette(s)"
          % ("À MIGRER" if etat else "MIGRÉE", page, len(selects), sum(n for _, n in selects), len(laisses), len(etayes), len(etiquetes)))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for a in args:
        migrer(a, "--etat" in sys.argv)
