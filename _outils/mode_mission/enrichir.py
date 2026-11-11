#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrire dans une séquence le pourquoi des erreurs et les réponses leurres, depuis un fichier de données.

Pourquoi (rapport de recherche du 11/11/2026, `docs/mode-mission/PLAN.md`) : un retour qui explique l'erreur aide
bien plus qu'un « juste / faux » ; et une grille où il y a autant de réponses que de lignes donne la dernière.

Le fichier de données (`mission_<lot>.json`, à côté de la séquence) :

    {
      "pourquoi": { "e1_5": { "le capteur de luminosité": "Il mesure la lumière : il ne voit pas un passage.", … } },
      "indices":  { "e1_2": "Stocker, c'est garder l'énergie pour s'en servir plus tard.", … },
      "leurres":  { "e1_1": ["le mât", "le capteur de luminosité"] }
    }

  · "pourquoi" — par question à choix, pour chaque MAUVAISE proposition : pourquoi elle ne convient pas, sans dire
    la bonne. La proposition se nomme par son début (un début qui désigne deux propositions est refusé).
    Écrit `data-pourquoi` sur le bouton radio.
  · "indices" — par ligne d'une grille ou d'une rangée : ce que la ligne demande. Écrit `data-indice` sur le groupe.
  · "leurres" — par grille (nommée par sa première ligne) : des réponses de trop, plausibles, qui ne vont avec aucune
    ligne. Ajoute la réponse à la légende et à chaque ligne, à une place tirée du nom (jamais toujours la dernière),
    relettre A, B, C… et le dit dans le titre de la légende.

L'outil ne change ni les questions ni les réponses attendues ; il se rejoue sans rien changer. Le mode mission lit
ces attributs ; le banc générique refuse un « pourquoi » posé sur une bonne réponse.

Usage :
    python3 _outils/mode_mission/enrichir.py <sequence.html> <mission_<lot>.json>            # écrit
    python3 _outils/mode_mission/enrichir.py <sequence.html> <mission_<lot>.json> --verifier # dit si la page est à jour
"""
import hashlib
import html
import json
import pathlib
import re
import sys

GROUPE = r'<fieldset class="(qcm-groupe[^"]*)" id="%s"([^>]*)>(.*?)</fieldset>'
RADIO = re.compile(r'<input type="radio"([^>]*?)\svalue="([^"]*)"([^>]*)>')
CLES = re.compile(r'<div class="qcm-cles"><p class="qcm-cles-titre">(.*?)</p><ol>(.*?)</ol></div>', re.S)
LETTRES = 'ABCDEFGHIJKL'
TROP = re.compile(r'&nbsp;; <b>[^<]*aucune ligne</b>')


def brut(v):
    return html.unescape(v)


def attr(v):
    return html.escape(v, quote=True).replace('&#x27;', "'")        # l'attribut est entre guillemets doubles


def sans(attrs, nom):
    return re.sub(r'\s%s="[^"]*"' % nom, '', attrs)


def groupe(source, ident):
    m = re.search(GROUPE % re.escape(ident), source, re.S)
    if not m:
        raise SystemExit('✘ groupe introuvable : %s' % ident)
    return m


def poser_pourquoi(source, ident, raisons):
    m = groupe(source, ident)
    corps = m.group(3)
    valeurs = [brut(v) for _, v, _ in RADIO.findall(corps)]
    cible = {}
    for debut, texte in raisons.items():
        trouve = [v for v in valeurs if v == debut] or [v for v in valeurs if v.startswith(debut)]
        if len(trouve) != 1:
            raise SystemExit('✘ %s : « %s » désigne %d proposition(s) — %s' % (ident, debut, len(trouve), ' | '.join(valeurs)))
        cible[trouve[0]] = texte

    def un(r):
        avant, v, apres = r.group(1), r.group(2), sans(r.group(3), 'data-pourquoi')
        avant = sans(avant, 'data-pourquoi')
        t = cible.get(brut(v))
        return '<input type="radio"%s value="%s"%s%s>' % (avant, v, apres, ' data-pourquoi="%s"' % attr(t) if t else '')

    return source[:m.start(3)] + RADIO.sub(un, corps) + source[m.end(3):]


def poser_indice(source, ident, texte):
    m = groupe(source, ident)
    attrs = sans(m.group(2), 'data-indice') + ' data-indice="%s"' % attr(texte)
    return source[:m.start()] + '<fieldset class="%s" id="%s"%s>%s</fieldset>' % (m.group(1), ident, attrs, m.group(3)) + source[m.end():]


def poser_leurres(page, source, ident, leurres):
    m = groupe(source, ident)
    if 'qcm-grille' not in m.group(1).split():
        raise SystemExit('✘ %s n\'est pas la première ligne d\'une grille' % ident)
    legendes = [c for c in CLES.finditer(source) if c.end() <= m.start()]
    if not legendes:
        raise SystemExit('✘ %s : pas de légende de grille avant ce groupe' % ident)
    cles = legendes[-1]
    if source[cles.end():m.start()].strip():
        raise SystemExit('✘ %s ne suit pas directement sa légende' % ident)
    # les lignes de la grille : les groupes `qcm-grille` qui se suivent après la légende
    lignes, pos = [], cles.end()
    suivant = re.compile(r'\s*<fieldset class="(qcm-groupe[^"]*)" id="([^"]+)"([^>]*)>(.*?)</fieldset>', re.S)
    while True:
        g = suivant.match(source, pos)
        if not g or 'qcm-grille' not in g.group(1).split():
            break
        lignes.append(g)
        pos = g.end()
    reponses = [brut(re.sub(r'<[^>]+>', '', li)[1:]) for li in re.findall(r'<li>(.*?)</li>', cles.group(2), re.S)]
    dedans = [brut(v) for _, v, _ in RADIO.findall(lignes[0].group(4))]
    if reponses != dedans:
        raise SystemExit('✘ %s : la légende et la première ligne ne portent pas les mêmes réponses' % ident)
    nom = pathlib.Path(page).name
    for texte in leurres:
        if texte in reponses:
            continue
        graine = int(hashlib.sha256((nom + '#' + ident + '#' + texte).encode()).hexdigest(), 16)
        reponses.insert(graine % (len(reponses) + 1), texte)
    en_trop = len(reponses) - len(lignes)
    titre = TROP.sub('', cles.group(1))
    if en_trop > 0:
        accord = ('%d réponses ne servent' % en_trop) if en_trop > 1 else 'une réponse ne sert'
        titre = re.sub(r'(&nbsp;:|\s:)\s*$', '', titre) + '&nbsp;; <b>%s à aucune ligne</b>&nbsp;:' % accord
    legende = '<div class="qcm-cles"><p class="qcm-cles-titre">%s</p><ol>%s</ol></div>' % (
        titre, ''.join('<li><b>%s</b>%s</li>' % (LETTRES[k], attr(t)) for k, t in enumerate(reponses)))
    morceaux, fin = [source[:cles.start()], legende, source[cles.end():lignes[0].start()]], lignes[0].start()
    for g in lignes:
        gid = g.group(2)
        options = '\n'.join(
            '  <div class="qcm-option"><input type="radio" name="%s" id="%s__%d" value="%s" aria-label="%s — %s"><label for="%s__%d" title="%s">%s</label></div>'
            % (gid, gid, k + 1, attr(t), LETTRES[k], attr(t), gid, k + 1, attr(t), LETTRES[k]) for k, t in enumerate(reponses))
        leg = re.search(r'<legend>.*?</legend>', g.group(4), re.S).group(0)
        morceaux.append(source[fin:g.start()])
        morceaux.append(re.match(r'\s*', g.group(0)).group(0) + '<fieldset class="%s" id="%s"%s>\n  %s\n%s\n</fieldset>' % (g.group(1), gid, g.group(3), leg, options))
        fin = g.end()
    morceaux.append(source[fin:])
    return ''.join(morceaux)


def enrichir(page, donnees):
    source = pathlib.Path(page).read_text(encoding='utf-8')
    for ident, liste in donnees.get('leurres', {}).items():
        source = poser_leurres(page, source, ident, liste)
    for ident, raisons in donnees.get('pourquoi', {}).items():
        source = poser_pourquoi(source, ident, raisons)
    for ident, texte in donnees.get('indices', {}).items():
        source = poser_indice(source, ident, texte)
    return source


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    if len(args) != 2:
        print(__doc__)
        return 2
    page, fichier = args
    donnees = json.loads(pathlib.Path(fichier).read_text(encoding='utf-8'))
    avant = pathlib.Path(page).read_text(encoding='utf-8')
    apres = enrichir(page, donnees)
    n = (sum(len(v) for v in donnees.get('pourquoi', {}).values()), len(donnees.get('indices', {})),
         sum(len(v) for v in donnees.get('leurres', {}).values()))
    if '--verifier' in argv:
        print(('✅ à jour' if avant == apres else '✘ la page n\'est pas à jour avec ses données') + ' — %d pourquoi, %d indices, %d leurres' % n)
        return 0 if avant == apres else 1
    if avant != apres:
        pathlib.Path(page).write_text(apres, encoding='utf-8')
    print('%s %s : %d pourquoi, %d indices, %d leurres' % ('✎' if avant != apres else '·', page, *n))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
