# -*- coding: utf-8 -*-
"""tests_controle_marqueurs.py — le banc de la pointe de flèche mesurée en « traits ».

Rejoue le cas réel (un marqueur sans markerUnits : 8 × un trait de 12 = une pointe de 96 px sur un tracé de
80 px), les cas qui doivent passer, la panne d'une racine vide (règle d'or n°299) et le dépôt réel.

Usage : python3 _outils/tests_controle_marqueurs.py
"""
import contextlib, io, os, pathlib, shutil, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_marqueurs as C  # noqa: E402

BON = ('<marker id="f" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="52.8" markerHeight="52.8" '
       'orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8 z"/></marker>')
MAUVAIS = '<marker id="fj" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z"/></marker>'


def svg(marqueur):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 50"><defs>%s</defs></svg>\n' % marqueur


def jouer(racine, toleres=None):
    """stdout ET stderr : la panne de la règle n°299 part sur stderr."""
    ancien = C.DEPOT; C.DEPOT = str(racine); s = io.StringIO(); e = io.StringIO()
    try:
        with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
            code = C.main(toleres=toleres)
    finally:
        C.DEPOT = ancien
    return code, s.getvalue() + e.getvalue()


def lancer(script, cwd=None):
    """Le contrôle lancé comme on le lance vraiment : `python <script>` (règle d'or n°299)."""
    r = subprocess.run([sys.executable, script], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=300, cwd=cwd)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    echecs, n = [], 0

    def cas(titre, fichiers, doit_refuser, attendu="", toleres=None):
        nonlocal n; n += 1
        with tempfile.TemporaryDirectory() as tmp:
            for nom, contenu in fichiers.items():
                p = pathlib.Path(tmp, nom); p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(contenu, encoding="utf-8")
            code, texte = jouer(tmp, toleres if toleres is not None else {})
        if doit_refuser and code != 1: echecs.append("%s : sortie %d au lieu de 1\n     %s" % (titre, code, texte.strip()))
        elif not doit_refuser and code != 0: echecs.append("%s : refusé\n     %s" % (titre, texte.strip()))
        elif attendu and attendu not in texte: echecs.append("%s : message sans « %s »" % (titre, attendu))

    cas("le cas du 05/10 : marker sans markerUnits (8 × trait 12 = 96 px)", {"a.svg": svg(MAUVAIS)}, True, "markerUnits absent")
    cas("marker en pixels, avec viewBox : accepté", {"a.svg": svg(BON)}, False)
    cas("markerUnits=\"strokeWidth\" écrit en toutes lettres : refusé aussi",
        {"a.svg": svg(BON.replace("userSpaceOnUse", "strokeWidth"))}, True, "= « strokeWidth »")
    cas("userSpaceOnUse sans markerWidth/markerHeight : la pointe vaudrait 3 px",
        {"a.svg": svg('<marker id="g" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0"/></marker>')},
        True, "vaut 3 px")
    cas("balise écrite sur plusieurs lignes : lue quand même",
        {"a.svg": svg('<marker id="h"\n   markerWidth="8"\n   markerHeight="8"\n   orient="auto">\n<path d="M0 0"/></marker>')},
        True, "ligne 1")
    cas("marqueur fabriqué par une page HTML (SVG en chaîne JavaScript)",
        {"qcm.html": "<script>const s=`<svg><defs>%s</defs></svg>`;</script>" % MAUVAIS}, True)
    cas("marqueur fabriqué par un générateur Python",
        {"gen/gantt.py": 'SVG = """<defs>%s</defs>"""\n' % MAUVAIS}, True)
    cas("le dossier d'archives n'est pas jugé",
        {"_archive-anciennes-versions/vieux.svg": svg(MAUVAIS), "ok.svg": svg(BON)}, False)
    cas("un SVG sans marqueur n'est pas jugé", {"a.svg": '<svg xmlns="http://www.w3.org/2000/svg"/>'}, False)
    cas("deux marqueurs, un seul mauvais : le fichier est refusé et la ligne dite",
        {"a.svg": svg(BON) + "\n" + svg(MAUVAIS)}, True, "ligne 3")
    cas("le même fichier, toléré nommément, passe et le dit",
        {"a.svg": svg(MAUVAIS)}, False, "TOLÉRÉS nommément", toleres={"a.svg": "raison écrite"})
    cas("une tolérance dont le fichier est devenu conforme est annoncée périmée, sans refus",
        {"a.svg": svg(BON)}, False, "périmée", toleres={"a.svg": "raison écrite"})

    # Règle d'or n°299 — une racine sans fichier lisible n'est pas « aucun écart », c'est une panne.
    n += 1
    with tempfile.TemporaryDirectory() as tmp:
        pathlib.Path(tmp, "notes.md").write_text("# rien à lire", encoding="utf-8")
        code, texte = jouer(tmp, {})
    if code != 2: echecs.append("une racine sans fichier lisible : sortie %d au lieu de 2" % code)
    elif "EN PANNE" not in texte: echecs.append("une racine sans fichier lisible : la panne n'est pas annoncée")

    # … et au vrai point d'entrée : le script recopié dans une racine vide sort à 2, pas à 0.
    n += 1
    ici = os.path.dirname(os.path.abspath(__file__))
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "_outils"))
        for f in ("controle_marqueurs.py", "panne.py"):
            shutil.copy(os.path.join(ici, f), os.path.join(tmp, "_outils", f))
        code, texte = lancer(os.path.join(tmp, "_outils", "controle_marqueurs.py"))
    if code != 2: echecs.append("lancé en ligne de commande sur une racine vide, le contrôle sort à %d (attendu 2) :\n     %s" % (code, texte.strip()[:300]))

    # Le dépôt réel, par le point d'entrée, avec des chiffres à l'écran (un script muet ne prouve rien).
    n += 1
    code, texte = lancer(os.path.join(ici, "controle_marqueurs.py"))
    if code != 0: echecs.append("le dépôt réel ne passe pas (code %d) :\n     %s" % (code, texte.strip()[:600]))
    elif not any(c.isdigit() for c in texte): echecs.append("lancé en ligne de commande, le contrôle n'écrit AUCUN chiffre (règle d'or n°299)")

    if echecs:
        for e in echecs: print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n)); return 1
    print("✅ %d contrôles — la pointe de flèche mesurée en « traits » est refusée, partout où elle peut se cacher" % n)
    print("\n%d / %d" % (n, n)); return 0


if __name__ == "__main__":
    sys.exit(main())
