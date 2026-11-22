# -*- coding: utf-8 -*-
"""Règle d'or n°360 — les tests jouent l'élève qui ne lit pas.

Un élève qui ne lit pas choisit toujours la proposition la plus longue, ou la plus courte, ou toujours la même place,
ou au hasard. Aucune de ces stratégies ne doit valider une activité (audit de l'entraînement DNB, 21/11/2026 : la plus
longue validait la manche 4 entière).

    python3 _outils/eleve_qui_ne_lit_pas.py <page.html> [<page.html> …]
    python3 _outils/eleve_qui_ne_lit_pas.py --tout          (toutes les pages des trois thèmes qui ont `const CHECKS`)

Ce que l'outil lit : les groupes de boutons radio placés dans un `<fieldset>` (n°300), et les fonctions `CHECKS[n]()`
du gabarit commun (bouton `[data-check="n"]`, retour `{score, total, valide}`). Pour chaque stratégie, il coche une
proposition dans chaque groupe, appelle chaque fonction de vérification et compte les activités validées. Quand
`CHECKS` est enfermé dans une fonction (pages du thème 3), il appuie sur chaque bouton « Vérifier » et lit la classe
`ok` du retour `#fb<n>` ; une activité fermée par un verrou d'expérience (retour qui commence par 🔒) est dite « non mesurée ».

Une activité validée par les huit stratégies à la fois ne dépend pas de la justesse des réponses (un billet d'entrée
« fait dès qu'il est répondu ») : elle n'est pas comptée en faute, elle est listée à part.

Ce qu'il ne lit pas (n°47) : les listes déroulantes, les champs à écrire, les simulateurs. Une activité qui en demande
aussi ne peut pas être validée par les seuls boutons radio ; elle est comptée, et signalée « mixte ».

Sortie : 0 aucune stratégie ne valide · 1 au moins une validation · 2 rien n'a été lu (Playwright absent, ou aucune
page avec `CHECKS` et des groupes radio) — règle n°299.

Réutilisable dans un banc : `from eleve_qui_ne_lit_pas import mesurer` puis `mesurer(page)` sur une page Playwright
déjà chargée (contexte neuf conseillé : l'outil coche des réponses).
"""
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
THEMES = ("theme-1-objets-systemes-usages-interactions", "theme-2-structure-fonctionnement-comportement",
          "theme-3-creation-conception-realisation-innovations")

STRATEGIES = ["la plus longue", "la plus courte", "toujours la 1re", "toujours la 2e", "toujours la 3e",
              "toujours la 4e", "au hasard (graine 2026)", "au hasard (graine 360)"]

JS_MESURER = r"""
(strategie) => {
  const accessible = (typeof CHECKS !== "undefined");
  const boutons = [...document.querySelectorAll("[data-check]")];
  if (!accessible && !boutons.length) return {lu: false, raison: "ni CHECKS ni bouton [data-check]"};
  const groupes = {};
  document.querySelectorAll("fieldset input[type=radio]").forEach(r => { (groupes[r.name] = groupes[r.name] || []).push(r); });
  const noms = Object.keys(groupes);
  if (!noms.length) return {lu: false, raison: "aucun groupe radio dans un fieldset"};
  let graine = strategie.includes("2026") ? 2026 : 360;
  const hasard = () => { graine = (graine * 1103515245 + 12345) % 2147483648; return graine / 2147483648; };
  const texte = r => { const l = r.id && document.querySelector('label[for="' + r.id + '"]');
                       return ((l && l.textContent) || r.value || "").trim(); };
  noms.forEach(n => groupes[n].forEach(r => { r.checked = false; }));
  for (const n of noms) {
    const rs = groupes[n], t = rs.map(texte);
    let k = 0;
    if (strategie === "la plus longue") k = t.reduce((m, x, i) => x.length > t[m].length ? i : m, 0);
    else if (strategie === "la plus courte") k = t.reduce((m, x, i) => x.length < t[m].length ? i : m, 0);
    else if (strategie.startsWith("toujours la ")) k = Math.min(parseInt(strategie.slice(12)) - 1, rs.length - 1);
    else k = Math.floor(hasard() * rs.length);
    rs[k].checked = true;
    rs[k].dispatchEvent(new Event("change", {bubbles: true}));
    rs[k].dispatchEvent(new Event("input", {bubbles: true}));
  }
  const res = {};
  if (accessible) {
    for (const n of Object.keys(CHECKS)) {
      try { const r = CHECKS[n](); res[n] = {score: r.score, total: r.total, valide: !!r.valide}; }
      catch (e) { res[n] = {erreur: String(e).slice(0, 120)}; }
    }
    return {lu: true, mode: "CHECKS", groupes: noms.length, resultats: res};
  }
  // CHECKS enfermé dans une fonction (thème 3) : on appuie sur « Vérifier » et on lit le retour #fb<n>
  for (const b of boutons) {
    const n = b.dataset.check, fb = document.getElementById("fb" + n);
    try { b.click(); } catch (e) { res[n] = {erreur: String(e).slice(0, 120)}; continue; }
    const c = fb ? " " + fb.className + " " : "";
    // « warn » sert au 🟡 (score partiel) comme au 🔒 (verrou d'expérience) : seul le cadenas dit le verrou
    res[n] = {valide: / ok /.test(c), verrou: !!fb && fb.textContent.trim().startsWith("🔒"), lu: !!fb};
  }
  return {lu: true, mode: "boutons", groupes: noms.length, resultats: res};
}
"""


def mesurer(pg):
    """Joue chaque stratégie sur la page chargée. Renvoie {"lu", "groupes", "par_strategie": {stratégie: {n: {...}}},
    "validations": [(stratégie, n)]}."""
    sortie = {"lu": False, "groupes": 0, "par_strategie": {}, "validations": []}
    for s in STRATEGIES:
        r = pg.evaluate(JS_MESURER, s)
        if not r.get("lu"):
            sortie["raison"] = r.get("raison")
            return sortie
        sortie["lu"] = True
        sortie["groupes"] = r["groupes"]
        sortie["mode"] = r.get("mode")
        sortie["verrous"] = sorted(n for n, v in r["resultats"].items() if v.get("verrou"))
        sortie["par_strategie"][s] = r["resultats"]
        sortie["validations"] += [(s, n) for n, v in r["resultats"].items() if v.get("valide")]
    # une activité validée par TOUTES les stratégies ne dépend pas de la justesse : billet d'entrée, positionnement
    # (« fait dès qu'il est répondu »). Elle n'est pas comptée en faute, mais listée : la page doit le dire (n°340).
    par_n = {}
    for s, n in sortie["validations"]:
        par_n.setdefault(n, []).append(s)
    sortie["a_la_completion"] = sorted(n for n, ss in par_n.items() if len(ss) == len(STRATEGIES))
    sortie["validations"] = [(s, n) for s, n in sortie["validations"] if n not in sortie["a_la_completion"]]
    return sortie


def pages_tout():
    for th in THEMES:
        for p in sorted((RACINE / th).rglob("*.html")):
            try:
                if "const CHECKS" in p.read_text(encoding="utf-8", errors="ignore"):
                    yield p
            except OSError:
                pass


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
    lues, fautives = 0, 0
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for page in pages:
            ctx = nav.new_context()
            pg = ctx.new_page()
            erreurs = []
            pg.on("pageerror", lambda e: erreurs.append(str(e)))
            try:
                pg.goto(page.resolve().as_uri())
                pg.wait_for_timeout(300)
                m = mesurer(pg)
            except Exception as e:  # une page qui casse ne doit pas arrêter le balayage
                m = {"lu": False, "raison": "page illisible : " + str(e)[:80]}
            ctx.close()
            nom = page.resolve().relative_to(RACINE) if RACINE in page.resolve().parents else page
            if not m["lu"]:
                print(f"○ {nom} — rien lu ({m.get('raison')})")
                continue
            lues += 1
            if m["validations"]:
                fautives += 1
                detail = ", ".join(f"activité {n} par « {s} »" for s, n in m["validations"][:6])
                print(f"✘ {nom} — {len(m['validations'])} validation(s) sans lire : {detail}")
            else:
                print(f"✔ {nom} — {m['groupes']} groupes radio, {len(STRATEGIES)} stratégies : aucune activité validée")
            if m.get("verrous"):
                print(f"   ○ activité(s) {', '.join(m['verrous'])} fermée(s) par un verrou d'expérience : "
                      "non mesurée(s) sans le geste")
            if m.get("a_la_completion"):
                print(f"   ○ activité(s) {', '.join(m['a_la_completion'])} validée(s) quelle que soit la réponse "
                      "(billet d'entrée, positionnement ?) : vérifier que la page le dit")
        nav.close()
    print(f"\n{lues} page(s) lue(s), {fautives} validée(s) par un élève qui ne lit pas.")
    if lues == 0:
        print("Rien n'a été lu : ce contrôle n'a rien vérifié (n°299).")
        return 2
    return 1 if fautives else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
