#!/usr/bin/env python3
"""Suite de tests du lot Shenzhen 5e_C2.1 · C2.2.

    python3 tests_5e_C2.1-C2.2_shenzhen.py

À lancer depuis le dossier du lot. Les chemins sont relatifs à ce dossier.
"""
from playwright.sync_api import sync_playwright
import pathlib
import sys

SEQ = pathlib.Path("sequence_5e_C2_shenzhen_station_velos.html").resolve().as_uri()
QCM = pathlib.Path("qcm_5e_C2_shenzhen_station_velos.html").resolve().as_uri()
SYE = pathlib.Path("Synthèses/synthese_eleve_5e_C2.1-C2.2.html").resolve().as_uri()
SYP = pathlib.Path("Synthèses/synthese_professeur_5e_C2.1-C2.2.html").resolve().as_uri()

res = []

# La bête à cornes de la séance 1 : le gabarit de Pascal (04/11/2026), cadre 50 150 960 570. Les formes, au dixième près.
GABARIT = {"ellipse": [("350", "284.5", "134", "59.5"), ("825.5", "284.5", "133.5", "59.5"), ("583", "476", "122", "73")],
           "rect": [("250", "573", "732", "132")]}
JS_GABARIT = '''(id)=>{const s=document.querySelector('#'+id+' .bac-svg'); if(!s) return null;
  return {vb:s.getAttribute('viewBox'),
          e:[...s.querySelectorAll('ellipse')].map(x=>['cx','cy','rx','ry'].map(a=>x.getAttribute(a))),
          r:[...s.querySelectorAll('rect.bac-contour')].map(x=>['x','y','width','height'].map(a=>x.getAttribute(a))),
          corneApresProduit: (()=>{const tr=[...s.querySelectorAll('path.bac-trait')], el=[...s.querySelectorAll('ellipse')];
            return tr.length===2 && !!(el[2].compareDocumentPosition(tr[0]) & 4);})(),
          bleu:[...s.querySelectorAll('path.bac-trait')].map(x=>x.getAttribute('stroke')),
          contour:[...s.querySelectorAll('.bac-contour')].every(x=>x.getAttribute('stroke')==='#1f3864' && x.getAttribute('fill')==='#fff')};}'''
# Un contrôle posé dans sa forme : ses quatre coins dans l'ellipse (ou le rectangle), en unités du gabarit.
JS_DANS_FORME = '''(id)=>{const bac=document.getElementById(id), svg=bac.querySelector('.bac-svg').getBoundingClientRect(), k=svg.width/960;
  const F={hg:['e',350,284.5,134,59.5],hd:['e',825.5,284.5,133.5,59.5],objet:['e',583,476,122,73],bas:['r',250,573,732,132]};
  return [...bac.querySelectorAll('.bac-ctrl')].map(c=>{const r=c.querySelector('.menu-case,input,textarea').getBoundingClientRect();
    const f=F[['hg','hd','objet','bas'].find(x=>c.classList.contains(x))];
    const P=[[r.left,r.top],[r.right,r.top],[r.left,r.bottom],[r.right,r.bottom]].map(([x,y])=>[50+(x-svg.left)/k,150+(y-svg.top)/k]);
    return f[0]==='e' ? P.every(([x,y])=>((x-f[1])/f[3])**2+((y-f[2])/f[4])**2<=1) : P.every(([x,y])=>x>f[1]&&x<f[1]+f[3]&&y>f[2]&&y<f[2]+f[4]);});}'''
JS_MIROIR = "(p)=>{const e=document.querySelector('.bac-miroir[data-pour=\"'+p+'\"]'); return e ? [...e.querySelectorAll('tspan')].map(t=>t.textContent).join(' ') : null;}"


def t(n, ok, d=""):
    res.append((n, bool(ok)))
    print(("✔" if ok else "✘"), n, d)


# Huit entrées, deux par famille — les quatre familles du programme :
# usagers, données, autres objets, éléments de l'environnement.
LISTE_OK = ("l'usager abonné : il prend et rend un vélo\n"
            "l'agent de maintenance : il répare et débloque\n"
            "l'identifiant de l'abonné (donnée) : sans lui, rien ne se déverrouille\n"
            "l'état « disponible » du vélo (donnée) : il vient du serveur\n"
            "le vélo (autre objet) : il est ancré à la borne\n"
            "le smartphone (autre objet) : il transmet l'identifiant\n"
            "la pluie (environnement) : elle mouille les bornes\n"
            "le trottoir (environnement) : la station y est fixée")

# c) Le vélo-cargo : cinq interacteurs extérieurs (exercice 1 de l'atelier, incrusté).
LISTE_VELO_OK = "Léa\nles enfants\nles courses\nla pluie\nle téléphone"
LISTE_VELO_FAUSSE = "Léa\nla pédale\naller au marché\nla pluie"

# Huit entrées, mais aucune donnée : la famille qu'on oublie toujours.
LISTE_SANS_DONNEE = ("l'usager abonné\nl'agent de maintenance\nle riverain\nle maire\n"
                     "le vélo\nle smartphone\nla pluie\nle trottoir")

CHOIX_SANS_DD = ("La borne est inclinée : ce choix répond à la pluie, il relève de la sécurité.\n"
                 "L'ancrage est à 90 cm : ce choix répond à l'usager, il relève de l'ergonomie.\n"
                 "Les arêtes sont arrondies : ce choix répond à l'usager, sécurité.\n"
                 "Le boîtier a une vis unique : il répond à l'agent de maintenance, ergonomie.")

CHOIX_OK = ("La borne est inclinée : ce choix répond à la pluie, il relève de la sécurité.\n"
            "L'ancrage est à 90 cm : ce choix répond à l'usager, il relève de l'ergonomie.\n"
            "Les arêtes sont arrondies : ce choix répond à l'usager, il relève de la sécurité.\n"
            "Les pièces se remplacent une par une : cela répond au budget de la ville et à la "
            "matière à produire, cela relève du développement durable.")

TRANSF_OK = ("L'air salin change : il attaque les métaux, il faut revoir les matériaux.\n"
             "La pluie change : elle est bien plus intense, l'inclinaison ne suffit plus.\n"
             "Le cyclone apparaît : il faut pouvoir démonter ou arrimer la station.")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 900})
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))

    # ───────────────────────────── la séquence ─────────────────────────────
    pg.goto(SEQ)
    pg.wait_for_timeout(500)
    t("séquence : aucune erreur JS", not errs, str(errs))
    contenu = pg.content()
    # L'exemption avait été écrite pour « https:// » — et l'espace de noms SVG
    # s'écrit « http:// ». La clause suivante le rattrapait donc, et ce contrôle
    # était rouge dès qu'un schéma était dessiné dans la page. On regarde
    # maintenant ce que la page IRAIT CHERCHER : les attributs de chargement, sans
    # les hyperliens, qui eux ont le droit d'être distants (n°40, corrigé le
    # 31/08/2026).
    distantes = pg.eval_on_selector_all(
        "[src], link[href], object[data], iframe[src], use[href]",
        "l=>l.map(e=>e.getAttribute('src')||e.getAttribute('href')||e.getAttribute('data'))"
        ".filter(u=>u && /^(https?:)?\/\//i.test(u))")
    t("séquence : hors ligne, aucune ressource distante (n°40)",
      "fonts.googleapis" not in contenu and not distantes, str(distantes))
    t("séquence : lien d'accueil valide (n°11)",
      pathlib.Path("../../../../index.html").exists())
    t("bandeau de tâches affiché (n°30)",
      "Séance 1" in pg.inner_text("#tachesBandeau"))

    n_ta = pg.eval_on_selector_all("textarea", "a=>a.length")
    n_et = pg.eval_on_selector_all("details.etayage", "a=>a.length")
    t("chaque zone de rédaction a sa version étayée (n°31)",
      # Le nombre de zones a changé avec les exercices incrustés du vélo-cargo (24/10/2026) :
      # on vérifie la règle (une version étayée par zone), plus un compte figé.
      n_ta >= 7 and n_et >= n_ta, f"{n_ta} zones / {n_et} étayages")

    t("chaque champ porte une étiquette (n°34)",
      pg.evaluate("[...document.querySelectorAll('select,textarea')].every(e=>!e.id||"
                  "document.querySelector(`label[for=\"${e.id}\"]`)||e.getAttribute('aria-label'))"))
    t("chaque figure a une alternative longue (n°1)",
      pg.evaluate("[...document.querySelectorAll('.fig img')].every(i=>i.alt.length>120)"))
    # Six figures depuis la vague 1 bis (13/09/2026) : les deux documents à lire, plus quatre
    # schémas — la station et sa limite, les cinq détails, les deux stations, et Shenzhen /
    # Sainte-Luce, rangé dans la correction de l'activité 3.
    t("les six figures sont présentes",
      pg.evaluate("[...document.querySelectorAll('.fig img')].length===6"))

    t("le compteur annonce 4 activités (n°39)", "/ 4 activités" in pg.inner_text("#progTxt")
      and pg.get_attribute("#progBar", "aria-valuemax") == "4")

    # le billet d'entrée oriente, il ne sanctionne pas
    pg.click('[data-check="0"]')
    pg.wait_for_timeout(120)
    t("billet d'entrée : oriente sans note (n°26)",
      "aucune note" in pg.inner_text("#fb0"), pg.inner_text("#fb0")[:55])
    t("billet d'entrée : ne compte pas dans la progression",
      "0 / 4" in pg.inner_text("#progTxt"))

    # activité 2 (l'ancienne activité 1, en séance 2 depuis le 04/11/2026) : le verrou de production
    pg.click("#tab-s2")
    pg.wait_for_timeout(120)
    pg.evaluate("['a1_1','a1_2','a1_3','a1_4','a1_5','a1_6','a1_7']"
                ".forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : les exercices du vélo-cargo (c) sont exigés",
      "vélo-cargo" in pg.inner_text("#fb2"), pg.inner_text("#fb2")[-60:])
    # c) exercice 1 — une liste avec une pièce et une action : refusée, et l'élève sait pourquoi
    pg.fill("#pv_5e_e1__liste", LISTE_VELO_FAUSSE)
    pg.click("#pv_5e_e1 button.verifier")
    pg.wait_for_timeout(120)
    retour = pg.inner_text("#pv_5e_e1 .retour")
    t("c) exercice 1 : une pièce et un usage sont refusés, avec leur raison",
      "pièce du vélo-cargo" in retour and "usage" in retour, retour[-80:])
    pg.fill("#pv_5e_e1__liste", LISTE_VELO_OK)
    pg.click("#pv_5e_e1 button.verifier")
    pg.wait_for_timeout(120)
    t("c) exercice 1 : cinq interacteurs extérieurs acceptés",
      "Tout est juste" in pg.inner_text("#pv_5e_e1 .retour"))
    # c) exercice 3 — compléter le diagramme pieuvre ; le choix s'écrit dans le schéma
    pg.check('#pv_5e_e3 input[name="pv_5e_e3__b1"][value="les enfants"]')
    t("c) exercice 3 : le mot choisi s'écrit dans la bulle du schéma",
      "les enfants" in pg.text_content("#pv-b1"))
    pg.check('#pv_5e_e3 input[name="pv_5e_e3__b2"][value="les courses"]')
    pg.check('#pv_5e_e3 input[name="pv_5e_e3__b3"][value="la route en pente"]')
    pg.check('#pv_5e_e3 input[name="pv_5e_e3__intrus"][value="pieces"]')
    pg.check('#pv_5e_e3 input[name="pv_5e_e3__fp"][value="service"]')
    pg.check('#pv_5e_e3 input[name="pv_5e_e3__fc_0"][value="pente"]')
    pg.check('#pv_5e_e3 input[name="pv_5e_e3__fc_1"][value="lire"]')
    for k, v in enumerate(["depart", "arrivee", "phrase", "centre"]):
        pg.check('#pv_5e_e3 input[name="pv_5e_e3__bete_%d"][value="%s"]' % (k, v))
    pg.click("#pv_5e_e3 button.verifier")
    pg.wait_for_timeout(120)
    t("c) exercice 3 : le diagramme complété est reconnu", "Tout est juste" in pg.inner_text("#pv_5e_e3 .retour"))
    pg.click('[data-check="2"]')
    pg.wait_for_timeout(120)
    t("activité 2 : validée quand les deux exercices du vélo-cargo sont réussis",
      "7 / 7" in pg.inner_text("#fb2"), pg.inner_text("#fb2")[:30])
    t("progression mise à jour", "1 / 4" in pg.inner_text("#progTxt"))

    # activité 3
    pg.click("#tab-s3")
    pg.wait_for_timeout(120)
    pg.evaluate("['a2_1','a2_2','a2_3','a2_4','a2_5','a2_6','a2_7','a2_8']"
                ".forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : le relevé écrit est exigé",
      "QUATRE choix" in pg.inner_text("#fb3"), pg.inner_text("#fb3")[-50:])
    pg.fill("#a2_choix", CHOIX_SANS_DD)
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : un relevé sans développement durable est refusé",
      "développement durable" in pg.inner_text("#fb3"))
    pg.fill("#a2_choix", CHOIX_OK)
    pg.click('[data-check="3"]')
    pg.wait_for_timeout(120)
    t("activité 3 : validée une fois le développement durable présent",
      "8 / 8" in pg.inner_text("#fb3"))

    # activité 4 + transfert
    pg.click("#tab-s4")
    pg.wait_for_timeout(120)
    pg.evaluate("['a3_1','a3_2','a3_3','a3_4']"
                ".forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : le transfert martiniquais est exigé",
      "TROIS interacteurs" in pg.inner_text("#fb4"), pg.inner_text("#fb4")[-50:])
    pg.fill("#a3_transf", TRANSF_OK)
    pg.click('[data-check="4"]')
    pg.wait_for_timeout(120)
    t("activité 4 : validée une fois le transfert rédigé", "4 / 4" in pg.inner_text("#fb4"))
    t("trois activités sur quatre (la bête à cornes reste à faire)", "3 / 4" in pg.inner_text("#progTxt"))

    # mode essentiel (n°29)
    pg.click("#btnEssentiel")
    pg.wait_for_timeout(120)
    t("mode essentiel : actif et annoncé",
      pg.get_attribute("#btnEssentiel", "aria-pressed") == "true")
    pg.click("#btnEssentiel")
    pg.wait_for_timeout(100)

    # rappel de l'hypothèse au bilan
    pg.click("#tab-s1")
    pg.fill("#hyp1", "l'usager, le vélo et la pluie")
    pg.wait_for_timeout(150)
    pg.click("#tab-s4")
    pg.wait_for_timeout(120)
    t("l'hypothèse de départ est rappelée au bilan",
      "l'usager, le vélo et la pluie" in pg.inner_text("#rappelHyp"))

    # sauvegarde / restauration
    pg.reload()
    pg.wait_for_timeout(400)
    t("sauvegarde locale restaurée après rechargement",
      pg.input_value("#pv_5e_e1__liste").startswith("Léa")
      and "3 / 4" in pg.inner_text("#progTxt"))

    # blocs de la règle n°4
    corps = pg.content()
    t("bloc « Prêt·e à t'entraîner » présent (n°4)", "Prêt·e à t'entraîner" in corps)
    t("bloc « Bonus » présent (n°4)", "Bonus (facultatif" in corps)
    t("un seul bouton QCM dans toute la séquence (n°4)",
      corps.count('href="qcm_5e_C2_shenzhen_station_velos.html"') == 1)


    # ═══════════ 04/11/2026 — la séance 1 « Le besoin : la bête à cornes », « Entoure » à l'écran ═══════════
    errs.clear()
    pg.goto(SEQ)
    pg.evaluate("localStorage.clear()")
    pg.reload()
    pg.wait_for_timeout(400)

    # — les quatre séances —
    onglets = pg.eval_on_selector_all(".seance-tab", "l=>l.map(e=>e.dataset.panel+'|'+e.textContent)")
    t("quatre séances : quatre onglets, la séance 1 est « Le besoin : la bête à cornes »",
      [o.split("|")[0] for o in onglets] == ["s1", "s2", "s3", "s4"] and "bête à cornes" in onglets[0], str(onglets))
    t("quatre séances : chaque panneau a sa question de la séance et son lien vers les mots de la séance",
      pg.evaluate("['s1','s2','s3','s4'].every(s=>{const p=document.getElementById(s);"
                  "return p.querySelector('.question-seance') && p.querySelector('.mots-seance a[href=\"lexique_5e_C2.1.html#seance-'+s+'\"]');})"))
    t("quatre séances : chaque séance mène à la suivante, la dernière porte la clôture",
      pg.evaluate("['s1','s2','s3'].every((s,i)=>document.querySelector('#'+s+' .vers-seance[data-vers=\"s'+(i+2)+'\"]'))"
                  "&& !document.querySelector('#s4 .vers-seance') && !!document.querySelector('#s4 #pos1')"))
    t("quatre séances : les titres des activités sont numérotés de 1 à 4, dans l'ordre des séances",
      pg.evaluate("['s1','s2','s3','s4'].every((s,i)=>[...document.querySelectorAll('#'+s+' h2')].some(h=>h.textContent.includes('Activité '+(i+1)+' —')))"))
    t("aucun identifiant de champ ancien n'a changé (a1_*, a2_*, a3_*, be_*, hyp1, bilan, positionnement)",
      pg.evaluate("['be_1','be_2','be_3','hyp1','a1_1','a1_7','a2_1','a2_8','a2_choix','a3_1','a3_4','a3_transf','hyp_retour','bilan1','bilan2','pos1','pos2','bonusRep']"
                  ".every(i=>document.getElementById(i))"))
    t("séance 1 : le billet d'entrée reste en tête, avant l'activité 1",
      pg.evaluate("(()=>{const s=document.getElementById('s1'), b=s.querySelector('#be_1'), a=s.querySelector('#activite-bac');"
                  "return b && a && (b.compareDocumentPosition(a) & Node.DOCUMENT_POSITION_FOLLOWING);})()"))
    t("le bandeau des tâches de la séance 1 annonce la bête à cornes",
      "bête à cornes" in pg.inner_text("#tachesBandeau").lower())

    # — point 1 : la fonction d'usage est nommée —
    note = pg.evaluate("[...document.querySelectorAll('#s1 p.meta')].map(p=>p.textContent).join(' ')")
    t("billet : la note nomme la fonction d'usage (EN : use function)",
      "c'est la fonction d'usage" in note and "use function" in note and "principe" in note, note[:120])
    caps = " ".join(pg.text_content("#capsule").split())
    t("capsule : la définition des ateliers, mot pour mot",
      "ce à quoi sert l'objet, pour la personne qui l'utilise. Elle s'écrit avec un verbe à l'infinitif" in caps
      and "use function" in caps)
    pg.check("#be_1__1"); pg.check("#be_2__2"); pg.check("#be_3__1")
    pg.click('[data-check="0"]')
    pg.wait_for_timeout(100)
    t("billet : choisir « à quoi l'objet SERT » pour la fonction technique fait nommer la fonction d'usage",
      "c'est la fonction d'usage, pas la fonction technique" in pg.inner_text("#fb0"), pg.inner_text("#fb0")[-90:])

    # — a) les trois questions, un menu dans chaque case du schéma —
    menus_a = pg.eval_on_selector_all("#bac_a .bac-ctrl select", "l=>l.map(s=>[s.id,s.options.length,s.getAttribute('aria-label')])")
    t("a) un menu à la place de chaque question du schéma (trois places, sept questions et « choisir »), chacun nommé",
      len(menus_a) == 3 and all(n == 8 and lab for _, n, lab in menus_a), str(menus_a))
    t("a) la question de droite a la formulation du modèle : « Sur quoi agit-il ? »",
      pg.evaluate("[...document.querySelectorAll('#bac_a_hd option')].some(o=>o.value==='sur_quoi'&&o.text==='Sur quoi agit-il ?')"))
    for ident in ("bac_a", "bac_c", "bac_d", "bac_p"):
        g = pg.evaluate(JS_GABARIT, ident) if ident != "bac_p" else pg.evaluate(JS_GABARIT.replace("'#'+id+' .bac-svg'", "'.bac-papier .bac-svg'"), ident)
        t("gabarit %s : le cadre 50 150 960 570, les trois ellipses et le rectangle du modèle, fonds blancs, contours #1f3864" % ident,
          g and g["vb"] == "50 150 960 570" and [tuple(x) for x in g["e"]] == GABARIT["ellipse"]
          and [tuple(x) for x in g["r"]] == GABARIT["rect"] and g["contour"], str(g)[:160])
        t("gabarit %s : la corne et la flèche en #2e75b6, la corne tracée après le produit (elle passe sur son haut)" % ident,
          g and g["bleu"] == ["#2e75b6", "#2e75b6"] and g["corneApresProduit"])
    t("1280 px, a) : chaque menu est posé à la place de sa question, au-dessus de sa case",
      pg.evaluate('''(()=>{const svg=document.querySelector('#bac_a .bac-svg').getBoundingClientRect(), k=svg.width/960;
        const B={hg:[60,150,560,225],hd:[640,150,1010,225],bas:[60,345,470,572]};
        return [...document.querySelectorAll('#bac_a .bac-ctrl')].every(c=>{const r=c.querySelector('.menu-case').getBoundingClientRect(), b=B[['hg','hd','bas'].find(x=>c.classList.contains(x))];
          return getComputedStyle(c).position==='absolute' && r.height>=44 && 50+(r.left-svg.left)/k>=b[0] && 50+(r.right-svg.left)/k<=b[2] && 150+(r.top-svg.top)/k>=b[1] && 150+(r.bottom-svg.top)/k<=b[3];});})()'''))
    BAC = pg.evaluate("BAC")
    LEURRES = pg.evaluate("BAC_LEURRES")
    ok_retours = True
    for cid, c in BAC["a"].items():
        for v in pg.eval_on_selector_all("#%s option" % cid, "l=>l.map(o=>o.value).filter(Boolean)"):
            pg.select_option("#" + cid, v)
            pg.click('[data-bac="a"]')
            vd = pg.inner_text("#%s_verdict" % cid)
            attendu = c["ok"] if v == c["bonne"] else (c["retours"].get(v) or LEURRES[v])
            if attendu[:40] not in vd or (("✔" in vd) != (v == c["bonne"])):
                ok_retours = False
                print("   a)", cid, v, "→", vd[:80])
    t("a) chaque question fausse a son propre retour, écrit sous le dessin avec son repère ; la bonne est marquée ✔ juste", ok_retours)
    pg.select_option("#bac_a_hg", "a_qui"); pg.select_option("#bac_a_hd", "prix"); pg.select_option("#bac_a_bas", "but")
    t("a) le choix s'écrit en entier dans le menu, et, en miroir, à la place de la question dans le dessin",
      pg.inner_text("#bac_a .hg .menu-vu") == "À qui le produit rend-il service ?"
      and pg.evaluate(JS_MIROIR, "bac_a_hg") == "À qui le produit rend-il service ?")
    pg.click('[data-bac="a"]')
    t("a) le bilan compte les cases : 2 / 3, la case fausse marquée ✘ avec le mot « à revoir »",
      pg.inner_text("#bac_a_retour").startswith("2 / 3") and "✘ à revoir" in pg.inner_text("#bac_a_hd_verdict"))
    t("a) le retour s'écrit sous le dessin, avec son repère : « ② En haut à droite — ✘ à revoir… »",
      pg.inner_text("#bac_a_hd_verdict").startswith("② En haut à droite — ✘ à revoir")
      and pg.evaluate("document.getElementById('bac_a_hd_verdict').getBoundingClientRect().top >= document.querySelector('#bac_a .bac-svg').getBoundingClientRect().bottom"))
    t("a) la case fausse : contour rouge et marque ✘ écrite, sur le menu ; la juste : contour vert et ✔",
      pg.evaluate("getComputedStyle(document.querySelector('#bac_a .hd .menu-case')).borderTopColor") == "rgb(185, 28, 28)"
      and pg.inner_text("#bac_a .hd .bac-marque-case") == "✘"
      and pg.evaluate("getComputedStyle(document.querySelector('#bac_a .hg .menu-case')).borderTopColor") == "rgb(22, 101, 52)"
      and pg.inner_text("#bac_a .hg .bac-marque-case") == "✔")
    pg.select_option("#bac_a_hd", "sur_quoi")
    t("a) changer de réponse efface le retour périmé de la case",
      pg.inner_text("#bac_a_hd_verdict") == "")
    pg.click('[data-bac="a"]')
    t("a) les trois questions à leur place : 3 / 3", pg.inner_text("#bac_a_retour").startswith("✔ 3 / 3"))

    # — b) l'exercice du vélo-cargo, incrusté depuis l'atelier « Le besoin » —
    t("b) l'exercice « Lire la bête à cornes du vélo-cargo » est incrusté entre a) et c)",
      pg.evaluate("(()=>{const e=document.getElementById('bc_5e_e1'), a=document.getElementById('bac_a'), c=document.getElementById('bac_c');"
                  "return !!e && e.closest('#s1') && (a.compareDocumentPosition(e) & 4) && (e.compareDocumentPosition(c) & 4);})()"))
    t("b) l'introduction dit la continuité : le même vélo-cargo, son diagramme pieuvre en séance 2",
      "séance 2" in pg.inner_text("#incruste-bc-5e-shenzhen-c2") and "diagramme pieuvre" in pg.inner_text("#incruste-bc-5e-shenzhen-c2"))

    # — c) la bête à cornes de la station —
    ok_retours = True
    for cid, c in BAC["c"].items():
        for v in pg.eval_on_selector_all("#%s option" % cid, "l=>l.map(o=>o.value).filter(Boolean)"):
            pg.select_option("#" + cid, v)
            pg.click('[data-bac="c"]')
            vd = pg.inner_text("#%s_verdict" % cid)
            attendu = c["ok"] if v == c["bonne"] else c["retours"][v]
            if attendu[:40] not in vd or (("✔" in vd) != (v == c["bonne"])):
                ok_retours = False
                print("   c)", cid, v, "→", vd[:80])
    t("c) chaque leurre a son retour (la ville qui paie, le fabricant, le vélo ; l'usager, le trottoir, la pluie ; "
      "fonction technique, solution, sujet, contrainte)", ok_retours)
    t("1280 px, c) : les trois menus sont posés dans leurs formes (les coins dans l'ellipse, dans le rectangle), 44 px au moins",
      all(pg.evaluate(JS_DANS_FORME, "bac_c")) and pg.evaluate("[...document.querySelectorAll('#bac_c .menu-case')].every(m=>m.getBoundingClientRect().height>=44)"))
    t("c) les retours sont sous le dessin, chacun avec son repère, et le dessin reste le gabarit",
      pg.inner_text("#bac_c_qui_verdict").startswith("① À qui le produit rend-il service ?")
      and pg.inner_text("#bac_c_quoi_verdict").startswith("② Sur quoi agit-il ?")
      and pg.inner_text("#bac_c_but_verdict").startswith("③ Dans quel but ?")
      and [tuple(x) for x in pg.evaluate(JS_GABARIT, "bac_c")["e"]] == GABARIT["ellipse"])
    pg.select_option("#bac_c_but", "verrouiller")
    pg.click('[data-bac="c"]')
    t("c) le piège central : « verrouiller le vélo » est refusé comme fonction technique, renvoyé à la fonction d'usage",
      "fonction technique" in pg.inner_text("#bac_c_but_verdict") and "fonction d'usage" in pg.inner_text("#bac_c_but_verdict"))
    t("c) l'encadré À retenir dit la fonction d'usage, mot pour mot",
      "écrite avec un verbe à l'infinitif et sans solution, est la fonction d'usage de l'objet : le service qu'il rend à l'usager"
      in pg.inner_text("#activite-bac").replace(" ", " "))
    pg.select_option("#bac_c_qui", "usager"); pg.select_option("#bac_c_quoi", "velo"); pg.select_option("#bac_c_but", "service")
    pg.click('[data-bac="c"]')
    t("c) la bête à cornes de la station juste : 3 / 3", pg.inner_text("#bac_c_retour").startswith("✔ 3 / 3"))

    # — d) ta bête à cornes : le miroir, les critères, le cahier —
    pg.fill("#bac_d_objet", "le cartable")
    pg.fill("#bac_d_qui", "l'élève qui le porte")
    t("d) ce que l'élève tape s'écrit dans le schéma (le produit, en italique, à la place de « Nom du produit » ; la case « à qui ? »)",
      pg.evaluate(JS_MIROIR, "bac_d_objet") == "le cartable" and pg.evaluate(JS_MIROIR, "bac_d_qui") == "l'élève qui le porte"
      and pg.get_attribute('#bac_d .bac-miroir[data-pour="bac_d_objet"]', "font-style") == "italic")
    t("1280 px, d) : les quatre champs sont posés dans leurs formes (les coins dedans), 44 px au moins",
      all(pg.evaluate(JS_DANS_FORME, "bac_d")) and pg.evaluate("[...document.querySelectorAll('#bac_d .bac-ctrl input,#bac_d .bac-ctrl textarea')].every(m=>m.getBoundingClientRect().height>=44)"))
    def criteres(but):
        pg.fill("#bac_d_but", but)
        pg.click('[data-bac="d"]')
        return pg.eval_on_selector_all(".bac-criteres .bac-marque", "l=>l.map(m=>m.classList.contains('juste'))")
    t("d) une case du haut vide : le premier critère n'est pas rempli",
      criteres("Transporter ses affaires de classe")[0] is False)
    pg.fill("#bac_d_quoi", "ses livres et ses cahiers")
    t("d) « Un cartable avec deux bretelles » : ni verbe, et une solution", criteres("Un cartable avec deux bretelles") == [True, False, False])
    t("d) « Le cartable porte les livres » : une phrase avec un sujet, pas un verbe à l'infinitif",
      criteres("Le cartable porte les livres")[1] is False)
    t("d) « Fermer avec une fermeture éclair » : un verbe, mais une solution", criteres("Fermer avec une fermeture éclair") == [True, True, False])
    t("d) le but ne nomme pas l'objet lui-même", criteres("Ranger le cartable de l'élève")[2] is False)
    t("d) « Transporter ses affaires de classe entre la maison et le collège » : les trois critères",
      criteres("Transporter ses affaires de classe entre la maison et le collège") == [True, True, True]
      and pg.inner_text("#bac_d_retour").startswith("✔ 3 critères"))
    t("d) le but tapé s'écrit dans la case du bas du schéma",
      "Transporter ses affaires" in (pg.evaluate(JS_MIROIR, "bac_d_but") or ""))
    pg.fill("#bac_d_quoi", "ses livres, ses cahiers, sa trousse, son agenda et sa gourde de la journée")
    t("d) un texte long : c'est la taille du texte qui baisse (deux lignes au plus), jamais la forme",
      pg.evaluate("document.querySelectorAll('#bac_d .bac-miroir[data-pour=\"bac_d_quoi\"] tspan').length") <= 2
      and float(pg.get_attribute('#bac_d .bac-miroir[data-pour="bac_d_quoi"]', "font-size")) < 30
      and [tuple(x) for x in pg.evaluate(JS_GABARIT, "bac_d")["e"]] == GABARIT["ellipse"])
    pg.fill("#bac_d_quoi", "ses livres et ses cahiers")
    t("d) la consigne dit où dessiner : « Dessine-la à main levée sur ton cahier »",
      "Dessine-la à main levée sur ton cahier" in pg.inner_text("#activite-bac"))
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(100)
    t("activité 1 : non validée tant que le vélo-cargo (b) n'est pas réussi et le dessin pas déclaré",
      "vélo-cargo" in pg.inner_text("#fb1") and "cahier" in pg.inner_text("#fb1") and not pg.evaluate("!!window.__valid[1]"))
    for nom, v in (("qui", "sert"), ("quoi", "deplace"), ("but", "but")):
        pg.check('#bc_5e_e1 input[name="bc_5e_e1__%s"][value="%s"]' % (nom, v))
    pg.click("#bc_5e_e1 button.verifier")
    pg.wait_for_timeout(100)
    t("b) l'exercice du vélo-cargo se vérifie seul dans la séquence", "Tout est juste" in pg.inner_text("#bc_5e_e1 .retour"))
    pg.check("#bac_d_cahier")
    pg.click('[data-check="1"]')
    pg.wait_for_timeout(100)
    t("activité 1 : validée (11 / 11) quand a), b), c), d) sont justes et le dessin déclaré",
      pg.inner_text("#fb1").startswith("11 / 11") and pg.evaluate("!!window.__valid[1]"), pg.inner_text("#fb1")[:40])
    t("progression : 1 / 4, et la coche de la séance 1", "1 / 4" in pg.inner_text("#progTxt") and "✔" in pg.inner_text("#done-s1"))

    # — « Entoure » à l'écran —
    pg.click("#tab-s2")
    pg.wait_for_timeout(150)
    btns = pg.eval_on_selector_all(".ent-btn", "l=>l.map(b=>[b.dataset.el,b.getAttribute('aria-pressed'),b.getBoundingClientRect().height,b.getBoundingClientRect().width])")
    t("entourer : huit boutons, un par nom de la figure, tous « non entourés » au départ",
      len(btns) == 8 and all(a == "false" for _, a, _, _ in btns), str(btns))
    t("entourer : des cibles d'au moins 44 px", all(h >= 44 and w >= 44 for _, _, h, w in btns))
    dedans = pg.evaluate("(()=>{const r=document.querySelector('#entourer img').getBoundingClientRect();"
                         "return [...document.querySelectorAll('.ent-btn')].every(b=>{const q=b.getBoundingClientRect();"
                         "return q.left>=r.left-1&&q.right<=r.right+1&&q.top>=r.top-1&&q.bottom<=r.bottom+1;});})()")
    t("entourer, 1280 px : chaque bouton est posé sur le dessin, à la place de son nom", dedans)
    chev = pg.evaluate("(()=>{const q=[...document.querySelectorAll('.ent-btn')].map(b=>b.getBoundingClientRect());"
                       "for(let i=0;i<q.length;i++)for(let j=i+1;j<q.length;j++){const a=q[i],b=q[j];"
                       "if(a.left<b.right&&b.left<a.right&&a.top<b.bottom&&b.top<a.bottom) return true;} return false;})()")
    t("entourer, 1280 px : aucun bouton n'en recouvre un autre", not chev)
    pg.click('.ent-btn[data-el="borne"]')
    t("entourer : un clic entoure — aria-pressed, le mot « entourée » écrit, l'ellipse dessinée",
      pg.get_attribute('.ent-btn[data-el="borne"]', "aria-pressed") == "true"
      and pg.is_visible('.ent-btn[data-el="borne"] .ent-etat') and pg.inner_text('.ent-btn[data-el="borne"] .ent-etat') == "entourée"
      and pg.evaluate("getComputedStyle(document.querySelector('.ent-btn[data-el=\"borne\"]')).borderTopStyle") == "solid")
    pg.click('.ent-btn[data-el="borne"]')
    t("entourer : un second clic retire le trait", pg.get_attribute('.ent-btn[data-el="borne"]', "aria-pressed") == "false"
      and not pg.is_visible('.ent-btn[data-el="borne"] .ent-etat'))
    pg.focus('.ent-btn[data-el="ecran"]'); pg.keyboard.press("Space")
    pg.focus('.ent-btn[data-el="ancrage"]'); pg.keyboard.press("Enter")
    t("entourer : au clavier, Espace et Entrée entourent", pg.get_attribute('.ent-btn[data-el="ecran"]', "aria-pressed") == "true"
      and pg.get_attribute('.ent-btn[data-el="ancrage"]', "aria-pressed") == "true")
    pg.click('.ent-btn[data-el="velo"]')
    pg.click("#ent_verifier")
    retour = pg.inner_text("#ent_retour")
    t("entourer : « Vérifier » donne un retour pour chacun des huit éléments",
      pg.eval_on_selector_all("#ent_retour li", "l=>l.length") == 8 and retour.startswith("4 / 8"), retour[:60])
    t("entourer : le vélo entouré à tort est refusé — un autre objet, un interacteur, pas une pièce",
      "le vélo — entouré : à retirer" in retour and "un interacteur, pas une de ses pièces" in retour)
    t("entourer : le câble oublié est demandé — il apporte l'énergie, le réseau de la ville est un interacteur",
      "le câble d'alimentation — pas entouré : à entourer" in retour and "le réseau électrique de la ville, est un autre objet, un interacteur" in retour)
    t("entourer : le trottoir et le sol laissés de côté sont justes — des éléments de l'environnement",
      "le trottoir — pas entouré : juste" in retour and "le sol — pas entouré : juste" in retour)
    t("entourer : chaque bouton porte sa marque ✔ ou ✘ après « Vérifier »",
      pg.eval_on_selector_all(".ent-btn .ent-marque", "l=>l.length") == 8)
    pg.reload()
    pg.wait_for_timeout(400)
    pg.click("#tab-s2")
    t("entourer : ce qui est entouré et le retour reviennent après un rechargement",
      pg.get_attribute('.ent-btn[data-el="velo"]', "aria-pressed") == "true" and pg.inner_text("#ent_retour").startswith("4 / 8"))
    t("après rechargement : les menus, le miroir et la case du cahier de la séance 1 sont restaurés",
      pg.input_value("#bac_c_but") == "service" and pg.is_checked("#bac_d_cahier")
      and pg.evaluate(JS_MIROIR, "bac_d_objet") == "le cartable")
    for k in ("velo",):
        pg.click('.ent-btn[data-el="%s"]' % k)
    for k in ("borne", "boitier", "cable"):
        pg.click('.ent-btn[data-el="%s"]' % k)
    pg.click("#ent_verifier")
    retour = pg.inner_text("#ent_retour")
    t("entourer : tout juste — 8 / 8, et la phrase qui relie à la suite (« tu viens de tracer sa limite »)",
      retour.startswith("8 / 8") and "tu viens de tracer sa limite" in retour and "est un interacteur" in retour)
    t("entourer : une correction complète, repliée", pg.evaluate("!document.getElementById('ent_correction').open")
      and "réseau électrique de la ville" in pg.text_content("#ent_correction"))
    t("séance 1 : aucune erreur JS pendant tout le parcours", not errs, str(errs))

    # — l'ancienne sauvegarde (trois activités, sans version) passe aux activités 2 à 4 —
    pg.evaluate("localStorage.setItem('seq_5e_C2_shenzhen', JSON.stringify({inputs:{hyp1:'ancienne'}, valid:{0:true,1:true,2:true,3:true}, exp:{}}))")
    pg.reload()
    pg.wait_for_timeout(300)
    t("sauvegarde d'avant le 04/11/2026 : ses trois validations passent aux activités 2, 3 et 4 (3 / 4)",
      "3 / 4" in pg.inner_text("#progTxt") and pg.evaluate("!window.__valid[1] && window.__valid[2] && window.__valid[4]")
      and pg.inner_text("#done-s1") == "" and "✔" in pg.inner_text("#done-s4"))

    # — 390 px : rien ne déborde, les noms restent atteignables —
    ptl = b.new_page(viewport={"width": 390, "height": 844})
    ptl.goto(SEQ); ptl.evaluate("localStorage.clear()"); ptl.reload(); ptl.wait_for_timeout(300)
    t("390 px, séance 1 : aucun défilement de côté", ptl.evaluate("document.documentElement.scrollWidth - innerWidth") <= 0)
    t("390 px : la bête à cornes reste le gabarit, entier, dans l'écran (a, c, d)",
      ptl.evaluate("['bac_a','bac_c','bac_d'].every(id=>{const r=document.querySelector('#'+id+' .bac-svg').getBoundingClientRect();"
                   "return r.left>=0 && r.right<=innerWidth && Math.abs(r.width/r.height-960/570)<0.02;})"))
    t("390 px : les menus et les champs passent sous le dessin, chacun avec sa question visible, en cibles de 44 px",
      ptl.evaluate("['bac_a','bac_c','bac_d'].every(id=>{const s=document.querySelector('#'+id+' .bac-svg').getBoundingClientRect();"
                   "return [...document.querySelectorAll('#'+id+' .bac-ctrl')].every(c=>{const r=c.getBoundingClientRect(), e=c.querySelector('.bac-etiquette'),"
                   "m=c.querySelector('.menu-case,input,textarea').getBoundingClientRect();"
                   "return r.top>=s.bottom-1 && e.getBoundingClientRect().width>40 && m.height>=44 && m.right<=innerWidth;});})"))
    ptl.select_option("#bac_c_qui", "usager")
    t("390 px : le choix s'écrit dans sa forme, en miroir",
      ptl.evaluate(JS_MIROIR, "bac_c_qui") == "l'usager, cycliste abonné ou touriste"
      and ptl.evaluate("getComputedStyle(document.querySelector('.bac-miroir[data-pour=\"bac_c_qui\"]')).display") != "none")
    ptl.select_option("#bac_c_qui", "")
    ptl.click("#tab-s2"); ptl.wait_for_timeout(150)
    t("390 px, séance 2 : aucun défilement de côté", ptl.evaluate("document.documentElement.scrollWidth - innerWidth") <= 0)
    rang = ptl.evaluate("(()=>{const r=document.querySelector('#entourer img').getBoundingClientRect();"
                        "return [...document.querySelectorAll('.ent-btn')].every(b=>{const q=b.getBoundingClientRect();"
                        "return q.top>=r.bottom-1 && q.left>=0 && q.right<=innerWidth && q.height>=44;});})()")
    t("390 px : les noms deviennent une rangée de puces sous la figure, toutes à l'écran, de 44 px", rang)
    ptl.click('.ent-btn[data-el="cable"]')
    t("390 px : entourer une puce dessine l'ellipse sur la figure, autour du nom",
      ptl.evaluate("getComputedStyle(document.querySelector('.ent-traits ellipse[data-pour=\"cable\"]')).display") != "none")
    # l'impression de la séance 2 : la consigne « Entoure », la figure sans marques
    ptl.evaluate("window.dispatchEvent(new Event('beforeprint'))")
    ptl.emulate_media(media="print")
    t("impression : « Entoure uniquement ce qui appartient à la station », la figure sans boutons ni traits",
      ptl.is_visible("#entourer figcaption .pp-papier") and not ptl.is_visible("#entourer figcaption .pp-ecran")
      and not ptl.is_visible(".ent-boutons") and not ptl.is_visible(".ent-traits") and ptl.is_visible("#entourer img"))
    ptl.emulate_media(media="screen")
    ptl.click("#tab-s1"); ptl.wait_for_timeout(100)
    ptl.evaluate("window.dispatchEvent(new Event('beforeprint'))")
    ptl.emulate_media(media="print")
    t("impression de la séance 1 : un cadre vide pour dessiner sa bête à cornes, sans les champs de l'écran",
      ptl.is_visible(".bac-cadre") and not ptl.is_visible("#bac_d_objet") and not ptl.is_visible("#bac_d"))
    t("impression de la séance 1 : a) donne la liste des sept questions, et une ligne pointillée à la place de chaque question",
      ptl.is_visible(".bac-liste") and not ptl.is_visible("#bac_a .bac-ctrl")
      and ptl.evaluate("[...document.querySelectorAll('#bac_a .bac-pointilles')].filter(l=>getComputedStyle(l).display!=='none').length") == 6)
    t("impression de la séance 1 : c) imprime ses propositions en cases à cocher, à côté du dessin, sous leur question",
      ptl.eval_on_selector_all("#bac_c .pp-choix .pp-case", "l=>l.filter(e=>e.offsetParent).length") == 13
      and ptl.evaluate("document.querySelector('#bac_c .bac-ctrl').getBoundingClientRect().left >= document.querySelector('#bac_c .bac-svg').getBoundingClientRect().right"))
    t("impression de la séance 1 : le gabarit en noir sur blanc (contours noirs, corne et flèche gris foncé), jamais coupé",
      ptl.evaluate("getComputedStyle(document.querySelector('#bac_c .bac-contour')).stroke") == "rgb(0, 0, 0)"
      and ptl.evaluate("getComputedStyle(document.querySelector('#bac_c .bac-trait')).stroke") == "rgb(64, 64, 64)"
      and ptl.evaluate("[...document.querySelectorAll('.bac')].every(b=>getComputedStyle(b).breakInside==='avoid')"))
    ptl.close()

    # — le lexique : une section par séance ; la bête à cornes, le besoin, la fonction d'usage en séance 1 —
    pg.goto(pathlib.Path("lexique_5e_C2.1.html").resolve().as_uri())
    s1 = pg.inner_text("#seance-s1")
    t("lexique : une section par séance, jusqu'à #seance-s4",
      all(pg.query_selector("#seance-s%d" % i) for i in (1, 2, 3, 4)))
    t("lexique, séance 1 : besoin, bête à cornes, fonction d'usage, en français et en anglais",
      all(m in s1 for m in ("besoin", "bête à cornes", "fonction d'usage", "need", "use function")))
    t("lexique, séance 1 : la fonction d'usage avec la définition des ateliers",
      "Ce à quoi sert l'objet, pour la personne qui l'utilise. Elle s'écrit avec un verbe à l'infinitif" in s1)

    # — le QCM : les trois questions de la bête à cornes —
    pg.goto(QCM)
    pg.evaluate("localStorage.clear()")
    pg.reload()
    pg.wait_for_timeout(300)
    nouv = pg.evaluate("QUESTIONS.slice(0,3).map(q=>[q.n,q.c,q.d.filter((x,j)=>j!==q.r&&x.length>20).length,q.o[q.r]])")
    t("QCM : en tête, les trois questions de la bête à cornes (les trois questions, « à qui » ou « sur quoi », "
      "fonction d'usage ou fonction technique), chacune avec trois réfutations",
      [x[0] for x in nouv] == ["Les trois questions de la bête à cornes", "À qui ou sur quoi", "Fonction d'usage ou fonction technique"]
      and all(x[1] == "C2.1" and x[2] == 3 for x in nouv), str(nouv))
    t("QCM : la bonne réponse de « Fonction d'usage ou fonction technique » est la fonction d'usage",
      nouv[2][3].startswith("sa fonction d'usage"))
    t("QCM : la dernière question reste la frontière avec la 4e", pg.evaluate("QUESTIONS[QUESTIONS.length-1].n") == "Ce qu'on fera l'an prochain")
    t("QCM : l'en-tête annonce 33 questions", "33 questions" in pg.inner_text(".badges") and "(33)" in pg.inner_text('[data-mode="complet"]'))
    t("QCM : nouvelle clé de sauvegarde (la banque a changé)", pg.evaluate("KEY") == "qcm_5e_C2_shenzhen_33q")
    # — la synthèse élève : la partie « Pour commencer », sans casser les ancres —
    pg.goto(SYE)
    t("synthèse élève : la partie sur la bête à cornes et la fonction d'usage (#partie-0), dans la carte de tête",
      pg.query_selector("#partie-0") is not None and pg.query_selector('.cartes a[href="#partie-0"]') is not None
      and "fonction d'usage" in pg.inner_text("#partie-0 >> xpath=..").lower())
    t("synthèse élève : les ancres #partie-1 à #partie-6 sont toujours là, sur les mêmes titres",
      [pg.inner_text("#partie-%d" % i)[:3] for i in range(1, 7)] == ["%d. " % i for i in range(1, 7)])

    # ─────────────────────────────── le QCM ───────────────────────────────
    errs.clear()
    pg.goto(QCM)
    pg.wait_for_timeout(400)
    t("QCM : aucune erreur JS", not errs, str(errs))
    info = pg.evaluate("""()=>({
        n: QUESTIONS.length,
        rep: [0,1,2,3].map(k=>QUESTIONS.filter(q=>q.r===k).length),
        dvide: QUESTIONS.every(q=>q.d[q.r]===""),
        courtes: QUESTIONS.flatMap(q=>q.d.filter((x,j)=>j!==q.r&&x.trim().length<=20)).length,
        imgs: QUESTIONS.filter(q=>q.img).length,
        c21: QUESTIONS.filter(q=>q.c==="C2.1").length,
        c22: QUESTIONS.filter(q=>q.c==="C2.2").length,
        complets: QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret&&q.o.length===4&&q.d.length===4)
    })""")
    t("QCM : 33 questions", info["n"] == 33, str(info["n"]))
    t("QCM : 18 pour 5e_C2.1 (dont 3 sur la bête à cornes), 15 pour 5e_C2.2", info["c21"] == 18 and info["c22"] == 15,
      f"{info['c21']} / {info['c22']}")
    t("QCM : bonnes réponses réparties sur A/B/C/D", max(info["rep"]) - min(info["rep"]) <= 1,
      str(info["rep"]))
    t("QCM : 5 questions illustrées", info["imgs"] == 5, str(info["imgs"]))
    t("QCM : les trois domaines du code sont ceux du programme",
      pg.evaluate("QUESTIONS.find(q=>q.n==='Trois domaines').o[QUESTIONS.find("
                  "q=>q.n==='Trois domaines').r]")
      == "l'ergonomie, la sécurité et le développement durable")
    t("QCM : chaque distracteur porte une réfutation qui explique",
      info["courtes"] == 0 and info["dvide"], f"{info['courtes']} réfutation(s) trop courte(s)")
    t("QCM : chaque question a explication, exemple, erreur classique et à-retenir",
      info["complets"])

    # parcours complet : toutes les bonnes réponses
    n = pg.evaluate("QUESTIONS.length")
    for i in range(n):
        r = pg.evaluate(f"QUESTIONS[{i}].r")
        pg.click(f".option >> nth={r}")
        pg.click("#btnValider")
        if i < n - 1:
            pg.click("#btnSuiv")
    pg.click("#btnTerminer")
    pg.wait_for_timeout(300)
    bilan = pg.inner_text("body")
    t("QCM : parcours complet, 33 bonnes réponses acceptées",
      pg.evaluate("etat.reponses.filter((x,i)=>x===QUESTIONS[i].r).length") == 33)
    # Règle n°42 : la formulation d'une compétence se recopie. « esthétique » était
    # une substitution de ma main, corrigée dans la séquence en juillet et restée
    # dans le QCM jusqu'au 8 août — le contrôle mécanisé ne regardait que la carte
    # de la séquence. On le vérifie désormais ici aussi.
    libelles = pg.evaluate("Object.values(COMP_LABELS).join(' | ')")
    t("QCM : aucune formulation de compétence ne dit « esthétique »",
      "esthétique" not in libelles, libelles[:80])
    t("QCM : la formulation de C2.2 est celle du référentiel",
      "développement durable" in libelles)
    t("QCM : bilan par compétence affiché",
      "5e_C2.1" in bilan and "5e_C2.2" in bilan)
    pg.reload()
    pg.wait_for_timeout(300)
    t("QCM : sauvegarde restaurée après rechargement",
      pg.evaluate("etat.validees.filter(Boolean).length") == 33)

    # une mauvaise réponse affiche bien la réfutation du distracteur choisi
    pg.evaluate("localStorage.clear()")
    pg.reload()
    pg.wait_for_timeout(300)
    r0 = pg.evaluate("QUESTIONS[0].r")
    faux = (r0 + 1) % 4
    pg.click(f".option >> nth={faux}")
    pg.click("#btnValider")
    pg.wait_for_timeout(200)
    attendu = pg.evaluate(f"QUESTIONS[0].d[{faux}]")
    t("QCM : la réfutation du distracteur choisi est affichée",
      attendu[:40] in pg.inner_text("body"))

    # ───────────────────────────── les synthèses ─────────────────────────────
    for nom, uri, figs in (("élève", SYE, 0), ("professeur", SYP, 0)):   # n°316 révisée (29/10/2026) : deux pages A4, les grands schémas <object> restent dans la séquence
        errs.clear()
        pg.goto(uri)
        pg.wait_for_timeout(300)
        t(f"synthèse {nom} : aucune erreur JS", not errs, str(errs))
        t(f"synthèse {nom} : {figs} figure(s) référencée(s)",
          pg.eval_on_selector_all("object", "a=>a.length") == figs)
        t(f"synthèse {nom} : liens de navigation valides",
          all(pathlib.Path("Synthèses").joinpath(h.split("#")[0]).exists()
              for h in pg.eval_on_selector_all("a", "a=>a.map(e=>e.getAttribute('href'))")
              if not h.startswith("#")))   # n°316 : la carte renvoie aux parties de la page (#partie-N)

    b.close()

ko = [n for n, ok in res if not ok]
print(f"\n{len(res) - len(ko)} / {len(res)} tests passés")
if ko:
    print("Échecs :")
    for n in ko:
        print("  -", n)
sys.exit(1 if ko else 0)
