# -*- coding: utf-8 -*-
"""Banc de `controle_loupe.py` : des pages fabriquées pour chaque cas, puis le dépôt réel.

    python3 _outils/tests_controle_loupe.py
"""
import pathlib
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
OUTIL = ICI / "controle_loupe.py"
SIGNE = "var fond, grande, legende, dernier = null;"
V2 = "<!-- loupe-images-v2 --><script>(function(){ %s function figer(){} })();</script>" % SIGNE
V1 = "<!-- loupe-images-v1 --><script>(function(){ %s })();</script>" % SIGNE
res = []


def t(nom, ok, detail=""):
    res.append(bool(ok))
    print(("✔" if ok else "✘"), nom, "" if ok else detail)


def lancer(fichiers):
    with tempfile.TemporaryDirectory() as d:
        for nom, contenu in fichiers.items():
            (pathlib.Path(d) / nom).write_text(contenu, encoding="utf-8")
        r = subprocess.run([sys.executable, str(OUTIL), d], capture_output=True, text=True, encoding="utf-8")
        return r.returncode, r.stdout


code, out = lancer({"a.html": "<html><body>%s</body></html>" % V2})
t("une page v2 : sortie 0", code == 0, out)
code, out = lancer({"a.html": "<html><body><p>sans image</p></body></html>"})
t("une page sans agrandisseur : sortie 0", code == 0, out)
code, out = lancer({"a.html": "<html><body>%s</body></html>" % V1})
t("une page v1 : sortie 1, nommée", code == 1 and "a.html" in out and "v1" in out, out)
code, out = lancer({"a.html": "<html><body><script>(function(){ %s function figer(){} })();</script></body></html>" % SIGNE})
t("un agrandisseur sans marqueur : sortie 1", code == 1 and "sans le marqueur" in out, out)
code, out = lancer({"a.html": "<html><body>%s%s</body></html>" % (V2, V2)})
t("deux agrandisseurs : sortie 1", code == 1 and "2 agrandisseurs" in out, out)
code, out = lancer({"g.tpl": "<html><body>%s</body></html>" % V1})
t("un gabarit .tpl en v1 : sortie 1", code == 1 and "g.tpl" in out, out)
code, out = lancer({"a.html": "<html><body><!-- loupe-images-v2 --><script>(function(){ %s })();</script></body></html>" % SIGNE})
t("un marqueur v2 posé sur un code v1 (pas de figer) : sortie 1", code == 1 and "recopie pas" in out, out)
with tempfile.TemporaryDirectory() as d:
    r = subprocess.run([sys.executable, str(OUTIL), d], capture_output=True, text=True, encoding="utf-8")
    t("racine vide : sortie 2 (n°299)", r.returncode == 2, r.stdout)
with tempfile.TemporaryDirectory() as d:
    a = pathlib.Path(d) / "_archive-anciennes-versions"; a.mkdir()
    (a / "vieux.html").write_text("<html><body>%s</body></html>" % V1, encoding="utf-8")
    (pathlib.Path(d) / "b.html").write_text("<html><body>%s</body></html>" % V2, encoding="utf-8")
    r = subprocess.run([sys.executable, str(OUTIL), d], capture_output=True, text=True, encoding="utf-8")
    t("les archives ne sont pas lues", r.returncode == 0, r.stdout)
r = subprocess.run([sys.executable, str(OUTIL), str(ICI.parent)], capture_output=True, text=True, encoding="utf-8")
t("le dépôt réel : sortie 0", r.returncode == 0, r.stdout[-600:])

print("\n%d / %d" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
