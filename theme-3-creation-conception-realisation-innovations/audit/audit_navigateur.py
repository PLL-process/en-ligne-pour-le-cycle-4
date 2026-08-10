# -*- coding: utf-8 -*-
"""Ouvre CHAQUE page du dépôt dans un vrai navigateur et rapporte ce qui casse.

Un script qui lit le HTML ne voit pas : une erreur de syntaxe JavaScript qui
tue toute l'interactivité, une image injectée par le code, un lien mort calculé
à l'exécution. Le navigateur, si. C'est le contrôle qui manquait — et c'est
lui qui a trouvé les défauts les plus graves.

    python3 theme-3-.../audit/audit_navigateur.py > RAPPORT_NAVIGATEUR.md

Nécessite Playwright et Chromium.
"""
import asyncio, re, sys
from pathlib import Path
from playwright.async_api import async_playwright

R = Path(".").resolve()
IGNORE = ("_archive-anciennes-versions", "node_modules", ".git")
# Un GABARIT n'est pas une page : il contient des emplacements (@@CHECKS@@)
# que le générateur remplira. Le juger comme une page produit de faux défauts.
EXEMPTES = ("dnb_gabarit.html", "vittascience_embed.html", "tp_modele_demonstration.html")

def pages():
    for p in sorted(R.rglob("*.html")):
        if any(i in str(p) for i in IGNORE) or p.name in EXEMPTES or "gabarit" in p.name:
            continue
        yield p

async def examiner(pg, f):
    erreurs, reseau = [], set()
    pg.on("pageerror", lambda e: erreurs.append(str(e)))
    pg.on("console", lambda m: erreurs.append("console: " + m.text) if m.type == "error" else None)
    pg.on("request", lambda r: reseau.add(r.url.split("/")[2]) if r.url.startswith("http") else None)
    try:
        await pg.goto(f.as_uri(), timeout=15000)
    except Exception as e:
        return {"charge": False, "erreurs": [str(e)[:120]], "images": [], "reseau": []}
    await pg.wait_for_timeout(250)
    await pg.evaluate("()=>window.scrollTo(0, document.body.scrollHeight)")
    await pg.wait_for_timeout(600)
    await pg.evaluate("()=>window.scrollTo(0, 0)")
    imgs = await pg.evaluate(
        "()=>[...document.images]"
        ".filter(i=>i.getAttribute('src'))"   # un <img> sans src attend son contenu
        ".filter(i=>!i.complete||i.naturalWidth===0)"
        ".map(i=>i.getAttribute('src')).slice(0,5)")
    return {"charge": True, "erreurs": erreurs[:3], "images": imgs, "reseau": sorted(reseau)}

async def main():
    liste = list(pages())
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for f in liste:
            pg = await b.new_page()
            res[f] = await examiner(pg, f)
            await pg.close()
        await b.close()

    casses = {f: r for f, r in res.items() if r["erreurs"] or r["images"] or not r["charge"]}
    print("# Audit au navigateur — ce que la lecture du code ne montre pas\n")
    print("*Chaque page ouverte dans Chromium, erreurs JavaScript et images en échec relevées.*\n")
    print("**%d pages ouvertes · %d présentent un défaut.**\n" % (len(liste), len(casses)))
    if not casses:
        print("Aucune page ne produit d'erreur ni d'image cassée.\n")
    for f, r in casses.items():
        print("### `%s`\n" % f.relative_to(R))
        for e in r["erreurs"]:
            print("- **JavaScript** : %s" % e[:160])
        for i in r["images"]:
            print("- **Image absente** : `%s`" % i)
        if not r["charge"]:
            print("- **La page ne s'ouvre pas.**")
        print()
    print("---\n\n## Périmètre\n")
    print("**Vérifié** : la page s'ouvre, son JavaScript s'exécute sans erreur au chargement,")
    print("toutes ses images se chargent réellement.\n")
    print("**NON couvert** : ce qui ne casse qu'après une interaction précise, la justesse des")
    print("réponses, et le fait que la page enseigne quelque chose. Un script sans erreur peut")
    print("être un script qui ne fait rien.")

asyncio.run(main())
