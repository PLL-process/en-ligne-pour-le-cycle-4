# -*- coding: utf-8 -*-
"""Banc de la fiche papier, au navigateur : chaque séquence imprimée en PDF (A4), séance par séance.

    python3 _outils/impression_papier/banc_papier.py [racine] [--json <fichier>] [--pdf <dossier>] [--ecran <dossier>] [--filtre <texte>]

Pour chaque `sequence*.html` (hors archives) :
  · imprimée comme le fait le navigateur (événement « beforeprint », puis PDF A4) : séance 1 affichée, puis chaque
    autre séance (onglet cliqué) ; nombre de pages de chaque fiche ;
  · en « media: print », à la largeur d'une page A4 : aucun champ d'écran visible (un menu, un bouton, ou un champ, une
    case, un bouton radio qui n'a pas pris son habit de papier),
    aucun texte sous 4,5 : 1 sur un fond clair (un fond en dégradé compte pour la moyenne de ses couleurs), aucun grand
    fond foncé (plus de 30 000 px² : un rectangle d'encre), l'en-tête de la fiche présent, une seule séance imprimée ;
  · dans le PDF : la première page porte autre chose que l'en-tête (une séance renvoyée à la page 2 la laisse vide) ;
  · zéro erreur JavaScript.
`--ecran <dossier>` enregistre une capture pleine page à 1280 px (écran) : deux passages comparés prouvent que l'écran
n'a pas changé. `--pdf <dossier>` garde les PDF. `--json` écrit les mesures. `--filtre <texte>` ne joue que les pages
dont le chemin contient ce texte (pour corriger vite ; la livraison se juge sans filtre).

Sortie 0 / 1 (refus nommés ; seulement pour les pages qui portent la fiche papier) / 2 (aucune séquence lue, n°299).
Ce qu'il NE juge PAS : la beauté d'une fiche (cela se regarde : `--pdf`), la justesse du contenu.
"""
import json
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

args = sys.argv[1:]
def opt(nom):
    if nom in args:
        i = args.index(nom); v = args[i + 1]; del args[i:i + 2]; return v
    return None
SORTIE_JSON, DOSSIER_PDF, DOSSIER_ECRAN, FILTRE = opt("--json"), opt("--pdf"), opt("--ecran"), opt("--filtre")
RACINE = pathlib.Path(args[0] if args else pathlib.Path(__file__).resolve().parents[2]).resolve()
pages = sorted(p for p in RACINE.rglob("sequence*.html") if "_archive-anciennes-versions" not in p.parts
               and (not FILTRE or FILTRE in str(p.relative_to(RACINE))))
if not pages:
    print("⛔ aucune séquence lue sous %s : rien n'a été vérifié" % RACINE); sys.exit(2)
for d in (DOSSIER_PDF, DOSSIER_ECRAN):
    if d: pathlib.Path(d).mkdir(parents=True, exist_ok=True)

MESURE = """() => {
  const lum = s => { const m = /rgba?\\(([\\d.]+),\\s*([\\d.]+),\\s*([\\d.]+)(?:,\\s*([\\d.]+))?\\)/.exec(s || '');
    if (!m || (m[4] !== undefined && +m[4] < .15)) return null;
    const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); };
    return .2126 * f(+m[1]) + .7152 * f(+m[2]) + .0722 * f(+m[3]); };
  const fond = cs => { const g = cs.backgroundImage;
    if (g && /gradient/.test(g)) { const l = (g.match(/rgba?\\([^)]*\\)/g) || []).map(lum).filter(v => v !== null); if (l.length) return l.reduce((a, b) => a + b) / l.length; }
    return lum(cs.backgroundColor); };
  const vu = e => { for (let x = e; x; x = x.parentElement) { const c = getComputedStyle(x); if (c.display === 'none' || c.visibility === 'hidden') return false; } return true; };
  const nom = x => x.tagName.toLowerCase() + (x.id ? '#' + x.id : '') + (typeof x.className === 'string' && x.className.trim() ? '.' + x.className.trim().split(/\\s+/).slice(0, 2).join('.') : '');
  let pales = [], champs = [], sombres = [];
  for (const e of document.querySelectorAll('body *')) {
    if (/^(SCRIPT|STYLE|SVG|PATH|TEXT|TSPAN|G|IMG|CANVAS|NOSCRIPT|OPTION)$/i.test(e.tagName)) continue;
    // un menu ou un bouton imprimé est un champ d'écran ; un champ de texte, une case ou un bouton radio s'imprime habillé
    // pour le papier (appearance:none : des lignes, un trait, un carré, un rond) — sinon, c'est encore l'écran
    if (/^(SELECT|TEXTAREA|INPUT|BUTTON)$/.test(e.tagName)) {
      const cs = getComputedStyle(e);
      // habillé : sans apparence d'écran, et, pour un champ de texte, avec ses lignes (fond rayé) ou son trait (bordure basse)
      const ecrit = e.tagName === 'TEXTAREA' || !/^(radio|checkbox)$/.test(e.type);
      const habille = /^(TEXTAREA|INPUT)$/.test(e.tagName) && cs.appearance === 'none'
        && (!ecrit || (e.tagName === 'TEXTAREA' ? /gradient/.test(cs.backgroundImage) : parseFloat(cs.borderBottomWidth) > 0));
      if (e.type !== 'hidden' && vu(e) && !habille) champs.push(e.tagName.toLowerCase() + (e.id ? '#' + e.id : ''));
      continue; }
    if (!/^(IMG|SVG|CANVAS|VIDEO|OBJECT|PICTURE)$/i.test(e.tagName) && !e.closest('svg')) {
      const r = e.getBoundingClientRect(), v = fond(getComputedStyle(e));
      if (v !== null && v < .25 && r.width * r.height > 30000 && vu(e)) sombres.push(nom(e) + ' ' + Math.round(r.width) + '×' + Math.round(r.height));
    }
    const t = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
    if (t.length < 3 || !vu(e)) continue;
    const c = lum(getComputedStyle(e).color); if (c === null) continue;
    let f = null; for (let x = e; x; x = x.parentElement) { const v = fond(getComputedStyle(x)); if (v !== null) { f = v; break; } }
    if (f === null) f = 1;
    if (f < .4) continue;                                          // fond resté sombre : l'affaire de controle_impression
    const r = (Math.max(c, f) + .05) / (Math.min(c, f) + .05);
    if (r < 4.5) pales.push(t.slice(0, 50) + ' (' + r.toFixed(1) + ')');
  }
  const panneaux = [...document.querySelectorAll('[role=tabpanel]')].filter(vu).length;
  return {pales, champs, sombres, panneaux, entete: !!document.querySelector('.pp-entete') && vu(document.querySelector('.pp-entete')),
          fiche: !!document.querySelector('.pp-entete')};
}"""


def nb_pages(pdf):
    return int(subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])


def mots_page_1(pdf):
    return len(subprocess.run(["pdftotext", "-f", "1", "-l", "1", pdf, "-"], capture_output=True, text=True).stdout.split())

#: L'en-tête et le pied d'une fiche font une trentaine de mots : en dessous de ce seuil, la première page est vide.
PAGE_1_VIDE = 60


resultats, refus = [], []
with sync_playwright() as pw:
    nav = pw.chromium.launch()
    for p in pages:
        nom = str(p.relative_to(RACINE))
        pg = nav.new_page(viewport={"width": 1280, "height": 900}); err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto(p.as_uri()); pg.wait_for_timeout(500)
        # Le papier n'a pas de transitions : sans cela, une couleur d'écran en train de passer à celle d'impression
        # serait mesurée à mi-chemin (fond foncé fantôme).
        pg.add_style_tag(content="*,*::before,*::after{transition:none!important}")
        if DOSSIER_ECRAN:
            pg.screenshot(path=str(pathlib.Path(DOSSIER_ECRAN) / (nom.replace("/", "__") + ".png")), full_page=True)
        onglets = pg.evaluate("[...document.querySelectorAll('[role=tab]')].map(t => t.id).filter(Boolean)") or [None]
        fiches = []
        for k, onglet in enumerate(onglets):
            if onglet and k:
                pg.emulate_media(media="screen"); pg.click("#" + onglet); pg.wait_for_timeout(250)
            pg.evaluate("window.dispatchEvent(new Event('beforeprint'))")
            pg.emulate_media(media="print")                # le PDF et la mesure, tous deux en « media: print »
            fichier = str(pathlib.Path(DOSSIER_PDF or "/tmp") / (nom.replace("/", "__") + "__s%d.pdf" % (k + 1)))
            pg.pdf(path=fichier, format="A4", print_background=True, prefer_css_page_size=True)
            pg.set_viewport_size({"width": 794, "height": 1123})   # la largeur d'une page A4, pour mesurer
            m = pg.evaluate(MESURE)
            pg.set_viewport_size({"width": 1280, "height": 900})
            n, mots = nb_pages(fichier), mots_page_1(fichier)
            fiches.append({"seance": k + 1, "pages": n, "mots_page_1": mots, "pales": len(m["pales"]), "exemples_pales": m["pales"][:4],
                           "champs": m["champs"][:6], "nb_champs": len(m["champs"]), "sombres": m["sombres"][:4],
                           "panneaux": m["panneaux"], "entete": m["entete"]})
            if m["fiche"]:
                if m["champs"]: refus.append("%s séance %d — %d champ(s) d'écran imprimé(s) : %s" % (nom, k + 1, len(m["champs"]), ", ".join(m["champs"][:4])))
                if m["pales"]: refus.append("%s séance %d — %d texte(s) trop pâle(s) : %s" % (nom, k + 1, len(m["pales"]), " | ".join(m["pales"][:3])))
                if m["sombres"]: refus.append("%s séance %d — %d grand(s) fond(s) foncé(s) imprimé(s) : %s" % (nom, k + 1, len(m["sombres"]), " | ".join(m["sombres"][:3])))
                if n > 1 and mots < PAGE_1_VIDE: refus.append("%s séance %d — première page presque vide (%d mots) : la suite part à la page 2" % (nom, k + 1, mots))
                if not m["entete"]: refus.append("%s séance %d — pas d'en-tête de fiche" % (nom, k + 1))
                if onglet and m["panneaux"] != 1: refus.append("%s séance %d — %d séances imprimées au lieu d'une" % (nom, k + 1, m["panneaux"]))
        if err: refus.append("%s — erreur JavaScript : %s" % (nom, err[0][:120]))
        resultats.append({"page": nom, "fiches": fiches, "erreurs": err[:2]})
        pg.close()
    nav.close()

if SORTIE_JSON:
    pathlib.Path(SORTIE_JSON).write_text(json.dumps(resultats, ensure_ascii=False, indent=1), encoding="utf-8")
tot = sum(f["pages"] for r in resultats for f in r["fiches"])
s1 = sum(r["fiches"][0]["pages"] for r in resultats)
print("%d séquence(s) · %d fiche(s) imprimée(s) · %d pages en tout · %d pages pour la première fiche de chaque séquence"
      % (len(resultats), sum(len(r["fiches"]) for r in resultats), tot, s1))
print("textes trop pâles : %d · champs d'écran imprimés : %d · grands fonds foncés : %d · premières pages presque vides : %d" % (
    sum(f["pales"] for r in resultats for f in r["fiches"]), sum(f["nb_champs"] for r in resultats for f in r["fiches"]),
    sum(len(f["sombres"]) for r in resultats for f in r["fiches"]),
    sum(1 for r in resultats for f in r["fiches"] if f["pages"] > 1 and f["mots_page_1"] < PAGE_1_VIDE)))
for x in refus[:60]:
    print("  ✘ " + x)
if len(refus) > 60:
    print("  … et %d autre(s)" % (len(refus) - 60))
if refus:
    sys.exit(1)
print("✅ chaque séquence s'imprime en fiche papier : en-tête, une séance, aucun champ d'écran, aucun texte pâle, aucun grand"
      " fond foncé, une première page remplie")
