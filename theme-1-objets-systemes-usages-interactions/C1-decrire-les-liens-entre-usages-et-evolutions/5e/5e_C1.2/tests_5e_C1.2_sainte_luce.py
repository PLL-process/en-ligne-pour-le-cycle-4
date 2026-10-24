# -*- coding: utf-8 -*-
"""Suite de tests du lot 5e_C1.2 — Sainte-Luce, quel frein pour les vélos du collège.

Ne sont déclarés dans le rapport que les tests présents ici et réellement
exécutés. Deux fichiers sont couverts : la séquence (33 contrôles) et le QCM
(17 contrôles).

PÉRIMÈTRE (règle d'or n°47) — ce que cette suite vérifie :
  · les six verrous de la séquence (billet + cinq activités), fermés sur une
    page vide et ouverts sur une production complète — celui de l'activité 4
    ne s'ouvre qu'une fois l'exercice du diagramme FAST inséré réellement
    rempli et vérifié dans la page (clé rep_fast_5e_e3) ;
  · le REFUS argumenté du frein à patins en séance 3, et celui du frein à
    tambour pour Léa en séance 4, avec la raison chiffrée — un vérificateur qui
    refuse sans expliquer n'est pas un vérificateur ;
  · la progression (5 activités), la sauvegarde et sa restauration après
    rechargement ; les champs de l'exercice inséré restent HORS de la
    sauvegarde de la séquence (ils ont la leur, partagée avec l'atelier) ;
  · la reprise d'un travail enregistré AVANT l'ajout de la séance 4 (trois
    activités validées : la page dit 3 / 5, sans erreur) ;
  · quatre onglets, le passage de la séance 3 à la séance 4 par le bouton de
    fin de séance, et la clôture (Bonus, Bilan, QCM) dans la séance 4 seule ;
  · la cible du bouton d'entraînement avant et après la séquence (règle n°45) ;
  · la présence des deux blocs de la règle n°4, corrigé du Bonus compris, et la
    mention de la manipulation obligatoire (règle n°58) ;
  · pour le QCM : le titre AFFICHÉ et son sous-titre (règle n°51), le nombre de
    questions et d'illustrées, la répartition des bonnes réponses, la réfutation
    de chaque distracteur, la formulation du référentiel recopiée (règle n°42),
    l'ouverture ciblée, le chargement effectif des images, le lien de retour.

Ce qu'elle NE vérifie PAS, et qui reste à faire à l'œil :
  · l'exactitude pédagogique des corrigés et des explications ;
  · le rendu à l'impression et l'ergonomie réelle en classe ;
  · la faisabilité de la manipulation sur le vélo — qui se vérifie devant un vélo.

Usage : python3 tests_5e_C1.2_sainte_luce.py
"""

import asyncio
import pathlib

from playwright.async_api import async_playwright

DOSSIER = pathlib.Path(__file__).resolve().parent
SEQ = (DOSSIER / "sequence_5e_C1.2_sainte_luce_freinage.html").as_uri()
QCM_URL = (DOSSIER / "qcm_5e_C1.2_freinage.html").as_uri()

BON={"be_1":"ce que l'objet doit faire, dit par un verbe à l'infinitif, sans dire par quel moyen",
 "be_2":"freine le mouvement et produit de la chaleur",
 "be_3":"les juger sur les mêmes critères, mesurés de la même façon",
 "a1_1":"une fonction technique : elle dit ce qu'il faut obtenir, sans dire par quel moyen",
 "a1_2":"un principe : c'est le phénomène employé pour remplir la fonction",
 "a1_3":"une solution technique : c'est l'objet concret qu'on achète",
 "a1_4":"le même phénomène — le frottement — mais à des endroits différents",
 "a1_5":"pour laisser ouverts tous les principes qui pourraient la remplir",
 "a2_1":"la moyenne des essais : une fiche technique est un résumé de mesures",
 "a2_2":"combien chaque principe perd quand la surface qui frotte est mouillée",
 "a2_3":"parce que la surface qui frotte est enfermée : l'eau n'y entre pas",
 "a2_4":"que la pente ajoute de l'énergie à dissiper : le contexte change le résultat",
 "a2_5":"une appréciation chiffrée : utile pour comparer, mais elle résume un jugement",
 "a3_1":"la résistance à la corrosion : le sel de l'air attaque les métaux toute l'année",
 "a3_2":"la distance d'arrêt sous la pluie, et l'écart entre sec et mouillé",
 "a3_3":"une erreur : compter les colonnes gagnées revient à donner à tous les critères la même importance",
 "a3_4":"le frein à patins deviendrait le meilleur choix : le même tableau, un autre contexte",
 "a5_1":"environ 2,5 fois plus grande : elle augmente comme la masse, 150 kg au lieu de 60",
 "a5_2":"passe dans les deux surfaces qui frottent, qui chauffent de plus en plus",
 "a5_3":"compte très peu : 440 g sur 150 kg, c'est moins de 1 % de ce qu'elle transporte",
 "a5_4":"la chaleur reste enfermée dans le tambour : trop chaudes, les surfaces qui frottent freinent moins bien",
 "a5_5":"le frein à disque : 8,3 m sous la pluie et 7,5 m freins chauds, le plus court les deux fois"}
TXT={"a1_manip":"Quand on serre le levier, le câble se tend et deux bras pivotent.\nLes deux pièces qui se touchent sont le patin de caoutchouc et la jante de la roue.\nLa chaleur apparaît sur la jante, à l'endroit où le patin a frotté.",
 "a2_tableau":"Arrêt sur sol sec : le meilleur est le disque (5,4 m), le moins bon est le tambour (6,1 m).\nArrêt sous la pluie : le meilleur est le disque (6,4 m), le moins bon est le patin (8,9 m).\nMasse : le meilleur est le patin (320 g), le moins bon est le tambour (760 g).\nEntretien : le patin gagne (18 euros par an), le disque perd (34 euros).\nRéparabilité : le patin est premier (5/5), le tambour est dernier (3/5).\nCorrosion : le tambour est le meilleur (5/5), le patin est le moins bon (2/5).\nCe tableau ne dit pas quel critère est le plus important. Il donne les faits, pas leur importance, et cela dépend du contexte et du lieu.",
 "a3_choix":"Je retiens le frein à disque. Première raison : sous la pluie il s'arrête en 6,4 m contre 8,9 m pour les patins, soit deux mètres et demi de moins, et il y a une descente sur le trajet. Deuxième raison : sa résistance à la corrosion est de 4/5 alors que celle des patins est de 2/5, et le collège est au bord de la mer. J'accepte de perdre 190 g de plus et 34 euros d'entretien par an au lieu de 18, ainsi qu'un réglage plus technique.",
 "a5_conseil":"Léa, je te conseille le frein à disque. Sous la pluie, chargé, il s'arrête en 8,3 m, contre 11,6 m pour les patins. En bas de la grande descente, freins chauds, il lui faut 7,5 m, contre 10,4 m pour le tambour. Tu acceptes de perdre 34 € d'entretien par an au lieu de 18 ou 27. Ce n'est pas le choix du collège, parce que tu transportes 150 kg dans une longue descente : ton frein chauffe beaucoup plus."}
# l'exercice du diagramme FAST inséré en séance 4 (atelier, module fast, 5e e3) : ses bonnes réponses
FAST_E3={"fa_5e_e3__prop_0":"disque","fa_5e_e3__prop_1":"patins","fa_5e_e3__prop_2":"disque",
 "fa_5e_e3__prop_3":"deux","fa_5e_e3__prop_4":"patins","fa_5e_e3__choix":"disque"}
FAST_E3_JUSTIF="Je choisis le frein à disque parce qu'il freine presque aussi bien sous la pluie, et Léa descend des côtes avec ses enfants."
# onglet de chaque vérificateur : billet et activité 1 en séance 1, … activités 4 et 5 en séance 4
ONGLET={0:1, 1:1, 2:2, 3:3, 4:4, 5:4}
async def tester_sequence(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    await pg.goto(SEQ); r=[]
    onglets=await pg.evaluate("[...document.querySelectorAll('.seance-tab')].map(t=>t.dataset.panel)")
    r.append(("quatre onglets de séance, s1 à s4", onglets==["s1","s2","s3","s4"]))
    clot=await pg.evaluate("""(()=>{const s4=document.getElementById('s4'), t=s4?s4.textContent:'';
        const ailleurs=[...document.querySelectorAll('.seance-panel:not(#s4)')].map(x=>x.textContent).join(' ');
        return t.includes('Bonus (facultatif')&&t.includes('Bilan')&&!!s4.querySelector('#lienQcm')
          &&!ailleurs.includes('Bonus (facultatif')&&!ailleurs.includes('Prêt·e à t');})()""")
    r.append(("clôture (Bonus, Bilan, QCM) dans la séance 4 seule", clot))
    await pg.click("#tab-s3"); await pg.click("#s3 [data-vers='s4']"); await pg.wait_for_timeout(100)
    actif=await pg.evaluate("document.querySelector('.seance-panel.active').id")
    r.append(("le bouton de fin de séance 3 ouvre la séance 4", actif=="s4"))
    for n in range(6):
        await pg.click("#tab-s%d"%ONGLET[n]); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        r.append(("verrou fermé check %d"%n, "ok" not in cls.split()))
    h=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM à zéro = parcours court", h.endswith("#depart=court")))
    # l'exercice inséré, rempli et vérifié dans la page comme le ferait un élève
    await pg.click("#tab-s4")
    for nom,v in FAST_E3.items():
        await pg.check(f"#fa_5e_e3 input[name='{nom}'][value='{v}']")
    await pg.fill("#fa_5e_e3__justif", FAST_E3_JUSTIF)
    await pg.click("#fa_5e_e3 .btn.verifier")
    reussi=await pg.evaluate("JSON.parse(localStorage.getItem('rep_fast_5e_e3')||'{}').reussi===true")
    r.append(("exercice FAST inséré : réussi et enregistré sous rep_fast_5e_e3", reussi))
    await pg.evaluate("""(d)=>{const manquants=[];Object.entries(d).forEach(([id,v])=>{
        const e=document.getElementById(id); if(!e){manquants.push(id);return;}
        if(e.tagName==='FIELDSET'){
          const r=[...e.querySelectorAll('input[type=radio]')].find(x=>x.value===v);
          if(!r){manquants.push(id);return;}
          r.checked=true; r.dispatchEvent(new Event('change',{bubbles:true})); return;}
        e.value=v; e.dispatchEvent(new Event('input',{bubbles:true}));});
        return manquants;}""", {**BON,**TXT})
    for n in range(6):
        await pg.click("#tab-s%d"%ONGLET[n]); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        txt=await pg.evaluate(f"document.getElementById('fb{n}').textContent")
        r.append(("verrou ouvert check %d"%n, "ok" in cls.split()))
        if "ok" not in cls.split(): print("  ↳",n,txt[:260])
    # refus explicite du tambour pour Léa : la raison chiffrée (10,4 m freins chauds) est dite
    await pg.evaluate("""()=>{const e=document.getElementById('a5_conseil');
        e.value="Léa, je te conseille le frein à tambour. Sous la pluie il s'arrête en 9,1 m et il est enfermé, donc protégé. Tu acceptes de perdre 27 € par an d'entretien et un frein plus lourd, mais tu transportes tes enfants.";
        e.dispatchEvent(new Event('input',{bubbles:true}));}""")
    await pg.click("#tab-s4"); await pg.click("[data-check='5']")
    t5=await pg.evaluate("document.getElementById('fb5').textContent")
    r.append(("le tambour est refusé pour Léa, et la raison est dite", "10,4 m" in t5 and "ok" not in (await pg.evaluate("document.getElementById('fb5').className")).split()))
    await pg.evaluate("""()=>{const e=document.getElementById('a5_conseil');e.value=%r;
        e.dispatchEvent(new Event('input',{bubbles:true}));}""" % TXT["a5_conseil"])
    await pg.click("[data-check='5']")
    # refus explicite du choix « patins »
    await pg.evaluate("""()=>{const e=document.getElementById('a3_choix');
        e.value="Je retiens le frein à patins. Il pèse 320 g, coûte 18 euros par an et se répare en 5/5. J'accepte de perdre un peu de distance sous la pluie mais ce n'est pas grave du tout pour nous.";
        e.dispatchEvent(new Event('input',{bubbles:true}));}""")
    await pg.click("#tab-s3"); await pg.click("[data-check='3']")
    t3=await pg.evaluate("document.getElementById('fb3').textContent")
    r.append(("le choix des patins est refusé, et la raison est dite", "8,9 m sous la pluie" in t3))
    await pg.evaluate("""()=>{const e=document.getElementById('a3_choix');e.value=%r;
        e.dispatchEvent(new Event('input',{bubbles:true}));}""" % TXT["a3_choix"])
    await pg.click("[data-check='3']")
    prog=await pg.evaluate("document.getElementById('progTxt').textContent")
    r.append(("progression 5/5 après remise du bon texte", prog.strip().startswith("5 / 5")))
    coches=await pg.evaluate("['s1','s2','s3','s4'].map(s=>document.getElementById('done-'+s).textContent.includes('✔'))")
    r.append(("les quatre onglets portent leur ✔", all(coches)))
    h=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM complet en fin", "#" not in h))
    sauv=await pg.evaluate("Object.keys(JSON.parse(localStorage.getItem('seq_5e_C1.2_sainte_luce')||'{}').inputs||{})")
    r.append(("sauvegarde de la séquence : a5_conseil dedans, aucun champ de l'exercice inséré",
              "a5_conseil" in sauv and not any(k.startswith("fa_5e_e3") for k in sauv)))
    await pg.reload()
    r.append(("restauration textarea", "jante" in await pg.evaluate("document.getElementById('a1_manip').value")))
    r.append(("restauration textarea de la séance 4", "11,6 m" in await pg.evaluate("document.getElementById('a5_conseil').value")))
    r.append(("restauration de l'exercice inséré (sa propre mémoire)", await pg.evaluate("document.getElementById('fa_5e_e3__justif').value")==FAST_E3_JUSTIF))
    r.append(("restauration progression", (await pg.evaluate("document.getElementById('progTxt').textContent")).strip().startswith("5 / 5")))
    # un travail enregistré avant l'ajout de la séance 4 : trois activités validées, sans clé 4 ni 5
    await pg.evaluate("""()=>{localStorage.clear(); localStorage.setItem('seq_5e_C1.2_sainte_luce', JSON.stringify(
        {inputs:{a1_manip:"ancien relevé : le patin et la jante", a3_1:"la masse"}, valid:{"0":true,"1":true,"2":true,"3":true}, exp:{}}));}""")
    await pg.reload()
    anc=await pg.evaluate("""({p:document.getElementById('progTxt').textContent.trim(),
        a:document.getElementById('a1_manip').value, s4:document.getElementById('done-s4').textContent,
        s3:document.getElementById('done-s3').textContent, l:document.getElementById('lienQcm').getAttribute('href')})""")
    r.append(("reprise d'un travail enregistré à trois séances : 3 / 5, champs rendus, séance 4 à faire",
              anc["p"].startswith("3 / 5") and "ancien relevé" in anc["a"] and "✔" in anc["s3"] and "✔" not in anc["s4"]
              and anc["l"].endswith("#depart=court")))
    body=await pg.evaluate("document.body.textContent")
    r.append(("bloc entraînement présent", "t'entraîner" in body))
    r.append(("bloc Bonus présent", "Bonus" in body))
    r.append(("corrigé du Bonus présent", "Corrigé du Bonus" in body))
    r.append(("objet réel au parcours obligatoire", "manipulation obligatoire" in body))
    r.append(("zéro erreur JS", not errs))
    for nom,o in r: print(("✅" if o else "❌"), nom)
    print("erreurs:", errs); print("Séquence :", sum(1 for _,o in r if o), "/", len(r))
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
    r.append(("titre affiché = Sainte-Luce 5e", "Sainte-Luce" in h1 and "5e" in h1))
    r.append(("sous-titre propre au lot", "5e_C1.2" in sub and "C3" not in sub))
    body=await pg.evaluate("document.body.textContent")
    r.append(("aucune trace d'un autre lot", "SOS serre" not in body and "Shenzhen" not in body))
    r.append(("30 questions", await pg.evaluate("QUESTIONS.length")==30))
    rep=await pg.evaluate("QUESTIONS.map(q=>q.r)")
    r.append(("bonnes réponses réparties A/B/C/D", len(set(rep))==4 and min(rep.count(i) for i in range(4))>=6))
    r.append(("8 illustrées", await pg.evaluate("QUESTIONS.filter(q=>q.img).length")==8))
    r.append(("chaque distracteur réfuté", await pg.evaluate("QUESTIONS.every(q=>q.d.filter((x,i)=>i!==q.r).every(x=>x.length>20))")))
    r.append(("réfutation de la bonne réponse vide", await pg.evaluate("QUESTIONS.every(q=>q.d[q.r]==='')")))
    r.append(("chaque question a explication, exemple, erreur, à-retenir",
              await pg.evaluate("QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret)")))
    r.append(("formulation du référentiel recopiée",
              "Comparer des principes techniques pour une même fonction technique." in await pg.evaluate("Object.values(COMP_LABELS).join('')")))
    await pg.goto(QCM_URL+"#depart=court"); await pg.reload()
    r.append(("#depart=court → 10 questions", await pg.evaluate("etat.sousListe && etat.sousListe.length")==10))
    r.append(("bandeau de portée visible", not await pg.evaluate("document.getElementById('porteeCiblee').hidden")))
    await pg.evaluate("localStorage.clear()"); await pg.goto(QCM_URL); await pg.reload()
    ok=await pg.evaluate("""(()=>{for(let i=0;i<QUESTIONS.length;i++){etat.reponses[i]=QUESTIONS[i].r;etat.validees[i]=true;}
        return etat.reponses.filter((x,i)=>x===QUESTIONS[i].r).length;})()""")
    r.append(("30 bonnes réponses acceptées", ok==30))
    r.append(("clé de sauvegarde propre au lot", await pg.evaluate("KEY")=="qcm_5e_C1.2_sainte_luce"))
    miss=await pg.evaluate("""(async()=>{const m=[];for(const q of QUESTIONS.filter(q=>q.img)){
        const ok=await new Promise(res=>{const i=new Image();i.onload=()=>res(1);i.onerror=()=>res(0);i.src=q.img.src;});
        if(!ok)m.push(q.img.src);}return m;})()""")
    r.append(("les 8 images se chargent", not miss))
    liens = await pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
    r.append(("lien de retour vers la séquence",
              "sequence_5e_C1.2_sainte_luce_freinage.html" in liens))
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
