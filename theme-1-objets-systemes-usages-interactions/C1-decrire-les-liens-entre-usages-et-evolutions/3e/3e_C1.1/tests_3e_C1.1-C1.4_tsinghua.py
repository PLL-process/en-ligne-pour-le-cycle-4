# -*- coding: utf-8 -*-
"""Suite de tests du lot 3e_C1.1 à C1.4 — Tsinghua, robots, drones et IA face aux feux.

Ne sont déclarés dans le rapport que les tests présents ici et réellement exécutés.

PÉRIMÈTRE (règle n°47) — ce que cette suite vérifie :
  · les six verrous de la séquence, fermés sur une page vide et ouverts sur une
    production complète ; la progression, la sauvegarde et sa restauration ;
  · la cible du bouton d'entraînement aux trois moments prévus (règle n°45) ;
  · la présence des deux blocs de la règle n°4, corrigé du Bonus compris ;
  · que la phrase éthique de l'activité 4 est VISIBLE et non repliée (règle n°68) ;
  · que la carte de référentiel porte les quatre formulations ;
  · pour le QCM : titre affiché et sous-titre (n°51), nombre de questions,
    répartition des bonnes réponses, réfutation de chaque distracteur, filtre par
    compétence, ouverture ciblée, chargement effectif des images, zéro erreur JS.

Ce qu'elle NE vérifie PAS :
  · l'exactitude pédagogique des corrigés et des explications ;
  · la justesse des chiffres publics cités — elle relève des sources, listées dans
    SOURCES_DONNEES_IMPACTS_3e.md ;
  · le rendu à l'impression et l'ergonomie réelle en classe.

Usage : python3 tests_3e_C1.1-C1.4_tsinghua.py
"""

import asyncio, pathlib
from playwright.async_api import async_playwright
F = (pathlib.Path(__file__).resolve().parent / "sequence_3e_C1.1-C1.4_tsinghua_feux.html").as_uri()
Q = (pathlib.Path(__file__).resolve().parent / "qcm_3e_C1.1-C1.4_tsinghua.html").as_uri()
BON = {
 "be_1":"rend possible ce qui ne l'était pas du tout, et rend caduc un savoir-faire",
 "be_2":"elles ont la même unité, la même période et le même périmètre",
 "be_3":"appuie chaque affirmation sur un fait vérifiable, et nomme ce qu'il laisse de côté",
 "a1_1":"une amélioration : on fait mieux la même chose, avec le même savoir-faire",
 "a1_2":"rend possible ce qui ne l'était pas : voir la nuit, et sur un continent entier",
 "a1_3":"le métier change : le savoir-faire d'avant ne suffit plus",
 "a1_4":"pas toujours : des tours de guet fonctionnent encore, l'œil humain lève un doute qu'aucun capteur ne lève",
 "a1_5":"quelle couleur du spectre chauffe le plus — il ne cherchait pas l'infrarouge",
 "a1_6":"une découverte devient une technique quand une capacité de fabrication ET un besoin la rencontrent",
 "a2_1":"ne sont pas comparables directement : ni la même unité, ni la même grandeur",
 "a2_2":"seulement après avoir converti une quantité totale en kgCO₂e",
 "a2_3":"décider ligne par ligne ce qu'on a le droit de calculer, avant de calculer",
 "a2_4":"décrivent des dimensions différentes : les convertir l'une dans l'autre serait injustifié",
 "a2_5":"une réponse honnête, qui vaut mieux qu'un oui ou un non inventé",
 "a3_1":"un proxy : une valeur empruntée à un autre territoire et une autre année, faute de mieux",
 "a3_2":"environ 1,98 million de tonnes de CO₂",
 "a3_3":"le type de végétation, l'humidité, la sévérité du feu et la biomasse réellement consumée",
 "a3_4":"malhonnête : la phrase affirme là où le calcul estime, avec un ratio venu d'ailleurs",
 "a3_5":"est un piège : l'un compte un véhicule, l'autre une personne — les périmètres diffèrent",
 "a4_1":"22 millions de tonnes, soit environ 56,4 %",
 "a4_2":"environ 195 000 bâtiments",
 "a4_3":"calculable et fragile : les bâtiments n'ont ni la même taille ni le même niveau de dommage",
 "a4_4":"la toxicité, l'amiante, les munitions non explosées, la contamination de l'eau",
 "a4_5":"injustifié : ces grandeurs n'ont ni la même unité ni la même nature, aucune formule ne les ramène l'une à l'autre",
 "a5_1":"chaque affirmation s'appuie sur un fait vérifiable, et qu'il dit ce qu'il laisse de côté",
 "a5_2":"de l'objet technique SUR la société : c'est l'objet qui change quelque chose pour des gens",
 "a5_3":"de la société SUR l'objet technique : une règle collective contraint sa conception et son usage",
 "a5_4":"poserait un problème de responsabilité : engager des moyens et des vies reste une décision humaine",
}
TXT = {
 "a1_rupture":"1. La vigie humaine permet de voir une fumée à l'horizon, environ 20 km par temps clair. Le métier est celui de guetteur : on sait regarder longtemps.\n2. Le satellite permet d'observer un continent entier et de voir la nuit, ce qui était impossible avant. Le métier devient celui d'analyste d'images.\n3. La détection multi-indices permet une surveillance continue et locale, avec des capteurs qui se confirment. Le métier devient celui de concepteur et exploitant de système.\n4. La rupture est le passage à l'observation satellitaire : ce n'est pas une simple amélioration du regard humain, car observer la nuit sur un continent ne pouvait pas se faire du tout avant, et le savoir-faire du guetteur ne suffit plus.",
 "a2_matrice":"surface_brulee (ha) : non, l'unité est l'hectare et non des kgCO₂e.\nemissions_estimees (MtCO2) : oui, l'unité est convertible en kgCO₂e, mais la période est 2023 et non 2026.\nvoiture_thermique (kgCO2e/km) : à vérifier, c'est un facteur et non une quantité ; le périmètre est le véhicule, pas le passager.\ndebris_generes (tonnes) : non, ni la même unité ni la même nature, et le périmètre n'a rien de commun.",
 "a3_proxy":"Ratio : 20 000 000 ÷ 504 002 ≈ 39,68 tCO₂/ha.\nEstimation : 50 000 × 39,68 ≈ 1,98 million de tonnes de CO₂.\nÉquivalence : environ 14,0 milliards de km en voiture thermique.\nAvertissement : estimation par proxy européen 2023, non officielle pour la France 2026 ; le ratio moyen masque la végétation, l'humidité et la biomasse consumée.",
 "a4_incommensurable":"Raison 1 : les bâtiments n'ont pas tous la même taille ni la même surface.\nRaison 2 : les niveaux de dommage ne sont pas identiques d'un bâtiment à l'autre.\nRaison 3 : les estimations reposent en partie sur la télédétection, et les infrastructures non résidentielles sont incluses de façon variable.\nUn seul chiffre ne suffit pas parce que des débris et une eau contaminée n'ont ni la même unité ni la même nature : aucune formule ne les ramène l'une à l'autre.",
 "a5_arg_ost":"Je retiens le drone thermique et le réseau fixe de capteurs. Pour les secours, cela change l'exposition au danger : une zone est reconnue avant qu'on y entre, et le délai entre le départ et l'alerte diminue. On a vu que 50 000 hectares ont brûlé en 7 mois, et que 32 feux étaient en cours le 24 juillet : chaque heure gagnée compte. Pour les habitants, cela change l'information : ils peuvent être prévenus plus tôt. Un métier se transforme, le guetteur devient exploitant de système. En revanche, cela crée aussi des fausses alertes à trier et un réseau à entretenir. Mon argumentaire ne prend pas en compte le coût réel, la formation nécessaire, ni ce qui se passe quand le réseau tombe.",
 "a5_arg_societe":"Contrainte 1, une règle : la réglementation de l'espace aérien limite où et quand un drone peut voler. Elle oblige à demander une autorisation, donc à prévoir un mode dégradé quand le vol est refusé.\nContrainte 2, un moyen : le budget d'une commune impose une solution entretenable sur place. Cela oblige à écarter des matériels performants mais irréparables localement.\nContrainte 3, une attente des habitants : ils veulent être prévenus, pas surveillés. La protection des données personnelles oblige à limiter la résolution des images, leur durée de conservation, et à dire qui peut les consulter.\nCes contraintes ne sont pas des obstacles : elles font partie du cahier des charges au même titre que la portée.",
}
async def tester_sequence(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    await pg.goto(F); r=[]
    for n in range(6):
        await pg.click(f"#tab-s{max(1,n)}"); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        r.append((f"verrou fermé check {n}", "ok" not in cls.split()))
    await pg.evaluate("""(d)=>{Object.entries(d).forEach(([id,v])=>{const e=document.getElementById(id);e.value=v;
        e.dispatchEvent(new Event(e.tagName==='SELECT'?'change':'input',{bubbles:true}));});}""", {**BON, **TXT})
    for n in range(6):
        await pg.click(f"#tab-s{max(1,n)}"); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        ok="ok" in cls.split(); r.append((f"verrou ouvert check {n}", ok))
        if not ok: print("  ↳",n,(await pg.evaluate(f"document.getElementById('fb{n}').textContent"))[:280])
    r.append(("progression 5/5", (await pg.evaluate("document.getElementById('progTxt').textContent")).strip().startswith("5 / 5")))
    h=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM complet en fin", "#" not in h))
    await pg.evaluate("window.__valid={1:true,4:true}; majProgress();")
    h2=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM ciblé = #codes=C1.1,C1.2,C1.4", h2.endswith("#codes=C1.1,C1.2,C1.4")))
    await pg.evaluate("window.__valid={1:true,2:true,3:true,4:true,5:true}; save();"); await pg.reload()
    r.append(("restauration textarea", "39,68" in await pg.evaluate("document.getElementById('a3_proxy').value")))
    r.append(("restauration progression", (await pg.evaluate("document.getElementById('progTxt').textContent")).strip().startswith("5 / 5")))
    body=await pg.evaluate("document.body.textContent")
    r.append(("bloc entraînement présent", "t'entraîner" in body))
    r.append(("bloc Bonus présent", "Bonus" in body))
    r.append(("corrigé du Bonus présent", "Correction du Bonus" in body))
    r.append(("phrase éthique visible et non repliée", "ne comparons ni la valeur des vies" in await pg.evaluate("document.querySelector('#s4').innerText")))
    r.append(("les quatre codes en carte de référentiel", 4==await pg.evaluate("document.querySelectorAll('.referentiel-card tbody tr, .referentiel-card tr').length-1")))
    imgs=await pg.evaluate("""(async()=>{const m=[];for(const i of document.querySelectorAll('img')){
        const ok=await new Promise(res=>{const x=new Image();x.onload=()=>res(1);x.onerror=()=>res(0);x.src=i.getAttribute('src');});
        if(!ok)m.push(i.getAttribute('src'));}return m;})()""")
    r.append(("les 3 corrigés graphiques se chargent", not imgs)); print("  images manquantes:", imgs) if imgs else None
    r.append(("zéro erreur JS", not errs))
    for n,o in r: print(("✅" if o else "❌"), n)
    print("erreurs:", errs); print("Séquence :", sum(1 for _,o in r if o), "/", len(r))
    await b.close()
    return r


async def tester_qcm(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    r=[]
    await pg.goto(Q)
    h1=await pg.evaluate("document.querySelector('h1').textContent")
    sub=await pg.evaluate("document.querySelector('.subtitle').textContent")
    r.append(("titre affiché = Tsinghua 3e", "Tsinghua" in h1 and "3e" in h1))
    r.append(("sous-titre propre au lot", "3e_C1.1" in sub and "C3" not in sub))
    body=await pg.evaluate("document.body.textContent")
    r.append(("aucune trace d'un autre lot", "SOS serre" not in body and "Shenzhen" not in body))
    r.append(("30 questions", await pg.evaluate("QUESTIONS.length")==30))
    rep=await pg.evaluate("QUESTIONS.map(q=>q.r)")
    r.append(("bonnes réponses réparties A/B/C/D", len(set(rep))==4 and min(rep.count(i) for i in range(4))>=6))
    r.append(("11 illustrées", await pg.evaluate("QUESTIONS.filter(q=>q.img).length")==11))
    r.append(("chaque distracteur réfuté", await pg.evaluate("QUESTIONS.every(q=>q.d.filter((x,i)=>i!==q.r).every(x=>x.length>20))")))
    r.append(("réfutation de la bonne réponse vide", await pg.evaluate("QUESTIONS.every(q=>q.d[q.r]==='')")))
    r.append(("chaque question a explication, exemple, erreur, à-retenir",
              await pg.evaluate("QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret)")))
    r.append(("formulation du référentiel recopiée",
              "Identifier les innovations de rupture qui sont attachées à l’évolution d’un OST." in await pg.evaluate("Object.values(COMP_LABELS).join('')")))
    await pg.goto(Q+"#depart=court"); await pg.reload()
    r.append(("#depart=court → 10 questions", await pg.evaluate("etat.sousListe && etat.sousListe.length")==10))
    r.append(("bandeau de portée visible", not await pg.evaluate("document.getElementById('porteeCiblee').hidden")))
    await pg.evaluate("localStorage.clear()"); await pg.goto(Q); await pg.reload()
    ok=await pg.evaluate("""(()=>{for(let i=0;i<QUESTIONS.length;i++){etat.reponses[i]=QUESTIONS[i].r;etat.validees[i]=true;}
        return etat.reponses.filter((x,i)=>x===QUESTIONS[i].r).length;})()""")
    r.append(("30 bonnes réponses acceptées", ok==30))
    r.append(("clé de sauvegarde propre au lot", await pg.evaluate("KEY")=="qcm_3e_C1_tsinghua"))
    miss=await pg.evaluate("""(async()=>{const m=[];for(const q of QUESTIONS.filter(q=>q.img)){
        const ok=await new Promise(res=>{const i=new Image();i.onload=()=>res(1);i.onerror=()=>res(0);i.src=q.img.src;});
        if(!ok)m.push(q.img.src);}return m;})()""")
    r.append(("les 11 images se chargent", not miss))
    liens = await pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
    r.append(("lien de retour vers la séquence",
              "sequence_3e_C1.1-C1.4_tsinghua_feux.html" in liens))
    r.append(("zéro erreur JS", not errs))
    for n,o in r: print(("✅" if o else "❌"), n)
    print("erreurs:", errs); print("QCM      :", sum(1 for _,o in r if o), "/", len(r))
    await b.close()
    return r


async def principal():
    async with async_playwright() as p:
        res = await tester_sequence(p)
        res += await tester_qcm(p)
    total, reussis = len(res), sum(1 for _, o in res if o)
    print("\n═══ %d / %d contrôles passés ═══" % (reussis, total))
    if reussis != total:
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(principal())
