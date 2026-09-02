# -*- coding: utf-8 -*-
"""tests_controle_regle4.py — le banc des six erreurs.

`controle_regle4.py` s'est trompé **six fois** le 31/08/2026 avant de dire vrai :
cinq fois en accusant une page conforme, une fois en absolvant quatre pages qui
ne l'étaient pas. Chacune de ces six est un cas ci-dessous, écrit avec la forme
exacte qui l'avait piégé. Un banc qui ne rejouerait que les cas simples laisserait
le contrôle libre de retomber dans les six.

S'y ajoutent les cas de base — un bloc manquant est refusé, une page-pointeur et
une étape « Page N sur M » sont écartées — et le dépôt réel, qui doit passer.

Usage : python3 _outils/tests_controle_regle4.py
Sortie : 0 si tout passe, 1 sinon.
"""

import contextlib
import io
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import controle_regle4 as C  # noqa: E402


PRET = ('<section id="pret-a-s-entrainer"><h2>🧠 Prêt·e à t\'entraîner&nbsp;?</h2>'
        '<p><a class="btn" href="qcm_x.html">🚀 Ouvrir le QCM</a></p></section>')
BONUS = ('<section id="bonus"><h2>🎁 Bonus (facultatif — hors parcours obligatoire)</h2>'
         '<ol><li>un défi</li></ol></section>')

#: de quoi dépasser les 6 000 octets d'une page-pointeur, et donner à la page une
#: longueur réaliste : ce contrôle mesure des POSITIONS, en pourcentage.
CORPS = "<p>Le parcours de l'élève, séance après séance. </p>\n" * 220


def page(avant="", apres="", corps=CORPS, tete=""):
    return ("<!doctype html><html><head><meta charset=\"utf-8\">%s</head><body>"
            "<nav><a href=\"qcm_x.html\">QCM</a></nav>%s%s%s"
            "<footer>pied de page</footer></body></html>\n" % (tete, avant, corps, apres))


def ecrire(racine, chemin, contenu):
    p = pathlib.Path(racine) / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contenu, encoding="utf-8")
    return p


def jouer(racine, tolerees=None):
    anciens = (C.DEPOT, C.TOLEREES)
    C.DEPOT = str(racine)
    C.TOLEREES = tolerees if tolerees is not None else {}
    sortie = io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie):
            code = C.main()
    finally:
        C.DEPOT, C.TOLEREES = anciens
    return code, sortie.getvalue()


def main():
    echecs, controles = [], 0

    def cas(titre, contenu, doit_refuser, attendu="", nom="sequence_x.html", tolerees=None):
        """Une page seule dans un dépôt jetable, jugée."""
        nonlocal controles
        controles += 1
        with tempfile.TemporaryDirectory() as tmp:
            ecrire(tmp, nom, contenu)
            code, texte = jouer(tmp, tolerees)
        if doit_refuser and code == 0:
            echecs.append("%s : acceptée, alors qu'il fallait refuser\n     %s"
                          % (titre, texte.strip().replace("\n", "\n     ")))
        elif not doit_refuser and code != 0:
            echecs.append("%s : refusée\n     %s"
                          % (titre, texte.strip().replace("\n", "\n     ")))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s"
                          % (titre, attendu, texte.strip().replace("\n", "\n     ")))

    # ══ la forme juste ═══════════════════════════════════════════════════════
    cas("une page qui close sur les deux blocs, un seul bouton QCM à la fin",
        page(apres=PRET + BONUS), False)

    # ══ LES CINQ FOIS OÙ IL A ACCUSÉ UNE PAGE CONFORME ═══════════════════════

    # 1. l'apostrophe typographique de `5e_C1.3`
    cas("l'apostrophe typographique de « t’entraîner »",
        page(apres=PRET.replace("t'entraîner", "t’entraîner") + BONUS), False)

    # 2. le 🎁 du « palier récompense » des TP CAO : un 🎁 n'est pas le bloc
    cas("un 🎁 de palier récompense ne remplace pas le bloc Bonus",
        page(apres=PRET + '<section class="palier"><h2>🎁 Ton boîtier, dehors pour de bon</h2>'
                          '</section>'),
        True, "pas de bloc « Bonus »")

    # 3. l'aparté du professeur de `3e_C9.2`, annoncé dans un <summary>
    cas("un bloc Bonus annoncé dans un <summary> est un aparté, pas le bloc de l'élève",
        page(apres=PRET + '<details class="prof"><summary>🎁 Bonus (facultatif — hors parcours '
                          'obligatoire)</summary><p>note pour le professeur</p></details>'),
        True, "pas de bloc « Bonus »")
    cas("le vrai bloc et l'aparté du professeur dans la même page : le vrai compte",
        page(apres='<details class="prof"><summary>🎁 Bonus (facultatif — hors parcours '
                   'obligatoire)</summary><p>note</p></details>' + PRET + BONUS), False)

    # 4. la mention « Page N sur M » au-delà des 20 000 premiers octets
    #    (les quatre stations de `3e_C9.2` la portent à l'octet 20 826)
    loin = "<p>" + "x" * 21000 + "</p>"
    cas("une étape qui se déclare « Page 2 sur 4 » à l'octet 21 000 est écartée",
        page(avant=loin + "<p>Page 2 sur 4 — programmer</p>"),
        False, "étape d'une séquence en plusieurs pages")
    cas("la DERNIÈRE page d'une série est jugée, elle, et non écartée",
        page(avant=loin + "<p>Page 4 sur 4 — la recette</p>"),
        True, "pas de bloc")

    # 5. une balise entre « Bonus » et « (facultatif », comme dans `3e_C1.1`
    cas("« Bonus <span>(facultatif… » — le titre coupé par une balise",
        page(apres=PRET + '<section id="bonus"><h2>🎁 Bonus <span style="font-size:.8em">'
                          '(facultatif — hors parcours obligatoire)</span></h2>'
                          '<ol><li>un défi</li></ol></section>'), False)

    # ══ LA SIXIÈME : CELLE QUI ABSOLVAIT ═════════════════════════════════════
    # Les quatre TP CAO portaient un SECOND lien QCM, en texte courant, au
    # premier quart de la page. Sans `class="btn"`, il ne se voyait pas.
    cas("un second lien QCM en texte courant, au début, est un écart",
        page(avant='<p>Ce qui s\'évalue vient après : <a href="qcm_x.html">le QCM</a>.</p>',
             apres=PRET + BONUS),
        True, "avant la région finale")
    cas("deux liens QCM tous deux dans la région finale ne sont pas un écart",
        page(apres=PRET + '<p>Voir aussi <a href="qcm_x.html">le QCM</a>.</p>' + BONUS), False)
    cas("un renvoi interne vers #pret-a-s-entrainer n'est pas un lien vers le QCM",
        page(avant='<p>le QCM (<a href="#pret-a-s-entrainer">en bas de cette page</a>)</p>',
             apres=PRET + BONUS), False)

    # ══ LES CAS DE BASE ══════════════════════════════════════════════════════
    cas("un bloc « Prêt·e » absent est refusé", page(apres=BONUS),
        True, "pas de bloc « Prêt·e")
    cas("un QCM atteignable seulement par la barre de navigation est refusé",
        page(apres='<section id="pret-a-s-entrainer"><h2>🧠 Prêt·e à t\'entraîner ?</h2>'
                   '</section>' + BONUS),
        True, "aucun bouton QCM")
    cas("un bouton QCM au premier tiers de la page est refusé",
        page(avant='<p><a class="btn" href="qcm_x.html">QCM</a></p>',
             apres='<section id="pret-a-s-entrainer"><h2>🧠 Prêt·e à t\'entraîner ?</h2>'
                   '</section>' + BONUS),
        True, "pas à la fin")
    cas("une page-pointeur de moins de 6 Ko est écartée, non jugée",
        page(corps="<p>Ce TP a déménagé.</p>"), False, "page-pointeur")
    cas("une page nommée dans TOLEREES est écartée avec sa raison",
        page(), False, "tolérée par déclaration",
        tolerees={"sequence_x.html": "raison écrite, et ce qui la débloquera"})

    # ══ ce que le contrôle ne regarde pas ════════════════════════════════════
    cas("un QCM d'une autre page ne se juge pas ici (seuls sequence/tp/atelier)",
        page(), False, nom="qcm_x.html")

    # ══ le dépôt réel doit passer ════════════════════════════════════════════
    controles += 1
    code, texte = jouer(C.DEPOT, C.TOLEREES)
    if code != 0:
        echecs.append("le dépôt réel ne passe pas :\n     "
                      + texte.strip().replace("\n", "\n     "))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — les six erreurs du 31/08 sont rejouées, et aucune ne passe" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
