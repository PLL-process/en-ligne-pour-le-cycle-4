#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Banc des trois freins en 3D (5e_C1.2, activité 1, bloc #freins-3d) — films, affiches, page, impression.

    python3 tests_trois_freins_3d.py

Ce qu'il vérifie : les douze fichiers (trois films en .mp4 et .webm, trois affiches, trois images d'impression), leur
forme et leur poids ; que chaque film fait 4,5 s, 960 × 676, 24 images/s, sans son ; que sa dernière image est son
affiche (règle d'or n°176) ; les scripts de fabrication ; dans la page : le bloc posé après les trois vidéos et avant la
manipulation, les blocs « ressource » intacts, le lecteur (muet, sans boucle, sans lecture automatique,
`preload="none"`), les adresses écrites en entier, la légende aux mêmes numéros que les pastilles ; dans Chromium : rien
de demandé ni joué à l'ouverture, le choix du frein, un film joué une fois jusqu'à son image complète, aucun débordement
à 390 px, le mode mission, le « mouvement réduit », aucune ressource distante, zéro erreur JavaScript ; à l'impression :
la bande des trois images sur fond clair, et la séance 1 toujours sur cinq pages A4.
Ce qu'il NE vérifie PAS : que les films soient justes et clairs pour un élève (cela se regarde, en classe) ; leur lecture
sur les postes du collège, sous Safari ou sur tablette (seul Chromium tourne ici) ; l'impression hors Chromium.
Codes de sortie : 0 tout passe, 1 un contrôle échoue, 2 un outil manque (ffmpeg, ffprobe, Pillow, Playwright).
"""
import ast
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
GEN = ICI / "_generation" / "films_trois_freins"
ATELIER = DEPOT / "_ressources-communes" / "blender-atelier" / "atelier.py"
PAGE = ICI / "sequence_5e_C1.2_sainte_luce_freinage.html"
FREINS = ("patins", "disque", "tambour")
MOTS = {"patins": ("levier", "câble", "bras", "patins", "jante"),
        "disque": ("levier", "durite", "étrier", "plaquettes", "disque"),
        "tambour": ("levier", "câble", "came", "mâchoires", "tambour")}
res = []

try:
    from PIL import Image, ImageChops, ImageStat
    from playwright.sync_api import sync_playwright
except ImportError as e:
    print("outil manquant :", e)
    sys.exit(2)
if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
    print("outil manquant : ffmpeg et ffprobe")
    sys.exit(2)


def t(nom, ok, detail=""):
    res.append((nom, bool(ok)))
    print(("✔" if ok else "✘"), nom, "" if ok else detail)


def sonder(chemin):
    r = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-show_entries",
                        "stream=codec_type,codec_name,width,height,pix_fmt,r_frame_rate,nb_read_frames", "-of", "json",
                        str(chemin)], capture_output=True, text=True)
    return json.loads(r.stdout or "{}").get("streams", [])


# 1 · les fichiers : forme, poids, format
for f in FREINS:
    mp4, webm = ICI / "Films" / ("trois-freins_%s.mp4" % f), ICI / "Films" / ("trois-freins_%s.webm" % f)
    jpg, clair = ICI / "Images" / ("trois-freins_%s_3d.jpg" % f), ICI / "Images" / ("trois-freins_%s_3d_impression.jpg" % f)
    presents = all(p.exists() for p in (mp4, webm, jpg, clair))
    t("%s : .mp4, .webm, affiche et image d'impression présents, de bonne forme" % f,
      presents and mp4.read_bytes()[4:8] == b"ftyp" and webm.read_bytes()[:4] == b"\x1a\x45\xdf\xa3"
      and jpg.read_bytes()[:2] == b"\xff\xd8" and clair.read_bytes()[:2] == b"\xff\xd8")
    if not presents:
        continue
    t("%s : moins de 600 Ko par film, 100 Ko par affiche, 60 Ko par image d'impression" % f,
      mp4.stat().st_size < 600_000 and webm.stat().st_size < 600_000 and jpg.stat().st_size < 100_000
      and clair.stat().st_size < 60_000, "%d %d %d %d" % tuple(p.stat().st_size for p in (mp4, webm, jpg, clair)))
    for chemin, codec in ((mp4, "h264"), (webm, "vp9")):
        flux = sonder(chemin)
        v = [s for s in flux if s.get("codec_type") == "video"]
        ok = (len(flux) == 1 and v and v[0]["codec_name"] == codec and (v[0]["width"], v[0]["height"]) == (960, 676)
              and v[0]["pix_fmt"] == "yuv420p" and v[0]["r_frame_rate"] == "24/1" and v[0].get("nb_read_frames") == "108")
        t("%s %s : %s, 960 × 676, 24 images/s, 108 images (4,5 s), sans son" % (f, chemin.suffix, codec), ok, str(flux))
    with tempfile.TemporaryDirectory() as tmp:
        fin = pathlib.Path(tmp) / "fin.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp4), "-vf", "select=eq(n\\,107)", "-frames:v", "1",
                        str(fin)], check=False)
        ecart = 255.0
        if fin.exists():
            a, b = Image.open(fin).convert("RGB"), Image.open(jpg).convert("RGB")
            ecart = sum(ImageStat.Stat(ImageChops.difference(a, b)).mean) / 3 if a.size == b.size else 255.0
        t("%s : la dernière image du film est son affiche (n°176)" % f, ecart < 4.0, "écart moyen %.1f" % ecart)
    t("%s : l'image d'impression fait 720 × 507, sur fond clair" % f,
      Image.open(clair).size == (720, 507) and sum(Image.open(clair).convert("RGB").getpixel((8, 8))) > 600)

# 2 · les scripts de fabrication
for p in (GEN / "generer.py", GEN / "habiller.py", ATELIER):
    try:
        ast.parse(p.read_text(encoding="utf-8"))
        ok = True
    except (OSError, SyntaxError):
        ok = False
    t("script %s présent et lisible par Python" % p.name, ok)
t("assembler.sh présent, il encode les douze fichiers de la page",
  (GEN / "assembler.sh").exists() and all(m in (GEN / "assembler.sh").read_text(encoding="utf-8")
                                          for m in ("libx264", "libvpx-vp9", "_3d.jpg", "_3d_impression.jpg")))
r = subprocess.run([sys.executable, str(GEN / "habiller.py")], capture_output=True, text=True)
t("habiller.py sans argument : sa notice et le code 2", r.returncode == 2 and "habiller.py" in r.stdout)
_spec = importlib.util.spec_from_file_location("habiller", GEN / "habiller.py")
habiller = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(habiller)
plan = habiller.PLAN
t("habiller.py : cinq pastilles par frein, numérotées de 1 à 5",
  all(sorted(p[0] for p in plan[f]["pastilles"]) == [1, 2, 3, 4, 5] for f in FREINS))

# 3 · la page, lue comme un texte
html = PAGE.read_text(encoding="utf-8")
debut = html.find('<section class="f3d" id="freins-3d"')
fin_bloc = html.find("</section>", debut)
bloc = html[debut:fin_bloc]
t("un seul bloc #freins-3d", html.count('id="freins-3d"') == 1 and debut > 0)
t("posé après les trois vidéos et avant « a) La manipulation »",
  html.find("<!-- /ressource: res-5e-C1-2-tambour -->") < debut < html.find("a) La manipulation", debut) and
  html.find("a) La manipulation") > debut)
t("les trois blocs « ressource » sont intacts (une ouverture, une fermeture chacun)",
  all(html.count("<!-- ressource: res-5e-C1-2-%s -->" % k) == 1 and html.count("<!-- /ressource: res-5e-C1-2-%s -->" % k) == 1
      for k in ("jante", "disque", "tambour")),
  "marqueurs")
video = re.search(r"<video[^>]*>", bloc)
v = video.group(0) if video else ""
t("le lecteur : muet, playsinline, preload=\"none\", une affiche ; ni autoplay ni loop",
  all(m in v for m in (" muted", " playsinline", 'preload="none"', 'poster="Images/trois-freins_patins_3d.jpg"'))
  and "autoplay" not in bloc and " loop" not in bloc, v)
t("deux sources : .mp4 puis .webm", re.search(r'<source src="Films/trois-freins_patins\.mp4" type="video/mp4">\s*'
                                             r'<source src="Films/trois-freins_patins\.webm" type="video/webm">', bloc))
adresses = set(re.findall(r'"((?:Films|Images)/trois-freins_[a-z_0-9]+\.(?:mp4|webm|jpg))"', bloc))
attendues = {"Films/trois-freins_%s.%s" % (f, x) for f in FREINS for x in ("mp4", "webm")} | \
            {"Images/trois-freins_%s_3d%s.jpg" % (f, s) for f in FREINS for s in ("", "_impression")}
t("les douze adresses écrites en entier dans le bloc, et chacune existe",
  adresses == attendues and all((ICI / a).exists() for a in adresses), str(sorted(attendues - adresses)))
papier = re.findall(r'<div><img src="Images/trois-freins_(\w+)_3d_impression\.jpg"[^>]*alt="([^"]+)"[^>]*><p>.*?</p>'
                    r'<ol class="f3d-mini">(.*?)</ol></div>', bloc)
t("à l'impression : trois images décrites (alt), légendées par une liste de cinq numéros, aux mots des pastilles",
  [p[0] for p in papier] == list(FREINS) and all(len(p[1]) > 60 and p[2].count("<li>") == 5
                                                and all(m in p[2] for m in MOTS[p[0]]) for p in papier))

# 4 · dans Chromium
DEMANDES, ERREURS = [], []
ETAT = """() => { const v = document.getElementById('f3dFilm');
  const b = [...document.querySelectorAll('#freins-3d .f3d-choix button')];
  return { enPause: v.paused, temps: v.currentTime, fini: v.ended, boucle: v.loop, affiche: v.getAttribute('poster'),
    source: [...v.querySelectorAll('source')].map(s => s.getAttribute('src')), etiquette: v.getAttribute('aria-label'),
    choisi: b.filter(x => x.getAttribute('aria-pressed') === 'true').map(x => x.dataset.frein),
    legende: [...document.querySelectorAll('#f3dListe li')].map(l => l.textContent),
    nom: document.getElementById('f3dNom').textContent, coupe: document.getElementById('f3dCoupe').textContent,
    bouton: document.getElementById('f3dJouer').textContent,
    hauts: b.map(x => Math.round(x.getBoundingClientRect().top)), tailles: b.map(x => Math.round(x.getBoundingClientRect().height)),
    deborde: document.documentElement.scrollWidth - document.documentElement.clientWidth } }"""


def ouvrir(b, largeur=390, calme=False, ecrit=True):
    ctx = b.new_context(viewport={"width": largeur, "height": 844}, reduced_motion="reduce" if calme else "no-preference")
    pg = ctx.new_page()
    demandes, erreurs = [], []
    pg.on("request", lambda r: demandes.append(r.url))
    pg.on("pageerror", lambda e: erreurs.append(str(e)))
    pg.goto(PAGE.as_uri())
    pg.wait_for_timeout(900)
    return ctx, pg, demandes, erreurs


def films(demandes):
    return [u.rsplit("/", 1)[-1] for u in demandes if "/Films/" in u]


with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, demandes, erreurs = ouvrir(b)
    e = pg.evaluate(ETAT)
    t("à l'ouverture : aucun film demandé, rien ne joue", not films(demandes) and e["enPause"] and e["temps"] == 0, str(films(demandes)))
    t("à l'ouverture : frein à patins choisi, son affiche, sa légende (5 numéros)",
      e["choisi"] == ["patins"] and e["affiche"].endswith("patins_3d.jpg") and len(e["legende"]) == 5
      and all(m in " ".join(e["legende"]) for m in MOTS["patins"]), str(e))
    t("à 390 px : les trois boutons sur une ligne, 44 px de haut au moins ; aucun débordement",
      len(set(e["hauts"])) == 1 and min(e["tailles"]) >= 44 and e["deborde"] <= 0, str(e["hauts"]) + str(e["tailles"]))
    pg.click('#freins-3d button[data-frein="disque"]')
    pg.wait_for_timeout(400)
    e = pg.evaluate(ETAT)
    t("« à disque » : bouton enfoncé, affiche, sources, description, légende et coupe du disque",
      e["choisi"] == ["disque"] and e["affiche"].endswith("disque_3d.jpg") and e["source"][0].endswith("disque.mp4")
      and "frein à disque" in e["etiquette"] and all(m in " ".join(e["legende"]) for m in MOTS["disque"])
      and "disque" in e["nom"].lower() and "étrier" in e["coupe"], str(e))
    t("changer de frein ne demande aucun film", not films(demandes), str(films(demandes)))
    pg.click("#f3dJouer")
    pg.wait_for_timeout(5600)
    e = pg.evaluate(ETAT)
    t("« Lancer le film » : il se joue une fois, sans boucle, et s'arrête sur sa dernière image (4,5 s)",
      e["fini"] and not e["boucle"] and abs(e["temps"] - 4.5) < 0.2 and e["bouton"].startswith("↻"), str(e))
    t("seul le film choisi est demandé (le .mp4)", set(films(demandes)) == {"trois-freins_disque.mp4"}, str(films(demandes)))
    pg.click("#f3dFilm")
    pg.wait_for_timeout(700)
    e = pg.evaluate(ETAT)
    t("un geste sur le film le relance depuis le début", not e["enPause"] and 0 < e["temps"] < 2, str(e))
    pg.click('#freins-3d button[data-frein="tambour"]')
    pg.wait_for_timeout(400)
    e = pg.evaluate(ETAT)
    t("« à tambour » : le film précédent s'arrête ; affiche, légende et coupe du tambour",
      e["enPause"] and e["affiche"].endswith("tambour_3d.jpg") and all(m in " ".join(e["legende"]) for m in MOTS["tambour"])
      and "tambour" in e["coupe"], str(e))
    t("à l'écran : la bande d'impression est cachée",
      pg.evaluate("getComputedStyle(document.querySelector('#freins-3d .f3d-papier')).display") == "none")
    t("aucune ressource distante, aucune erreur JavaScript",
      not [u for u in demandes if u.startswith(("http://", "https://"))] and not erreurs, str(erreurs)[:300])
    ctx.close()

    ctx, pg, demandes, erreurs = ouvrir(b, largeur=1280)
    e = pg.evaluate(ETAT)
    t("à 1 280 px : aucun débordement, rien ne joue", e["deborde"] <= 0 and e["enPause"] and not films(demandes))
    pg.emulate_media(media="print")
    pg.wait_for_timeout(400)
    imp = pg.evaluate("""() => { const z = document.querySelector('#freins-3d .f3d-papier');
      const cache = s => [...document.querySelectorAll(s)].every(x => getComputedStyle(x).display === 'none');
      return { grille: getComputedStyle(z).display, images: [...z.querySelectorAll('img')].map(i => [i.complete && i.naturalWidth, Math.round(i.getBoundingClientRect().width)]),
        caches: cache('#freins-3d .f3d-ecran') && cache('#freins-3d .f3d-choix') && cache('#freins-3d .f3d-outils') && cache('#freins-3d .f3d-legende') } }""")
    t("à l'impression : la bande des trois images (chargées, 50 mm de large au moins) ; film, boutons et légende cachés",
      imp["grille"] == "grid" and len(imp["images"]) == 3 and all(n == 720 and w >= 189 for n, w in imp["images"])
      and imp["caches"], str(imp))
    pdf = pg.pdf(format="A4")
    pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf))
    t("à l'impression : la séance 1 tient toujours sur cinq pages A4", 0 < pages <= 5, "%d pages" % pages)
    ctx.close()

    ctx, pg, demandes, erreurs = ouvrir(b, calme=True)
    e = pg.evaluate(ETAT)
    t("« mouvement réduit » : l'affiche (l'image complète) est montrée, aucun film ne part seul",
      e["affiche"].endswith("patins_3d.jpg") and e["enPause"] and not films(demandes) and not erreurs, str(e))
    ctx.close()

    ctx, pg, demandes, erreurs = ouvrir(b)
    pg.get_by_role("button", name=re.compile("Mode mission")).first.click()
    pg.wait_for_timeout(600)
    vu = False
    for _ in range(12):
        vu = pg.evaluate("() => { const r = document.getElementById('freins-3d').getBoundingClientRect(); return r.height > 200 }")
        if vu or not pg.locator("#msSuiv").count():
            break
        pg.click("#msSuiv")
        pg.wait_for_timeout(250)
    ou = pg.evaluate("() => (document.getElementById('msOu') || {}).textContent || ''")
    t("mode mission : le bloc se montre avec l'activité 1, sans erreur", vu and "Activité 1" in ou and not erreurs, ou)
    ctx.close()
    b.close()

ok = sum(1 for _, v in res if v)
print("\n%d / %d tests passés" % (ok, len(res)))
sys.exit(0 if ok == len(res) else 1)
