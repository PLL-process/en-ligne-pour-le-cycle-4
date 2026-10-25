#!/usr/bin/env python3
"""Banc de l'animation des trois principes (5e_C1.1, activité 1, bloc #trois-principes-pas-a-pas) — dessin, voix, finale.

    python3 tests_animation_trois_principes.py

Ce qu'il vérifie : les vingt-deux fichiers audio existent et ont la bonne forme ; les phrases dites sont celles de la page ;
à l'écran l'animation remplace les trois schémas, à l'impression c'est l'inverse ; les onze étapes, les chapitres, les
boutons ; rien ne se charge ni ne se joue sans geste, rien ne vient du réseau ; « Écouter », « Regarder », « Pause » ; le MP3
de secours, la voix locale, le message « lis les phrases » ; le compteur d'éclats et la lentille sale ; l'horloge de la
pesée ; les résultats de la finale (moyennes sur 1 h et 24 h, calculées à la main ci-dessous) ; le mouvement réduit ;
aucun débordement à 390 px ; le lien direct ; zéro erreur JavaScript.
Ce qu'il NE vérifie PAS : que la voix soit belle ni qu'elle dise bien la phrase (cela s'écoute) ; que l'animation soit
claire pour un élève (cela se voit en classe) ; la lecture sous Safari ou sur tablette (seul Chromium tourne ici).
"""
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
PAGE = (ICI / "sequence_5e_C1.1-C1.6_chengdu_air.html").as_uri()
res = []


def t(nom, ok, detail=""):
    res.append((nom, bool(ok)))
    print(("✔" if ok else "✘"), nom, detail if not ok else "")


# 1 · les fichiers
for n in range(1, 12):
    ogg = ICI / "Audio" / ("trois-principes_scene%d.ogg" % n)
    mp3 = ICI / "Audio" / ("trois-principes_scene%d.mp3" % n)
    ok = ogg.exists() and mp3.exists() and ogg.read_bytes()[:4] == b"OggS" and mp3.stat().st_size > 5000
    t("étape %d : .ogg (Opus) et .mp3 présents, de bonne forme, moins de 100 Ko" % n,
      ok and ogg.stat().st_size < 100_000 and mp3.stat().st_size < 100_000)

# 2 · les phrases dites sont celles de la page
r = subprocess.run([sys.executable, str(ICI / "_generation" / "voix_trois_principes" / "generer.py"), "--verifier"],
                   capture_output=True, text=True, encoding="utf-8")
t("phrases.json = tableau SCENES de la page, mot pour mot", r.returncode == 0, (r.stdout + r.stderr).strip()[-200:])

ESPION = """
window.__sons = []; window.__dits = [];
const jouer = HTMLMediaElement.prototype.play;
HTMLMediaElement.prototype.play = function(){ window.__sons.push(this.src); %s };
"""
JOUER_VRAI = "return jouer.apply(this, arguments);"
JOUER_REFUSE = "return Promise.reject(new Error('lecture refusée'));"
SYNTHESE_FAUSSE = """
window.SpeechSynthesisUtterance = function(texte){ this.text = texte; };
Object.defineProperty(window, 'speechSynthesis', { configurable: true, value: {
  getVoices(){ return [{lang: 'fr-FR', localService: true, name: 'fausse voix'}]; },
  addEventListener(){}, cancel(){},
  speak(u){ window.__dits.push(u.text); setTimeout(function(){ if (u.onend) u.onend(); }, 20); }
}});
"""
SYNTHESE_SANS_VOIX = """
Object.defineProperty(window, 'speechSynthesis', { configurable: true, value: {
  getVoices(){ return []; }, addEventListener(){}, cancel(){}, speak(){} }});
"""
SANS_OPUS = """
const cp = HTMLMediaElement.prototype.canPlayType;
HTMLMediaElement.prototype.canPlayType = function(type){ return /opus|ogg/i.test(type) ? '' : cp.call(this, type); };
"""
ALLER = "n => { document.getElementById('tpaZero').click(); for (let i = 1; i < n; i++) document.getElementById('tpaSuiv').click(); }"
TEXTE = "id => document.getElementById(id).textContent.trim()"

with sync_playwright() as p:
    b = p.chromium.launch()

    def ouvrir(script_init="", largeur=1280, calme=False, ancre="#trois-principes-pas-a-pas"):
        ctx = b.new_context(viewport={"width": largeur, "height": 900}, reduced_motion="reduce" if calme else "no-preference")
        pg = ctx.new_page()
        erreurs, demandes = [], []
        pg.on("pageerror", lambda e: erreurs.append(str(e)))
        pg.on("console", lambda m: erreurs.append("console:" + m.text) if m.type == "error" else None)
        pg.on("request", lambda rq: demandes.append(rq.url))
        pg.add_init_script(ESPION % JOUER_VRAI + script_init)
        pg.goto(PAGE + ancre)
        pg.wait_for_timeout(700)
        return ctx, pg, erreurs, demandes

    # 3 · à l'écran, l'animation remplace les schémas ; à l'impression, l'inverse
    ctx, pg, erreurs, demandes = ouvrir()
    t("l'animation est affichée à l'écran", pg.is_visible("#trois-principes-pas-a-pas"))
    schemas = pg.evaluate("[...document.querySelectorAll('#planche3 .schema3, #planche3 .p3reperer')].map(e => getComputedStyle(e).display)")
    t("les trois schémas fixes et leurs « À repérer » sont masqués à l'écran", len(schemas) == 6 and set(schemas) == {"none"}, str(schemas))
    t("les étapes ①②③ des cartes restent à l'écran", pg.evaluate("[...document.querySelectorAll('#planche3 .p3etapes')].every(e => e.offsetHeight > 0)"))
    pg.emulate_media(media="print")
    t("à l'impression : l'animation disparaît, les trois schémas reviennent",
      pg.evaluate("getComputedStyle(document.getElementById('trois-principes-pas-a-pas')).display") == "none" and
      pg.evaluate("[...document.querySelectorAll('#planche3 .schema3')].every(s => getComputedStyle(s).display !== 'none')"))
    pg.emulate_media(media="screen")
    # 4 · rien ne se charge ni ne se joue sans geste
    t("à l'ouverture : aucun fichier audio demandé ni joué",
      not [u for u in demandes if "/Audio/" in u] and pg.evaluate("window.__sons.length") == 0)
    t("« Écouter » est proposé (les fichiers suffisent)", pg.is_visible("#tpaEcouter"))
    # 5 · les onze étapes et les chapitres
    t("étape 1 : « Précédent » désactivé, compteur 1 / 11",
      pg.is_disabled("#tpaPrec") and pg.evaluate(TEXTE, "tpaCompte") == "Étape 1 / 11")
    phrases = pg.evaluate("""() => { const out = [], s = document.getElementById('tpaSuiv');
        document.getElementById('tpaZero').click();
        for (let i = 1; i <= 11; i++) { out.push([document.getElementById('tpaTexte').textContent.trim(),
            document.getElementById('tpaDessin').getAttribute('aria-label') || '']); if (i < 11) s.click(); } return out; }""")
    t("onze étapes, chacune avec sa phrase", len(phrases) == 11 and all(len(x[0]) > 20 for x in phrases))
    t("étapes 1 à 10 : le dessin a une description pour les lecteurs d'écran", all(len(x[1]) > 40 for x in phrases[:10]))
    t("étape 11 : « Suivant » désactivé, finale affichée, dessin masqué",
      pg.is_disabled("#tpaSuiv") and pg.is_visible("#tpaFinal") and not pg.is_visible("#tpaDessin"))
    chap = {}
    for debut in (1, 2, 5, 8, 11):
        pg.click("[data-aller='%d']" % debut)
        chap[debut] = (pg.evaluate("document.getElementById('trois-principes-pas-a-pas').getAttribute('data-scene')"),
                       pg.evaluate("document.querySelector('[data-aller=\"%d\"]').getAttribute('aria-current')" % debut))
    t("les cinq chapitres mènent à leur étape et se marquent", all(v == (str(k), "step") for k, v in chap.items()), str(chap))
    # 6 · la voix
    pg.evaluate(ALLER, 2)
    pg.click("#tpaEcouter")
    pg.wait_for_timeout(500)
    sons = pg.evaluate("window.__sons")
    t("« Écouter » à l'étape 2 joue trois-principes_scene2.ogg", sons and sons[-1].endswith("/Audio/trois-principes_scene2.ogg"), str(sons))
    pg.click("#tpaZero")
    pg.click("#tpaRegarder")
    pg.wait_for_timeout(600)
    sons = pg.evaluate("window.__sons")
    t("« Regarder » joue d'abord trois-principes_scene1.ogg", sons[-1].endswith("/Audio/trois-principes_scene1.ogg"), str(sons[-2:]))
    pg.wait_for_function("document.getElementById('trois-principes-pas-a-pas').getAttribute('data-scene') === '2'", timeout=20000)
    pg.wait_for_timeout(400)
    sons = pg.evaluate("window.__sons")
    t("à la fin de l'audio, « Regarder » passe à l'étape 2 et joue son fichier", sons[-1].endswith("/Audio/trois-principes_scene2.ogg"), str(sons[-2:]))
    pg.click("#tpaRegarder")
    n_avant = pg.evaluate("window.__sons.length")
    pg.wait_for_timeout(6500)
    t("« Pause » arrête l'enchaînement", pg.evaluate("window.__sons.length") == n_avant)
    # 7 · P1 : le capteur compte ; la lentille sale ajoute des éclats ; le bouton n'existe qu'à l'étape 4
    pg.evaluate(ALLER, 3)
    t("étape 3 : pas de bouton « lentille »", pg.is_hidden("#tpaLentille"))
    pg.evaluate(ALLER, 4)
    pg.locator("#tpaDessin").scroll_into_view_if_needed()
    c0 = int(pg.evaluate(TEXTE, "tpaP1Compte"))
    pg.wait_for_timeout(4000)
    c1 = int(pg.evaluate(TEXTE, "tpaP1Compte"))
    t("étape 4 : le compteur d'éclats monte (%d → %d en 4 s)" % (c0, c1), c1 >= c0 + 3)
    pg.click("#tpaLentille")
    c2 = int(pg.evaluate(TEXTE, "tpaP1Compte"))
    pg.wait_for_timeout(4000)
    c3 = int(pg.evaluate(TEXTE, "tpaP1Compte"))
    t("lentille sale : le compteur monte plus vite (%d en 4 s contre %d), la note s'affiche" % (c3 - c2, c1 - c0),
      c3 - c2 > c1 - c0 and pg.is_visible("#tpaNoteSale") and pg.get_attribute("#tpaLentille", "aria-pressed") == "true")
    # 8 · P2 : l'horloge va de 0 à 24 h et s'arrête
    pg.evaluate(ALLER, 5)
    h0 = pg.evaluate(TEXTE, "tpaP2Heures")
    pg.wait_for_timeout(9000)
    t("étape 5 : l'horloge part de 0 h et s'arrête à 24 h", h0 == "0 h" and pg.evaluate(TEXTE, "tpaP2Heures") == "24 h",
      h0 + " → " + pg.evaluate(TEXTE, "tpaP2Heures"))
    pg.evaluate(ALLER, 6)
    pg.wait_for_timeout(3000)
    t("étape 6 : la balance « après » affiche 100 020 µg", pg.evaluate(TEXTE, "tpaP2Apres").replace(" ", " ").replace(" ", " ") == "100 020 µg")
    # 9 · P3 : la jauge tombe quand le dépôt s'épaissit
    pg.evaluate(ALLER, 10)
    m0 = pg.evaluate(TEXTE, "tpaP3Mot")
    pg.wait_for_timeout(6500)
    t("étape 10 : « il en passe beaucoup », puis « il en passe peu »", m0 == "il en passe beaucoup" and pg.evaluate(TEXTE, "tpaP3Mot") == "il en passe peu")
    # 10 · la finale : P1 tout de suite, P3 à l'heure, P2 à la journée (moyennes calculées à la main)
    pg.evaluate(ALLER, 11)
    pg.wait_for_timeout(300)
    t("étape 11 : l'horloge tourne seule", pg.evaluate(TEXTE, "tpaHorlogeBtn") == "⏸ Pause")
    pg.click("#tpaHorlogeBtn")                           # pause
    pg.click("#tpaHorlogeZero")
    t("remise à 0 h : P2 et P3 sans résultat", pg.evaluate(TEXTE, "tpaR2") == "—" and pg.evaluate(TEXTE, "tpaR3") == "—")

    def regler(v):
        pg.evaluate("v => { const c = document.getElementById('tpaCurseur'); c.value = v; c.dispatchEvent(new Event('input', {bubbles: true})); }", v)

    def heures(n):
        for _ in range(n):
            pg.click("#tpaPlusHeure")

    regler(40)
    t("curseur à 40 : P1 donne 40 µg/m³ tout de suite, P3 attend", pg.evaluate(TEXTE, "tpaR1") == "40 µg/m³" and pg.evaluate(TEXTE, "tpaR3") == "—")
    heures(1)
    t("après 1 h : P3 = 40 µg/m³, P2 attend encore", pg.evaluate(TEXTE, "tpaR3") == "40 µg/m³" and pg.evaluate(TEXTE, "tpaR2") == "—")
    regler(20); heures(11); regler(60); heures(12)
    # P2 = (40×1 + 20×11 + 60×12) / 24 = (40 + 220 + 720) / 24 = 980 / 24 = 40,8 → 41 ; P3 = 60
    t("après 24 h (40 pendant 1 h, 20 pendant 11 h, 60 pendant 12 h) : P2 = 41 µg/m³, P3 = 60 µg/m³",
      pg.evaluate(TEXTE, "tpaR2") == "41 µg/m³" and pg.evaluate(TEXTE, "tpaR3") == "60 µg/m³",
      pg.evaluate(TEXTE, "tpaR2") + " / " + pg.evaluate(TEXTE, "tpaR3"))
    t("l'horloge affiche « Jour 2 · 00 h »", pg.evaluate(TEXTE, "tpaHeure") == "Jour 2 · 00 h", pg.evaluate(TEXTE, "tpaHeure"))
    regler(80); heures(1)
    t("curseur à 80, 1 h plus tard : P3 = 80, P2 garde la moyenne de la veille (41)",
      pg.evaluate(TEXTE, "tpaR3") == "80 µg/m³" and pg.evaluate(TEXTE, "tpaR2") == "41 µg/m³")
    t("aucune ressource distante, aucune erreur JavaScript",
      not [u for u in demandes if u.startswith(("http://", "https://"))] and not erreurs, str(erreurs)[:300])
    ctx.close()

    # 11 · mouvement réduit : rien ne bouge seul
    ctx, pg, erreurs, _ = ouvrir(calme=True)
    pg.evaluate(ALLER, 3)
    a = pg.evaluate("[...document.querySelectorAll('#tpaP1Grains circle')].map(c => c.getAttribute('cy') + c.getAttribute('opacity')).join()")
    pg.wait_for_timeout(1200)
    b2 = pg.evaluate("[...document.querySelectorAll('#tpaP1Grains circle')].map(c => c.getAttribute('cy') + c.getAttribute('opacity')).join()")
    t("mouvement réduit : les grains restent immobiles, un éclat est montré",
      a == b2 and pg.evaluate("[...document.querySelectorAll('#tpaP1Eclats > g')].some(g => +g.getAttribute('opacity') > 0)"), a + " / " + b2)
    pg.evaluate(ALLER, 11)
    h1 = pg.evaluate(TEXTE, "tpaHeure")
    pg.wait_for_timeout(1500)
    t("mouvement réduit : l'horloge de la finale attend un geste", pg.evaluate(TEXTE, "tpaHeure") == h1 and
      pg.evaluate(TEXTE, "tpaHorlogeBtn").startswith("▶"))
    t("… sans erreur JavaScript", not erreurs, str(erreurs))
    ctx.close()

    # 12 · 390 px : rien ne déborde, à aucune étape
    ctx, pg, erreurs, _ = ouvrir(largeur=390)
    larges = []
    for n in range(1, 12):
        pg.evaluate(ALLER, n)
        pg.wait_for_timeout(150)
        if pg.evaluate("document.documentElement.scrollWidth") > 390:
            larges.append(n)
    t("390 px : aucune étape ne fait défiler la page en largeur", not larges, str(larges))
    ctx.close()

    # 13 · le lien direct ouvre la séance 1 et montre l'animation, même si une autre séance était ouverte
    ctx, pg, erreurs, _ = ouvrir(ancre="")
    pg.click("#tab-s3")
    pg.evaluate("location.hash = '#trois-principes-pas-a-pas'")
    pg.wait_for_timeout(900)
    t("#trois-principes-pas-a-pas ouvre la séance 1 et amène l'animation à l'écran",
      pg.evaluate("document.getElementById('tab-s1').classList.contains('active')") and
      pg.evaluate("(() => { const r = document.getElementById('trois-principes-pas-a-pas').getBoundingClientRect(); return r.top < 300 && r.bottom > 0; })()"))
    ctx.close()

    # 14 · l'Opus n'est pas lu : le MP3 de secours
    ctx, pg, erreurs, _ = ouvrir(SANS_OPUS)
    pg.click("#tpaEcouter")
    pg.wait_for_timeout(500)
    sons = pg.evaluate("window.__sons")
    t("sans Opus, « Écouter » joue le MP3", sons and sons[-1].endswith("/Audio/trois-principes_scene1.mp3"), str(sons))
    ctx.close()

    # 15 · un fichier ne se lit pas : la voix locale prend le relais
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    erreurs = []
    pg.on("pageerror", lambda e: erreurs.append(str(e)))
    pg.add_init_script(ESPION % JOUER_REFUSE + SYNTHESE_FAUSSE)
    pg.goto(PAGE + "#trois-principes-pas-a-pas")
    pg.wait_for_timeout(600)
    pg.click("#tpaEcouter")
    pg.wait_for_timeout(800)
    dits = pg.evaluate("window.__dits")
    t("fichier refusé : la voix locale dit la phrase de l'étape 1", dits and dits[0].startswith("Une seule fonction"), str(dits))
    t("… sans erreur JavaScript", not erreurs, str(erreurs))
    ctx.close()

    # 16 · ni fichier lisible ni voix locale : le message « lis les phrases »
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    pg.add_init_script(ESPION % JOUER_REFUSE + SYNTHESE_SANS_VOIX)
    pg.goto(PAGE + "#trois-principes-pas-a-pas")
    pg.wait_for_timeout(600)
    pg.click("#tpaEcouter")
    pg.wait_for_timeout(600)
    t("ni fichier ni voix : « Écouter » disparaît, le message « lis les phrases » s'affiche",
      pg.is_hidden("#tpaEcouter") and pg.is_visible("#tpaSansVoix"))
    ctx.close()
    b.close()

ok = sum(1 for _, v in res if v)
print("\n%d / %d tests passés" % (ok, len(res)))
sys.exit(0 if ok == len(res) else 1)
