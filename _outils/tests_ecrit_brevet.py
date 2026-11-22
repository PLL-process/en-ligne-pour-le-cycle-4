# -*- coding: utf-8 -*-
"""Banc commun des écrits « comme au brevet » (règle d'or n°346, skill `tache-finale-redigee`).

    python3 _outils/tests_ecrit_brevet.py <page.html> [<page.html> …]
    python3 _outils/tests_ecrit_brevet.py --tout        (toutes les pages qui portent un bloc .ecrit-brevet)

Pour chaque bloc `.ecrit-brevet` d'une page, au navigateur, à 390 px :
  1. la forme : au moins deux zones de texte, aucune proposition (ni bouton radio, ni liste), une version étayée par
     zone (n°31), deux aides repliées avant la correction — un indice, puis la démarche (n°367) —, une correction
     repliée avec une phrase de copie par zone (n°356), une grille de cases à cocher ;
  2. le programme ou le document sous les yeux : un listing ou une figure dans le bloc (n°331) ;
  3. rien n'est noté : écrire et cocher change la ligne d'état, jamais `window.__valid` (n°340) ;
  4. la reprise : après rechargement, le texte et les cases reviennent ;
  5. le lien direct `#<id du bloc>` ouvre la séance qui le contient (n°359) ;
  6. aucune erreur JavaScript, aucun défilement horizontal de la page.

Sortie : 0 tout passe · 1 un échec · 2 rien n'a été lu (Playwright absent, aucun bloc) — règle n°299.
"""
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
THEMES = ("theme-1-objets-systemes-usages-interactions", "theme-2-structure-fonctionnement-comportement",
          "theme-3-creation-conception-realisation-innovations")

JS_FORME = r"""(id) => {
  const z = document.getElementById(id);
  const zones = [...z.querySelectorAll('textarea')];
  const avantCorr = el => { const c = z.querySelector('details.correction'); return c && (el.compareDocumentPosition(c) & Node.DOCUMENT_POSITION_FOLLOWING); };
  const aides = [...z.querySelectorAll('details.aide, details.aide1, details.aide2')].filter(avantCorr);
  const corr = z.querySelector('details.correction');
  return {
    zones: zones.length,
    propositions: z.querySelectorAll('input[type=radio], select').length,
    etayages: z.querySelectorAll('details.etayage').length,
    aides: aides.length, aidesFermees: aides.every(a => !a.open),
    correction: !!corr, correctionFermee: !!corr && !corr.open,
    copies: corr ? (corr.textContent.match(/Sur ta copie, on peut écrire/g) || []).length : 0,
    grille: z.querySelectorAll('.grille-ecrit input[type=checkbox]').length,
    sousLesYeux: z.querySelectorAll('pre, svg, img, figure, table').length,
    etat: !!z.querySelector('.etat-ecrit'),
    ids: zones.map(t => t.id), cases: [...z.querySelectorAll('.grille-ecrit input[type=checkbox]')].map(c => c.id),
  };
}"""


def pages_tout():
    for th in THEMES:
        for p in sorted((RACINE / th).rglob("*.html")):
            try:
                if 'class="ecrit-brevet"' in p.read_text(encoding="utf-8", errors="ignore"):
                    yield p
            except OSError:
                pass


def ouvrir_seance(pg, bloc_id):
    pg.evaluate("""(id) => { const z = document.getElementById(id); const pan = z && z.closest('.seance-panel');
      if (pan && !pan.classList.contains('active')) { const o = document.querySelector('.seance-tab[data-panel="' + pan.id + '"]'); if (o) o.click(); } }""", bloc_id)
    pg.wait_for_timeout(250)


def banc_page(nav, page, res):
    url = page.resolve().as_uri()
    nom = page.name
    ctx = nav.new_context(viewport={"width": 390, "height": 844})
    pg = ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    pg.goto(url)
    pg.wait_for_timeout(500)
    blocs = pg.eval_on_selector_all(".ecrit-brevet[id]", "l => l.map(e => e.id)")
    if not blocs:
        print(f"○ {nom} — aucun bloc .ecrit-brevet avec un id : rien lu")
        ctx.close()
        return False
    for b in blocs:
        def t(quoi, ok, detail=""):
            res.append(bool(ok))
            print(("✔" if ok else "✘"), f"{nom} #{b} — {quoi}", "" if ok else f"— {detail}")
        f = pg.evaluate(JS_FORME, b)
        t("au moins deux zones de texte, aucune proposition", f["zones"] >= 2 and f["propositions"] == 0, f)
        t("une version étayée par zone (n°31)", f["etayages"] >= f["zones"], f["etayages"])
        t("deux aides repliées avant la correction : un indice, puis la démarche (n°367)",
          f["aides"] >= 2 and f["aidesFermees"], f["aides"])
        t("une correction repliée, une phrase de copie par zone (n°356)",
          f["correctionFermee"] and f["copies"] >= f["zones"], (f["correctionFermee"], f["copies"]))
        t("une grille à cocher et une ligne d'état", f["grille"] >= 2 and f["etat"], (f["grille"], f["etat"]))
        t("le programme ou le document sous les yeux, dans le bloc (n°331)", f["sousLesYeux"] >= 1, f["sousLesYeux"])
        ouvrir_seance(pg, b)
        valide_avant = pg.evaluate("JSON.stringify(window.__valid || null)")
        etat_avant = pg.inner_text(f"#{b} .etat-ecrit")
        premier, case = f["ids"][0], f["cases"][0]
        pg.fill(f"#{premier}", "Réponse du banc : une phrase complète, avec la valeur et le signe.")
        pg.check(f"#{case}")
        pg.wait_for_timeout(800)
        etat_apres = pg.inner_text(f"#{b} .etat-ecrit")
        t("écrire et cocher change la ligne d'état, sans rien valider ni noter (n°340)",
          etat_apres != etat_avant and pg.evaluate("JSON.stringify(window.__valid || null)") == valide_avant
          and "note" in etat_apres, etat_apres)
        pg.reload()
        pg.wait_for_timeout(600)
        ouvrir_seance(pg, b)
        t("après rechargement, le texte et la case reviennent",
          pg.input_value(f"#{premier}").startswith("Réponse du banc") and pg.is_checked(f"#{case}"))
        large = pg.evaluate("document.documentElement.scrollWidth")
        t("aucun défilement horizontal à 390 px", large <= 392, large)
        c2 = nav.new_context(viewport={"width": 390, "height": 844})
        p2 = c2.new_page()
        p2.goto(url + "#" + b)
        p2.wait_for_timeout(600)
        t(f"le lien direct #{b} ouvre la séance qui le contient (n°359)", p2.is_visible(f"#{b}"))
        c2.close()
    t2 = not err
    res.append(t2)
    print(("✔" if t2 else "✘"), f"{nom} — aucune erreur JavaScript", "" if t2 else err[:2])
    ctx.close()
    return True


def main(argv):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("✘ Playwright absent : rien n'a été vérifié (n°299)")
        return 2
    if not argv:
        print(__doc__)
        return 2
    pages = list(pages_tout()) if argv == ["--tout"] else [pathlib.Path(a) for a in argv]
    res, lues = [], 0
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for page in pages:
            lues += banc_page(nav, page, res)
        nav.close()
    if not lues:
        print("Rien n'a été lu : ce banc n'a rien vérifié (n°299).")
        return 2
    print(f"\n{sum(res)} / {len(res)} contrôles passés sur {lues} page(s)")
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
