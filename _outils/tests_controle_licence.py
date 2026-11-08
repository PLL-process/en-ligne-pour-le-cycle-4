# -*- coding: utf-8 -*-
"""tests_controle_licence.py — le banc du contrôle de licence (n°321).

Lance le contrôle EN SOUS-PROCESSUS, par sa ligne de commande (n°299, second corollaire),
sur un bac d'essai jetable : une page avec footer, une sans footer, une déjà conforme,
une archive à ignorer ; puis `--corriger` ; puis le LICENSE.md absent.

Usage : python3 _outils/tests_controle_licence.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "controle_licence.py")
sys.path.insert(0, ICI)
from licence_cc import MENTION, injecter, retirer, porte_mention  # noqa: E402

AVEC_FOOTER = "<html><body><main>x</main><footer><p>pied</p></footer></body></html>\n"
SANS_FOOTER = "<html><body><main>y</main></body></html>\n"
SANS_BODY = "<p>fragment</p>\n"
LICENCE = "# Licence\n\nCC BY-NC-SA 4.0\n"


def bac(fichiers):
    d = tempfile.mkdtemp(prefix="banc-licence-")
    for rel, contenu in fichiers.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8").write(contenu)
    return d


def lancer(d, *args):
    return subprocess.run([sys.executable, SCRIPT, "--racine", d, *args], capture_output=True, text=True)


echecs = 0


def verifier(nom, ok, detail=""):
    global echecs
    print(("✓ " if ok else "✘ ") + nom + ("" if ok or not detail else " — " + detail))
    if not ok:
        echecs += 1


# unité : l'injection
verifier("injecter pose la mention avant </footer>", injecter(AVEC_FOOTER).index(MENTION) < injecter(AVEC_FOOTER).index("</footer>"))
verifier("injecter pose la mention avant </body> faute de footer", injecter(SANS_FOOTER).index(MENTION) < injecter(SANS_FOOTER).index("</body>"))
verifier("injecter ajoute en fin de fichier faute de body", injecter(SANS_BODY).endswith(MENTION + "\n"))
verifier("injecter est idempotent", injecter(injecter(AVEC_FOOTER)) == injecter(AVEC_FOOTER))
verifier("retirer défait injecter", not porte_mention(retirer(injecter(AVEC_FOOTER))))

# 1. des pages nues → sortie 1, liste exacte, l'archive ignorée
d = bac({
    "LICENSE.md": LICENCE,
    "theme-1/a.html": AVEC_FOOTER,
    "theme-1/b.html": SANS_FOOTER,
    "theme-1/c.html": injecter(AVEC_FOOTER),
    "_archive-anciennes-versions/vieux.html": SANS_FOOTER,
})
r = lancer(d)
verifier("pages sans mention → sortie 1", r.returncode == 1, r.stdout)
verifier("les deux pages nues sont nommées, la conforme non", "theme-1/a.html" in r.stdout and "theme-1/b.html" in r.stdout and "c.html" not in r.stdout)
verifier("l'archive n'est pas comptée", "vieux.html" not in r.stdout)

# 2. --corriger répare puis sort à 0
r = lancer(d, "--corriger")
verifier("--corriger pose les mentions manquantes et sort à 0", r.returncode == 0 and "2 mention(s) posée(s)" in r.stdout, r.stdout)
verifier("la page sans footer a bien reçu la mention avant </body>", porte_mention(open(os.path.join(d, "theme-1/b.html"), encoding="utf-8").read()))
verifier("l'archive n'a pas été touchée", not porte_mention(open(os.path.join(d, "_archive-anciennes-versions/vieux.html"), encoding="utf-8").read()))
r = lancer(d)
verifier("un second passage reste vert", r.returncode == 0)
shutil.rmtree(d)

# 3. LICENSE.md absent ou muet
d = bac({"theme-1/c.html": injecter(AVEC_FOOTER)})
r = lancer(d)
verifier("LICENSE.md absent → sortie 1", r.returncode == 1 and "LICENSE.md" in r.stdout)
open(os.path.join(d, "LICENSE.md"), "w", encoding="utf-8").write("# Licence\n\nMIT\n")
r = lancer(d)
verifier("LICENSE.md qui ne nomme pas BY-NC-SA → sortie 1", r.returncode == 1)
shutil.rmtree(d)

# 4. README engendré sans mention
d = bac({"LICENSE.md": LICENCE, "README.md": "# Site\n", "theme-1/c.html": injecter(AVEC_FOOTER)})
r = lancer(d)
verifier("README sans mention → sortie 1, renvoyé vers make_index.py", r.returncode == 1 and "make_index.py" in r.stdout)
shutil.rmtree(d)

print("\nBanc vert." if not echecs else f"\n{echecs} échec(s)")
sys.exit(1 if echecs else 0)
