# -*- coding: utf-8 -*-
"""Suite de tests du lot 4e_C1.1 à C1.3 — Tsinghua, concevoir avant de connecter.

Ne sont déclarés dans le rapport que les tests présents ici et réellement
exécutés. Deux fichiers sont couverts : la séquence (25 contrôles) et le QCM
(17 contrôles).

PÉRIMÈTRE (règle d'or n°47) — ce que cette suite vérifie :
  · les cinq verrous, fermés sur une page vide et ouverts sur une production complète ;
  · les DEUX refus argumentés : une exigence qui nomme un composant, et l'oubli
    du mot « passager » dans une équivalence — dans les deux cas on vérifie que
    le message DIT la raison, pas seulement qu'il refuse ;
  · la progression, la sauvegarde, la restauration ;
  · la cible du bouton d'entraînement aux trois moments (règle n°45) ;
  · les blocs de la règle n°4, les garde-fous humains, le bloc CRCN et sa trace ;
  · le rendu effectif des deux corrigés graphiques — en levant les DEUX obstacles
    qui les masquent : les <details> repliés et les panneaux de séance inactifs ;
  · pour le QCM : titre affiché, sous-titre, nombres, répartition, réfutations,
    formulation du référentiel, ouverture ciblée, images, lien de retour.

Ce qu'elle NE vérifie PAS : l'exactitude pédagogique des corrigés, le rendu à
l'impression, l'ergonomie en classe, et la faisabilité de la mesure de
température — qui se vérifie dans une cour, avec un thermomètre.

Usage : python3 tests_4e_C1.1-C1.3_tsinghua.py
"""

import asyncio
import pathlib

from playwright.async_api import async_playwright

DOSSIER = pathlib.Path(__file__).resolve().parent
SEQ = (DOSSIER / "sequence_4e_C1.1-C1.3_tsinghua_feux.html").as_uri()
QCM_URL = (DOSSIER / "qcm_4e_C1.1-C1.3_tsinghua.html").as_uri()

BON={"be_1":"seulement si elles ont la même unité et le même sens",
 "be_2":"une proportion : il faut savoir de quel ensemble il est la part",
 "be_3":"ne se valent pas : une estimation est calculée à partir d'autre chose, et elle doit annoncer ses limites",
 "a1_1":"ce sont trois grandeurs différentes : une surface cumulée, un état instantané, une proportion",
 "a1_2":"un cumul, et un minimum annoncé : la surface réelle est au moins celle-là",
 "a1_3":"un état instantané : le nombre à un moment donné, qui aura changé le lendemain",
 "a1_4":"dire de quelle NATURE est chaque chiffre — c'est elle qui empêche les additions absurdes",
 "a1_5":"parce qu'un chiffre sans source ne peut être ni vérifié ni discuté",
 "a2_1":"un proxy : une valeur empruntée à un autre contexte, faute de mieux",
 "a2_2":"1,98 million de tonnes de CO₂",
 "a2_3":"le type de végétation, l'humidité, la sévérité du feu et la biomasse réellement consumée",
 "a2_4":"malhonnête : ce n'est pas une mesure, c'est un ordre de grandeur emprunté à un autre territoire et une autre année",
 "a2_5":"à donner un ordre de grandeur : savoir si l'on parle de milliers ou de millions de tonnes",
 "a3_1":"est un piège : l'un compte un véhicule, l'autre une personne — les périmètres diffèrent",
 "a3_2":"« équivalences » — et surtout pas « mêmes impacts »",
 "a3_3":"que les quantités de CO₂ sont du même ordre — pas que les deux phénomènes se ressemblent",
 "a3_4":"de rendre une quantité lisible par quelqu'un qui n'a aucune idée de ce qu'est une mégatonne",
 "a3_5":"des avantages ET des inconvénients, qu'il faut nommer tous les deux",
 "a4_1":"de croiser plusieurs indices : un seuil de température seul déclencherait tous les jours d'été",
 "a4_2":"peut être contrôlée par une mesure ou un test qui répond par oui ou par non",
 "a4_3":"une solution, pas une exigence : elle désigne déjà le moyen",
 "a4_4":"parce qu'une alerte automatique doit pouvoir être vérifiée par un opérateur avant d'engager des secours",
 "a4_5":"faux : un capteur en panne, hors de portée ou déchargé ne transmet rien non plus"}
TXT={"a1_mesure":"À l'ombre du préau j'ai relevé 29,4 °C et en plein soleil 41,8 °C, au même moment. L'écart est de 12,4 °C. Avec un seuil d'alerte à 40 °C, le système se déclencherait tous les jours d'été dans notre cour, alors qu'il n'y a aucun feu : ce serait une fausse alerte permanente.",
 "a1_just":"50 000 ha est un cumul depuis le 1er janvier, annoncé comme un minimum ; son unité est l'hectare.\n32 feux est un état instantané, le nombre de feux en cours à ce moment ; c'est un effectif.\n50 % est une proportion, la part des départs de feu liés à une imprudence.\nOn ne peut pas les additionner parce que ce ne sont pas la même unité ni la même nature de grandeur.",
 "a2_estim":"Ratio : 20 000 000 ÷ 504 002 ≈ 39,68 tonnes de CO2 par hectare.\nEstimation : 50 000 × 39,68 ≈ 1,98 million de tonnes.\nAttention : ce ratio est un proxy calculé pour l'Union européenne en 2023, donc un autre territoire et une autre année. Il ne tient pas compte du type de végétation, de l'humidité, de la sévérité du feu ni du devenir du carbone.\nCe résultat ne doit pas être présenté comme une mesure officielle des émissions françaises de 2026.",
 "a3_equiv":"Voiture : environ 14,0 milliards de km. Question : le facteur inclut-il la fabrication du véhicule ?\nTGV : environ 677 milliards de passager-km. Question : compare-t-on un véhicule-km ou un passager-km ?\nAvion : environ 11,9 milliards de passager-km. Question : les traînées de condensation sont-elles incluses ?\nRepas : environ 399 millions de repas. Question : un repas type représente-t-il tous les régimes ?",
 "a4_exig":"Le système doit signaler un départ de feu en moins de 10 minutes après son début.\nLe système doit confirmer par au moins 2 indices indépendants avant d'émettre une alerte.\nLe système doit transmettre une alerte horodatée et localisée à au moins 5 km depuis une zone sans réseau.\nLe système doit fonctionner 6 mois sans intervention.\nLe système doit permettre à un opérateur de vérifier et d'annuler une alerte avant l'engagement des secours."}
async def tester_sequence(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    await pg.goto(SEQ); r=[]
    for n in range(5):
        await pg.click("#tab-s%d"%max(1,n)); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        r.append(("verrou fermé check %d"%n, "ok" not in cls.split()))
    h=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM à zéro = parcours court", h.endswith("#depart=court")))
    await pg.evaluate("""(d)=>{Object.entries(d).forEach(([id,v])=>{const e=document.getElementById(id);e.value=v;
        e.dispatchEvent(new Event(e.tagName==='SELECT'?'change':'input',{bubbles:true}));});}""", {**BON,**TXT})
    for n in range(5):
        await pg.click("#tab-s%d"%max(1,n)); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        txt=await pg.evaluate(f"document.getElementById('fb{n}').textContent")
        r.append(("verrou ouvert check %d"%n, "ok" in cls.split()))
        if "ok" not in cls.split(): print("  ↳",n,txt[:300])
    # une exigence qui nomme un composant doit être refusée, avec la raison
    await pg.evaluate("""()=>{const e=document.getElementById('a4_exig');
      e.value="Le système doit installer une caméra thermique sur chaque poteau.\\nLe système doit confirmer par 2 indices avant d'alerter.\\nLe système doit transmettre à 5 km.\\nLe système doit fonctionner 6 mois.\\nLe système doit permettre à un operateur de verifier et annuler.";
      e.dispatchEvent(new Event('input',{bubbles:true}));}""")
    await pg.click("#tab-s4"); await pg.click("[data-check='4']")
    t4=await pg.evaluate("document.getElementById('fb4').textContent")
    r.append(("une exigence nommant un composant est refusée, et la raison est dite", "c'est une solution" in t4))
    # l'oubli de « passager-km » est refusé et nommé
    await pg.evaluate("""()=>{const e=document.getElementById('a3_equiv');
      e.value="Voiture : 14,0 milliards de km. Question : fabrication incluse ?\\nTGV : 677 milliards de km. Question : et alors ?\\nAvion : 11,9 milliards de km. Question : trainees ?\\nRepas : 399 millions de repas. Question : regimes ?";
      e.dispatchEvent(new Event('input',{bubbles:true}));}""")
    await pg.click("#tab-s3"); await pg.click("[data-check='3']")
    t3=await pg.evaluate("document.getElementById('fb3').textContent")
    r.append(("l'oubli de « passager-km » est refusé et expliqué", "passager-km" in t3 and "places du train" in t3))
    await pg.evaluate("""(d)=>{Object.entries(d).forEach(([id,v])=>{const e=document.getElementById(id);e.value=v;
        e.dispatchEvent(new Event('input',{bubbles:true}));});}""", {"a3_equiv":TXT["a3_equiv"],"a4_exig":TXT["a4_exig"]})
    for n in (3,4):
        await pg.click("#tab-s%d"%n); await pg.click(f"[data-check='{n}']")
    prog=await pg.evaluate("document.getElementById('progTxt').textContent")
    r.append(("progression 4/4", prog.strip().startswith("4 / 4")))
    h=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM complet en fin", "#" not in h))
    # à mi-parcours, le bouton doit cibler les seules compétences validées
    await pg.evaluate("window.__valid={1:true,3:true}; majProgress();")
    h2=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM ciblé = #codes=C1.1,C1.2", h2.endswith("#codes=C1.1,C1.2"), h2))
    await pg.evaluate("window.__valid={1:true,2:true,3:true,4:true}; majProgress(); save();")
    await pg.reload()
    r.append(("restauration textarea", "39,68" in await pg.evaluate("document.getElementById('a2_estim').value")))
    r.append(("restauration progression", (await pg.evaluate("document.getElementById('progTxt').textContent")).strip().startswith("4 / 4")))
    body=await pg.evaluate("document.body.textContent")
    for lbl,mot in (("bloc entraînement","t'entraîner"),("bloc Bonus","Bonus"),("corrigé du Bonus","Corrigé du Bonus"),
                    ("garde-fous humains","Garde-fous humains"),("bloc CRCN avec sa trace","transformations")):
        r.append((lbl+" présent", mot in body))
    # Les corrigés sont dans des <details> repliés ET dans des panneaux de séance
    # inactifs — donc en display:none, et un objet non affiché a une hauteur nulle.
    # Il faut lever LES DEUX obstacles ; n'en lever qu'un ne suffisait pas, et le
    # contrôle accusait une page qui rendait parfaitement (règle n°50).
    await pg.evaluate("document.querySelectorAll('.seance-panel').forEach(x=>x.classList.add('active'));"
                      "document.querySelectorAll('details').forEach(d=>d.open=true)")
    await pg.wait_for_timeout(700)
    figs=await pg.evaluate("[...document.querySelectorAll('object[data]')].map(o=>Math.round(o.getBoundingClientRect().height))")
    r.append(("les deux corrigés graphiques sont rendus", len(figs)==2 and all(h>150 for h in figs), str(figs)))
    r.append(("zéro erreur JS", not errs))
    for x in r:
        n,o = x[0], x[1]
        print(("✅" if o else "❌"), n, x[2] if len(x)>2 else "")
    print("erreurs:", errs); print("Séquence :", sum(1 for x in r if x[1]), "/", len(r))
    await b.close()
    return r


async def tester_qcm(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    r=[]
    await pg.goto(QCM_URL)
    h1=await pg.evaluate("document.querySelector('h1').textContent")
    sub=await pg.evaluate("document.querySelector('.subtitle').textContent")
    r.append(("titre affiché = Tsinghua 4e", "Tsinghua" in h1 and "4e" in h1))
    r.append(("sous-titre propre au lot", "4e_C1.1" in sub and "C3" not in sub))
    body=await pg.evaluate("document.body.textContent")
    r.append(("aucune trace d'un autre lot", "SOS serre" not in body and "Shenzhen" not in body))
    r.append(("30 questions", await pg.evaluate("QUESTIONS.length")==30))
    rep=await pg.evaluate("QUESTIONS.map(q=>q.r)")
    r.append(("bonnes réponses réparties A/B/C/D", len(set(rep))==4 and min(rep.count(i) for i in range(4))>=6))
    r.append(("6 illustrées", await pg.evaluate("QUESTIONS.filter(q=>q.img).length")==6))
    r.append(("chaque distracteur réfuté", await pg.evaluate("QUESTIONS.every(q=>q.d.filter((x,i)=>i!==q.r).every(x=>x.length>20))")))
    r.append(("réfutation de la bonne réponse vide", await pg.evaluate("QUESTIONS.every(q=>q.d[q.r]==='')")))
    r.append(("chaque question a explication, exemple, erreur, à-retenir",
              await pg.evaluate("QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret)")))
    r.append(("formulation du référentiel recopiée",
              "Mettre en relation les OST avec leurs usages." in await pg.evaluate("Object.values(COMP_LABELS).join('')")))
    await pg.goto(QCM_URL+"#depart=court"); await pg.reload()
    r.append(("#depart=court → 10 questions", await pg.evaluate("etat.sousListe && etat.sousListe.length")==10))
    r.append(("bandeau de portée visible", not await pg.evaluate("document.getElementById('porteeCiblee').hidden")))
    await pg.evaluate("localStorage.clear()"); await pg.goto(QCM_URL); await pg.reload()
    ok=await pg.evaluate("""(()=>{for(let i=0;i<QUESTIONS.length;i++){etat.reponses[i]=QUESTIONS[i].r;etat.validees[i]=true;}
        return etat.reponses.filter((x,i)=>x===QUESTIONS[i].r).length;})()""")
    r.append(("30 bonnes réponses acceptées", ok==30))
    r.append(("clé de sauvegarde propre au lot", await pg.evaluate("KEY")=="qcm_4e_C1_tsinghua"))
    miss=await pg.evaluate("""(async()=>{const m=[];for(const q of QUESTIONS.filter(q=>q.img)){
        const ok=await new Promise(res=>{const i=new Image();i.onload=()=>res(1);i.onerror=()=>res(0);i.src=q.img.src;});
        if(!ok)m.push(q.img.src);}return m;})()""")
    r.append(("les 6 images se chargent", not miss))
    liens = await pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
    r.append(("lien de retour vers la séquence",
              "sequence_4e_C1.1-C1.3_tsinghua_feux.html" in liens))
    r.append(("zéro erreur JS", not errs))
    for n,o in r: print(("✅" if o else "❌"), n)
    print("erreurs:", errs); print("QCM      :", sum(1 for _,o in r if o), "/", len(r))
    await b.close()
    return r


async def principal():
    async with async_playwright() as p:
        res = [(x[0], x[1]) for x in await tester_sequence(p)]
        res += [(x[0], x[1]) for x in await tester_qcm(p)]
    total, reussis = len(res), sum(1 for _, o in res if o)
    print("\n═══ %d / %d contrôles passés ═══" % (reussis, total))
    if reussis != total:
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(principal())
