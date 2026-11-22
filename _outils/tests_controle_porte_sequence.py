# -*- coding: utf-8 -*-
"""tests_controle_porte_sequence.py — banc de `controle_porte_sequence.py` (règle d'or n°366).

Un dossier de séquence fabriqué, cinq pages, une frontière chacune :
  atelier_a      reliée par la séquence                                  → a sa porte ;
  atelier_b      page-pointeur dont le bouton vise un atelier commun que la séquence relie → a sa porte ;
  deplacee       « Ressource déplacée » (renvoi)                         → n'en demande pas ;
  atelier_c      reliée par personne                                     → SANS porte ;
  atelier_d      page-pointeur dont l'atelier visé n'est relié par personne → SANS porte.
Plus : une page `qcm_*` non reliée n'est pas lue (hors porte), un dossier sans séquence n'est pas compté, et la
référence du dépôt est vide (depuis le 22/11/2026).
Sortie 0 si tout passe, 1 sinon.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_porte_sequence as c  # noqa: E402


def page(corps):
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>t</title></head><body>{corps}</body></html>'


def main():
    T = []
    with tempfile.TemporaryDirectory() as racine:
        seq = os.path.join(racine, "theme-9-essai", "C1-x", "5e", "5e_C1.1")
        commun = os.path.join(racine, "theme-9-essai", "ateliers-communs")
        sans = os.path.join(racine, "theme-9-essai", "C1-x", "5e", "5e_C1.2")
        for d in (seq, commun, sans):
            os.makedirs(d)
        ecrit = lambda d, n, h: open(os.path.join(d, n), "w", encoding="utf-8").write(h)
        ecrit(seq, "sequence_essai.html", page('<a href="atelier_a.html">A</a> <a href="../../../ateliers-communs/commun_b.html">B</a>'))
        ecrit(seq, "atelier_a.html", page("<h1>A</h1>"))
        ecrit(seq, "atelier_b.html", page('<a class="btn" href="../../../ateliers-communs/commun_b.html">Ouvrir</a>'))
        ecrit(seq, "deplacee.html", page("<h1>Ressource déplacée</h1>"))
        ecrit(seq, "atelier_c.html", page("<h1>C</h1>"))
        ecrit(seq, "atelier_d.html", page('<a href="x.html" class="btn grand">Ouvrir</a>'))
        ecrit(seq, "qcm_essai.html", page("<h1>QCM</h1>"))
        ecrit(commun, "commun_b.html", page("<h1>B commun</h1>"))
        ecrit(sans, "atelier_seul.html", page("<h1>sans séquence</h1>"))
        dossiers, sans_porte = c.mesurer(racine)
        noms = sorted(os.path.basename(p) for p in sans_porte)
        T.append(("un seul dossier de séquence compté (celui sans séquence ne l'est pas)", dossiers == 1, dossiers))
        T.append(("sans porte : exactement atelier_c et atelier_d", noms == ["atelier_c.html", "atelier_d.html"], noms))
        T.append(("la page reliée, la page-pointeur dont l'atelier est relié et le renvoi ont leur porte",
                  not {"atelier_a.html", "atelier_b.html", "deplacee.html"} & set(noms), noms))
        T.append(("une page qcm_* n'est pas lue", "qcm_essai.html" not in noms, noms))
    T.append(("la référence du dépôt ne garde que des pages qui existent",
              all(os.path.exists(os.path.join(c.RACINE, p)) for p in c.REFERENCE), sorted(c.REFERENCE)))
    T.append(("la référence du dépôt est vide depuis le 22/11/2026 (n°273 : elle ne peut que le rester)",
              not c.REFERENCE, sorted(c.REFERENCE)))
    for nom, ok, detail in T:
        print(("✅ " if ok else "❌ ") + nom + ("" if ok else f" — {detail}"))
    n = sum(1 for _, ok, _ in T if ok)
    print(f"{n} / {len(T)}")
    return 0 if n == len(T) else 1


if __name__ == "__main__":
    sys.exit(main())
