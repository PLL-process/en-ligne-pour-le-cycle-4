#!/usr/bin/env python3
"""Suite de tests du lot Shenzhen 3e_C3.1 à C3.4.  python3 tests_3e_C3.1-C3.4_shenzhen.py"""
from playwright.sync_api import sync_playwright
import pathlib, sys
SEQ = pathlib.Path("sequence_3e_C3.1-C3.4_shenzhen.html").resolve().as_uri()
QCM = pathlib.Path("qcm_3e_C3.1-C3.4_shenzhen.html").resolve().as_uri()
res = []
def t(n, ok, d=""): res.append((n, bool(ok))); print(("✔" if ok else "✘"), n, d)

# Les exercices insérés (ateliers « Le besoin » et « Les exigences ») : les bonnes réponses sont lues dans leurs
# définitions, embarquées dans la page — le banc suit l'exercice si son rédacteur le retouche. Seules les réponses
# écrites sont données ici (l'exemple juste de la définition).
REMPLIR = """([uid, textes]) => {
  const box = document.getElementById(uid);
  const D = JSON.parse(box.closest('.atelier-incruste').querySelector('script[type="application/json"]').textContent).exercices[uid];
  const coche = (name, val) => { const i = box.querySelector(`input[name="${name}"][value="${val}"]`);
    if (!i) throw new Error('option absente : ' + name + ' = ' + val); i.checked = true; i.dispatchEvent(new Event('change', {bubbles: true})); };
  for (const w of D.widgets) {
    if (w.type === 'choix') coche(w.name, w.bonne);
    else if (w.type === 'cases') box.querySelectorAll(`input[name="${w.name}"]`).forEach(i => { i.checked = w.bonnes.includes(i.value); });
    else if (w.type === 'classer') w.items.forEach(it => coche(it.name, it.bonne));
    else if (w.type === 'slots') w.slots.forEach(s => coche(s.name, s.bonnes[0]));
    else { const z = box.querySelector(`textarea[name="${w.name}"]`); z.value = textes[w.name.split('__')[1]]; z.dispatchEvent(new Event('input', {bubbles: true})); }
  }
}"""
def exercice_insere(pg, uid, nom, textes=None):
    """Vérifié à vide (retour 🔴), puis rempli juste (« Tout est juste »)."""
    pg.click(f"#{uid} button.verifier"); pg.wait_for_timeout(80)
    t(f"{nom} : à vide, le retour demande de reprendre", "🔴" in pg.inner_text(f"#{uid} .retour"))
    pg.evaluate(REMPLIR, [uid, textes or {}])
    pg.click(f"#{uid} button.verifier"); pg.wait_for_timeout(80)
    t(f"{nom} : rempli juste, il est réussi", "Tout est juste" in pg.inner_text(f"#{uid} .retour"))

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1280,"height":900})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))

    pg.goto(SEQ); pg.wait_for_timeout(600)
    t("séquence : aucune erreur JS", not errs, str(errs))
    # `pg.content()` sérialise le DOM : chaque SVG en ligne y porte son
    # `xmlns="http://www.w3.org/2000/svg"`, qui est un identifiant d'espace de noms
    # et non une ressource — aucun navigateur ne le demande. Chercher « http:// »
    # dans le HTML rendait donc ce contrôle rouge dès qu'un schéma était dessiné
    # dans la page. On regarde maintenant ce que la page IRAIT CHERCHER : les
    # attributs de chargement, sans les hyperliens, qui eux ont le droit d'être
    # distants (règle d'or n°40, correction du 31/08/2026).
    distantes = pg.eval_on_selector_all(
        "[src], link[href], object[data], iframe[src], use[href]",
        "l=>l.map(e=>e.getAttribute('src')||e.getAttribute('href')||e.getAttribute('data'))"
        ".filter(u=>u && /^(https?:)?\/\//i.test(u))")
    t("séquence : hors ligne, aucune ressource distante (n°40)",
      "fonts.googleapis" not in pg.content() and not distantes, str(distantes))
    t("bandeau de tâches affiché (n°30)", "Séance 1" in pg.inner_text("#tachesBandeau"))
    # Les exercices insérés (atelier des représentations) apportent leurs propres zones : comptées à part.
    n_ta = pg.eval_on_selector_all("textarea:not(.atelier-incruste textarea)", "a=>a.length")
    n_et = pg.eval_on_selector_all("details.etayage:not(.atelier-incruste details)", "a=>a.length")
    t("chaque zone de rédaction a sa version étayée (n°31)",
      n_ta == n_et == 9, f"{n_ta} zones / {n_et} étayages")
    i_ta = pg.eval_on_selector_all(".atelier-incruste textarea", "a=>a.length")
    i_et = pg.eval_on_selector_all(".atelier-incruste details.etayage", "a=>a.length")
    t("exercices insérés : chaque zone de rédaction a sa version étayée (n°31)",
      i_ta >= 1 and i_ta == i_et, f"{i_ta} zones / {i_et} étayages")
    t("chaque champ porte une étiquette (n°34)",
      pg.evaluate("[...document.querySelectorAll('select,textarea')].every(e=>!e.id||"
                  "document.querySelector(`label[for=\"${e.id}\"]`)||e.getAttribute('aria-label'))"))
    t("chaque figure a une alternative longue",
      pg.evaluate("[...document.querySelectorAll('.fig img')].every(i=>i.alt.length>120)"))
    # billet d'entrée : oriente sans sanctionner
    pg.click('[data-check="0"]'); pg.wait_for_timeout(150)
    t("billet d'entrée : oriente sans note (n°26)",
      "aucune note" in pg.inner_text("#fb0"), pg.inner_text("#fb0")[:60])
    # activité 1 complète
    pg.evaluate("['a1_1','a1_2','a1_3','a1_4','a1_5','a1_6']"
                ".forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
    pg.click('[data-check="1"]'); pg.wait_for_timeout(150)
    t("activité 1 : la liste des trois familles est exigée",
      "TROIS familles" in pg.inner_text("#fb1"), pg.inner_text("#fb1")[-45:])
    pg.fill("#a1_liste", "Solution 1 (passive) : ventilation naturelle traversante. "
                         "Solution 2 (passive) : ombrage du mur ouest. "
                         "Solution 3 (active) : extracteur asservi au thermostat. "
                         "Solution 4 (active) : climatiseur split. "
                         "Solution 5 (organisationnelle) : réduire le nombre de machines.")
    pg.click('[data-check="1"]'); pg.wait_for_timeout(150)
    t("activité 1 : l'exercice de l'alerte cyclonique est exigé",
      "alerte cyclonique" in pg.inner_text("#fb1") and "0 / 5" in pg.inner_text("#progTxt"), pg.inner_text("#fb1")[-90:])
    # l'exercice inséré en tête de l'activité 1 (atelier « Le besoin », 3e)
    exercice_insere(pg, "bc_3e_e6", "activité 1 : la liste d'OST de l'alerte cyclonique",
                    {"liste": "une sirène\nun SMS sur le téléphone\nla radio locale\nun haut-parleur sur une voiture\nun panneau lumineux"})
    pg.click('[data-check="1"]'); pg.wait_for_timeout(150)
    t("activité 1 : validée une fois la liste écrite", "6 / 6" in pg.inner_text("#fb1"))
    t("progression mise à jour", "1 / 5" in pg.inner_text("#progTxt"))
    # verrou de rédaction : l'activité 2 refuse sans texte
    pg.click("#tab-s2"); pg.wait_for_timeout(150)
    pg.evaluate("['a2_1','a2_2','a2_3','a2_4','a2_5','a2_6']"
                ".forEach(i=>{const g=document.getElementById(i);const r=g.querySelector('input[type=radio]');if(!r)throw new Error('aucune proposition dans '+i);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));})")
    pg.click('[data-check="2"]'); pg.wait_for_timeout(150)
    t("activité 2 : la défense de la grille est exigée",
      "grille" in pg.inner_text("#fb2"), pg.inner_text("#fb2")[-55:])
    pg.fill("#a2_grille", "J'ai retenu le coût sur dix ans, la performance, la consommation "
                          "et la réparabilité. Le coût sur dix ans pèse le plus car le collège "
                          "doit tenir un budget durable. Si le besoin avait été urgent, "
                          "j'aurais privilégié la performance.")
    pg.click('[data-check="2"]'); pg.wait_for_timeout(150)
    t("activité 2 : l'exercice de la flexibilité est exigé",
      "flexibilité" in pg.inner_text("#fb2") and "1 / 5" in pg.inner_text("#progTxt"), pg.inner_text("#fb2")[-90:])
    # l'exercice inséré avant « b) Construire la grille » (atelier « Les exigences », 3e : classes F0 à F3)
    exercice_insere(pg, "ex_3e_e5", "activité 2 : les classes de flexibilité")
    pg.click('[data-check="2"]'); pg.wait_for_timeout(150)
    t("activité 2 : validée une fois rédigée", "6 / 6" in pg.inner_text("#fb2"))
    # mode essentiel
    pg.click("#btnEssentiel"); pg.wait_for_timeout(150)
    t("mode essentiel masque référentiel et corrections (n°29)",
      not pg.is_visible(".referentiel-card") and not pg.is_visible("details.correction"))
    # la version étayée de la séquence (celle de l'exercice inséré est rangée dans son aide 2, repliée)
    t("mode essentiel laisse les versions étayées visibles",
      pg.is_visible(".seance-panel.active details.etayage:not(.atelier-incruste details)"))
    pg.click("#btnEssentiel")
    # sauvegarde
    pg.reload(); pg.wait_for_timeout(600)
    t("sauvegarde et restauration après rechargement",
      "1 / 5" in pg.inner_text("#progTxt") or "2 / 5" in pg.inner_text("#progTxt"))
    # innerText ignore les panneaux masqués : on interroge le document, pas l'affichage.
    contenu = pg.content()
    t("blocs de la règle n°4 présents",
      "Prêt·e à t'entraîner" in contenu and "Bonus (facultatif" in contenu)
    t("un seul bouton QCM",
      pg.eval_on_selector_all('a.btn.qcm',"a=>a.length")==1)
    t("pas de défilement horizontal à 1280 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"))
    pg.set_viewport_size({"width":390,"height":844}); pg.wait_for_timeout(300)
    t("pas de défilement horizontal à 390 px",
      pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+2"))
    pg.set_viewport_size({"width":1280,"height":900})

    # ── le vérificateur de l'activité 3 juge un PROTOCOLE, pas quatre chiffres (audit du 08/09, A02) ──
    ATT3 = {"a3_1":"la grandeur mesurée, son unité et l'appareil",
            "a3_2":"ne suffit pas : l'air est plus chaud près des machines et sous le plafond",
            "a3_3":"à plusieurs moments de la journée, dont le plus défavorable — ici, la fin d'après-midi",
            "a3_4":"la position du capteur, la porte fermée, et le nombre de machines allumées",
            "a3_5":"que la solution doit faire gagner au moins 9 °C au moment le plus défavorable",
            "a3_6":"ne dit rien du pic d'été : il faut préciser les conditions extérieures dans le protocole"}
    def verif3(prot):
        return pg.evaluate("""([att, prot])=>{ for (const [id,v] of Object.entries(att)) { document.getElementById(id).value=v; }
            document.getElementById('a3_prot').value=prot; return CHECKS[3](); }""", [ATT3, prot])
    pg.goto(SEQ); pg.wait_for_timeout(300)
    bon = ("1. Grandeur : la température de l'air en °C.\n2. Appareil : un thermomètre numérique, le même pour toutes les mesures.\n"
           "3. Points de mesure : au centre de la salle à 1,5 m du sol et près des machines.\n4. Moments : 9 h, 12 h et 17 h, trois relevés à chaque fois.\n"
           "5. Conditions constantes : même position du capteur, porte fermée, toutes les machines allumées.")
    faible = ("1. On mesure la température. 2. On note. 3. On recommence. 4. On compare avec avant. "
              "Il faut faire attention à bien mesurer au bon endroit et au bon moment pour que ce soit juste et fiable.")
    t("activité 3 : un protocole à cinq étapes, avec unité, appareil et conditions constantes, est validé", verif3(bon)["valide"])
    t("activité 3 : quatre numéros et 120 caractères sans unité ni appareil ne sont PAS validés", not verif3(faible)["valide"])

    errs.clear(); pg.goto(QCM); pg.wait_for_timeout(600)
    t("QCM : aucune erreur JS", not errs, str(errs))
    t("QCM : hors ligne (n°40)", "fonts.googleapis" not in pg.content())
    t("QCM : 30 questions", pg.evaluate("QUESTIONS.length")==30)
    t("QCM : 1 illustrée avec alternative longue",
      pg.evaluate("QUESTIONS.filter(q=>q.img).length")==1
      and pg.evaluate("QUESTIONS.filter(q=>q.img).every(q=>q.img.alt.length>80)"))
    rep = pg.evaluate("QUESTIONS.reduce((a,q)=>(a[q.r]=(a[q.r]||0)+1,a),{})")
    t("QCM : bonnes réponses réparties sur A/B/C/D", min(rep.values())>=7, str(rep))
    t("QCM : aucune réfutation en face de la bonne réponse",
      pg.evaluate("QUESTIONS.every(q=>q.d[q.r]==='')"))
    t("QCM : chaque distracteur réfuté",
      pg.evaluate("QUESTIONS.every(q=>q.d.filter((x,i)=>i!==q.r).every(x=>x&&x.length>20))"))
    t("QCM : les quatre codes sont couverts",
      set(pg.evaluate("[...new Set(QUESTIONS.map(q=>q.c))]"))=={"C3.1","C3.2","C3.3","C3.4"})
    t("QCM : les cinq champs de correction sont remplis",
      pg.evaluate("QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret&&q.n)"))
    b.close()

print(f"\n{sum(1 for _,o in res if o)} / {len(res)} tests passés")
sys.exit(0 if all(o for _,o in res) else 1)
