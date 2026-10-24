# -*- coding: utf-8 -*-
"""Assemble les ateliers des représentations.

    python3 build.py              # toutes les représentations, les cahiers, les panneaux
    python3 build.py interacteurs # une seule représentation (nom du module sans « donnees_ »)

Écrit, pour chaque représentation <slug> :
  ../<slug>/atelier_<niv>_<slug>.html   une page par niveau servi
  ../<slug>/Images/*.svg                les dessins lus hors de la page (QCM, synthèses)
  ../<slug>/Synthèses/…                  synthèses élève et professeur
  <dossier du code>/atelier_<…>.html    un panneau dans le dossier de chaque code servi
puis les cahiers de niveau ../cahiers/cahier_<niv>_representations.html.

Le QCM s'assemble à part : build_qcm.py.
"""
import importlib
import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

import moteur  # noqa: E402
import syntheses  # noqa: E402

RACINE = moteur.RACINE_ATELIERS
DEPOT = moteur.DEPOT
CARTE = moteur.THEME1 / "_reperes" / "carte_des_representations.html"
CAHIERS = RACINE / "cahiers"

#: L'ordre est celui de la démarche : analyse externe, analyse interne, conception.
MODULES = ["besoin", "interacteurs", "exigences", "cas_utilisation", "croquis", "fast", "carte_mentale"]


def charger(noms=None):
    out = []
    for n in (noms or MODULES):
        try:
            out.append(importlib.import_module("donnees_" + n))
        except ModuleNotFoundError as err:
            if noms:
                raise
            print("  (pas encore de données pour « %s » : %s)" % (n, err))
    return out


def dossier(at):
    return RACINE / at.SLUG


def page_niveau(at, niv):
    return dossier(at) / ("atelier_%s_%s.html" % (niv, at.SLUG))


def qcm(at):
    return dossier(at) / ("qcm_%s.html" % at.SLUG)


def synthese_eleve(at):
    return dossier(at) / "Synthèses" / ("synthese_eleve_%s.html" % at.SLUG)


def synthese_prof(at):
    return dossier(at) / "Synthèses" / ("synthese_professeur_%s.html" % at.SLUG)


def cahier(niv):
    return CAHIERS / ("cahier_%s_representations.html" % niv)


def compte_qcm(at):
    """(nb de questions, nb illustrées), lus dans la banque — jamais recopiés."""
    try:
        q = importlib.import_module("q_" + at.MODULE)
        return len(q.Q), sum(1 for x in q.Q if "img" in x)
    except ModuleNotFoundError:
        return None


def resoudre(lien, at, niv, depuis):
    """Les liens de rattrapage écrits « @synthese#ancre » ou « @niveau:5e#ancre »."""
    if not lien or not lien.startswith("@"):
        return lien
    cible, _, ancre = lien[1:].partition("#")
    if cible == "synthese":
        chemin = synthese_eleve(at)
    elif cible.startswith("niveau:"):
        chemin = page_niveau(at, cible.split(":")[1])
    elif cible.startswith("atelier:"):
        _, nom, n2 = cible.split(":")
        autre = importlib.import_module("donnees_" + nom)
        chemin = page_niveau(autre, n2)
    else:
        raise SystemExit("Lien de rattrapage inconnu : %s" % lien)
    return moteur.rel(depuis, chemin) + ("#" + ancre if ancre else "")


def chemins(at, niv, depuis):
    seq = moteur.sequence_du_code(at.NIVEAUX[niv]["codes"][0])
    c = {"accueil": moteur.rel(depuis, DEPOT / "index.html"),
         "sequence": moteur.rel(depuis, seq) if seq else None,
         "cahier": moteur.rel(depuis, cahier(niv)),
         "carte": moteur.rel(depuis, CARTE),
         "synthese": moteur.rel(depuis, synthese_eleve(at))}
    n = compte_qcm(at)
    if n:
        c.update(qcm=moteur.rel(depuis, qcm(at)), qcm_nb=n[0], qcm_illustrees=n[1], qcm_ancre="?codes=" + ",".join(at.NIVEAUX[niv]["codes"]))
    return c


def preparer(at):
    """Les liens « @… » de l'ouverture deviennent des chemins réels, niveau par niveau."""
    for niv, N in at.NIVEAUX.items():
        depuis = dossier(at)
        N["avant"] = [(t, code, resoudre(l, at, niv, depuis), lib) for (t, code, l, lib) in N["avant"]]


def ecrire(chemin, contenu):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    ancien = chemin.read_text(encoding="utf-8") if chemin.exists() else None
    if ancien != contenu:
        chemin.write_text(contenu, encoding="utf-8")
        return True
    return False


def ecrire_images(at):
    n = 0
    for nom, contenu in getattr(at, "IMAGES", {}).items():
        n += ecrire(dossier(at) / "Images" / nom, '<?xml version="1.0" encoding="UTF-8"?>\n' + contenu + "\n")
    return n


def ecrire_sources(at):
    """SOURCES_MEDIAS.md : d'où vient chaque image du dossier (toutes sont écrites par programme)."""
    lignes = ["# Sources des médias — atelier « %s »" % at.TITRE_COURT, "",
              "Toutes les images de ce dossier sont des **SVG originaux**, écrits par programme pour ce dépôt "
              "(`_generation/figures.py` pour les schémas, `_generation/dessins.py` pour les scènes). Aucune image "
              "n'est reprise d'un manuel, d'un site ou d'une banque d'images.", "",
              "| Fichier | Nature | Auteur | Licence | Ce que l'élève en fait |", "|---|---|---|---|---|"]
    for nom, contenu in sorted(getattr(at, "IMAGES", {}).items()):
        m = re.search(r"<title[^>]*>(.*?)</title>", contenu)
        titre = moteur.html.unescape(m.group(1)) if m else nom
        role = getattr(at, "ROLES_IMAGES", {}).get(nom, titre)
        lignes.append("| `Images/%s` | SVG original, écrit par programme | Claude (Anthropic), pour ce dépôt | CC0 1.0 | %s |"
                      % (nom, role.replace("|", "/")))
    lignes += ["", "Les schémas des pages d'atelier sont écrits **dans** la page (SVG en ligne) par le même générateur : "
               "la version « à compléter » et la version « corrigée » sont le même dessin, case pour case.", ""]
    return ecrire(dossier(at) / "SOURCES_MEDIAS.md", "\n".join(lignes))


def ecrire_atelier(at):
    faits = []
    for niv in at.NIVEAUX:
        p = page_niveau(at, niv)
        html = moteur.page_atelier(at, niv, chemins(at, niv, p.parent))
        ecrire(p, html)
        faits.append(p)
    return faits


# ─────────────────────────────────────────────────────────────────────────────
# Panneaux dans le dossier de chaque code servi (une ressource partagée doit
# être atteignable depuis chaque code qu'elle sert)
# ─────────────────────────────────────────────────────────────────────────────
PANNEAU_CSS = """body{background:#050f24;color:#e4eaf5;font-family:'Segoe UI',system-ui,sans-serif;line-height:1.6;margin:0;padding:0 0 40px}
.page{max-width:760px;margin:0 auto;padding:0 18px}h1{color:#81aaff;font-size:1.45em;margin:26px 0 6px}
.sous{color:#9bbefc;margin:0 0 18px}.card{background:#0d2347;border:1px solid #274a8a;border-radius:12px;padding:16px 20px;margin:16px 0}
a,a:where(:visited){color:#61dafb}.btn{display:inline-block;background:#1d4e89;color:#fff!important;text-decoration:none;padding:11px 18px;border-radius:10px;font-weight:700;margin-top:6px}
.note{color:#9bbefc;font-size:.92em}b{color:#c68ef2}
#navharm{display:flex;flex-wrap:wrap;gap:10px;max-width:760px;margin:14px auto 0;padding:0 18px}
#navharm a{padding:6px 12px;border:1.5px solid #274a8a;border-radius:999px;background:#0d2347;color:#9bbefc;font-size:.92em;text-decoration:none;line-height:1.2}
.evitement{position:absolute;left:-9999px}.evitement:focus{left:10px;top:10px;background:#fff;color:#000;padding:8px}
@media print{body{background:#fff;color:#111}.card{background:#fff;border-color:#999}h1{color:#111}#navharm{display:none}
a,a:visited{color:#00309e!important}.btn{background:#fff!important;color:#00309e!important;border:1px solid #00309e}b{color:#5a1a9a}.note,.sous{color:#1a3a7a}}
"""


def nom_panneau(at):
    return "atelier_%s.html" % at.NOM_PANNEAU


def ecrire_panneaux(at):
    faits = []
    for niv, N in at.NIVEAUX.items():
        for code in N["codes"]:
            d = moteur.dossier_code(code)
            if not d.is_dir():
                raise SystemExit("Dossier du code introuvable : %s" % d)
            p = d / nom_panneau(at)
            seq = moteur.sequence_du_code(code)
            n = compte_qcm(at)
            liens = ['<a href="%s">&#8962; Accueil</a>' % moteur.rel(d, DEPOT / "index.html")]
            if seq:
                liens.append('<a href="%s">&#8592; Revenir à la séquence</a>' % moteur.rel(d, seq))
            if n:
                liens.append('<a href="%s">&#129504; Le QCM</a>' % moteur.rel(d, qcm(at)))
            corps = [
                '<!DOCTYPE html>\n<html lang="fr">\n<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">',
                '<meta name="description" content="%s">' % moteur.e("Atelier de %s : %s, pour le code %s." % (niv, at.TITRE_COURT, code)),
                '<title>%s</title>' % moteur.e("%s — Atelier : %s (%s)" % (niv, at.TITRE_COURT, code)),
                "<style>%s</style></head>\n<body>" % PANNEAU_CSS,
                '<a class="evitement" href="#contenu">Aller au contenu</a>',
                '<nav id="navharm" aria-label="Navigation du site">%s</nav>' % "".join(liens),
                '<main id="contenu" class="page">',
                "<h1>%s %s</h1>" % (at.EMOJI, at.TITRE),
                '<p class="sous">%s · %s — %s</p>' % (niv, code, moteur.avec_sigles(moteur.formulation(code))),
                '<div class="card"><p>%s</p>' % at.PANNEAU_TEXTE[niv],
                '<p><a class="btn" href="%s">%s Ouvrir l\'atelier de %s</a></p>' % (moteur.rel(d, page_niveau(at, niv)), at.EMOJI, niv),
                '<p class="note">%d exercices corrigés, environ %d minutes en tout. Ton travail s\'enregistre dans ce navigateur, '
                'et se retrouve aussi dans <a href="%s">ton cahier de %s</a>, qui rassemble les exercices de toutes les représentations.</p></div>'
                % (len(N["exercices"]), sum(x["duree"] for x in N["exercices"]), moteur.rel(d, cahier(niv)), niv),
            ]
            if n:
                corps.append('<div class="card"><p>Pour t\'entraîner ensuite&nbsp;: <a href="%s">&#129504; le QCM de l\'atelier</a> — '
                             '%d questions, dont %d illustrées. Il va de la 5e à la 3e&nbsp;: tu peux ne garder que les questions de '
                             'ton niveau.</p></div>' % (moteur.rel(d, qcm(at)) + "?codes=" + code, n[0], n[1]))
            corps.append('<div class="card"><p>Les autres façons de représenter une idée technique&nbsp;: '
                         '<a href="%s">🧭 la carte des représentations</a>.</p></div>' % moteur.rel(d, CARTE))
            corps.append("</main></body></html>\n")
            ecrire(p, "\n".join(corps))
            faits.append(p)
    return faits


def main(argv):
    noms = argv[1:] or None
    ats = charger(noms)
    for at in ats:
        preparer(at)
    for at in ats:
        n_img = ecrire_images(at)
        ecrire_sources(at)
        pages = ecrire_atelier(at)
        pann = ecrire_panneaux(at)
        syn = syntheses.ecrire(at, page_niveau, synthese_eleve, synthese_prof, chemins, ecrire)
        print("%-24s %d page(s) de niveau · %d panneau(x) · %d image(s) · %d synthèse(s)"
              % (at.SLUG, len(pages), len(pann), n_img, syn))
    if not noms:
        import cahiers
        tous = charger()
        n = cahiers.ecrire(tous, cahier, page_niveau, chemins, ecrire)
        print("cahiers : %d page(s)" % n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
