# -*- coding: utf-8 -*-
"""Banc de l'entraînement DNB « algorigrammes » (3e_C6.2) — rejoue les critères de recette de l'audit du 21/11/2026.

    python3 tests_entrainement_dnb.py          (depuis ce dossier ; Playwright + Chromium)

Sortie : 0 tout passe · 1 au moins un échec · 2 Playwright absent : rien n'a été vérifié (règle d'or n°299).
"""
import pathlib
import re
import shutil
import sys
import tempfile

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("✘ Playwright absent : rien n'a été vérifié")
    sys.exit(2)

ICI = pathlib.Path(__file__).resolve().parent
PAGE = ICI / "entrainement_dnb_algorigrammes.html"
URL = PAGE.as_uri()
res = []


def t(nom, ok, detail=""):
    res.append((nom, bool(ok)))
    print(("✔" if ok else "✘"), nom, ("— " + str(detail)) if detail and not ok else "")


def lum(c):
    v = [int(x) / 255 for x in re.findall(r"\d+", c)[:3]]
    v = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in v]
    return .2126 * v[0] + .7152 * v[1] + .0722 * v[2]


def contraste(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + .05) / (lb + .05)


JS_BONNES = """(()=>{const s=[...document.scripts].map(x=>x.textContent).join('\\n');const o={};
  for(const m of s.matchAll(/"(q\\d+)":"((?:[^"\\\\]|\\\\.)*)"/g)) o[m[1]]=JSON.parse('"'+m[2]+'"'); return o;})()"""


def cocher(pg, qid, valeur):
    pg.evaluate("""([q,v])=>{const r=[...document.querySelectorAll('input[name="'+q+'"]')].find(x=>x.value===v);
      const f=document.getElementById(q); if(f) f.classList.add('vu'); r.click();}""", [qid, valeur])


def onglet(pg, p):
    pg.click(f"#tab-{p}")
    pg.wait_for_timeout(120)


with sync_playwright() as p:
    nav = p.chromium.launch()
    ctx = nav.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(URL)
    pg.wait_for_timeout(500)
    t("aucune erreur JavaScript au chargement", not errs, errs)

    # ── structure ──
    n = pg.eval_on_selector_all("article.exo", "a=>a.length")
    t("30 exercices, 4 manches et l'épreuve écrite", n == 30 and pg.eval_on_selector_all(".seance-panel", "a=>a.length") == 5, n)
    t("aucune liste déroulante (n°300)", pg.eval_on_selector_all("select", "a=>a.length") == 0)
    t("chaque exercice : fieldset, légende, 4 boutons radio d'un même groupe, valeur = texte (n°300)", pg.evaluate("""
      [...document.querySelectorAll('article.exo')].every(a=>{const f=a.querySelector('fieldset.qcm-groupe');
        const r=f?[...f.querySelectorAll('input[type=radio]')]:[];
        return f && f.querySelector('legend') && r.length===4 && new Set(r.map(x=>x.name)).size===1
          && r.every(x=>{const l=document.querySelector('label[for="'+x.id+'"]'); return l && l.textContent.trim()===x.value;});})"""))
    t("trois propositions fausses par exercice, chacune avec son pourquoi", pg.evaluate("""
      [...document.querySelectorAll('article.exo')].every(a=>[...a.querySelectorAll('input[data-pourquoi]')]
        .filter(x=>x.dataset.pourquoi.length>25).length===3)"""))
    t("2 aides et 1 correction par exercice, 3 réfutations par correction",
      pg.evaluate("""[...document.querySelectorAll('article.exo')].every(a=>a.querySelectorAll('details.aide').length===2
        && a.querySelectorAll('details.correction').length===1 && a.querySelectorAll('details.correction ul > li').length===3)"""))
    t("corrections citées par leur texte, jamais par une lettre A/B/C/D",
      pg.evaluate("""[...document.querySelectorAll('details.correction li')].every(l=>!/^\\s*[ABCD][.)]/.test(l.textContent))"""))
    t("corrections et aides repliées au chargement",
      pg.evaluate("[...document.querySelectorAll('details.correction,details.aide')].every(d=>!d.open)"))
    t("onglets nommés Symboles, Déroulement, Auto-test, Transfert, Épreuve écrite", pg.evaluate("""
      ['Symboles','Déroulement','Auto-test','Transfert','écrite'].every((w,i)=>document.querySelectorAll('.seance-tab')[i].textContent.includes(w))"""))
    t("accès direct à l'atelier C6.2 en haut de page et à la fin de la manche 3", pg.evaluate("""
      !!document.querySelector('#navharm a[href="sequence_3e_C6.2_auto_test_station.html"]')
      && !!document.querySelector('#m3 a[href="sequence_3e_C6.2_auto_test_station.html#banc-essai"]')"""))
    atelier = (ICI / "sequence_3e_C6.2_auto_test_station.html").read_text(encoding="utf-8")
    t("l'ancre #banc-essai existe dans l'atelier (activité 4)", 'id="banc-essai"' in atelier)
    # lien de l'accès rapide de l'index (21/11/2026) : l'adresse #ep ouvre l'épreuve écrite, #exo17 la manche 3 ;
    # contexte à part, pour que l'onglet retenu n'influe pas sur la suite du banc
    cx = nav.new_context(viewport={"width": 390, "height": 800})
    pa = cx.new_page(); e2 = []; pa.on("pageerror", lambda e: e2.append(str(e)))
    pa.goto(URL + "#ep"); pa.wait_for_timeout(400)
    vu_ep = pa.evaluate("document.querySelector('.seance-panel.active')?.id")
    pa.evaluate("location.hash='exo17'"); pa.wait_for_timeout(300)
    vu_17 = pa.evaluate("document.querySelector('.seance-panel.active')?.id")
    t("lien direct de l'index : #ep ouvre « Épreuve écrite », #exo17 ouvre la manche 3",
      vu_ep == "ep" and vu_17 == "m3" and not e2, (vu_ep, vu_17, e2))
    cx.close()
    t("rappel : « cinq repères pour cet entraînement », pas une liste exhaustive",
      "cinq repères graphiques" in pg.inner_text("#rappel") and "Il en existe d'autres" in pg.inner_text("#rappel"))
    t("schémas : chaque envoi au gardien est un parallélogramme (polygone vert), jamais un rectangle", pg.evaluate("""
      [...document.querySelectorAll('svg.algo-svg')].every(s=>[...s.querySelectorAll('text')].filter(x=>/envoyer/.test(x.textContent))
        .every(x=>{const b=x.getBBox(); return [...s.querySelectorAll('polygon[fill="#0d3320"]')].some(p=>{const q=p.getBBox();
          return b.x>=q.x-2 && b.x+b.width<=q.x+q.width+2 && b.y>=q.y-2 && b.y+b.height<=q.y+q.height+2;});}))"""))

    bonnes = pg.evaluate(JS_BONNES)
    t("30 réponses attendues lues dans le vérificateur", len(bonnes) == 30, len(bonnes))

    # ── place de la bonne réponse ──
    places = pg.evaluate("""(b)=>[...document.querySelectorAll('article.exo fieldset')].map(f=>
      [...f.querySelectorAll('input')].findIndex(x=>x.value===b[f.id]))""", bonnes)
    manches = [places[0:8], places[8:16], places[16:22], places[22:30]]
    t("bonne réponse : chaque place sert dans chaque manche, au plus 2 fois",
      all(set(m) == {0, 1, 2, 3} and max(m.count(k) for k in range(4)) <= 2 for m in manches), places)
    t("bonne réponse : jamais trois fois de suite à la même place, aucun motif 2-1-4-3",
      not any(places[i] == places[i + 1] == places[i + 2] for i in range(28))
      and not any(places[i:i + 4] == places[i + 4:i + 8] for i in range(22)), places)

    # ── stratégies sans lecture ──
    def jouer(strategie):
        pg.evaluate("localStorage.clear()")
        pg.reload()
        pg.wait_for_timeout(300)
        validees = 0
        for m, (a, b) in enumerate([(1, 8), (9, 16), (17, 22), (23, 30)], 1):
            onglet(pg, f"m{m}")
            for q in range(a, b + 1):
                vals = pg.eval_on_selector_all(f"#q{q} input", "r=>r.map(x=>x.value)")
                cocher(pg, f"q{q}", strategie(vals))
            pg.click(f'[data-check="{m}"]')
            validees += pg.evaluate(f"!!window.__valid[{m}]")
        return validees

    def longue(vals):
        return max(vals, key=len)

    t("choisir toujours la proposition la plus longue ne valide aucune manche", jouer(longue) == 0)
    t("répondre toujours à la même place ne valide aucune manche",
      all(jouer(lambda v, k=k: v[k]) == 0 for k in range(4)))

    # ── une manche parfaite ──
    pg.evaluate("localStorage.clear()")
    pg.reload()
    pg.wait_for_timeout(300)
    for q in range(1, 9):
        cocher(pg, f"q{q}", bonnes[f"q{q}"])
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(120)
    t("manche 1 parfaite : validée, « 8 / 8 renseignés », progression 1 / 4",
      "8 / 8 renseignés" in pg.inner_text("#fb1") and "seuil atteint" in pg.inner_text("#fb1")
      and pg.inner_text("#progTxt").startswith("1 / 4"))
    t("chaque exercice juste porte « ✔ juste »",
      all("juste" in pg.inner_text(f"#etat-q{q}") for q in range(1, 9)))
    t("le bandeau coche les deux tâches", pg.inner_text("#tachesBandeau").count("☑") == 2)

    # ── 6 justes et 2 blancs (critère de recette de l'audit) ──
    onglet(pg, "m2")
    for q in range(9, 15):
        cocher(pg, f"q{q}", bonnes[f"q{q}"])
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    fb = pg.inner_text("#fb2")
    bandeau = pg.inner_text("#tachesBandeau")
    t("6 justes + 2 blancs : « 6 / 8 renseignés · seuil atteint », exercices 15 et 16 à faire",
      "6 / 8 renseignés" in fb and "seuil atteint" in fb and "À faire" in fb and "15 et 16" in fb, fb)
    t("6 justes + 2 blancs : la tâche « Répondre aux 8 exercices » n'est PAS cochée",
      "☐ Répondre aux 8 exercices (6 / 8)" in bandeau and "☑ Vérifier" in bandeau, bandeau)
    t("6 justes + 2 blancs : les deux exercices sont marqués « ○ à faire »",
      "à faire" in pg.inner_text("#etat-q15") and "à faire" in pg.inner_text("#etat-q16"))

    # ── une erreur : « à revoir », sans dévoiler la solution ──
    onglet(pg, "m3")
    faux = [v for v in pg.eval_on_selector_all("#q17 input", "r=>r.map(x=>x.value)") if v != bonnes["q17"]][0]
    cocher(pg, "q17", faux)
    for q in range(18, 23):
        cocher(pg, f"q{q}", bonnes[f"q{q}"])
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    fb = pg.inner_text("#fb3")
    rv = pg.inner_text("#revoir-q17")
    t("une erreur en 17 : « À revoir : exercice 17 », chip « ✘ à revoir »",
      "À revoir" in fb and "17" in fb and "à revoir" in pg.inner_text("#etat-q17"), fb)
    t("« Revoir mon erreur » cite le choix et ce qui cloche, sans la bonne réponse",
      pg.is_visible("#revoir-q17") and faux in rv and bonnes["q17"] not in rv, rv)
    t("le message de la manche ne contient aucune bonne réponse",
      not any(bonnes[f"q{q}"] in fb for q in range(17, 23)))
    pg.click("#revoir-q17 [data-aide1]")
    t("« Ouvrir l'aide 1 » ouvre l'aide 1 de l'exercice", pg.evaluate("document.querySelector('#exo17 details.aide1').open"))

    # ── retrait de la validation (n°340) ──
    onglet(pg, "m1")
    autre = [v for v in pg.eval_on_selector_all("#q2 input", "r=>r.map(x=>x.value)") if v != bonnes["q2"]][0]
    cocher(pg, "q2", autre)
    pg.wait_for_timeout(120)
    t("une réponse changée après « Vérifier » retire la validation et le dit",
      not pg.evaluate("window.__valid[1]") and "vérifie de nouveau" in pg.inner_text("#fb1")
      and "à vérifier" in pg.inner_text("#etat-q2"))
    cocher(pg, "q2", bonnes["q2"])
    pg.click('[data-check="1"]')

    # ── trace et rappel ──
    onglet(pg, "m3")
    for k, v in enumerate([1, 1, 2, 3], 1):
        pg.fill(f"#tr_{k}", str(v))
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(100)
    t("la trace de l'exercice 18 est marquée case par case (non notée)",
      pg.inner_text("#m_tr_3") == "✔" and pg.inner_text("#m_tr_4") == "✘")
    t("remplir la trace ne retire pas la validation de la manche 3", pg.evaluate("!!window.__valid[3]"))
    onglet(pg, "m1")
    pg.evaluate("document.getElementById('rappel').open=true")
    for k, v in (("ra_a", 1), ("ra_b", 2), ("ra_aff", 2)):
        pg.fill(f"#{k}", str(v))
    cocher(pg, "rappel_rz", "1 défaut")
    pg.click('[data-check="r"]')
    t("rappel « À toi » : la trace des deux voyants est validée", "4 / 4" in pg.inner_text("#fbr"))

    # ── prédiction ──
    pg.evaluate("localStorage.clear()")
    pg.reload()
    pg.wait_for_timeout(300)
    onglet(pg, "m2")
    t("manche 2 : les propositions attendent la prédiction", not pg.is_visible("#q9"))
    pg.fill("#pred-q9", "13")
    pg.click('[data-montrer="q9"]')
    t("« Voir les propositions » les affiche", pg.is_visible("#q9"))

    # ── rechargement ──
    cocher(pg, "q9", bonnes["q9"])
    cocher(pg, "q10", [v for v in pg.eval_on_selector_all("#q10 input", "r=>r.map(x=>x.value)") if v != bonnes["q10"]][0])
    pg.click('[data-check="2"]')
    choisis = pg.evaluate("[...document.querySelectorAll('main input[type=radio]:checked')].map(r=>r.id+'='+r.value)")
    pg.reload()
    pg.wait_for_timeout(500)
    apres = pg.evaluate("[...document.querySelectorAll('main input[type=radio]:checked')].map(r=>r.id+'='+r.value)")
    t("après rechargement, les mêmes propositions sont cochées, à la même place", choisis == apres and choisis, apres)
    t("après rechargement, les états et « Revoir mon erreur » reviennent",
      "à revoir" in pg.inner_text("#etat-q10") and pg.evaluate("!document.getElementById('revoir-q10').hidden"))
    t("après rechargement, la prédiction est gardée", pg.input_value("#pred-q9") == "13" and pg.is_visible("#q9"))
    t("après reprise, « Où en suis-je ? » est ouvert et dit ce qui est à revoir",
      pg.evaluate("document.getElementById('ouJenSuis').open") and "à revoir : 10" in pg.inner_text("#ouJenSuisListe"))

    # ── mode essentiel ──
    pg.click("#btnEssentiel")
    onglet(pg, "m2")
    t("mode essentiel : rappel replié mais présent, corrections et « Revoir mon erreur » gardés", pg.evaluate("""
      (()=>{const r=document.getElementById('rappel'); return r && r.getClientRects().length && !r.open
        && document.querySelector('#exo10 details.correction').getClientRects().length
        && document.getElementById('revoir-q10').getClientRects().length})()"""))
    t("mode essentiel : textes d'accompagnement retirés, propositions visibles sans prédiction",
      not pg.is_visible("#methode") and not pg.is_visible(".seance-panel.active .prediction") and pg.is_visible("#q11"))
    pg.click("#btnEssentiel")

    # ── épreuve écrite ──
    onglet(pg, "ep")
    for k in range(1, 5):
        pg.fill(f"#ep{k}", f"Réponse {k} : la branche « oui » est suivie car 79 < 80 est vrai.")
    pg.evaluate("document.getElementById('epCorrection').open=true")
    pg.check("#crit1")
    pg.wait_for_timeout(150)
    bd = pg.inner_text("#tachesBandeau")
    t("épreuve : bandeau « 4 / 4 », correction lue, grille cochée", bd.count("☑") == 3, bd)
    t("épreuve : aucun bouton « Vérifier » (une réponse écrite n'est pas notée par la machine)",
      pg.eval_on_selector_all("#ep [data-check]", "a=>a.length") == 0)
    pg.reload()
    pg.wait_for_timeout(400)
    t("épreuve : réponses écrites et grille gardées au rechargement",
      pg.input_value("#ep3").startswith("Réponse 3") and pg.is_checked("#crit1"))

    # ── fiche bilan ──
    pg.evaluate("window.print=()=>{window.__imprime=document.body.className}")
    pg.click("#btnFiche")
    fiche = pg.inner_text("#ficheBilan") if pg.evaluate("document.getElementById('ficheBilan').innerHTML.length>0") else ""
    fiche = pg.evaluate("document.getElementById('ficheBilan').textContent")
    t("« Ma fiche bilan » : manches, erreurs avec leur pourquoi, réponses écrites",
      "Manche 2" in fiche and "Exercice 10" in fiche and "Réponse 4" in fiche
      and "imprime-fiche" in pg.evaluate("window.__imprime"))

    # ── contraste ──
    c = pg.evaluate("""(()=>{const o=document.querySelector('.qcm-option'),k=document.querySelector('.seance-panel.active .card')||document.querySelector('.card');
      return [getComputedStyle(o).borderTopColor, getComputedStyle(k).backgroundColor]})()""")
    t("contour d'un choix : au moins 3:1 sur la carte (WCAG 1.4.11)", contraste(*c) >= 3, round(contraste(*c), 2))

    # ── stockage refusé ──
    ctx2 = nav.new_context(viewport={"width": 1280, "height": 900})
    ctx2.add_init_script("Storage.prototype.setItem=function(){throw new Error('quota')}")
    p2 = ctx2.new_page()
    p2.goto(URL)
    p2.wait_for_timeout(300)
    t("stockage refusé : l'élève est prévenu que sa progression n'est pas enregistrée", p2.is_visible("#alerteStockage"))
    ctx2.close()

    # ── la page seule, sans réseau ──
    d = pathlib.Path(tempfile.mkdtemp())
    shutil.copy(PAGE, d / PAGE.name)
    ctx3 = nav.new_context(viewport={"width": 390, "height": 844})
    bloques = []
    ctx3.route("**/*", lambda r: r.continue_() if r.request.url.startswith(("file:", "data:", "blob:"))
               else (bloques.append(r.request.url), r.abort()))
    p3 = ctx3.new_page()
    e3 = []
    p3.on("pageerror", lambda e: e3.append(str(e)))
    manquants = []
    p3.on("requestfailed", lambda r: manquants.append(r.url))
    p3.goto((d / PAGE.name).as_uri())
    p3.wait_for_timeout(500)
    t("copiée seule dans un dossier vide, sans réseau : aucune erreur, aucun fichier manquant",
      not e3 and not manquants and not bloques, (e3, manquants, bloques))
    t("… les schémas sont dans la page et le code est coloré",
      p3.eval_on_selector_all("svg.algo-svg", "a=>a.length") >= 10 and p3.eval_on_selector_all("pre .py-kw", "a=>a.length") > 5)
    ctx3.close()
    shutil.rmtree(d)

    # ── largeur ──
    largeurs = []
    for w in (320, 390, 1280):
        pg.set_viewport_size({"width": w, "height": 900})
        for o in ("m1", "m2", "m3", "m4", "ep"):
            onglet(pg, o)
            sw = pg.evaluate("document.documentElement.scrollWidth")
            if sw > w + 1:
                largeurs.append((w, o, sw))
    t("aucun défilement horizontal à 320, 390 et 1 280 px, sur les cinq pages", not largeurs, largeurs)

    # ── impression ──
    pg.emulate_media(media="print")
    t("impression : la manche ouverte seule, sans boutons ni replis fermés, texte foncé", pg.evaluate("""
      [...document.querySelectorAll('.seance-panel')].filter(x=>getComputedStyle(x).display!=='none').length===1
      && [...document.querySelectorAll('.btn')].every(b=>getComputedStyle(b).display==='none')
      && [...document.querySelectorAll('.seance-panel.active details:not([open])')].every(d=>getComputedStyle(d).display==='none')
      && [...document.querySelectorAll('.seance-panel.active legend')].every(l=>getComputedStyle(l).color==='rgb(17, 17, 17)')"""))
    ctx4 = nav.new_context()
    p4 = ctx4.new_page()
    p4.goto(URL)
    p4.wait_for_timeout(300)
    onglet(p4, "m4")
    pdf = pathlib.Path(tempfile.mkdtemp()) / "m4.pdf"
    p4.pdf(path=str(pdf), format="A4", margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"})
    try:
        import pypdf
        pages = len(pypdf.PdfReader(str(pdf)).pages)
    except ImportError:
        pages = len(re.findall(rb"/Type\s*/Page(?![s\w])", pdf.read_bytes()))
    t("impression A4 de la manche 4 (quatre schémas, chacun avec sa question) : 6 pages au plus", 0 < pages <= 6, pages)
    shutil.rmtree(pdf.parent)
    ctx4.close()
    t("aucune erreur JavaScript pendant le banc", not errs, errs)
    nav.close()

print(f"\n{sum(1 for _, o in res if o)} / {len(res)} tests passés")
sys.exit(0 if all(o for _, o in res) else 1)
