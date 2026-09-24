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

L'OUVERTURE ET LA GARDE (24/09/2026). Un mot `"seance": "ouverture"` doit
figurer avant la barre d'onglets — pas seulement dans une séance, pas dans la
<nav> ; il ouvre le lexique (`#ouverture`). Et le script n'écrase ni un lexique
sans sa signature, ni un lexique dont il effacerait un id ; il repose les ids
de IDS_POSES et saute les lots de EXCLUS en le disant.

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

from generer_lexique import (page_de_retour, ecrire_lexique, RefusVocabulaire,  # noqa: E402
                             LexiqueProtege, IDS_POSES, EXCLUS)

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

SEQUENCE = ('<html><body><nav>Accueil · un objet naturel</nav>'
            '<section class="card"><h2>Avant de commencer</h2><p>Un <b>objet technique</b>.</p></section>'
            '<div class="seance-tabs" role="tablist"><button>Séance 1</button></div>'
            '<a class="btn" href="qcm_x.html">QCM</a>'
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
    {"mot": "objet technique", "definition": "Un objet fabriqué par l'être humain.",
     "seance": "ouverture", "source": "programme 2024"},
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
        ([dict(NOMINAL[1], seance="ouverture")], "pluviomètre",
         "un mot d'ouverture qui ne figure que dans une séance"),
        ([dict(NOMINAL[3], mot="objet naturel", formes=["objet naturel"])], "objet naturel",
         "un mot d'ouverture qui ne figure que dans la <nav>"),
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
        for attendu in ('<section id="ouverture">', "🔄 Avant de commencer — les mots de base",
                        '<section id="seance-s1">', '<section id="seance-s2">',
                        "📚 Séance 1 — les mots de la séance", "📚 Séance 2 — les mots de la séance",
                        '<small class="source">Source : TLFi, « caduc »</small>',
                        "4 mots de l'ouverture et des séances, puis 1 notions", "vocabulaire_x.json",
                        # une adresse web dans une source ne doit pas élargir la page à 390 px
                        "overflow-wrap:anywhere"):
            if attendu not in page:
                echecs.append("cas nominal : %r absent de la page" % attendu)
        rangs = [page.find(t) for t in ('id="ouverture"', 'id="seance-s1"', 'id="seance-s2"', "<h2>C1.1")]
        if not -1 < rangs[0] < rangs[1] < rangs[2] < rangs[3]:
            echecs.append("cas nominal : ouverture puis séances ne viennent pas en tête, dans l'ordre")
    finally:
        shutil.rmtree(d.parent)
    return echecs, 1 + len(refus) + 1


def cas_garde():
    """Ce que le script n'écrase pas — et ce qu'il repose."""
    echecs = []
    # a. un lexique écrit à la main (sans signature) : refusé, fichier intact
    d = lot()
    try:
        (d / "lexique_x.html").write_text("<h1>Mon lexique</h1>", encoding="utf-8")
        try:
            ecrire_lexique(str(d), "x", "sequence_x.html")
            echecs.append("garde : un lexique écrit à la main a été écrasé")
        except LexiqueProtege as e:
            if e.exclu or "signature" not in str(e):
                echecs.append("garde : refus mal motivé : %s" % e)
        if (d / "lexique_x.html").read_text(encoding="utf-8") != "<h1>Mon lexique</h1>":
            echecs.append("garde : le fichier écrit à la main a changé")
    finally:
        shutil.rmtree(d.parent)
    # b. un lexique engendré qui porte un id posé à la main : refusé, l'id nommé
    d = lot()
    try:
        page = pathlib.Path(ecrire_lexique(str(d), "x", "sequence_x.html")[0]).read_text(encoding="utf-8")
        (d / "lexique_x.html").write_text(page.replace("<dt>Innovation", '<dt id="mon-ancre">Innovation'),
                                          encoding="utf-8")
        try:
            ecrire_lexique(str(d), "x", "sequence_x.html")
            echecs.append("garde : un id posé à la main a été effacé")
        except LexiqueProtege as e:
            if "mon-ancre" not in str(e):
                echecs.append("garde : refus qui ne nomme pas l'id : %s" % e)
        # c. le même, régénéré tel quel (signature, aucun id perdu) : accepté
        (d / "lexique_x.html").write_text(page, encoding="utf-8")
        ecrire_lexique(str(d), "x", "sequence_x.html")
    except LexiqueProtege as e:
        echecs.append("garde : un lexique engendré intact a été refusé : %s" % e)
    finally:
        shutil.rmtree(d.parent)
    # d. IDS_POSES : l'id vit dans le générateur, il est reposé
    d = pathlib.Path(tempfile.mkdtemp()) / "4e_C1.1"
    d.mkdir()
    try:
        (d / "sequence_x.html").write_text(SEQUENCE, encoding="utf-8")
        (d / "qcm_x.html").write_text('const QUESTIONS = [{c:"C1.2",n:"Justifier une évolution",ret:"r"}];',
                                      encoding="utf-8")
        page = pathlib.Path(ecrire_lexique(str(d), "4e_C1.1", "sequence_x.html")[0]).read_text(encoding="utf-8")
        if '<dt id="justifier-une-evolution">Justifier une évolution</dt>' not in page:
            echecs.append("IDS_POSES : l'id de 4e_C1.1 n'est pas reposé")
    finally:
        shutil.rmtree(d.parent)
    # e. EXCLUS : sauté, en le disant, sans toucher au fichier
    for code in ("3e_C8.1", "5e_C8.1"):
        d = pathlib.Path(tempfile.mkdtemp()) / code
        d.mkdir()
        try:
            (d / "sequence_x.html").write_text(SEQUENCE, encoding="utf-8")
            (d / "qcm_x.html").write_text(QCM, encoding="utf-8")
            try:
                ecrire_lexique(str(d), code, "sequence_x.html")
                echecs.append("EXCLUS : %s a été engendré" % code)
            except LexiqueProtege as e:
                if not e.exclu or "à la main" not in str(e):
                    echecs.append("EXCLUS : %s sauté sans sa raison : %s" % (code, e))
            if (d / ("lexique_%s.html" % code)).exists():
                echecs.append("EXCLUS : un fichier a été écrit pour %s" % code)
        finally:
            shutil.rmtree(d.parent)
    if set(IDS_POSES) != {"4e_C1.1", "4e_C1.4"} or set(EXCLUS) != {"3e_C8.1", "5e_C8.1"}:
        echecs.append("registres : IDS_POSES ou EXCLUS ont changé sans que ce banc le sache")
    return echecs, 7


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
    e_garde, n_garde = cas_garde()
    echecs += e_vocab + e_garde
    n = len(CAS) + n_vocab + n_garde
    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (n - len(echecs), n))
        return 1
    print("✅ %d contrôles — un lot dont la séquence est mutualisée reçoit son lexique, "
          "un dossier sans page de retour le dit, les mots de l'ouverture et des séances sont "
          "vérifiés avant d'entrer au lexique, et rien d'écrit à la main n'est écrasé" % n)
    print("\n%d / %d" % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
