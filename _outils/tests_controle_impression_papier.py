# -*- coding: utf-8 -*-
"""Banc de `controle_impression_papier.py` : des pages fabriquées pour chaque cas, puis le dépôt réel.

    python3 _outils/tests_controle_impression_papier.py

Sortie 0 si tout passe, 1 sinon.
"""
import importlib.util
import pathlib
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
OUTIL = ICI / "controle_impression_papier.py"
_spec = importlib.util.spec_from_file_location("poser_papier", ICI / "impression_papier" / "poser.py")
poser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser)
res = []


def page(corps="<h1>Une séquence</h1>", tete=""):
    return "<html><head><title>t</title>%s</head><body>%s</body></html>" % (tete, corps)


def t(nom, ok, detail=""):
    res.append(bool(ok))
    print(("✔" if ok else "✘"), nom, "" if ok else "\n     " + str(detail).strip().replace("\n", "\n     "))


def lancer(fichiers, racine=None):
    with tempfile.TemporaryDirectory() as d:
        for nom, contenu in fichiers.items():
            f = pathlib.Path(d) / nom
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(contenu, encoding="utf-8")
        r = subprocess.run([sys.executable, str(OUTIL), racine or d], capture_output=True, text=True, encoding="utf-8")
        return r.returncode, r.stdout


bon = poser.poser(page())
code, out = lancer({"sequence_a.html": bon})
t("une séquence qui porte la fiche à jour : sortie 0", code == 0, out)
code, out = lancer({"sequence_a.html": page()})
t("une séquence sans la fiche : sortie 1, nommée", code == 1 and "sequence_a.html" in out and "sans la fiche papier" in out, out)
code, out = lancer({"sequence_a.html": bon, "index.html": page()})
t("une page qui n'est pas une séquence n'est pas obligée de la porter", code == 0, out)
code, out = lancer({"sequence_a.html": bon.replace("Rien ne change à l'écran", "Tout change à l'écran")})
t("une fiche modifiée dans la page : sortie 1", code == 1 and "différent de la source" in out, out)
code, out = lancer({"sequence_a.html": bon, "index.html": bon.replace("display:none}", "display:none }", 1)})
t("une copie périmée dans une autre page : sortie 1", code == 1 and "index.html" in out, out)
deux = bon.replace("</head>", poser.bloc() + "\n</head>")
code, out = lancer({"sequence_a.html": deux})
t("deux fiches dans la page : sortie 1", code == 1 and "2 blocs" in out, out)
try:
    poser.poser(deux); t("poser.py refuse une page à deux fiches", False)
except ValueError:
    t("poser.py refuse une page à deux fiches", True)
sans_tete = poser.poser("<html><title>t</title><body>sans balise de fin de tête</body></html>")
t("une page sans </head> (permis en HTML) reçoit la fiche juste avant </body>",
  sans_tete.index(poser.FIN) < sans_tete.index("</body>") and poser.poser(sans_tete) == sans_tete)
try:
    poser.poser("<html><body>ni l'un</body><body>ni l'autre</body></html>"); t("poser.py refuse une page sans place unique", False)
except ValueError:
    t("poser.py refuse une page sans place unique", True)
t("poser.py est idempotent", poser.poser(bon) == bon)
t("poser.py met à jour une fiche périmée, à la même place",
  poser.poser(bon.replace("Rien ne change à l'écran", "ancien")) == bon)
t("la fiche se pose juste avant </head>, et nulle part ailleurs",
  bon.index(poser.FIN) < bon.index("</head>") and bon.count(poser.DEBUT) == 1)
code, out = lancer({"_archive-anciennes-versions/sequence_vieille.html": page(), "sequence_a.html": bon})
t("les archives ne sont pas lues", code == 0, out)
code, out = lancer({"notes.txt": "rien"})
t("aucune séquence lue : sortie 2 (n°299), en le disant", code == 2 and "rien n'a été vérifié" in out, out)
r = subprocess.run([sys.executable, str(OUTIL), str(ICI.parent)], capture_output=True, text=True, encoding="utf-8")
t("le dépôt réel : chaque séquence porte la fiche à jour", r.returncode == 0, r.stdout[-1500:])

print("\n%d / %d" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
