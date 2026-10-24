# -*- coding: utf-8 -*-
"""tests_generer_bibliotheque_chaines.py — banc de generer_bibliotheque_chaines.py.

Le générateur est lancé comme on le lance vraiment, en sous-processus, et ses codes de sortie sont
lus (règle d'or n°299, second corollaire). Chaque défaut qu'il doit refuser est essayé pour de bon,
et le cas conforme doit passer : des cas dans les deux sens (règle d'or n°277).

Usage : python3 _outils/tests_generer_bibliotheque_chaines.py
Sortie : 0 si tous les cas passent, 1 sinon.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

OUTIL = Path(__file__).resolve().parent / "generer_bibliotheque_chaines.py"


def lancer(*args):
    r = subprocess.run([sys.executable, str(OUTIL), *args], capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout + r.stderr


def main():
    cas, rates = 0, []

    def attendre(nom, code_attendu, args, contient=None):
        nonlocal cas
        cas += 1
        code, sortie = lancer(*args)
        ok = code == code_attendu and (contient is None or contient in sortie)
        print(("✔" if ok else "✘"), nom, "— code", code, "(attendu %d)" % code_attendu)
        if not ok:
            rates.append(nom)
            print("   ", sortie.strip().replace("\n", "\n    ")[:600])

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        bonne = tmp / "bonne.xml"
        attendre("génère dans un fichier à part, sans toucher au dépôt", 0, ["--sortie", str(bonne)], "34 formes")
        texte = bonne.read_text(encoding="utf-8") if bonne.exists() else ""
        attendre("la bibliothèque générée se relit sans écart", 0, ["--verifier", str(bonne)], "0 écart")

        def variante(nom, ancien, nouveau, compte=1):
            f = tmp / nom
            f.write_text(texte.replace(ancien, nouveau, compte), encoding="utf-8")
            return str(f)

        attendre("refuse un texte HTML (html=1)", 1,
                 ["--verifier", variante("html1.xml", "html=0", "html=1")], "html=0 attendu")
        attendre("refuse un saut de ligne brut, que la lecture XML change en espace", 1,
                 ["--verifier", variante("saut.xml", "Énergie&amp;#10;électrique", "Énergie\\nélectrique", -1)],
                 "saut de ligne perdu")
        attendre("refuse un bloc hors du vocabulaire (AGIR)", 1,
                 ["--verifier", variante("agir.xml", 'value=\\"TRANSMETTRE\\"', 'value=\\"AGIR\\"')], "AGIR")
        attendre("refuse des pointillés sans fixDash=1", 1,
                 ["--verifier", variante("dash.xml", "fixDash=1;", "", -1)], "fixDash")
        attendre("en panne (2) sur un fichier absent", 2, ["--verifier", str(tmp / "absent.xml")], "aucune bibliothèque")
        vide = tmp / "vide.xml"
        vide.write_text("", encoding="utf-8")
        attendre("en panne (2) sur un fichier vide", 2, ["--verifier", str(vide)], "illisible")
        autre = tmp / "autre.xml"
        autre.write_text("<mxfile></mxfile>", encoding="utf-8")
        attendre("en panne (2) sur un XML qui n'est pas une bibliothèque", 2, ["--verifier", str(autre)])

    print("\n%d / %d" % (cas - len(rates), cas))
    return 1 if rates else 0


if __name__ == "__main__":
    sys.exit(main())
