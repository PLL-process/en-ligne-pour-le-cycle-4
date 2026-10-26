# -*- coding: utf-8 -*-
"""controle_mode_essentiel.py — le mode essentiel ne laisse aucun titre seul (règle d'or n°29, décision du 26/10/2026).

    python3 _outils/controle_mode_essentiel.py [racine] [--muet]

LE CONSTAT
----------
Le 26/10/2026, Pascal ouvre le jardin de New York (4e_C8.1) en « Mode essentiel : ON » : une carte « 🎯 CRCN mobilisés »
s'affiche, vide. Le mode essentiel (règle n°29) masque le référentiel, les corrections et les compléments — ici, tout le
contenu de la carte — mais pas son titre. Un titre sans rien dessous dit à l'élève qu'il lui manque quelque chose.

CE QU'IL FAIT
-------------
Il ouvre dans Chromium chaque page qui offre le mode essentiel (`#btnEssentiel`), relève les cartes à titre (`section`,
`.card` qui commencent par un h2 ou un h3) qui ont un contenu visible, active le mode essentiel par son bouton, et
REFUSE une carte dont il ne reste que le titre. Il désactive ensuite le mode (la page reste comme il l'a trouvée).

Sortie 0 : aucune carte réduite à son titre ; 1 : refus nommés ; 2 : aucune page lue (règle n°299).
NON VU : une carte dont il ne reste qu'une phrase sans intérêt (cela se regarde) ; ce qui n'apparaît qu'après un clic ;
les pages sans bouton de mode essentiel.
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import panne  # noqa: E402

RELEVE = r"""() => {
  const vis = e => !!e && e.checkVisibility({checkVisibilityCSS: true});
  const plein = x => vis(x) && (x.textContent.trim() || x.querySelector('img,svg,canvas,video,object,input,textarea,select,iframe'));
  return [...document.querySelectorAll('section, .card')].filter(c => c.querySelector(':scope > h2, :scope > h3'))
    .map((c, i) => { c.setAttribute('data-ce', i); return {i, plein: vis(c) && [...c.children].some(x => !/^H[23]$/.test(x.tagName) && plein(x))}; })
    .filter(x => x.plein).map(x => x.i);
}"""
APRES = r"""(avant) => {
  const vis = e => !!e && e.checkVisibility({checkVisibilityCSS: true});
  const plein = x => vis(x) && (x.textContent.trim() || x.querySelector('img,svg,canvas,video,object,input,textarea,select,iframe'));
  const seuls = [];
  for (const i of avant) {
    const c = document.querySelector('[data-ce="' + i + '"]'); if (!c || !vis(c)) continue;
    if (![...c.children].some(x => !/^H[23]$/.test(x.tagName) && plein(x)))
      seuls.push(c.querySelector(':scope > h2, :scope > h3').textContent.replace(/\s+/g, ' ').trim().slice(0, 70));
  }
  document.querySelectorAll('[data-ce]').forEach(c => c.removeAttribute('data-ce'));
  return seuls;
}"""


def main(racine=None, muet=False):
    racine = pathlib.Path(racine or pathlib.Path(__file__).resolve().parents[1]).resolve()
    pages = sorted(p for p in racine.rglob("sequence*.html") if "_archive-anciennes-versions" not in p.parts)
    lues, avec, refus = 0, 0, []
    if pages:
        with sync_playwright() as pw:
            nav = pw.chromium.launch()
            for p in pages:
                ctx = nav.new_context(viewport={"width": 1280, "height": 900})   # contexte neuf : mode essentiel éteint
                pg = ctx.new_page()
                try:
                    pg.goto(p.as_uri()); pg.wait_for_timeout(300)
                except Exception:
                    ctx.close(); continue
                lues += 1
                if pg.locator("#btnEssentiel").count() == 0:
                    ctx.close(); continue
                avec += 1
                if pg.evaluate("document.body.classList.contains('essentiel')"):
                    pg.click("#btnEssentiel"); pg.wait_for_timeout(100)
                avant = pg.evaluate(RELEVE)
                pg.click("#btnEssentiel"); pg.wait_for_timeout(150)
                seuls = pg.evaluate(APRES, avant)
                pg.click("#btnEssentiel")
                if seuls:
                    refus.append((str(p.relative_to(racine)), seuls))
                ctx.close()
            nav.close()
    if not lues:
        return panne.rien_vu("aucune séquence lue sous %s" % racine)
    if not muet:
        print("%d séquence(s) lues · %d offrent le mode essentiel · %d laissent un titre seul" % (lues, avec, len(refus)))
        print("     NON VU : une carte réduite à une phrase sans intérêt (cela se regarde), ce qui n'apparaît qu'après un clic.")
    if refus:
        print("\n⛔ en mode essentiel, %d page(s) laissent un titre sans contenu :" % len(refus))
        for rel, seuls in refus:
            print("  %s\n     %s" % (rel, " | ".join(seuls)))
        print("\n     Masque la carte entière (titre compris), ou déplace son contenu là où il sert (synthèse professeur).")
        return 1
    print("\n✅ en mode essentiel, aucune carte ne se réduit à son titre")
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != "--muet"]
    sys.exit(main(a[0] if a else None, "--muet" in sys.argv))
