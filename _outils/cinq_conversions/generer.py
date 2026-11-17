#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les cinq conversions d'énergie du programme 2024 : le même dessin, à chaque étage du cycle 4.

Le programme (SFC 11, connaissance reprise en CCRI 14) demande « les conversions d'énergie des constituants suivants :
moteur électrique, lampe, radiateur, génératrice, vérin ». La progression validée le 17/11/2026
(`docs/specifications/progression-cinq-conversions-cycle4.md`) veut que l'élève retrouve la même image d'une année
sur l'autre. Ce générateur dessine cette image une seule fois et la pose, à l'identique, dans chaque lot qui s'en sert.

Deux dessins :
  · `cinq_constituants_muet.svg` — les cinq constituants et leurs flèches, l'énergie qui entre et celle qui sort en
    « ? » : c'est le schéma de la QUESTION, muet sur ce qu'elle fait trouver (règle d'or n°331) ;
  · `cinq_conversions.svg` — le même, complet, avec la perte de chaleur : c'est le schéma de la CORRECTION et de la
    synthèse (règle d'or n°336).

Usage :
    python3 _outils/cinq_conversions/generer.py <dossier Images>…            écrit les deux dessins dans chaque dossier
    python3 _outils/cinq_conversions/generer.py --verifier <dossier Images>…  vérifie qu'ils sont à jour (sortie 1 sinon)

Les mots suivent la règle des chaînes d'énergie (skill `chaine-energie-fonctionnelle`, 16-17/11/2026) : moteur →
cinétique ; génératrice : mécanique → électrique ; vérin → mécanique (fiche SFC1b de l'académie de Bordeaux).
"""
import os
import sys

FOND = "#050f24"
CADRE_FOND = "#0d1c3a"
CADRE_TRAIT = "#81aaff"
ENERGIE = "#ffb15c"
ETIQUETTE = "#ffd2a0"
TEXTE = "#e4eaf5"
DISCRET = "#9aa5b8"
GRIS_CLAIR = "#c9d6f2"
JAUNE = "#ffd66b"
CHAUD = "#ff8a7a"

# constituant : (nom sur une ou deux lignes, entrée, sortie, ligne sous la sortie)
CONSTITUANTS = [
    ("moteur", ["Moteur", "électrique"], ["électrique"], ["cinétique"], "+ chaleur perdue"),
    ("lampe", ["Lampe"], ["électrique"], ["lumineuse"], "+ chaleur perdue"),
    ("radiateur", ["Radiateur"], ["électrique"], ["thermique"], "(c'est son but)"),
    ("generatrice", ["Génératrice"], ["mécanique"], ["électrique"], "+ chaleur perdue"),
    ("verin", ["Vérin"], ["pneumatique", "ou hydraulique"], ["mécanique"], "+ chaleur perdue"),
]

LARGEUR, HAUTEUR = 920, 352
# cinq colonnes, à lire de haut en bas : ce qui entre, le constituant, ce qui sort (une bande large et basse : le
# schéma reste lisible épinglé au-dessus des questions, qui lui laissent 30 % de la hauteur de l'écran)
COL0, COL_PAS = 92, 184
BOITE_L, BOITE_H, BOITE_Y = 164, 104, 136
FLECHE1, FLECHE2 = (86, 128), (248, 290)


def icone(cle, cy):
    """Le petit dessin du constituant, à gauche dans son cadre (aucun texte : ce n'est pas un cadre)."""
    if cle == "moteur":
        return (f'<rect x="248" y="{cy - 14}" width="34" height="28" rx="5" fill="{DISCRET}"/>'
                f'<rect x="282" y="{cy - 9}" width="6" height="18" rx="2" fill="{GRIS_CLAIR}"/>'
                f'<line x1="288" y1="{cy}" x2="300" y2="{cy}" stroke="{TEXTE}" stroke-width="3" stroke-linecap="round"/>'
                f'<line x1="256" y1="{cy - 8}" x2="256" y2="{cy + 8}" stroke="{CADRE_FOND}" stroke-width="2"/>'
                f'<line x1="264" y1="{cy - 8}" x2="264" y2="{cy + 8}" stroke="{CADRE_FOND}" stroke-width="2"/>'
                f'<line x1="272" y1="{cy - 8}" x2="272" y2="{cy + 8}" stroke="{CADRE_FOND}" stroke-width="2"/>')
    if cle == "lampe":
        return (f'<circle cx="274" cy="{cy - 5}" r="13" fill="{JAUNE}"/>'
                f'<rect x="267" y="{cy + 8}" width="14" height="10" rx="2" fill="{DISCRET}"/>'
                f'<line x1="274" y1="{cy - 24}" x2="274" y2="{cy - 29}" stroke="{JAUNE}" stroke-width="2.5" stroke-linecap="round"/>'
                f'<line x1="256" y1="{cy - 17}" x2="252" y2="{cy - 21}" stroke="{JAUNE}" stroke-width="2.5" stroke-linecap="round"/>'
                f'<line x1="292" y1="{cy - 17}" x2="296" y2="{cy - 21}" stroke="{JAUNE}" stroke-width="2.5" stroke-linecap="round"/>')
    if cle == "radiateur":
        ailettes = "".join(f'<rect x="{250 + i * 12}" y="{cy - 17}" width="8" height="32" rx="3" fill="{CHAUD}"/>'
                           for i in range(4))
        return ailettes + (f'<line x1="250" y1="{cy - 11}" x2="294" y2="{cy - 11}" stroke="{CHAUD}" stroke-width="3"/>'
                           f'<line x1="250" y1="{cy + 9}" x2="294" y2="{cy + 9}" stroke="{CHAUD}" stroke-width="3"/>')
    if cle == "generatrice":
        return (f'<circle cx="266" cy="{cy}" r="15" fill="{DISCRET}"/>'
                f'<circle cx="266" cy="{cy}" r="5" fill="{CADRE_FOND}"/>'
                f'<line x1="281" y1="{cy}" x2="288" y2="{cy}" stroke="{TEXTE}" stroke-width="3"/>'
                f'<circle cx="294" cy="{cy}" r="8" fill="none" stroke="{TEXTE}" stroke-width="2.5"/>'
                f'<line x1="294" y1="{cy - 8}" x2="294" y2="{cy + 8}" stroke="{TEXTE}" stroke-width="1.5"/>'
                f'<line x1="286" y1="{cy}" x2="302" y2="{cy}" stroke="{TEXTE}" stroke-width="1.5"/>')
    if cle == "verin":
        return (f'<rect x="246" y="{cy - 9}" width="36" height="18" rx="3" fill="{DISCRET}"/>'
                f'<rect x="276" y="{cy - 7}" width="4" height="14" fill="{GRIS_CLAIR}"/>'
                f'<line x1="282" y1="{cy}" x2="298" y2="{cy}" stroke="{TEXTE}" stroke-width="4" stroke-linecap="round"/>'
                f'<circle cx="300" cy="{cy}" r="3.5" fill="{TEXTE}"/>')
    raise ValueError(cle)


def lignes(x, y, mots, ancre, taille, couleur, gras=True):
    """Un texte d'une ou deux lignes, centré verticalement sur y."""
    poids = ' font-weight="700"' if gras else ""
    if len(mots) == 1:
        return f'<text x="{x}" y="{y + 6}" text-anchor="{ancre}" font-size="{taille}" fill="{couleur}"{poids}>{mots[0]}</text>'
    return (f'<text x="{x}" y="{y - 4}" text-anchor="{ancre}" font-size="{taille - 2}" fill="{couleur}"{poids}>{mots[0]}</text>'
            f'<text x="{x}" y="{y + 15}" text-anchor="{ancre}" font-size="{taille - 2}" fill="{couleur}"{poids}>{mots[1]}</text>')


def dessin(complet):
    if complet:
        titre = "Les cinq conversions d'énergie à connaître"
        desc = ("Cinq colonnes, une par constituant, à lire de haut en bas : l'énergie qui entre, le constituant, "
                "l'énergie qui sort. Moteur électrique : électrique, puis cinétique, et un peu de chaleur perdue. "
                "Lampe : électrique, puis lumineuse, et un peu de chaleur perdue. Radiateur : électrique, puis "
                "thermique ; la chaleur est son but. Génératrice : mécanique, puis électrique, et un peu de chaleur "
                "perdue. Vérin : pneumatique ou hydraulique, puis mécanique, et un peu de chaleur perdue.")
    else:
        titre = "Les cinq constituants : quelle énergie entre, quelle énergie sort ?"
        desc = ("Cinq colonnes, une par constituant, à lire de haut en bas : un point d'interrogation pour l'énergie "
                "qui entre, une flèche, le constituant, une flèche, un point d'interrogation pour l'énergie qui sort. "
                "Les constituants : moteur électrique, lampe, radiateur, génératrice, vérin.")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LARGEUR} {HAUTEUR}" '
         f'font-family="system-ui, \'Segoe UI\', Arial, sans-serif" role="img" aria-labelledby="t d">',
         f'<title id="t">{titre}</title>',
         f'<desc id="d">{desc}</desc>',
         f'<rect width="{LARGEUR}" height="{HAUTEUR}" fill="{FOND}"/>',
         '<defs><marker id="fe" markerWidth="12" markerHeight="12" refX="9" refY="5" orient="auto" '
         'markerUnits="userSpaceOnUse" viewBox="0 0 10 10">'
         f'<path d="M0,0 L10,5 L0,10 z" fill="{ENERGIE}"/></marker></defs>',
         f'<text x="{LARGEUR // 2}" y="26" text-anchor="middle" font-size="15" fill="{DISCRET}">'
         "Lis chaque colonne de haut en bas : ce qui entre, le constituant, ce qui sort.</text>"]
    for i, (cle, nom, entree, sortie, note) in enumerate(CONSTITUANTS):
        cx = COL0 + i * COL_PAS
        o.append(f'<!-- {cle} -->')
        if complet:
            o.append(lignes(cx, 64, entree, "middle", 17, ETIQUETTE))
        else:
            o.append(f'<text x="{cx}" y="72" text-anchor="middle" font-size="24" fill="{DISCRET}" font-weight="700">?</text>')
        o.append(f'<line x1="{cx}" y1="{FLECHE1[0]}" x2="{cx}" y2="{FLECHE1[1]}" stroke="{ENERGIE}" stroke-width="4" marker-end="url(#fe)"/>')
        o.append(f'<rect x="{cx - BOITE_L // 2}" y="{BOITE_Y}" width="{BOITE_L}" height="{BOITE_H}" rx="12" '
                 f'fill="{CADRE_FOND}" stroke="{CADRE_TRAIT}" stroke-width="3"/>')
        o.append(f'<g transform="translate({cx - 274},{BOITE_Y + 36 - 100})">{icone(cle, 100)}</g>')
        o.append(lignes(cx, BOITE_Y + 76, nom, "middle", 17, TEXTE))
        o.append(f'<line x1="{cx}" y1="{FLECHE2[0]}" x2="{cx}" y2="{FLECHE2[1]}" stroke="{ENERGIE}" stroke-width="4" marker-end="url(#fe)"/>')
        if complet:
            o.append(lignes(cx, 310, sortie, "middle", 17, ETIQUETTE))
            o.append(f'<text x="{cx}" y="338" text-anchor="middle" font-size="13" fill="{DISCRET}">{note}</text>')
        else:
            o.append(f'<text x="{cx}" y="322" text-anchor="middle" font-size="24" fill="{DISCRET}" font-weight="700">?</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


FICHIERS = {"cinq_constituants_muet.svg": False, "cinq_conversions.svg": True}


def main(args):
    verifier = "--verifier" in args
    dossiers = [a for a in args if not a.startswith("--")]
    if not dossiers:
        print(__doc__)
        return 2
    ecarts = 0
    for d in dossiers:
        if not os.path.isdir(d):
            print(f"✘ {d} : pas un dossier")
            return 2
        for nom, complet in FICHIERS.items():
            chemin = os.path.join(d, nom)
            attendu = dessin(complet)
            actuel = open(chemin, encoding="utf-8").read() if os.path.exists(chemin) else None
            if verifier:
                if actuel != attendu:
                    ecarts += 1
                    print(f"✘ {chemin} : {'absent' if actuel is None else 'pas à jour'}")
            elif actuel != attendu:
                open(chemin, "w", encoding="utf-8").write(attendu)
                print(f"✎ {chemin}")
    if verifier:
        n = len(dossiers) * len(FICHIERS)
        print(f"{'✅' if not ecarts else '✘'} {n - ecarts} / {n} dessins à jour dans {len(dossiers)} dossier(s)")
        return 1 if ecarts else 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
