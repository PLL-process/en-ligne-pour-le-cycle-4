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

# ── Ressources héritées (règle d'or n°12) : badge 🛠 « modernisation prévue ».
# Source : _outils/heritees.json. Une entrée se retire quand le remplaçant est
# livré et l'ancienne version archivée dans _archive-anciennes-versions/.
HERITEES_PATH = os.path.join(os.path.dirname(__file__), "heritees.json")
try:
    with open(HERITEES_PATH, encoding="utf-8") as _f:
        HERITEES = set(json.load(_f).get("heritees", []))
except FileNotFoundError:
    HERITEES = set()



# ─────────────────────────────────────────────────────────────────────────────
# Règle d'or n°37 — l'interface montre des RESSOURCES PÉDAGOGIQUES, pas des fichiers.
# Règle d'or n°39 — un compteur compte ce que son étiquette annonce.
#
# Les fichiers de gouvernance (manifest, rapport de tests, matrice, SOURCES_MEDIAS,
# README, suites de tests) restent dans le dépôt et restent accessibles : ils passent
# simplement dans une seconde liste, repliée, et ne sont PLUS comptés comme ressources
# pédagogiques. Avant cette évolution, un lot complet affichait « 7 ressources » alors
# qu'il en propose trois à l'élève.
# ─────────────────────────────────────────────────────────────────────────────
TYPES_PEDAGOGIQUES = [
    (r"^sequence_mutualisee", "🔗", "Séquence mutualisée"),
    (r"^sequence(\b|[-_.])", "📘", "Séquence"),
    (r"^entrainement[-_]", "🏋", "Entraînement"),
    (r"^qcm[-_]", "🧠", "QCM"),
    (r"^synthese_eleve", "📌", "Synthèse élève"),
    (r"^synthese_professeur", "🎓", "Synthèse professeur"),
    (r"^(activite|activites)[-_]", "🔧", "Activité"),
    (r"^tp[-_]", "🔧", "Travaux pratiques"),
    (r"^evaluation[-_]", "📝", "Évaluation"),
    (r"^(fiche_pedagogique|FICHE_PEDAGOGIQUE)", "🧭", "Fiche pédagogique"),
    (r"\.pkt$", "🖧", "Fichier Packet Tracer"),
    (r"\.drawio$", "✏️", "Fichier draw.io"),
    (r"^(atelier|vittascience)[-_]", "🔧", "Activité"),
    (r"^(donnees|solutions|mesures|exo)[-_].*\.csv$", "📊", "Jeu de données"),
    (r"\.(xlsx|ods)$", "📊", "Classeur tableur"),
]

MOTIFS_MAINTENANCE = (
    r"^README\.md$", r"^SOURCES_MEDIAS\.md$", r"^matrice_couverture", r"^manifest",
    r"^MANIFESTE_LOT", r"^rapport_tests", r"^RAPPORT_TESTS", r"^JOURNAL_LOT",
    # Une suite de tests n'est pas une ressource pour la classe. Ce motif ne
    # connaissait que Python : les suites `.mjs` livrées depuis le 31/08/2026
    # étaient comptées et affichées comme ressources pédagogiques — un outil qui
    # reconnaît les fichiers par leur extension doit connaître toutes celles que
    # le dépôt emploie (règle d'or n°269).
    r"^tests_.*\.(py|mjs|js)$", r"^CRCN_regle7\.md$",
    # Documents de travail internes : utiles au dépôt, sans usage en classe.
    r"^(CADRAGE|PLAN_LOT|RAPPORT_CONTROLES|ANTICIPATION|AVIS_|MIGRATION_|ENTREE_NOUVEAUTES"
    r"|MATRICE_COUVERTURE|REGLE_OR|SOURCES_DONNEES)", r"^couverture_.*\.json$", r"\.json$",
)


def classer(nom):
    """(emoji, libellé pédagogique) ou None si le fichier relève de la maintenance."""
    # Les médias sont lus DANS la séquence, pas à côté : ils ne sont pas des
    # ressources autonomes. Ce contrôle passe en premier, sinon atelier_procedes.svg
    # serait annoncé comme une « Activité ».
    if nom.lower().endswith((".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".xml")):
        return None
    for motif in MOTIFS_MAINTENANCE:
        if re.search(motif, nom):
            return None
    for motif, emoji, libelle in TYPES_PEDAGOGIQUES:
        if re.search(motif, nom):
            return emoji, libelle
    return "📄", "Ressource"


def titre_pedagogique(nom, libelle):
    """Un nom lisible, tiré du fichier — jamais le nom physique (règle n°37).

    On retire le préfixe de type puis, jeton par jeton, tout ce qui relève de la
    codification interne : « 5e », « C4.1 », « C4.8 », les numéros isolés. Sans ce
    filtre par jeton, `qcm_5e_C4.1-C4.8_lampadaire_intelligent.html` donnait
    « QCM — 8 lampadaire intelligent » : un 8 orphelin, reste d'un code coupé en deux.
    """
    base = re.sub(r"\.[a-zA-Z0-9]+$", "", nom)
    base = re.sub(r"^(sequence_mutualisee_avec|sequence|qcm|synthese_eleve|synthese_professeur"
                  r"|activite|activites|atelier|vittascience|tp|evaluation|fiche_pedagogique"
                  r"|FICHE_PEDAGOGIQUE|entrainement|donnees|solutions|mesures|exo)([-_.]|$)", "", base)
    jetons = [j for j in re.split(r"[-_\s.]+", base) if j]
    garde = []
    for j in jetons:
        if re.fullmatch(r"\d+e", j) or re.fullmatch(r"C\d+", j, re.I) or re.fullmatch(r"\d+", j):
            continue
        garde.append(j)
    base = " ".join(garde).strip()
    if not base:
        return libelle
    return f"{libelle} — {base[0].upper() + base[1:]}"


# ── Règle d'or n°37, appliquée aux TP : la ressource porte son propre nom ────
#
# Constat de Pascal, le 27/08/2026, en regardant l'index : « 4e_C7.2 » et
# « 4e_C7.6 » affichaient tous deux « Travaux pratiques — Socle assemblage ».
# Impossible de les distinguer, et impossible de voir qu'il existe une SÉRIE de
# quatre TP qui va de la 5e à la 3e. Le libellé venait du nom de fichier — or le
# nom de fichier ne connaît ni le rang du TP, ni le niveau.
#
# Un TP, lui, se nomme dans son <h1> : « TP n°2 — Le dé sur son socle ». On lit
# donc ce titre-là, et on lui adjoint le niveau tiré du chemin. Le lecteur voit
# alors la série entière, et sa chronologie.
TITRE_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
RANG_TP = re.compile(r"TP\s*n[°º]\s*(\d+)\s*[—-]\s*(.+)$")


def titre_depuis_h1(chemin_relatif, nom, racine):
    """Le titre que le fichier se donne, ou None. Jamais deviné : lu."""
    if not nom.lower().endswith(".html"):
        return None
    try:
        with open(os.path.join(racine, chemin_relatif, nom), encoding="utf-8") as f:
            src = f.read(20000)
    except OSError:
        return None
    m = TITRE_H1.search(src)
    if not m:
        return None
    brut = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
    # on retire l'emoji de tête et les espaces insécables
    brut = brut.replace("\u00a0", " ").strip()
    brut = re.sub(r"^[^\w]+", "", brut).strip()
    r = RANG_TP.match(brut)
    if not r:
        return None
    niveau = ""
    for seg in chemin_relatif.replace("\\", "/").split("/"):
        if re.fullmatch(r"[3-6]e", seg):
            niveau = seg
            break
    rang, titre = r.group(1), r.group(2).strip()
    return "TP n°%s%s — %s" % (rang, (" · " + niveau) if niveau else "", titre)


# ── Statuts d'audit (règle n°35 : l'information est là où on la lit) ──────────
STATUTS_PATH = os.path.join(os.path.dirname(__file__), "..", "audit_couverture.csv")
STATUT_PAR_CODE, STATUT_PUCE = {}, {
    "COMPLET ET VALIDABLE": ("✅", "#81fba1"),
    "COUVERT PAR UNE SÉQUENCE MUTUALISÉE": ("🔗", "#61dafb"),
    "PARTIEL": ("🟡", "#ffd66b"),
    "EXISTANT À AMÉLIORER": ("🔧", "#ffb454"),
    "À VÉRIFIER PAR L’ENSEIGNANT": ("🔍", "#c68ef2"),
    "À CORRIGER": ("⚠️", "#ff7b88"),
    "À CRÉER": ("⬜", "#5b7bb8"),
}
try:
    import csv as _csv
    with open(STATUTS_PATH, encoding="utf-8-sig") as _f:
        for _r in _csv.DictReader(_f, delimiter=";"):
            STATUT_PAR_CODE[_r["code"]] = _r["statut"]
except (FileNotFoundError, KeyError):
    pass


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
    # "/" explicite (jamais os.path.join) : ce chemin sert d'URL dans index.html,
    # et sous Windows os.path.join produirait des "\" qui cassent tous les liens
    # sur GitHub Pages. os.path.join(DST, rel) accepte les "/" sur tous les OS.
    return "/".join([THEME_SLUG[theme], f"{cnum}-{slugify(text)}", niveau, f"{niveau}_{code}"])


def lot_sibling_dirs(cnum, niveau, code):
    """Dossiers freres de lots : {niveau}_{code}_<slug> (un dossier = un lot,
    arbitrage Pascal 02/08/2026 - ex. 4e_C4.1_book-train a cote de 4e_C4.1)."""
    base = code_dir(cnum, niveau, code)
    parent_rel = base.rsplit("/", 1)[0]
    parent_full = os.path.join(DST, parent_rel)
    prefix = f"{niveau}_{code}_"
    out = []
    if os.path.isdir(parent_full):
        for d in sorted(os.listdir(parent_full)):
            if d.startswith(prefix) and os.path.isdir(os.path.join(parent_full, d)):
                out.append(parent_rel + "/" + d)
    return out


#: Les sous-dossiers d'un lot dont le contenu est une ressource pour la classe.
#: Le 31/08/2026, une marche depuis `index.html` de lien en lien a montré que
#: **56 des 76 synthèses du dépôt n'étaient atteignables par aucun chemin** :
#: elles vivent dans `Synthèses/`, ce générateur ne lisait que le dossier du
#: code, et 40 séquences sur 46 ne les lient pas davantage. Une synthèse est
#: pourtant le document que l'élève emporte — et un fichier livré qu'aucun
#: chemin n'atteint n'est pas livré (règle d'or n°272).
SOUS_DOSSIERS_PEDAGOGIQUES = ("Synthèses",)


def content_files(rel_dir):
    """Fichiers de contenu réel (hors .gitkeep) du dossier code, puis de ses
    sous-dossiers pédagogiques — rendus avec leur chemin relatif au dossier."""
    full = os.path.join(DST, rel_dir)
    if not os.path.isdir(full):
        return []
    out = []
    for fn in sorted(os.listdir(full)):
        p = os.path.join(full, fn)
        if os.path.isfile(p) and fn != ".gitkeep":
            out.append(fn)
    for sous in SOUS_DOSSIERS_PEDAGOGIQUES:
        chemin = os.path.join(full, sous)
        if not os.path.isdir(chemin):
            continue
        for fn in sorted(os.listdir(chemin)):
            if os.path.isfile(os.path.join(chemin, fn)) and fn != ".gitkeep":
                out.append(sous + "/" + fn)
    return out


# ---------------------------------------------------------------- index.html
parts = []
parts.append("""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Technologie Cycle 4 — Programme 2024 | Compétences, séquences, QCM, socle et CRCN</title>
<meta name="description" content="Banque pédagogique de technologie pour le cycle 4 (programme 2024) : séquences, QCM, synthèses et évaluations pour la 5e, la 4e et la 3e, classées par thème, compétence de fin de cycle et repère de progressivité.">
<meta name="color-scheme" content="dark light">
<style>
:root{--bg:#050f24;--panel:#0d2347;--panel2:#0a1b3d;--border:#274a8a;--title:#81aaff;--sub:#9bbefc;--head:#c68ef2;--text:#e4eaf5;--hl:#61dafb}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:'Poppins','Segoe UI',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif;margin:0;padding:0 18px 60px;line-height:1.5}
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
/* ── badge héritée 🛠 (règle d'or n°12 — _outils/heritees.json) ── */
.badge-herit{margin-left:4px;cursor:help;font-size:.8em;filter:grayscale(.2)}
/* ── badge NEW (règle obligatoire — nouveautes.json) ── */
.badge-new{display:inline-block;background:linear-gradient(90deg,#ff7b88,#ffb454);color:#111;font-weight:700;font-size:.68em;padding:2px 8px;border-radius:999px;margin-left:6px;letter-spacing:.5px;vertical-align:middle;animation:nvpulse 2.2s ease-in-out infinite}
@keyframes nvpulse{0%,100%{opacity:1}50%{opacity:.62}}
@media (prefers-reduced-motion: reduce){.badge-new{animation:none}}
@media print{.badge-new{animation:none;background:#fff;border:1.5px solid #111;color:#111}}
.code-line.nv-cible{background:rgba(255,180,84,.1);border-radius:8px;outline:1px solid rgba(255,180,84,.45)}
.code-line{scroll-margin-top:14px}

/* ── Règle d'or n°41 — l'index tenu au même niveau que ce qu'il indexe ── */
a:focus-visible,summary:focus-visible,button:focus-visible{outline:3px solid var(--hl);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:-9999px}
.skip:focus{position:static;display:inline-block;margin:8px;padding:8px 14px;background:var(--panel);border:1px solid var(--hl);border-radius:8px;color:var(--hl)}
.code-line a{text-decoration:underline;text-underline-offset:2px}   /* jamais la couleur seule */
/* ── Règle d'or n°35 — un code n'apparaît jamais seul ── */
.rep{display:grid;grid-template-columns:1fr;gap:3px;padding:9px 0;border-bottom:1px dashed rgba(39,74,138,.55);font-size:.8em}
.rep:last-child{border-bottom:none}
.rep-tete{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.rep .cc{font-weight:700;white-space:nowrap;padding:1px 8px;border-radius:999px;background:rgba(39,74,138,.45)}
.rep .form{display:block;color:var(--text);overflow-wrap:anywhere;line-height:1.45}
.rep .meta{color:#7d9bd6;font-size:.92em}
.rep .statut{font-size:.92em;white-space:nowrap}
.rep ul{list-style:none;margin:4px 0 0;padding:0}
.rep li{margin:2px 0;overflow-wrap:anywhere}
.rep .maint{margin-top:3px}
.rep .maint summary{cursor:pointer;color:#5b7bb8;font-size:.92em}
.rep .maint a{color:#7d9bd6}
.socle-cle{max-width:1080px;margin:0 auto 22px;background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:10px 18px;font-size:.82em;color:var(--sub)}
.socle-cle b{color:var(--text)}
@media print{
  body{background:#fff;color:#111;padding:0}
  .theme,.lvl,.socle-cle{background:#fff;border-color:#666}
  .comp[open] .levels{display:block}
  details{border:none}
  .rep .maint{display:none}
  h1,.rep .form,.rep .cc{color:#111}
  a{color:#111}
}
</style>
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header>
<h1>🎓 Technologie — Cycle 4 (programme 2024)</h1>
<p class="sub">Séquences, QCM et ressources classés par <strong>Thème → Compétence de fin de cycle → Niveau → Repère</strong></p>
<p class="note"><b>Référence normative</b> : programme de technologie du cycle 4, <b>BO n°9 du 29 février 2024</b> —
il fixe les trois thèmes, les neuf compétences de fin de cycle, les connaissances, les capacités et les repères de progressivité 5e → 4e → 3e.<br>
<b>Codification opérationnelle</b> : les identifiants du type <code>5e_C4.1</code> sont des <b>codes de classement internes</b> à ce dépôt,
construits à partir de ces repères de progressivité et de la structuration des cahiers Nathan 2024. <b>Ils ne figurent pas comme tels au BO.</b></p>
</header>
<div class="socle-cle"><b>Domaines du socle commun</b> — D1 : les langages pour penser et communiquer · D2 : les méthodes et outils pour apprendre ·
D3 : la formation de la personne et du citoyen · D4 : les systèmes naturels et les systèmes techniques ·
D5 : les représentations du monde et l'activité humaine.</div>
<div class="legend">
  <span><span class="dot" style="background:#8fd18f"></span>5e</span>
  <span><span class="dot" style="background:#7db3f0"></span>4e</span>
  <span><span class="dot" style="background:#f0a878"></span>3e</span>
  <span>✅ couvert</span><span>🔗 mutualisé</span><span>🟡 partiel</span>
  <span>🔧 à actualiser</span><span>🔍 à vérifier</span><span>⚠️ à corriger</span>
  <span style="color:#5b7bb8">⬜ à créer</span>
</div>
<main id="contenu">
""")

total_peda = 0
for theme_n in [1, 2, 3]:
    parts.append(f'<section class="theme" id="theme-{theme_n}"><header style="color:{THEME_COLOR[theme_n]}">{THEME_EMOJI[theme_n]} Thème {theme_n} — {html.escape(THEME_TITLES[theme_n])}<span class="nv-theme-slot" data-theme="{theme_n}"></span></header>')
    for cnum in [f"C{i}" for i in range(1, 10)]:
        text, socle_parent, t = C_PARENT[cnum]
        if t != theme_n:
            continue
        n_peda = 0
        lvl_html = []
        for niveau in ["5e", "4e", "3e"]:
            lignes = []
            for code, ctext, socle in COMP_BY_LEVEL[niveau][cnum]:
                rel = code_dir(cnum, niveau, code)
                paires = [(rel, fn) for fn in content_files(rel)]
                for rel2 in lot_sibling_dirs(cnum, niveau, code):
                    paires += [(rel2, fn) for fn in content_files(rel2)]
                full_code = f"{niveau}_{code}"

                peda, maint = [], []
                for r, fn in paires:
                    # `fn` peut porter un sous-dossier (« Synthèses/… ») : le lien
                    # a besoin du chemin, le classement et le titre du seul nom.
                    nom = fn.rsplit("/", 1)[-1]
                    genre = classer(nom)
                    lien = f'{html.escape(r)}/{html.escape(fn)}'
                    herit = ('<span class="badge-herit" title="Ressource héritée — modernisation prévue (règle d\'or n°12)">🛠</span>'
                             if f"{r}/{fn}" in HERITEES else "")
                    if genre:
                        emoji, libelle = genre
                        # Un TP porte son rang et son nom dans son <h1> : on les
                        # lit plutôt que de les deviner d'après le nom de fichier.
                        titre = (titre_depuis_h1(r, fn, DST) if libelle == "Travaux pratiques" else None) \
                                or titre_pedagogique(nom, libelle)
                        peda.append(f'<li>{emoji} <a href="{lien}">{html.escape(titre)}</a>{herit}</li>')
                    else:
                        maint.append(f'<a href="{lien}">{html.escape(nom)}</a>')
                n_peda += len(peda)

                statut = STATUT_PAR_CODE.get(full_code, "")
                puce, couleur = STATUT_PUCE.get(statut, ("", "#5b7bb8"))
                bloc_statut = (f'<span class="statut" style="color:{couleur}" title="{html.escape(statut)}">{puce} {html.escape(statut.capitalize())}</span>'
                               if statut else "")
                corps = f'<ul>{"".join(peda)}</ul>' if peda else '<span class="empty">Aucune ressource pédagogique publiée pour ce repère.</span>'
                if maint:
                    corps += ('<details class="maint"><summary>🔧 Fichiers de gouvernance ('
                              + str(len(maint)) + ')</summary><p>' + " · ".join(maint) + '</p></details>')
                lignes.append(
                    f'<div class="rep" id="{full_code}">'
                    f'<div class="rep-tete"><span class="cc" style="color:{NIVEAU_COLOR[niveau]}">{full_code}</span>{bloc_statut}</div>'
                    f'<span class="form">{html.escape(ctext)}</span>'
                    f'<span class="meta">Socle : {html.escape(socle)}</span>'
                    f'{corps}</div>')
            lvl_html.append(f'<div class="lvl"><h4 style="color:{NIVEAU_COLOR[niveau]}">{niveau}</h4>{"".join(lignes)}</div>')
        total_peda += n_peda
        # Règle n°39 : l'étiquette dit exactement ce qui est compté.
        count_label = (f"{n_peda} ressource(s) pédagogique(s)" if n_peda else "à compléter")
        parts.append(
            f'<details class="comp" id="comp-{cnum}"><summary><span class="cnum">{cnum}</span>'
            f'<span>{html.escape(text)}<span class="nv-comp-slot" data-comp="{cnum}"></span></span>'
            f'<span class="count">{count_label}</span></summary>'
            f'<div class="levels">{"".join(lvl_html)}</div></details>'
        )
    parts.append("</section>")
parts.append("</main>")

parts.append(f"""<footer>
<p>📦 <a href="_ressources-communes/">Ressources communes</a> · 🗄️ <a href="_archive-anciennes-versions/">Archive des anciennes versions</a> · <a href="RAPPORT_MIGRATION.md">Rapport de migration</a></p>
<p><b>Référence normative</b> : programme de technologie du cycle 4 — BO n°9 du 29 février 2024.<br><b>Codification opérationnelle</b> : adaptation pédagogique de ce dépôt, appuyée sur les repères de progressivité du programme et sur les cahiers Nathan 5e/4e/3e (éd. 2024). Structure générée depuis le classeur <em>Référentiel_Technologie_Cycle4_2024.xlsx</em>.<br><span style="color:#7d9bd6">Page générée automatiquement depuis <code>_outils/data_competences.py</code> — aucun intitulé n'est ressaisi à la main (règle d'or n°38).</span></p>
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
print("index.html généré —", total_peda, "ressources pédagogiques référencées")

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
