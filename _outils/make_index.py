# -*- coding: utf-8 -*-
"""Génère index.html (navigation GitHub Pages) + README.md racine pour le repo réorganisé."""
import os, re, sys, unicodedata, html, json
sys.path.insert(0, os.path.dirname(__file__))
from data_competences import COMP_BY_LEVEL, C_PARENT, THEME_TITLES

DST = os.path.join(os.path.dirname(__file__), "..")  # racine du dépôt
PAGES_BASE = "https://pll-process.github.io/en-ligne-pour-le-cycle-4"

THEME_SLUG = {
    1: "theme-1-objets-systemes-usages-interactions",
    2: "theme-2-structure-fonctionnement-comportement",
    3: "theme-3-creation-conception-realisation-innovations",
}
THEME_EMOJI = {1: "🔍", 2: "⚙️", 3: "🛠️"}
THEME_COLOR = {1: "#61dafb", 2: "#ffb454", 3: "#81fba1"}
NIVEAU_COLOR = {"5e": "#8fd18f", "4e": "#7db3f0", "3e": "#f0a878"}


# ----------------------------------------------------------------- nouveautés (badge NEW)
# Source : nouveautes.json à la racine. Le badge est posé côté client (JS embarqué) :
# il apparaît si la date de publication est atteinte et disparaît automatiquement
# après duree_jours (21 par défaut), sans regénération manuelle.
NOUVEAUTES_PATH = os.path.join(os.path.dirname(__file__), "..", "nouveautes.json")
try:
    with open(NOUVEAUTES_PATH, encoding="utf-8") as _f:
        _nv = json.load(_f)
    NOUVEAUTES = _nv.get("entrees", [])
    NV_DUREE_DEFAUT = _nv.get("config", {}).get("duree_jours_defaut", 21)
except FileNotFoundError:
    NOUVEAUTES, NV_DUREE_DEFAUT = [], 21


def slugify(s, maxlen=45):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    parts, out, total = s.split("-"), [], 0
    for p in parts:
        if total + len(p) + 1 > maxlen and out:
            break
        out.append(p); total += len(p) + 1
    return "-".join(out)


def code_dir(cnum, niveau, code):
    text, _, theme = C_PARENT[cnum]
    return os.path.join(THEME_SLUG[theme], f"{cnum}-{slugify(text)}", niveau, f"{niveau}_{code}")


def content_files(rel_dir):
    """Fichiers de contenu réel (hors .gitkeep) directement dans le dossier code."""
    full = os.path.join(DST, rel_dir)
    if not os.path.isdir(full):
        return []
    out = []
    for fn in sorted(os.listdir(full)):
        p = os.path.join(full, fn)
        if os.path.isfile(p) and fn != ".gitkeep":
            out.append(fn)
    return out


# ---------------------------------------------------------------- index.html
parts = []
parts.append("""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Technologie Cycle 4 (2024) — En ligne pour le cycle 4</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#050f24;--panel:#0d2347;--panel2:#0a1b3d;--border:#274a8a;--title:#81aaff;--sub:#9bbefc;--head:#c68ef2;--text:#e4eaf5;--hl:#61dafb}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:'Poppins',sans-serif;margin:0;padding:0 18px 60px;line-height:1.5}
h1{text-align:center;color:var(--title);font-size:1.9em;margin:30px 0 4px}
.sub{text-align:center;color:var(--sub);margin-bottom:8px}
.note{max-width:880px;margin:0 auto 26px;text-align:center;color:#7d9bd6;font-size:.85em}
.legend{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-bottom:26px;font-size:.82em}
.legend span{display:inline-flex;align-items:center;gap:6px}
.dot{width:10px;height:10px;border-radius:50%;display:inline-block}
.theme{max-width:1080px;margin:0 auto 30px;background:var(--panel);border:1px solid var(--border);border-radius:16px;overflow:hidden}
.theme>header{padding:16px 22px;font-weight:700;font-size:1.08em;border-bottom:1px solid var(--border)}
.comp{border-bottom:1px solid rgba(39,74,138,.5)}
.comp:last-child{border-bottom:none}
.comp>summary{cursor:pointer;padding:13px 22px;font-weight:600;color:var(--text);list-style:none;display:flex;gap:10px;align-items:baseline}
.comp>summary::-webkit-details-marker{display:none}
.comp>summary:hover{background:var(--panel2)}
.comp>summary .cnum{color:var(--head);font-weight:700;min-width:34px}
.comp>summary>span:nth-child(2){min-width:0;overflow-wrap:anywhere}
.comp>summary .count{margin-left:auto;font-size:.75em;color:var(--hl);white-space:nowrap}
.levels{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;padding:6px 22px 20px}
@media(max-width:980px){.levels{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:680px){body{padding-left:8px;padding-right:8px}.levels{grid-template-columns:1fr;padding:6px 10px 16px}.comp>summary{padding:12px 10px;align-items:flex-start;flex-wrap:wrap}.comp>summary .count{width:100%;margin-left:44px}}
.lvl{background:var(--panel2);border:1px solid var(--border);border-radius:12px;padding:12px 14px;min-width:0;overflow:hidden}
.lvl h4{margin:0 0 8px;font-size:.9em}
.code-line{display:grid;grid-template-columns:minmax(64px,auto) minmax(0,1fr);gap:8px;align-items:start;padding:5px 0;border-bottom:1px dashed rgba(39,74,138,.55);font-size:.8em;min-width:0}
.code-line:last-child{border-bottom:none}
.code-line .cc{font-weight:700;white-space:nowrap;min-width:64px}
.code-line>span:last-child{min-width:0;overflow-wrap:anywhere;word-break:break-word}
.code-line a{color:var(--hl);text-decoration:none;overflow-wrap:anywhere;word-break:break-word}
.code-line a:hover{text-decoration:underline}
.code-line .empty{color:#5b7bb8}
.pill{font-size:.85em}
footer{max-width:1080px;margin:34px auto 0;text-align:center;color:#5b7bb8;font-size:.8em}
footer a{color:var(--hl)}
/* ── badge NEW (règle obligatoire — nouveautes.json) ── */
.badge-new{display:inline-block;background:linear-gradient(90deg,#ff7b88,#ffb454);color:#111;font-weight:700;font-size:.68em;padding:2px 8px;border-radius:999px;margin-left:6px;letter-spacing:.5px;vertical-align:middle;animation:nvpulse 2.2s ease-in-out infinite}
@keyframes nvpulse{0%,100%{opacity:1}50%{opacity:.62}}
@media (prefers-reduced-motion: reduce){.badge-new{animation:none}}
@media print{.badge-new{animation:none;background:#fff;border:1.5px solid #111;color:#111}}
.code-line.nv-cible{background:rgba(255,180,84,.1);border-radius:8px;outline:1px solid rgba(255,180,84,.45)}
.code-line{scroll-margin-top:14px}
</style>
</head>
<body>
<h1>🎓 Technologie — Cycle 4 (programme 2024)</h1>
<p class="sub">Séquences, QCM et ressources classés par <strong>Thème → Compétence → Niveau → Code</strong></p>
<p class="note">Codage : <code>5e_C1.1</code> = sous-compétence C1.1 du cahier Nathan 5e — chaque niveau (5e/4e/3e) décline différemment les 9 compétences C1-C9 du BO n°9 du 29/02/2024.</p>
<div class="legend">
  <span><span class="dot" style="background:#8fd18f"></span>5e</span>
  <span><span class="dot" style="background:#7db3f0"></span>4e</span>
  <span><span class="dot" style="background:#f0a878"></span>3e</span>
  <span>📄 = ressource disponible</span>
  <span style="color:#5b7bb8">— = à créer</span>
</div>
""")

total_content = 0
for theme_n in [1, 2, 3]:
    parts.append(f'<div class="theme" id="theme-{theme_n}"><header style="color:{THEME_COLOR[theme_n]}">{THEME_EMOJI[theme_n]} Thème {theme_n} — {html.escape(THEME_TITLES[theme_n])}<span class="nv-theme-slot" data-theme="{theme_n}"></span></header>')
    for cnum in [f"C{i}" for i in range(1, 10)]:
        text, _, t = C_PARENT[cnum]
        if t != theme_n:
            continue
        # count content in this competence
        n_files = 0
        lvl_html = []
        for niveau in ["5e", "4e", "3e"]:
            lines = []
            for code, ctext, _ in COMP_BY_LEVEL[niveau][cnum]:
                rel = code_dir(cnum, niveau, code)
                files = content_files(rel)
                full_code = f"{niveau}_{code}"
                if files:
                    n_files += len([f for f in files if f != "README.md"]) or 1
                    links = " · ".join(
                        f'<a href="{html.escape(rel)}/{html.escape(fn)}">📄 {html.escape(fn if len(fn) <= 34 else fn[:31] + "…")}</a>'
                        for fn in files
                    )
                    lines.append(f'<div class="code-line" id="{full_code}"><span class="cc" style="color:{NIVEAU_COLOR[niveau]}">{full_code}</span><span>{links}</span></div>')
                else:
                    lines.append(f'<div class="code-line" id="{full_code}"><span class="cc" style="color:{NIVEAU_COLOR[niveau]}">{full_code}</span><span class="empty">—</span></div>')
            lvl_html.append(f'<div class="lvl"><h4 style="color:{NIVEAU_COLOR[niveau]}">{niveau}</h4>{"".join(lines)}</div>')
        total_content += n_files
        count_label = f"{n_files} ressource(s)" if n_files else "à compléter"
        parts.append(
            f'<details class="comp" id="comp-{cnum}"><summary><span class="cnum">{cnum}</span>'
            f'<span>{html.escape(text if len(text) <= 110 else text[:107] + "…")}<span class="nv-comp-slot" data-comp="{cnum}"></span></span>'
            f'<span class="count">{count_label}</span></summary>'
            f'<div class="levels">{"".join(lvl_html)}</div></details>'
        )
    parts.append("</div>")

parts.append(f"""<footer>
<p>📦 <a href="_ressources-communes/">Ressources communes</a> · 🗄️ <a href="_archive-anciennes-versions/">Archive des anciennes versions</a> · <a href="RAPPORT_MIGRATION.md">Rapport de migration</a></p>
<p>Référentiel : BO n°9 du 29/02/2024 · Cahiers Nathan 5e/4e/3e (éd. 2024) · Structure générée depuis le classeur <em>Référentiel_Technologie_Cycle4_2024.xlsx</em></p>
</footer>
<script>
/* ── Badges NEW automatiques (source : nouveautes.json, embarqué à la génération) ── */
"use strict";
const NOUVEAUTES = {json.dumps(NOUVEAUTES, ensure_ascii=False)};
const NV_DUREE_DEFAUT = {NV_DUREE_DEFAUT};
(function(){{
  const jour = 24*3600*1000;
  const actives = NOUVEAUTES.filter(e => {{
    const pub = new Date(e.date_publication + "T00:00:00");
    if (isNaN(pub) || Date.now() < pub.getTime()) return false;
    const duree = (e.duree_jours || NV_DUREE_DEFAUT) * jour;
    return Date.now() <= pub.getTime() + duree;
  }});
  if (!actives.length) return;
  function badge() {{
    const b = document.createElement("span");
    b.className = "badge-new";
    b.innerHTML = 'NEW<span class="sr-only" style="position:absolute;left:-9999px">— Nouveau</span>';
    return b;
  }}
  const themesVus = new Set(), compsVus = new Set();
  actives.forEach(e => {{
    const ligne = document.getElementById(e.code);
    if (ligne) {{
      const cc = ligne.querySelector(".cc");
      if (cc && !cc.querySelector(".badge-new")) cc.appendChild(badge());
      /* mise en évidence des liens séquence/QCM nouveaux */
      ligne.querySelectorAll("a").forEach(a => {{
        const fichier = (a.getAttribute("href") || "").split("/").pop();
        const seq = (e.sequence || "").split("/").pop(), q = (e.qcm || "").split("/").pop();
        if ((fichier === seq || fichier === q) && !a.parentElement.querySelector(".badge-new-l-" + CSS.escape(fichier)))
          a.insertAdjacentElement("afterend", badge());
      }});
    }}
    if (e.competence && !compsVus.has(e.competence)) {{
      compsVus.add(e.competence);
      const slot = document.querySelector('.nv-comp-slot[data-comp="' + e.competence + '"]');
      if (slot) slot.appendChild(badge());
    }}
    if (e.theme && !themesVus.has(e.theme)) {{
      themesVus.add(e.theme);
      const slot = document.querySelector('.nv-theme-slot[data-theme="' + e.theme + '"]');
      if (slot) slot.appendChild(badge());
    }}
  }});
}})();
/* ── Ancres directes : #3e_C4.3 ouvre la compétence et défile jusqu'au code ── */
(function(){{
  function ouvrir() {{
    const h = decodeURIComponent(location.hash.replace("#", ""));
    if (!h) return;
    const cible = document.getElementById(h);
    if (!cible || !cible.classList.contains("code-line")) return;
    const det = cible.closest("details.comp");
    if (det) det.open = true;
    cible.classList.add("nv-cible");
    const reduit = matchMedia("(prefers-reduced-motion: reduce)").matches;
    setTimeout(() => cible.scrollIntoView({{behavior: reduit ? "auto" : "smooth", block: "center"}}), 60);
  }}
  window.addEventListener("hashchange", ouvrir);
  ouvrir();
}})();
</script>
</body>
</html>
""")

with open(os.path.join(DST, "index.html"), "w", encoding="utf-8") as f:
    f.write("".join(parts))
print("index.html généré —", total_content, "entrées de contenu référencées")

# ---------------------------------------------------------------- README.md
readme = f"""# 🎓 En ligne pour le cycle 4 — Technologie (programme 2024)

Séquences, QCM et ressources de **technologie collège (cycle 4)**, classés selon le
**programme 2024** (BO n°9 du 29 février 2024) et les cahiers **Nathan 5e / 4e / 3e (éd. 2024)**.

👉 **Navigation en ligne : [{PAGES_BASE}]({PAGES_BASE}/)** (page d'accueil interactive)

## 🗂️ Organisation

```text
theme-1-objets-systemes-usages-interactions/        🔍 Thème 1
theme-2-structure-fonctionnement-comportement/      ⚙️ Thème 2
theme-3-creation-conception-realisation-innovations/ 🛠️ Thème 3
└── C4-decrire-et-caracteriser-lorganisation/        ← compétence (C1 à C9)
    └── 4e/                                          ← niveau (5e, 4e, 3e)
        └── 4e_C6.2/                                 ← code (sous-compétence Nathan)
            ├── Images/        ← illustrations de la séquence
            ├── Synthèses/     ← traces écrites « à retenir »
            └── *.html …       ← séances, QCM, fichiers élève
_ressources-communes/       📦 images et documents transversaux
_archive-anciennes-versions/ 🗄️ anciennes versions conservées (rien n'est perdu)
```

### Pourquoi des codes préfixés (`5e_C1.1`, `4e_C1.1`, `3e_C1.1`) ?

Nathan publie un cahier par niveau ; dans chacun, la numérotation `C1.1 → C9.3` repart de zéro.
Un même code désigne donc **trois sous-compétences différentes** selon le niveau. Le préfixe lève
l'ambiguïté et suit la logique du programme officiel : chaque compétence C1-C9 est décomposée
**pour chacune des trois classes** du cycle (114 sous-compétences au total : 38 par niveau).

## 📅 Calendrier du programme 2024

| Niveau | Programme 2024 applicable depuis |
|--------|----------------------------------|
| 5e     | rentrée 2024-2025 ✅ |
| 4e     | rentrée 2025-2026 ✅ |
| 3e     | **rentrée 2026-2027** (la prochaine !) |

## 🧭 Construire une nouvelle séquence

Le gabarit de référence (situation déclenchante → problématique → compétences du référentiel →
domaines du socle → séances → synthèse → évaluation LSU → différenciation) est illustré par la
séquence 🌱 **[Jardin connecté — 4e_C6.2](theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html)** ·
inspirations : fiches [Édubase Technologie — programme 2024](https://edubase.eduscol.education.fr/recherche?discipline%5B0%5D=Technologie&keywords%5B0%5D=Techno%20-%20Programme%202024).

## 🔎 Référentiel source

La structure de ce dépôt est générée depuis l'onglet **« Référentiel C1-C9 »** du classeur
`Référentiel_Technologie_Cycle4_2024.xlsx` (9 compétences × 3 niveaux, domaines du socle,
CRCN, grille LSU). Voir aussi le [rapport de migration](RAPPORT_MIGRATION.md).
"""
with open(os.path.join(DST, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)
print("README.md racine généré")
