#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesures_rendu.py — ce que les skills de design demandent de vérifier sur la page OUVERTE.

Audit du 26/11/2026. Chaque page vivante est ouverte dans Chromium (Playwright), telle qu'elle s'affiche au
chargement : ce qui est replié ou dans un autre onglet n'est PAS mesuré, et le rapport le dit.

À 1 280 px :
  · noms accessibles : contrôles qui prennent le focus et n'ont aucun nom (arbre d'accessibilité de Chromium) ;
  · souris seulement : éléments au curseur « main » qui ne sont ni natifs ni atteignables au clavier ;
  · parcours au clavier (60 arrêts de Tab au plus) : focus sans indicateur visible, focus caché sous une barre collante ;
  · texte : caractères par ligne des paragraphes, interligne des textes de 3 lignes et plus, texte sous 12 px.
À 390 px puis 320 px, écran tactile :
  · défilement horizontal de la page ; cibles sous 24 × 24 px (critère 2.5.8) ; hauteur de la page en écrans.

Rien n'est modifié. Usage : python3 mesures_rendu.py <racine du dépôt> --json sortie.json [--filtre motif] [--procs 2] [--eleve]
--eleve : la page s'ouvre comme pour un élève, mode mission allumé. Sans lui, elle s'ouvre comme pour un robot : la page complète.
Code de sortie (n°299) : 0 mesures faites · 2 aucune page mesurée.
"""
import argparse, json, statistics, sys, time
from multiprocessing import Pool
from pathlib import Path

JS_OUTILS = r"""
() => {
  const NATIF = 'a[href],button,input,select,textarea,summary,label,[tabindex],[role=button],[role=tab],[role=link],[role=checkbox],[role=radio],[contenteditable],details>summary,audio[controls],video[controls]';
  // Un <details> fermé garde des boîtes de mise en page (content-visibility) : la taille seule ne dit pas « visible ».
  const visible = el => { const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && el.checkVisibility({ visibilityProperty: true, contentVisibilityAuto: true }); };
  const nom = el => (el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.classList.length ? '.' + [...el.classList].slice(0, 2).join('.') : '')).slice(0, 60);
  window.__audit = { NATIF, visible, nom,
    sig: el => { if (!el || el.nodeType !== 1) return ''; const c = getComputedStyle(el);
      return [c.outlineStyle, c.outlineWidth, c.outlineColor, c.boxShadow, c.borderTopColor, c.borderBottomColor, c.backgroundColor, c.textDecorationLine, c.color, c.borderTopWidth].join('|'); } };
  return true;
}
"""

JS_SOURIS_SEULE = r"""
() => { const A = window.__audit, out = {};
  for (const el of document.body.querySelectorAll('*')) {
    if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') continue;
    const cs = getComputedStyle(el);
    if (cs.cursor !== 'pointer' || !A.visible(el)) continue;
    if (el.matches(A.NATIF) || el.closest(A.NATIF) || el.querySelector(A.NATIF)) continue;
    if (el.parentElement && getComputedStyle(el.parentElement).cursor === 'pointer') continue;
    const k = A.nom(el).replace(/#[^.]+/, ''); out[k] = (out[k] || 0) + 1; }
  return out; }
"""

JS_TEXTE = r"""
() => { const A = window.__audit; const cpl = [], serre = {}, petit = {};
  for (const el of document.querySelectorAll('main p, main li, body > p, article p, article li, section p, section li')) {
    if (!A.visible(el) || el.closest('svg,pre,code,table')) continue;
    const t = el.innerText.trim(); if (t.length < 100) continue;
    const cs = getComputedStyle(el); const fs = parseFloat(cs.fontSize);
    const lh = cs.lineHeight === 'normal' ? fs * 1.2 : parseFloat(cs.lineHeight);
    const lignes = Math.round(el.getBoundingClientRect().height / lh);
    if (lignes >= 2) cpl.push(Math.round(t.length / lignes));
    if (lignes >= 3 && lh / fs < 1.39) { const k = A.nom(el).replace(/#[^.]+/, ''); serre[k] = (serre[k] || 0) + 1; } }
  const marche = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n; while ((n = marche.nextNode())) { const el = n.parentElement;
    if (!el || !n.nodeValue.trim() || n.nodeValue.trim().length < 3) continue;
    if (el.closest('svg,script,style,noscript,sup,sub') || !A.visible(el)) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs < 12) { const k = A.nom(el).replace(/#[^.]+/, '') + ' ' + fs + 'px'; petit[k] = (petit[k] || 0) + 1; } }
  return { cpl, serre, petit }; }
"""

JS_ARRET = r"""
(base) => { const A = window.__audit; const el = document.activeElement;
  if (!el || el === document.body || el === document.documentElement) return null;
  const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
  const voisins = [el, el.labels && el.labels[0], el.parentElement, el.nextElementSibling, el.previousElementSibling].filter(Boolean);
  const cle = e => { if (!e.dataset.auditId) e.dataset.auditId = String(++window.__auditN); return e.dataset.auditId; };
  window.__auditN = window.__auditN || 0;
  let indique = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0);
  const avant = window.__auditBase || {};
  for (const v of voisins) { const k = v.dataset.auditId; if (k && avant[k] !== undefined && avant[k] !== A.sig(v)) indique = true; }
  if (voisins.some(v => { const c = getComputedStyle(v); return v !== el && c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0; })) indique = true;
  let cache = null;
  if (r.width > 0 && r.height > 0) { const cx = Math.min(Math.max(r.left + r.width / 2, 1), innerWidth - 1), cy = Math.min(Math.max(r.top + Math.min(r.height / 2, 12), 1), innerHeight - 1);
    const dessus = document.elementFromPoint(cx, cy);
    if (dessus && dessus !== el && !el.contains(dessus) && !dessus.contains(el) && !(el.labels && [...el.labels].some(l => l.contains(dessus)))) {
      let p = dessus; while (p && p !== document.body) { const pos = getComputedStyle(p).position; if (pos === 'fixed' || pos === 'sticky') { cache = A.nom(p); break; } p = p.parentElement; } } }
  return { nom: A.nom(el).replace(/#[^.]+/, ''), texte: (el.innerText || el.value || el.getAttribute('aria-label') || '').trim().slice(0, 30), indique, cache, vu: r.width > 0 && r.height > 0, id: cle(el) }; }
"""

JS_BASE = r"""
() => { const A = window.__audit; window.__auditN = window.__auditN || 0; const base = {};
  const pose = e => { if (!e || e.nodeType !== 1) return; if (!e.dataset.auditId) e.dataset.auditId = String(++window.__auditN); base[e.dataset.auditId] = A.sig(e); };
  for (const el of document.querySelectorAll('a[href],button,input,select,textarea,summary,[tabindex]')) {
    pose(el); if (el.labels && el.labels[0]) pose(el.labels[0]); pose(el.parentElement); pose(el.nextElementSibling); pose(el.previousElementSibling); }
  window.__auditBase = base; return Object.keys(base).length; }
"""

JS_MOBILE = r"""
() => { const A = window.__audit; const petites = {};
  for (const el of document.querySelectorAll('a[href],button,input:not([type=hidden]),select,summary,[role=button],[role=tab]')) {
    if (!A.visible(el)) continue;
    if (el.tagName === 'A' && el.closest('p,li,td,dd,figcaption') && getComputedStyle(el).display.startsWith('inline')) continue;  // lien dans une phrase : exempté par 2.5.8
    let r = el.getBoundingClientRect();
    if ((el.type === 'radio' || el.type === 'checkbox') && el.labels && el.labels[0]) r = el.labels[0].getBoundingClientRect();
    if (r.width < 24 || r.height < 24) { const k = A.nom(el).replace(/#[^.]+/, '') + ' ' + Math.round(r.width) + '×' + Math.round(r.height); petites[k] = (petites[k] || 0) + 1; } }
  let large = null, max = 0;
  if (document.documentElement.scrollWidth > innerWidth + 1) for (const el of document.body.querySelectorAll('*')) {
    const r = el.getBoundingClientRect(); if (r.right > max && r.width > 0 && getComputedStyle(el).position !== 'fixed') { max = r.right; large = A.nom(el) + ' → ' + Math.round(r.right) + 'px'; } }
  return { petites, deborde: document.documentElement.scrollWidth - innerWidth, large, hauteur: document.documentElement.scrollHeight }; }
"""


def mesurer_page(page_ctx, ctx_mobile, chemin, racine):
    rel = str(chemin.relative_to(racine))
    url = chemin.resolve().as_uri()
    r = dict(page=rel)
    page = page_ctx.new_page()
    try:
        page.goto(url, wait_until="load", timeout=30000)
        page.wait_for_timeout(250)
        if page.url.split("#")[0] != url:
            r["renvoi"] = page.url.rsplit("/", 1)[-1][:80]
            return r
        page.evaluate(JS_OUTILS)
        # noms accessibles
        cdp = page.context.new_cdp_session(page)
        arbre = cdp.send("Accessibility.getFullAXTree")["nodes"]
        sans_nom = {}
        for n in arbre:
            if n.get("ignored"):
                continue
            role = (n.get("role") or {}).get("value", "")
            if role not in ("button", "link", "textbox", "combobox", "checkbox", "radio", "slider", "tab", "switch", "searchbox", "spinbutton", "listbox", "menuitem"):
                continue
            focusable = any(p.get("name") == "focusable" and (p.get("value") or {}).get("value") for p in n.get("properties", []))
            if focusable and not ((n.get("name") or {}).get("value") or "").strip():
                sans_nom[role] = sans_nom.get(role, 0) + 1
        r["sans_nom"] = sans_nom
        r["souris_seule"] = page.evaluate(JS_SOURIS_SEULE)
        r["texte"] = page.evaluate(JS_TEXTE)
        # parcours au clavier
        page.evaluate(JS_BASE)
        arrets, vus = [], set()
        for _ in range(60):
            page.keyboard.press("Tab")
            a = page.evaluate(JS_ARRET, None)
            if a is None or a["id"] in vus:
                break
            vus.add(a["id"])
            arrets.append(a)
        r["arrets"] = len(arrets)
        r["premier"] = arrets[0]["texte"] if arrets else ""
        sans = {}
        caches = {}
        for a in arrets:
            if a["vu"] and not a["indique"]:
                sans[a["nom"]] = sans.get(a["nom"], 0) + 1
            if a["cache"]:
                caches[a["nom"] + " sous " + a["cache"]] = caches.get(a["nom"] + " sous " + a["cache"], 0) + 1
        r["focus_invisible"], r["focus_cache"] = sans, caches
    finally:
        page.close()
    page = ctx_mobile.new_page()
    try:
        page.goto(url, wait_until="load", timeout=30000)
        page.wait_for_timeout(250)
        page.evaluate(JS_OUTILS)
        m390 = page.evaluate(JS_MOBILE)
        page.set_viewport_size({"width": 320, "height": 640})
        page.wait_for_timeout(150)
        m320 = page.evaluate(JS_MOBILE)
        r["mobile"] = dict(petites=m390["petites"], deborde_390=m390["deborde"], large_390=m390["large"],
                           deborde_320=m320["deborde"], large_320=m320["large"], ecrans_390=round(m390["hauteur"] / 844, 1))
    finally:
        page.close()
    return r


def lot(args):
    racine, chemins, eleve = args
    from playwright.sync_api import sync_playwright
    res = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(viewport={"width": 1280, "height": 800}, locale="fr-FR")
        mob = nav.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True, device_scale_factor=2, locale="fr-FR")
        if eleve:  # mission.js ouvre la page complète à un robot (navigator.webdriver) : on se présente comme un élève
            for c_ in (ctx, mob):
                c_.add_init_script("Object.defineProperty(Navigator.prototype, 'webdriver', {get: () => false})")
        for c in chemins:
            try:
                res.append(mesurer_page(ctx, mob, Path(c), Path(racine)))
            except Exception as e:  # n°299 : une page non mesurée se dit
                res.append(dict(page=str(Path(c).relative_to(racine)), panne=str(e).splitlines()[0][:160]))
        nav.close()
    return res


def principal():
    ap = argparse.ArgumentParser()
    ap.add_argument("racine"); ap.add_argument("--json", required=True); ap.add_argument("--filtre", default=""); ap.add_argument("--procs", type=int, default=2)
    ap.add_argument("--eleve", action="store_true", help="ouvrir la page comme un élève (mode mission allumé), pas comme un robot")
    a = ap.parse_args()
    racine = Path(a.racine).resolve()
    pages = sorted(str(f) for f in racine.rglob("*.html")
                   if not any(part.startswith(("_archive", ".git", "node_modules", "_outils", "docs")) for part in f.relative_to(racine).parts)
                   and a.filtre in str(f))
    if not pages:
        print("PANNE — aucune page (code 2)"); return 2
    t0 = time.time()
    morceaux = [(str(racine), pages[i::a.procs], a.eleve) for i in range(a.procs)]
    with Pool(a.procs) as pool:
        res = [x for m in pool.map(lot, morceaux) for x in m]
    res.sort(key=lambda x: x["page"])
    Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    pannes = [x for x in res if "panne" in x]
    renvois = [x for x in res if "renvoi" in x]
    mesurees = [x for x in res if "arrets" in x]
    print(f"{len(res)} pages · {len(mesurees)} mesurées · {len(renvois)} renvois · {len(pannes)} pannes · {time.time() - t0:.0f} s")
    for x in pannes[:10]:
        print("  ✘", x["page"], "—", x["panne"])
    return 0 if mesurees else 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(principal())
