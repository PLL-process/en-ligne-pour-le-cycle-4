#!/usr/bin/env python3
"""replier_referentiel.py — le référentiel revient sur la page élève, replié.

LE CONSTAT (07/11/2026)
-----------------------
Depuis la règle d'or n°298 (15/09/2026), la carte « 📚 Le référentiel de la
séquence — en toutes lettres » a quitté les pages élèves pour la synthèse
professeur du lot, recopiée sans réécriture dans un
`<div class="bloc referentiel-eleve">`. Sur la page, il ne reste que les
étiquettes de codes, avec une infobulle au survol — et au doigt, rien ne
survole : Pascal, sur son téléphone, ne pouvait plus lire ce qu'est 5e_C2.1.

LA DÉCISION (n°298 amendée, 07/11/2026)
---------------------------------------
La carte revient sur la page, **repliée** : un `<details class="referentiel-replie">`
fermé par défaut, posé juste sous la ligne d'étiquettes. L'élève ne la lit
pas sans le vouloir (le constat du 15/09 tient) ; le professeur l'ouvre d'un
tap. Le contenu est la copie de la synthèse professeur, qui reste la
référence : ce script ne réécrit rien, il recopie.

CE QUE FAIT CE SCRIPT
---------------------
Pour chaque synthèse professeur qui porte un bloc `referentiel-eleve` :
  · lit, dans le commentaire qui le précède, le nom de la page élève d'origine ;
  · recopie le bloc, son `<h2>` devenant le `<summary>` du dépliant ;
  · l'insère après `<div class="badges">…</div>` (ou, à défaut, après `</h1>`) ;
  · ajoute la feuille de style du dépliant avant le premier `</style>`
    (masqué en mode essentiel, masqué à l'impression : un dépliant fermé n'a
    rien à imprimer).
Une page qui porte déjà `referentiel-replie` n'est pas touchée (rejouable).
Les pages engendrées par un générateur (ateliers) sont listées, pas modifiées :
c'est leur générateur qu'il faut changer.

    python3 _outils/replier_referentiel.py --etat      dit ce qui serait fait
    python3 _outils/replier_referentiel.py             applique
"""
import glob
import os
import re
import sys

RACINE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

CSS = """
/* n°298 amendée (07/11/2026) : le référentiel, replié sous les étiquettes */
details.referentiel-replie{margin:0 auto 14px;max-width:960px;border-left:4px solid var(--head,#c68ef2);border-radius:8px;padding:6px 12px;background:rgba(255,255,255,.04)}
details.referentiel-replie>summary{cursor:pointer;font-weight:600;color:var(--head,#c68ef2);list-style:none;display:flex;gap:8px;align-items:center;min-height:44px}
details.referentiel-replie>summary::-webkit-details-marker{display:none}
details.referentiel-replie>summary::before{content:"▸";transition:transform .15s}
details.referentiel-replie[open]>summary::before{transform:rotate(90deg)}
details.referentiel-replie table{width:100%;border-collapse:collapse;font-size:.92em;margin:8px 0}
details.referentiel-replie th,details.referentiel-replie td{border:1px solid var(--border,#274a8a);padding:5px 8px;vertical-align:top;text-align:left}
details.referentiel-replie p{margin:8px 0}
body.essentiel details.referentiel-replie{display:none}
@media print{details.referentiel-replie{display:none}}
@media(prefers-reduced-motion:reduce){details.referentiel-replie>summary::before{transition:none}}
"""

COMMENTAIRE = ("<!-- n°298 amendée (07/11/2026) : le référentiel revient, replié, "
               "copie du bloc referentiel-eleve de la synthèse professeur -->")

GENEREES = ("ateliers-representations", "atelier-planification")


def bloc_equilibre(src, debut):
    """Le texte de `debut` (un <div …>) jusqu'à son </div> fermant."""
    prof = 0
    for m in re.finditer(r"<div\b|</div>", src[debut:]):
        prof += 1 if m.group(0) == "<div" else -1
        if prof == 0:
            return src[debut:debut + m.end()]
    raise ValueError("div non refermé")


def page_origine(commentaire):
    m = re.search(r"page élève\s+(\S+?\.html)", commentaire) or re.search(r"(\S+?\.html)", commentaire)
    return m.group(1) if m else None


#: La synthèse professeur peut parler de « dépôt » ; la page élève, non (règle n°309 : l'élève
#: lit le savoir, pas la fabrique). Ces deux phrases viennent du gabarit de la carte ; elles
#: prennent, sur la page, la forme que l'index a déjà depuis le 21/10/2026.
MOTS_DE_FABRIQUE = (
    ("sont des codes de classement <b>internes à ce dépôt</b>&nbsp;; ils ne figurent pas comme tels au BO.",
     "servent à ranger les séquences&nbsp;; ils ne viennent pas du programme officiel."),
    ("Le référentiel du dépôt rattache officiellement ces codes à",
     "Ces codes sont rattachés à"),
)


def depliant(bloc, remonter):
    """Le bloc recopié, son h2 devenu summary, ses mots de fabrique traduits, ses liens rebasés."""
    m = re.search(r"<h2[^>]*>(.*?)</h2>\s*", bloc, re.S)
    titre = re.sub(r"\s+", " ", m.group(1)).strip() if m else "📚 Le référentiel de la séquence — en toutes lettres"
    corps = bloc.replace(m.group(0), "", 1) if m else bloc
    for avant, apres in MOTS_DE_FABRIQUE:
        corps = corps.replace(avant, apres)
    if remonter:
        # la synthèse vit dans Synthèses/ : un lien « ../x » vu de là est « x » vu de la séquence
        corps = re.sub(r'(href|src)="\.\./', r'\1="', corps)
    return (f'\n{COMMENTAIRE}\n<details class="referentiel-replie">\n'
            f'  <summary>{titre}</summary>\n{corps}\n</details>\n')


def envelopper(corps, titre="📚 Le référentiel de la séquence — en toutes lettres"):
    """Le dépliant fermé autour d'un corps déjà écrit (pour les générateurs qui
    construisent la carte eux-mêmes, comme le moteur des ateliers des représentations)."""
    return (f'\n{COMMENTAIRE}\n<details class="referentiel-replie">\n'
            f'  <summary>{titre}</summary>\n<div class="bloc referentiel-eleve">\n{corps}\n</div>\n</details>\n')


def replier_depuis_synthese(page_src, chemin_synthese, remonter=True):
    """Pour un générateur : la page engendrée reçoit, repliée, la carte que sa synthèse
    professeur conserve. Lève une erreur si la synthèse n'a pas de bloc : une page
    engendrée doit porter elle-même tout ce que les règles exigent (même esprit que la
    loupe, règle n°92)."""
    src = open(chemin_synthese, encoding="utf-8").read()
    m = re.search(r'<div class="bloc referentiel-eleve[^"]*">', src)
    if not m:
        raise SystemExit("n°298 amendée : aucun bloc referentiel-eleve dans %s" % chemin_synthese)
    bloc = bloc_equilibre(src, m.start())
    nouveau, ou = inserer(page_src, depliant(bloc, remonter))
    if nouveau is None:
        raise SystemExit("n°298 amendée : ni étiquettes ni titre où poser le dépliant (%s)" % ou)
    return styler(nouveau)


def inserer(page_src, html):
    m = re.search(r'<div class="badges">|<div class="etiquettes">', page_src)
    if m:
        fin = m.start() + len(bloc_equilibre(page_src, m.start()))
        return page_src[:fin] + html + page_src[fin:], "après les étiquettes"
    m = re.search(r"</h1>\s*(<p class=\"sous\">.*?</p>)?", page_src, re.S)
    if m:
        return page_src[:m.end()] + html + page_src[m.end():], "après le titre"
    return None, "ni étiquettes ni titre"


def styler(page_src):
    if "details.referentiel-replie" in page_src:
        return page_src
    i = page_src.find("</style>")
    if i < 0:
        return page_src
    return page_src[:i] + CSS + page_src[i:]


def traiter(appliquer):
    faits, sautes, generees, erreurs = [], [], [], []
    for synth in sorted(glob.glob(os.path.join(RACINE, "theme-*", "**", "synthese_professeur_*.html"), recursive=True)):
        src = open(synth, encoding="utf-8").read()
        for m in re.finditer(r"<!--([^>]*?)-->\s*(?=<div class=\"bloc referentiel-eleve\">)", src):
            rel = os.path.relpath(synth, RACINE)
            if any(g in rel for g in GENEREES):
                generees.append(rel)
                continue
            page = page_origine(m.group(1))
            dossier = os.path.dirname(synth)
            remonter = os.path.basename(dossier) == "Synthèses"
            if remonter:
                dossier = os.path.dirname(dossier)
            chemin = os.path.join(dossier, page) if page else None
            if not chemin or not os.path.exists(chemin):
                erreurs.append((rel, page or "?"))
                continue
            page_src = open(chemin, encoding="utf-8").read()
            if 'class="referentiel-replie"' in page_src:
                sautes.append(os.path.relpath(chemin, RACINE))
                continue
            bloc = bloc_equilibre(src, m.end())
            nouveau, ou = inserer(page_src, depliant(bloc, remonter))
            if nouveau is None:
                erreurs.append((os.path.relpath(chemin, RACINE), ou))
                continue
            nouveau = styler(nouveau)
            if appliquer:
                open(chemin, "w", encoding="utf-8").write(nouveau)
            faits.append((os.path.relpath(chemin, RACINE), ou))
    return faits, sautes, generees, erreurs


if __name__ == "__main__":
    appliquer = "--etat" not in sys.argv
    faits, sautes, generees, erreurs = traiter(appliquer)
    verbe = "repliée sur" if appliquer else "à replier sur"
    for p, ou in faits:
        print(f"  ✔ {verbe} {p}  ({ou})")
    for p in sautes:
        print(f"  = déjà repliée : {p}")
    for p in sorted(set(generees)):
        print(f"  ⚙ page engendrée, générateur à modifier : {p}")
    for p, why in erreurs:
        print(f"  ✘ {p} — {why}")
    print(f"\n{len(faits)} page(s) {verbe.split()[0]}, {len(sautes)} déjà faite(s), "
          f"{len(set(generees))} engendrée(s) laissée(s), {len(erreurs)} erreur(s)")
    sys.exit(1 if erreurs else 0)
