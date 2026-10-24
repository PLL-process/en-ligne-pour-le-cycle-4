# -*- coding: utf-8 -*-
"""generer_bibliotheque_chaines.py — la bibliothèque de formes draw.io des chaînes, écrite par un script.

LE CONSTAT
----------
Le 24/10/2026, la bibliothèque `PLL-chaines.xml` de Pascal et celle que télécharge l'élève du Book Train
(`bibliotheque_chaines_book-train.xml`, du 02/08/2026) dataient d'avant la règle d'or n°310 (21/10/2026) :
pas de bloc STOCKER, pas de fonction absente en pointillés grisés (n°131), une flèche d'ordre rouge qui ne
disait pas où elle arrivait, des composants dans des boîtes comme des fonctions, et des énergies sans forme.
Deux défauts techniques en plus, mesurés dans Chromium (la lecture de draw.io) :
  · `html=1` partout : à l'export SVG, draw.io écrit les textes en foreignObject, que le dépôt refuse
    (textes natifs, skill du dépôt `chaine-energie-fonctionnelle`) ;
  · des sauts de ligne bruts dans les attributs XML : la lecture XML les change en espaces
    (« Carte programmable » sur une ligne). Ils s'écrivent `&#10;`.

CE QUE FAIT CE SCRIPT
---------------------
Il écrit 34 formes conformes aux n°310, n°131 et n°6 : les sept fonctions et STOCKER, chacune avec sa
ligne de composant dessous ; deux fonctions absentes ; les flèches d'information, de compte rendu, d'ordre
(qui descend vers DISTRIBUER) et d'énergie, chacune avec sa forme ; l'action finale, le titre et le pied
qui disent la convention. `html=0` partout, `&#10;` pour les sauts de ligne, pointillés en
`dashPattern=8 6;fixDash=1` (sans fixDash, draw.io multiplie le motif par l'épaisseur du trait), couleurs
de `regenerer_chaines_energie.py` dans leur version impression (fond blanc).

Il écrit la bibliothèque à sa place dans le Book Train, remplace la copie incorporée dans la page
(`var FICHIERS`, téléchargement hors ligne), puis RELIT le fichier écrit comme draw.io le lit et le
vérifie. `regenerer_chaines_energie.py` ne touche pas cette entrée de `FICHIERS` : les deux scripts
peuvent tourner dans n'importe quel ordre.

NON VÉRIFIÉ ICI : le rendu dans draw.io lui-même (essayé par Pascal dans draw.io pour Windows le
24/10/2026 : palette chargée, STOCKER et ses deux lignes affichés).

Usage :
    python3 _outils/generer_bibliotheque_chaines.py                  # écrit la bibliothèque et la page
    python3 _outils/generer_bibliotheque_chaines.py --sortie F.xml   # écrit seulement F.xml
    python3 _outils/generer_bibliotheque_chaines.py --verifier F.xml # vérifie une bibliothèque existante
Sortie : 0 conforme, 1 écart (nommé), 2 rien n'a pu être lu (règle d'or n°299).
"""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import panne

DEPOT = Path(__file__).resolve().parent.parent
LOT = DEPOT / ("theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/"
               "4e/4e_C4.1_book-train")
CIBLE = LOT / "fichiers_drawio/bibliotheque_chaines_book-train.xml"
PAGE = LOT / "sequence_4e_C4.1-C4.2-C4.4_book-train.html"
NOM_INCORPORE = "bibliotheque_chaines_book-train.xml"
TITRE = "Chaînes d’information et d’énergie"

# Palette « impression » du générateur du dépôt (CSS @media print de regenerer_chaines_energie.py)
CYAN, YELLOW, VIOLET, GREEN, ORANGE, BLUE = '#006a86', '#805600', '#7836ad', '#126c2a', '#925000', '#244e9a'
TEXTE, GRIS, GRIS_TEXTE = '#172a49', '#9e9e9e', '#7a7a7a'
FONT = 'fontFamily=Arial;'

FONCTIONS = {  # fonction -> couleur (même attribution que le générateur)
    'ACQUÉRIR': CYAN, 'TRAITER': VIOLET, 'COMMUNIQUER': GREEN,
    'ALIMENTER': YELLOW, 'STOCKER': YELLOW, 'DISTRIBUER': CYAN, 'CONVERTIR': VIOLET, 'TRANSMETTRE': GREEN,
}
W_BLOC, H_BLOC = 210, 76
POINTILLES = '………………'


def bloc_style(c):
    return (f'rounded=1;arcSize=16;html=0;fillColor=#ffffff;strokeColor={c};strokeWidth=3;'
            f'fontColor={c};fontSize=23;fontStyle=1;{FONT}align=center;verticalAlign=middle;')


def texte_style(c=TEXTE, size=21, bold=False, italic=False, align='center', valign='top'):
    st = (1 if bold else 0) + (2 if italic else 0)
    return (f'text;html=0;align={align};verticalAlign={valign};{FONT}fontColor={c};fontSize={size};'
            f'fontStyle={st};strokeColor=none;fillColor=none;')


class Entree:
    def __init__(self, titre):
        self.titre = titre
        self.model = ET.Element('mxGraphModel')
        self.root = ET.SubElement(self.model, 'root')
        ET.SubElement(self.root, 'mxCell', id='0')
        ET.SubElement(self.root, 'mxCell', id='1', parent='0')
        self.n = 1
        self.x1 = self.y1 = 0

    def _id(self):
        self.n += 1
        return str(self.n)

    def vertex(self, value, style, x, y, w, h):
        c = ET.SubElement(self.root, 'mxCell', id=self._id(), value=value, style=style, vertex='1', parent='1')
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as': 'geometry'})
        self.x1, self.y1 = max(self.x1, x + w), max(self.y1, y + h)

    def edge(self, value, style, p0, p1, larg=0, haut=0):
        c = ET.SubElement(self.root, 'mxCell', id=self._id(), value=value, style=style, edge='1', parent='1')
        g = ET.SubElement(c, 'mxGeometry', relative='1', **{'as': 'geometry'})
        ET.SubElement(g, 'mxPoint', x=str(p0[0]), y=str(p0[1]), **{'as': 'sourcePoint'})
        ET.SubElement(g, 'mxPoint', x=str(p1[0]), y=str(p1[1]), **{'as': 'targetPoint'})
        self.x1 = max(self.x1, p0[0], p1[0], larg)
        self.y1 = max(self.y1, p0[1], p1[1], haut)

    def json(self):
        # ElementTree écrit les sauts de ligne des attributs en &#10; : ils survivent à la relecture XML.
        return {'xml': ET.tostring(self.model, encoding='unicode'), 'w': self.x1, 'h': self.y1,
                'aspect': 'fixed', 'title': self.titre}


def fonction(titre, nom, composant=POINTILLES, stock=False):
    e = Entree(titre)
    e.vertex(nom, bloc_style(FONCTIONS[nom]), 0, 0, W_BLOC, H_BLOC)
    e.vertex(composant, texte_style(), 0, H_BLOC + 8, W_BLOC, 32)
    if stock:
        e.vertex('Énergie chimique\nstockée', texte_style(YELLOW, 19), 0, H_BLOC + 44, W_BLOC, 50)
    return e


def absente(titre, nom, raison):
    e = Entree(titre)
    e.vertex(nom, f'rounded=1;arcSize=16;html=0;fillColor=#f2f2f2;strokeColor={GRIS};strokeWidth=3;dashed=1;'
                  f'dashPattern=8 6;fixDash=1;fontColor={GRIS_TEXTE};fontSize=23;fontStyle=1;{FONT}align=center;verticalAlign=middle;',
             0, 0, W_BLOC, H_BLOC)
    e.vertex(raison, texte_style(GRIS_TEXTE, 19, italic=True), 0, H_BLOC + 8, W_BLOC, 56)
    return e


def fleche(titre, label, c, dashed=False, both=False, vertical=False, size=18):
    e = Entree(titre)
    st = (f'edgeStyle=none;html=0;strokeColor={c};strokeWidth=3;endArrow=block;endFill=1;'
          f'startArrow={"block" if both else "none"};startFill=1;dashed={1 if dashed else 0};'
          f'{"dashPattern=8 6;fixDash=1;" if dashed else ""}fontColor={c};fontSize={size};{FONT}')
    if vertical:  # étiquette à droite du trait, jamais dessus (piège 7) — sans fond, qui masquerait le trait
        st += 'align=left;verticalAlign=middle;spacingLeft=10;'
        e.edge(label, st, (10, 0), (10, 130), larg=200, haut=130)
    else:         # étiquette au-dessus du trait
        st += 'align=center;verticalAlign=bottom;spacingBottom=4;labelBackgroundColor=#ffffff;'
        e.edge(label, st, (0, 60), (160, 60), larg=160, haut=60)
    return e


def texte(titre, value, c=TEXTE, size=21, bold=False, w=210, h=40):
    e = Entree(titre)
    e.vertex(value, texte_style(c, size, bold, valign='middle'), 0, 0, w, h)
    return e


def zone(titre, label, c, w):
    e = Entree(titre)
    e.vertex(label, f'rounded=1;arcSize=6;html=0;dashed=1;dashPattern=8 8;fixDash=1;fillColor=none;strokeColor={c};'
                    f'strokeWidth=2;fontColor={c};fontSize=21;fontStyle=1;{FONT}align=left;spacingLeft=14;'
                    f'verticalAlign=top;spacingTop=8;container=1;collapsible=0;', 0, 0, w, 230)
    return e


def pastille(titre, value, h=40):
    e = Entree(titre)
    e.vertex(value, f'rounded=1;arcSize=40;html=0;dashed=1;fillColor=#f5f5f5;strokeColor=#999999;strokeWidth=1;'
                    f'fontColor=#333333;fontSize=14;{FONT}align=center;verticalAlign=middle;', 0, 0, 170, h)
    return e


def matiere(titre, value, h=70):
    e = Entree(titre)
    e.vertex(value, f'rounded=0;html=0;fillColor=#d5e8d4;strokeColor=#82b366;strokeWidth=2;fontColor=#000000;'
                    f'fontSize=15;fontStyle=1;{FONT}align=center;verticalAlign=middle;', 0, 0, 170, h)
    return e


def vierge(titre, value):
    e = Entree(titre)
    e.vertex(value, f'rounded=1;arcSize=16;html=0;fillColor=#ffffff;strokeColor=#4d4d4d;strokeWidth=3;'
                    f'fontColor={TEXTE};fontSize=23;fontStyle=1;{FONT}align=center;verticalAlign=middle;',
             0, 0, W_BLOC, H_BLOC)
    e.vertex(POINTILLES, texte_style(), 0, H_BLOC + 8, W_BLOC, 32)
    return e


ENTREES = [
    # Chaîne d'information (en haut)
    fonction('1 · ACQUÉRIR + composant', 'ACQUÉRIR'),
    fonction('2 · TRAITER + composant', 'TRAITER'),
    fonction('3 · COMMUNIQUER + composant', 'COMMUNIQUER'),
    # Chaîne d'énergie (en bas)
    fonction('4 · ALIMENTER + composant', 'ALIMENTER'),
    fonction('4 bis · STOCKER (batterie, énergie stockée)', 'STOCKER', 'Batterie', stock=True),
    fonction('5 · DISTRIBUER + composant (l’ordre arrive ici)', 'DISTRIBUER'),
    fonction('6 · CONVERTIR + composant', 'CONVERTIR'),
    fonction('7 · TRANSMETTRE + composant', 'TRANSMETTRE'),
    absente('Fonction absente — TRANSMETTRE (pointillés, grisée)', 'TRANSMETTRE', 'Absente :\nrien ne se déplace'),
    absente('Fonction absente — à renommer, raison à écrire', 'FONCTION', 'Absente :\n' + POINTILLES),
    # Exercices
    vierge('Bloc vierge (fonction à écrire)', ''),
    vierge('Bloc « ? » (fonction à trouver)', '?'),
    # Zones
    zone('Zone — Chaîne d’information (en haut)', 'CHAÎNE D’INFORMATION — en haut (elle décide)', CYAN, 760),
    zone('Zone — Chaîne d’énergie (en bas)', 'CHAÎNE D’ÉNERGIE — en bas (elle obéit)', ORANGE, 1000),
    # Flèches
    fleche('Flèche d’information', 'Information', CYAN),
    fleche('Flèche de compte rendu (pointillés)', 'Compte rendu', CYAN, dashed=True),
    fleche('Flèche d’ordre — descend vers DISTRIBUER', 'Ordre :\nl’ordre descend', GREEN, dashed=True, vertical=True),
    fleche('Énergie électrique (flèche)', 'Énergie\nélectrique', ORANGE),
    fleche('Énergie mécanique (flèche)', 'Énergie\nmécanique', ORANGE),
    fleche('Énergie lumineuse (flèche)', 'Énergie\nlumineuse', ORANGE),
    fleche('Énergie sonore (flèche)', 'Énergie\nsonore', ORANGE),
    fleche('Énergie thermique (flèche)', 'Énergie\nthermique', ORANGE),
    fleche('Énergie à nommer (flèche)', 'Énergie\n' + POINTILLES, ORANGE),
    fleche('Batterie : charge / décharge (double flèche)', 'Énergie électrique\nCharge / décharge', YELLOW,
           both=True, vertical=True),
    # Sortie et textes
    texte('Action finale (en gras, à la sortie)', 'Action finale :\n' + POINTILLES, TEXTE, 22, True, 210, 60),
    texte('Titre du schéma (deux chaînes)', 'OBJET : l’information (en haut) commande l’énergie (en bas)',
          BLUE, 26, True, 820, 44),
    texte('Pied de schéma — la convention',
          'Convention : l’information EN HAUT, l’énergie EN BAS — l’ordre descend.\n'
          'Les fonctions sont dans les blocs ; les composants en dessous ; les formes d’énergie sur les flèches.',
          BLUE, 17, False, 900, 56),
    # Entrées de la chaîne d'information
    pastille('Grandeur physique à mesurer', 'Grandeur physique\nà mesurer', 48),
    pastille('Consigne', 'Consigne'),
    pastille('Information', 'Information'),
    pastille('Compte rendu', 'Compte rendu'),
    # Matière d'œuvre (circuit distinct des flèches d'énergie)
    matiere('Matière d’œuvre entrante', 'Matière d’œuvre\nENTRANTE'),
    matiere('Matière d’œuvre sortante', 'Matière d’œuvre\nSORTANTE'),
    matiere('Valeur ajoutée', 'VALEUR AJOUTÉE', 60),
]



VOCABULAIRE = {"ACQUÉRIR", "TRAITER", "COMMUNIQUER", "ALIMENTER", "STOCKER", "DISTRIBUER", "CONVERTIR",
               "TRANSMETTRE", "FONCTION", "?", ""}
DOIVENT_SE_LIRE = ("Énergie\nélectrique", "Énergie chimique\nstockée", "Grandeur physique\nà mesurer")


def texte_bibliotheque():
    data = json.dumps([e.json() for e in ENTREES], ensure_ascii=False, indent=1)
    return '<mxlibrary title="%s">%s</mxlibrary>\n' % (html.escape(TITRE, quote=True),
                                                       html.escape(data, quote=False))


def verifier(texte):
    """Relit une bibliothèque comme draw.io : XML, puis JSON, puis le XML de chaque forme.
    Rend (nombre de formes, liste des écarts) ; lève ValueError si rien n'est lisible."""
    try:
        racine = ET.fromstring(texte)
        formes = json.loads(racine.text or "")
    except (ET.ParseError, ValueError) as err:
        raise ValueError("bibliothèque illisible : %s" % err)
    if racine.tag != "mxlibrary" or not isinstance(formes, list) or not formes:
        raise ValueError("ce n'est pas une bibliothèque draw.io (mxlibrary avec au moins une forme)")
    ecarts, valeurs = [], []
    for f in formes:
        titre = f.get("title", "?")
        try:
            modele = ET.fromstring(f["xml"])
        except (ET.ParseError, KeyError, TypeError):
            ecarts.append("forme illisible : %s" % titre)
            continue
        for c in modele.iter("mxCell"):
            st = c.get("style")
            if st is None:
                continue
            v = c.get("value", "")
            valeurs.append(v)
            if not re.search(r"(^|;)html=0(;|$)", st):
                ecarts.append("texte HTML (html=0 attendu) : %s" % titre)
            if st.startswith("rounded=1;arcSize=16;") and v not in VOCABULAIRE:
                ecarts.append("bloc hors du vocabulaire des fonctions « %s » : %s" % (v, titre))
            if "dashPattern" in st and "fixDash=1" not in st:
                ecarts.append("pointillés sans fixDash=1 : %s" % titre)
    for attendu in DOIVENT_SE_LIRE:
        if attendu not in valeurs:
            ecarts.append("saut de ligne perdu ou forme absente : %r" % attendu)
    return len(formes), ecarts


def incorporer(texte):
    page = PAGE.read_text(encoding="utf-8")
    def remplace(m):
        fichiers = json.loads(m.group(1))
        if NOM_INCORPORE not in fichiers:
            raise SystemExit("La page du Book Train n'incorpore pas %s : arrêt." % NOM_INCORPORE)
        fichiers[NOM_INCORPORE] = texte
        return "var FICHIERS = " + json.dumps(fichiers, ensure_ascii=False) + ";"
    page, n = re.subn(r"var FICHIERS = (\{[^\n]*\});", remplace, page, count=1)
    if n != 1:
        raise SystemExit("Fichiers incorporés du Book Train introuvables : arrêt.")
    PAGE.write_text(page, encoding="utf-8")


def main(argv):
    if argv[:1] == ["--verifier"]:
        chemin = Path(argv[1]) if len(argv) > 1 else CIBLE
        if not chemin.is_file():
            return panne.rien_vu("aucune bibliothèque à lire : %s" % chemin)
        try:
            n, ecarts = verifier(chemin.read_text(encoding="utf-8"))
        except ValueError as err:
            return panne.rien_vu("%s (%s)" % (err, chemin))
        for e in ecarts:
            print("✘", e)
        print("%s : %d forme(s) lue(s), %d écart(s)." % (chemin.name, n, len(ecarts)))
        return 1 if ecarts else 0
    texte = texte_bibliotheque()
    n, ecarts = verifier(texte)
    if ecarts:
        print("\n".join("✘ " + e for e in ecarts))
        return 1
    if argv[:1] == ["--sortie"]:
        Path(argv[1]).write_text(texte, encoding="utf-8")
        print("écrit : %s (%d formes)" % (argv[1], n))
        return 0
    CIBLE.write_text(texte, encoding="utf-8")
    incorporer(texte)
    relu = CIBLE.read_text(encoding="utf-8")
    n2, ecarts2 = verifier(relu)
    print("écrit : %s (%d formes) et sa copie incorporée dans %s" % (CIBLE.relative_to(DEPOT), n2, PAGE.name))
    print("relu comme draw.io : %d écart(s)" % len(ecarts2))
    return 1 if ecarts2 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
