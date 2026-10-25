# -*- coding: utf-8 -*-
"""tests_controle_sigles.py — le banc de la règle d'or n°313 : un sigle garde ses capitales.

Rejoue le cas qui a fait naître la règle (« Activité — Diagramme fast » sur l'index), les cas qui doivent
passer (le sigle en capitales, le mot anglais cité « fast », un nom de fichier, un identifiant de script, un
listing), les textes lus ailleurs que dans le corps (question de QCM, attribut title), la forme mixte
(« SysML »), un schéma SVG, la panne d'une racine vide (règle d'or n°299) et le dépôt réel.

Usage : python3 _outils/tests_controle_sigles.py
"""
import contextlib, io, os, pathlib, shutil, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_sigles as C  # noqa: E402

PAGE = '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>t</title></head><body>%s</body></html>\n'
ok = ko = 0


def verifier(nom, cond, detail=""):
    global ok, ko
    if cond:
        ok += 1
        print("✅", nom)
    else:
        ko += 1
        print("❌", nom, detail)


def jouer(corps):
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        p = racine / "theme-1-essai" / "atelier_a.html"
        p.parent.mkdir(parents=True)
        p.write_text(PAGE % corps, encoding="utf-8")
        ancien, C.DEPOT = C.DEPOT, str(racine)
        s = io.StringIO()
        try:
            with contextlib.redirect_stdout(s), contextlib.redirect_stderr(s):
                code = C.main([str(racine)])
        finally:
            C.DEPOT = ancien
        return code, s.getvalue()
    finally:
        shutil.rmtree(racine, ignore_errors=True)


code, out = jouer('<li><a href="atelier_diagramme_fast.html">Activité — Diagramme fast</a></li>')
verifier("le cas d'origine, « Diagramme fast », est refusé", code == 1 and "« fast » au lieu de « FAST »" in out, out)
code, out = jouer('<li><a href="atelier_diagramme_fast.html">Activité — Diagramme FAST</a></li>')
verifier("« Diagramme FAST » passe, et le nom de fichier n'est pas lu", code == 0, out)
code, out = jouer('<p>Le mot anglais « fast » veut dire rapide ; le Fast de l\'atelier, non.</p>')
verifier("le mot cité « fast » passe ; « Fast » hors guillemets est refusé",
         code == 1 and "« Fast »" in out and out.count("au lieu de") == 1, out)
code, out = jouer('<p>Ouvre qcm_fast.html ou fast/index.html.</p><pre>module = "fast"</pre><code>fast</code>'
                  '<script>const K = {"gps": 1}; localStorage.getItem("rep_fast_3e_e6");</script>')
verifier("noms de fichiers, chemins, listing et identifiants de script ne sont pas lus", code == 0, out)
code, out = jouer('<script>const QUESTIONS = [{q:"Que montre le diagramme fast ?",o:["a","b"],r:0}];</script>')
verifier("une question de QCM écrite « fast » est refusée", code == 1 and "(script)" in out, out)
code, out = jouer('<img src="x.svg" alt="Diagramme fast du lampadaire"><p>Un diagramme Sysml, un Qcm.</p>')
verifier("l'attribut alt, « Sysml » et « Qcm » sont refusés", code == 1 and "(alt)" in out and "« SysML »" in out
         and "« QCM »" in out, out)

d = tempfile.mkdtemp()
try:
    f = os.path.join(d, "fast_lampadaire.svg")
    open(f, "w", encoding="utf-8").write('<svg id="fast-1"><title>Diagramme fast</title><text>FAST</text></svg>')
    e = C.ecarts(f)
    verifier("un schéma SVG : son titre « Diagramme fast » est refusé, son id et son nom de fichier non",
             len(e) == 1 and e[0]["ecrit"] == "fast", e)
finally:
    shutil.rmtree(d, ignore_errors=True)

racine = tempfile.mkdtemp()
try:
    ancien, C.DEPOT = C.DEPOT, racine
    e = io.StringIO()
    with contextlib.redirect_stderr(e), contextlib.redirect_stdout(io.StringIO()):
        code = C.main([racine])
    C.DEPOT = ancien
    verifier("une racine vide sort en panne (2)", code == 2 and "PANNE" in e.getvalue(), e.getvalue())
finally:
    shutil.rmtree(racine, ignore_errors=True)

r = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "controle_sigles.py"), "--muet"],
                   capture_output=True, text=True, timeout=600)
verifier("le dépôt réel est lu (sortie 0 ou 1, jamais 2), index compris",
         r.returncode in (0, 1) and "page(s) lues" in r.stdout, r.stdout + r.stderr)

print("\n%d / %d" % (ok, ok + ko))
sys.exit(0 if ko == 0 else 1)
