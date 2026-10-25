# -*- coding: utf-8 -*-
"""Banc du lecteur pas à pas commun, au navigateur, sur chaque animation du dépôt.

    python3 _outils/lecteur_pas_a_pas/banc_lecteur.py [racine]

Pour chaque bloc `[data-lpp-racine]` de chaque page (hors archives) :
  · il s'ouvre (bouton d'ouverture s'il y en a un), commence à « Étape 1 / N », Précédent désactivé ;
  · « Suivant » parcourt toutes les étapes : à chacune, une phrase non vide, le compteur juste, zéro erreur
    JavaScript ; à la dernière, Suivant est désactivé ; « Recommencer » ramène à l'étape 1 ;
  · s'il parle (`data-lpp-voix`), chaque étape a son fichier .ogg ET son .mp3 sur le disque ;
  · à 390 px, aucune étape ne fait défiler la page en largeur ;
  · sous « mouvement réduit », toutes les étapes se montrent sans erreur ;
  · à l'impression : le bloc est masqué s'il le demande (`lpp-sans-impression`, la page imprime autre chose),
    sinon la liste des N étapes s'imprime ;
  · le lien direct `page.html#id` amène le bloc à l'écran (et l'ouvre).
Sortie 0 / 1 (refus nommés) / 2 (aucun bloc trouvé : rien n'a été vérifié, règle n°299).

Ce qu'il NE juge PAS : la justesse des phrases et des dessins, la qualité de la voix (écoute de Pascal),
ce qui est propre à une animation (bancs des lots : `tests_animation_trois_principes.py`, `tests_4e_C8.mjs`…).
"""
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

RACINE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[2]).resolve()
pages = [p for p in sorted(RACINE.rglob("*.html"))
         if "_archive-anciennes-versions" not in p.parts and "data-lpp-racine" in p.read_text(encoding="utf-8", errors="replace")]
refus, vus = [], []


def r(page, bloc, quoi):
    refus.append("%s #%s — %s" % (page.relative_to(RACINE), bloc, quoi))


def ouvrir(pg, sel):
    b = pg.locator(sel + ' [data-lpp="ouvrir"]')
    if b.count() and pg.locator(sel + ' [data-lpp="panneau"]').first.is_hidden():
        b.first.click(); pg.wait_for_timeout(150)


def compte(pg, sel):
    return (pg.locator(sel + ' [data-lpp="compte"]').first.text_content() or "").strip()


def parcourir(pg, page, bid, largeur):
    sel = "#" + bid
    pg.locator(sel).scroll_into_view_if_needed(); ouvrir(pg, sel)
    c = compte(pg, sel)
    m = re.match(r"^(\S+) 1 / (\d+)$", c)                # « Étape 1 / 7 », « Scène 1 / 6 »
    if not m:
        r(page, bid, "%d px : ne commence pas à l'étape 1 (« %s »)" % (largeur, c)); return 0
    mot, n = m.group(1), int(m.group(2))
    if not pg.locator(sel + ' [data-lpp="prec"]').first.is_disabled():
        r(page, bid, "Précédent actif à l'étape 1")
    for k in range(1, n + 1):
        if k > 1:
            s = pg.locator(sel + ' [data-lpp="suiv"]').first
            if s.is_disabled():
                r(page, bid, "%d px : Suivant désactivé à l'étape %d / %d" % (largeur, k - 1, n)); return n
            s.click(); pg.wait_for_timeout(120)
        if compte(pg, sel) != "%s %d / %d" % (mot, k, n):
            r(page, bid, "%d px : compteur « %s » à l'étape %d" % (largeur, compte(pg, sel), k))
        if not (pg.locator(sel + ' [data-lpp="texte"]').first.text_content() or "").strip():
            r(page, bid, "%d px : étape %d sans phrase" % (largeur, k))
        if largeur <= 400 and pg.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1"):
            r(page, bid, "390 px : l'étape %d fait défiler la page en largeur" % k)
    if not pg.locator(sel + ' [data-lpp="suiv"]').first.is_disabled():
        r(page, bid, "Suivant encore actif à la dernière étape")
    z = pg.locator(sel + ' [data-lpp="zero"]')
    if z.count():
        z.first.click(); pg.wait_for_timeout(100)
        if not compte(pg, sel).startswith(mot + " 1 /"):
            r(page, bid, "Recommencer ne ramène pas à l'étape 1")
    return n


with sync_playwright() as pw:
    nav = pw.chromium.launch()
    for page in pages:
        for largeur, calme in ((1280, False), (390, False), (1280, True)):
            ctx = nav.new_context(viewport={"width": largeur, "height": 900}, reduced_motion="reduce" if calme else "no-preference")
            pg = ctx.new_page(); err = []
            pg.on("pageerror", lambda e: err.append(str(e)))
            pg.goto(page.as_uri()); pg.wait_for_timeout(400)
            ids = pg.evaluate("[...document.querySelectorAll('[data-lpp-racine]')].map(b => b.id)")
            for bid in ids:
                pg.evaluate("id => { const b = document.getElementById(id); const p = b.closest('[role=tabpanel],.seance,.panel'); "
                            "if (p && getComputedStyle(p).display === 'none') { const t = document.querySelector('[aria-controls=\"' + p.id + '\"]'); if (t) t.click(); } }", bid)
                pg.wait_for_timeout(150)
                n = parcourir(pg, page, bid, largeur)
                if largeur == 1280 and not calme:
                    vus.append((page, bid, n))
                    voix = pg.evaluate("id => document.getElementById(id).getAttribute('data-lpp-voix')", bid)
                    if voix:
                        manque = [voix + str(k) + e for k in range(1, n + 1) for e in (".ogg", ".mp3") if not (page.parent / (voix + str(k) + e)).exists()]
                        if manque:
                            r(page, bid, "fichiers de voix absents : " + ", ".join(manque[:4]))
                    pg.emulate_media(media="print")
                    etat = pg.evaluate("id => { const b = document.getElementById(id), l = b.querySelector('.lpp-imprime');"
                                       " return {cache: getComputedStyle(b).display === 'none', sans: b.classList.contains('lpp-sans-impression'),"
                                       " liste: l ? (getComputedStyle(l).display !== 'none' ? l.children.length : -1) : 0}; }", bid)
                    pg.emulate_media(media="screen")
                    if etat["sans"] and not etat["cache"]:
                        r(page, bid, "impression : le bloc devait être masqué")
                    if not etat["sans"] and etat["liste"] != n:
                        r(page, bid, "impression : la liste des étapes n'a pas %d éléments (%s)" % (n, etat["liste"]))
            if err:
                r(page, "-", "%d px%s : erreur JavaScript : %s" % (largeur, " (mouvement réduit)" if calme else "", err[0][:140]))
            ctx.close()
        # lien direct
        for p2, bid, n in [v for v in vus if v[0] == page]:
            ctx = nav.new_context(viewport={"width": 1280, "height": 900}); pg = ctx.new_page()
            pg.goto(page.as_uri() + "#" + bid); pg.wait_for_timeout(1300)
            ok = pg.evaluate("id => { const b = document.getElementById(id).getBoundingClientRect(); return b.top < innerHeight && b.bottom > 0 && b.height > 0; }", bid)
            if not ok:
                r(page, bid, "le lien direct #%s n'amène pas le bloc à l'écran" % bid)
            ctx.close()
    nav.close()

if not vus:
    print("⛔ aucun bloc [data-lpp-racine] trouvé sous %s : rien n'a été vérifié" % RACINE)
    sys.exit(2)
print("%d animation(s) sur %d page(s) : %s" % (len(vus), len(pages), ", ".join("%s (%d étapes)" % (b, n) for _, b, n in vus)))
for x in refus:
    print("  ✘ " + x)
if refus:
    sys.exit(1)
print("✅ chaque animation se parcourt, à 1280 et 390 px et sous « mouvement réduit », s'imprime et s'ouvre par son lien")
