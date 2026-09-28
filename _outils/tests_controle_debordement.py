# -*- coding: utf-8 -*-
"""tests_controle_debordement.py — le banc de la règle d'or n°135, second passage.

Chaque cas pose une page d'essai dans une racine vide, joue le contrôle, et vérifie
qu'il refuse un tableau large sans filet — et SURTOUT qu'il laisse passer tout ce qui
est déjà protégé, quel que soit le sélecteur exact utilisé : un contrôle qui refuse le
juste finit désactivé (même principe que tests_controle_hierarchie.py).

Usage : python3 _outils/tests_controle_debordement.py
"""
import contextlib, io, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_debordement as C  # noqa: E402
from tests_controle_cadres import reproches_de_la_ligne_de_commande  # noqa: E402

SEQ = "theme-2-essai/C4/4e/sequence_4e_essai.html"


def page(style, corps):
    return "<!doctype html><html lang='fr'><head><style>%s</style></head><body>%s</body></html>" % (style, corps)


def table(n_colonnes, classe=""):
    cls = ' class="%s"' % classe if classe else ""
    ligne = "<tr>" + "<td>x</td>" * n_colonnes + "</tr>"
    return "<table%s>%s</table>" % (cls, ligne)


FILET_GENERIQUE = "@media(max-width:680px){table{display:block;overflow-x:auto}}"
FILET_ORIGINAL = "@media(max-width:680px){section.card table{display:block;overflow-x:auto}}"
FILET_PAR_CLASSE = "@media(max-width:680px){.voc{display:block;overflow-x:auto}}"


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
    cas("une page sans tableau passe", {SEQ: page("", "<p>Une phrase.</p>")}, 0, "1 page(s) lues")

    # — le cœur du contrôle : tableau large, filet absent
    cas("un tableau de 3 colonnes sans filet est refusé",
        {SEQ: page("", table(3))}, 1, "tableau 3 colonnes")
    cas("un tableau de 4 colonnes sans filet est refusé",
        {SEQ: page("", table(4, "voc"))}, 1, "classe voc")
    cas("un tableau de 2 colonnes seulement passe, filet ou pas",
        {SEQ: page("", table(2))}, 0)

    # — couvert, quel que soit le sélecteur : c'est la page qui est protégée, pas la classe
    cas("filet générique table{} couvre un tableau sans classe",
        {SEQ: page(FILET_GENERIQUE, table(3))}, 0)
    cas("filet générique table{} couvre aussi un tableau .voc",
        {SEQ: page(FILET_GENERIQUE, table(4, "voc"))}, 0)
    cas("filet d'origine section.card table{} (n°135, 26/08) reste reconnu",
        {SEQ: page(FILET_ORIGINAL, '<section class="card">%s</section>' % table(3))}, 0)
    cas("filet posé par classe précise (.voc{}) suffit lui aussi",
        {SEQ: page(FILET_PAR_CLASSE, table(4, "voc"))}, 0)

    # — ce qui ne doit PAS compter comme un filet
    cas("overflow-x:auto hors de tout @media max-width ne protège rien sur mobile",
        {SEQ: page("table{overflow-x:auto}", table(3))}, 1, "tableau 3 colonnes")
    cas("un @media max-width sans overflow-x:auto ne protège rien",
        {SEQ: page("@media(max-width:680px){table{font-size:.9em}}", table(3))}, 1)

    # — deux tableaux en écart sur la même page : les deux sont comptés
    cas("deux tableaux larges sans filet sont comptés séparément",
        {SEQ: page("", table(3) + "<p>Entre deux.</p>" + table(4))}, 1, "2 tableau")

    # — n°299, second corollaire : le point d'entrée réel, sur le vrai dépôt
    echecs.extend(reproches_de_la_ligne_de_commande("controle_debordement.py")); n += 1

    if echecs:
        print("✘ %d échec(s) sur %d cas :" % (len(echecs), n))
        for e in echecs:
            print("  - " + e)
        return 1
    print("✔ %d cas — controle_debordement refuse les tableaux larges sans filet mobile et "
          "laisse passer ceux déjà protégés, quel que soit le sélecteur" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
