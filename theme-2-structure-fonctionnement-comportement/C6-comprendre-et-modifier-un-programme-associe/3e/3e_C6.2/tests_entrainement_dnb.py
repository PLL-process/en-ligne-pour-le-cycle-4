from playwright.sync_api import sync_playwright
import pathlib, sys
f = pathlib.Path("entrainement_dnb_algorigrammes.html").resolve().as_uri()
res=[]
def t(n, ok, d=""): res.append((n,bool(ok),d)); print(("✔" if ok else "✘"), n, d)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":900})
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(f); pg.wait_for_timeout(600)
    t("aucune erreur JS", not errs, str(errs))
    t("30 exercices", pg.eval_on_selector_all("article.exo","a=>a.length")==30)
    t("chaque exercice a 4 options + le choix vide",
      pg.evaluate("[...document.querySelectorAll('article.exo select')].every(s=>s.options.length===5)"))
    t("chaque select a une étiquette (n°34)",
      pg.evaluate("[...document.querySelectorAll('select')].every(s=>document.querySelector(`label[for=\"${s.id}\"]`))"))
    t("chaque exercice a 2 aides et 1 correction",
      pg.evaluate("""[...document.querySelectorAll('article.exo')].every(a=>
        a.querySelectorAll('details.aide').length===2 && a.querySelectorAll('details.correction').length===1)"""))
    t("chaque correction réfute les 3 distracteurs",
      pg.evaluate("""[...document.querySelectorAll('details.correction')].every(d=>d.querySelectorAll('li').length===3)"""))
    t("corrections repliées au chargement",
      pg.evaluate("[...document.querySelectorAll('details.correction')].every(d=>!d.open)"))
    t("images avec alternative textuelle",
      pg.evaluate("[...document.querySelectorAll('img')].every(i=>i.alt && i.alt.length>40)"))
    t("bandeau de tâches affiché (n°30)", "Manche 1" in pg.inner_text("#tachesBandeau"))
    # répartition des bonnes réponses sur les 4 positions
    pos = pg.evaluate("""(()=>{const c={};document.querySelectorAll('article.exo').forEach(a=>{
      const bonne=a.querySelector('details.correction p b').nextSibling.textContent.trim();
      const opts=[...a.querySelectorAll('option')].slice(1).map(o=>o.textContent.trim());
      const i=opts.indexOf(bonne); c[i]=(c[i]||0)+1;}); return c;})()""")
    t("bonnes réponses réparties sur les 4 positions",
      len([k for k,v in pos.items() if k!="-1" and v>0])==4 and pos.get("-1",0)==0, str(pos))
    # une manche complète, toutes justes
    n = pg.evaluate("""(()=>{let k=0;document.querySelectorAll('#m1 article.exo').forEach(a=>{
      const bonne=a.querySelector('details.correction p b').nextSibling.textContent.trim();
      a.querySelector('select').value=bonne; k++;}); return k;})()""")
    pg.click('[data-check="1"]'); pg.wait_for_timeout(200)
    t("manche 1 : score parfait reconnu", f"{n} / {n} réponses justes" in pg.inner_text("#fb1"),
      pg.inner_text("#fb1")[:70])
    t("progression mise à jour", "1 / 4 manches" in pg.inner_text("#progTxt"))
    t("bandeau coché", "☑" in pg.inner_text("#tachesBandeau"))
    # message quand il reste des vides
    pg.click('#tab-m2'); pg.wait_for_timeout(150)
    pg.click('[data-check="2"]'); pg.wait_for_timeout(150)
    t("manche 2 : les exercices vides sont signalés", "sans réponse" in pg.inner_text("#fb2"),
      pg.inner_text("#fb2")[:70])
    # mode essentiel
    pg.click("#btnEssentiel"); pg.wait_for_timeout(150)
    t("mode essentiel masque les corrections (n°29)",
      not pg.is_visible("details.correction") and not pg.is_visible(".referentiel-card"))
    t("mode essentiel laisse les exercices et les aides",
      pg.is_visible(".seance-panel.active article.exo")
      and pg.is_visible(".seance-panel.active details.aide"))
    pg.click("#btnEssentiel")
    # persistance
    pg.click('#tab-m1'); pg.wait_for_timeout(120)
    pg.reload(); pg.wait_for_timeout(600)
    t("réponses et progression restaurées après rechargement",
      "1 / 4 manches" in pg.inner_text("#progTxt") and pg.eval_on_selector("#m1 select","e=>e.value")!="")
    # onglets
    for m in (2,3,4):
        pg.click(f'#tab-m{m}'); pg.wait_for_timeout(120)
    t("les 4 onglets affichent leur bandeau", "Manche 4" in pg.inner_text("#tachesBandeau"))
    t("pas de défilement horizontal à 1280 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"))
    pg.set_viewport_size({"width":420,"height":900}); pg.wait_for_timeout(300)
    t("pas de défilement horizontal à 420 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+2"),
      str(pg.evaluate("document.documentElement.scrollWidth")))
    t("liens internes présents",
      pg.eval_on_selector_all("a[href$='.html']","a=>a.length")>=3)
    b.close()
print(f"\n{sum(1 for _,o,_ in res if o)} / {len(res)} tests passés")
sys.exit(0 if all(o for _,o,_ in res) else 1)
