# -*- coding: utf-8 -*-
"""Banc de `entete_telephone.py` (19/11/2026) : au navigateur, sur une page témoin du gabarit à onglets.

La page témoin porte le nom (avec « 💾 Sauvegardé » dedans), la barre d'outils (dont un bouton qui parle, aria-live),
la note « Ordinateur partagé », le choix du parcours et sa ligne d'état, puis le volet « Rappel », l'invitation au mode
mission (avec son petit bouton flottant), une longue carte de tête (un banc d'essai), une carte courte, et deux onglets.
"""
import os
import sys
import tempfile

from playwright.sync_api import sync_playwright

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
import entete_telephone as ET  # noqa: E402

PAGE = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head><body>
<main id="principal">
<h1>Témoin</h1>
<div class="identite" id="identite"><label>Nom : <input id="nom"></label><label>Classe : <input id="classe"></label>
<span class="saved-note" id="savedNote">💾 Sauvegardé</span></div>
<div class="toolbar"><button class="btn">🖨 Imprimer</button><button class="btn" id="btnReset" aria-live="polite">🗑 Effacer</button></div>
<p class="saved-note" data-note="poste-partage">🖥️ Ordinateur partagé : …</p>
<div class="toolbar choix-parcours-boutons"><button class="btn parcours-btn">🅰</button><button class="btn parcours-btn">🅱</button></div>
<p class="saved-note" id="parcoursNote" role="status">Parcours affiché : tous.</p>
<details class="rappel-ouverture" id="ouverture" open><summary>📖 Rappel</summary><p>La situation.</p></details>
<div class="toolbar" id="apres">Barre placée après le volet : elle reste.</div>
<div class="progress-wrap"><span>0 / 3</span><div class="ms-invite"><button class="btn" id="btnMission">🎮 Mode mission</button>
<button class="ms-revenir" id="msRevenir" style="position:fixed;right:8px;bottom:8px">🎮</button></div></div>
<section class="card" id="banc"><h2>🧪 Le banc d'essai (version 🅱 — toujours là)</h2><div style="height:700px">simulateur</div><input id="curseur" type="range"></section>
<div class="cadre"><div class="card" id="mini"><h2>Petite carte</h2></div></div>
<div class="card" id="courte"><h3>Une carte courte</h3><p>deux mots</p></div>
<div class="seance-tabs"><button class="seance-tab active" data-panel="s1">Séance 1</button><button class="seance-tab" data-panel="s2">Séance 2</button></div>
<section class="seance-panel active" id="s1">un</section><section class="seance-panel" id="s2">deux</section>
</main>
<script>
document.querySelectorAll(".seance-tab").forEach(function(t){ t.addEventListener("click", function(){
  document.querySelectorAll(".seance-tab").forEach(function(x){ x.classList.toggle("active", x === t); });
  document.querySelectorAll(".seance-panel").forEach(function(p){ p.classList.toggle("active", p.id === t.dataset.panel); });
}); });
</script>
</body></html>"""

ok = ko = 0


def verifie(nom, cond, detail=""):
    global ok, ko
    ok, ko = (ok + 1, ko) if cond else (ok, ko + 1)
    print(("  ✔ " if cond else "  ✘ ") + nom + ("" if cond else "  — %s" % detail))


src = ET.poser(PAGE)
verifie("le bloc est posé une fois, avant </body>", src.count(ET.DEBUT) == 1 and src.index(ET.DEBUT) < src.index("</body>"))
verifie("reposé, il ne change rien", ET.poser(src) == src)
lien = PAGE.replace('<button class="seance-tab active" data-panel="s1">', '<a class="seance-tab active" href="p1.html">').replace(
    'Séance 1</button>', 'Séance 1</a>')

VUS = """() => { const v = (s) => { const e = document.querySelector(s); return !!e && e.checkVisibility(); };
  return { bouton: v('.entete-bascule'), ouvert: (document.querySelector('.entete-bascule') || {}).getAttribute?.('aria-expanded'),
    nom: v('#nom'), sauve: v('#savedNote'), barre: v('.toolbar'), effacer: v('#btnReset'), poste: v('[data-note=poste-partage]'),
    parcours: v('.choix-parcours-boutons'), etat: v('#parcoursNote'), apres: v('#apres'),
    mission: v('#btnMission'), revenir: v('#msRevenir'), banc: (document.querySelector('#banc').getBoundingClientRect().height > 50),
    bancInerte: document.querySelector('#banc').inert, courte: v('#courte'),
    carte: (() => { const b = [...document.querySelectorAll('.entete-carte-bascule')].find(x => x.checkVisibility()); return b ? b.textContent : null; })(),
    largeur: document.querySelector('#banc').getBoundingClientRect().width,
    libelle: (document.querySelector('.entete-bascule') || {}).textContent || '' }; }"""

with tempfile.TemporaryDirectory() as d, sync_playwright() as p:
    b = p.chromium.launch()
    f = os.path.join(d, "temoin.html")
    open(f, "w", encoding="utf-8").write(src)
    for w in (390, 1280):
        ctx = b.new_context(viewport={"width": w, "height": 844})
        pg = ctx.new_page()
        err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto("file://" + f)
        pg.wait_for_timeout(100)
        s1 = pg.evaluate(VUS)
        verifie("%d px, séance 1 : tout se voit, pas de bouton ⚙️" % w,
                not s1["bouton"] and s1["nom"] and s1["barre"] and s1["poste"] and s1["parcours"], s1)
        pg.click('.seance-tab >> nth=1')
        pg.wait_for_timeout(80)
        s2 = pg.evaluate(VUS)
        if w == 390:
            verifie("390 px, séance 2 : les réglages se replient derrière ⚙️",
                    s2["bouton"] and s2["ouvert"] == "false" and not s2["nom"] and not s2["barre"] and not s2["poste"]
                    and not s2["parcours"], s2)
            verifie("390 px, séance 2 : les zones d'état restent (« Sauvegardé », « Parcours affiché »)",
                    s2["sauve"] and s2["etat"], s2)
            verifie("un bouton qui parle (aria-live) n'est pas une zone d'état : il se replie avec sa barre", not s2["effacer"], s2)
            verifie("ce qui suit le volet « Rappel » ne se replie pas", s2["apres"], s2)
            verifie("le bouton dit que le nom n'est pas écrit", "pas encore écrit" in s2["libelle"], s2["libelle"])
            verifie("l'invitation au mode mission se replie, le petit bouton flottant « 🎮 » reste",
                    not s2["mission"] and s2["revenir"], s2)
            verifie("une longue carte de tête se replie en une ligne, au titre court, inerte, sans perdre sa largeur",
                    not s2["banc"] and s2["bancInerte"] and s2["carte"] == "▸ 🧪 Le banc d'essai" and s2["largeur"] > 300, s2)
            verifie("une carte courte ne se replie pas (le bouton prendrait autant de place qu'elle)", s2["courte"], s2)
            pg.click(".entete-carte-bascule >> visible=true")
            pg.wait_for_timeout(50)
            o = pg.evaluate(VUS)
            verifie("un appui rouvre la carte (et elle n'est plus inerte)", o["banc"] and not o["bancInerte"]
                    and o["carte"].startswith("▾"), o)
            pg.click(".entete-bascule")
            pg.wait_for_timeout(50)
            o = pg.evaluate(VUS)
            verifie("un appui montre les réglages", o["ouvert"] == "true" and o["nom"] and o["barre"] and o["parcours"], o)
            pg.fill("#nom", "Léa")
            pg.fill("#classe", "4eB")
            o = pg.evaluate(VUS)
            verifie("le bouton porte le nom écrit", "Léa 4eB" in o["libelle"], o["libelle"])
            pg.click(".entete-bascule")
            pg.wait_for_timeout(50)
            verifie("un second appui les replie", not pg.evaluate(VUS)["nom"])
            pg.click('.seance-tab >> nth=0')
            pg.wait_for_timeout(80)
            verifie("retour à la séance 1 : tout se voit de nouveau", pg.evaluate(VUS)["nom"])
        else:
            verifie("1280 px, séance 2 : rien ne se replie", not s2["bouton"] and s2["nom"] and s2["barre"] and s2["parcours"]
                    and s2["banc"] and s2["mission"] and s2["carte"] is None, s2)
        verifie("%d px : aucune erreur JavaScript" % w, not err, err[:1])
        ctx.close()
    # des onglets qui sont des liens : la page n'est pas touchée
    f2 = os.path.join(d, "lien.html")
    open(f2, "w", encoding="utf-8").write(ET.poser(lien))
    ctx = b.new_context(viewport={"width": 390, "height": 844})
    pg = ctx.new_page()
    pg.goto("file://" + f2)
    pg.wait_for_timeout(80)
    verifie("des onglets qui sont des liens : aucun bouton ⚙️", pg.locator(".entete-bascule").count() == 0)
    ctx.close()
    b.close()

with tempfile.TemporaryDirectory() as d:
    import subprocess
    vide = subprocess.run([sys.executable, os.path.join(OUT, "entete_telephone.py"), d], capture_output=True, text=True)
    verifie("n°299. aucune page lue : sortie 2", vide.returncode == 2)

print("══ entete_telephone : %d / %d ══" % (ok, ok + ko))
sys.exit(1 if ko else 0)
