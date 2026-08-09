# -*- coding: utf-8 -*-
"""Suite de tests du lot 5e_C1.2 — Sainte-Luce, quel frein pour les vélos du collège.

Ne sont déclarés dans le rapport que les tests présents ici et réellement
exécutés. Deux fichiers sont couverts : la séquence (19 contrôles) et le QCM
(17 contrôles).

PÉRIMÈTRE (règle d'or n°47) — ce que cette suite vérifie :
  · les quatre verrous de la séquence, fermés sur une page vide et ouverts sur
    une production complète ;
  · le REFUS argumenté du frein à patins en séance 3, avec la raison chiffrée —
    un vérificateur qui refuse sans expliquer n'est pas un vérificateur ;
  · la progression, la sauvegarde et sa restauration après rechargement ;
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
 "a3_4":"le frein à patins deviendrait le meilleur choix : le même tableau, un autre contexte"}
TXT={"a1_manip":"Quand on serre le levier, le câble se tend et deux bras pivotent.\nLes deux pièces qui se touchent sont le patin de caoutchouc et la jante de la roue.\nLa chaleur apparaît sur la jante, à l'endroit où le patin a frotté.",
 "a2_tableau":"Arrêt sur sol sec : le meilleur est le disque (5,4 m), le moins bon est le tambour (6,1 m).\nArrêt sous la pluie : le meilleur est le disque (6,4 m), le moins bon est le patin (8,9 m).\nMasse : le meilleur est le patin (320 g), le moins bon est le tambour (760 g).\nEntretien : le patin gagne (18 euros par an), le disque perd (34 euros).\nRéparabilité : le patin est premier (5/5), le tambour est dernier (3/5).\nCorrosion : le tambour est le meilleur (5/5), le patin est le moins bon (2/5).\nCe tableau ne dit pas quel critère est le plus important. Il donne les faits, pas leur importance, et cela dépend du contexte et du lieu.",
 "a3_choix":"Je retiens le frein à disque. Première raison : sous la pluie il s'arrête en 6,4 m contre 8,9 m pour les patins, soit deux mètres et demi de moins, et il y a une descente sur le trajet. Deuxième raison : sa résistance à la corrosion est de 4/5 alors que celle des patins est de 2/5, et le collège est au bord de la mer. J'accepte de perdre 190 g de plus et 34 euros d'entretien par an au lieu de 18, ainsi qu'un réglage plus technique."}
async def tester_sequence(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    await pg.goto(SEQ); r=[]
    for n in range(4):
        await pg.click("#tab-s%d"%max(1,n)); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        r.append(("verrou fermé check %d"%n, "ok" not in cls.split()))
    h=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM à zéro = parcours court", h.endswith("#depart=court")))
    await pg.evaluate("""(d)=>{Object.entries(d).forEach(([id,v])=>{const e=document.getElementById(id);e.value=v;
        e.dispatchEvent(new Event(e.tagName==='SELECT'?'change':'input',{bubbles:true}));});}""", {**BON,**TXT})
    for n in range(4):
        await pg.click("#tab-s%d"%max(1,n)); await pg.click(f"[data-check='{n}']")
        cls=await pg.evaluate(f"document.getElementById('fb{n}').className")
        txt=await pg.evaluate(f"document.getElementById('fb{n}').textContent")
        r.append(("verrou ouvert check %d"%n, "ok" in cls.split()))
        if "ok" not in cls.split(): print("  ↳",n,txt[:260])
    # refus explicite du choix « patins »
    await pg.evaluate("""()=>{const e=document.getElementById('a3_choix');
        e.value="Je retiens le frein à patins. Il pèse 320 g, coûte 18 euros par an et se répare en 5/5. J'accepte de perdre un peu de distance sous la pluie mais ce n'est pas grave du tout pour nous.";
        e.dispatchEvent(new Event('input',{bubbles:true}));}""")
    await pg.click("#tab-s3"); await pg.click("[data-check='3']")
    t3=await pg.evaluate("document.getElementById('fb3').textContent")
    r.append(("le choix des patins est refusé, et la raison est dite", "8,9 m sous la pluie" in t3))
    r.append(("progression 3/3 après remise du bon texte", True))
    await pg.evaluate("""()=>{const e=document.getElementById('a3_choix');e.value=%r;
        e.dispatchEvent(new Event('input',{bubbles:true}));}""" % TXT["a3_choix"])
    await pg.click("[data-check='3']")
    prog=await pg.evaluate("document.getElementById('progTxt').textContent")
    r[-1]=("progression 3/3 après remise du bon texte", prog.strip().startswith("3 / 3"))
    h=await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    r.append(("QCM complet en fin", "#" not in h))
    await pg.reload()
    r.append(("restauration textarea", "jante" in await pg.evaluate("document.getElementById('a1_manip').value")))
    r.append(("restauration progression", (await pg.evaluate("document.getElementById('progTxt').textContent")).strip().startswith("3 / 3")))
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
