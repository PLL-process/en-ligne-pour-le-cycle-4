# -*- coding: utf-8 -*-
"""tests_controle_hierarchie.py — le banc de la règle d'or n°307 (la hiérarchie se voit).

Chaque cas pose une page d'essai dans une racine vide, joue le contrôle, et vérifie
qu'il refuse ce qu'il doit refuser — et SURTOUT qu'il laisse passer ce qui est déjà
hiérarchisé : un contrôle qui refuse le juste finit désactivé.

Usage : python3 _outils/tests_controle_hierarchie.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_hierarchie as C  # noqa: E402
from tests_controle_cadres import reproches_de_la_ligne_de_commande  # noqa: E402

SEQ = "theme-2-essai/C4/4e/sequence_4e_essai.html"
TP = "theme-3-essai/C7/atelier-cao/tp_5e_essai.html"


def page(corps):
    return "<!doctype html><html lang='fr'><body>%s</body></html>" % corps


def mots(n, mot="mot"):
    return " ".join([mot] * n)


def jouer(racine):
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main([str(racine)])
    finally:
        C.DEPOT = ancien
    return code, s.getvalue() + e.getvalue()


def main():
    echecs, n = [], 0

    def cas(titre, fichiers, attendu_code, attendu=""):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            for rel, contenu in fichiers.items():
                p = pathlib.Path(tmp, rel); p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp)
        if code != attendu_code:
            echecs.append("%s : sortie %d au lieu de %d\n     %s" % (titre, code, attendu_code, texte.strip()[:500]))
        elif attendu and attendu not in texte:
            echecs.append("%s : message sans « %s »\n     %s" % (titre, attendu, texte.strip()[:500]))

    # — n°299 : ne rien voir n'est pas être vert
    cas("une racine sans page élève est une panne", {"notes.md": "# rien"}, 2, "EN PANNE")
    cas("un QCM seul n'est pas une page lue ici", {"theme-1-x/qcm_essai.html": page("<p>x</p>")}, 2, "EN PANNE")
    cas("une page propre passe", {SEQ: page("<h2>Titre</h2><p>Une phrase courte.</p>")}, 0, "1 page(s) lues")

    # — H1 énumération en ligne
    cas("H1 · un protocole numéroté écrit sur une ligne est refusé",
        {SEQ: page("<p><b>Protocole :</b> 1. brancher le shield ; 2. téléverser le programme ; 3. noter la valeur.</p>")},
        1, "H1 énumération en ligne")
    cas("H1 · le même protocole, une entrée par ligne, passe",
        {SEQ: page("<p><b>Protocole :</b><br>1. brancher le shield ;<br>2. téléverser le programme ;<br>3. noter la valeur.</p>")}, 0)
    cas("H1 · un saut de ligne du SOURCE n'est pas un saut de ligne à l'écran",
        {SEQ: page("<p>Trois choses.\n  <b>1.</b> la première chose\n  <b>2.</b> la deuxième chose\n  <b>3.</b> la troisième chose</p>")},
        1, "1. 2. 3.")
    cas("H1 · les cercles ①②③ en ligne sont refusés",
        {SEQ: page("<p>Auto-vérification : ① deux ovales · ② une commande · ③ des losanges étiquetés.</p>")}, 1, "①②③")
    cas("H1 · la chaîne fléchée « capteur (1) → carte (2) → écran (3) » se lit comme un schéma",
        {SEQ: page("<p>Ordre : capteur (1) → carte (2) → écran (3) → buzzer (4).</p>")}, 0)
    cas("H1 · « ② et ③ » forment une seule entrée",
        {SEQ: page("<p>① la première ligne.<br>② et ③ : à l'intérieur des branches.<br>④ tout en bas.</p>")}, 0)
    cas("H1 · « Pour a) » en tête de ligne commence bien sa ligne",
        {SEQ: page("<p>Pour a) : regarde le capteur.<br>Pour b) : compare les courants.<br>Pour c) : pense à l'entrée.</p>")}, 0)

    # — H2 mur sans repère
    trois = "".join("<p>%s.</p>" % mots(62) for _ in range(3))
    cas("H2 · trois paragraphes sans repère, 186 mots, sont refusés", {SEQ: page("<div>%s</div>" % trois)}, 1, "H2 mur sans repère")
    cas("H2 · un gras de tête sur un paragraphe coupe le mur",
        {SEQ: page("<div><p>%s.</p><p><b>Ensuite</b> %s.</p><p>%s.</p></div>" % (mots(62), mots(62), mots(62)))}, 0)
    cas("H2 · « La <b>borne inclinée</b> » : un gras dans les trois premiers mots est un repère",
        {SEQ: page("<div><p>%s.</p><p>La <b>borne inclinée</b> %s.</p><p>%s.</p></div>" % (mots(62), mots(62), mots(62)))}, 0)
    cas("H2 · un encadré typé (classe) coupe le mur",
        {SEQ: page("<div><p>%s.</p><p class='retenir'>%s.</p><p>%s.</p></div>" % (mots(62), mots(62), mots(62)))}, 0)
    cas("H2 · une question qui porte son champ est un repère",
        {SEQ: page("<div><p>%s <select><option>a</option></select></p><p>%s.</p><p>%s.</p></div>" % (mots(62), mots(62), mots(62)))}, 0)

    # — H3 paragraphe tout en gras
    cas("H3 · 45 mots tout en gras sont refusés", {SEQ: page("<p><b>%s</b></p>" % mots(45))}, 1, "H3 paragraphe tout en gras")
    cas("H3 · la phrase-clé de 30 mots en gras reste", {SEQ: page("<p><b>%s</b></p>" % mots(30))}, 0)

    # — H4 cellule-pavé
    cas("H4 · une cellule de 60 mots d'un bloc est refusée",
        {SEQ: page("<table><tr><td>%s</td></tr></table>" % mots(60))}, 1, "H4 cellule-pavé")
    cas("H4 · la même cellule coupée par <br> se juge à sa plus longue ligne",
        {SEQ: page("<table><tr><td>%s<br>%s</td></tr></table>" % (mots(30), mots(30)))}, 0)

    # — H5 item-pavé
    cas("H5 · un item de 65 mots sans gras de tête est refusé",
        {SEQ: page("<ul><li>%s</li></ul>" % mots(65))}, 1, "H5 item-pavé")
    cas("H5 · 65 mots qui s'ouvrent sur un gras passent",
        {SEQ: page("<ul><li><b>Nommer.</b> %s</li></ul>" % mots(65))}, 0)
    cas("H5 · 105 mots, même avec un gras de tête, sont refusés",
        {SEQ: page("<ul><li><b>Nommer.</b> %s</li></ul>" % mots(105))}, 1, "H5 item-pavé")
    cas("H5 · les sous-blocs typés d'une étape ne comptent pas dans sa tête",
        {TP: page("<ol><li>Ouvre Onshape.<span class='voir'>%s</span><div class='avertir'>%s</div></li></ol>" % (mots(50), mots(50)))}, 0)

    # — H6 pavé hors séquence
    cas("H6 · un paragraphe de 120 mots dans un TP est refusé", {TP: page("<p>%s</p>" % mots(120))}, 1, "H6 pavé hors séquence")
    cas("H6 · sur une séquence, c'est la n°33 de verif_regles_audit qui compte : pas deux fois",
        {SEQ: page("<p>%s</p>" % mots(120))}, 0)

    # — n°299, second corollaire : le point d'entrée réel, sur le vrai dépôt
    echecs.extend(reproches_de_la_ligne_de_commande("controle_hierarchie.py")); n += 1

    if echecs:
        print("✘ %d échec(s) sur %d cas :" % (len(echecs), n))
        for e in echecs:
            print("  - " + e)
        return 1
    print("✔ %d cas — controle_hierarchie refuse les blocs sans hiérarchie visible et laisse passer "
          "ceux qui en ont une" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
