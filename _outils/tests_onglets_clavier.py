# -*- coding: utf-8 -*-
"""Banc de `onglets_clavier.py` (17/11/2026) : la pose, sa reprise, ce qu'elle laisse tranquille, et le clavier au navigateur."""
import os
import subprocess
import sys
import tempfile

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
import onglets_clavier as O  # noqa: E402

PAGE = """<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>t</title></head><body>
<div role="tablist" id="seances">
<button class="seance-tab active" role="tab" aria-selected="true" data-panel="s1" id="tab-s1">Séance 1</button>
<button class="seance-tab" role="tab" aria-selected="false" data-panel="s2" id="tab-s2">Séance 2</button>
<button class="seance-tab" role="tab" aria-selected="false" data-panel="s3">Séance 3</button>
</div>
<section id="s1">un</section><section id="s2" hidden>deux</section><section id="s3" hidden>trois</section>
<script>
document.querySelectorAll('[role="tab"]').forEach(function(t){ t.addEventListener("click", function(){
  document.querySelectorAll('[role="tab"]').forEach(function(u){ var on = u === t; u.classList.toggle("active", on);
    u.setAttribute("aria-selected", on ? "true" : "false"); document.getElementById(u.dataset.panel).hidden = !on; }); }); });
</script>
</body></html>
"""
ok = ko = 0


def verifie(nom, cond):
    global ok, ko
    if cond:
        ok += 1
        print("  ✔ " + nom)
    else:
        ko += 1
        print("  ✘ " + nom)


u = O.poser(PAGE)
verifie("1. le bloc est posé une fois, avant </body>", u.count(O.DEBUT) == 1 and u.index(O.FIN) < u.index("</body>"))
verifie("2. reposer ne change rien (idempotent)", O.poser(u) == u)
vieux = u.replace('e.key === "End"', 'e.key === "Fin"')
verifie("3. un bloc d'une autre version est remis à jour", O.poser(vieux) == u)
deja = PAGE.replace("</body>", "<script>document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){}});</script></body>")
verifie("4. une page qui gère déjà les flèches est laissée telle quelle", O.poser(deja) == deja)
sans = "<html><body><p>pas d'onglets</p></body></html>"
verifie("5. une page sans onglets est laissée telle quelle", O.poser(sans) == sans)

# 6 à 9 : au navigateur
with tempfile.TemporaryDirectory() as d:
    f = os.path.join(d, "p.html")
    open(f, "w", encoding="utf-8").write(u)
    js = r"""
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage(); const err = []; p.on('pageerror', e => err.push(e.message));
  await p.goto('file://' + process.argv[2]);
  const etat = () => p.evaluate(() => { const t = [...document.querySelectorAll('[role=tab]')];
    return { focus: document.activeElement.textContent, zero: t.filter(x => x.tabIndex === 0).map(x => x.textContent),
      ctrl: t.map(x => x.getAttribute('aria-controls')).join(','), lab: document.getElementById('s3').getAttribute('aria-labelledby'),
      role: document.getElementById('s2').getAttribute('role'), vis: [...document.querySelectorAll('section')].filter(s => !s.hidden).map(s => s.id).join() }; });
  const r = { debut: await etat() };
  await p.focus('#tab-s1'); await p.keyboard.press('ArrowRight'); await p.waitForTimeout(60); r.droite = await etat();
  await p.keyboard.press('End'); await p.waitForTimeout(60); r.fin = await etat();
  await p.keyboard.press('ArrowRight'); await p.waitForTimeout(60); r.boucle = await etat();
  await p.keyboard.press('ArrowLeft'); await p.waitForTimeout(60); r.gauche = await etat();
  await p.keyboard.press('Home'); await p.waitForTimeout(60); r.home = await etat();
  r.err = err; console.log(JSON.stringify(r)); await b.close();
})();
"""
    sj = os.path.join(d, "t.js")
    open(sj, "w").write(js)
    res = subprocess.run(["node", sj, f], capture_output=True, text=True)
    import json
    try:
        r = json.loads(res.stdout.strip().splitlines()[-1])
    except Exception:
        print(res.stdout, res.stderr)
        r = None
    if r:
        verifie("6. chaque onglet est relié à son panneau (aria-controls, tabpanel, aria-labelledby)",
                r["debut"]["ctrl"] == "s1,s2,s3" and r["debut"]["role"] == "tabpanel" and r["debut"]["lab"] == "onglet-3")
        verifie("7. un seul onglet dans l'ordre de tabulation : la séance ouverte", r["debut"]["zero"] == ["Séance 1"])
        verifie("8. → ouvre la séance suivante et y met le focus ; Fin la dernière ; → y revient à la première",
                r["droite"]["vis"] == "s2" and r["droite"]["focus"] == "Séance 2" and r["droite"]["zero"] == ["Séance 2"]
                and r["fin"]["vis"] == "s3" and r["boucle"]["vis"] == "s1")
        verifie("9. ← revient en arrière (en boucle), Début ouvre la première, sans erreur JavaScript",
                r["gauche"]["vis"] == "s3" and r["home"]["vis"] == "s1" and r["home"]["focus"] == "Séance 1" and not r["err"])
    else:
        verifie("6 à 9. le navigateur a répondu", False)

print("══ onglets_clavier : %d / %d ══" % (ok, ok + ko))
sys.exit(1 if ko else 0)
