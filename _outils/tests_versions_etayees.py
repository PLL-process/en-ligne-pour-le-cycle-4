from playwright.sync_api import sync_playwright
import pathlib, json, sys
racine = pathlib.Path("theme-2-structure-fonctionnement-comportement")
fichiers = [f for f in sorted(racine.glob("**/sequence_*.html"))
            if "etayage" in f.read_text(encoding="utf-8")]
res=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":900})
    for f in fichiers:
        errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(500)
        n = pg.evaluate("document.querySelectorAll('details.etayage').length")
        # chaque bloc suit bien un textarea
        ok_place = pg.evaluate("""[...document.querySelectorAll('details.etayage')]
            .every(d => d.previousElementSibling && d.previousElementSibling.tagName==='TEXTAREA')""")
        # au moins 2 amorces par bloc, chacune contenant un ____
        ok_texte = pg.evaluate("""[...document.querySelectorAll('details.etayage')].every(d=>{
            const li=[...d.querySelectorAll('li')];
            return li.length>=2 && li.every(x=>x.textContent.includes('____'));})""")
        # visible en mode essentiel
        pg.evaluate("document.body.classList.add('essentiel')")
        vis = pg.evaluate("""(()=>{const d=document.querySelector('details.etayage');
            return d ? getComputedStyle(d).display!=='none' : false;})()""")
        pg.evaluate("document.body.classList.remove('essentiel')")
        # ouverture au clavier / dépliage
        pg.evaluate("document.querySelector('details.etayage').open=true")
        haut = pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1")
        res.append([f.name, not errs, n, ok_place, ok_texte, vis, haut])
        print(f"{'✔' if (not errs and ok_place and ok_texte and vis and haut) else '✘'} {f.name}"
              f" | {n} blocs | JS {'OK' if not errs else errs} | place {ok_place}"
              f" | texte {ok_texte} | visible en essentiel {vis} | pas de scroll H {haut}")
    b.close()
bad=[r[0] for r in res if not all(r[1:2]+r[3:])]
print(f"\n{len(res)} séquences testées · {len(bad)} en défaut : {bad or 'aucune'}")
print("total blocs :", sum(r[2] for r in res))
