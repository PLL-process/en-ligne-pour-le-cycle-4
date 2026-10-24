# -*- coding: utf-8 -*-
"""Synthèses élève et professeur d'un atelier, tirées des mêmes données que ses pages.

La synthèse élève est la trace à garder : les mots, le schéma, ce qu'il faut
retenir, les erreurs fréquentes, le vocabulaire anglais. Elle s'imprime sur fond
blanc. La synthèse professeur porte le référentiel en toutes lettres, la place
de l'atelier sur la chaîne d'analyse, le verbe de chaque niveau, le déroulé et
les corrigés résumés.
"""
import re

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


def _texte_brut(h):
    return re.sub(r"<[^>]+>", "", h)


def _mots(at):
    vus, out = set(), []
    for niv, N in at.NIVEAUX.items():
        for ex in N["exercices"]:
            for m, d in ex.get("mots", []):
                cle = _texte_brut(m).lower()
                if cle in vus:
                    continue
                vus.add(cle)
                out.append((m, d, niv))
    return out


def eleve(at, page_niveau, chemins_fn, chemin):
    d = chemin.parent
    nav = ['<a href="%s">&#8962; Accueil</a>' % moteur.rel(d, moteur.DEPOT / "index.html")]
    for niv in at.NIVEAUX:
        nav.append('<a href="%s">&#8592; L\'atelier de %s</a>' % (moteur.rel(d, page_niveau(at, niv)), niv))
    h = [_tete("Synthèse élève — %s" % at.TITRE_COURT, "Trace à garder de l'atelier : %s." % at.TITRE_COURT, "".join(nav))]
    h.append("<h1>%s %s</h1>" % (at.EMOJI, at.TITRE))
    h.append('<p class="sous">La trace à garder — %s</p>' % " · ".join(at.NIVEAUX))
    h.append('<p style="text-align:center"><button class="btn" type="button" onclick="window.print()">🖨 Imprimer ma synthèse</button></p>')
    h.append('<section class="card"><h2>🏷 Deux noms pour une même représentation</h2><p>%s</p></section>' % at.DEUX_NOMS)
    for niv, N in at.NIVEAUX.items():
        cours = getattr(at, "COURS", {}).get(niv)
        if cours:
            h.append('<section class="card" id="cours-%s"><h2>📘 En %s — le cours</h2><div class="cours-corps">%s</div></section>' % (niv, niv, cours))
        h.append('<section class="card"><h2>📌 En %s — à retenir</h2><div class="retenir">%s</div>' % (niv, N["a_retenir"]))
        schema = getattr(at, "SCHEMAS_SYNTHESE", {}).get(niv)
        if schema:
            h.append('<figure class="figure">%s</figure>' % schema)
        h.append("</section>")
    h.append('<section class="card" id="les-mots"><h2>📖 Les mots</h2><dl>')
    for m, d_, niv in _mots(at):
        h.append("<dt>%s <small>(%s)</small></dt><dd>%s</dd>" % (m, niv, d_))
    h.append("</dl></section>")
    h.append('<section class="card"><h2>⚠ Les erreurs fréquentes</h2><ul class="piege">')
    for niv, N in at.NIVEAUX.items():
        for ex in N["exercices"]:
            if ex.get("piege"):
                h.append("<li><b>%s</b> — %s</li>" % (niv, ex["piege"]))
    h.append("</ul></section>")
    if getattr(at, "VOCAB_EN", None):
        h.append('<section class="card"><h2>🇬🇧 En anglais</h2><div class="defile"><table><thead><tr><th scope="col">Français</th>'
                 '<th scope="col">English</th></tr></thead><tbody>')
        for fr, en in at.VOCAB_EN:
            h.append('<tr><td>%s</td><td lang="en">%s</td></tr>' % (e(fr), e(en)))
        h.append("</tbody></table></div></section>")
    h.append("</main>\n</body>\n</html>\n")
    return "".join(h)


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


def ecrire(at, page_niveau, synthese_eleve, synthese_prof, chemins_fn, ecrire_fn):
    n = 0
    p = synthese_eleve(at)
    ecrire_fn(p, eleve(at, page_niveau, chemins_fn, p))
    n += 1
    p = synthese_prof(at)
    ecrire_fn(p, professeur(at, page_niveau, chemins_fn, p))
    n += 1
    return n
