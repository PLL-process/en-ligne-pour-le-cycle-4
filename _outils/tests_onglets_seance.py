# -*- coding: utf-8 -*-
"""Banc de `onglets_seance.py` (audit du jardin connecté, 19/11/2026) : au navigateur, sur deux pages témoins.

Page A : trois onglets de séance, sans clavier. Page B : les mêmes, avec le bloc de `onglets_clavier.py` (n°326) qui
gère déjà ← → : le bloc ne doit pas déplacer une seconde fois.
"""
import os
import sys
import tempfile

from playwright.sync_api import sync_playwright

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
import onglets_clavier as OC  # noqa: E402
import onglets_seance as OS  # noqa: E402

PAGE = """<!doctype html><html><head><meta charset="utf-8"></head><body>
<div class="seance-tabs" role="tablist">
<button class="seance-tab active" role="tab" aria-selected="true" data-panel="s1">Séance 1</button>
<button class="seance-tab" role="tab" aria-selected="false" data-panel="s2">Séance 2</button>
<button class="seance-tab" role="tab" aria-selected="false" data-panel="s3">Séance 3</button>
</div>
<section class="seance-panel active" id="s1"><p>un</p></section>
<section class="seance-panel" id="s2"><p>deux</p></section>
<section class="seance-panel" id="s3"><p>trois</p><div style="height:3000px"></div></section>
<script>
document.querySelectorAll(".seance-tab").forEach(function(t){ t.addEventListener("click", function(){
  document.querySelectorAll(".seance-tab").forEach(function(x){ x.classList.toggle("active", x === t); x.setAttribute("aria-selected", x === t); });
  document.querySelectorAll(".seance-panel").forEach(function(p){ p.classList.toggle("active", p.id === t.dataset.panel); });
}); });
</script>
</body></html>"""

ok = ko = 0


def verifie(nom, cond, detail=""):
    global ok, ko
    ok, ko = (ok + 1, ko) if cond else (ok, ko + 1)
    print(("  ✔ " if cond else "  ✘ ") + nom + ("" if cond else "  — %s" % detail))


src = OS.poser(PAGE)
verifie("le bloc est posé une fois, avant </body>", src.count(OS.DEBUT) == 1 and src.index(OS.DEBUT) < src.index("</body>"))
verifie("reposé, il ne change rien", OS.poser(src) == src)
verifie("des onglets qui sont des liens : la page n'est pas visée par le clavier",
        "a[href]" in OS.SCRIPT)
avec_clavier = OS.poser(OC.poser(PAGE))   # onglets_clavier.py ne se pose pas sur une page qui gère déjà ses flèches
verifie("la page témoin B porte aussi le bloc de onglets_clavier.py", OC.DEBUT in avec_clavier)


def ouvert(pg):
    return pg.evaluate("() => [...document.querySelectorAll('.seance-tab')].findIndex(o => o.classList.contains('active'))")


with tempfile.TemporaryDirectory() as d, sync_playwright() as p:
    b = p.chromium.launch()
    for nom, html in (("A", src), ("B", avec_clavier)):
        f = os.path.join(d, "temoin_%s.html" % nom)
        open(f, "w", encoding="utf-8").write(html)
        ctx = b.new_context(viewport={"width": 1280, "height": 700})
        pg = ctx.new_page()
        err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto("file://" + f)
        pg.evaluate("() => localStorage.clear()")
        pg.reload()
        pg.wait_for_timeout(100)
        tabs = pg.evaluate("() => [...document.querySelectorAll('.seance-tab')].map(o => o.tabIndex)")
        verifie("%s : seul l'onglet ouvert est dans l'ordre de tabulation" % nom, tabs == [0, -1, -1], tabs)
        pg.focus(".seance-tab >> nth=0")
        pg.keyboard.press("ArrowRight")
        pg.wait_for_timeout(50)
        verifie("%s : → ouvre la séance 2, une seule fois" % nom, ouvert(pg) == 1, ouvert(pg))
        pg.keyboard.press("End")
        pg.wait_for_timeout(50)
        verifie("%s : Fin ouvre la dernière séance" % nom, ouvert(pg) == 2, ouvert(pg))
        pg.keyboard.press("ArrowRight")
        pg.wait_for_timeout(50)
        verifie("%s : → depuis la dernière revient à la première (en boucle)" % nom, ouvert(pg) == 0, ouvert(pg))
        pg.keyboard.press("ArrowLeft")
        pg.wait_for_timeout(50)
        pg.evaluate("() => window.scrollTo(0, 400)")
        pg.wait_for_timeout(50)
        pg.reload()
        pg.wait_for_timeout(250)
        verifie("%s : rechargée, la page rouvre la séance où l'élève était" % nom, ouvert(pg) == 2, ouvert(pg))
        pg.goto("about:blank")
        pg.goto("file://" + f + "#s1")
        pg.wait_for_timeout(250)
        verifie("%s : une adresse qui vise une ancre l'emporte (rien n'est rouvert)" % nom, ouvert(pg) == 0, ouvert(pg))
        verifie("%s : aucune erreur JavaScript" % nom, not err, err[:1])
        ctx.close()
    b.close()

with tempfile.TemporaryDirectory() as d:
    import subprocess
    vide = subprocess.run([sys.executable, os.path.join(OUT, "onglets_seance.py"), d], capture_output=True, text=True)
    verifie("n°299. aucune page lue : sortie 2", vide.returncode == 2)

print("══ onglets_seance : %d / %d ══" % (ok, ok + ko))
sys.exit(1 if ko else 0)
