#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Banc de `enrichir.py` (22/11/2026) : relancer l'outil ne retire pas le balisage posé dans la légende d'une grille.

Pourquoi : la vague des infobulles du thème 3 (n°44) a posé des infobulles de sigles dans les légendes que
`enrichir.py` écrit (« elle imprime du PLA… »). L'outil réécrivait la légende en texte brut : `--verifier-tout`
refusait 3e_C7.5 et 4e_C7.7, et le relancer aurait effacé l'explication des sigles.

Ce que le banc joue, sur une page minimale écrite dans un dossier temporaire :
  1. un leurre ajouté à une grille : la légende et chaque ligne le portent, le titre le dit ;
  2. relancé sur sa propre sortie, l'outil ne change rien ;
  3. une infobulle posée après coup dans la légende : relancé, l'outil la garde, à l'octet près ;
  4. un leurre de plus sur cette page : il s'ajoute en texte brut, et l'infobulle reste.

Usage : python3 _outils/mode_mission/tests_enrichir.py — sortie 0 si tout passe, 1 sinon.
"""
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import enrichir as E  # noqa: E402

REPONSES = ["le PLA", "le bois"]


def ligne(gid, legende):
    options = "\n".join(
        '  <div class="qcm-option"><input type="radio" name="%s" id="%s__%d" value="%s" aria-label="%s — %s">'
        '<label for="%s__%d" title="%s">%s</label></div>' % (gid, gid, k + 1, t, E.LETTRES[k], t, gid, k + 1, t, E.LETTRES[k])
        for k, t in enumerate(REPONSES))
    return '<fieldset class="qcm-groupe qcm-grille" id="%s">\n  <legend>%s</legend>\n%s\n</fieldset>' % (gid, legende, options)


PAGE = ('<!doctype html><html lang="fr"><body>\n'
        '<div class="qcm-cles"><p class="qcm-cles-titre">Les matériaux&nbsp;:</p><ol>'
        + ''.join('<li><b>%s</b>%s</li>' % (E.LETTRES[k], t) for k, t in enumerate(REPONSES))
        + '</ol></div>\n' + ligne("g1", "La console") + '\n' + ligne("g2", "Le support") + '\n</body></html>\n')

ABBR = '<abbr class="sigle" title="acide polylactique, le plastique des imprimantes 3D" tabindex="0">PLA</abbr>'

ok = ko = 0


def t(nom, cond, detail=""):
    global ok, ko
    if cond:
        ok += 1
        print("  ✓", nom)
    else:
        ko += 1
        print("  ✘", nom, ("— " + detail) if detail else "")


with tempfile.TemporaryDirectory() as d:
    page = pathlib.Path(d) / "sequence_banc.html"
    page.write_text(PAGE, encoding="utf-8")

    # 1. un leurre ajouté
    un = E.enrichir(str(page), {"leurres": {"g1": ["l'acier"]}})
    legende = E.CLES.search(un)
    t("1. la légende porte le leurre", legende and "l'acier" in legende.group(2), un[:400])
    t("1. le titre dit qu'une réponse ne sert à aucune ligne", "une réponse ne sert à aucune ligne" in un)
    t("1. chaque ligne porte le leurre", un.count('value="l\'acier"') == 2)

    # 2. relancé sur sa sortie : rien ne change
    page.write_text(un, encoding="utf-8")
    t("2. relancé sur sa sortie, l'outil ne change rien", E.enrichir(str(page), {"leurres": {"g1": ["l'acier"]}}) == un)

    # 3. une infobulle posée après coup dans la légende (comme la vague des sigles) est gardée
    cles = E.CLES.search(un)
    avec = un[:cles.start(2)] + cles.group(2).replace("le PLA", "le " + ABBR, 1) + un[cles.end(2):]
    page.write_text(avec, encoding="utf-8")
    trois = E.enrichir(str(page), {"leurres": {"g1": ["l'acier"]}})
    t("3. relancé, l'outil garde l'infobulle de la légende", ABBR in trois)
    t("3. relancé, la page ne change pas d'un octet", trois == avec)

    # 4. un leurre de plus : ajouté en texte brut, l'infobulle reste
    quatre = E.enrichir(str(page), {"leurres": {"g1": ["l'acier", "le verre"]}})
    leg4 = E.CLES.search(quatre).group(2)
    t("4. le nouveau leurre est dans la légende, en texte brut", "</b>le verre</li>" in leg4, leg4)
    t("4. l'infobulle est toujours là", ABBR in leg4)
    t("4. chaque ligne porte le nouveau leurre", quatre.count('value="le verre"') == 2)

print("══ enrichir.py : %d / %d tests réussis ══" % (ok, ok + ko))
sys.exit(1 if ko else 0)
