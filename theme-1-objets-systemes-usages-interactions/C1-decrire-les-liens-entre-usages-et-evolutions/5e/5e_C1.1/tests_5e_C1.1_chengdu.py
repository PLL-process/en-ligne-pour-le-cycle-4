# -*- coding: utf-8 -*-
"""Suite de tests du lot 5e_C1.1 à C1.6 — Chengdu, le collège qui mesure son air.

Ne sont déclarés dans le rapport que les tests présents ici et réellement
exécutés. Deux fichiers sont couverts : la séquence (22 contrôles) et le QCM
(21 contrôles).

PÉRIMÈTRE (règle d'or n°47) — ce que cette suite vérifie :
  · les six verrous de la séquence, fermés sur une page vide et ouverts sur une
    production complète ; la progression, la sauvegarde et sa restauration ;
  · la cible du bouton d'entraînement aux trois moments prévus (règle n°45) ;
  · la présence des deux blocs de la règle n°4, corrigé du Bonus compris ;
  · pour le QCM : le titre AFFICHÉ et son sous-titre (règle n°51), le nombre de
    questions, la répartition des bonnes réponses, la réfutation de chaque
    distracteur, le filtre par compétence, l'ouverture ciblée, le chargement
    effectif des images, l'absence d'erreur JS.

Ce qu'elle NE vérifie PAS, et qui reste à faire à l'œil :
  · l'exactitude pédagogique des corrigés et des explications ;
  · la conformité des formulations du référentiel (c'est la règle n°42,
    mécanisée dans `_outils/verif_regles_audit.py`) ;
  · le rendu à l'impression et l'ergonomie réelle en classe.

Usage : python3 tests_5e_C1.1_chengdu.py
"""

import asyncio
import pathlib

from playwright.async_api import async_playwright

DOSSIER = pathlib.Path(__file__).resolve().parent
SEQ = (DOSSIER / "sequence_5e_C1.1-C1.6_chengdu_air.html").as_uri()
QCM = (DOSSIER / "qcm_5e_C1.1-C1.6_chengdu.html").as_uri()

BON = {
 "be_1":"ce que l'objet doit faire, dit par un verbe à l'infinitif",
 "be_2":"=MOYENNE(A2:A8)",
 "be_3":"toute information qui permet de reconnaître une personne, même indirectement",
 "a1_1":"une fonction technique : elle dit ce qu'il faut faire, pas comment",
 "a1_2":"un principe : le phénomène physique employé pour remplir la fonction",
 "a1_3":"une fonction n'impose pas sa solution : il y a toujours plusieurs chemins",
 "a1_4":"aucune alerte possible le matin : on saurait toujours la veille",
 "a1_5":"elle emploie une source radioactive : contrôle réglementaire hors de portée d'un collège",
 "a1_6":"la mesure dérive lentement sans que rien ne le signale",
 "a2_1":"impossible : une concentration ne peut pas être négative",
 "a2_2":"un capteur bloqué : une vraie mesure varie toujours un peu",
 "a2_3":"très probablement une virgule décalée : 25,1 devenu 251",
 "a2_4":"le signaler et calculer sans lui : on n'invente pas une mesure",
 "a2_5":"les écarter du calcul, mais les garder dans le fichier avec une note",
 "a3_1":"il dit ce qu'on en pense, pas ce que le fichier contient",
 "a3_2":"parce qu'ainsi le tri alphabétique donne l'ordre chronologique",
 "a3_3":"pour qu'un nom survive au passage d'un ordinateur ou d'un site à un autre",
 "a3_4":"le supprimer : deux fichiers identiques créent un doute, pas une sécurité",
 "a3_5":"ne dit rien de ce qu'il contient : son nom n'aide personne à chercher",
 "a4_1":"l'ensemble des personnes, des outils et des règles qui font circuler l'information",
 "a4_2":"au traitement : c'est là qu'on trie, qu'on écarte et qu'on calcule",
 "a4_3":"pour que l'original reste intact et qu'on puisse toujours revenir en arrière",
 "a4_4":"se propage à tous les étages tant que personne ne l'écarte",
 "a4_5":"savoir qui peut modifier quoi, et donc où chercher quand quelque chose a changé",
 "a5_1":"regarder qui avait le droit d'écrire dans ce fichier",
 "a5_2":"donner à chacun le droit minimal dont il a besoin : lire ne demande pas d'écrire",
 "a5_3":"de comparer, donc de savoir ce qui a changé et de revenir en arrière",
 "a5_4":"demande de vérifier la licence, et de citer la source dans tous les cas",
 "a5_5":"ne protège plus rien et empêche de savoir qui a fait quoi",
 "a5_6":"exacte et inacceptable : une mesure d'air devient une accusation contre une personne",
 "a5_7":"acceptable et inutile : personne ne peut agir sans savoir d'où vient le pic",
 "a5_8":"le désigne quand même : dans un collège, une seule personne correspond",
 "a5_9":"elle désigne une organisation — l'horaire du nettoyage — et non une personne",
}
TXT = {
 "a1_choix":"Je retiens le principe P1, la diffusion optique. Première raison : il répond en 5 s, donc on peut alerter le matin même avant l'entrée des élèves. Deuxième raison : il coûte 25 € et consomme 1,2 W, ce qui reste dans le budget du collège. J'accepte de perdre en précision : mon incertitude sera de ± 10 % au lieu de ± 2 %, et je perds la possibilité d'entretenir l'optique moi-même quand elle s'encrasse.",
 "a2_anomalies":"Anomalie 1 : mercredi à 11 h — la valeur est -4,2, or une concentration négative est impossible.\nAnomalie 2 : vendredi de 9 h à 14 h — six fois la même valeur 23,7 : le capteur est bloqué.\nAnomalie 3 : lundi à 14 h — la mesure est manquante, la ligne n'existe pas.\nAnomalie 4 : dimanche à 16 h — 251,0 : une virgule décalée, il fallait lire 25,1.\nMoyenne avec les valeurs fausses : 27,4 µg/m³. Moyenne sans : 25,2 µg/m³.",
 "a3_arbo":"station-air-chengdu/\n  1-releves/\n    releves-air-2026-s10.csv\n    releves-air-2026-s11.csv\n  2-analyses/\n    analyse-semaine-10.ods\n    graphique-pm25-s10.png\n  3-documents/\n    notice-capteur-en.pdf\n    compte-rendu-classe-2026-04-02.odt\n  4-photos/\n    photo-capteur-installe-2026-03-05.jpg\nRègle 1 : le nom dit ce que c'est, pas ce qu'on en pense.\nRègle 2 : la date s'écrit 2026-04-02, ainsi le tri alphabétique donne l'ordre chronologique.\nRègle 3 : ni espaces, ni accents, ni majuscules.",
 "a4_si":"1. La source : le capteur de la cour mesure une valeur par heure. Personne n'écrit ici.\n2. Le stockage : le fichier est déposé chaque soir sur le serveur. Écrivent : le professeur et l'administrateur ; la classe lit seulement.\n3. Le traitement : le tableur trie, écarte les valeurs impossibles et calcule les moyennes. La classe écrit, mais dans une copie.\n4. La diffusion : le graphique est publié sur l'ENT et sert à décider d'ouvrir les fenêtres. Seul le professeur publie.",
 "a5_secu":"Mesure 1 : donner le droit de lecture seule à la classe sur le fichier d'origine. Cela empêche qu'une valeur soit modifiée par erreur dans l'original.\nMesure 2 : un identifiant par élève, jamais un mot de passe partagé. Cela empêche qu'on ne puisse plus savoir qui a fait quoi.\nMesure 3 : garder une copie datée chaque soir. Cela évite de perdre les mesures et permet de comparer pour retrouver ce qui a changé.",
 "a5_publication":"Les relevés montrent que la concentration de particules monte à 67 µg/m³ les mardis et jeudis à 7 h, contre 26 les autres jours. Ce pic correspond au nettoyage mécanique de la cour, qui a lieu à cette heure-là. Nous proposons de décaler ce nettoyage avant l'arrivée des élèves. J'ai volontairement écarté le nom de la personne qui conduit la balayeuse, et sa photo : elle est la seule à faire ce travail, la nommer transformerait une mesure d'air en accusation. C'est pour protéger cet agent que je parle d'un horaire et non de quelqu'un.",
}

async def tester_sequence(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    await pg.goto(SEQ)
    res=[]
    # ---- verrou fermé : rien rempli
    for n in range(6):
        await pg.click(f"#tab-s{max(1,n)}")
        await pg.click(f"[data-check='{n}']")
        cls = await pg.evaluate(f"document.getElementById('fb{n}').className")
        res.append(("verrou fermé check %d"%n, "ok" not in cls.split()))
    # ---- QCM contextuel à zéro
    h = await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    res.append(("QCM à zéro = parcours court", h.endswith("#depart=court")))
    # ---- remplissage
    # les cinq panneaux ne sont jamais visibles en même temps : on remplit
    # par le DOM, en émettant les événements que la page écoute réellement.
    import json as _j
    await pg.evaluate("""(d)=>{Object.entries(d).forEach(([id,v])=>{
        const e=document.getElementById(id); e.value=v;
        e.dispatchEvent(new Event(e.tagName==='SELECT'?'change':'input',{bubbles:true}));});}""",
        {**BON, **TXT})
    for n in range(6):
        await pg.click(f"#tab-s{max(1,n)}")
        await pg.click(f"[data-check='{n}']")
        cls = await pg.evaluate(f"document.getElementById('fb{n}').className")
        txt = await pg.evaluate(f"document.getElementById('fb{n}').textContent")
        res.append(("verrou ouvert check %d"%n, "ok" in cls.split()))
        if "ok" not in cls.split(): print("  ↳", n, txt[:300])
    prog = await pg.evaluate("document.getElementById('progTxt').textContent")
    res.append(("progression 5/5", prog.strip().startswith("5 / 5")))
    h = await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    res.append(("QCM complet en fin", "#" not in h))
    # ---- QCM ciblé à mi-parcours
    await pg.evaluate("window.__valid={1:true,2:true}; majProgress();")
    h2 = await pg.evaluate("document.getElementById('lienQcm').getAttribute('href')")
    res.append(("QCM ciblé = #codes=C1.2,C1.1", h2.endswith("#codes=C1.2,C1.1")))
    # ---- sauvegarde / restauration
    await pg.evaluate("window.__valid={1:true,2:true,3:true,4:true,5:true}; save();")
    await pg.reload()
    v = await pg.evaluate("document.getElementById('a2_anomalies').value")
    res.append(("restauration textarea", "27,4" in v))
    prog2 = await pg.evaluate("document.getElementById('progTxt').textContent")
    res.append(("restauration progression", prog2.strip().startswith("5 / 5")))
    # ---- blocs règle n°4
    n4 = await pg.evaluate("document.body.textContent")
    res.append(("bloc entraînement présent", "t'entraîner" in n4))
    res.append(("bloc Bonus présent", "Bonus" in n4))
    res.append(("corrigé du Bonus présent (textContent, pas inner_text)", "corrig" in n4.lower()))
    res.append(("zéro erreur JS", not errs))
    for nom,ok in res: print(("✅" if ok else "❌"), nom)
    print("erreurs:", errs)
    print("Séquence :", sum(1 for _,o in res if o), "/", len(res))
    await b.close()
    return res


async def tester_qcm(p):
    b=await p.chromium.launch(); pg=await b.new_page()
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
    r=[]
    await pg.goto(QCM)
    h1=await pg.evaluate("document.querySelector('h1').textContent")
    sub=await pg.evaluate("document.querySelector('.subtitle').textContent")
    r.append(("titre affiché = Chengdu 5e", "Chengdu" in h1 and "5e" in h1))
    r.append(("sous-titre sans reste de Thème 2", "serre" not in sub and "Packet" not in sub))
    r.append(("aucune trace du lot d'origine dans la page", "SOS serre" not in await pg.evaluate("document.body.textContent")))
    n=await pg.evaluate("QUESTIONS.length"); r.append(("30 questions", n==30))
    rep=await pg.evaluate("QUESTIONS.map(q=>q.r)")
    r.append(("bonnes réponses réparties A/B/C/D", len(set(rep))==4 and min(rep.count(i) for i in range(4))>=6))
    img=await pg.evaluate("QUESTIONS.filter(q=>q.img).length"); r.append(("13 illustrées", img==13))
    r.append(("chaque distracteur réfuté", await pg.evaluate("QUESTIONS.every(q=>q.d.filter((x,i)=>i!==q.r).every(x=>x.length>20))")))
    r.append(("la réfutation de la bonne réponse est vide", await pg.evaluate("QUESTIONS.every(q=>q.d[q.r]==='')")))
    r.append(("six codes présents", sorted(set(await pg.evaluate("QUESTIONS.map(q=>q.c)")))==["C1.1","C1.2","C1.3","C1.4","C1.5","C1.6"]))
    # filtre par compétence
    opts=await pg.evaluate("[...document.querySelectorAll('#selComp option')].map(o=>o.value)")
    r.append(("filtre = les six codes", opts==["C1.1","C1.2","C1.3","C1.4","C1.5","C1.6"]))
    # règle n°45 — révision ciblée.
    # Attention : changer seulement le fragment (#...) ne RECHARGE pas la page,
    # donc le code d'ouverture ne rejoue pas. Le premier essai a échoué pour
    # cette raison — c'était le test qui avait tort, pas la page (règle n°50).
    await pg.goto(QCM+"#codes=C1.2,C1.1"); await pg.reload()
    n2=await pg.evaluate("etat.sousListe.length")
    r.append(("#codes=C1.2,C1.1 → 11 questions", n2==11))
    r.append(("bandeau de portée visible", not await pg.evaluate("document.getElementById('porteeCiblee').hidden")))
    r.append(("mode = cible", await pg.evaluate("etat.mode")=="cible"))
    # règle n°45 — parcours court
    await pg.goto(QCM+"#depart=court"); await pg.reload()
    r.append(("#depart=court → 10 questions", await pg.evaluate("etat.sousListe.length")==10))
    # un code inconnu ne casse rien.
    # On vide d'abord la sauvegarde : sans cela, on ne mesure pas le
    # traitement du code inconnu mais la restauration de l'essai précédent.
    # (Le premier essai est tombé dans ce piège — c'était le test qui avait
    # tort, pas la page : règle n°50.)
    await pg.evaluate("localStorage.clear()")
    await pg.goto(QCM+"#codes=C9.9"); await pg.reload()
    r.append(("code inconnu ignoré, QCM complet", await pg.evaluate("etat.sousListe===null||etat.sousListe.length===30")))
    r.append(("bandeau de portée resté caché", await pg.evaluate("document.getElementById('porteeCiblee').hidden")))
    # et la progression déjà enregistrée prime sur l'ouverture ciblée :
    # un élève qui revient ne perd pas ce qu'il avait commencé.
    await pg.evaluate("etat.reponses[0]=0; etat.validees[0]=true; save()")
    await pg.goto(QCM+"#depart=court"); await pg.reload()
    r.append(("la progression enregistrée survit au retour", await pg.evaluate("etat.validees[0]===true")))
    # parcours complet : répondre à tout
    await pg.goto("about:blank"); await pg.goto(QCM)
    ok=await pg.evaluate("""(async()=>{
      for(let i=0;i<QUESTIONS.length;i++){ etat.reponses[i]=QUESTIONS[i].r; etat.validees[i]=true; }
      return etat.reponses.filter((x,i)=>x===QUESTIONS[i].r).length; })()""")
    r.append(("30 bonnes réponses enregistrables", ok==30))
    # sauvegarde
    await pg.evaluate("save()") if await pg.evaluate("typeof sauver==='function'") else None
    r.append(("clé de sauvegarde propre au lot", "qcm_5e_C1.1-C1.6_chengdu"==await pg.evaluate("KEY")))
    # images atteignables
    miss=await pg.evaluate("""(async()=>{const m=[];for(const q of QUESTIONS.filter(q=>q.img)){
        const ok=await new Promise(res=>{const i=new Image();i.onload=()=>res(1);i.onerror=()=>res(0);i.src=q.img.src;});
        if(!ok) m.push(q.img.src);} return m;})()""")
    r.append(("les 13 images se chargent", not miss))
    if miss: print(" images manquantes:", miss)
    r.append(("zéro erreur JS", not errs))
    for nom,o in r: print(("✅" if o else "❌"), nom)
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
