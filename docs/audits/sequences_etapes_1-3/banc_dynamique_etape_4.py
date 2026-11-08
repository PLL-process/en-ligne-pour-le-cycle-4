#!/usr/bin/env python3
"""Étape 4 — banc dynamique : boutons Vérifier, console, sauvegarde locale, focus clavier.
Usage : python3 banc_dynamique.py <racine_depot> <page_relative>..."""
import sys, json, pathlib
from playwright.sync_api import sync_playwright

root = pathlib.Path(sys.argv[1]).resolve()
pages = sys.argv[2:]
out = {}

def run(page, rel):
    url = (root / rel).as_uri()
    res = {"console": [], "boutons": [], "storage": {}, "focus": {}}
    page.on("console", lambda m: res["console"].append(f"{m.type}: {m.text[:160]}") if m.type in ("error", "warning") else None)
    page.on("pageerror", lambda e: res["console"].append(f"pageerror: {str(e)[:160]}"))
    page.goto(url, wait_until="load")
    page.wait_for_timeout(500)
    # inventaire boutons Vérifier
    btns = page.locator("button").filter(has_text="Vérifier")
    n = btns.count()
    for i in range(n):
        b = btns.nth(i)
        label = b.inner_text().strip()[:60]
        before_keys = page.evaluate("Object.keys(localStorage)")
        try:
            page.evaluate("""(i)=>{const bs=[...document.querySelectorAll('button')].filter(b=>b.textContent.includes('Vérifier'));
                const b=bs[i]; const panel=b.closest('[role=tabpanel],[id^=s][class*=panel],section[id]');
                if(panel){const t=document.querySelector('[role=tab][data-panel="'+panel.id+'"]'); if(t) t.click();}
                for(const d of [...document.querySelectorAll('details')]) if(d.contains(b)) d.open=true;}""", i)
            page.wait_for_timeout(150)
            b.scroll_into_view_if_needed(timeout=3000)
            b.click(timeout=3000, force=True)
        except Exception as e:
            res["boutons"].append({"label": label, "erreur_clic": str(e)[:100]}); continue
        page.wait_for_timeout(250)
        # retour visible : élément d'état proche (classes ok/err/mixte ou aria-live non vide)
        fb = page.evaluate("""(i)=>{
            const bs=[...document.querySelectorAll('button')].filter(b=>b.textContent.includes('Vérifier'));
            const b=bs[i]; let box=b.closest('section,.card,.exo,.boite,fieldset,div[data-exo],div[id]')||document.body;
            const cand=[...box.querySelectorAll('.retour,.feedback,[aria-live],.resultat,.score,.msg')].filter(e=>e.textContent.trim());
            const vis=cand.filter(e=>e.offsetParent!==null);
            return {retours:vis.length, texte:(vis[0]||cand[0]||{}).textContent?.trim().slice(0,140)||'', classe:(vis[0]||{}).className||''};
        }""", i)
        after_keys = page.evaluate("Object.keys(localStorage)")
        res["boutons"].append({"label": label, "retour_visible": fb["retours"] > 0, "texte": fb["texte"], "classe": fb["classe"],
                               "succes_a_vide": ("ok" in fb["classe"].split()) and "✔" in fb["texte"] or "🎉" in fb["texte"],
                               "nouvelles_cles": sorted(set(after_keys) - set(before_keys))})
    # sauvegarde : remplir identité + une sélection, sauver, effacer, inspecter
    page.evaluate("""()=>{for(const id of ['id_nom','id_prenom','id_classe']){const e=document.getElementById(id); if(e){e.value='TEST_'+id; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true}));}}
        const s=document.querySelector('select'); if(s&&s.options.length>1){s.selectedIndex=1; s.dispatchEvent(new Event('change',{bubbles:true}));}
        const r=document.querySelector('input[type=radio]'); if(r){r.click();}
        for(const b of document.querySelectorAll('button')) if(/Enregistrer|Sauvegarder|Sauver/i.test(b.textContent)) b.click();}""")
    page.wait_for_timeout(400)
    keys = page.evaluate("Object.keys(localStorage)")
    dump = page.evaluate("JSON.stringify(Object.fromEntries(Object.entries(localStorage)))")
    res["storage"]["cles_apres_saisie"] = keys
    res["storage"]["identite_en_clair"] = ("TEST_id_nom" in dump) or ("TEST_id_prenom" in dump)
    # bouton Effacer
    page.on("dialog", lambda d: d.accept())
    page.evaluate("window.confirm=()=>true; window.prompt=()=>'effacer-definitivement-ta-sauvegarde';")
    eff = page.locator("button").filter(has_text="Effacer")
    res["storage"]["bouton_effacer"] = eff.count()
    if eff.count():
        try:
            eff.first.click(timeout=3000, force=True); page.wait_for_timeout(300)
            eff.first.click(timeout=3000, force=True); page.wait_for_timeout(1200)
        except Exception as e:
            res["storage"]["erreur_effacer"] = str(e)[:100]
    rest = page.evaluate("Object.keys(localStorage)")
    res["storage"]["cles_restantes_apres_effacer"] = rest
    # focus clavier : les boutons Vérifier sont-ils atteignables et le focus visible ?
    res["focus"] = page.evaluate("""()=>{
        const b=[...document.querySelectorAll('button')].find(b=>b.textContent.includes('Vérifier'));
        if(!b) return {};
        b.focus(); const cs=getComputedStyle(b);
        return {tabindex:b.tabIndex, outline:cs.outlineStyle+' '+cs.outlineWidth, boxShadow:cs.boxShadow.slice(0,60), type:b.getAttribute('type')};
    }""")
    res["alt_manquants"] = page.evaluate("[...document.images].filter(i=>!i.hasAttribute('alt')).length")
    res["images_total"] = page.evaluate("document.images.length")
    res["h1"] = page.evaluate("document.querySelectorAll('h1').length")
    # débordement horizontal à 375 px
    page.set_viewport_size({"width": 375, "height": 800}); page.wait_for_timeout(300)
    res["debordement_375"] = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    return res

with sync_playwright() as p:
    br = p.chromium.launch()
    for rel in pages:
        ctx = br.new_context(viewport={"width": 1100, "height": 900})
        pg = ctx.new_page()
        try:
            out[rel] = run(pg, rel)
        except Exception as e:
            out[rel] = {"erreur": str(e)[:200]}
        ctx.close()
    br.close()
print(json.dumps(out, ensure_ascii=False, indent=1))
