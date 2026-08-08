from playwright.sync_api import sync_playwright
import pathlib
racine = pathlib.Path("theme-2-structure-fonctionnement-comportement")
fichiers = [f for f in sorted(racine.glob("**/sequence_*.html"))
            if "tachesBandeau" in f.read_text(encoding="utf-8")]
mauvais=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":900})
    for f in fichiers:
        errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(500)
        ok = {"js": not errs}
        ok["visible"] = pg.is_visible("#tachesBandeau")
        ok["etape"] = "étape 1 sur" in pg.inner_text("#tachesBandeau")
        # chaque onglet affiche SON bloc, non vide, et le titre correspond
        onglets = pg.eval_on_selector_all(".seance-tab", "a=>a.map(x=>x.dataset.panel||x.id.replace('tab-',''))")
        detail=[]
        for i,pan in enumerate(onglets):
            pg.click(f'.seance-tab[data-panel="{pan}"], #tab-{pan}'); pg.wait_for_timeout(120)
            t = pg.inner_text("#tachesBandeau")
            detail.append((pan, t.split("\n")[0][:44], t.count("☐")+t.count("☑")))
        ok["tous_onglets"] = all(n>0 for _,_,n in detail)
        # cocher la 1re tâche de la 1re séance : la case doit passer à ☑
        pg.click(f'.seance-tab[data-panel="{onglets[0]}"], #tab-{onglets[0]}'); pg.wait_for_timeout(120)
        n0 = pg.evaluate("(()=>{const t=document.querySelector('.seance-tab.active');return TACHES[t.dataset.panel||t.id.replace('tab-','')];})().taches[0].n")
        pg.evaluate(f"window.__valid[{n0}]=true; majProgress();"); pg.wait_for_timeout(120)
        ok["coche"] = "☑" in pg.inner_text("#tachesBandeau")
        pg.evaluate(f"window.__valid[{n0}]=false; majProgress();")
        # visible en mode essentiel
        pg.evaluate("document.body.classList.add('essentiel')")
        ok["essentiel"] = pg.is_visible("#tachesBandeau")
        pg.evaluate("document.body.classList.remove('essentiel')")
        ok["scroll"] = pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1")
        bon = all(ok.values())
        if not bon: mauvais.append((f.name, ok, errs))
        print(("✔" if bon else "✘"), f.name, "|", " ".join(f"{k}={v}" for k,v in ok.items()))
        for d in detail: print("      ", d)
    b.close()
print(f"\n{len(fichiers)} séquences · {len(mauvais)} en défaut")
for m in mauvais: print("  ", m)
