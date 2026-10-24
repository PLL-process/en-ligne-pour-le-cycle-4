# -*- coding: utf-8 -*-
"""Moteur des ateliers des représentations : des données aux pages.

Une représentation = un module `donnees_<slug>.py` qui décrit, niveau par
niveau, ses exercices. Ce moteur en tire :
  · une page d'atelier par niveau (`<slug>/atelier_<niv>_<slug>.html`) ;
  · les exercices du même niveau pour le cahier de ce niveau (cahiers/) ;
  · des pages-panneaux dans le dossier de chaque code servi.

Les textes destinés à l'élève sont dans les données, jamais ici : ce fichier ne
fait que la mise en page. Rien n'est chargé depuis Internet.
"""
import html
import json
import os
import pathlib
import re

ICI = pathlib.Path(__file__).resolve().parent
RACINE_ATELIERS = ICI.parent                       # …/ateliers-representations
THEME1 = RACINE_ATELIERS.parent                    # …/theme-1-…
DEPOT = THEME1.parent

KIT_CSS = (ICI / "kit.css").read_text(encoding="utf-8")
KIT_JS = (ICI / "kit.js").read_text(encoding="utf-8")

NIVEAUX_NOMS = {"5e": "5e", "4e": "4e", "3e": "3e"}
LSU = ["Maîtrise insuffisante", "Maîtrise fragile", "Maîtrise satisfaisante", "Très bonne maîtrise"]
RONDS = "①②③④⑤⑥⑦⑧⑨"


def e(s):
    return html.escape(str(s), quote=True)


def rel(depuis_dossier, cible):
    """Chemin relatif POSIX d'un dossier vers un fichier du dépôt."""
    return os.path.relpath(str(cible), str(depuis_dossier)).replace(os.sep, "/")


# ─────────────────────────────────────────────────────────────────────────────
# Le référentiel : les formulations se recopient, elles ne se réécrivent pas.
# ─────────────────────────────────────────────────────────────────────────────
def _referentiel():
    import importlib.util
    spec = importlib.util.spec_from_file_location("dc", str(DEPOT / "_outils" / "data_competences.py"))
    dc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dc)
    table = {}
    for niv, nom in (("5e", "COMP_5E"), ("4e", "COMP_4E"), ("3e", "COMP_3E")):
        for cp, liste in getattr(dc, nom).items():
            for code, texte, socle in liste:
                table["%s_%s" % (niv, code)] = (texte, socle)
    return table, dc.C_PARENT, dc


REFERENTIEL, C_PARENT, _DC = _referentiel()


def avec_sigles(texte):
    """Aucun sigle nu : OST se lit en toutes lettres au survol et au lecteur d'écran."""
    return e(texte).replace("OST", '<abbr title="objet ou système technique">OST</abbr>')


def formulation(code):
    if code not in REFERENTIEL:
        raise SystemExit("Code inconnu du référentiel : %s" % code)
    return REFERENTIEL[code][0]


def dossier_code(code):
    """Le dossier d'un code, calculé comme le fait le générateur de l'index."""
    niv, cc = code.split("_")
    cnum = cc.split(".")[0]
    import importlib.util
    spec = importlib.util.spec_from_file_location("mi", str(DEPOT / "_outils" / "make_index.py"))
    # make_index régénère l'index à l'import : on recopie seulement sa règle de nommage.
    texte, _, theme = C_PARENT[cnum]
    slug = _slugify(texte)
    themes = {1: "theme-1-objets-systemes-usages-interactions",
              2: "theme-2-structure-fonctionnement-comportement",
              3: "theme-3-creation-conception-realisation-innovations"}
    return DEPOT / themes[theme] / ("%s-%s" % (cnum, slug)) / niv / ("%s_%s" % (niv, cc))


def _slugify(s, maxlen=45):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    parts, out, total = s.split("-"), [], 0
    for p in parts:
        if total + len(p) + 1 > maxlen and out:
            break
        out.append(p)
        total += len(p) + 1
    return "-".join(out)


def sequence_du_code(code):
    """La séquence qui porte ce code : dans son dossier, ou indiquée par son README."""
    d = dossier_code(code)
    if not d.is_dir():
        return None
    seq = sorted(d.glob("sequence*.html"))
    if seq:
        return seq[0]
    readme = d / "README.md"
    if readme.exists():
        m = re.search(r"\]\((\.\./[^)]+?sequence[^)]+?\.html)\)", readme.read_text(encoding="utf-8"))
        if m:
            p = (d / m.group(1)).resolve()
            if p.exists():
                return p
    # dossiers frères (un lot = un dossier : 4e_C4.1_book-train)
    for frere in sorted(d.parent.glob(d.name + "_*")):
        seq = sorted(frere.glob("sequence*.html"))
        if seq:
            return seq[0]
    return None


# ─────────────────────────────────────────────────────────────────────────────
# Les questions : HTML + définition pour le moteur de la page
# ─────────────────────────────────────────────────────────────────────────────
class Rendu:
    """Accumule le HTML d'un exercice et la définition JSON de ses vérificateurs."""

    def __init__(self, uid):
        self.uid = uid
        self.defs = []

    def nom(self, n):
        return "%s__%s" % (self.uid, n)

    def options(self, name, options, miroir=None):
        h = ['<div class="options">']
        for i, (val, lib) in enumerate(options):
            ident = "%s-%d" % (name, i)
            extra = (' data-miroir="%s" data-texte="%s"' % (miroir, e(lib))) if miroir else ""
            h.append('<label class="option" for="%s"><input type="radio" id="%s" name="%s" value="%s"%s>'
                     '<span>%s</span></label>' % (ident, ident, name, e(val), extra, lib))
        h.append("</div>")
        return "".join(h)

    def choix(self, w):
        name = self.nom(w["name"])
        self.defs.append({"type": "choix", "name": name, "bonne": w["bonne"],
                          "retours": w.get("retours", {}), "indice": w.get("indice")})
        return ('<fieldset class="qcm-groupe"><legend>%s <span class="encoche" data-pour="%s"></span></legend>%s</fieldset>'
                % (w["legende"], name, self.options(name, w["options"])))

    def cases(self, w):
        name = self.nom(w["name"])
        toutes = [v for v, _ in w["options"]]
        self.defs.append({"type": "cases", "name": name, "toutes": toutes, "bonnes": w["bonnes"],
                          "retours": w.get("retours", {}), "indice": w.get("indice")})
        h = ['<fieldset class="qcm-groupe"><legend>%s <span class="note">(plusieurs réponses possibles)</span></legend><div class="options">' % w["legende"]]
        for i, (val, lib) in enumerate(w["options"]):
            ident = "%s-%d" % (name, i)
            h.append('<label class="option" for="%s"><input type="checkbox" id="%s" name="%s" value="%s">'
                     '<span>%s <span class="encoche" data-pour="%s::%d"></span></span></label>'
                     % (ident, ident, name, e(val), lib, name, i))
        h.append("</div></fieldset>")
        return "".join(h)

    def classer(self, w):
        items = []
        h = []
        if w.get("intro"):
            h.append("<div>%s</div>" % w["intro"])
        for i, (lib, bonne, indice) in enumerate(w["items"]):
            name = self.nom("%s_%d" % (w["name"], i))
            items.append({"name": name, "bonne": bonne, "indice": indice})
            h.append('<fieldset class="qcm-groupe"><legend>%s <span class="encoche" data-pour="%s"></span></legend>%s</fieldset>'
                     % (lib, name, self.options(name, w["categories"])))
        self.defs.append({"type": "classer", "items": items})
        return "".join(h)

    def liste(self, w):
        name = self.nom(w["name"])
        self.defs.append({"type": "liste", "name": name, "min": w["min"], "attendus": w["attendus"],
                          "refuses": w.get("refuses", []), "inconnu": w.get("inconnu"), "vide": w.get("vide")})
        h = ['<label class="champ" for="%s">%s <span class="encoche" data-pour="%s"></span></label>' % (name, w["label"], name),
             '<textarea id="%s" name="%s" rows="%d" spellcheck="true"></textarea>' % (name, name, w.get("lignes", 6))]
        if w.get("etayage"):
            h.append(self.etayage(w["etayage"]))
        return "".join(h)

    def texte(self, w):
        name = self.nom(w["name"])
        crit = [{"motifs": c["motifs"], "min": c.get("min", 1), "manque": c["manque"]} for c in w["criteres"]]
        self.defs.append({"type": "texte", "name": name, "criteres": crit, "minCar": w.get("minCar", 12),
                          "interdits": w.get("interdits", []), "vide": w.get("vide")})
        miroir = (' data-miroir="%s"' % w["miroir"]) if w.get("miroir") else ""
        h = ['<label class="champ" for="%s">%s <span class="encoche" data-pour="%s"></span></label>' % (name, w["label"], name),
             '<textarea id="%s" name="%s" rows="%d" spellcheck="true"%s></textarea>' % (name, name, w.get("lignes", 3), miroir)]
        h.append('<div class="note">Ce que je regarde dans ta réponse&nbsp;:<ul>')
        for i, c in enumerate(w["criteres"]):
            h.append('<li>%s <span class="encoche" data-pour="%s::%d"></span></li>' % (c["label"], name, i))
        h.append("</ul></div>")
        if w.get("etayage"):
            h.append(self.etayage(w["etayage"]))
        return "".join(h)

    def slots(self, w):
        defs = []
        h = []
        if w.get("intro"):
            h.append("<div>%s</div>" % w["intro"])
        for s in w["slots"]:
            name = self.nom(s["name"])
            defs.append({"name": name, "bonnes": s["bonnes"], "groupe": s.get("groupe"), "indice": s.get("indice")})
            h.append('<fieldset class="qcm-groupe"><legend>%s <span class="encoche" data-pour="%s"></span></legend>%s</fieldset>'
                     % (s["legende"], name, self.options(name, [(o, o) for o in s["options"]], miroir=s.get("cible"))))
        self.defs.append({"type": "slots", "slots": defs})
        return "".join(h)

    def croquis(self, w, cle):
        name = self.nom(w["name"])
        self.defs.append({"type": "croquis", "name": name, "cle": cle, "minTraits": w.get("minTraits", 4),
                          "checklist": [c for c in w["checklist"]], "vide": w.get("vide")})
        h = ['<p class="champ" id="%s-lab"><b>%s</b> <span class="encoche" data-pour="%s"></span></p>' % (name, w["label"], name),
             '<div class="croquis-boite">',
             '<div class="croquis-outils" role="toolbar" aria-label="Outils du croquis">',
             '<button type="button" class="btn" data-outil="crayon" aria-pressed="true">✏ Crayon fin</button>',
             '<button type="button" class="btn" data-outil="epais" aria-pressed="false">🖊 Trait épais</button>',
             '<button type="button" class="btn" data-outil="rouge" aria-pressed="false">🔴 Crayon rouge (cotes, flèches)</button>',
             '<button type="button" class="btn" data-outil="gomme" aria-pressed="false">🧽 Gomme</button>',
             '<button type="button" class="btn ghost" data-action="annuler">↶ Annuler le dernier trait</button>',
             '<button type="button" class="btn ghost" data-action="effacer">🗑 Tout effacer</button>',
             '</div>',
             '<canvas class="croquis-zone" width="760" height="440" data-cle-croquis="%s__croquis" '
             'aria-labelledby="%s-lab" role="img" tabindex="0">Zone de dessin</canvas>' % (cle, name),
             '</div>',
             '<label class="champ" for="%s_desc">Si tu ne peux pas dessiner à l\'écran&nbsp;: décris ton croquis en mots '
             '(ce que l\'on voit, où, avec quelles légendes)</label>' % name,
             '<textarea id="%s_desc" name="%s_desc" rows="3"></textarea>' % (name, name),
             self.etayage(["Au centre de mon croquis, on voit …", "Les légendes nomment …", "La flèche montre …"]),
             '<fieldset class="qcm-groupe"><legend>Je relis mon croquis&nbsp;: je coche ce qui y est vraiment</legend><div class="options">']
        for i, c in enumerate(w["checklist"]):
            ident = "%s_check-%d" % (name, i)
            h.append('<label class="option" for="%s"><input type="checkbox" id="%s" name="%s_check" value="%d"><span>%s</span></label>'
                     % (ident, ident, name, i, c))
        h.append("</div></fieldset>")
        return "".join(h)

    def etayage(self, amorces):
        return ('<details class="etayage"><summary>🪜 Version étayée : des débuts de phrase pour t\'aider</summary><ul>%s</ul></details>'
                % "".join("<li>%s</li>" % a for a in amorces))


def figure(doc, base_rel=""):
    """Un document lu par l'élève : SVG dans la page, ou image du dossier Images/."""
    h = ['<figure class="figure">']
    if doc.get("svg"):
        h.append(doc["svg"])
    else:
        h.append('<img src="%s%s" alt="%s" loading="lazy">' % (base_rel, doc["src"], e(doc["alt"])))
    if doc.get("legende"):
        h.append("<figcaption>%s <span class=\"note\">(clique sur l'image pour l'agrandir)</span></figcaption>" % doc["legende"])
    h.append("</figure>")
    if doc.get("description"):
        h.append('<details class="description"><summary>📝 Ce que montre le schéma, en mots</summary>%s</details>' % doc["description"])
    return "".join(h)


def correction_demo(lignes):
    h = ['<div class="demo">']
    for l in lignes:
        if isinstance(l, tuple):
            genre, contenu = l
        else:
            genre, contenu = "ligne", l
        h.append('<div class="ligne%s">%s</div>' % (" conclusion" if genre == "conclusion" else "", contenu))
    h.append("</div>")
    return "".join(h)


def mots(liste):
    if not liste:
        return ""
    return ('<details class="mots"><summary>📖 Les mots de cet exercice</summary><dl>%s</dl></details>'
            % "".join("<dt>%s</dt><dd>%s</dd>" % (m, d) for m, d in liste))


def exercice(ex, numero, uid, cle, base_img="", balise="h2", duree_au_titre=True):
    """Rend la carte d'un exercice ; renvoie (html, def_json).
    `balise` : le niveau du titre (h2 dans une page d'atelier, plus bas quand l'exercice est
    incrusté dans une activité de séquence)."""
    r = Rendu(uid)
    corps = []
    for w in ex["widgets"]:
        t = w["type"]
        if t == "croquis":
            corps.append(r.croquis(w, cle))
        else:
            corps.append(getattr(r, t)(w))
    code = ex["code"]
    h = ['<section class="card exercice" id="%s" data-exo="%s" data-cle="%s" aria-labelledby="%s-titre">' % (uid, uid, cle, uid),
         ('<%s id="%s-titre">Exercice %d — %s <span class="note">(≈ %d min)</span></%s>' % (balise, uid, numero, ex["titre"], ex["duree"], balise))
         if duree_au_titre else ('<%s id="%s-titre">Exercice %d — %s</%s>' % (balise, uid, numero, ex["titre"], balise)),
         '<div class="meta"><b>🎯 Objectif&nbsp;:</b> %s<br><b>🧩 Compétence&nbsp;:</b> <span title="%s" aria-label="%s : %s">%s</span>'
         '<br><b>✍ Ce que tu produis&nbsp;:</b> %s%s</div>'
         % (ex["objectif"], e(formulation(code)), e(code), e(formulation(code)), e(code), ex["production"],
            "" if duree_au_titre else "<br><b>Durée&nbsp;:</b> environ %d minutes, comptées dans celle de l'activité." % ex["duree"]),
         mots(ex.get("mots"))]
    for doc in ex.get("documents", []):
        corps_doc = figure(doc, base_img)
        h.append(corps_doc)
    if ex.get("intro"):
        h.append('<div>%s</div>' % ex["intro"])
    h.append('<div class="consigne">%s</div>' % ex["consigne"])
    if ex.get("critere"):
        h.append('<p class="critere"><b>✅ Tu as réussi si…</b> %s</p>' % ex["critere"])
    h.extend(corps)
    h.append('<p><button type="button" class="btn verifier">✔ Vérifier mes réponses</button></p>')
    h.append('<div class="retour" data-retour aria-live="polite"></div>')
    aides = ex.get("aides", [])
    if aides:
        h.append('<details class="aide"><summary>💡 Aide 1 — pour démarrer</summary>%s</details>' % aides[0])
    if len(aides) > 1:
        jumeau = ""
        if ex.get("jumeau"):
            jumeau = ('<div class="critere"><b>🔁 Exercice jumeau, à faire seul ensuite&nbsp;:</b> %s</div>' % ex["jumeau"]["consigne"])
            jumeau += ('<label class="champ" for="%s__jumeau">Ma réponse à l\'exercice jumeau</label>'
                       '<textarea id="%s__jumeau" name="%s__jumeau" rows="2"></textarea>'
                       '%s<details class="correction"><summary>🔍 Correction de l\'exercice jumeau</summary>%s</details>'
                       % (uid, uid, uid, r.etayage(ex["jumeau"].get("amorces", ["Dans cette nouvelle situation, je pose la même question que dans l'aide 2 : …",
                                                                                    "Ma réponse : … parce que …"])), ex["jumeau"]["correction"]))
        h.append('<details class="aide"><summary>💡 Aide 2 — le raisonnement pas à pas</summary>%s%s</details>' % (aides[1], jumeau))
    h.append('<details class="correction"><summary>🔍 La correction complète, et pourquoi</summary>%s</details>'
             % correction_demo(ex["correction"]))
    if ex.get("retenir"):
        h.append('<p class="retenir"><b>📌 À retenir&nbsp;:</b> %s</p>' % ex["retenir"])
    if ex.get("piege"):
        h.append('<p class="piege"><b>⚠ Le piège classique&nbsp;:</b> %s</p>' % ex["piege"])
    h.append("</section>")
    return "".join(h), {"cle": cle, "widgets": r.defs}


# ─────────────────────────────────────────────────────────────────────────────
# La page d'atelier d'un niveau
# ─────────────────────────────────────────────────────────────────────────────
def entete(titre_onglet, description, css_extra=""):
    return ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="description" content="%s">\n<title>%s</title>\n<style>\n%s%s</style>\n</head>\n'
            % (e(description), e(titre_onglet), KIT_CSS, css_extra))


def loupe():
    """L'agrandisseur d'images du site (images et schémas), recopié tel quel."""
    src = (DEPOT / "theme-3-creation-conception-realisation-innovations" / "audit" / "loupe.py").read_text(encoding="utf-8")
    ns = {}
    exec(compile(src.split("\ndef injectable")[0], "loupe", "exec"), ns)
    return ns["BLOC"]


LOUPE = loupe()


def fin_page(donnees):
    return ('<script type="application/json" id="donnees-page">%s</script>\n<script>\n%s</script>\n%s</body>\n</html>\n'
            % (json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/"), KIT_JS, LOUPE))


def avant_de_commencer(liste, cle):
    h = ['<section class="card" data-cle="%s"><h2>🔄 Avant de commencer&nbsp;: ce que je vérifie</h2>' % cle,
         '<p>Coche ce que tu sais déjà faire. Pour ce qui n\'est pas encore en place, ouvre le lien&nbsp;: '
         'il te donne de quoi le rattraper en quelques minutes.</p><ul class="verif-liste">']
    for i, (texte, code, lien, libelle) in enumerate(liste):
        ident = "%s-%d" % (cle, i)
        h.append('<li><label for="%s"><input type="checkbox" id="%s" name="avant" value="%d"><span>%s '
                 '<span class="code">(%s)</span></span></label>' % (ident, ident, i, texte, e(code)))
        if lien:
            h.append('<div class="note">Pour le rattraper&nbsp;: <a href="%s">%s</a></div>' % (e(lien), libelle))
        h.append("</li>")
    h.append("</ul></section>")
    return "".join(h)


def page_atelier(at, niv, chemins):
    """at : module de données ; niv : '5e' ; chemins : dict des liens calculés."""
    N = at.NIVEAUX[niv]
    slug = at.SLUG
    page_id = "rep_%s_%s" % (slug, niv)
    codes = N["codes"]
    exos_html, defs, onglets, panneaux = [], {}, [], []
    total_min = sum(x["duree"] for x in N["exercices"])
    for i, ex in enumerate(N["exercices"]):
        uid = "%s_%s_%s" % (at.COURT, niv, ex["id"])
        cle = "rep_%s_%s_%s" % (slug, niv, ex["id"])
        h, d = exercice(ex, i + 1, uid, cle)
        defs[uid] = d
        onglets.append(('Exercice %d<span class="etat" id="onglet-etat-%s">à faire</span>' % (i + 1, uid), "p-" + uid))
        suivant_lib = ("Exercice %d" % (i + 2)) if i + 1 < len(N["exercices"]) else "Pour finir"
        panneaux.append((h + '<p><button type="button" class="btn suivant" data-vers="%d">%s ›</button></p>'
                         % (i + 1, suivant_lib), "p-" + uid))
    # La clôture : à retenir → Bonus → Bilan → QCM
    fin = [cloture(at, niv, chemins)]
    onglets.append(('🏁 Pour finir<span class="etat">retenir, bonus, bilan</span>', "p-fin"))
    panneaux.append(("".join(fin), "p-fin"))

    titre = "%s %s" % (at.EMOJI, at.TITRE)
    h = [entete("Thème 1 · %s — Atelier : %s (%s)" % (niv, at.TITRE_COURT, " · ".join(codes)),
                "Atelier de %s : %s — exercices corrigés, %s." % (niv, at.TITRE_COURT, " · ".join(codes))),
         '<body>\n<a class="evitement" href="#contenu">Aller au contenu</a>\n',
         navigation(chemins, niv),
         '<main id="contenu" class="page">',
         '<h1>%s</h1>' % titre,
         '<p class="mission">%s</p>' % N["mission"],
         '<div class="toolbar"><button type="button" class="btn" id="btnImprimer">🖨 Imprimer</button>'
         '<button type="button" class="btn ghost" id="btnEffacer">🗑 Effacer ma sauvegarde</button>'
         '<button type="button" class="btn ghost" id="btnEssentiel" aria-pressed="false">🎯 Mode essentiel : désactivé</button></div>',
         '<p class="note" id="noteSauvegarde" style="text-align:center" aria-live="polite">Ton travail s\'enregistre tout seul dans ce navigateur.</p>',
         '<div class="etiquettes">',
         '<span class="etiquette niveau" title="Niveau de classe" aria-label="Niveau : %s">%s</span>' % (niv, niv)]
    for c in codes:
        h.append('<span class="etiquette code" title="%s" aria-label="Compétence %s : %s">%s</span>' % (e(formulation(c)), e(c), e(formulation(c)), e(c)))
    h.append('<span class="etiquette duree" title="Durée indicative de tous les exercices" aria-label="Durée indicative : environ %d minutes">⏱ ≈ %d min</span>' % (total_min, total_min))
    h.append('<span class="etiquette" title="%s" aria-label="Représentation : %s">%s</span>' % (e(at.TITRE_COMPLET), e(at.TITRE_COMPLET), e(at.ETIQUETTE)))
    h.append("</div>")
    # Ouverture (repliée à partir du 2e onglet)
    h.append('<details class="rappel-ouverture" open><summary>📖 Rappel : la situation et ton hypothèse</summary>')
    h.append(avant_de_commencer(N["avant"], page_id + "__avant"))
    h.append('<section class="card"><h2>🧭 %s</h2>%s</section>' % (N["situation_titre"], N["situation"]))
    h.append('<section class="card" data-cle="%s__hyp"><h2>💭 Ton hypothèse de départ</h2>'
             '<p><b>La question&nbsp;:</b> %s</p><label class="champ" for="%s__hyp_t">Ce que je pense avant les exercices</label>'
             '<textarea id="%s__hyp_t" name="hyp" rows="3"></textarea>%s</section>'
             % (page_id, N["question"], page_id, page_id, Rendu("x").etayage(N["hypothese_amorces"])))
    h.append("</details>")
    h.append('<div class="progression"><div class="barre" aria-hidden="true"><div id="barreProgression"></div></div>'
             '<p id="texteProgression" aria-live="polite"></p></div>')
    h.append('<div class="onglets" role="tablist" aria-label="Les exercices de l\'atelier">')
    for i, (lib, pid) in enumerate(onglets):
        h.append('<button type="button" class="onglet" role="tab" id="tab-%s" aria-controls="%s" aria-selected="%s" tabindex="%d">%s</button>'
                 % (pid, pid, "true" if i == 0 else "false", 0 if i == 0 else -1, lib))
    h.append("</div>")
    for i, (contenu, pid) in enumerate(panneaux):
        h.append('<section class="panneau" role="tabpanel" id="%s" aria-labelledby="tab-%s"%s>%s</section>'
                 % (pid, pid, "" if i == 0 else " hidden", contenu))
    h.append("</main>")
    h.append('<footer class="pied"><p>%s</p><p>Technologie cycle 4 · programme 2024 · page utilisable sans Internet · '
             'ton travail reste dans ce navigateur, rien n\'est envoyé.</p></footer>' % at.MENTION_FICTION)
    h.append(fin_page({"page": page_id, "exercices": defs}))
    return "".join(h)


def navigation(chemins, niv):
    liens = ['<a href="%s">&#8962; Accueil</a>' % chemins["accueil"]]
    if chemins.get("sequence"):
        liens.append('<a href="%s">&#8592; Revenir à la séquence</a>' % chemins["sequence"])
    liens.append('<a href="%s">📒 Mon cahier de %s</a>' % (chemins["cahier"], niv))
    liens.append('<a href="%s">🧭 Toutes les représentations</a>' % chemins["carte"])
    if chemins.get("qcm"):
        liens.append('<a href="%s">🧠 Le QCM</a>' % chemins["qcm"])
    return '<nav id="navharm" aria-label="Navigation du site">%s</nav>\n' % "".join(liens)


def cloture(at, niv, chemins):
    N = at.NIVEAUX[niv]
    pid = "rep_%s_%s" % (at.SLUG, niv)
    h = ['<section class="card"><h2>📌 À retenir de l\'atelier</h2>%s' % N["a_retenir"]]
    if chemins.get("synthese"):
        h.append('<p>📜 La trace à garder&nbsp;: <a href="%s">la synthèse de l\'atelier</a>, à imprimer ou à recopier.</p>' % chemins["synthese"])
    h.append("</section>")
    # Bonus
    h.append('<section class="card bonus" data-cle="%s__bonus"><h2>🎁 Bonus (facultatif — hors parcours obligatoire)</h2>' % pid)
    for i, b in enumerate(N["bonus"]):
        h.append('<h3>Défi %d — %s</h3><div>%s</div>' % (i + 1, b["titre"], b["consigne"]))
        h.append('<label class="champ" for="%s__bonus%d">Ma réponse</label><textarea id="%s__bonus%d" name="bonus%d" rows="3"></textarea>'
                 % (pid, i, pid, i, i))
        h.append(Rendu("x").etayage(b.get("amorces", ["Je relis la question du défi : on me demande …", "Ma réponse : … parce que …"])))
        h.append('<details class="corrige-bonus"><summary>🔍 Voir la correction du défi %d</summary>%s</details>'
                 % (i + 1, correction_demo(b["correction"])))
    h.append("</section>")
    # Bilan
    h.append('<section class="card bilan" data-cle="%s__bilan"><h2>🏁 Bilan</h2>' % pid)
    h.append('<p><b>Retour à ton hypothèse.</b> La question était&nbsp;: %s</p>' % N["question"])
    h.append('<label class="champ" for="%s__bilan_h">Relis ton hypothèse de départ (onglet 1). Qu\'est-ce que tu gardes, qu\'est-ce que tu changes&nbsp;?</label>'
             '<textarea id="%s__bilan_h" name="bilan_h" rows="3"></textarea>' % (pid, pid))
    h.append(Rendu("x").etayage(["Au départ je pensais que… ; maintenant je sais que…",
                                 "Je garde l'idée que… parce que…",
                                 "Je change d'avis sur… : l'exercice … m'a montré que…"]))
    h.append('<label class="champ" for="%s__bilan_m">%s</label><textarea id="%s__bilan_m" name="bilan_m" rows="3"></textarea>'
             % (pid, N.get("metacognition", "Où as-tu hésité&nbsp;? Qu'est-ce que tu dois encore revoir, et comment vas-tu t'y prendre&nbsp;?"), pid))
    h.append(Rendu("x").etayage(["J'ai hésité entre … et … dans l'exercice …", "Je dois encore revoir … ; pour cela, je vais refaire …"]))
    h.append('<h3>Je me positionne</h3><p class="lsu-legende">Pour chaque compétence travaillée, choisis la phrase qui te ressemble aujourd\'hui. '
             'Ce n\'est pas une note&nbsp;: c\'est ce qui t\'aide, toi et ton professeur, à savoir quoi reprendre.</p>')
    for c in N["codes"]:
        name = "pos_%s" % c.replace(".", "_")
        h.append('<fieldset class="qcm-groupe"><legend>%s <span class="note">(%s)</span></legend><div class="options">'
                 % (avec_sigles(formulation(c)), e(c)))
        for j, niveau in enumerate(LSU):
            ident = "%s__%s-%d" % (pid, name, j)
            h.append('<label class="option" for="%s"><input type="radio" id="%s" name="%s" value="%d"><span>%s</span></label>'
                     % (ident, ident, name, j, niveau))
        h.append("</div></fieldset>")
    h.append("</section>")
    # QCM
    if chemins.get("qcm"):
        h.append('<section class="card"><h2>🧠 Prêt·e à t\'entraîner&nbsp;?</h2><p>Le QCM de cet atelier compte <b>%d questions</b>, '
                 'dont <b>%d illustrées</b>, chacune avec sa correction complète. Il va de la 5e à la 3e&nbsp;: '
                 'tu peux choisir de ne travailler que les questions de ton niveau.</p>'
                 '<p><a class="btn qcm" href="%s">🧠 Ouvrir le QCM de l\'atelier</a></p></section>'
                 % (chemins["qcm_nb"], chemins["qcm_illustrees"], chemins["qcm"] + chemins.get("qcm_ancre", "")))
    return "".join(h)
