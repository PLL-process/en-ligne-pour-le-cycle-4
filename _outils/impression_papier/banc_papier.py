# -*- coding: utf-8 -*-
"""Banc de la fiche papier, au navigateur : chaque séquence imprimée en PDF (A4), séance par séance.

    python3 _outils/impression_papier/banc_papier.py [racine] [--json <fichier>] [--pdf <dossier>] [--ecran <dossier>]

Pour chaque `sequence*.html` (hors archives) :
  · imprimée comme le fait le navigateur (événement « beforeprint », puis PDF A4) : séance 1 affichée, puis chaque
    autre séance (onglet cliqué) ; nombre de pages de chaque fiche ;
  · en « media: print » : aucun champ d'écran visible (menu, case, champ de texte, bouton), aucun texte sous 4,5 : 1 sur
    un fond clair, l'en-tête de la fiche présent, une seule séance imprimée ;
  · zéro erreur JavaScript.
`--ecran <dossier>` enregistre une capture pleine page à 1280 px (écran) : deux passages comparés prouvent que l'écran
n'a pas changé. `--pdf <dossier>` garde les PDF. `--json` écrit les mesures.

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
SORTIE_JSON, DOSSIER_PDF, DOSSIER_ECRAN = opt("--json"), opt("--pdf"), opt("--ecran")
RACINE = pathlib.Path(args[0] if args else pathlib.Path(__file__).resolve().parents[2]).resolve()
pages = sorted(p for p in RACINE.rglob("sequence*.html") if "_archive-anciennes-versions" not in p.parts)
if not pages:
    print("⛔ aucune séquence lue sous %s : rien n'a été vérifié" % RACINE); sys.exit(2)
for d in (DOSSIER_PDF, DOSSIER_ECRAN):
    if d: pathlib.Path(d).mkdir(parents=True, exist_ok=True)

MESURE = """() => {
  const lum = s => { const m = /rgba?\\(([\\d.]+),\\s*([\\d.]+),\\s*([\\d.]+)(?:,\\s*([\\d.]+))?\\)/.exec(s || '');
    if (!m || (m[4] !== undefined && +m[4] < .15)) return null;
    const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); };
    return .2126 * f(+m[1]) + .7152 * f(+m[2]) + .0722 * f(+m[3]); };
  const vu = e => { for (let x = e; x; x = x.parentElement) { const c = getComputedStyle(x); if (c.display === 'none' || c.visibility === 'hidden') return false; } return true; };
  let pales = [], champs = [];
  for (const e of document.querySelectorAll('body *')) {
    if (/^(SCRIPT|STYLE|SVG|PATH|TEXT|TSPAN|G|IMG|CANVAS|NOSCRIPT|OPTION)$/i.test(e.tagName)) continue;
    if (/^(SELECT|TEXTAREA|INPUT|BUTTON)$/.test(e.tagName)) { if (e.type !== 'hidden' && vu(e)) champs.push(e.tagName.toLowerCase() + (e.id ? '#' + e.id : '')); continue; }
    const t = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
    if (t.length < 3 || !vu(e)) continue;
    const c = lum(getComputedStyle(e).color); if (c === null) continue;
    let f = null; for (let x = e; x; x = x.parentElement) { const v = lum(getComputedStyle(x).backgroundColor); if (v !== null) { f = v; break; } }
    if (f === null) f = 1;
    if (f < .4) continue;                                          // fond resté sombre : l'affaire de controle_impression
    const r = (Math.max(c, f) + .05) / (Math.min(c, f) + .05);
    if (r < 4.5) pales.push(t.slice(0, 50) + ' (' + r.toFixed(1) + ')');
  }
  const panneaux = [...document.querySelectorAll('[role=tabpanel]')].filter(vu).length;
  return {pales, champs, panneaux, entete: !!document.querySelector('.pp-entete') && vu(document.querySelector('.pp-entete')),
          fiche: !!document.querySelector('.pp-entete')};
}"""


def nb_pages(pdf):
    return int(subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])


resultats, refus = [], []
with sync_playwright() as pw:
    nav = pw.chromium.launch()
    for p in pages:
        nom = str(p.relative_to(RACINE))
        pg = nav.new_page(viewport={"width": 1280, "height": 900}); err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto(p.as_uri()); pg.wait_for_timeout(500)
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
            m = pg.evaluate(MESURE)
            fiches.append({"seance": k + 1, "pages": nb_pages(fichier), "pales": len(m["pales"]), "exemples_pales": m["pales"][:4],
                           "champs": m["champs"][:6], "nb_champs": len(m["champs"]), "panneaux": m["panneaux"], "entete": m["entete"]})
            if m["fiche"]:
                if m["champs"]: refus.append("%s séance %d — %d champ(s) d'écran imprimé(s) : %s" % (nom, k + 1, len(m["champs"]), ", ".join(m["champs"][:4])))
                if m["pales"]: refus.append("%s séance %d — %d texte(s) trop pâle(s) : %s" % (nom, k + 1, len(m["pales"]), " | ".join(m["pales"][:3])))
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
print("textes trop pâles : %d · champs d'écran imprimés : %d" % (sum(f["pales"] for r in resultats for f in r["fiches"]),
                                                               sum(f["nb_champs"] for r in resultats for f in r["fiches"])))
for x in refus[:60]:
    print("  ✘ " + x)
if len(refus) > 60:
    print("  … et %d autre(s)" % (len(refus) - 60))
if refus:
    sys.exit(1)
print("✅ chaque séquence s'imprime en fiche papier : en-tête, une séance, aucun champ d'écran, aucun texte pâle")
