# -*- coding: utf-8 -*-
"""tests_controle_blocs_dessines.py — le banc de la règle d'or n°308.

Usage : python3 _outils/tests_controle_blocs_dessines.py
"""
import contextlib, io, json, os, pathlib, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_blocs_dessines as C  # noqa: E402
from tests_controle_cadres import par_la_ligne_de_commande, reproches_de_la_ligne_de_commande  # noqa: E402

PNG = (b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00"
       b"\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xa7\x9a\xa0\xa0"
       b"\x00\x00\x00\x00IEND\xaeB`\x82")
ALT = "Programme en blocs : affecter à x la valeur 14."
DECL = "| `Images/bloc_vitta_B01.png` | Capture d'écran réelle (règles n°94, n°308), Vittascience, 17/10/2026 |\n"


def jouer(racine, registre=None, **kw):
    """Le contrôle joué sur une racine d'essai — stdout ET stderr (règle n°299)."""
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main(registre={} if registre is None else registre, **kw)
    finally:
        C.DEPOT = ancien
    return code, s.getvalue() + e.getvalue()


def main():
    echecs, n = [], 0

    def cas(titre, fichiers, doit_refuser, attendu="", registre=None, **kw):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            for rel, contenu in fichiers.items():
                p = pathlib.Path(tmp, rel); p.parent.mkdir(parents=True, exist_ok=True)
                (p.write_bytes if isinstance(contenu, bytes) else
                 lambda c: p.write_text(c, encoding="utf-8"))(contenu)
            code, texte = jouer(tmp, registre, **kw)
        if doit_refuser and code != 1: echecs.append(titre + " : sort à %d, il fallait refuser\n     %s" % (code, texte.strip()[:300]))
        elif not doit_refuser and code != 0: echecs.append(titre + " : sort à %d\n     %s" % (code, texte.strip()[:300]))
        elif attendu and attendu not in texte: echecs.append(titre + " : message sans « %s »\n     %s" % (attendu, texte.strip()[:300]))

    page = lambda corps: "<!doctype html><html><body>%s</body></html>" % corps
    img = lambda nom="bloc_vitta_B01.png", alt=ALT, cl="bloc-capture": \
        '<img class="%s" src="Images/%s" width="300" height="80" alt="%s">' % (cl, nom, alt)

    # Règle n°299 : rien lu, c'est une panne.
    n += 1
    with tempfile.TemporaryDirectory() as tmp:
        pathlib.Path(tmp, "notes.md").write_text("rien", encoding="utf-8")
        code, texte = jouer(tmp)
    if code != 2 or "EN PANNE" not in texte: echecs.append("une racine sans page n'est pas en panne : %d" % code)

    # D1 — les dessins HTML
    cas("une page sans bloc passe", {"s.html": page("<p>Un algorigramme, du code : <code>x = 14</code></p>")}, False, "0 dessin(s) en attente")
    cas("un programme data-blocs hors registre est refusé",
        {"s.html": page('<div class="vb-prog" data-blocs="[[&quot;set&quot;,&quot;x&quot;,14]]"></div>')}, True, "1 dessin(s) de blocs hors registre")
    cas("un programme data-programme hors registre est refusé",
        {"s.html": page('<div class="prog" data-programme="arrosage"></div>')}, True, "règle n°308")
    cas("le schéma qui suit les curseurs (vb-prog sans data-blocs) est compté",
        {"s.html": page('<div id="waterBlocks" class="vb-prog vb-inline"></div>')}, True, "D1")
    cas("le schéma décoratif .programme-heros est compté",
        {"s.html": page('<div class="programme-heros" aria-label="x"></div>')}, True, "D1")
    cas("une règle CSS seule n'est pas un dessin",
        {"s.html": "<style>.vb-prog{color:red}.programme-heros::before{content:'vittascience'}</style>" + page("")}, False)
    cas("un dessin en commentaire ne compte pas",
        {"s.html": page('<!-- <div class="vb-prog" data-blocs="[]"></div> -->')}, False)
    cas("une classe « prog » seule (le code Arduino en texte des C7.5) n'est pas un dessin",
        {"s.html": page('<div class="prog">vent = analogRead(A0)</div>')}, False)

    # D2 — les SVG de blocs
    cas("une référence à un SVG de blocs hors registre est refusée",
        {"s.html": page('<img src="Images/blocs_palier1_lire_vent.svg" alt="x">')}, True, "D2")
    cas("chaque référence compte : <object> et chaîne de script",
        {"s.html": page('<object data="Images/programme_blocs_lampadaire.svg"></object><script>var q={img:"Images/programme_blocs_lampadaire.svg"}</script>')},
        False, "2 dessin(s) en attente", registre={"s.html": 2})
    cas("un algorigramme SVG n'est pas un dessin de blocs",
        {"s.html": page('<img src="Images/algorigramme_arrosage.svg" alt="x">')}, False)

    # Le registre
    cas("une page du registre au bon compte passe, en attente",
        {"s.html": page('<div class="vb-prog" data-blocs="[]"></div>' * 3)}, False, "3 dessin(s) en attente", registre={"s.html": 3})
    cas("un compte qui baisse sans mise à jour du registre est refusé (registre périmé)",
        {"s.html": page('<div class="vb-prog" data-blocs="[]"></div>')}, True, "EN_ATTENTE dit 3", registre={"s.html": 3})
    cas("une page remplacée qui reste au registre est refusée (registre périmé)",
        {"s.html": page("<p>captures</p>")}, True, "la page en porte 0", registre={"s.html": 1})
    cas("une page du registre disparue est refusée",
        {"t.html": page("")}, True, "n'existe plus", registre={"s.html": 1})

    # D3 — les captures
    cas("une capture bien faite et déclarée passe",
        {"d/s.html": page(img()), "d/Images/bloc_vitta_B01.png": PNG, "d/SOURCES_MEDIAS.md": DECL}, False, "0 dessin(s) en attente")
    cas("la déclaration d'un dossier parent vaut",
        {"d/e/s.html": page(img()), "d/e/Images/bloc_vitta_B01.png": PNG, "d/SOURCES_MEDIAS.md": DECL}, False)
    cas("une capture sans déclaration « Capture d'écran réelle » est refusée",
        {"s.html": page(img()), "Images/bloc_vitta_B01.png": PNG, "SOURCES_MEDIAS.md": "| bloc_vitta_B01.png | SVG original |\n"},
        True, "Capture d'écran réelle")
    cas("une capture de blocs mal nommée est refusée",
        {"s.html": page(img("programme.png")), "Images/programme.png": PNG, "SOURCES_MEDIAS.md": DECL}, True, "bloc_vitta_*.png")
    cas("une capture sans alt suffisant ou trop lourde est refusée",
        {"s.html": page(img(alt="blocs")), "Images/bloc_vitta_B01.png": PNG + b"\0" * (301 * 1024), "SOURCES_MEDIAS.md": DECL},
        True, "plus de 300 Ko")

    # --json, lisible et complet
    n += 1
    with tempfile.TemporaryDirectory() as tmp:
        pathlib.Path(tmp, "s.html").write_text(page('<div class="vb-prog" data-blocs="[]"></div>'), encoding="utf-8")
        code, texte = jouer(tmp, {"s.html": 1}, en_json=True)
    try:
        j = json.loads(texte)
        if code != 0 or j["dessins_en_attente"] != 1 or j["en_attente"]["s.html"]["compte"] != 1:
            echecs.append("--json : contenu inattendu : %s" % texte[:300])
    except ValueError:
        echecs.append("--json n'écrit pas du JSON : %s" % texte[:300])

    # Le dépôt réel : le registre doit coller à la page près.
    n += 1
    code, texte = jouer(C.DEPOT, C.EN_ATTENTE)
    if code != 0: echecs.append("le dépôt réel ne colle pas au registre :\n     " + texte.strip())

    # Le VRAI point d'entrée, en sous-processus (règle n°299).
    n += 1
    echecs.extend(reproches_de_la_ligne_de_commande("controle_blocs_dessines.py"))

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — un bloc ne se dessine pas, il se capture (règle n°308)" % n)
    print("\n%d / %d" % (n, n)); return 0


if __name__ == "__main__":
    sys.exit(main())
