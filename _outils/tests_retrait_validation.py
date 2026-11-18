# -*- coding: utf-8 -*-
"""Banc de `retrait_validation.py` (n°340, V3) : au navigateur, sur une page témoin.

Une page témoin garde ses validations dans `window.__valid`, avec deux activités : la première a un champ de texte,
un menu et un curseur ; la seconde, ses validations sous la clé « act2 ». La sauvegarde relue au chargement remet une
réponse en place (événement « change ») : elle ne doit rien retirer.
"""
import os
import sys
import tempfile

from playwright.sync_api import sync_playwright

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
import retrait_validation as RV  # noqa: E402

PAGE = """<!doctype html><html><head><meta charset="utf-8"></head><body>
<div class="activite"><input id="a1" value=""><select id="m1"><option>a</option><option>b</option></select>
<input type="range" id="r1" min="0" max="10" value="5">
<button data-check="1">Vérifier</button><p id="fb1" class="feedback ok"></p></div>
<div class="activite"><input id="a2" value="x"><button data-check="2">Vérifier</button><p id="fb2"></p></div>
<div class="seance-panel"><div class="card"><select id="m3"><option value=""></option><option>oui</option></select>
<button data-check="3">Vérifier</button><p id="fb3"></p></div>
<div class="card"><textarea id="bilan"></textarea></div></div>
<script>
window.__valid = {1: true, act2: true, 3: true};
let sauves = 0, recomptes = 0;
function save(){ sauves++; }
function majProgress(){ recomptes++; }
/* la reprise d'une sauvegarde : elle remet une réponse et prévient la page */
const a = document.getElementById("a1"); a.value = "repris"; a.dispatchEvent(new Event("change", {bubbles: true}));
window.addEventListener("load", () => { a.dispatchEvent(new Event("input", {bubbles: true})); });
</script>
</body></html>"""

ok = ko = 0


def verifie(nom, cond, detail=""):
    global ok, ko
    ok, ko = (ok + 1, ko) if cond else (ok, ko + 1)
    print(("  ✔ " if cond else "  ✘ ") + nom + ("" if cond else "  — %s" % detail))


src = RV.poser(PAGE)
verifie("le bloc est posé une fois, avant </body>", src.count(RV.DEBUT) == 1 and src.index(RV.DEBUT) < src.index("</body>"))
verifie("reposé, il ne change rien", RV.poser(src) == src)
verifie("une page qui retire déjà ses validations n'est pas touchée",
        RV.poser(PAGE.replace("let sauves", "window.__valid[1] = false; let sauves")) == PAGE.replace("let sauves", "window.__valid[1] = false; let sauves"))

with tempfile.TemporaryDirectory() as d, sync_playwright() as p:
    f = os.path.join(d, "temoin.html")
    open(f, "w", encoding="utf-8").write(src)
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto("file://" + f)
    pg.wait_for_timeout(150)
    v = pg.evaluate("() => Object.assign({}, window.__valid)")
    verifie("la reprise d'une sauvegarde, au chargement, ne retire rien", v.get("1") is True and v.get("act2") is True, v)
    pg.evaluate("() => { const r = document.getElementById('r1'); r.value = '8'; r.dispatchEvent(new Event('input', {bubbles: true})); }")
    verifie("un curseur bougé ne retire rien", pg.evaluate("() => window.__valid[1]") is True)
    pg.fill("#a1", "autre")
    verifie("un texte changé retire la validation de SON activité",
            pg.evaluate("() => window.__valid[1]") is False and pg.evaluate("() => window.__valid.act2") is True)
    verifie("le retour le dit, sans la marque de réussite",
            "vérifie de nouveau" in pg.text_content("#fb1") and "ok" not in pg.get_attribute("#fb1", "class"))
    verifie("la page enregistre et recompte", pg.evaluate("() => sauves > 0 && recomptes > 0"))
    pg.fill("#a2", "y")
    verifie("la clé « act2 » est retirée aussi", pg.evaluate("() => window.__valid.act2") is False)
    pg.fill("#bilan", "ce que j'ai appris")
    verifie("le bilan de la séance n'est pas l'activité : il ne retire rien", pg.evaluate("() => window.__valid[3]") is True)
    pg.evaluate("() => { const m = document.getElementById('m3'); m.value = ''; m.dispatchEvent(new Event('change', {bubbles: true})); }")
    verifie("une réponse vidée (le mode mission efface une proposition fausse) ne retire rien",
            pg.evaluate("() => window.__valid[3]") is True)
    pg.select_option("#m3", "oui")
    verifie("une réponse choisie retire la validation", pg.evaluate("() => window.__valid[3]") is False)
    b.close()

with tempfile.TemporaryDirectory() as d:
    import subprocess
    vide = subprocess.run([sys.executable, os.path.join(OUT, "retrait_validation.py"), d], capture_output=True, text=True)
    verifie("n°299. aucune page lue : sortie 2", vide.returncode == 2)

print("══ retrait_validation : %d / %d ══" % (ok, ok + ko))
sys.exit(1 if ko else 0)
