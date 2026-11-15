#!/usr/bin/env python3
"""generer_algorigramme_book_train.py — l'algorigramme corrigé du Book Train : le fichier draw.io et son dessin (15/11/2026).

Demande de Pascal du 15/11/2026, sur l'activité 3.2 du Book Train : « la correction doit montrer l'algorigramme complet,
de préférence de draw.io, car l'élève n'a encore aucune référence » ; « il découvre ces outils ». Règle d'or n°332.

CE QUE FAIT L'OUTIL
-------------------
Une seule description de l'algorigramme (les formes, leur place, les flèches) donne :
  · `fichiers_drawio/algorigramme_book-train_correction.drawio` : le fichier que l'élève ouvre dans draw.io. Les formes
    sont celles de la catégorie « Flowchart » de draw.io que le guide de l'activité fait chercher (Terminator, Data,
    Process, Decision), avec les couleurs du nuancier de draw.io ; les textes sont natifs (`html=0`) ;
  · `Images/algorigramme_book-train_correction.svg` : le même dessin, à la même place, pour la page (textes natifs, aucune
    ressource distante) ;
  · dans la page, la figure de la correction de 3.2 (en ligne, ses id préfixés `fig3`) et le fichier embarqué pour le
    bouton de téléchargement (`var FICHIERS`), avec celui de la chaîne d'information corrigée (correction de 2.3).
Les flèches NON rejoignent le trait vertical du flux (un point de jonction), jamais le flanc d'un bloc : c'est
l'auto-vérification ⑥ de l'activité.

Usage : python3 _outils/generer_algorigramme_book_train.py            # écrit les trois
        python3 _outils/generer_algorigramme_book_train.py --verifier # 0 : à jour ; 1 : à régénérer
"""
from html import escape
from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET

RACINE = Path(__file__).resolve().parents[1]
LOT = RACINE / 'theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1_book-train'
DRAWIO = LOT / 'fichiers_drawio/algorigramme_book-train_correction.drawio'
SVG = LOT / 'Images/algorigramme_book-train_correction.svg'
PAGE = LOT / 'sequence_4e_C4.1-C4.2-C4.4_book-train.html'

W, H, CX = 480, 1030, 240
# le nuancier de draw.io (panneau Format → Style) : ce que l'élève obtient en cliquant une pastille
STYLES = {
    'debut':    ('shape=mxgraph.flowchart.terminator', '#d5e8d4', '#82b366'),
    'donnee':   ('shape=mxgraph.flowchart.data', '#dae8fc', '#6c8ebf'),
    'action':   ('shape=mxgraph.flowchart.process', '#f8cecc', '#b85450'),
    'test':     ('shape=mxgraph.flowchart.decision', '#fff2cc', '#d6b656'),
}
# (id, sorte, texte, x, y, largeur, hauteur)
FORMES = [
    ('debut', 'debut', 'DÉBUT', 180, 20, 120, 44),
    ('commande', 'donnee', 'Entrée : le lecteur\ncommande un livre', 120, 94, 240, 56),
    ('chercher', 'action', 'Chercher le livre au sous-sol\n(magasinier)', 120, 180, 240, 56),
    ('vacant', 'test', 'Wagonnet vacant\ndisponible ?', 105, 290, 270, 110),
    ('deposer', 'action', 'Déposer le livre et\nprogrammer la destination', 120, 440, 240, 56),
    ('rouler', 'action', 'Rouler : tunnel puis\nmontée verticale', 120, 550, 240, 56),
    ('arrive', 'test', 'Arrivé à la station\ndu 3ᵉ étage ?', 105, 636, 270, 110),
    ('remis', 'donnee', 'Sortie : le livre est\nremis au lecteur', 120, 786, 240, 56),
    ('repartir', 'action', 'Repartir à vide au sous-sol', 120, 872, 240, 56),
    ('fin', 'debut', 'FIN', 180, 958, 120, 44),
]
JONCTIONS = [('j1', CX, 266), ('j2', CX, 526)]   # là où la flèche NON rejoint le trait vertical du flux
# (de, vers, points intermédiaires, étiquette, (x, y) de l'étiquette, pointe)
FLECHES = [
    ('debut', 'commande', [], None, None, True),
    ('commande', 'chercher', [], None, None, True),
    ('chercher', 'j1', [], None, None, False),
    ('j1', 'vacant', [], None, None, True),
    ('vacant', 'j1', [(60, 345), (60, 266)], 'NON', (82, 330), True),
    ('vacant', 'deposer', [], 'OUI', (262, 422), True),
    ('deposer', 'j2', [], None, None, False),
    ('j2', 'rouler', [], None, None, True),
    ('rouler', 'arrive', [], None, None, True),
    ('arrive', 'j2', [(60, 691), (60, 526)], 'NON', (82, 676), True),
    ('arrive', 'remis', [], 'OUI', (262, 768), True),
    ('remis', 'repartir', [], None, None, True),
    ('repartir', 'fin', [], None, None, True),
]
TITRE = 'Algorigramme corrigé du trajet d’un livre dans le Book Train'
DESC = ('Algorigramme de haut en bas. DÉBUT. Entrée : le lecteur commande un livre. Action : chercher le livre au sous-sol '
        '(magasinier). Test : wagonnet vacant disponible ? Si NON, la flèche remonte et rejoint le trait vertical juste '
        'au-dessus du test : on attend. Si OUI : déposer le livre et programmer la destination, puis rouler (tunnel puis '
        'montée verticale). Test : arrivé à la station du 3ᵉ étage ? Si NON, la flèche remonte et rejoint le trait vertical '
        'juste au-dessus de « rouler » : on continue de rouler. Si OUI : sortie, le livre est remis au lecteur ; action : '
        'repartir à vide au sous-sol. FIN.')


def _ancres():
    a = {f[0]: f for f in FORMES}
    pts = {}
    for i, s, t, x, y, w, h in FORMES:
        pts[i] = {'haut': (x + w / 2, y), 'bas': (x + w / 2, y + h), 'gauche': (x, y + h / 2)}
    for i, x, y in JONCTIONS:
        pts[i] = {'haut': (x, y), 'bas': (x, y), 'gauche': (x, y)}
    return a, pts


def _trace(de, vers, inter):
    _, pts = _ancres()
    if inter:   # la boucle NON : elle part du sommet gauche du losange
        return [pts[de]['gauche']] + inter + [pts[vers]['haut']]
    return [pts[de]['bas'], pts[vers]['haut']]


def drawio():
    fichier = ET.Element('mxfile', host='app.diagrams.net', type='device')
    dg = ET.SubElement(fichier, 'diagram', id='algorigramme', name='Algorigramme du Book Train — correction')
    mod = ET.SubElement(dg, 'mxGraphModel', dx='800', dy='1100', grid='1', gridSize='10', guides='1', tooltips='1',
                        connect='1', arrows='1', fold='1', page='1', pageScale='1', pageWidth=str(W), pageHeight=str(H),
                        math='0', shadow='0')
    root = ET.SubElement(mod, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')
    for i, s, t, x, y, w, h in FORMES:
        forme, fond, trait = STYLES[s]
        c = ET.SubElement(root, 'mxCell', id=i, value=t, vertex='1', parent='1',
                          style=f'{forme};whiteSpace=wrap;html=0;fillColor={fond};strokeColor={trait};strokeWidth=2;'
                                f'fontFamily=Helvetica;fontSize=15;fontColor=#1a1a1a;' + ('fontStyle=1;' if s == 'debut' else ''))
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as': 'geometry'})
    for i, x, y in JONCTIONS:
        c = ET.SubElement(root, 'mxCell', id=i, value='', vertex='1', parent='1',
                          style='shape=waypoint;sketch=0;size=6;pointerEvents=1;points=[];fillColor=none;resizable=0;'
                                'rotatable=0;perimeter=centerPerimeter;snapToPoint=1;strokeColor=#1a1a1a;')
        ET.SubElement(c, 'mxGeometry', x=str(x - 10), y=str(y - 10), width='20', height='20', **{'as': 'geometry'})
    for k, (de, vers, inter, etiq, _, pointe) in enumerate(FLECHES):
        style = ('edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;strokeColor=#1a1a1a;strokeWidth=2;'
                 f'endArrow={"block" if pointe else "none"};endFill=1;fontFamily=Helvetica;fontSize=14;fontStyle=1;'
                 'labelBackgroundColor=#ffffff;')
        if inter:
            style += 'exitX=0;exitY=0.5;exitDx=0;exitDy=0;'
        c = ET.SubElement(root, 'mxCell', id=f'f{k}', value=etiq or '', edge='1', parent='1', source=de, target=vers, style=style)
        g = ET.SubElement(c, 'mxGeometry', relative='1', **{'as': 'geometry'})
        if inter:
            a = ET.SubElement(g, 'Array', **{'as': 'points'})
            for x, y in inter:
                ET.SubElement(a, 'mxPoint', x=str(x), y=str(y))
    ET.indent(fichier)
    return ET.tostring(fichier, encoding='unicode') + '\n'


def svg():
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
         f'aria-labelledby="t d" font-family="Helvetica, Arial, sans-serif" style="width:100%;height:auto">',
         f'<title id="t">{escape(TITRE)}</title><desc id="d">{escape(DESC)}</desc>',
         '<defs><marker id="pointe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" '
         'orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M0 0L10 5L0 10Z" fill="#1a1a1a"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    for de, vers, inter, etiq, pos, pointe in FLECHES:
        pts = _trace(de, vers, inter)
        if pointe:   # la pointe touche la forme (ou le trait) sans le recouvrir
            (x0, y0), (x1, y1) = pts[-2], pts[-1]
            dx, dy = (x1 > x0) - (x1 < x0), (y1 > y0) - (y1 < y0)
            pts[-1] = (x1 - dx, y1 - dy)
        d = 'M ' + ' L '.join(f'{x:g} {y:g}' for x, y in pts)
        p.append(f'<path d="{d}" fill="none" stroke="#1a1a1a" stroke-width="2"{" marker-end=" + chr(34) + "url(#pointe)" + chr(34) if pointe else ""}/>')
    for i, x, y in JONCTIONS:
        p.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#1a1a1a"/>')
    for i, s, t, x, y, w, h in FORMES:
        _, fond, trait = STYLES[s]
        att = f'fill="{fond}" stroke="{trait}" stroke-width="2"'
        if s == 'debut':
            p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2:g}" {att}/>')
        elif s == 'donnee':
            e = 20
            p.append(f'<polygon points="{x + e},{y} {x + w},{y} {x + w - e},{y + h} {x},{y + h}" {att}/>')
        elif s == 'action':
            p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {att}/>')
        else:
            p.append(f'<polygon points="{x + w / 2:g},{y} {x + w},{y + h / 2:g} {x + w / 2:g},{y + h} {x},{y + h / 2:g}" {att}/>')
        lignes = t.split('\n')
        for k, l in enumerate(lignes):
            yy = y + h / 2 + 5 + (k - (len(lignes) - 1) / 2) * 19
            p.append(f'<text x="{x + w / 2:g}" y="{yy:g}" font-size="15" text-anchor="middle" fill="#1a1a1a"'
                     f'{" font-weight=" + chr(34) + "700" + chr(34) if s == "debut" else ""}>{escape(l)}</text>')
    for de, vers, inter, etiq, pos, pointe in FLECHES:
        if etiq:
            x, y = pos
            p.append(f'<rect x="{x - 19}" y="{y - 14}" width="38" height="19" fill="#ffffff"/>'
                     f'<text x="{x}" y="{y}" font-size="14" font-weight="700" text-anchor="middle" fill="#1a1a1a">{etiq}</text>')
    p.append('</svg>')
    return '\n'.join(p) + '\n'


def page(html, dessin, source):
    """La figure de la correction de 3.2 (en ligne, id préfixés fig3) et le fichier embarqué pour le téléchargement."""
    en_ligne = dessin.rstrip('\n')
    for ident in re.findall(r'\bid="([^"]+)"', en_ligne):
        en_ligne = en_ligne.replace(f'id="{ident}"', f'id="fig3{ident}"').replace(f'url(#{ident})', f'url(#fig3{ident})')
    en_ligne = en_ligne.replace('aria-labelledby="t d"', 'aria-labelledby="fig3t fig3d"')
    en_ligne = en_ligne.replace('style="width:100%;height:auto"', 'style="width:100%;height:auto;max-width:440px"', 1)
    html, n = re.subn(r'<svg\b[^>]*aria-labelledby="fig3t fig3d"[^>]*>.*?</svg>', lambda _: en_ligne, html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('Figure 3 du Book Train introuvable')

    def fichiers(m):
        f = json.loads(m.group(1))
        f['algorigramme_book-train_correction.drawio'] = source
        # la chaîne d'information corrigée de 2.3 : l'élève la télécharge aussi (n°332), plus seulement le professeur
        f['chaine_information_correction.drawio'] = (LOT / 'fichiers_drawio/chaine_information_correction.drawio').read_text(encoding='utf-8')
        return 'var FICHIERS = ' + json.dumps(f, ensure_ascii=False) + ';'
    html, n = re.subn(r'var FICHIERS = (\{[^\n]*\});', fichiers, html, count=1)
    if n != 1:
        raise SystemExit('Fichiers embarqués du Book Train introuvables')
    return html


def main(argv):
    source, dessin = drawio(), svg()
    html = page(PAGE.read_text(encoding='utf-8'), dessin, source)
    cibles = [(DRAWIO, source), (SVG, dessin), (PAGE, html)]
    if '--verifier' in argv:
        perimes = [str(c.relative_to(RACINE)) for c, t in cibles if not c.exists() or c.read_text(encoding='utf-8') != t]
        for c in perimes:
            print('✘ à régénérer :', c)
        print('✅ algorigramme du Book Train à jour' if not perimes else '✘ python3 _outils/generer_algorigramme_book_train.py')
        return 1 if perimes else 0
    for c, t in cibles:
        c.write_text(t, encoding='utf-8')
        print('✎', c.relative_to(RACINE))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
