# -*- coding: utf-8 -*-
"""Banc des séances de 3e_C1.5 — Numérique, société, environnement et santé (390 px).

Écrit le 24/10/2026, quand la séquence est passée de trois à quatre séances de 55 min :
la clôture débordait de la séance 3, elle a suivi la nouvelle séance 4, qui porte
l'activité 5 « L'argumentaire court » (3e_C1.3). Ne sont déclarés que les tests
présents ici et réellement exécutés.

PÉRIMÈTRE (règle n°47) — ce que ce banc vérifie, à 390 px de large :
  · les cinq onglets dans l'ordre (s1 à s4, puis le hors-parcours) et le titre court
    de la séance 4 ; chaque panneau s'ouvre, sans défilement horizontal ;
  · le bouton de fin de chaque séance ouvre la suivante ; la séance 4, dernière, n'en a pas ;
  · Bonus, Bilan, synthèse, autoévaluation et QCM sont dans la séance 4, après l'activité 5,
    dans cet ordre ; le volet « Rappel » y est replié ;
  · le vérificateur de l'activité 5 : à vide (🔴, 11 encoches « sans réponse ») ; des choix
    faux (réfutation sous la question) ; une dernière ligne « complet » refusée ; le modèle
    de la correction et une réponse écrite avec la version étayée acceptés (🎉) ; l'angle
    mort écrit au milieu ; un texte de moins de six lignes ;
  · la sauvegarde à la saisie, puis la reprise après rechargement (argumentaire, choix,
    exercice jumeau, séance ouverte) ;
  · le volet « Tes réponses des séances précédentes » ;
  · l'exercice 2.d de la séance 2 (atelier carte mentale) : il se vérifie toujours, et son
    introduction annonce la séance 4 ;
  · le mode essentiel masque la correction de l'activité 5 ;
  · un travail enregistré AVANT l'ajout de la séance (clé de séance « s3 », réponses
    d'ouverture, de séance 3 et de clôture) revient à sa place ;
  · zéro erreur JS.

Ce qu'il NE vérifie PAS :
  · la justesse pédagogique des corrigés, ni la pertinence des motifs du vérificateur
    au-delà des réponses éprouvées ici ;
  · l'ouverture et le volet « Rappel » à 1280 px, sans JavaScript et à l'impression :
    c'est le banc tests_regle_311_3e_C1.5.mjs ;
  · le QCM du lot.

Usage : python3 tests_3e_C1.5_seances.py   (depuis n'importe quel dossier)
Sortie (règle n°299) : 0 tout passe · 1 au moins un test refuse · 2 rien n'a pu être vérifié
(page absente, Playwright ou Chromium manquant, aucun test exécuté).
"""
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
PAGE = ICI / "sequence-numerique-societe-economie-environnement-sante.html"

MODELE = "\n".join([
    "Le smartphone est une bonne chose pour la société, à condition de savoir ce qu'il coûte.",
    "Il a fait naître des métiers, comme gérer une boutique en ligne, et il garde le contact avec ses proches.",
    "Cependant, tout ce qu'on y fait laisse des traces : une photo publiée sans accord peut exposer la vie privée d'un ami.",
    "Il coûte aussi à l'environnement, surtout par sa fabrication : selon l'étude de l'ADEME et de l'Arcep, "
    "le numérique pesait 4,4 % de l'empreinte carbone de la France en 2022.",
    "Le garder plus longtemps et le faire réparer réduit cet effet.",
    "En conclusion, c'est un outil utile, si l'on règle sa confidentialité et qu'on ne le remplace pas sans raison.",
    "Ce que mon argumentaire ne sait pas : ce que vaut ce chiffre pour la Martinique, où l'électricité ne vient pas "
    "des mêmes sources, ni ce qu'en pensent ceux qui n'ont pas de smartphone."])
DERNIERE_FAUSSE = "Mon argumentaire est complet : il n'y a rien à ajouter."
ETAYE = "\n".join([
    "Je pense que le smartphone est utile pour la société, parce qu'il aide à rester en contact.",
    "Par exemple, il a fait naître des métiers comme vendre en ligne.",
    "Cependant, une photo publiée sans accord peut nuire à la vie privée d'un ami.",
    "Selon l'étude de l'ADEME et de l'Arcep, le numérique pesait 4,4 % de l'empreinte carbone de la France en 2022.",
    "En conclusion, c'est une bonne chose, à condition de régler sa confidentialité.",
    "Ce que mon argumentaire ne sait pas : ce que vaut ce chiffre en Martinique."])

ok = ko = 0


def t(condition, message):
    global ok, ko
    if condition:
        ok += 1
        print("✅", message)
    else:
        ko += 1
        print("❌", message)


def panne(message):
    print("⛔ PANNE — " + message, file=sys.stderr)
    sys.exit(2)


def actif(pg):
    return pg.evaluate("document.querySelector('.seance-panel.active').id")


def debord(pg):
    return pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")


def verifier(pg):
    pg.click("#a5_verifier")
    pg.wait_for_timeout(100)
    return pg.inner_text("#a5_retour")


def banc_page(b, url):
    ctx = b.new_context(viewport={"width": 390, "height": 844})
    pg = ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)[:120]))
    pg.on("console", lambda m: err.append("console:" + m.text[:120]) if m.type == "error" else None)
    pg.on("dialog", lambda d: d.dismiss())
    pg.goto(url)
    pg.evaluate("localStorage.clear()")
    pg.reload()
    pg.wait_for_timeout(300)

    ids = pg.evaluate("[...document.querySelectorAll('.seance-tab')].map(x => x.dataset.panel)")
    t(ids == ["s1", "s2", "s3", "s4", "shors"], f"onglets dans l'ordre : {ids}")
    lib = pg.evaluate("document.getElementById('tab-s4') ? document.getElementById('tab-s4').textContent.trim() : ''")
    t(lib == "Séance 4L'argumentaire court", f"onglet de la séance 4 : « {lib} »")
    for pid in ids:
        pg.click(f'.seance-tab[data-panel="{pid}"]')
        pg.wait_for_timeout(120)
        a, d = actif(pg), debord(pg)
        t(a == pid and d <= 0, f"{pid} s'ouvre (actif = {a}), sans défilement horizontal ({d})")

    for de, vers in [("s1", "s2"), ("s2", "s3"), ("s3", "s4")]:
        pg.click(f'.seance-tab[data-panel="{de}"]')
        pg.wait_for_timeout(80)
        pg.click(f'#{de} .vers-seance[data-vers="{vers}"]')
        pg.wait_for_timeout(150)
        t(actif(pg) == vers, f"le bouton de fin de {de} ouvre {vers}")
    t(pg.evaluate("document.querySelectorAll('#s4 .vers-seance').length") == 0,
      "la séance 4, dernière, n'a pas de bouton « séance suivante »")

    clo = pg.evaluate("['bonus','bilan','synthese-meta','auto-eval','pret-a-s-entrainer']"
                      ".map(id => document.getElementById(id).closest('.seance-panel').id)")
    t(all(x == "s4" for x in clo), f"Bonus, Bilan, synthèse, autoévaluation, QCM dans la séance 4 : {clo}")
    ordre = pg.evaluate("""(() => { const g = id => document.getElementById(id), apres = (x, y) => !!(x.compareDocumentPosition(y) & 4);
      return apres(g('argumentaire-court'), g('bonus')) && apres(g('bonus'), g('bilan')) && apres(g('bilan'), g('pret-a-s-entrainer')); })()""")
    t(ordre, "ordre dans la séance 4 : activité 5 → Bonus → Bilan → QCM")
    vol = pg.evaluate("(() => { const v = document.getElementById('ouverture'); return [v.open, v.classList.contains('volet')]; })()")
    t(vol == [False, True], f"séance 4 : volet « Rappel » replié {vol}")

    # Activité 5 — le vérificateur
    r = verifier(pg)
    t(r.startswith("🔴 0 point"), "vérification à vide : 🔴 0 point sur 11")
    enc = pg.evaluate("[...document.querySelectorAll('#argumentaire-court .enc')].map(e => e.className)")
    t(len(enc) == 11 and all("vide" in c for c in enc), f"11 encoches « sans réponse » à vide ({len(enc)})")

    for case in ["#a5_q1__1", "#a5_q2__1", "#a5_q3__2", "#a5_q4__1"]:
        pg.check(case)
    pg.fill("#a5_arg", MODELE.replace(MODELE.split("\n")[-1], DERNIERE_FAUSSE))
    r = verifier(pg)
    fb1, fb3 = pg.inner_text("#a5_q1_fb"), pg.inner_text("#a5_q3_fb")
    t(fb1.startswith("✘") and "fonctionnement" in fb1, "Q1 fausse : réfutation affichée (fonctionnement)")
    t(fb3.startswith("✘") and "2022" in fb3, "Q3 fausse : réfutation affichée (année des données)")
    t("ce n'est pas un angle mort" in r, "dernière ligne « complet » refusée avec son explication")
    t("🟡" in r and "7 points sur 11" in r, f"score partiel annoncé : {r.splitlines()[0][:70]}")

    for case in ["#a5_q1__2", "#a5_q3__3", "#a5_q4__2"]:
        pg.check(case)
    pg.fill("#a5_arg", MODELE)
    t(verifier(pg).startswith("🎉 Tout est juste"), "modèle de la correction : « Tout est juste » (11/11)")
    pg.fill("#a5_arg", ETAYE)
    t(verifier(pg).startswith("🎉 Tout est juste"), "réponse écrite avec la version étayée : « Tout est juste »")
    lignes = ETAYE.split("\n")
    pg.fill("#a5_arg", "\n".join(lignes[:2] + [lignes[5]] + lignes[2:5]))
    t("pas à la fin" in verifier(pg), "angle mort écrit au milieu : « pas à la fin »")
    pg.fill("#a5_arg", " ".join(lignes[:4]) + " Encore une phrase pour la longueur du texte écrit ici.")
    t("six au moins" in verifier(pg), "moins de six lignes : message « six au moins »")

    # sauvegarde à la saisie, puis reprise
    pg.fill("#a5_arg", MODELE)
    pg.evaluate("document.querySelectorAll('#argumentaire-court > details.aide')[1].open = true")
    pg.fill("#a5_jumeau", "Ce que cet argumentaire ne sait pas : l'avis des préparateurs.")
    pg.wait_for_timeout(1100)
    sv = pg.inner_text("#a5_sauve")
    t(sv.startswith("✔ Enregistré"), f"sauvegarde à la saisie : « {sv[:40]} »")
    pg.reload()
    pg.wait_for_timeout(400)
    t(actif(pg) == "s4", f"après rechargement : la séance 4 est rouverte ({actif(pg)})")
    t(pg.input_value("#a5_arg") == MODELE and pg.is_checked("#a5_q3__3")
      and pg.input_value("#a5_jumeau").startswith("Ce que cet"),
      "après rechargement : argumentaire, choix et jumeau repris")

    # les réponses des séances précédentes
    pg.click('.seance-tab[data-panel="s1"]')
    pg.fill("#auto_17", "Non : les sites gardent des traces.")
    pg.click('.seance-tab[data-panel="s3"]')
    pg.fill("#auto_25", "4,4 %, ADEME et Arcep, données 2022.")
    pg.click('#s3 .vers-seance[data-vers="s4"]')
    pg.wait_for_timeout(200)
    vis = pg.evaluate("!document.getElementById('a5_notes').hidden")
    nb = pg.evaluate("document.querySelectorAll('#a5_notes_liste li').length")
    t(vis and nb == 2, f"« Tes réponses des séances précédentes » : visible, {nb} réponses reprises")

    # l'exercice inséré de la séance 2
    pg.click('.seance-tab[data-panel="s2"]')
    pg.wait_for_timeout(100)
    pg.click("#cm_3e_e5 button.verifier")
    pg.wait_for_timeout(100)
    t(pg.inner_text("#cm_3e_e5 .retour").startswith("🔴"), "séance 2 : l'exercice 2.d se vérifie toujours (🔴 à vide)")
    t("séance 4" in pg.inner_text("#incruste-cm-3e-numerique-societe > p"),
      "séance 2 : l'introduction de 2.d annonce la séance 4")

    # mode essentiel
    pg.click('.seance-tab[data-panel="s4"]')
    pg.click("#btnEssentiel")
    cache = pg.evaluate("getComputedStyle(document.querySelector('#argumentaire-court > details.correction')).display")
    t(cache == "none", "mode essentiel : la correction de l'activité 5 est masquée")
    pg.click("#btnEssentiel")
    t(not err, f"aucune erreur JS {err}")
    ctx.close()


def banc_ancienne_sauvegarde(b, url):
    """Un travail enregistré avant l'ajout de la séance 4 doit revenir à sa place."""
    ctx = b.new_context(viewport={"width": 390, "height": 844})
    pg = ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)[:120]))
    pg.goto(url)
    pg.evaluate("""localStorage.clear(); localStorage.setItem('seance_3e_C1.5', 's3');
      localStorage.setItem('reponses_3e_C1.5', JSON.stringify({auto_15: 'Ma reformulation', auto_30: 'éteindre, wifi, HD',
        auto_54: 'la fabrication', bilan1: 'un effet', pos1__3: true}));""")
    pg.reload()
    pg.wait_for_timeout(400)
    t(actif(pg) == "s3", f"ancienne sauvegarde (séance 3 ouverte) : la séance 3 se rouvre ({actif(pg)})")
    vals = pg.evaluate("""[document.getElementById('auto_15').value, document.getElementById('auto_30').value,
      document.getElementById('auto_54').value, document.getElementById('bilan1').value, document.getElementById('pos1__3').checked]""")
    t(vals == ["Ma reformulation", "éteindre, wifi, HD", "la fabrication", "un effet", True],
      f"ancienne sauvegarde : chaque réponse revient à sa place, y compris celles passées en séance 4 {vals}")
    t(not err, f"aucune erreur JS {err}")
    ctx.close()


def main():
    if not PAGE.is_file():
        panne(f"page introuvable : {PAGE.name}, cherchée dans {ICI}")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        panne("Playwright (Python) n'est pas installé : pip install playwright, puis playwright install chromium")
    url = PAGE.as_uri()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            banc_page(b, url)
            banc_ancienne_sauvegarde(b, url)
            b.close()
    except Exception as e:  # une exception au milieu du banc est un échec, pas une panne silencieuse
        if ok + ko == 0:
            panne(f"aucun test n'a pu s'exécuter : {str(e)[:300]}")
        t(False, f"le banc s'est arrêté sur une exception : {str(e)[:300]}")
    if ok + ko == 0:
        panne("aucun test exécuté")
    print(f"\n══ 3e_C1.5, séances : {ok} / {ok + ko} tests réussis — 1 page lue ({PAGE.name}) ══")
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
