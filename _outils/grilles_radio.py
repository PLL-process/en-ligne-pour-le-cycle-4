#!/usr/bin/env python3
"""grilles_radio.py — des questions qui partagent leurs réponses se lisent en grille (08/11/2026).

Révision des trois thèmes (skill `revision-sequence`). La règle d'or n°300 change chaque question posée par une liste
déroulante en groupe de boutons radio : l'énoncé reste visible, le menu natif ne se dessine plus par-dessus. Mais
quand plusieurs questions de suite partagent les MÊMES réponses (« Associe chaque personne à ce qu'elle engage » :
cinq personnes, cinq réponses), la conversion écrit cinq fois les cinq réponses : 25 lignes à lire au lieu de 5.
Mesuré le 08/11/2026 : 427 listes sur 1 173 sont dans ce cas ; sur 5e_C1.5, l'activité 4 passait à 580 mots visibles.

L'outil range ces questions en grille, sans rien changer à ce que la page vérifie :
  · les réponses possibles s'écrivent UNE fois, au-dessus, lettrées A, B, C… ;
  · chaque question garde son énoncé et ses boutons radio, libellés par leur lettre, sur une rangée ;
  · chaque bouton garde sa valeur (le texte de la réponse : la vérification, la sauvegarde et les bancs n'y voient
    rien) et porte le texte entier en `aria-label` : un lecteur d'écran lit « A — il est l'auteur… ».
Une suite de groupes est rangée en grille quand ils sont au moins trois, à la suite (rien d'autre qu'un blanc entre
eux), avec au moins trois réponses identiques, dans le même ordre.

Usage : python3 _outils/grilles_radio.py <page.html>… [--ecrire]     (sans --ecrire : ce qui changerait)
Rejouable : une grille déjà posée n'est pas reposée.
"""
import html as H
import re
import sys

LETTRES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GROUPE = re.compile(r'<fieldset class="qcm-groupe"(?P<attrs>[^>]*)>(?P<corps>.*?)</fieldset>', re.S)
OPTION = re.compile(r'<div class="qcm-option"><input type="radio"(?P<ia>[^>]*)><label for="(?P<for>[^"]+)">(?P<lib>.*?)</label></div>',
                    re.S)
CSS = """<style id="css-qcm-grille">
/* grilles_radio.py (08/11/2026) : des questions qui partagent leurs réponses se lisent en grille — les réponses une
   fois, lettrées ; chaque question, une rangée de lettres. La valeur de chaque bouton est le texte de la réponse. */
.qcm-cles{margin:10px 0 6px;padding:8px 12px;border:1px solid var(--border,#274a8a);border-radius:10px;background:var(--panel2,#0a1b3d)}
.qcm-cles-titre{margin:0 0 4px;font-weight:600}
.qcm-cles ol{margin:0;padding-left:0;list-style:none}
.qcm-cles li{margin:3px 0;padding-left:1.9em;text-indent:-1.9em}
.qcm-cles li b{display:inline-block;width:1.6em;text-indent:0;color:var(--hl,#61dafb)}
.qcm-groupe.qcm-grille .qcm-option{display:inline-flex;align-items:center;gap:2px;margin:0;padding:3px 3px;width:auto;min-width:0}
.qcm-groupe.qcm-grille .qcm-option label{flex:none;font-weight:700}
.qcm-groupe.qcm-grille{display:flex;flex-wrap:wrap;align-items:center;column-gap:4px;row-gap:2px}
/* six lettres tiennent sur une rangée à 390 px, même au fond de trois cadres emboîtés (revue d'écran V2 4e, 10/11/2026 :
   la lettre F partait seule à la ligne sur 4e_C7.5) : bouton 17 px, lettre resserrée */
.qcm-groupe.qcm-grille .qcm-option input[type=radio]{width:17px;height:17px;margin:0}
.qcm-groupe.qcm-grille .qcm-option label{padding:0 1px;letter-spacing:0}
@media print{.qcm-cles{background:#fff!important;border-color:#999!important;color:#111!important}.qcm-cles li b{color:#111!important}}
</style>
"""


def valeurs(corps):
    return [m.group("ia") for m in OPTION.finditer(corps)]


def valeur(ia):
    m = re.search(r'\bvalue="([^"]*)"', ia)
    return H.unescape(m.group(1)) if m else None


def jeu(corps):
    return tuple(valeur(ia) for ia in valeurs(corps))


def griller(corps, lettres_de):
    def remplace(m):
        ia, lib = m.group("ia"), m.group("lib")
        v = valeur(ia)
        L = lettres_de[v]
        ia2 = ia + ' aria-label="%s"' % H.escape("%s — %s" % (L, v), quote=True)
        return '<div class="qcm-option"><input type="radio"%s><label for="%s" title="%s">%s</label></div>' % (
            ia2, m.group("for"), H.escape(v, quote=True), L)
    return OPTION.sub(remplace, corps)


def poser_css(s):
    """la feuille des grilles, à jour : posée si la page a une grille, remplacée si elle a changé"""
    if "qcm-grille" not in s.replace('id="css-qcm-grille"', ""):
        return s
    m = re.search(r'<style id="css-qcm-grille">.*?</style>\n?', s, re.S)
    if m:
        return s[:m.start()] + CSS + s[m.end():]
    k = s.lower().rfind("</head>")
    return s[:k] + CSS + s[k:]


def traiter(chemin, ecrire):
    s = open(chemin, encoding="utf-8").read()
    groupes = list(GROUPE.finditer(s))
    suites, i = [], 0
    while i < len(groupes):
        j = i
        while (j + 1 < len(groupes) and not s[groupes[j].end():groupes[j + 1].start()].strip()
               and jeu(groupes[j + 1].group("corps")) == jeu(groupes[i].group("corps"))):
            j += 1
        j_ = jeu(groupes[i].group("corps"))
        if j - i + 1 >= 3 and len(j_) >= 3 and None not in j_ and "qcm-grille" not in groupes[i].group(0):
            suites.append((i, j))
        i = j + 1
    if not suites:
        neuf = poser_css(s)
        if ecrire and neuf != s:
            open(chemin, "w", encoding="utf-8").write(neuf)
        return 0, 0
    sortie, pos = [], 0
    for i, j in suites:
        j_ = jeu(groupes[i].group("corps"))
        lettres_de = {v: LETTRES[k] for k, v in enumerate(j_)}
        cles = ('<div class="qcm-cles"><p class="qcm-cles-titre">Les réponses possibles — choisis une lettre pour '
                'chaque ligne&nbsp;:</p><ol>%s</ol></div>\n' %
                "".join("<li><b>%s</b>%s</li>" % (LETTRES[k], H.escape(v, quote=False)) for k, v in enumerate(j_)))
        sortie.append(s[pos:groupes[i].start()])
        sortie.append(cles)
        for g in groupes[i:j + 1]:
            a = g.group("attrs")
            sortie.append('<fieldset class="qcm-groupe qcm-grille"%s>%s</fieldset>' % (a, griller(g.group("corps"), lettres_de)))
            if g is not groupes[j]:
                sortie.append(s[g.end():groupes[groupes.index(g) + 1].start()])
        pos = groupes[j].end()
    sortie.append(s[pos:])
    neuf = poser_css("".join(sortie))
    if ecrire:
        open(chemin, "w", encoding="utf-8").write(neuf)
    return len(suites), sum(j - i + 1 for i, j in suites)


def main():
    args = sys.argv[1:]
    ecrire = "--ecrire" in args
    pages = [a for a in args if not a.startswith("--")]
    if not pages:
        print(__doc__)
        return 2
    tg = tq = 0
    for p in pages:
        g, q = traiter(p, ecrire)
        tg += g
        tq += q
        if g:
            print(("✎ " if ecrire else "· ") + p + " : %d grille(s), %d question(s)" % (g, q))
    print("%d page(s) lues, %d grille(s) %s (%d questions)" % (len(pages), tg, "posées" if ecrire else "à poser", tq))
    return 0


if __name__ == "__main__":
    sys.exit(main())
