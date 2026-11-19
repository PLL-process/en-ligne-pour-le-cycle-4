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

Écrire un pourquoi (veille du 15/11/2026 — idée prise de `anthropics/k12-teacher-skills`, skill
`k12-check-for-understanding`, Apache 2.0, réécrite ici de zéro) : un leurre vient d'une erreur qu'un élève fait
vraiment (un prérequis qui manque, une confusion du niveau) ; son pourquoi dit ce qui ne va pas DANS CE CAS, puis
NOMME L'ÉTAPE SUIVANTE, à l'impératif — « Relis la ligne du capteur », « Compare au besoin : 100 exactement ». Un
pourquoi qui explique sans dire quoi faire laisse l'élève devant son erreur. `--etapes` mesure, sur toutes les
données `mission_*.json` du dépôt, les pourquoi qui ne nomment aucune étape (mesure, sortie 0) : le repérage est
mécanique (un verbe à l'impératif en tête d'une proposition, ou une forme en « -toi ») et se relit.

L'outil ne change ni les questions ni les réponses attendues ; il se rejoue sans rien changer. Le mode mission lit
ces attributs ; le banc générique refuse un « pourquoi » posé sur une bonne réponse.

Usage :
    python3 _outils/mode_mission/enrichir.py <sequence.html> <mission_<lot>.json>            # écrit
    python3 _outils/mode_mission/enrichir.py <sequence.html> <mission_<lot>.json> --verifier # dit si la page est à jour
    python3 _outils/mode_mission/enrichir.py --etapes [dossier]   # les pourquoi qui ne nomment pas l'étape suivante
    python3 _outils/mode_mission/enrichir.py --verifier-tout [racine]   # chaque mission_*.json et sa page sont à jour

`--verifier-tout` (19/11/2026) : après une passe qui change des propositions dans la page (changer_proposition.py),
une donnée restée sur l'ancien texte rendait la page « pas à jour » sans que rien ne le dise — trois séquences l'ont
été pendant une journée. La page d'un mission_*.json est la séquence de son dossier qui porte tous ses groupes. Sortie
1 si une page n'est pas à jour ou si aucune page ne porte les groupes d'un fichier, 2 si aucun fichier n'est lu.
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


# les impératifs d'une étape suivante (relevés le 15/11/2026 dans les 2 201 pourquoi du dépôt), plus toute forme « -toi »
IMPERATIFS = set("""lis relis observe regarde coche complète écris relie ouvre clique choisis indique note range place compare
vérifie teste calcule trace dessine repère associe glisse explique justifie propose cite nomme réponds utilise branche téléverse
enregistre retrouve souligne entoure classe mesure fais va prends mets lance copie colle remplis sélectionne déplace ajoute
modifie supprime rédige décris identifie cherche reprends compte pense essaie imagine suis remonte relève examine refais demande
pose garde retourne isole écoute touche additionne multiplie divise convertis applique attends reviens tape saisis vois relance
rejoue recompte retiens remets reporte situe localise""".split())
TETE = re.compile(r"(?:^|[:;.!?—]\s+|,\s+(?:puis|et|alors|donc)\s+|\(\s*)([A-Za-zÀ-ÿ]+(?:-toi|-le|-la|-les)?)\b")


def etape_suivante(texte):
    """le pourquoi nomme-t-il une étape suivante ? un impératif en tête d'une proposition, ou une forme en « -toi »"""
    for m in TETE.finditer(texte):
        mot = m.group(1).lower()
        if mot.endswith('-toi') or mot.split('-')[0] in IMPERATIFS:
            return True
    return False


def etapes(racine):
    """mesure : les pourquoi de chaque `mission_*.json` qui ne nomment aucune étape suivante"""
    fichiers = sorted(pathlib.Path(racine).rglob('mission_*.json'))
    fichiers = [f for f in fichiers if '_archive' not in str(f)]
    if not fichiers:
        print('✘ aucun fichier mission_*.json sous %s : rien n\'a été mesuré' % racine)
        return 2
    total, sans_etape = 0, 0
    lignes = []
    for f in fichiers:
        d = json.loads(f.read_text(encoding='utf-8'))
        textes = [t for r in d.get('pourquoi', {}).values() for t in r.values()]
        k = sum(1 for t in textes if not etape_suivante(t))
        total += len(textes)
        sans_etape += k
        if textes:
            exemple = next((t for t in textes if not etape_suivante(t)), '')
            lignes.append((k / len(textes), f, k, len(textes), exemple))
    for part, f, k, n, ex in sorted(lignes, key=lambda x: (-x[0], str(x[1]))):
        print('%3.0f %%  %3d / %3d  %s%s' % (100 * part, k, n, f.parent.name, ('  · « %s »' % ex[:70]) if ex else ''))
    print('⚠ étape suivante (mesure, hors score) : %d pourquoi sur %d ne nomment aucune étape suivante (%.0f %%), dans %d fichier(s)'
          % (sans_etape, total, 100 * sans_etape / max(total, 1), len(lignes)))
    return 0


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


def verifier_tout(racine):
    racine = pathlib.Path(racine)
    fichiers = sorted(f for f in racine.rglob('mission_*.json') if '_archive' not in str(f) and 'node_modules' not in str(f))
    refus = 0
    for fichier in fichiers:
        donnees = json.loads(fichier.read_text(encoding='utf-8'))
        groupes = list(donnees.get('pourquoi', {})) + list(donnees.get('indices', {})) + list(donnees.get('leurres', {}))
        pages = [p for p in sorted(fichier.parent.glob('sequence*.html'))
                 if all(re.search(GROUPE % re.escape(g), t, re.S) for t in [p.read_text(encoding='utf-8')] for g in groupes)]
        if not pages:
            print('✘ %s : aucune séquence du dossier ne porte ses %d groupes' % (fichier.relative_to(racine), len(groupes)))
            refus += 1
            continue
        for page in pages:
            try:
                a_jour = page.read_text(encoding='utf-8') == enrichir(str(page), donnees)
            except SystemExit as e:
                print('✘ %s : %s' % (page.relative_to(racine), e))
                refus += 1
                continue
            if not a_jour:
                print('✘ %s : pas à jour avec %s (relancer enrichir.py sur la page)' % (page.relative_to(racine), fichier.name))
                refus += 1
    if not fichiers:
        print('✘ aucun mission_*.json lu sous %s' % racine)
        return 2
    print('%s %d fichier(s) mission_*.json lus · %d refus' % ('✅' if not refus else '✘', len(fichiers), refus))
    return 1 if refus else 0


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    if '--verifier-tout' in argv:
        return verifier_tout(args[0] if args else pathlib.Path(__file__).resolve().parents[2])
    if '--etapes' in argv:
        return etapes(args[0] if args else pathlib.Path(__file__).resolve().parents[2])
    if len(args) != 2:
        print(__doc__)
        return 2
    page, fichier = args
    donnees = json.loads(pathlib.Path(fichier).read_text(encoding='utf-8'))
    avant = pathlib.Path(page).read_text(encoding='utf-8')
    apres = enrichir(page, donnees)
    n = (sum(len(v) for v in donnees.get('pourquoi', {}).values()), len(donnees.get('indices', {})),
         sum(len(v) for v in donnees.get('leurres', {}).values()))
    muets = sum(1 for r in donnees.get('pourquoi', {}).values() for t in r.values() if not etape_suivante(t))
    if muets:
        print('⚠ %d pourquoi sur %d ne nomment pas l\'étape suivante (--etapes : la mesure du dépôt)' % (muets, n[0]))
    if '--verifier' in argv:
        print(('✅ à jour' if avant == apres else '✘ la page n\'est pas à jour avec ses données') + ' — %d pourquoi, %d indices, %d leurres' % n)
        return 0 if avant == apres else 1
    if avant != apres:
        pathlib.Path(page).write_text(apres, encoding='utf-8')
    print('%s %s : %d pourquoi, %d indices, %d leurres' % ('✎' if avant != apres else '·', page, *n))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
