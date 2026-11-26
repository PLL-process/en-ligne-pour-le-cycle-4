#!/usr/bin/env python3
"""replier_bonus.py — le Bonus se déplie quand on a fini (08/11/2026).

Révision des trois thèmes (skill `revision-sequence`) : la charge de lecture. Le Bonus est facultatif, hors parcours
obligatoire (n°301, n°311) : il ne sert qu'à l'élève qui a fini. Ouvert, il ajoute 150 à 250 mots à la séance de
clôture, déjà la plus chargée (synthèse, Bonus, bilan, positionnement, QCM).

L'outil garde le titre du Bonus visible, à sa place (la clôture se lit toujours Bonus → Bilan → QCM, n°311,
`controle_squelette.mjs`), et range tout ce qui le suit — la note, les défis, leurs champs, le corrigé — dans un
`<details>` fermé : « 🎁 Les 3 défis du Bonus — ouvre-les quand tu as fini ». Rien n'est retiré ni réécrit ; les
champs gardent leurs identifiants (la sauvegarde ne change pas).

Un Bonus est reconnu à son bloc `<section … id="bonus">` (ou `class="… bonus …"`), ou à toute `<section>` qui s'ouvre
sur un titre h2/h3 « Bonus ».
Un Bonus déjà replié n'est pas touché. Rejouable.

Usage : python3 _outils/replier_bonus.py <page.html>… [--ecrire]       (sans --ecrire : ce qui changerait)
        python3 _outils/replier_bonus.py --titres <page.html>… [--ecrire]   recompte les défis des Bonus déjà repliés
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from controle_bonus_corrige import bonus_etendue, lire as lire_bonus  # noqa: E402

OUVRE = re.compile(r'<section\b[^>]*(?:\bid="bonus"|class="[^"]*\bbonus\b[^"]*")[^>]*>', re.I)
TITRE = re.compile(r"<h([23])\b[^>]*>.*?</h\1>", re.S | re.I)
CSS = """<style id="css-bonus-replie">
/* replier_bonus.py (08/11/2026) : le Bonus se déplie quand on a fini */
details.bonus-replie>summary{cursor:pointer;font-weight:700;padding:6px 0;min-height:24px}
details.bonus-replie[open]>summary{margin-bottom:8px}
</style>
"""


def fin_section(s, debut):
    profondeur = 0
    for m in re.finditer(r"<(/?)section\b[^>]*>", s[debut:], re.I):
        profondeur += -1 if m.group(1) else 1
        if profondeur == 0:
            return debut + m.start()
    return -1


def trouver(s):
    """(début de la section, son titre) : le bloc `<section … id="bonus">`, ou toute `<section>` dont le premier
    élément est un titre h2/h3 qui dit « Bonus »"""
    m = OUVRE.search(s)
    if m:
        return m, TITRE.search(s, m.end(), fin_section(s, m.start()))
    for t in TITRE.finditer(s):
        if "bonus" not in re.sub(r"<[^>]+>", "", t.group(0)).lower():
            continue
        k = s.rfind("<section", 0, t.start())
        if k >= 0:
            m = re.compile(r"<section\b[^>]*>", re.I).match(s, k)
            if m and not s[m.end():t.start()].strip():
                return m, t
    return None, None


def compter(corps):
    """le nombre de défis du Bonus : ceux que la page NOMME (« Défi carte : », « 1. », « Citoyen : », ou les items
    d'une liste de défis), lus par `controle_bonus_corrige.lire` — la même lecture que le contrôle (B3).
    Jusqu'au 25/11/2026, l'outil comptait les items de la première liste, sinon les champs : il prenait les quatre
    phrases de la version étayée pour quatre défis, et un Bonus à un seul champ pour un seul défi (21 titres faux)."""
    return len(lire_bonus(corps)[0]) or 1


def resume(n):
    return ("🎁 Les %d défis du Bonus — ouvre-les quand tu as fini" % n) if n > 1 else "🎁 Le défi du Bonus — ouvre-le quand tu as fini"


TITRE_REPLIE = re.compile(r'(<details class="bonus-replie"><summary>)🎁 (?:Les \d+ défis du Bonus — ouvre-les quand tu as fini'
                          r'|Le défi du Bonus — ouvre-le quand tu as fini)(</summary>)')


def retitrer(chemin, ecrire):
    """un Bonus déjà replié dont le titre standard annonce un nombre faux reçoit le bon. Un titre écrit à la main
    (« Le défi du Bonus : faire retenir le bon geste ») n'est pas touché. Rend (ancien, nouveau) ou None."""
    s = open(chemin, encoding="utf-8").read()
    e = bonus_etendue(s)
    m = TITRE_REPLIE.search(s, e[0], e[1]) if e else None
    if not m:
        return None
    neuf = resume(compter(s[e[0]:e[1]]))
    ancien = s[m.end(1):m.start(2)]
    if neuf == ancien:
        return None
    if ecrire:
        open(chemin, "w", encoding="utf-8").write(s[:m.end(1)] + neuf + s[m.start(2):])
    return ancien, neuf


def traiter(chemin, ecrire):
    s = open(chemin, encoding="utf-8").read()
    m, t = trouver(s)
    if not m:
        return None
    fin = fin_section(s, m.start())
    if fin < 0 or not t or "bonus" not in re.sub(r"<[^>]+>", "", t.group(0)).lower():
        return None
    corps = s[t.end():fin]
    if 'class="bonus-replie"' in corps:
        return 0
    n = compter(corps)
    neuf = (s[:t.end()] + '\n<details class="bonus-replie"><summary>%s</summary>' % resume(n) + corps.rstrip()
            + "\n</details>\n" + s[fin:])
    if 'id="css-bonus-replie"' not in neuf:
        k = neuf.lower().rfind("</head>")
        neuf = neuf[:k] + CSS + neuf[k:]
    if ecrire:
        open(chemin, "w", encoding="utf-8").write(neuf)
    return n or 1


def main():
    args = sys.argv[1:]
    ecrire = "--ecrire" in args
    pages = [a for a in args if not a.startswith("--")]
    if not pages:
        print(__doc__)
        return 2
    faits = 0
    if "--titres" in args:
        for p in pages:
            r = retitrer(p, ecrire)
            if r:
                faits += 1
                print("%s %s : « %s » → « %s »" % ("✔" if ecrire else "·", p.split("/")[-1], r[0], r[1]))
        print("\n%d titre(s) %s" % (faits, "corrigé(s)" if ecrire else "à corriger (relancer avec --ecrire)"))
        return 0
    for p in pages:
        r = traiter(p, ecrire)
        if r is None:
            print("· %s : aucun bloc Bonus reconnu (section id=\"bonus\") — à replier à la main s'il existe" % p)
        elif r == 0:
            print("· %s : Bonus déjà replié" % p)
        else:
            faits += 1
            print(("✎ " if ecrire else "· ") + "%s : Bonus replié (%d défi(s))" % (p, r))
    print("%d page(s) lues, %d Bonus %s" % (len(pages), faits, "replié(s)" if ecrire else "à replier"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
