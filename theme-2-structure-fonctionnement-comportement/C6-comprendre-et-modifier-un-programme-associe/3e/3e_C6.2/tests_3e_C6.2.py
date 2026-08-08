from playwright.sync_api import sync_playwright
import pathlib, json
SEQ = pathlib.Path("sequence_3e_C6.2_auto_test_station.html").resolve().as_uri()
QCM = pathlib.Path("qcm_3e_C6.2_auto_test.html").resolve().as_uri()
res = []
def t(nom, ok, det=""): res.append((nom, bool(ok), det)); print(("✔" if ok else "✘"), nom, det)

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1280,"height":900})
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))

    # ── SÉQUENCE ──
    pg.goto(SEQ); pg.wait_for_timeout(600)
    t("séquence : aucune erreur JS au chargement", not errs, str(errs))
    bandeau = pg.inner_text("#tachesBandeau")
    t("séquence : bandeau de tâches affiché (n°30)",
      "Séance 1" in bandeau and "étape 1 sur" in bandeau and "☐" in bandeau,
      bandeau.split("\n")[0])
    # billet d'entrée sans note
    pg.click('button[data-check="0"]'); pg.wait_for_timeout(200)
    m0 = pg.inner_text("#fb0")
    t("billet d'entrée : oriente sans sanctionner (n°26)",
      "0 / 3" in m0 and "aucun" in m0.lower(), m0[:70].replace("\n"," "))
    pg.click("#tab-s2"); pg.wait_for_timeout(200)
    # banc d'essai à deux pannes
    pg.evaluate("""() => {["org_anemo","org_sirene"].forEach(i=>document.getElementById(i).checked=true);
                        ["org_gyro","org_radio"].forEach(i=>document.getElementById(i).checked=false);}""")
    pg.click("#btnBanc"); pg.wait_for_timeout(200)
    trace = pg.inner_text("#journalBanc")
    t("banc d'essai : compte 2 défauts et ne redescend pas", "defauts = 2" in trace, "")
    t("banc d'essai : détecte la défaillance silencieuse",
      pg.evaluate("!!(window.__exp||{}).banc_deux_pannes"), "")
    # verrou expérientiel : check 4 refuse sans les deux essais
    pg.evaluate("window.__exp={}")
    pg.click('button[data-check="4"]'); pg.wait_for_timeout(200)
    t("verrou expérientiel : l'activité 4 refuse sans les deux essais",
      "6" in pg.inner_text("#fb4"), pg.inner_text("#fb4")[:60].replace("\n"," "))
    # mode essentiel
    pg.click("#btnEssentiel"); pg.wait_for_timeout(150)
    t("mode essentiel : bascule et masque le référentiel (n°29)",
      pg.evaluate("document.body.classList.contains('essentiel')") and
      not pg.is_visible(".referentiel-card"), "")
    pg.click("#btnEssentiel")
    # sauvegarde / restauration
    pg.click("#tab-s1"); pg.wait_for_timeout(200)
    pg.fill("textarea", "hypothèse de test")
    pg.evaluate("save(false)"); pg.reload(); pg.wait_for_timeout(500)
    t("sauvegarde puis restauration après rechargement",
      pg.eval_on_selector("textarea","e=>e.value")=="hypothèse de test", "")
    # onglets de séance
    pg.click("#tab-s3"); pg.wait_for_timeout(200)
    t("onglets de séance : le bandeau suit la séance affichée",
      "Séance 3" in pg.inner_text("#tachesBandeau"), "")
    # blocs de la règle n°4
    txt = pg.inner_text("body")
    t("blocs règle n°4 présents (entraînement + bonus)",
      "Prêt·e à t'entraîner" in txt and "Bonus" in txt, "")
    t("un seul bouton QCM dans toute la séquence",
      len(pg.query_selector_all('a[href$="qcm_3e_C6.2_auto_test.html"].btn'))==1, "")
    # accessibilité statique (n°34)
    t("n°34 : tout champ de saisie porte une étiquette",
      pg.evaluate("""[...document.querySelectorAll('select,textarea,input')].every(e=>
        !e.id || e.getAttribute('aria-label') || document.querySelector(`label[for="${e.id}"]`) || e.closest('label'))"""), "")
    t("n°34 : pas de défilement horizontal à 1280 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"), "")
    pg.set_viewport_size({"width":420,"height":900}); pg.wait_for_timeout(300)
    t("n°34 : pas de défilement horizontal à 420 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+2"),
      str(pg.evaluate("document.documentElement.scrollWidth")))
    pg.set_viewport_size({"width":1280,"height":900})
    t("n°34 : le focus clavier reste visible (Tab)",
      pg.evaluate("""() => { const e=document.querySelector('button'); e.focus();
        const s=getComputedStyle(e,':focus-visible'); return document.activeElement===e; }"""), "")

    # ── QCM ──
    errs.clear(); pg.goto(QCM); pg.wait_for_timeout(600)
    t("QCM : aucune erreur JS au chargement", not errs, str(errs))
    t("QCM : 30 questions", pg.evaluate("QUESTIONS.length")==30, "")
    t("QCM : 3 questions illustrées, alt renseigné",
      pg.evaluate("QUESTIONS.filter(q=>q.img).length")==3 and
      pg.evaluate("QUESTIONS.filter(q=>q.img).every(q=>q.img.alt.length>40)"), "")
    rep = pg.evaluate("QUESTIONS.reduce((a,q)=>(a[q.r]=(a[q.r]||0)+1,a),{})")
    t("QCM : bonnes réponses réparties sur A/B/C/D", min(rep.values())>=7, json.dumps(rep))
    t("QCM : aucune réfutation en face de la bonne réponse",
      pg.evaluate("QUESTIONS.every(q=>q.d[q.r]==='')"), "")
    t("QCM : chaque distracteur est réfuté",
      pg.evaluate("QUESTIONS.every(q=>q.d.filter((x,i)=>i!==q.r).every(x=>x&&x.length>20))"), "")
    t("QCM : les 5 champs obligatoires sont remplis partout",
      pg.evaluate("QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret&&q.n)"), "")
    b.close()

print(f"\n{sum(1 for _,ok,_ in res if ok)} / {len(res)} tests passés")
pathlib.Path("/tmp/res_c62.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
