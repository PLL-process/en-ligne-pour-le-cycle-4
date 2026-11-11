#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mélanger les propositions des groupes de boutons radio (règle d'or n°300).

Constat de Pascal, le 11/11/2026, sur le lampadaire de 5e : « on dirait que les bonnes réponses sont
toujours les premières ». Les listes déroulantes rangeaient la bonne réponse juste sous « — choisir — » ;
converties en boutons radio, elles la montrent en tête de chaque question.

Ce que fait l'outil, pour chaque `fieldset.qcm-groupe` d'une page :
  · la proposition qui était en tête prend une place tirée à tour de rôle (1re, 2e, 3e, 4e…), pour que,
    sur la page, la tête de liste ne dise plus rien ; les autres propositions sont mélangées autour ;
  · le tirage est fixé par le nom de la page et l'identifiant du groupe : rejouer l'outil ne change rien
    (le groupe porte `data-melange="1"`).

Ce qu'il ne touche pas :
  · une grille lettrée (`qcm-grille`), une rangée (`qcm-rangee`) et un positionnement (`positionnement`) :
    leur ordre est une échelle ou une légende ;
  · un groupe dont les propositions sont des nombres, ou une échelle à pastilles (🔴 🟠 🟡 🟢 ⭐) ;
  · un groupe de deux propositions ;
  · une incrustation d'atelier (son texte se règle à sa source) ;
  · les propositions qui ferment une liste (« je ne sais pas encore », « aucune de ces réponses »,
    « les deux », « autre »…) : elles restent en dernier.

Usage :
    python3 _outils/melanger_propositions.py <page.html> [...]            # dit ce qui serait fait
    python3 _outils/melanger_propositions.py <page.html> [...] --ecrire   # le fait
"""
import hashlib
import html
import pathlib
import random
import re
import sys

GROUPE = re.compile(r'<fieldset class="(qcm-groupe[^"]*)"([^>]*)>(.*?)</fieldset>', re.S)
OPTION = re.compile(r'[ \t]*<div class="qcm-option">.*?</div>[ \t]*\n?', re.S)
INCRUSTATION = re.compile(r'<!-- ateliers-representations:debut.*?<!-- ateliers-representations:fin[^>]*-->', re.S)
FIXES = ('qcm-grille', 'qcm-rangee', 'positionnement')
PASTILLES = ('🔴', '🟠', '🟡', '🟢', '⭐')
FERMETURE = re.compile(r"^(je ne sais pas|aucun|aucune|toutes ces|tous ces|les deux|les trois|autre\b|"
                       r"on ne peut pas savoir|ni l.un ni l.autre)", re.I)


def texte(option):
    m = re.search(r'<label[^>]*>(.*?)</label>', option, re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1) if m else option)).strip()


def melanger(page, source):
    zones = [(m.start(), m.end()) for m in INCRUSTATION.finditer(source)]
    nom = pathlib.Path(page).name
    tour = [0]
    faits = []

    def un_groupe(m):
        classes, attrs, corps = m.group(1), m.group(2), m.group(3)
        if any(a <= m.start() < b for a, b in zones):
            return m.group(0)
        if any(c in classes.split() for c in FIXES) or 'data-melange' in attrs:
            return m.group(0)
        options = OPTION.findall(corps)
        if len(options) < 3 or ''.join(options) not in corps:
            return m.group(0)                      # les propositions ne se suivent pas : on ne devine pas
        libelles = [texte(o) for o in options]
        if all(re.fullmatch(r'[\d\s.,%°]+', t) for t in libelles) or any(t.startswith(PASTILLES) for t in libelles):
            return m.group(0)
        mobiles = [k for k, t in enumerate(libelles) if not FERMETURE.match(t)]
        if len(mobiles) < 3:
            return m.group(0)
        ident = re.search(r'id="([^"]+)"', attrs)
        graine = int(hashlib.sha256((nom + '#' + (ident.group(1) if ident else str(m.start()))).encode()).hexdigest(), 16)
        alea = random.Random(graine)
        place = (tour[0] + graine % 2) % len(mobiles)   # la tête de liste change de place à tour de rôle
        tour[0] += 1
        reste = mobiles[1:]
        alea.shuffle(reste)
        ordre = reste[:place] + [mobiles[0]] + reste[place:]
        nouvelles = list(options)
        for cible, origine in zip(mobiles, ordre):
            nouvelles[cible] = options[origine]
        bloc = ''.join(options)
        corps2 = corps.replace(bloc, ''.join(nouvelles), 1)
        faits.append(place)
        return '<fieldset class="%s"%s data-melange="1">%s</fieldset>' % (classes, attrs, corps2)

    return GROUPE.sub(un_groupe, source), faits


def main(argv):
    ecrire = '--ecrire' in argv
    pages = [a for a in argv if not a.startswith('--')]
    if not pages:
        print(__doc__)
        return 2
    total = 0
    for page in pages:
        source = pathlib.Path(page).read_text(encoding='utf-8')
        sortie, faits = melanger(page, source)
        total += len(faits)
        if faits:
            repartition = ' · '.join('%s : %d' % ('ABCDEFGH'[k], faits.count(k)) for k in sorted(set(faits)))
            print('%s %s : %d groupe(s) mélangé(s) — place de l\'ancienne tête de liste : %s'
                  % ('✎' if ecrire else '·', page, len(faits), repartition))
            if ecrire:
                pathlib.Path(page).write_text(sortie, encoding='utf-8')
    print('%d page(s) lues, %d groupe(s) %s' % (len(pages), total, 'mélangés' if ecrire else 'à mélanger'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
