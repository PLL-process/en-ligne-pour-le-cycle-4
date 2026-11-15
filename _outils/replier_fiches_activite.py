# -*- coding: utf-8 -*-
"""Replie la fiche de chaque activité (objectif, compétence, production attendue, ressources) dans un dépliant fermé.

    python3 _outils/replier_fiches_activite.py                 # toutes les séquences : ce qui serait replié
    python3 _outils/replier_fiches_activite.py --ecrire        # … et l'écrire
    python3 _outils/replier_fiches_activite.py <page.html> …   # seulement ces pages
    python3 _outils/replier_fiches_activite.py --etat          # pages à jour / à replier

Décision de Pascal du 15/11/2026 (révision des trois thèmes) : « replier les fiches d'activité sur toutes les
séquences ». La fiche d'une activité (100 à 130 mots, cinq fois dans une séquence de quatre séances) était la plus grosse
part de texte que l'élève lisait sans en avoir besoin pour faire : la consigne dit déjà quoi faire. Elle reste dans la
page, d'un tap, sous un résumé qui dit ce qu'elle contient ; le professeur l'ouvre pour présenter l'activité.

Trois formes, toutes reconnues par leur premier mot « Objectif » :
  · `<div class="meta-grid">` — la grille du gabarit commun (Objectif, Compétence, Production attendue, Ressources…) ;
  · `<div class="meta"><b>Objectif</b> … · <b>Compétences</b> …</div>` — la fiche en une ligne (thème 1) ;
  · `<p><b>Objectif&nbsp;:</b> …</p>` — la fiche en un paragraphe (familles C7/C8 du thème 3).
Chacune entre, telle quelle, dans `<details class="fiche-activite">` fermé ; le résumé nomme les rubriques présentes.
Rejouable : une fiche déjà repliée n'est pas touchée. À l'impression, la fiche papier ne montre pas un dépliant fermé :
la fiche d'activité ne s'imprime plus (une demi-ligne à quatre lignes de moins par activité). Le mode mission la range
dans l'en-tête de l'activité, comme la grille d'avant (`mission.js`).
"""
import pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CSS_MARQUE = "/* la fiche de l'activité, repliée (15/11/2026, _outils/replier_fiches_activite.py) */"
# posée avant le premier </style> de la page (comme replier_referentiel.py) : le générateur des quatre pages de 3e_C9.2
# reprend cette feuille-là, pas un <style> ajouté à part
CSS = ("\n" + CSS_MARQUE + "\n"
       "details.fiche-activite{margin:6px 0 10px}\n"
       "details.fiche-activite>summary{cursor:pointer;font-size:.9em;color:var(--sub,#9bbefc);min-height:24px;padding:2px 0}\n"
       "details.fiche-activite[open]>summary{margin-bottom:6px}\n")
# l'ordre du résumé, et le mot qui ouvre chaque rubrique (après son émoji) ; une étiquette en gras qui n'ouvre pas une
# rubrique (un nom de logiciel en gras dans les ressources) n'y entre pas
RUBRIQUES = [("objectif", "objectif"), ("compétence", "compétence"), ("production attendue", "production"),
             ("ce que tu produis", "ce que tu produis"), ("ressources", "ressource"), ("durée", "durée"), ("socle", "socle")]
OUVRE = '<details class="fiche-activite">'
# une incrustation d'atelier (entre ses marqueurs) se replie à l'identique de ce qu'écrit son générateur
# (ateliers-representations/_generation/moteur.py, exercice(…, fiche_repliee=True)) : « La fiche de l'exercice »
INCRUSTATION = re.compile(r"<!-- ateliers-representations:debut.*?<!-- ateliers-representations:fin", re.S)


def resume(bloc, quoi="l'activité"):
    vues = set()
    for b in re.findall(r"<b>(.*?)</b>", bloc, re.S):
        mot = re.sub(r"<[^>]+>|&nbsp;|[:\s]+$", " ", b).strip().lower()
        mot = re.sub(r"^[^a-zàâçéèêëîïôûùüÿœ]+", "", mot)
        for nom, debut in RUBRIQUES:
            if mot.startswith(debut):
                vues.add(nom)
                break
    return "🗂 La fiche de %s : %s" % (quoi, ", ".join(nom for nom, _ in RUBRIQUES if nom in vues))


def div_equilibre(t, i):
    """la fin du <div …> ouvert en i (balises div équilibrées)"""
    n = 0
    for m in re.finditer(r"<(/?)div\b[^>]*>", t[i:]):
        n += -1 if m.group(1) else 1
        if n == 0:
            return i + m.end()
    raise ValueError("div non fermé à %d" % i)


def fiches(t):
    """(début, fin) de chaque fiche d'activité pas encore repliée"""
    out = []
    for m in re.finditer(r'<div class="meta-grid"[^>]*>|<div class="meta"[^>]*>\s*<b>\s*(?:🎯\s*)?Objectif|<p><b>Objectifs?(?:&nbsp;|\s)*:</b>', t):
        i = m.start()
        avant = t[max(0, i - 200):i]
        if re.search(r'<details class="fiche-activite"><summary>[^<]*</summary>\s*$', avant):
            continue
        if m.group(0).startswith("<p>"):
            j = t.index("</p>", i) + len("</p>")
        else:
            j = div_equilibre(t, i)
        out.append((i, j))
    return out


def replier(t):
    morceaux, k, n = [], 0, 0
    zones = [(m.start(), m.end()) for m in INCRUSTATION.finditer(t)]
    for i, j in fiches(t):
        bloc = t[i:j]
        quoi = "l'exercice" if any(a < i < b for a, b in zones) else "l'activité"
        morceaux += [t[k:i], OUVRE, "<summary>%s</summary>" % resume(bloc, quoi), bloc, "</details>"]
        k = j; n += 1
    morceaux.append(t[k:])
    t = "".join(morceaux)
    return styler(t) if n or 'class="fiche-activite"' in t else t, n


def styler(t):
    if CSS_MARQUE in t:
        return t
    i = t.find("</style>")
    return t if i < 0 else t[:i] + CSS + t[i:]


def pages(args):
    if args:
        return [pathlib.Path(a) for a in args]
    return sorted(p for p in RACINE.glob("theme-*/**/sequence*.html") if "node_modules" not in p.parts)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ecrire, etat = "--ecrire" in sys.argv, "--etat" in sys.argv
    total = touchees = 0
    for p in pages(args):
        t = p.read_text(encoding="utf-8")
        nouveau, n = replier(t)
        if not n:
            continue
        total += n; touchees += 1
        if not etat:
            print("· %s : %d fiche(s)" % (p.relative_to(RACINE) if p.is_absolute() else p, n))
        if ecrire:
            p.write_text(nouveau, encoding="utf-8")
    verbe = "repliée(s)" if ecrire else "à replier"
    print("%d fiche(s) d'activité %s dans %d page(s)" % (total, verbe, touchees))


if __name__ == "__main__":
    main()
