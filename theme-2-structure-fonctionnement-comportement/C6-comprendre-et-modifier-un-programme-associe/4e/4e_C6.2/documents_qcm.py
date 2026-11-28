# -*- coding: utf-8 -*-
"""Les documents des QCM de 4e_C6.2, lus dans les pages du lot (règles d'or n°233 et n°345, 28/11/2026).

    · « Le programme de l'arrosage » : LU dans la correction de l'activité 5 de la séquence (le Python complété) ;
    · « Le banc de tests de l'arrosage » : LU dans le tableau de l'activité 6 (test, humidité, seuil, attendu) —
      la colonne « Obtenu » n'y est pas : le document ne dit pas ce que fait le programme ;
    · « Le programme de l'éclairage » : le programme Arduino que la banque du QCM d'éclairage cite par morceaux
      (`pinMode(LED, OUTPUT);`, `int lumiere = analogRead(A0)`, `if (lumiere < seuil)`, `digitalWrite(LED, HIGH);`,
      « Seuil à 400 ») ; le script vérifie que chaque morceau est bien dans la banque.

    python3 documents_qcm.py             écrit documents_qcm_4e_C6.2.json
    python3 documents_qcm.py --verifier  sortie 0 s'il est à jour, 1 sinon
    puis : python3 ../../../../_outils/document_qcm.py documents_qcm_4e_C6.2.json
"""
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "documents_qcm_4e_C6.2.json")
SEQ = open(os.path.join(ICI, "sequence-jardin-connecte-arrosage-automatique.html"), encoding="utf-8").read()
ECL = open(os.path.join(ICI, "qcm_eclairage_automatique.html"), encoding="utf-8").read()
NB = " "

# 1. le programme complété de l'activité 5
_i = SEQ.index('<details class="correction"><summary>📖 Correction complète</summary><div>\n<pre class="code">seuil = 30')
_p = SEQ[SEQ.index("<pre", _i):SEQ.index("</pre>", _i)]
PROG = html.unescape(re.sub(r"<[^>]+>", "", _p)).split("\n")
assert PROG[0] == "seuil = 30" and "    if humidite < seuil:" in PROG and PROG[-1] == "    attendre(1)", PROG
PROG_L = [l.replace("    ", NB * 4).replace(" = ", NB + "=" + NB).replace(" < ", NB + "<" + NB) for l in PROG]

# 2. le banc de tests de l'activité 6
TESTS = []
for n in (1, 2, 3):
    m = re.search(r'<tr><td>(T%d — [^<]+)</td><td>(\d+)</td><td>(\d+)</td><td>([^<]+)</td><td id="bt%d">' % (n, n), SEQ)
    TESTS.append([html.unescape(g) for g in m.groups()])
ATTENDU = {"POMPE EN MARCHE": "en marche", "pompe à l'arrêt": "à l'arrêt"}
assert [t[1:3] for t in TESTS] == [["10", "30"], ["80", "30"], ["30", "30"]], TESTS

# 3. le programme de l'éclairage, tel que la banque le cite
for morceau in ("pinMode(LED, OUTPUT);", "if (lumiere &lt; seuil)", "digitalWrite(LED, HIGH);", "analogRead", "Seuil à 400",
                "A0", "LOW pour éteindre"):
    assert morceau in ECL, morceau
ECL_L = ["int seuil = 400;", "void setup() {", NB * 4 + "pinMode(LED, OUTPUT);", "}", "void loop() {",
         NB * 4 + "int lumiere = analogRead(A0);", NB * 4 + "if (lumiere < seuil) {", NB * 8 + "digitalWrite(LED, HIGH);",
         NB * 4 + "} else {", NB * 8 + "digitalWrite(LED, LOW);", NB * 4 + "}", "}"]
ECL_L = [l.replace(" = ", NB + "=" + NB).replace(" < ", NB + "<" + NB).replace(", ", "," + NB) for l in ECL_L]


def donnees():
    return {
        "qcm": ["qcm_4e_C6.2_arrosage_automatique.html", "qcm_eclairage_automatique.html"],
        "documents": {
            "doc_programme_arrosage": {
                "titre": "Le programme de l'arrosage",
                "sous_titre": "Le programme Python du jardin, complété. L'humidité du sol est lue en % (pour cent).",
                "desc": "Le programme Python de l'arrosage, ligne par ligne : " + " / ".join(l.strip() for l in PROG)
                        + ". Le document ne dit pas ce que fait la pompe pour une mesure donnée.",
                "blocs": [{"fiches": [{"titre": "Le programme, dans l'ordre", "lignes": PROG_L}]}],
                "note": "Les lignes décalées appartiennent à la ligne qui les précède · attendre(1) : "
                        "attendre une seconde.",
            },
            "doc_banc_tests_arrosage": {
                "titre": "Le banc de tests de l'arrosage",
                "sous_titre": "Trois tests du programme, l'humidité et le seuil en % (pour cent), et ce que le besoin attend.",
                "desc": "Le banc de tests de l'arrosage : " + " ; ".join(
                    "%s, humidité %s %%, seuil %s %%, attendu : %s" % tuple(t) for t in TESTS)
                        + ". Le document ne dit pas ce que le programme a obtenu.",
                "blocs": [{"tableau": {"colonnes": ["Test", "Humidité", "Seuil", "Pompe"],
                                       "lignes": [[t[0].replace(" — ", " ").replace("FRONTIÈRE", "frontière"),
                                                   t[1] + NB + "%", t[2] + NB + "%", ATTENDU[t[3]]] for t in TESTS],
                                       "largeurs": [116, 62, 52, 92]}}],
                "note": "La colonne « Pompe » dit ce que le besoin attend. Chaque test compare la pompe à cette attente.",
            },
            "doc_programme_eclairage": {
                "titre": "Le programme de l'éclairage",
                "sous_titre": "Le programme d'une carte de type Arduino : une LDR, la cellule sensible à la lumière, sur A0, et une LED.",
                "desc": "Le programme de l'éclairage automatique, ligne par ligne : " + " / ".join(l.replace(NB, " ").strip() for l in ECL_L)
                        + ". Le document ne dit pas ce que fait"
                          " chaque instruction.",
                "blocs": [{"fiches": [{"titre": "Le programme, dans l'ordre", "lignes": ECL_L}]}],
                "note": "analogRead rend un nombre de 0 à 1023 · HIGH : allumée · LOW : éteinte.",
            },
        },
    }


def texte():
    return json.dumps(donnees(), ensure_ascii=False, indent=2) + "\n"


if __name__ == "__main__":
    neuf = texte()
    if "--verifier" in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding="utf-8").read() == neuf
        print("✅ documents_qcm_4e_C6.2.json est à jour des pages du lot" if ok
              else "✘ documents_qcm_4e_C6.2.json n'est pas à jour : relancer sans --verifier")
        sys.exit(0 if ok else 1)
    open(SORTIE, "w", encoding="utf-8").write(neuf)
    print("écrit :", os.path.relpath(SORTIE, ICI))
