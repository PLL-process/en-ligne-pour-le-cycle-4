#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""poser.py — la lisibilité à l'écran : texte aligné au début au téléphone, légendes à 13 px, barre du haut opaque,
focus jamais caché sous une barre (26-28/11/2026). Mode d'emploi et mesures : README.md, à côté.

Né de l'audit `docs/audits/AUDIT_SKILLS_DESIGN_2026-11-26.md` (constats « texte centré sur 3 lignes et plus » et
« légende sous 12 px »), sur carte blanche de Pascal. Source unique : ce fichier. Le bloc est posé avant `</head>`,
entre deux marqueurs, comme le mode mission (`_outils/mode_mission/poser.py`). Tout est sous `@media screen` :
l'impression ne change pas (n°316, fiche papier).

  · une page qui porte `class="saved-note"` ou `class="problematique"` : sous 700 px, ces textes s'alignent au début ;
  · le chapeau d'une page (QCM, lexique, atelier) : centré s'il tient sur une ligne, aligné à gauche s'il est long ;
  · une page à barre du haut collée ou en mode mission : une marge de défilement, pour que le champ atteint au
    clavier (Tab) ou le lien vers une ancre ne finisse pas caché sous la barre ou sous le pied « Suivant » ;
  · une page dont la barre du haut (`#navharm`) est translucide sans flou : même couleur, opaque — plus de texte lu
    à travers (une barre floutée, verre dépoli voulu, n'est pas touchée) ;
  · une synthèse élève dont une règle écrit une légende (`figcaption`) sous 13 px : la même règle est reposée avec
    un plancher, `max(13px, taille d'origine)` — jamais plus petit qu'avant, et rien si la page est déjà lisible.

    python3 _outils/lisibilite_ecran/poser.py <page.html> […]         # poser ou mettre à jour
    python3 _outils/lisibilite_ecran/poser.py --site                   # toutes les pages vivantes concernées
    python3 _outils/lisibilite_ecran/poser.py --verifier --site        # ne rien écrire : le bloc est-il là et à jour ?

Code de sortie (n°299) : 0 fait ou à jour · 1 des pages ne sont pas à jour (--verifier) · 2 aucune page lue.
"""
import re, sys
from pathlib import Path

VERSION = "7"
DEBUT = "<!-- lisibilite-ecran v%s : début — engendré par _outils/lisibilite_ecran/ (poser.py). Ne pas le modifier dans la page. -->" % VERSION
FIN = "<!-- lisibilite-ecran : fin -->"
# !important : sur 27 pages, la note de sauvegarde est centrée par un style écrit dans la balise.
TEXTE = "@media screen and (max-width:700px){.saved-note{text-align:start!important}.problematique{text-align:start}}"
# Chapeau d'une page (QCM, lexique, atelier) : court, il reste centré ; long (3 lignes et plus au téléphone), il prend
# toute la largeur et s'aligne à gauche. `width:fit-content` + marges automatiques : le bloc n'est large que de son
# texte quand le texte tient sur une ligne. Pas sur un chapeau en `nowrap` (une page) : il déborderait.
CHAPEAU = "{text-align:start;width:fit-content;max-width:100%;margin-inline:auto}"
CHAPEAUX = ((r'class="subtitle"', r"\.subtitle\{[^}]*nowrap", ".subtitle"),
            (r'class="sub ms-entete"', None, "p.sub.ms-entete"),
            (r'<p class="mission"', None, "p.mission"))
# La barre du haut était opaque à 93 % : le texte qui défile dessous se lisait à travers (vu en mode mission, à
# l'ouverture, sur le bouton « Mode essentiel »). Même couleur, opaque. `nav#navharm` et non `#navharm` : sur dix
# séquences, la règle de la barre est écrite dans le corps de la page, après ce bloc — à poids égal, elle gagnait.
BARRE = "@media screen{nav#navharm{background:rgb(%s)}}"
# Le clavier : en passant de champ en champ (Tab), le navigateur amène l'élément sous les yeux, mais sans savoir que
# la barre du haut (collée) et le pied du mode mission (fixe, ~73 px) le recouvrent. Mesuré le 27/11/2026 en vue élève :
# le focus finissait caché sur 137 pages (753 arrêts). Une marge de défilement suffit ; elle sert aussi aux liens
# vers une ancre (« relis la partie 5 »), qui ne tombent plus sous la barre. Une page qui règle déjà sa marge garde la
# sienne.
FOCUS_HAUT = "html{scroll-padding-top:64px}"
FOCUS_BAS = "html:has(body.ms){scroll-padding-bottom:104px}"
PLANCHER = 13  # px : en dessous, une légende ne se lit plus à l'écran (audit du 26/11/2026)


def hors_impression(css):
    """Le CSS d'une page sans ses blocs @media print (accolades comptées), commentaires retirés."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    out, i = [], 0
    for m in re.finditer(r"@media[^{]*\bprint\b[^{]*\{", css):
        if m.start() < i:
            continue
        out.append(css[i:m.start()])
        prof, j = 1, m.end()
        while j < len(css) and prof:
            prof += {"{": 1, "}": -1}.get(css[j], 0)
            j += 1
        i = j
    out.append(css[i:])
    return "".join(out)


def legendes(html):
    """Une règle par sélecteur de légende que la page écrit trop petit : même sélecteur, posé après, avec un plancher.
    `max(13px, taille d'origine)` : la légende ne rapetisse jamais, et une page déjà lisible ne reçoit rien."""
    css = hors_impression("\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, flags=re.DOTALL)))
    vus, regles = set(), []
    for m in re.finditer(r"([^{}@;]+)\{([^{}]*)\}", css):
        taille = re.search(r"(?:^|;)\s*font-size\s*:\s*([\d.]+)(em|rem|px)\s*(?:;|$)", m.group(2))
        if not taille:
            continue
        v, u = float(taille.group(1)), taille.group(2)
        if not ((u in ("em", "rem") and v < 0.86) or (u == "px" and v < PLANCHER)):
            continue
        for sel in (s.strip() for s in m.group(1).split(",")):
            if re.search(r"\bfigcaption(\s+\w+)?$", sel) and sel not in vus:
                vus.add(sel); regles.append("%s{font-size:max(%dpx,%s%s)}" % (sel, PLANCHER, taille.group(1), u))
    return "@media screen{%s}" % "".join(regles) if regles else ""
BLOC = re.compile(r"\n?<!-- lisibilite-ecran v\d+ : début.*?<!-- lisibilite-ecran : fin -->\n?", re.DOTALL)
BLOC_SEUL = re.compile(r"<!-- lisibilite-ecran v\d+ : début.*?<!-- lisibilite-ecran : fin -->", re.DOTALL)
RACINE = Path(__file__).resolve().parents[2]


def barre_sans_flou(html):
    """La couleur (« r,v,b ») de la barre du haut si elle est translucide SANS flou, sinon rien. Avec
    `backdrop-filter`, le texte de dessous est flouté : c'est un verre dépoli voulu, on n'y touche pas. Sans flou,
    il se lit à travers la barre : c'est le défaut."""
    for m in re.finditer(r"#navharm\{([^}]*)\}", hors_impression(html)):
        fond = re.search(r"background:rgba\((\d+,\d+,\d+),\.9\d\)", m.group(1))
        if fond:
            return "" if "backdrop-filter" in m.group(1) else fond.group(1)
    return ""


def regles(chemin, html):
    r = []
    if re.search(r'class="[^"]*\b(saved-note|problematique)\b', html):
        r.append(TEXTE)
    chapeaux = [sel for marque, exclu, sel in CHAPEAUX if marque in html and not (exclu and re.search(exclu, html))]
    if chapeaux:
        r.append("@media screen and (max-width:700px){%s%s}" % (",".join(chapeaux), CHAPEAU))
    fond = barre_sans_flou(html)
    if fond:
        r.append(BARRE % fond)
    if "scroll-padding" not in hors_impression(html).replace(DEBUT, ""):
        marges = (FOCUS_HAUT if 'id="navharm"' in html else "") + (FOCUS_BAS if "<!-- mode-mission v" in html else "")
        if marges:
            r.append("@media screen{%s}" % marges)
    if chemin.name.startswith("synthese_eleve") and "<figcaption" in html:
        leg = legendes(html)
        if leg:
            r.append(leg)
    return r


def attendu(chemin, html):
    r = regles(chemin, html)
    return "%s\n<style>%s</style>\n%s" % (DEBUT, "".join(r), FIN) if r else ""


def pages_du_site():
    return sorted(f for f in RACINE.rglob("*.html")
                  if not any(p.startswith(("_archive", ".git", "node_modules", "_outils", "docs")) for p in f.relative_to(RACINE).parts))


def poser_page(html, chemin):
    """La page avec son bloc à jour (ou sans bloc, si elle n'a rien à recevoir). Fonction pure : c'est elle qu'un
    générateur appelle sur la page qu'il vient d'écrire (règle d'or n°283 : sans cela, régénérer effacerait le bloc).
    Un bloc déjà là est remplacé SUR PLACE : un autre bloc posé après lui (fiche papier, mode mission) ne le déplace
    pas, et la page reste identique d'une passe à l'autre. Lève ValueError si la page a deux blocs, ou ni </head> ni
    <body> où poser le premier."""
    trouves = list(BLOC_SEUL.finditer(html))
    if len(trouves) > 1:
        raise ValueError("%d blocs lisibilite-ecran dans la page" % len(trouves))
    nu = BLOC.sub("\n", html) if trouves else html
    bloc = attendu(Path(chemin), nu)
    if trouves:
        m = trouves[0]
        if not bloc:                                  # plus rien à recevoir : la page rend son bloc
            return nu
        return html[:m.start()] + bloc + html[m.end():]
    if not bloc:
        return html
    # Quatre pages engendrées n'écrivent pas </head> (HTML5 le permet) : le bloc se pose alors juste avant <body>.
    # Le bloc commence toujours sur sa ligne (une page écrit `</style></head>` d'un trait).
    if "</head>" in html:
        return re.sub(r"\s*</head>", lambda m: "\n" + bloc + "\n</head>", html, count=1)
    if re.search(r"<body\b", html):
        return re.sub(r"\s*(<body\b)", lambda m: "\n" + bloc + "\n" + m.group(1), html, count=1)
    raise ValueError("ni </head> ni <body> : aucune place où poser le bloc")


def principal():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verifier = "--verifier" in sys.argv
    pages = pages_du_site() if "--site" in sys.argv else [Path(a) for a in args]
    if not pages:
        print("PANNE — aucune page (code 2)"); return 2
    poses, a_jour, sans, retard = 0, 0, 0, []
    for f in pages:
        html = f.read_text(encoding="utf-8")
        try:
            neuf = poser_page(html, f)
        except ValueError as e:
            retard.append("%s (%s)" % (f, e)); continue
        if neuf == html:
            if BLOC_SEUL.search(html):
                a_jour += 1
            else:
                sans += 1
        elif verifier:
            retard.append(str(f))
        else:
            f.write_text(neuf, encoding="utf-8"); poses += 1
    print("%d page(s) lues · %d posée(s) · %d à jour · %d sans objet" % (len(pages), poses, a_jour, sans)
          + ("" if not retard else " · ✘ %d pas à jour : %s" % (len(retard), ", ".join(Path(x.split(" (")[0]).name for x in retard[:5]))))
    return 1 if retard else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(principal())
