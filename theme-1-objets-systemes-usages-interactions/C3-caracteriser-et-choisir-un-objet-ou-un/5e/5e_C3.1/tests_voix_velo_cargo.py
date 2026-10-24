#!/usr/bin/env python3
"""Suite de tests de la voix du dessin animé du vélo-cargo (5e_C3.1) — fichiers audio, lecteur, secours.

    python3 tests_voix_velo_cargo.py

Ce qu'elle vérifie : les douze fichiers existent et ont la bonne forme ; les phrases dites sont celles de la séquence ;
rien ne se charge ni ne se joue sans geste, rien ne vient du réseau ; « Écouter » joue le fichier de la scène ;
« Regarder » enchaîne à la fin de l'audio ; le MP3 sert quand l'Opus n'est pas lu ; la voix locale prend le relais quand
un fichier ne se lit pas ; zéro erreur JavaScript.
Ce qu'elle NE vérifie PAS : que la voix soit belle, ni qu'elle dise bien la phrase (cela s'écoute) ; ni la lecture sous
Safari ou sur tablette (seul Chromium tourne ici).
"""
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
URL = (ICI / "sequence_5e_C3.1-C3.4_shanghai.html").as_uri() + "#velo-cargo-pas-a-pas"
res = []


def t(nom, ok, detail=""):
    res.append((nom, bool(ok)))
    print(("✔" if ok else "✘"), nom, detail)


# 1 · les fichiers
for n in range(1, 7):
    ogg = ICI / "Audio" / ("velo-cargo_scene%d.ogg" % n)
    mp3 = ICI / "Audio" / ("velo-cargo_scene%d.mp3" % n)
    ok = ogg.exists() and mp3.exists() and ogg.read_bytes()[:4] == b"OggS" and mp3.stat().st_size > 5000
    t("scène %d : .ogg (Opus) et .mp3 présents, de bonne forme" % n, ok)
    t("scène %d : moins de 100 Ko chacun" % n, ogg.stat().st_size < 100_000 and mp3.stat().st_size < 100_000)

# 2 · les phrases dites sont celles de la séquence
r = subprocess.run([sys.executable, str(ICI / "_generation" / "voix_velo_cargo" / "generer.py"), "--verifier"],
                   capture_output=True, text=True, encoding="utf-8")
t("phrases.json = tableau SCENES de la séquence, mot pour mot", r.returncode == 0, (r.stdout + r.stderr).strip()[-200:])

# les crochets posés avant le chargement : ce que la page joue, ce que la voix locale dit
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

with sync_playwright() as p:
    b = p.chromium.launch()

    def ouvrir(script_init="", largeur=1280):
        ctx = b.new_context(viewport={"width": largeur, "height": 1000})
        pg = ctx.new_page()
        erreurs, demandes = [], []
        pg.on("pageerror", lambda e: erreurs.append(str(e)))
        pg.on("request", lambda rq: demandes.append(rq.url))
        pg.add_init_script(ESPION % JOUER_VRAI + script_init if script_init is not None else "")
        pg.goto(URL)
        pg.wait_for_selector("#vppPanneau:not([hidden])", timeout=8000)
        pg.wait_for_timeout(500)
        return ctx, pg, erreurs, demandes

    # 3 · rien ne se charge ni ne se joue sans geste
    ctx, pg, erreurs, demandes = ouvrir()
    t("à l'ouverture du dessin animé : aucun fichier audio demandé ni joué",
      not [u for u in demandes if "/Audio/" in u] and pg.evaluate("window.__sons.length") == 0)
    t("« Écouter » est proposé (les fichiers suffisent, pas besoin de voix du système)", pg.is_visible("#vppEcouter"))
    # 4 · « Écouter » joue le fichier de la scène
    pg.click("#vppSuiv")
    pg.wait_for_timeout(300)
    pg.click("#vppEcouter")
    pg.wait_for_timeout(600)
    sons = pg.evaluate("window.__sons")
    t("« Écouter » à la scène 2 joue velo-cargo_scene2.ogg", sons and sons[-1].endswith("/Audio/velo-cargo_scene2.ogg"), str(sons))
    # 5 · « Regarder » : le premier fichier, puis la scène suivante à la fin de l'audio
    pg.click("#vppZero")
    pg.wait_for_timeout(300)
    pg.click("#vppRegarder")
    pg.wait_for_timeout(700)
    sons = pg.evaluate("window.__sons")
    t("« Regarder » joue d'abord velo-cargo_scene1.ogg", sons[-1].endswith("/Audio/velo-cargo_scene1.ogg"), str(sons[-2:]))
    pg.wait_for_function("document.getElementById('velo-cargo-pas-a-pas').getAttribute('data-scene') === '2'", timeout=15000)
    pg.wait_for_timeout(500)
    sons = pg.evaluate("window.__sons")
    t("à la fin de l'audio, « Regarder » passe à la scène 2 et joue son fichier", sons[-1].endswith("/Audio/velo-cargo_scene2.ogg"), str(sons[-2:]))
    pg.click("#vppRegarder")   # pause
    n_avant = pg.evaluate("window.__sons.length")
    pg.wait_for_timeout(5500)
    t("« Pause » arrête l'enchaînement : aucune scène ne démarre ensuite", pg.evaluate("window.__sons.length") == n_avant)
    t("aucune ressource distante, aucune erreur JavaScript",
      not [u for u in demandes if u.startswith(("http://", "https://"))] and not erreurs, str(erreurs))
    ctx.close()

    # 6 · l'Opus n'est pas lu : le MP3 de secours
    ctx, pg, erreurs, _ = ouvrir(SANS_OPUS)
    pg.click("#vppEcouter")
    pg.wait_for_timeout(500)
    sons = pg.evaluate("window.__sons")
    t("sans Opus, « Écouter » joue le MP3", sons and sons[-1].endswith("/Audio/velo-cargo_scene1.mp3"), str(sons))
    ctx.close()

    # 7 · un fichier ne se lit pas : la voix locale prend le relais, sans erreur
    ctx = b.new_context(viewport={"width": 1280, "height": 1000})
    pg = ctx.new_page()
    erreurs = []
    pg.on("pageerror", lambda e: erreurs.append(str(e)))
    pg.add_init_script(ESPION % JOUER_REFUSE + SYNTHESE_FAUSSE)
    pg.goto(URL)
    pg.wait_for_selector("#vppPanneau:not([hidden])", timeout=8000)
    pg.click("#vppEcouter")
    pg.wait_for_timeout(800)
    dits = pg.evaluate("window.__dits")
    t("fichier refusé : la voix locale dit la phrase de la scène 1", dits and dits[0].startswith("Ce vélo-cargo doit livrer un colis."), str(dits))
    t("… sans erreur JavaScript", not erreurs, str(erreurs))
    ctx.close()

    # 8 · ni fichier lisible ni voix locale : le message « lis les phrases » remplace le bouton
    ctx = b.new_context(viewport={"width": 1280, "height": 1000})
    pg = ctx.new_page()
    pg.add_init_script(ESPION % JOUER_REFUSE + SYNTHESE_SANS_VOIX)
    pg.goto(URL)
    pg.wait_for_selector("#vppPanneau:not([hidden])", timeout=8000)
    pg.click("#vppEcouter")
    pg.wait_for_timeout(600)
    t("ni fichier ni voix : « Écouter » disparaît et le message « lis les phrases » s'affiche",
      pg.is_hidden("#vppEcouter") and pg.is_visible("#vppSansVoix"))
    ctx.close()
    b.close()

ok = sum(1 for _, v in res if v)
print("\n%d / %d tests passés" % (ok, len(res)))
sys.exit(0 if ok == len(res) else 1)
