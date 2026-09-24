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

LES MOTS DES SÉANCES (23/09/2026). Un fichier `vocabulaire_<lot>.json` ouvre le
lexique sur une section par séance. Cinq cas : sans fichier, la page ne bouge
pas d'un octet ; un mot absent de sa séance, une entrée sans source, une
définition qui contredit le « à retenir » du QCM sont refusés, le mot nommé ;
le cas nominal pose les sections et leurs ancres `#seance-sN`.

Usage : python3 _outils/tests_generer_lexique.py
Sortie : 0 si tout passe, 1 sinon.
"""
import os
import pathlib
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json  # noqa: E402

from generer_lexique import page_de_retour, ecrire_lexique, RefusVocabulaire  # noqa: E402

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

SEQUENCE = ('<a class="btn" href="qcm_x.html">QCM</a>'
            '<section class="seance-panel" id="s1"><p>Une r&egrave;gle <b>CADUQUE</b>, une <i>Innovation</i>.</p>'
            '<script>var piege = "anémomètre";</script></section>'
            '<section class="seance-panel" id="s2"><p>Le pluviomètre mesure la pluie.</p></section>')
QCM = '''const QUESTIONS = [{c:"C1.1",n:"Innovation",ret:"Une nouveauté qui arrive jusqu'à ceux qui s'en servent."}];'''
NOMINAL = [
    {"mot": "caduc", "formes": ["caduc", "caduque"], "definition": "Qui ne vaut plus.",
     "seance": "s1", "source": "TLFi, « caduc »"},
    {"mot": "pluviomètre", "formes": ["pluviomètre"], "definition": "Appareil qui mesure la pluie.",
     "seance": "s2", "source": "Larousse en ligne"},
    {"mot": "Innovation", "formes": ["innovation"], "seance": "s1", "source": "Manuel d'Oslo 2018",
     "definition": "Une nouveauté qui arrive jusqu'à ceux qui s'en servent."},
]


def lot(vocab=None):
    """Un lot jetable : une séquence à deux séances, un QCM, et peut-être un vocabulaire."""
    d = pathlib.Path(tempfile.mkdtemp()) / "x"
    d.mkdir()
    (d / "sequence_x.html").write_text(SEQUENCE, encoding="utf-8")
    (d / "qcm_x.html").write_text(QCM, encoding="utf-8")
    if vocab is not None:
        (d / "vocabulaire_x.json").write_text(json.dumps(vocab, ensure_ascii=False), encoding="utf-8")
    return d


def cas_vocabulaire():
    echecs = []
    # 1. sans fichier : la page est celle d'avant, octet pour octet (le témoin est figé ici)
    d = lot()
    try:
        page = pathlib.Path(ecrire_lexique(str(d), "x", "sequence_x.html")[0]).read_text(encoding="utf-8")
        for attendu in ('<p class="sub">1 notions, tirées mot pour mot des QCM du lot · imprimable',
                        "  Chaque ligne provient d'une question de qcm_x.html. Rien n'a été réécrit ici :\n"
                        "  ce lexique rassemble ce que les corrections disaient déjà, une par une.\n</footer>",
                        "text-align:center}\n  @media print{\n",
                        "{color:#1a6af8}\n  }\n"):
            if attendu not in page:
                echecs.append("sans vocabulaire, la page a changé : %r manque" % attendu[:50])
        if "seance-s" in page or "source" in page:
            echecs.append("sans vocabulaire, la page parle de séances ou de sources")
    finally:
        shutil.rmtree(d.parent)
    # 2-4. les refus, le mot nommé
    refus = [
        ([dict(NOMINAL[1], seance="s1")], "pluviomètre", "un mot absent de sa séance"),
        ([{"mot": "anémomètre", "definition": "Mesure le vent.", "seance": "s1", "source": "TLFi"}],
         "anémomètre", "un mot qui n'est que dans un <script> du panneau"),
        ([dict(NOMINAL[0], source="")], "caduc", "une entrée sans source"),
        ([{k: v for k, v in NOMINAL[0].items() if k != "source"}], "caduc", "une entrée sans clé source"),
        ([dict(NOMINAL[2], definition="Une idée nouvelle.")], "Innovation",
         "une définition qui contredit le « à retenir » du QCM"),
    ]
    for vocab, mot, pourquoi in refus:
        d = lot(vocab)
        try:
            ecrire_lexique(str(d), "x", "sequence_x.html")
            echecs.append("non refusé : %s" % pourquoi)
        except RefusVocabulaire as e:
            if mot not in str(e):
                echecs.append("refus qui ne nomme pas « %s » (%s) : %s" % (mot, pourquoi, e))
            if (d / "lexique_x.html").exists():
                echecs.append("refusé, mais le lexique a été écrit quand même (%s)" % pourquoi)
        finally:
            shutil.rmtree(d.parent)
    # 5. le cas nominal
    d = lot(NOMINAL)
    try:
        page = pathlib.Path(ecrire_lexique(str(d), "x", "sequence_x.html")[0]).read_text(encoding="utf-8")
        for attendu in ('<section id="seance-s1">', '<section id="seance-s2">',
                        "📚 Séance 1 — les mots de la séance", "📚 Séance 2 — les mots de la séance",
                        '<small class="source">Source : TLFi, « caduc »</small>',
                        "3 mots des séances, puis 1 notions", "vocabulaire_x.json"):
            if attendu not in page:
                echecs.append("cas nominal : %r absent de la page" % attendu)
        rangs = [page.find(t) for t in ('id="seance-s1"', 'id="seance-s2"', "<h2>C1.1")]
        if not -1 < rangs[0] < rangs[1] < rangs[2]:
            echecs.append("cas nominal : les séances ne viennent pas en tête, dans l'ordre")
    finally:
        shutil.rmtree(d.parent)
    return echecs, 1 + len(refus) + 1


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

    e_vocab, n_vocab = cas_vocabulaire()
    echecs += e_vocab
    n = len(CAS) + n_vocab
    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n))
        return 1
    print("✅ %d contrôles — un lot dont la séquence est mutualisée reçoit son lexique, "
          "un dossier sans page de retour le dit, et les mots des séances sont vérifiés "
          "avant d'entrer au lexique" % n)
    print("\n%d / %d" % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
