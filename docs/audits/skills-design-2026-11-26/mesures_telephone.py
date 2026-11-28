#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesures_telephone.py — second passage, à 390 px, écran tactile : ce que la lecture d'une séquence a fait chercher.

Né de la lecture de `5e_C3.1` au téléphone (26/11/2026) : un paragraphe de consignes centré sur six lignes, un bouton
flottant posé sur le texte, une barre du haut qui laisse voir le texte dessous, des titres vides. Ce script compte ces
défauts sur toutes les pages, au chargement (ce qui est replié n'est pas mesuré).

  · texte centré de 3 lignes et plus (better-typography : le texte d'interface s'aligne au début) ;
  · bouton ou panneau flottant (position fixe) posé sur la colonne de lecture ;
  · barre collante ou fixe du haut au fond translucide, sans flou ;
  · titres visibles et vides ; boutons visibles sans texte ;
  · page sombre sans `color-scheme: dark` (Web Interface Guidelines : barres de défilement et listes natives restent claires) ;
  · boutons à bascule dont le libellé porte l'état (« … : OFF ») et leur attribut `aria-pressed`.

Usage : python3 mesures_telephone.py <racine du dépôt> --json sortie.json [--filtre motif] [--procs 2] [--eleve]
--eleve : la page s'ouvre comme pour un élève, mode mission allumé. Sans lui, elle s'ouvre comme pour un robot : la page complète.
Code de sortie (n°299) : 0 mesures faites · 2 aucune page mesurée.
"""
import argparse, json, sys, time
from multiprocessing import Pool
from pathlib import Path

JS = r"""
() => { // Un <details> fermé garde des boîtes de mise en page (content-visibility) : la taille seule ne dit pas « visible ».
  const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && el.checkVisibility({ visibilityProperty: true, opacityProperty: true, contentVisibilityAuto: true }); };
  const nom = el => (el.tagName.toLowerCase() + (el.classList.length ? '.' + [...el.classList].slice(0, 2).join('.') : (el.id ? '#' + el.id : ''))).slice(0, 50);
  const centre = {}, flottant = {}, barre = {}, titres = {}, boutons = {}, bascules = {};
  for (const el of document.querySelectorAll('p, li, div, td, figcaption, summary')) {
    if (!vis(el) || el.closest('svg,table')) continue;
    const direct = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.nodeValue).join('').trim();
    if (direct.length < 60) continue;
    const cs = getComputedStyle(el); if (cs.textAlign !== 'center') continue;
    const fs = parseFloat(cs.fontSize); const lh = cs.lineHeight === 'normal' ? fs * 1.2 : parseFloat(cs.lineHeight);
    const lignes = Math.round(el.getBoundingClientRect().height / lh);
    if (lignes >= 3) { const k = nom(el) + ' ' + lignes + ' l.'; centre[nom(el)] = Math.max(centre[nom(el)] || 0, lignes); } }
  for (const el of document.body.querySelectorAll('*')) {
    const cs = getComputedStyle(el); if (cs.position !== 'fixed' && cs.position !== 'sticky') continue; if (!vis(el)) continue;
    const r = el.getBoundingClientRect();
    const haut = r.top <= 2 && r.width >= innerWidth * 0.9;
    if (haut) { const m = cs.backgroundColor.match(/rgba?\(([^)]+)\)/); const p = m ? m[1].split(',').map(parseFloat) : [0, 0, 0, 0];
      const alpha = p.length > 3 ? p[3] : 1; const flou = (cs.backdropFilter && cs.backdropFilter !== 'none') || (cs.webkitBackdropFilter && cs.webkitBackdropFilter !== 'none');
      if (alpha < 0.95 && !flou) barre[nom(el) + ' alpha ' + alpha] = 1; continue; }
    if (cs.position === 'fixed' && r.width < innerWidth * 0.8 && r.height >= 30 && r.width >= 40 && r.left > 40 && r.left < innerWidth - 60 && r.top > 60)
      flottant[nom(el) + ' ' + Math.round(r.width) + '×' + Math.round(r.height)] = 1; }
  for (const h of document.querySelectorAll('h1,h2,h3,h4,h5,h6')) if (vis(h) && !h.innerText.trim() && !h.querySelector('img[alt]:not([alt=""]),svg[aria-label]') && !h.getAttribute('aria-label')) titres[nom(h)] = (titres[nom(h)] || 0) + 1;
  for (const b of document.querySelectorAll('button')) { if (!vis(b)) continue;
    if (!b.innerText.trim() && !b.getAttribute('aria-label') && !b.getAttribute('title') && !b.querySelector('img[alt]:not([alt=""])')) boutons[nom(b)] = (boutons[nom(b)] || 0) + 1;
    if (/:\s*(ON|OFF)\b/.test(b.innerText)) bascules[nom(b) + ' aria-pressed=' + b.getAttribute('aria-pressed')] = 1; }
  const fond = getComputedStyle(document.body).backgroundColor.match(/[\d.]+/g).map(Number);
  const lum = (0.2126 * fond[0] + 0.7152 * fond[1] + 0.0722 * fond[2]) / 255;
  return { centre, flottant, barre, titres, boutons, bascules, sombre: lum < 0.25 && (fond[3] === undefined || fond[3] > 0.5), schema: getComputedStyle(document.documentElement).colorScheme,
           selects: [...document.querySelectorAll('select')].length }; }
"""


def lot(args):
    racine, chemins, eleve = args
    from playwright.sync_api import sync_playwright
    res = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True, device_scale_factor=1, locale="fr-FR")
        if eleve:  # mission.js ouvre la page complète à un robot (navigator.webdriver) : on se présente comme un élève
            ctx.add_init_script("Object.defineProperty(Navigator.prototype, 'webdriver', {get: () => false})")
        for c in chemins:
            rel = str(Path(c).relative_to(racine))
            page = ctx.new_page()
            try:
                url = Path(c).resolve().as_uri()
                page.goto(url, wait_until="load", timeout=30000)
                page.wait_for_timeout(250)
                if page.url.split("#")[0] != url:
                    res.append(dict(page=rel, renvoi=True))
                else:
                    r = page.evaluate(JS); r["page"] = rel; res.append(r)
            except Exception as e:  # n°299
                res.append(dict(page=rel, panne=str(e).splitlines()[0][:160]))
            finally:
                page.close()
        nav.close()
    return res


def principal():
    ap = argparse.ArgumentParser()
    ap.add_argument("racine"); ap.add_argument("--json", required=True); ap.add_argument("--filtre", default=""); ap.add_argument("--procs", type=int, default=2)
    ap.add_argument("--eleve", action="store_true", help="ouvrir la page comme un élève (mode mission allumé), pas comme un robot")
    a = ap.parse_args()
    racine = Path(a.racine).resolve()
    pages = sorted(str(f) for f in racine.rglob("*.html")
                   if not any(part.startswith(("_archive", ".git", "node_modules", "_outils", "docs")) for part in f.relative_to(racine).parts) and a.filtre in str(f))
    if not pages:
        print("PANNE — aucune page (code 2)"); return 2
    t0 = time.time()
    with Pool(a.procs) as pool:
        res = [x for m in pool.map(lot, [(str(racine), pages[i::a.procs], a.eleve) for i in range(a.procs)]) for x in m]
    res.sort(key=lambda x: x["page"])
    Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    mes = [x for x in res if "centre" in x]
    print(f"{len(res)} pages · {len(mes)} mesurées · {sum('renvoi' in x for x in res)} renvois · {sum('panne' in x for x in res)} pannes · {time.time() - t0:.0f} s")
    from collections import Counter, defaultdict
    for cle, titre in (("centre", "Texte centré de 3 lignes et plus"), ("flottant", "Élément flottant sur la colonne de lecture"), ("barre", "Barre du haut translucide, sans flou"),
                       ("titres", "Titres visibles et vides"), ("boutons", "Boutons visibles sans texte ni nom"), ("bascules", "Bascules au libellé « … : ON/OFF »")):
        c, ou = Counter(), defaultdict(set)
        for x in mes:
            for k in x[cle]:
                c[k] += 1; ou[k].add(x["page"])
        print(f"\n## {titre} : {sum(bool(x[cle]) for x in mes)} pages")
        for k, v in c.most_common(7):
            print(f"   {v:>4} pages · {k[:70]:<70} ex. {sorted(ou[k])[0].rsplit('/', 1)[-1][:46]}")
    sombres = [x for x in mes if x["sombre"]]
    print(f"\n## Thème : {len(sombres)} pages sombres sur {len(mes)} · color-scheme déclaré « dark » sur {sum('dark' in x['schema'] for x in sombres)} d'entre elles · pages sombres avec une liste déroulante native : {sum(x['selects'] > 0 for x in sombres if 'dark' not in x['schema'])} ({sum(x['selects'] for x in sombres if 'dark' not in x['schema'])} listes)")
    return 0 if mes else 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(principal())
