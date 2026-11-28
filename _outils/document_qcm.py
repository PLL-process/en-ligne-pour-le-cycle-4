# -*- coding: utf-8 -*-
"""document_qcm.py — les documents à lire d'un QCM, dessinés pour le téléphone (règle d'or n°345, 21/11/2026).

LE CONSTAT
----------
Le 21/11/2026, la lecture question par question des QCM du thème 1 trouve des questions qui demandent un chiffre de la
séquence sans le montrer (« Avec les quatre exigences du centre, combien de solutions passent ? »), et neuf QCM de
séquence sous les six questions sur document. Les planches existantes sont dessinées pour l'ordinateur : 900 unités de
large, du texte de 12 px — au téléphone (390 px), il s'affiche à 5 px et ne se lit qu'à la loupe. Le cahier des charges
« ultra premium » du 12/11/2026 le dit : « aucun texte sous 14 px à la taille réellement affichée », « pas de planche
entière miniaturisée ».

CE QUE FAIT L'OUTIL
-------------------
Il lit `documents_qcm_<lot>.json`, à la racine d'un lot, et écrit dans `Images/` un SVG par document : 350 unités de
large, texte de 15 px et plus (13 à 14 px sur un téléphone de 390 px), fond et couleurs de la charte, `role="img"`, `<title>` et
`<desc>`, des cadres à 16 unités l'un de l'autre (le repère « serré » de `controle_schemas.mjs`, n°315). La coupe des
lignes suit la typographie : un « ? » ou un « : » ne passe jamais seul à la ligne, un nombre ne quitte pas ce qu'il
compte (« 8 abandons »), et les lignes d'un titre s'équilibrent (aucun mot seul sur la dernière). Quatre blocs :
  {"fiches": [{"titre": "…", "accent": true, "lignes": ["…"], "paires": [["Charge", "120 kg"], …]}]}
        des cartes empilées ; `paires` se range sur deux colonnes ; `accent` encadre en orange (ce qui est exigé) ;
  {"barres": [["étiquette", valeur, "valeur écrite"], …], "max": 100}
        des barres horizontales, l'étiquette au-dessus de sa barre, la valeur écrite au bout ;
  {"tableau": {"colonnes": ["", "…"], "lignes": [["…", "…"]], "largeurs": [150, 86, 86]}}
        un tableau d'au plus quatre colonnes ;
  {"intertitre": "…"}
        une ligne de titre entre deux blocs.
Chaque document porte `titre`, `sous_titre` (facultatif), `desc` (ce qu'il montre, pour qui ne le voit pas) et `note`
(facultatif : les unités en toutes lettres, n°312).
`"qcm": ["qcm_….html"]` nomme les pages qui affichent ces documents : l'outil y pose, une fois, le style qui les garde
à 400 px de large sur un grand écran (un document étroit étiré à 760 px ferait défiler la question hors de l'écran).

Rejouable : les SVG sont réécrits à l'identique ; le style n'est posé qu'une fois.

Usage : python3 _outils/document_qcm.py <lot>/documents_qcm_<lot>.json [--verifier]
  --verifier  n'écrit rien : dit si les SVG et le style sont ceux des données (0 / 1).
Sortie : 0 fait (ou à jour) · 1 écart avec --verifier · 2 données illisibles ou incomplètes.
"""
from __future__ import annotations

import json
import os
import re
import sys
from xml.sax.saxutils import escape

L = 350          # largeur du document, en unités (le téléphone l'affiche sur 312 px environ : 16 unités ≈ 14 px)
M = 14           # marge
ENTRE = 16       # entre deux cadres : 16 unités, le repère « serré » de controle_schemas.mjs (n°315)
POLICE = "Segoe UI, system-ui, sans-serif"
FOND, CARTE, BORD = "#0a1b3d", "#0d2347", "#274a8a"
TEXTE, DOUX, TITRE, ACCENT, BARRE = "#e4eaf5", "#9bbefc", "#61dafb", "#ffb454", "#61dafb"
STYLE_MARQUE = "/* documents-qcm : un document étroit ne s'étire pas (n°345) */"
STYLE = ("\n  " + STYLE_MARQUE + "\n  .q-figure img[src*=\"/doc_\"]{max-width:400px}\n")


def large(texte: str, taille: float, gras: bool = False) -> float:
    """Largeur approchée d'un texte, en unités (assez large pour ne jamais sous-estimer)."""
    etroits = sum(1 for c in texte if c in "il.,:;'’!| \u00a0")
    return (len(texte) - 0.5 * etroits) * taille * (0.60 if gras else 0.56)


def couper(texte: str, taille: float, place: float, gras: bool = False):
    """Coupe un texte en lignes qui tiennent dans `place`."""
    # un signe double (« ? », « ! », « : », « ; », « » », « % ») ne passe jamais seul à la ligne : il suit son mot ;
    # un nombre ne quitte pas ce qu'il compte (« 8 abandons », « 2 400 € »)
    mots = []
    for mot in texte.split(" "):
        if mots and (mot in ("?", "!", ":", ";", "»", "%") or mots[-1] == "«"
                     or re.fullmatch(r"[0-9][0-9,.]*", mots[-1].split("\u00a0")[-1])):
            mots[-1] += "\u00a0" + mot
        else:
            mots.append(mot)
    lignes, cours = [], ""
    for mot in mots:
        essai = (cours + " " + mot).strip(" ")   # une espace insécable en tête (l'indentation d'un programme) reste
        if cours and large(essai, taille, gras) > place:
            lignes.append(cours)
            cours = mot
        else:
            cours = essai
    if cours:
        lignes.append(cours)
    return lignes


def equilibrer(texte: str, taille: float, place: float, gras: bool = False):
    """Les lignes d'un titre à peu près égales : aucun mot seul sur la dernière ligne."""
    lignes = couper(texte, taille, place, gras)
    etroit = place
    while len(lignes) > 1 and etroit > place * 0.5:
        essai = couper(texte, taille, etroit - 4, gras)
        if len(essai) != len(lignes):
            break
        etroit, lignes = etroit - 4, essai
    return lignes


class Dessin:
    def __init__(self):
        self.y = M
        self.corps = []

    def texte(self, x, y, t, taille=15, couleur=TEXTE, gras=False, ancre="start"):
        self.corps.append('<text x="%.1f" y="%.1f" font-size="%s" fill="%s"%s%s>%s</text>' % (
            x, y, taille, couleur, ' font-weight="700"' if gras else "",
            ' text-anchor="%s"' % ancre if ancre != "start" else "", escape(t)))

    def paragraphe(self, t, taille=15, couleur=TEXTE, gras=False, x=M, place=L - 2 * M, interligne=1.35, egal=False):
        for ligne in (equilibrer if egal else couper)(t, taille, place, gras):
            self.y += taille * interligne
            self.texte(x, self.y - taille * 0.3, ligne, taille, couleur, gras)

    def rect(self, x, y, w, h, fond=CARTE, bord=BORD, epais=1.2, rx=12):
        self.corps.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
                          % (x, y, w, h, rx, fond, bord, epais))


def fiches(d: Dessin, cartes):
    for c in cartes:
        haut = d.y
        place = L - 2 * M - 24
        # mesurer d'abord, dessiner ensuite : la carte vient sous son texte
        lignes = []
        for l in c.get("lignes", []):
            lignes += couper(l, 15, place)
        paires = c.get("paires", [])
        rangs = (len(paires) + 1) // 2
        h = 14 + 22 + len(lignes) * 21 + rangs * 40 + 12
        accent = c.get("accent")
        d.rect(M, haut, L - 2 * M, h, bord=ACCENT if accent else BORD, epais=1.8 if accent else 1.2)
        y = haut + 14 + 16
        d.texte(M + 12, y, c["titre"], 16, ACCENT if accent else TITRE, True)
        y += 6
        for l in lignes:
            y += 21
            d.texte(M + 12, y, l, 15)
        col = (L - 2 * M - 24) / 2
        for i, (nom, valeur) in enumerate(paires):
            x = M + 12 + (i % 2) * col
            yy = y + 22 + (i // 2) * 40
            d.texte(x, yy, nom, 13.5, DOUX)
            d.texte(x, yy + 19, valeur, 16, TEXTE, True)
        d.y = haut + h + ENTRE


def barres(d: Dessin, lignes, maxi):
    place = L - 2 * M - 86
    for nom, valeur, ecrit in lignes:
        d.y += 20
        d.texte(M, d.y, nom, 15)
        d.y += 8
        w = max(3.0, place * float(valeur) / float(maxi))
        d.corps.append('<rect x="%d" y="%.1f" width="%.1f" height="16" rx="5" fill="%s"/>' % (M, d.y, w, BARRE))
        d.texte(M + w + 8, d.y + 13.5, ecrit, 15, TEXTE, True)
        d.y += 16 + 10


def tableau(d: Dessin, t):
    cols, lignes = t["colonnes"], t["lignes"]
    larg = t.get("largeurs") or [(L - 2 * M) / len(cols)] * len(cols)
    if abs(sum(larg) - (L - 2 * M)) > 0.5:
        raise ValueError("tableau : les largeurs font %s, attendu %s" % (sum(larg), L - 2 * M))
    hl = 34
    haut = d.y
    d.rect(M, haut, L - 2 * M, hl * (len(lignes) + 1), rx=10)
    x = M
    for i, c in enumerate(cols):
        d.texte(x + (10 if i == 0 else larg[i] / 2), haut + 22, c, 13.5, TITRE, True, "start" if i == 0 else "middle")
        x += larg[i]
    for r, ligne in enumerate(lignes, 1):
        y = haut + r * hl
        d.corps.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>' % (M, y, L - M, y, BORD))
        x = M
        for i, cel in enumerate(ligne):
            d.texte(x + (10 if i == 0 else larg[i] / 2), y + 22, cel, 15, TEXTE, i == 0, "start" if i == 0 else "middle")
            x += larg[i]
    d.y = haut + hl * (len(lignes) + 1) + ENTRE


def dessiner(doc: dict, ident: str) -> str:
    d = Dessin()
    d.paragraphe(doc["titre"], 17, TEXTE, True, egal=True)
    if doc.get("sous_titre"):
        d.y += 2
        d.paragraphe(doc["sous_titre"], 13.5, DOUX, egal=True)
    d.y += 12
    for bloc in doc["blocs"]:
        if "fiches" in bloc:
            fiches(d, bloc["fiches"])
        elif "barres" in bloc:
            barres(d, bloc["barres"], bloc["max"])
        elif "tableau" in bloc:
            tableau(d, bloc["tableau"])
        elif "intertitre" in bloc:
            d.y += 10
            d.paragraphe(bloc["intertitre"], 15.5, TITRE, True)
            d.y += 2
        else:
            raise ValueError("bloc inconnu : %s" % list(bloc))
    if doc.get("note"):
        d.paragraphe(doc["note"], 13.5, DOUX)
        d.y += 6
    h = d.y + M - 4
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %.0f" width="%d" height="%.0f" role="img" '
            'aria-labelledby="t_%s d_%s" font-family="%s">\n<title id="t_%s">%s</title>\n<desc id="d_%s">%s</desc>\n'
            '<rect width="%d" height="%.0f" rx="14" fill="%s"/>\n%s\n</svg>\n'
            % (L, h, L, h, ident, ident, POLICE, ident, escape(doc["titre"]), ident, escape(doc["desc"]), L, h, FOND,
               "\n".join(d.corps)))


def main(argv) -> int:
    verifier = "--verifier" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    if len(chemins) != 1:
        print(__doc__.split("Usage :")[1].strip())
        return 2
    try:
        donnees = json.load(open(chemins[0], encoding="utf-8"))
        lot = os.path.dirname(os.path.abspath(chemins[0]))
        sorties = {}
        for nom, doc in donnees["documents"].items():
            if not nom.startswith("doc_"):
                raise ValueError("« %s » : le nom d'un document commence par doc_ (le style s'y accroche)" % nom)
            for cle in ("titre", "desc", "blocs"):
                if not doc.get(cle):
                    raise ValueError("« %s » : « %s » manque" % (nom, cle))
            sorties[os.path.join(lot, "Images", nom + ".svg")] = dessiner(doc, nom.replace("doc_", "")[:24])
    except (OSError, ValueError, KeyError) as e:
        print("✘ données illisibles ou incomplètes : %s" % e)
        return 2
    ecarts = 0
    for chemin, svg in sorties.items():
        ancien = open(chemin, encoding="utf-8").read() if os.path.exists(chemin) else None
        if ancien != svg:
            ecarts += 1
            if not verifier:
                with open(chemin, "w", encoding="utf-8") as f:
                    f.write(svg)
    for q in donnees.get("qcm", []):
        p = os.path.join(lot, q)
        s = open(p, encoding="utf-8").read()
        pose = re.search(r"\n  " + re.escape(STYLE_MARQUE) + r"\n[^\n]*\n", s)
        if not pose or pose.group(0) != STYLE:
            ecarts += 1
            if not verifier:
                if pose:        # un style plus ancien est remplacé, jamais doublé
                    s = s[:pose.start()] + STYLE + s[pose.end():]
                else:
                    i = s.index("</style>")
                    s = s[:i].rstrip("\n") + STYLE + s[i:]
                with open(p, "w", encoding="utf-8") as f:
                    f.write(s)
    if verifier:
        print("%d document(s) lus · %d écart(s) avec les données" % (len(sorties), ecarts))
        return 1 if ecarts else 0
    print("%d document(s) écrits dans Images/ · %d changement(s) · %d page(s) de QCM au style posé"
          % (len(sorties), ecarts, len(donnees.get("qcm", []))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
