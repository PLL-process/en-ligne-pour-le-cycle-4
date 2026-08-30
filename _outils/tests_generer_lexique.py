# -*- coding: utf-8 -*-
"""tests_generer_lexique.py — le lot dont la séquence vit ailleurs.

L'outil cherchait `sequence*.html` dans le dossier du lot pour savoir vers quelle
page ramener l'élève. Faute d'en trouver une, il **sautait le dossier en
silence** : aucun lexique écrit, et aucun message.

Trois lots du dépôt sont dans ce cas, et ce n'est pas un défaut de leur part :
ceux de l'atelier CAO tournent autour d'un **TP mutualisé** entre les trois
niveaux. Leur dossier porte la page de renvoi `tp_*.html`, pas de séquence.

Deux choses à garantir, donc : que le TP fasse office de page de retour, et
qu'un dossier sans aucune des deux le **dise** au lieu de se taire.

Usage : python3 _outils/tests_generer_lexique.py
Sortie : 0 si tout passe, 1 sinon.
"""
import os
import pathlib
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generer_lexique import page_de_retour  # noqa: E402

CAS = [
    (["sequence_5e_C8.1_patere.html", "qcm_5e_C8.1_patere.html"],
     "sequence_5e_C8.1_patere.html",
     "le cas ordinaire : le lot porte sa séquence"),
    (["tp_5e_de_onshape.html", "qcm_5e_C7.6_le-de.html"],
     "tp_5e_de_onshape.html",
     "le lot de l'atelier CAO : pas de séquence, un renvoi vers le TP mutualisé"),
    (["sequence_a.html", "tp_b.html"],
     "sequence_a.html",
     "quand les deux existent, la séquence l'emporte"),
    (["qcm_seul.html", "README.md"],
     "",
     "ni l'un ni l'autre : l'outil doit répondre « rien », pas deviner"),
]


def main():
    echecs = []
    for fichiers, attendu, pourquoi in CAS:
        d = pathlib.Path(tempfile.mkdtemp())
        try:
            for f in fichiers:
                (d / f).write_text("x", encoding="utf-8")
            obtenu = page_de_retour(str(d))
            if obtenu != attendu:
                echecs.append("%s → %r, attendu %r (%s)"
                              % (fichiers, obtenu, attendu, pourquoi))
        finally:
            shutil.rmtree(d)

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (len(CAS) - len(echecs), len(CAS)))
        return 1
    print("✅ %d contrôles — un lot dont la séquence est mutualisée reçoit son lexique, "
          "et un dossier sans page de retour le dit" % len(CAS))
    print("\n%d / %d" % (len(CAS), len(CAS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
