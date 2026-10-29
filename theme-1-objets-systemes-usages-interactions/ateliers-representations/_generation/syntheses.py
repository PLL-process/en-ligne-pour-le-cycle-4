# -*- coding: utf-8 -*-
"""Synthèses élève et professeur d'un atelier, tirées des mêmes données que ses pages.

La synthèse élève est la trace à garder, une fiche de révision qu'un élève de
6e lit seul et qui tient sur deux pages A4 (règle d'or n°316 révisée, 29/10/2026) :
la carte « Ce que je dois retenir » (la question, ce que dit le programme, une
carte par partie), puis, par partie, le titre-question, l'exemple de l'atelier en
deux lignes, « À retenir » et le piège ; un seul lexique à la fin. Son texte est
dans synthese_<module>.py.

La synthèse professeur porte le référentiel en toutes lettres, la place de
l'atelier sur la chaîne d'analyse, le verbe de chaque niveau, le déroulé et les
corrigés résumés.
"""
import moteur

e = moteur.e

CSS = """
:root{--bg:#050f24;--panel:#0d2347;--border:#274a8a;--title:#81aaff;--sub:#9bbefc;--head:#c68ef2;--text:#e4eaf5;--hl:#61dafb;--ok:#81fba1}
*{box-sizing:border-box}body{background:var(--bg);color:var(--text);margin:0;padding:0 0 40px;line-height:1.6;
font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif;font-size:17px}
.page{max-width:900px;margin:0 auto;padding:0 16px}h1{color:var(--title);text-align:center;font-size:1.45em;margin:20px 0 4px}
h2{color:var(--head);font-size:1.15em;margin:22px 0 8px}h3{color:var(--hl);font-size:1em;margin:14px 0 4px}
.sous{text-align:center;color:var(--sub)}.card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:14px 18px;margin:14px 0}
a,a:where(:visited){color:var(--hl)}dl dt{font-weight:700;margin-top:8px}dl dd{margin:0 0 4px 16px}
table{width:100%;border-collapse:collapse;font-size:.92em}th,td{border:1px solid #2f5695;padding:6px 9px;text-align:left;vertical-align:top}
th{background:#0a1b3d;color:var(--sub)}.defile{overflow-x:auto}
@media (max-width:600px){.defile{overflow-x:auto;-webkit-overflow-scrolling:touch}.figure{overflow-x:auto}}
.figure svg{width:100%;height:auto;max-width:820px;display:block;margin:8px auto;border:1px solid var(--border);border-radius:10px;background:#fbfcff}
.retenir li{margin:6px 0}.piege li{margin:6px 0}
.bloc{border-left:4px solid var(--hl);padding:8px 14px;background:rgba(11,27,57,.6);border-radius:0 8px 8px 0;margin:10px 0}
#navharm{display:flex;flex-wrap:wrap;gap:8px;max-width:900px;margin:12px auto 0;padding:0 16px}
#navharm a{padding:6px 12px;border:1.5px solid var(--border);border-radius:999px;background:var(--panel);color:var(--sub);font-size:.88em;text-decoration:none}
.btn{background:#1d4e89;color:#fff;border:none;border-radius:9px;padding:9px 16px;font-weight:600;cursor:pointer;font-family:inherit}
.evitement{position:absolute;left:-9999px}.evitement:focus{left:10px;top:10px;background:#fff;color:#000;padding:8px}
@media print{body{background:#fff;color:#111;font-size:11.5pt}#navharm,.btn{display:none}.card{background:#fff;border-color:#999;break-inside:avoid-page}
h1,h2,h3{color:#111}a,a:visited{color:#00309e!important}.sous{color:#1a3a7a}th{background:#eee;color:#111}.bloc{background:#fff}}
"""


def _tete(titre, description, navigation):
    return ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="description" content="%s">\n<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n'
            '<a class="evitement" href="#contenu">Aller au contenu</a>\n<nav id="navharm" aria-label="Navigation du site">%s</nav>\n'
            '<main id="contenu" class="page">\n' % (e(description), e(titre), CSS, navigation))


def professeur(at, page_niveau, chemins_fn, chemin):
    d = chemin.parent
    nav = ['<a href="%s">&#8962; Accueil</a>' % moteur.rel(d, moteur.DEPOT / "index.html")]
    for niv in at.NIVEAUX:
        nav.append('<a href="%s">&#8592; L\'atelier de %s</a>' % (moteur.rel(d, page_niveau(at, niv)), niv))
    h = [_tete("Synthèse professeur — %s" % at.TITRE_COURT, "Synthèse professeur de l'atelier : %s." % at.TITRE_COURT, "".join(nav))]
    h.append("<h1>%s %s — synthèse professeur</h1>" % (at.EMOJI, at.TITRE))
    # Le référentiel, recopié sans réécriture
    h.append('<div class="bloc referentiel-eleve card"><h2>📚 Le référentiel de l\'atelier — en toutes lettres</h2><div class="defile"><table>'
             '<thead><tr><th scope="col">Code</th><th scope="col">Formulation</th><th scope="col">Domaines du socle</th></tr></thead><tbody>')
    for niv, N in at.NIVEAUX.items():
        for c in N["codes"]:
            texte, socle = moteur.REFERENTIEL[c]
            h.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (e(c), e(texte), e(socle)))
    h.append("</tbody></table></div><p><small>Référence normative&nbsp;: programme de technologie du cycle 4, BO n°9 du 29 février 2024. "
             "Codification opérationnelle&nbsp;: les codes (5e_C2.1…) sont des codes de classement internes à ce dépôt&nbsp;; ils ne "
             "figurent pas comme tels au BO.</small></p></div>")
    h.append('<section class="card"><h2>🔗 Place sur la chaîne d\'analyse</h2>%s</section>' % at.CHAINE)
    h.append('<section class="card"><h2>🌀 Le verbe de chaque niveau</h2><ul>')
    for niv in ("5e", "4e", "3e"):
        if niv in at.VERBES:
            h.append("<li><b>%s</b> — %s</li>" % (niv, at.VERBES[niv]))
    h.append("</ul><p>La notion reste la même d'un niveau à l'autre&nbsp;; c'est le geste demandé qui change.</p></section>")
    for niv, N in at.NIVEAUX.items():
        total = sum(x["duree"] for x in N["exercices"])
        h.append('<section class="card"><h2>🧭 %s — déroulé (≈ %d min d\'exercices, une séance de 55 min avec l\'ouverture et le bilan)</h2>'
                 '<div class="defile"><table><thead><tr><th scope="col">Exercice</th><th scope="col">Code</th><th scope="col">Durée</th>'
                 '<th scope="col">Production de l\'élève</th><th scope="col">Ce que vérifie la page</th></tr></thead><tbody>' % (niv, total))
        for i, ex in enumerate(N["exercices"]):
            verifs = []
            for w in ex["widgets"]:
                verifs.append({"choix": "une question à choix", "cases": "des cases à cocher", "classer": "un classement ligne par ligne",
                               "liste": "une liste (refus motivé des pièces et des actions)", "texte": "un texte (critères affichés)",
                               "slots": "les cases du schéma", "croquis": "un croquis et sa relecture"}[w["type"]])
            h.append("<tr><td>%d. %s</td><td>%s</td><td>%d min</td><td>%s</td><td>%s</td></tr>"
                     % (i + 1, ex["titre"], e(ex["code"]), ex["duree"], ex["production"], " ; ".join(verifs)))
        h.append("</tbody></table></div>")
        h.append("<h3>Corrigés, en bref</h3><ol>")
        for ex in N["exercices"]:
            dernier = ex["correction"][-1]
            h.append("<li><b>%s</b> — %s</li>" % (ex["titre"], dernier[1] if isinstance(dernier, tuple) else dernier))
        h.append("</ol><p>Les corrections complètes sont dans la page de l'atelier, repliées après chaque exercice.</p></section>")
    h.append('<section class="card"><h2>🧩 Différenciation</h2><ul>'
             "<li>Deux aides par exercice&nbsp;: la première dit <i>comment</i> chercher, la seconde donne le raisonnement, suivie "
             "d'un exercice jumeau à faire seul.</li>"
             "<li>Une version étayée (débuts de phrase) pour chaque production écrite.</li>"
             "<li>Le mode essentiel masque les corrections et les descriptions longues des schémas.</li>"
             "<li>Chaque exercice a son lexique « 📖 Les mots de cet exercice ».</li>"
             "<li>Chaque schéma s'agrandit d'un clic, et sa description en mots est dépliable.</li>"
             "<li>Tout se fait dans la page, sans papier ni Internet&nbsp;; le travail est partagé avec le cahier du niveau.</li></ul></section>")
    if getattr(at, "NOTES_PROF", None):
        h.append('<section class="card"><h2>📝 Choix de conception de l\'atelier</h2>%s</section>' % at.NOTES_PROF)
    h.append("</main>\n</body>\n</html>\n")
    return "".join(h)


# ─────────────────────────────────────────────────────────────────────────────
# La synthèse élève, règle d'or n°316 révisée (29/10/2026) : deux pages A4, la
# forme du pilote 5e_C1.1 (Chengdu) — la carte « Ce que je dois retenir », puis,
# par partie, le titre-question, l'exemple de l'atelier en deux lignes (en cases
# quand il compare ou enchaîne), « À retenir », le piège en une ligne ; un seul
# lexique à la fin. Le texte de chaque atelier est dans synthese_<module>.py ; la
# feuille de style est celle du pilote, mot pour mot, plus la pastille de niveau.
# ─────────────────────────────────────────────────────────────────────────────
CSS_ELEVE = """  :root{--bg:#050f24;--panel:#0d2347;--panel2:#0a1b3d;--border:#274a8a;--title:#81aaff;--sub:#9bbefc;--head:#c68ef2;
        --text:#e4eaf5;--hl:#61dafb;--ok:#81fba1;--warn:#ffd66b;--err:#ff7b88}
  *{box-sizing:border-box}
  body{background:var(--bg);color:var(--text);margin:0;padding:14px 18px 40px;line-height:1.5;font-size:.95em;
       font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif}
  .page{max-width:860px;margin:0 auto}
  h1{font-size:1.35em;color:var(--title);text-align:center;margin:8px 0 2px}
  .pb{text-align:center;color:var(--warn);font-weight:600;font-size:.95em;margin:4px 0 14px}
  h2{font-size:1.05em;color:var(--head);margin:14px 0 8px;border-bottom:1px solid var(--border);padding-bottom:4px}
  h3{font-size:.95em;color:var(--sub);margin:12px 0 4px}
  .bloc{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:12px 16px;margin-bottom:14px}
  .schema{width:100%;border:1px solid var(--border);border-radius:10px;background:#050f24;margin:6px 0}
  ul,ol{margin:4px 0;padding-left:22px}li{margin:4px 0}
  code{font-family:ui-monospace,Consolas,monospace;background:#08132c;padding:1px 6px;border-radius:5px;font-size:.9em}
  table{width:100%;border-collapse:collapse;margin:6px 0}
  th,td{text-align:left;padding:5px 8px;border-bottom:1px solid var(--border);vertical-align:top}
  th{color:var(--sub);font-size:.9em}
  .toolbar{text-align:center;margin:10px 0}
  .btn{background:#1d4e89;color:#fff;border:none;border-radius:8px;padding:8px 16px;cursor:pointer;font-family:inherit;font-weight:600}
  a:focus-visible,.btn:focus-visible,summary:focus-visible{outline:3px solid var(--hl);outline-offset:2px}
  #navharm{position:sticky;top:0;z-index:1200;display:flex;gap:8px;padding:7px 12px;background:rgba(5,15,36,.93);border-bottom:1px solid #274a8a;margin:-14px -18px 12px}
  /* règle n°304 : un lien de rattrapage arrive sur ce titre ; la barre collante (47 px) ne doit pas le recouvrir */
  h2[id]{scroll-margin-top:60px}
  #navharm a{padding:5px 14px;border:1.5px solid #274a8a;border-radius:999px;background:#0d2347;color:#9bbefc;font-size:.92em;text-decoration:none}

  /* ══ Règle d'or n°316 — la synthèse se lit seule, par un élève de 6e ══ */
  /* Une couleur par notion, la même partout : la donnée en jaune, l'information en vert. */
  .d{color:var(--warn);font-weight:600}.i{color:var(--ok);font-weight:600}
  /* La carte « Ce que je dois retenir » */
  .carte{border:2px solid var(--warn);border-radius:14px;padding:14px 16px;margin:0 0 18px;background:var(--panel2)}
  .carte h2{border:none;color:var(--warn);text-align:center;margin:0 0 4px;font-size:1.15em}
  .question{text-align:center;font-size:1.05em;font-weight:600;margin:0 0 10px}
  .programme{font-size:.85em;color:var(--sub);border-top:1px dashed var(--border);border-bottom:1px dashed var(--border);
             padding:6px 0;margin:0 0 12px}
  .programme b{color:var(--text)}
  .programme ul{margin:2px 0;padding-left:18px}.programme li{margin:1px 0}
  .cartes{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
  .cartes a{display:block;text-decoration:none;color:var(--text);background:var(--panel);border:1.5px solid var(--border);
            border-radius:10px;padding:9px 12px}
  .cartes a:hover{border-color:var(--hl)}
  .cartes .q{display:block;color:var(--hl);font-weight:600;margin-bottom:3px}
  .cartes .r{display:block;font-size:.92em}
  /* Une partie (format 2 pages A4, décision de Pascal du 29/10/2026) : la question, l'exemple de la séquence en
     deux lignes, l'encadré « À retenir », le piège en une ligne ; tous les mots dans un seul lexique, à la fin. */
  .retenir{border:2px solid var(--ok);border-radius:10px;padding:8px 12px;margin:10px 0;background:#0d3320}
  .piege{border-left:4px solid var(--err);padding:4px 12px;margin:10px 0;background:#2a1220;border-radius:0 8px 8px 0}
  .chaine{display:flex;flex-wrap:wrap;align-items:stretch;gap:10px;margin:8px 0;break-inside:avoid}
  .chaine div{flex:1 1 170px;border:1.5px solid var(--border);border-radius:8px;padding:6px 10px;background:var(--panel2)}
  .chaine b{display:block}
  .chaine code{white-space:nowrap} /* un nom de fichier ne se coupe pas : la case passe à la ligne entière */
  /* Les petits schémas en cases : une case par principe, par valeur, par règle ou par étape ; le bord dit le verdict. */
  .chaine div.ok{border-color:var(--ok)}.chaine div.ko{border-color:var(--err)}
  .chaine.etapes div{position:relative}
  .chaine.etapes div+div::before{content:"➜";position:absolute;left:-10px;top:38%;font-size:10px;color:var(--sub)}
  @media (max-width:600px){.chaine.etapes div+div::before{display:none}}
  ul.serre li{margin:1px 0}
  .vert{color:var(--ok)}.rouge{color:var(--err)}
  .en{color:var(--sub);font-style:italic;font-weight:400}
  /* Le lexique en colonnes (et non en grille) : une définition longue ne laisse pas de trou à côté d'elle. */
  dl.lexique{columns:2 300px;column-gap:18px;margin:6px 0}
  dl.lexique div{break-inside:avoid;margin-bottom:5px}
  dl.lexique dt{color:var(--hl);font-weight:600;display:inline}
  dl.lexique dd{display:inline;margin:0}
  dl.lexique dd::before{content:" : "}

  @media print{body{background:#fff;color:#111;font-size:8.6pt;line-height:1.32;padding:0}.bloc,.carte{background:#fff;border-color:#999}
    h1,h2,h3,.pb,.cartes .q{color:#111}.toolbar,#navharm{display:none}.page{max-width:none}code{background:#eee}a{color:#111}
    /* Impression sans blanc (29/10/2026, demande de Pascal) : pas de saut de page forcé ; un titre reste collé à ce qui
       le suit ; un schéma ne laisse pas son titre en bas de page. */
    h1,h2,h3,.pb,.question{break-after:avoid;page-break-after:avoid}
    .schema,table,.chaine{break-before:avoid;page-break-before:avoid}
    p,li,dd{orphans:3;widows:3}
    .cartes a,.retenir,.piege,.chaine div{background:#fff;color:#111}
    .chaine div.ok{border-color:#2d7a4a}.chaine div.ko{border-color:#b3261e}
    .retenir{border-color:#2d7a4a}.piege{border-left-color:#b3261e}
    .d{color:#8a5a00}.i{color:#1d6b38}.vert{color:#1d6b38}.rouge{color:#b3261e}
    .carte h2{color:#8a5a00}.programme,.programme b,.en,th,dl.lexique dt{color:#222}
    .bloc{break-inside:auto;padding:5px 10px;margin-bottom:6px}
    .schema{width:60%;display:block;margin:4px auto}
    h2{margin:6px 0 4px}h3{margin:6px 0 2px}p{margin:4px 0}
    .retenir,.piege{padding:3px 8px;margin:4px 0}
    table{margin:3px 0}th,td{padding:2px 6px}.chaine{gap:6px;margin:4px 0}.chaine div{padding:3px 8px}
    .carte{padding:8px 12px;margin-bottom:8px}.programme{margin-bottom:6px;padding:3px 0}.cartes{gap:6px}.cartes a{padding:4px 9px}
    .cartes .q{margin-bottom:1px}
    dl.lexique{columns:2;column-gap:14px;font-size:.95em}dl.lexique div{margin-bottom:1px}}

@media print{
/* — impression : fond blanc, couleurs conservées (décision du 02/09/2026) — */
  .bloc code,.schema{background:#fff!important;background-image:none!important;border-color:#999!important;box-shadow:none!important}
}

  /* ── Règle d'or n°303 — un lien se lit ───────────────────────────
     À l'écran ET sur le papier, cliqué ou non. La couleur d'écran est vérifiée
     contre le fond réel de CETTE page, celle du papier contre le blanc.
     `a:visited` est écrit parce qu'il ne se MESURE pas : les navigateurs
     refusent de révéler l'état visité. Sans cette ligne, le lien redevient
     violet après le premier clic — illisible sur fond sombre. */
  a,a:where(:visited){color:var(--hl)}
  @media print{
    a,a:visited{color:#00309e!important}
    a.btn,a.button,a.bouton{color:#00309e!important;background:#fff!important;border:1px solid #00309e!important}
  }

/* ══ Filet mobile (règle d'or n°135, volet débordement) ══ */
@media(max-width:680px){table{display:block;overflow-x:auto}}

  /* Revenir à la carte (Pascal, 29/10/2026 : « je ne peux pas revenir à la synthèse ») : chaque partie porte, en
     haut à droite, un lien vers la carte « Ce que je dois retenir » ; la barre de navigation collée en haut ne
     recouvre plus le titre visé par un lien. Rien de tout cela ne s'imprime. */
  .retour-carte{float:right;font-size:.82em;margin:1px 0 0 10px;padding:1px 10px;border:1.5px solid var(--border);
                border-radius:999px;text-decoration:none;white-space:nowrap}
  .retour-carte:hover,.retour-carte:focus-visible{border-color:var(--hl)}
  #carte-titre,[id^="partie-"]{scroll-margin-top:64px}
  @media print{.retour-carte{display:none}}

/* ══ Ateliers des représentations : plusieurs niveaux sur une même page ══ */
.niv{display:inline-block;font-size:.72em;font-weight:700;color:#050f24;background:var(--sub);border-radius:999px;
     padding:1px 8px;margin-left:6px;vertical-align:middle;white-space:nowrap}
.programme .niv{margin:0 6px 0 0}
.evitement{position:absolute;left:-9999px}.evitement:focus{left:10px;top:10px;background:#fff;color:#000;padding:8px}
#navharm{flex-wrap:wrap}
@media(max-width:600px){#navharm{position:static}}
@media print{.niv{background:#fff;color:#111;border:1px solid #999}.evitement{display:none}}
"""


def eleve(at, page_niveau, chemins_fn, chemin):
    import importlib
    S = importlib.import_module("synthese_" + at.MODULE)
    d = chemin.parent
    nav = ['<a href="%s">&#8962; Accueil</a>' % moteur.rel(d, moteur.DEPOT / "index.html")]
    for niv in at.NIVEAUX:
        nav.append('<a href="%s">&#8592; L\'atelier de %s</a>' % (moteur.rel(d, page_niveau(at, niv)), niv))
    c = chemins_fn(at, next(iter(at.NIVEAUX)), d)
    if c.get("qcm"):
        nav.append('<a href="%s">&#129504; Le QCM</a>' % c["qcm"])
    o = []
    a = o.append
    a('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      '<meta name="description" content="%s">\n<title>%s</title>\n<style>%s</style>\n</head>\n<body>'
      % (e("Trace à garder de l'atelier : %s." % at.TITRE_COURT), e("Synthèse élève — %s" % at.TITRE_COURT), CSS_ELEVE))
    a('<a class="evitement" href="#contenu">Aller au contenu</a>')
    a('<nav id="navharm" aria-label="Navigation du site">%s</nav>' % "".join(nav))
    a('<main id="contenu" class="page">\n<h1>%s Synthèse élève — %s</h1>\n<p class="pb">%s</p>' % (at.EMOJI, S.H1, S.PB))
    a('<div class="toolbar"><button class="btn" type="button" onclick="window.print()">🖨 Imprimer (2 pages A4)</button></div>')
    # La carte « Ce que je dois retenir »
    a('<section class="carte" aria-labelledby="carte-titre">\n  <h2 id="carte-titre">🧠 Ce que je dois retenir</h2>')
    a('  <p class="question">%s</p>' % S.QUESTION)
    a('  <div class="programme"><b>Ce que dit le programme</b>&nbsp;:\n    <ul>')
    for niv, N in at.NIVEAUX.items():
        for code in N["codes"]:
            a('      <li><span class="niv">%s</span>%s</li>' % (niv, moteur.avec_sigles(moteur.formulation(code))))
    a('    </ul>\n  </div>\n  <div class="cartes">')
    for k, p in enumerate(S.PARTIES, 1):
        a('    <a href="#partie-%d"><span class="q">%s %d. %s <span class="niv">%s</span></span>\n      <span class="r">%s</span></a>'
          % (k, p["emoji"], k, p.get("titre_court", p["titre"]), p["niveau"], p["carte"]))
    a('  </div>\n</section>')
    # Les parties : la question, l'exemple de l'atelier, à retenir, le piège
    for k, p in enumerate(S.PARTIES, 1):
        a('<!-- ══ %d ══ -->\n<div class="bloc">' % k)
        a('  <a class="retour-carte" href="#carte-titre">↑ La carte</a>')
        a('  <h2 id="partie-%d" style="margin-top:0">%d. %s <span class="niv">%s</span></h2>' % (k, k, p["titre"], p["niveau"]))
        a(p["exemple"].strip())
        a('  <p class="retenir">🧠 <b>À retenir</b>&nbsp;: %s</p>' % p["retenir"])
        a('  <p class="piege">⚠️ <b>Le piège</b>&nbsp;: %s</p>' % p["piege"])
        a('</div>')
    # Un seul lexique (les liens « @synthese#les-mots » des ouvertures y arrivent)
    a('<!-- ══ Les mots ══ -->\n<div class="bloc mots">')
    a('  <h2 id="les-mots" style="margin-top:0">📖 Les mots de l\'atelier</h2>\n  <dl class="lexique">')
    for fr, en, defi in S.LEXIQUE:
        a('    <div><dt>%s <span class="en" lang="en">— %s</span></dt><dd>%s</dd></div>' % (fr, en, defi))
    a('  </dl>\n</div>\n</main>\n</body>\n</html>\n')
    return "\n".join(o)


def ecrire(at, page_niveau, synthese_eleve, synthese_prof, chemins_fn, ecrire_fn):
    n = 0
    p = synthese_eleve(at)
    ecrire_fn(p, eleve(at, page_niveau, chemins_fn, p))
    n += 1
    p = synthese_prof(at)
    ecrire_fn(p, professeur(at, page_niveau, chemins_fn, p))
    n += 1
    return n
