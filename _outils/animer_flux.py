#!/usr/bin/env python3
"""animer_flux.py — les flux des chaînes d'énergie et d'information, animés (15/11/2026).

Demande de Pascal du 15/11/2026 : « les chaînes d'énergie et chaîne d'information devront être animées (tous les flux),
et de préférence faites avec draw.io », « nb la bibliothèque pour ces chaînes dans draw.io ».

CE QUE FAIT L'OUTIL
-------------------
Sur chaque flèche d'un schéma de chaîne (un trait qui porte une pointe : `marker-end`, ou `marker-start` pour une
double flèche), il pose, juste après elle, un second tracé de même géométrie : des points clairs qui avancent le long
de la flèche, dans son sens (une double flèche reçoit deux trains de points, un dans chaque sens). Le trait d'origine
ne change pas : couleur, pointillés (l'ordre, le compte rendu) et pointe restent ce qu'ils disent (n°6, n°310) ;
l'animation ne porte aucune information que le dessin ne porte déjà (n°119).
  · `prefers-reduced-motion` : les points disparaissent ;
  · à l'impression : les points disparaissent, le schéma s'imprime fixe ;
  · rien n'est chargé depuis Internet (n°305) : la feuille d'animation est dans le SVG.
L'outil est rejouable : un SVG déjà animé n'est pas touché (sa feuille porte `id="flux-anime"`).

Les sources draw.io des chaînes portent l'animation native de draw.io (`flowAnimation=1` sur chaque flèche) : c'est
`regenerer_chaines_energie.py` et `generer_bibliotheque_chaines.py` qui l'écrivent, pas cet outil.

OÙ IL S'APPLIQUE
----------------
  · un fichier SVG : tout le dessin ;
  · une page HTML : chaque `<svg>` en ligne qui est une chaîne (un nom de fonction ACQUÉRIR, TRAITER, ALIMENTER…
    et au moins une pointe de flèche) ; les autres SVG de la page ne sont pas touchés.

Usage :
    python3 _outils/animer_flux.py <fichier.svg|page.html>… [--ecrire]   # sans --ecrire : ce qui changerait
    python3 _outils/animer_flux.py --verifier <fichier>…                 # 0 : chaque chaîne est animée ; 1 : non
"""
import re
import sys

FEUILLE = (
    '<style id="flux-anime">'
    # des perles claires (un trait de longueur presque nulle, bouts ronds, un peu plus épais que la flèche) tous les
    # 42 px : le trait reste continu entre elles, on ne les confond pas avec les pointillés de l'ordre
    '.flux{fill:none;stroke:#ffffff;stroke-opacity:.9;stroke-linecap:round;stroke-dasharray:.1 42;'
    'animation:flux-avance 1.6s linear infinite;pointer-events:none}'
    '.flux.retour{animation-direction:reverse;animation-delay:-.8s}'
    '@keyframes flux-avance{from{stroke-dashoffset:42.1}to{stroke-dashoffset:0}}'
    '@media (prefers-reduced-motion:reduce){.flux{display:none}}'
    '@media print{.flux{display:none}}'
    '</style>'
)
FONCTIONS = re.compile(r'ALIMENTER|DISTRIBUER|CONVERTIR|ACQU(?:É|&#201;|&#xC9;)RIR|TRAITER|COMMUNIQUER|TRANSMETTRE|STOCKER')
TRACE = re.compile(r'<(path|line|polyline)\b([^>]*?)\s*(/?)>', re.S)
# une page qui incorpore le SVG peut préfixer ses id (« fig4flux-anime ») : la feuille compte quand même
DEJA = re.compile(r'id="[\w-]*flux-anime"')
GEOMETRIE = {'path': ('d',), 'line': ('x1', 'y1', 'x2', 'y2'), 'polyline': ('points',)}


def attr(attrs, nom):
    m = re.search(r'(?:^|\s)%s\s*=\s*"([^"]*)"' % re.escape(nom), attrs)
    return m.group(1) if m else None


def _animer_svg(svg):
    """Pose les points qui avancent sur chaque flèche d'un SVG ; rend (svg, nombre de flèches animées)."""
    if DEJA.search(svg):
        return svg, 0
    # les <defs> (pointes de flèche, motifs) ne sont jamais animés
    zones_defs = [(m.start(), m.end()) for m in re.finditer(r'<defs\b.*?</defs>', svg, re.S)]
    sortie, pos, n = [], 0, 0
    for m in TRACE.finditer(svg):
        if any(a <= m.start() < b for a, b in zones_defs):
            continue
        tag, attrs, ferme = m.group(1), m.group(2), m.group(3)
        fin_pointe, debut_pointe = attr(attrs, 'marker-end'), attr(attrs, 'marker-start')
        classe = attr(attrs, 'class') or ''
        # une flèche dessinée d'un seul tracé, sa pointe comprise (« M130 422H205 M197 416L205 422L197 428 ») : le
        # premier sous-tracé est le trait ; c'est lui qui porte les perles
        pointe_dessinee = tag == 'path' and re.search(r'(^|\s)(vpp-)?fleche(\s|$)', classe) and not (fin_pointe or debut_pointe)
        if not (fin_pointe or debut_pointe or pointe_dessinee) or classe.startswith('flux'):
            continue
        geo = ' '.join('%s="%s"' % (g, attr(attrs, g)) for g in GEOMETRIE[tag] if attr(attrs, g) is not None)
        if pointe_dessinee:
            trait = re.match(r'\s*(M[^M]*)', attr(attrs, 'd') or '')
            geo = 'd="%s"' % trait.group(1).strip() if trait else geo
        if not geo:
            continue
        extra = ' transform="%s"' % attr(attrs, 'transform') if attr(attrs, 'transform') else ''
        largeur = attr(attrs, 'stroke-width')
        if largeur is None:
            m_w = re.search(r'stroke-width\s*:\s*([\d.]+)', attr(attrs, 'style') or '')
            largeur = m_w.group(1) if m_w else '3'
        try:  # la perle déborde un peu du trait : 3 px de plus que lui
            extra += ' stroke-width="%g"' % (float(re.sub(r'[^\d.]', '', largeur) or 3) + 3)
        except ValueError:
            extra += ' stroke-width="6"'
        # la fin de l'élément d'origine : une balise auto-fermée, ou la balise fermante qui suit
        if ferme:
            fin = m.end()
        else:
            k = svg.find('</%s>' % tag, m.end())
            fin = k + len('</%s>' % tag) if k >= 0 else m.end()
        traces = []
        if fin_pointe or not debut_pointe:
            traces.append('<%s class="flux" %s%s aria-hidden="true"/>' % (tag, geo, extra))
        if debut_pointe:
            traces.append('<%s class="flux retour" %s%s aria-hidden="true"/>' % (tag, geo, extra))
        sortie.append(svg[pos:fin])
        sortie.append(''.join(traces))
        pos = fin
        n += 1
    if not n:
        return svg, 0
    sortie.append(svg[pos:])
    svg = ''.join(sortie)
    # la feuille juste après la balise <svg …>
    m = re.search(r'<svg\b[^>]*>', svg)
    svg = svg[:m.end()] + FEUILLE + svg[m.end():]
    return svg, n


def animer(texte, est_html=False):
    """Un SVG entier, ou une page : chaque <svg> en ligne qui est une chaîne. Rend (texte, flèches animées, dessins)."""
    if not est_html:
        t, n = _animer_svg(texte)
        return t, n, 1 if n else 0
    total = dessins = 0
    morceaux, pos = [], 0
    for m in re.finditer(r'<svg\b.*?</svg>', texte, re.S):
        bloc = m.group(0)
        if not (FONCTIONS.search(bloc) and ('marker' in bloc or 'fleche' in bloc)):
            continue
        neuf, n = _animer_svg(bloc)
        if n:
            morceaux += [texte[pos:m.start()], neuf]
            pos = m.end()
            total += n
            dessins += 1
    morceaux.append(texte[pos:])
    return ''.join(morceaux), total, dessins


def a_animer(texte, est_html):
    """Les chaînes du texte qui n'ont pas encore leurs flux animés (pour --verifier)."""
    blocs = re.findall(r'<svg\b.*?</svg>', texte, re.S) if est_html else [texte]
    reste = 0
    for b in blocs:
        if est_html and not (FONCTIONS.search(b) and ('marker' in b or 'fleche' in b)):
            continue
        if DEJA.search(b):
            continue
        if _animer_svg(b)[1]:
            reste += 1
    return reste


def main(argv):
    ecrire, verifier = '--ecrire' in argv, '--verifier' in argv
    fichiers = [a for a in argv if not a.startswith('--')]
    if not fichiers:
        print(__doc__)
        return 2
    t_fl = t_de = ecarts = 0
    for f in fichiers:
        est_html = f.endswith('.html')
        texte = open(f, encoding='utf-8').read()
        if verifier:
            r = a_animer(texte, est_html)
            if r:
                print('✘ %s : %d chaîne(s) sans flux animés' % (f, r))
                ecarts += 1
            continue
        neuf, n, d = animer(texte, est_html)
        if n:
            print(('✎ ' if ecrire else '· ') + '%s : %d flèche(s) animée(s) dans %d dessin(s)' % (f, n, d))
            t_fl += n
            t_de += d
            if ecrire:
                open(f, 'w', encoding='utf-8').write(neuf)
    if verifier:
        print('✅ chaque chaîne lue a ses flux animés' if not ecarts else '✘ %d fichier(s) à animer' % ecarts)
        return 1 if ecarts else 0
    print('%d fichier(s) lus · %d flèche(s) %s dans %d dessin(s)' % (len(fichiers), t_fl, 'animées' if ecrire else 'à animer', t_de))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
