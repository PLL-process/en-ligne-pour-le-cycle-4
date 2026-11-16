# -*- coding: utf-8 -*-
"""tests_registre_regles.py — banc de registre_regles.py.

Des journaux fabriqués, chacun avec UN cas connu : le doublon du 14/11/2026,
sa résolution par « renumérotée », le compte rendu rangé sous un numéro (qui
n'est pas un doublon), le tableau de tête, le prochain numéro libre.
Usage : python3 _outils/tests_registre_regles.py
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import registre_regles as R  # noqa: E402

TETE = ("# 📖 JOURNAL\n\n| N° | Titre | Rédacteur | Statut |\n|---|---|---|---|\n"
        "| 1 | Images v2 — SVG originaux | Fondatrices | ✅ |\n"
        "| 2 | En-tête QCM standard | Fondatrices | ✅ |\n\n"
        "Règle de réservation : tout nouveau numéro se prend ICI.\n\n")
DIX = ("## 10/11/2026 — Audit externe\n\n"
       "- **A05** — **règle d'or n°322 : une page qui garde les réponses sait les effacer** ; contrôle.\n")
QUATORZE = ("## 14/11/2026 — Règles d'or n°322 à n°330\n\n"
            "> **Règle d'or n°322 — Une réussite affichée prouve la production réelle.**\n")
COMPTE_RENDU = ("## 15/11/2026 — Révision\n\n"
                "- **n°322** — la page 4 garde ses réponses : bouton « Effacer » et note du poste partagé posés.\n")


def journal(texte):
    f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    f.write(texte)
    f.close()
    return f.name


def main():
    ok, ko = 0, []

    def t(titre, vrai, detail=""):
        nonlocal ok
        if vrai:
            ok += 1
        else:
            ko.append("%s — %s" % (titre, detail))

    j = journal(TETE + DIX + QUATORZE)
    d = R.lire(j)
    t("le doublon du 14/11 est vu", [n for n, _a, _b in R.doublons(d)] == [322], str(R.doublons(d)))
    t("la PREMIÈRE définition reste celle du 10/11", d[322][0][2] == "10/11/2026", str(d[322][0]))

    j = journal(TETE + DIX + QUATORZE.replace("réelle.**", "réelle.** *(renumérotée n°333 le 15/11/2026)*"))
    d = R.lire(j)
    t("« renumérotée n°333 » résout le doublon", R.doublons(d) == [], str(R.doublons(d)))
    t("la définition passe au n°333, sans la mention dans son titre",
      333 in d and "renumérotée" not in d[333][0][1] and "Une réussite" in d[333][0][1], str(d.get(333)))
    t("le prochain numéro libre suit le plus haut", R.prochain(d, j) == 334, str(R.prochain(d, j)))

    j = journal(TETE + DIX + COMPTE_RENDU)
    d = R.lire(j)
    t("FAUX COUPABLE — un compte rendu « - **n°322** — … » n'est pas un doublon", R.doublons(d) == [], str(R.doublons(d)))

    j = journal(TETE + "## 15/11/2026 — x\n\n> **Règle d'or n°2 — Le code se lit en couleurs, comme dans un IDE.**\n")
    d = R.lire(j)
    t("le tableau de tête compte : un n°2 introduit ailleurs sous un autre titre est un doublon",
      [n for n, _a, _b in R.doublons(d)] == [2], str(R.doublons(d)))
    t("les n°1 et n°2 prennent leur titre dans le tableau de tête",
      d[1][0][0] == "tableau" and d[1][0][1].startswith("Images v2"), str(d.get(1)))

    j = journal(TETE + "## 15/11/2026 — x\n\n### Règle d'or n°5\n\n> **Un test qui échoue accuse d'abord la page.**\n")
    t("un titre seul « ### Règle d'or n°5 » prend son énoncé à la ligne suivante",
      R.lire(j).get(5, [("", "")])[0][1].startswith("Un test qui échoue"), str(R.lire(j).get(5)))

    j = journal("# vide\n")
    ancien = R.JOURNAL
    R.JOURNAL = j
    try:
        code = R.main([])
    finally:
        R.JOURNAL = ancien
    t("aucune règle lue : EN PANNE (sortie 2, règle n°299), jamais vert", code == 2, str(code))

    for x in ko:
        print("✘", x)
    print("%d / %d" % (ok, ok + len(ko)))
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())
