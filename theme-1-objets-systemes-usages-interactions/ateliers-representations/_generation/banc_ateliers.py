# -*- coding: utf-8 -*-
"""Banc de tests des ateliers des représentations (Playwright / Chromium).

    python3 banc_ateliers.py                 # tous les ateliers construits, leurs QCM, synthèses et les cahiers
    python3 banc_ateliers.py interacteurs    # un ou plusieurs modules (--json fichier : résultats écrits)

Pour chaque page de niveau, à 390 px :
  - aucune erreur JavaScript, aucun défilement horizontal ;
  - un onglet par exercice, plus la clôture ;
  - chaque exercice : « Vérifier » à vide donne un retour 🔴 ; rempli juste (réponses tirées des définitions de la
    page, `exemple` des widgets texte/liste lu dans le module de données), il donne « Tout est juste » ;
  - la sauvegarde locale revient après un rechargement.
Pour chaque tableau à menus (widget « tableau ») : un menu par case à remplir, chacun nommé « ligne — colonne » ;
faux partout puis juste partout (marque et retour écrit dans la case) ; choix retrouvés au rechargement ; Tab et
flèche au clavier ; cartes sans débordement à 390 px ; à l'impression, le choix en texte, une ligne vide sans choix, et
pas la liste d'options de la fiche papier ; à 1280, 720 et 390 px, aucun mot coupé au milieu (chaque menu passe par
toutes ses options, puis les retours), un tableau qui tient dans son cadre et ne bouge pas ; pour les tableaux de
RETOURS_PAR_OPTION, un retour écrit et affiché pour chaque option fausse de chaque menu.
Pour un défi Bonus fait à l'écran (`champs`) : la carte se dessine à mesure, se sauvegarde, tient à 390 px ; sans
JavaScript et à l'impression, la consigne « sur ta feuille ».
Puis le QCM (30 questions), les deux synthèses et les cahiers de niveau : chargement sans erreur, sans débordement.

Code de sortie : 0 tout passe · 1 au moins un échec · 2 rien n'a été vérifié (règle d'or n°299).
"""
import importlib
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import build  # noqa: E402

RESULTATS = []


def t(nom, ok, detail=""):
    RESULTATS.append((nom, bool(ok)))
    print(("✔ " if ok else "✘ ") + nom + ("" if ok else "  — " + str(detail)[:220]))


def defs_page(pg):
    brut = pg.eval_on_selector("#donnees-page", "e => e.textContent")
    return json.loads(brut)["exercices"]


def exemples(at, niv):
    """{nom complet du widget : exemple} pour les widgets texte et liste du niveau."""
    ex = {}
    for e in at.NIVEAUX[niv]["exercices"]:
        uid = "%s_%s_%s" % (at.COURT, niv, e["id"])
        for w in e["widgets"]:
            if w.get("exemple"):
                ex["%s__%s" % (uid, w["name"])] = w["exemple"]
    return ex


def remplir(pg, uid, d, exs):
    """Remplit juste l'exercice uid ; rend la liste des widgets qu'il n'a pas su remplir."""
    rate = []
    sel = "#%s " % uid
    for w in d["widgets"]:
        ty = w["type"]
        if ty == "choix":
            pg.check(sel + 'input[name="%s"][value="%s"]' % (w["name"], w["bonne"]))
        elif ty == "cases":
            for val in w["toutes"]:
                loc = pg.locator(sel + 'input[name="%s"][value="%s"]' % (w["name"], val))
                (loc.check if val in w["bonnes"] else loc.uncheck)()
        elif ty == "classer":
            for it in w["items"]:
                pg.check(sel + 'input[name="%s"][value="%s"]' % (it["name"], it["bonne"]))
        elif ty == "slots":
            pris = {}   # dans un même groupe, chaque case reçoit une bonne réponse différente
            for s in w["slots"]:
                g = s.get("groupe")
                deja = pris.setdefault(g, set()) if g else set()
                rep = next((x for x in s["bonnes"] if x not in deja), s["bonnes"][0])
                deja.add(rep)
                pg.check(sel + 'input[name="%s"][value="%s"]' % (s["name"], rep))
        elif ty == "liste":
            texte = exs.get(w["name"]) or "\n".join(a["nom"] for a in w["attendus"])
            pg.fill("#" + w["name"], texte)
        elif ty == "texte":
            if w["name"] in exs:
                pg.fill("#" + w["name"], exs[w["name"]])
            else:
                rate.append(w["name"])
        elif ty in ("tableau", "menus"):
            for c in w["cases"]:
                pg.select_option(sel + 'select[name="%s"]' % c["name"], value=c["bonne"])
        elif ty == "croquis":
            pg.fill("#%s_desc" % w["name"], "Au centre de mon croquis, on voit l'objet en entier ; les légendes nomment chaque "
                                              "partie, et une flèche rouge montre le geste demandé.")
            for i in range(len(w["checklist"])):
                pg.check(sel + "#%s_check-%d" % (w["name"], i))
        else:
            rate.append(w.get("name", ty))
    return rate


def page_niveau(b, at, niv):
    chemin = build.page_niveau(at, niv)
    nom = "%s %s" % (at.SLUG, niv)
    ctx = b.new_context(viewport={"width": 390, "height": 900})
    pg = ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    pg.on("console", lambda m: err.append("console: " + m.text) if m.type == "error" else None)
    pg.goto(chemin.as_uri())
    pg.wait_for_timeout(250)
    t(nom + " : aucune erreur JavaScript au chargement", not err, err)
    t(nom + " : aucun défilement horizontal à 390 px", not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
    defs = defs_page(pg)
    exos = at.NIVEAUX[niv]["exercices"]
    onglets = pg.locator('[role="tab"]').count()
    t(nom + " : un onglet par exercice, plus la clôture (%d)" % (len(exos) + 1), onglets == len(exos) + 1, onglets)
    exs = exemples(at, niv)
    for i, e in enumerate(exos):
        uid = "%s_%s_%s" % (at.COURT, niv, e["id"])
        pg.locator('[role="tab"]').nth(i).click()
        pg.wait_for_timeout(60)
        pg.click("#%s button.verifier" % uid)
        r0 = pg.inner_text("#%s .retour" % uid)
        t(nom + " · %s : « Vérifier » à vide donne un retour à reprendre" % e["id"], "🔴" in r0, r0[:120])
        rate = remplir(pg, uid, defs[uid], exs)
        pg.click("#%s button.verifier" % uid)
        pg.wait_for_timeout(60)
        r1 = pg.inner_text("#%s .retour" % uid)
        t(nom + " · %s : rempli juste, « Tout est juste »%s" % (e["id"], " (sans exemple : %s)" % rate if rate else ""),
          "Tout est juste" in r1 and not rate, r1[:160])
    # sauvegarde : le premier exercice revient après rechargement
    pg.reload()
    pg.wait_for_timeout(250)
    uid0 = "%s_%s_%s" % (at.COURT, niv, exos[0]["id"])
    etat = pg.evaluate("k => localStorage.getItem(k)", "rep_%s_%s_%s" % (at.SLUG, niv, exos[0]["id"]))
    t(nom + " : la sauvegarde locale du premier exercice existe", bool(etat))
    reussi = False
    try:
        reussi = bool(json.loads(etat or "{}").get("reussi"))
    except ValueError:
        pass
    t(nom + " : le premier exercice est noté réussi après rechargement", reussi, (etat or "")[:120])
    t(nom + " : aucune erreur JavaScript pendant le parcours", not err, err)
    ctx.close()


#: Les tableaux qui donnent un retour écrit à CHAQUE option fausse de chaque menu (règle d'or n°317) : le banc le vérifie
#: dans les données, puis au navigateur, option par option.
RETOURS_PAR_OPTION = {("interacteurs-pieuvre", "4e", "e6"), ("exigences-sysml", "4e", "e3"),
                      ("exigences-sysml", "3e", "e4"), ("exigences-sysml", "3e", "e5"), ("fast", "3e", "e7")}

#: Un mot coupé au milieu : ses lettres tombent sur deux lignes. Chaque menu passe par toutes ses options, puis
#: « Vérifier » écrit les retours ; rend les mots coupés, et le nombre de mises en page des colonnes rencontrées.
JS_MOTS_COUPES = r"""s => {
  const t = document.querySelector(s);
  const coupe = () => {
    const out = [];
    const w = document.createTreeWalker(t, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = w.nextNode())) {
      const el = n.parentElement;
      if (!el || el.closest('.menu-mesure, .retour-mesure, select, option') || !el.getClientRects().length) continue;
      const re = /[\p{L}\p{N}’']+/gu; let m;
      while ((m = re.exec(n.textContent))) {
        if (m[0].length < 3) continue;
        const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
        if (new Set([...r.getClientRects()].filter(x => x.width > 0).map(x => Math.round(x.top))).size > 1) out.push(m[0]);
      }
    }
    return out;
  };
  const cols = () => [...t.querySelectorAll('tbody tr:first-child td')].map(td => Math.round(td.getBoundingClientRect().width)).join(',');
  const sels = [...t.querySelectorAll('select')], coupes = new Set(), mises = new Set([cols()]);
  const max = Math.max(1, ...sels.map(x => x.options.length));
  for (let k = 1; k < max; k++) {
    sels.forEach(x => { x.selectedIndex = Math.min(k, x.options.length - 1); x.dispatchEvent(new Event('change', {bubbles: true})); });
    coupe().forEach(x => coupes.add(x)); mises.add(cols());
  }
  t.closest('[data-exo]').querySelector('button.verifier').click();
  coupe().forEach(x => coupes.add(x + ' (retour)')); mises.add(cols());
  const f = t.querySelector('.defile');
  return [[...coupes], mises.size, f.scrollWidth - f.clientWidth];
}"""


def tableaux(b, at, niv):
    """Le widget « tableau » (cahier des charges à menus) : rendu, vérification fausse puis juste, sauvegarde,
    390 px, clavier, impression. Rien à faire si le niveau n'en a pas."""
    chemin = build.page_niveau(at, niv)
    exos = [e for e in at.NIVEAUX[niv]["exercices"] if any(w["type"] == "tableau" for w in e["widgets"])]
    if not exos:
        return
    for e in exos:
        uid = "%s_%s_%s" % (at.COURT, niv, e["id"])
        nom = "%s %s · %s (tableau à menus)" % (at.SLUG, niv, e["id"])
        for largeur in (1280, 720, 390):
            ctx = b.new_context(viewport={"width": largeur, "height": 900})
            pg = ctx.new_page()
            err = []
            pg.on("pageerror", lambda x: err.append(str(x)))
            pg.goto(chemin.as_uri())
            pg.evaluate("localStorage.clear()")
            pg.goto(chemin.as_uri())
            pg.wait_for_timeout(200)
            idx = pg.evaluate("u => [...document.querySelectorAll('[role=tab]')].findIndex(t => "
                              "document.getElementById(t.getAttribute('aria-controls')).contains(document.getElementById(u)))", uid)
            pg.locator('[role="tab"]').nth(idx).click()
            pg.wait_for_timeout(60)
            d = defs_page(pg)[uid]
            tw = [w for w in d["widgets"] if w["type"] == "tableau"]
            cases = [c for w in tw for c in w["cases"]]
            sel = "#%s .tableau-menus" % uid
            if largeur == 720:
                coupes, mises, deb = pg.evaluate(JS_MOTS_COUPES, sel)
                t(nom + " (720 px) : aucun mot coupé au milieu, chaque menu passant par toutes ses options, puis les retours",
                  not coupes, coupes[:6])
                t(nom + " (720 px) : le tableau tient dans son cadre — en cartes s'il ne tiendrait pas sans couper un mot",
                  deb <= 1, "%d px de trop" % deb)
                t(nom + " (720 px) : aucune erreur JavaScript", not err, err)
                ctx.close()
                continue
            if largeur == 390:
                t(nom + " (390 px) : aucun défilement horizontal de la page",
                  not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
                cartes = pg.evaluate("s => [...document.querySelectorAll(s + ' table.cdcf')].every(t => "
                                     "getComputedStyle(t.querySelector('tr')).display === 'block' && "
                                     "getComputedStyle(t.querySelector('thead')).display === 'none')", sel)
                deb = pg.evaluate("s => [...document.querySelectorAll(s + ' .defile')].some(f => f.scrollWidth > f.clientWidth + 1)", sel)
                t(nom + " (390 px) : chaque ligne devient une carte, rien ne déborde du cadre", cartes and not deb)
                noms_col = pg.evaluate("s => [...document.querySelectorAll(s + ' td')].every(td => "
                                       "getComputedStyle(td, '::before').content.replace(/\"/g, '') === td.dataset.col)", sel)
                t(nom + " (390 px) : chaque case de carte porte le nom de sa colonne", noms_col)
                coupes, mises, deb = pg.evaluate(JS_MOTS_COUPES, sel)
                t(nom + " (390 px) : aucun mot coupé au milieu, chaque menu passant par toutes ses options, puis les retours",
                  not coupes, coupes[:6])
                t(nom + " (390 px) : aucune erreur JavaScript", not err, err)
                ctx.close()
                continue
            # ── rendu
            n_sel = pg.locator(sel + " select").count()
            t(nom + " : un menu par case à remplir (%d), et pas plus" % len(cases), n_sel == len(cases), n_sel)
            lus = pg.evaluate("s => [...document.querySelectorAll(s + ' select')].map(x => [x.getAttribute('aria-label') || '', "
                              "x.options[0].value, x.getAttribute('aria-describedby') || ''])", sel)
            t(nom + " : chaque menu a un nom lisible « ligne — colonne » et commence vide",
              all(" — " in a and v == "" and r.endswith("-retour") for a, v, r in lus), lus[:2])
            donnees = pg.evaluate("s => [...document.querySelectorAll(s + ' td:not(.case-menu)')].filter(td => td.textContent.trim()).length", sel)
            t(nom + " : les cases données restent du texte (%d)" % donnees, donnees > 0)
            # ── vérification fausse : chaque case reçoit une mauvaise option
            for c in cases:
                opts = pg.eval_on_selector_all('#%s select[name="%s"] option' % (uid, c["name"]), "l => l.map(o => o.value).filter(Boolean)")
                pg.select_option('#%s select[name="%s"]' % (uid, c["name"]), value=next(o for o in opts if o != c["bonne"]))
            pg.click("#%s button.verifier" % uid)
            pg.wait_for_timeout(80)
            etat = pg.evaluate("""s => [...document.querySelectorAll(s + ' select')].map(x => {
                const td = x.closest('td'), r = td.querySelector('.retour-case'), en = td.querySelector('.encoche');
                return [td.classList.contains('faux'), !!r && r.classList.contains('visible') && r.textContent.trim().startsWith('✘')
                        && r.textContent.trim().length > 12, !!en && en.textContent.includes('à revoir')]; })""", sel)
            t(nom + " : faux partout, chaque case dit « ✘ à revoir » et son retour écrit, dans la case",
              etat and all(a and r and en for a, r, en in etat), [x for x in etat if not all(x)][:2])
            t(nom + " : faux partout, le retour général demande de reprendre", "🔴" in pg.inner_text("#%s .retour" % uid))
            # ── juste
            for c in cases:
                pg.select_option('#%s select[name="%s"]' % (uid, c["name"]), value=c["bonne"])
            pg.click("#%s button.verifier" % uid)
            pg.wait_for_timeout(80)
            justes = pg.evaluate("s => [...document.querySelectorAll(s + ' td.case-menu')].every(td => td.classList.contains('juste') "
                                 "&& !td.querySelector('.retour-case.visible') && td.querySelector('.encoche').textContent.includes('juste'))", sel)
            t(nom + " : juste partout, chaque case est marquée « ✔ juste », sans retour d'erreur", justes)
            # ── sauvegarde et rechargement (on guette la restauration du dernier menu au lieu d'un délai fixe, trop court
            #    quand la machine est chargée)
            pg.reload()
            try:
                pg.wait_for_function("([n, v]) => { const x = document.getElementsByName(n)[0]; return x && x.value === v; }",
                                     arg=[cases[-1]["name"], cases[-1]["bonne"]], timeout=5000)
            except Exception:
                pass
            pg.locator('[role="tab"]').nth(idx).click()
            revenus = pg.evaluate("""s => [...document.querySelectorAll(s + ' select')].map(x => [x.name, x.value,
                x.parentNode.querySelector('.menu-vu').textContent === x.options[x.selectedIndex].text])""", sel)
            bonnes = {c["name"]: c["bonne"] for c in cases}
            t(nom + " : après rechargement, chaque menu retrouve son choix, écrit en entier dans la case",
              all(v == bonnes[n] and vu for n, v, vu in revenus), [x for x in revenus if x[1] != bonnes[x[0]] or not x[2]][:2])
            # ── clavier : Tab mène au menu suivant, la flèche change le choix, le cadre montre le focus
            premier, second = cases[0]["name"], cases[1]["name"]
            pg.focus('#%s select[name="%s"]' % (uid, premier))
            pg.keyboard.press("Tab")
            focus = pg.evaluate("() => document.activeElement && document.activeElement.name")
            t(nom + " : au clavier, Tab passe d'un menu au suivant", focus == second, focus)
            avant = pg.input_value('#%s select[name="%s"]' % (uid, second))
            pg.keyboard.press("ArrowDown" if pg.evaluate("n => document.getElementsByName(n)[0].selectedIndex", second) <
                              pg.evaluate("n => document.getElementsByName(n)[0].options.length - 1", second) else "ArrowUp")
            pg.wait_for_timeout(60)
            apres = pg.input_value('#%s select[name="%s"]' % (uid, second))
            vu = pg.evaluate("n => { const x = document.getElementsByName(n)[0]; return x.parentNode.querySelector('.menu-vu').textContent "
                             "=== (x.value ? x.options[x.selectedIndex].text : ''); }", second)
            contour = pg.evaluate("n => getComputedStyle(document.getElementsByName(n)[0].parentNode).outlineStyle", second)
            t(nom + " : au clavier, la flèche change le choix, la case l'écrit, et le cadre montre le focus",
              avant != apres and vu and contour not in ("none", ""), (avant, apres, vu, contour))
            # ── impression : le choix s'imprime ; sans réponse, une ligne vide
            pg.select_option('#%s select[name="%s"]' % (uid, second), value="")
            pg.evaluate("""n => { const x = document.getElementsByName(n)[0], c = document.createElement('span');
                c.className = 'pp-papier pp-choix'; c.innerHTML = '<span class="pp-case">F0</span> <span class="pp-case">F1</span>';
                x.insertAdjacentElement('afterend', c); }""", premier)
            pg.emulate_media(media="print")
            pp = pg.evaluate("n => getComputedStyle(document.getElementsByName(n)[0].parentNode.querySelector('.pp-choix')).display", premier)
            imp = pg.evaluate("""([s, n1, n2]) => {
                const a = document.getElementsByName(n1)[0], b = document.getElementsByName(n2)[0];
                const va = a.parentNode.querySelector('.menu-vu'), vb = b.parentNode.querySelector('.menu-vu');
                const cs = getComputedStyle(vb);
                return [getComputedStyle(a).display, va.textContent === a.options[a.selectedIndex].text && va.getBoundingClientRect().height > 0,
                        vb.textContent === '' && parseFloat(cs.borderBottomWidth) > 0 && vb.getBoundingClientRect().width > 40,
                        getComputedStyle(va, '::before').content]; }""", [sel, premier, second])
            pg.emulate_media(media="screen")
            t(nom + " : à l'impression, le menu disparaît, le choix s'imprime en texte, une case vide donne une ligne à remplir",
              imp[0] == "none" and imp[1] and imp[2], imp)
            t(nom + " : à l'impression, la liste des options que la fiche papier pose sous un menu (.pp-choix) ne s'imprime pas",
              pp == "none", pp)
            pg.evaluate("() => document.querySelectorAll('.pp-choix').forEach(x => x.remove())")
            if (at.SLUG, niv, e["id"]) in RETOURS_PAR_OPTION:
                manque, total = [], 0
                for c in cases:
                    opts = pg.eval_on_selector_all('#%s select[name="%s"] option' % (uid, c["name"]), "l => l.map(o => o.value).filter(Boolean)")
                    for o in opts:
                        if o != c["bonne"]:
                            total += 1
                            if not (c.get("retours") or {}).get(o):
                                manque.append("%s=%s" % (c["name"].split("__")[-1], o))
                t(nom + " : un retour écrit pour chaque option fausse de chaque menu (%d / %d)" % (total - len(manque), total),
                  total and not manque, manque[:4])
                essais, rates = pg.evaluate("""([s, defs]) => {
                    const t = document.querySelector(s), btn = t.closest('[data-exo]').querySelector('button.verifier');
                    const sels = [...t.querySelectorAll('select')];
                    const faux = sels.map(x => [...x.options].map(o => o.value).filter(v => v && v !== defs[x.name].bonne));
                    let n = 0; const rates = [];
                    for (let k = 0; k < Math.max(...faux.map(f => f.length)); k++) {
                      sels.forEach((x, i) => { x.value = faux[i][Math.min(k, faux[i].length - 1)]; x.dispatchEvent(new Event('change', {bubbles: true})); });
                      btn.click();
                      sels.forEach((x, i) => { if (k >= faux[i].length) return; n++;
                        const r = x.closest('td').querySelector('.retour-case');
                        if (!r.classList.contains('visible') || r.textContent !== '✘ ' + (defs[x.name].retours || {})[x.value]) rates.push(x.name.split('__').pop() + '=' + x.value); });
                    }
                    return [n, rates]; }""", [sel, {c["name"]: c for c in cases}])
                t(nom + " : chaque option fausse, choisie puis vérifiée, écrit son propre retour sous sa case (%d essais)" % essais,
                  essais == total and not rates, rates[:4])
            coupes, mises, deb = pg.evaluate(JS_MOTS_COUPES, sel)
            t(nom + " : aucun mot coupé au milieu, chaque menu passant par toutes ses options, puis les retours",
              not coupes, coupes[:6])
            t(nom + " : le tableau tient dans son cadre, et ses colonnes ne bougent ni quand on choisit ni quand on vérifie",
              deb <= 1 and mises == 1, "débordement %d px, %d mises en page" % (deb, mises))
            t(nom + " : aucune erreur JavaScript", not err, err)
            ctx.close()


def bonus_vivants(b, at, niv):
    """Un défi Bonus fait à l'écran (`champs` dans les données) : ce que l'élève écrit se dessine dans le schéma, se
    sauvegarde ; sans JavaScript et sur le papier, la consigne « papier » reste, les champs disparaissent."""
    defis = [(i, d) for i, d in enumerate(at.NIVEAUX[niv].get("bonus", [])) if d.get("champs")]
    if not defis:
        return
    chemin = build.page_niveau(at, niv)
    pid = "rep_%s_%s" % (at.SLUG, niv)
    for i, d in defis:
        nom = "%s %s · Bonus, défi %d (la carte se dessine)" % (at.SLUG, niv, i + 1)
        ids = [["%s__bonus%d_%s" % (pid, i, c["name"]), c["cible"], c["exemple"]] for c in d["champs"]]
        for largeur in (1280, 390):
            ctx = b.new_context(viewport={"width": largeur, "height": 900})
            pg = ctx.new_page()
            err = []
            pg.on("pageerror", lambda x: err.append(str(x)))
            pg.goto(chemin.as_uri())
            pg.evaluate("localStorage.clear()")
            pg.goto(chemin.as_uri())
            pg.wait_for_timeout(200)
            pg.locator('[role="tab"]').last.click()
            pg.wait_for_timeout(60)
            vide = pg.evaluate("""ids => ids.map(([f, c]) => [!!document.querySelector('label[for="' + f + '"]'),
                document.getElementById(f).getAttribute('data-miroir') === c, document.getElementById(c).textContent.trim()])""", ids)
            t(nom + " (%d px) : un champ nommé pour chaque case de la carte (%d), et la carte vide attend" % (largeur, len(ids)),
              all(a and m and txt for a, m, txt in vide) and pg.is_visible(".bonus-vivant .consigne-ecran")
              and not pg.is_visible(".bonus-vivant .consigne-papier"), vide)
            for f, c, ex in ids:
                pg.fill("#" + f, ex)
            pg.wait_for_timeout(60)
            dessin = pg.evaluate("ids => ids.map(([f, c, ex]) => [document.getElementById(c).textContent.replace(/\\s+/g, ''), "
                                 "ex.replace(/\\s+/g, '')])", ids)
            t(nom + " (%d px) : ce que l'élève écrit se dessine dans la carte, case par case, à mesure" % largeur,
              all(a == x for a, x in dessin), dessin)
            if largeur == 390:
                tient = pg.evaluate("() => { const f = document.querySelector('.bonus-vivant figure'), s = f.querySelector('svg'); "
                                    "return f.scrollWidth <= f.clientWidth + 1 && s.getBoundingClientRect().width <= f.clientWidth + 1; }")
                t(nom + " (390 px) : la carte entière tient à l'écran, sans défiler, et la page ne défile pas de côté",
                  tient and not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
            pg.reload()
            try:
                pg.wait_for_function("([f, v]) => { const x = document.getElementById(f); return x && x.value === v; }",
                                     arg=[ids[-1][0], ids[-1][2]], timeout=5000)
            except Exception:
                pass
            pg.locator('[role="tab"]').last.click()
            revenu = pg.evaluate("ids => ids.map(([f, c, ex]) => document.getElementById(f).value === ex && "
                                 "document.getElementById(c).textContent.replace(/\\s+/g, '') === ex.replace(/\\s+/g, ''))", ids)
            t(nom + " (%d px) : après rechargement, chaque réponse revient, et la carte se redessine" % largeur, all(revenu), revenu)
            if largeur == 1280:
                pg.emulate_media(media="print")
                imp = [pg.is_visible(".bonus-vivant .consigne-papier"), not pg.is_visible(".bonus-vivant .consigne-ecran"),
                       not pg.is_visible(".bonus-vivant .bonus-champs"), pg.is_visible(".bonus-vivant figure svg")]
                pg.emulate_media(media="screen")
                t(nom + " : à l'impression, la consigne « sur ta feuille » et la carte (avec ce qui est écrit), sans les champs",
                  all(imp), imp)
            t(nom + " (%d px) : aucune erreur JavaScript" % largeur, not err, err)
            ctx.close()
        ctx = b.new_context(java_script_enabled=False, viewport={"width": 1280, "height": 900})
        pg = ctx.new_page()
        pg.goto(chemin.as_uri())
        sans = [pg.is_visible(".bonus-vivant .consigne-papier"), not pg.is_visible(".bonus-vivant .consigne-ecran"),
                not pg.is_visible(".bonus-vivant .bonus-champs"), pg.is_visible(".bonus-vivant figure svg"),
                pg.is_visible(".card.bonus details.corrige-bonus")]
        t(nom + " : sans JavaScript, le Bonus se lit (onglets dépliés), la consigne dit « sur ta feuille », la carte et la "
          "correction restent", all(sans) and "sur ta feuille" in pg.inner_text(".bonus-vivant .consigne-papier").lower(), sans)
        ctx.close()


# ─────────────────────────────────────────────────────────────────────────────
# Les mots de référence de la bête à cornes (04/11/2026) : le dessin de référence, les exercices de mots (menus dans les
# cases du gabarit vide), les piqûres de rappel des séquences et des panneaux, les questions des QCM.
# ─────────────────────────────────────────────────────────────────────────────
#: le gabarit de la n°318 : les ellipses et le rectangle, en unités du dessin
FORMES_BAC = {"aqui": ("e", 350, 284.5, 134, 59.5), "surquoi": ("e", 825.5, 284.5, 134, 59.5),
              "objet": ("e", 583, 476, 122, 73), "but": ("r", 250, 573, 732, 132)}
JS_REF = """id => { const s = document.getElementById(id); if (!s) return null; const f = s.closest('figure');
  return {mots: [...s.querySelectorAll('text')].map(t => t.textContent).join(' '), vb: s.getAttribute('viewBox'),
          titre: f ? f.querySelector('figcaption').textContent : '',
          ell: [...s.querySelectorAll('ellipse')].map(e => ['cx','cy','rx','ry'].map(a => e.getAttribute(a)).join(','))}; }"""
#: chaque case d'un widget « menus » : son menu est-il dans sa forme (les quatre coins), en unités du dessin ?
JS_MENUS_DANS = """([uid, F]) => { const b = document.getElementById(uid), svg = b.querySelector('.ms-dessin svg').getBoundingClientRect(),
  k = svg.width / 960;
  return [...b.querySelectorAll('.ms-case')].map(c => { const r = c.querySelector('select').getBoundingClientRect(),
    f = F[c.dataset.pour.split('__')[1]];
    const P = [[r.left, r.top], [r.right, r.top], [r.left, r.bottom], [r.right, r.bottom]].map(([x, y]) => [50 + (x - svg.left) / k, 150 + (y - svg.top) / k]);
    return getComputedStyle(c).position === 'absolute' && (f[0] === 'e' ? P.every(([x, y]) => ((x - f[1]) / f[3]) ** 2 + ((y - f[2]) / f[4]) ** 2 <= 1)
      : P.every(([x, y]) => x > f[1] && x < f[1] + f[3] && y > f[2] && y < f[2] + f[4])); }); }"""


def ref_ok(r, apte=True):
    """Le dessin de référence : le gabarit (cadre et ellipses de la n°318), ses quatre mots, son titre."""
    return (r and r["vb"] == "50 150 960 570" and all(m in r["mots"] for m in ("Utilisateur", "Matière", "d'œuvre", "Produit", "Fonction"))
            and r["ell"][:1] == ["350,284.5,134,59.5"] and "La bête à cornes (méthode APTE" in r["titre"]
            and (not apte or "APplication aux Techniques d'Entreprise" in r["titre"]))


def exo_menus(b, chemin, uid, w_def, nom):
    """Un exercice de mots : à 1280 px, les menus dans leurs formes, un retour par option (le texte des données), le
    miroir ; à 390 px, les menus sous le dessin, sans défilement ; le choix revient au rechargement ; l'impression."""
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    pg.goto(chemin.as_uri())
    pg.wait_for_timeout(250)
    pg.evaluate("id => { const p = document.getElementById(id).closest('[role=tabpanel]'); if (p) document.getElementById('tab-' + p.id).click(); }", uid)
    pg.wait_for_timeout(80)
    t(nom + " : à 1280 px, chaque menu est posé dans sa case (les quatre coins dans l'ellipse ou le rectangle)",
      all(pg.evaluate(JS_MENUS_DANS, [uid, FORMES_BAC])))
    bons, n = True, 0
    for c in w_def["cases"]:
        sel = "#%s select[name=\"%s\"]" % (uid, c["name"])
        for v in pg.eval_on_selector_all(sel + " option", "l => l.map(o => o.value).filter(Boolean)"):
            pg.select_option(sel, v)
            pg.click("#%s button.verifier" % uid)
            vu = pg.inner_text('#%s .retour-case[data-pour="%s"]' % (uid, c["name"]))
            attendu = c["ok"] if v == c["bonne"] else c["retours"][v]
            n += v != c["bonne"]
            if attendu[:50] not in vu or (vu.startswith("✔") != (v == c["bonne"])):
                bons = False
                print("   ", nom, c["name"], v, "→", vu[:70])
        pg.select_option(sel, c["bonne"])
    t(nom + " : chaque mot faux a son retour, propre à sa case (%d retours), et chaque bon mot le sien" % n, bons and n == 6 * len(w_def["cases"]))
    pg.click("#%s button.verifier" % uid)
    mir = pg.evaluate("uid => [...document.querySelectorAll('#' + uid + ' .ms-dessin svg text[data-car]')]"
                      ".map(t => [...t.querySelectorAll('tspan')].map(x => x.textContent).join(' '))", uid)
    t(nom + " : le mot choisi s'écrit dans sa case du dessin (miroir)", mir == ["Utilisateur", "Matière d'œuvre", "Produit", "Fonction"], mir)
    t(nom + " : les quatre mots justes donnent 4 ✔ sous le dessin", pg.locator("#%s .ms-retours .retour-case.juste" % uid).count() == 4)
    pg.reload()
    pg.wait_for_timeout(300)
    t(nom + " : les choix reviennent après un rechargement",
      pg.evaluate("uid => [...document.querySelectorAll('#' + uid + ' .ms-case select')].map(s => s.value).join(',')", uid) == "util,mo,prod,fonc")
    pg.emulate_media(media="print")
    t(nom + " : à l'impression, les menus disparaissent et la consigne « Sur ta feuille » s'imprime",
      not pg.is_visible("#%s .ms-case" % uid) and "Sur ta feuille" in pg.inner_text("#%s .ms-papier" % uid))
    pg.emulate_media(media="screen")
    pg.set_viewport_size({"width": 390, "height": 900})
    pg.wait_for_timeout(150)
    t(nom + " : à 390 px, les menus passent sous le dessin, sans défilement de côté",
      pg.evaluate("uid => [...document.querySelectorAll('#' + uid + ' .ms-case')].every(c => getComputedStyle(c).position === 'static')", uid)
      and not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
    t(nom + " : aucune erreur JavaScript", not err, err)
    ctx.close()


def rappel_incruste(b, chemin, uid, nom, avant=None):
    """Une piqûre de rappel incrustée (séquence ou panneau) : présente, à vide 🔴, juste « Tout est juste », la clé de
    sauvegarde de l'atelier, sans défilement de côté à 390 px ; `avant` : l'exercice qui la suit."""
    ctx = b.new_context(viewport={"width": 390, "height": 900})
    pg = ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    pg.goto(chemin.as_uri())
    pg.wait_for_timeout(300)
    pg.evaluate("localStorage.clear()")
    present = pg.locator("#" + uid).count() == 1
    t(nom + " : la piqûre de rappel est dans la page", present)
    if not present:
        ctx.close()
        return
    if avant:
        t(nom + " : elle vient juste avant l'exercice où la bête à cornes revient",
          pg.evaluate("([a, c]) => !!(document.getElementById(a).compareDocumentPosition(document.getElementById(c)) & 4)", [uid, avant]))
    # la séance qui la porte, ouverte comme le ferait l'élève
    pg.evaluate("""uid => { const p = document.getElementById(uid).closest('.seance-panel,[role=tabpanel]');
      if (!p) return; const t = document.querySelector('[data-panel="' + p.id + '"], #tab-' + p.id); if (t) t.click(); }""", uid)
    pg.wait_for_timeout(120)
    # un rappel replié (option `replie`, 08/11/2026) s'ouvre comme le ferait l'élève qui a oublié les mots
    pg.evaluate("uid => { const r = document.getElementById(uid).closest('details.incruste-repliee'); if (r) r.open = true; }", uid)
    d = pg.evaluate("uid => JSON.parse(document.getElementById(uid).closest('.atelier-incruste').querySelector('script[type=\"application/json\"]').textContent).exercices[uid]", uid)
    pg.click("#%s button.verifier" % uid)
    t(nom + " : « Vérifier » à vide donne un retour à reprendre", "🔴" in pg.inner_text("#%s .retour" % uid))
    rate = remplir(pg, uid, d, {})
    pg.click("#%s button.verifier" % uid)
    pg.wait_for_timeout(60)
    t(nom + " : rempli juste, « Tout est juste »", "Tout est juste" in pg.inner_text("#%s .retour" % uid) and not rate)
    t(nom + " : la réponse est sauvegardée sous la clé de l'atelier (%s)" % d["cle"],
      bool(json.loads(pg.evaluate("k => localStorage.getItem(k)", d["cle"]) or "{}").get("reussi")))
    t(nom + " : à 390 px, aucun défilement de côté", not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
    t(nom + " : aucune erreur JavaScript", not err, err)
    ctx.close()


def mots_de_reference(b):
    import donnees_besoin as at
    besoin = build.page_niveau
    # 1. le dessin de référence, là où l'outil est présenté
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    pg.goto(besoin(at, "5e").as_uri())
    pg.wait_for_timeout(200)
    t("dessin de référence, atelier 5e : dans la situation, avant les exercices — le gabarit, ses quatre mots, « La bête à "
      "cornes (méthode APTE) », APTE développé", ref_ok(pg.evaluate(JS_REF, "bc-ref"))
      and pg.evaluate("!!document.querySelector('.rappel-ouverture #bc-ref') && !!(document.getElementById('bc-ref').compareDocumentPosition(document.querySelector('.onglets')) & 4)"))
    t("atelier 5e : le premier onglet est « Pour commencer », l'exercice des mots ; les autres gardent leurs numéros",
      pg.evaluate("[...document.querySelectorAll('[role=tab]')].map(o => o.firstChild.textContent).slice(0, 2).join('|')") == "Pour commencer|Exercice 1")
    for niv in ("4e", "3e"):
        pg.goto(besoin(at, niv).as_uri())
        pg.wait_for_timeout(200)
        t("dessin de référence, atelier %s : dans le cours (« Rappel »), APTE développé" % niv,
          ref_ok(pg.evaluate(JS_REF, "bc-ref-k" + niv[0])) and pg.evaluate("id => !!document.getElementById(id).closest('details.cours')", "bc-ref-k" + niv[0]))
        t("atelier %s : le premier onglet est « 🧠 Rappel », les autres gardent leurs numéros" % niv,
          pg.evaluate("[...document.querySelectorAll('[role=tab]')].map(o => o.firstChild.textContent).slice(0, 2).join('|')") == "🧠 Rappel|Exercice 1")
    pg.goto(build.cahier("5e").as_uri())
    pg.wait_for_timeout(200)
    t("dessin de référence, cahier de 5e : dans la carte de l'atelier « Le besoin », avant ses exercices",
      ref_ok(pg.evaluate(JS_REF, "bc-ref-c5")) and pg.evaluate("!!(document.getElementById('bc-ref-c5').compareDocumentPosition(document.getElementById('bc_5e_mots')) & 4)"))
    for niv in ("4e", "3e"):
        pg.goto(build.cahier(niv).as_uri())
        pg.wait_for_timeout(150)
        t("cahier de %s : la piqûre de rappel, avec le dessin de référence dans sa correction" % niv,
          ref_ok(pg.evaluate(JS_REF, "bc-m%s-c" % niv[0]), apte=False))
    pg.goto(build.CARTE.as_uri())
    pg.wait_for_timeout(150)
    t("dessin de référence, carte des représentations : sous le tableau « Analyse externe », APTE développé dans le tableau",
      ref_ok(pg.evaluate(JS_REF, "bc-ref")) and "APplication aux Techniques d'Entreprise" in pg.inner_text("table"))
    shanghai = build.DEPOT / "theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/5e/5e_C3.1/sequence_5e_C3.1-C3.4_shanghai.html"
    pg.goto(shanghai.as_uri())
    pg.wait_for_timeout(200)
    t("dessin de référence, 5e_C3.1 Shanghai : avant l'exercice du vélo-cargo de Léa",
      ref_ok(pg.evaluate(JS_REF, "bc-ref")) and pg.evaluate("!!(document.getElementById('bc-ref').compareDocumentPosition(document.getElementById('bc_5e_e1')) & 4)"))
    # 2. les QCM : une question sur les mots de référence, des leurres réfutés, une clé nouvelle
    pg.goto(build.qcm(at).as_uri())
    pg.wait_for_timeout(200)
    q = pg.evaluate("(() => { const x = QUESTIONS.find(q => q.n === \"La matière d'œuvre\"); return x && [x.o[x.r], x.d.join(' | '), x.expl, KEY]; })()")
    t("QCM « Le besoin » : « La matière d'œuvre », leurres utilisateur, matériau, fonction réfutés, APTE développé, nouvelle clé",
      q and q[0].startswith("ce sur quoi il agit") and "utilisateur" in q[1] and "matériau" in q[1] and "fonction d'usage" in q[1]
      and "APplication aux Techniques d'Entreprise" in q[2] and q[3] == "qcm_besoin-bete-a-cornes_mots", str(q)[:160])
    q = pg.evaluate("(() => { const x = QUESTIONS.find(q => q.n === 'Le but devient…'); return x && [x.o[x.r], x.d.join(' | ')]; })()")
    t("QCM « Le besoin » : la case Fonction est la fonction d'usage, la fonction technique est un leurre réfuté",
      q and q[0] == "la fonction d'usage de l'objet" and "fonction technique" in q[1], str(q)[:120])
    import donnees_interacteurs as ati
    pg.goto(build.qcm(ati).as_uri())
    pg.wait_for_timeout(200)
    q = pg.evaluate("(() => { const x = QUESTIONS.find(q => q.n === 'La bête à cornes dans la pieuvre'); return x && [x.q, x.o[x.r], x.expl, KEY]; })()")
    t("QCM « pieuvre » : la bête à cornes → FP1 dite avec les mots de référence, nouvelle clé",
      q and "utilisatrice" in q[0] and "matière d'œuvre" in q[1] and "utilisateur" in q[2] and q[3] == "qcm_interacteurs-pieuvre_mots", str(q)[:160])
    ctx.close()
    # 3. les exercices de mots des trois ateliers
    for niv, exo in (("5e", "mots"), ("4e", "rappel"), ("3e", "rappel")):
        ex = next(x for x in at.NIVEAUX[niv]["exercices"] if x["id"] == exo)
        w = next(x for x in ex["widgets"] if x["type"] == "menus")
        uid = "bc_%s_%s" % (niv, exo)
        w_def = {"cases": [dict(name="%s__%s" % (uid, c["name"]), bonne=c["bonne"], ok=c["ok"], retours=c["retours"]) for c in w["cases"]]}
        exo_menus(b, besoin(at, niv), uid, w_def, "atelier %s, exercice des mots" % niv)
    # 4. les piqûres de rappel sur l'objet de la séquence : dans les panneaux des codes, et dans les séquences
    seqs = {"rappel-feux": ("4e", "theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/4e/4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html", "bc_4e_e4"),
            "rappel-velos": ("4e", "theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/4e/4e_C3.1/sequence_4e_C3.1-C3.3_hangzhou.html", "bc_4e_e5"),
            "rappel-local": ("3e", "theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/3e/3e_C3.1/sequence_3e_C3.1-C3.4_shenzhen.html", "bc_3e_e6")}
    for code, exo in at.RAPPEL_PANNEAU.items():
        niv, seq, suivant = seqs[exo]
        uid = "bc_%s_%s" % (niv, exo)
        rappel_incruste(b, build.DEPOT / seq, uid, "séquence %s, rappel « %s »" % (pathlib.Path(seq).name.split("_")[1], exo), avant=suivant)
        rappel_incruste(b, build.moteur.dossier_code(code) / build.nom_panneau(at), uid, "panneau %s, rappel « %s »" % (code, exo))


def page_simple(b, chemin, nom, attendu_q=None):
    if not chemin.exists():
        t(nom + " : la page existe", False, chemin)
        return
    for largeur in (390, 1280):
        ctx = b.new_context(viewport={"width": largeur, "height": 900})
        pg = ctx.new_page()
        err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto(chemin.as_uri())
        pg.wait_for_timeout(250)
        t("%s (%d px) : aucune erreur JavaScript" % (nom, largeur), not err, err)
        t("%s (%d px) : aucun défilement horizontal" % (nom, largeur),
          not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))
        if attendu_q and largeur == 390:
            n = pg.evaluate("typeof QUESTIONS !== 'undefined' ? QUESTIONS.length : -1")
            t("%s : %d questions" % (nom, attendu_q), n == attendu_q, n)
        ctx.close()


def main(modules, cahiers=False, sortie_json=None):
    construits = []
    for m in modules:
        try:
            at = importlib.import_module("donnees_" + m)
        except ModuleNotFoundError:
            continue
        if all(build.page_niveau(at, niv).exists() for niv in at.NIVEAUX):
            construits.append(at)
    if not construits:
        print("Aucun atelier construit à vérifier.")
        return 2
    with sync_playwright() as p:
        b = p.chromium.launch()
        for at in construits:
            for niv in at.NIVEAUX:
                page_niveau(b, at, niv)
                tableaux(b, at, niv)
                bonus_vivants(b, at, niv)
            page_simple(b, build.qcm(at), at.SLUG + " QCM", attendu_q=30)
            page_simple(b, build.synthese_eleve(at), at.SLUG + " synthèse élève")
            page_simple(b, build.synthese_prof(at), at.SLUG + " synthèse professeur")
            if at.SLUG == "besoin-bete-a-cornes":
                mots_de_reference(b)
        if cahiers:
            for niv in ("5e", "4e", "3e"):
                if build.cahier(niv).exists():
                    page_simple(b, build.cahier(niv), "cahier " + niv)
        b.close()
    ok = sum(1 for _, r in RESULTATS if r)
    print("\n%d / %d tests passés" % (ok, len(RESULTATS)))
    echecs = [n for n, r in RESULTATS if not r]
    if echecs:
        print("Échecs :\n  - " + "\n  - ".join(echecs))
    if sortie_json:
        pathlib.Path(sortie_json).write_text(json.dumps([{"test": n, "ok": r} for n, r in RESULTATS],
                                                        ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not echecs else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    sortie = None
    if "--json" in args:
        i = args.index("--json")
        sortie = args[i + 1]
        del args[i:i + 2]
    # sans module nommé : tous les ateliers, et les cahiers de niveau
    sys.exit(main(args or build.MODULES, cahiers=not args, sortie_json=sortie))
