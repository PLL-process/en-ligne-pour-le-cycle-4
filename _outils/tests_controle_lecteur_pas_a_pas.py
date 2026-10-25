# -*- coding: utf-8 -*-
"""Banc de `controle_lecteur_pas_a_pas.py` : des pages fabriquées pour chaque cas, puis le dépôt réel.

    python3 _outils/tests_controle_lecteur_pas_a_pas.py
"""
import importlib.util
import pathlib
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
OUTIL = ICI / "controle_lecteur_pas_a_pas.py"
_spec = importlib.util.spec_from_file_location("poser_lpp", ICI / "lecteur_pas_a_pas" / "poser.py")
poser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poser)
res = []

ANIME = '<div id="essai-pas-a-pas" data-lpp-racine></div><script>LecteurPasAPas(document.getElementById("essai-pas-a-pas"), {scenes: []});</script>'


def page(corps, tete=""):
    return "<html><head>%s</head><body>%s</body></html>" % (tete, corps)


def t(nom, ok, detail=""):
    res.append(bool(ok))
    print(("✔" if ok else "✘"), nom, "" if ok else detail)


def lancer(fichiers):
    with tempfile.TemporaryDirectory() as d:
        for nom, contenu in fichiers.items():
            f = pathlib.Path(d) / nom
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(contenu, encoding="utf-8")
        r = subprocess.run([sys.executable, str(OUTIL), d], capture_output=True, text=True, encoding="utf-8")
        return r.returncode, r.stdout


bon = poser.poser(page(ANIME))
code, out = lancer({"a.html": bon})
t("une animation avec le lecteur à jour : sortie 0", code == 0, out)
code, out = lancer({"a.html": page("<p>rien d'animé</p>")})
t("une page sans animation : sortie 0", code == 0, out)
code, out = lancer({"a.html": page('<div id="vieux-pas-a-pas"></div><script>/* lecteur recopié */</script>')})
t("une animation sans le lecteur commun : sortie 1, nommée", code == 1 and "a.html" in out and "n'utilise pas" in out, out)
code, out = lancer({"a.html": page(ANIME)})
t("un appel sans le lecteur posé : sortie 1", code == 1 and "sans porter" in out, out)
code, out = lancer({"a.html": bon.replace("Rien ne démarre", "Tout démarre")})
t("un lecteur modifié dans la page : sortie 1", code == 1 and "différent de la source" in out, out)
deux = bon.replace("</head>", poser.bloc() + "\n</head>")
code, out = lancer({"a.html": deux})
t("deux lecteurs dans la page : sortie 1", code == 1 and "2 blocs" in out, out)
try:
    poser.poser(deux); t("poser.py refuse une page à deux lecteurs", False)
except ValueError:
    t("poser.py refuse une page à deux lecteurs", True)
t("poser.py est idempotent", poser.poser(bon) == bon)
with tempfile.TemporaryDirectory() as d:
    r = subprocess.run([sys.executable, str(OUTIL), d], capture_output=True, text=True, encoding="utf-8")
    t("racine vide : sortie 2 (n°299)", r.returncode == 2, r.stdout)
code, out = lancer({"_archive-anciennes-versions/v.html": page('<div id="vieux-pas-a-pas"></div>'), "b.html": bon})
t("les archives ne sont pas lues", code == 0, out)
r = subprocess.run([sys.executable, str(OUTIL), str(ICI.parent)], capture_output=True, text=True, encoding="utf-8")
t("le dépôt réel : sortie 0", r.returncode == 0, r.stdout[-600:])

print("\n%d / %d" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
