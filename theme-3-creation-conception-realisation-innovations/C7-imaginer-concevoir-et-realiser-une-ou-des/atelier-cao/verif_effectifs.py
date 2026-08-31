#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verif_effectifs.py — un atelier qui grandit doit se recompter.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le 30 août 2026, l'atelier CAO est passé de **trois** TP à **quatre** : « Le dé, en
mieux » est né pour fermer le trou de `5e_C7.2`. Le lendemain, on a mesuré ce que
l'atelier disait encore de lui-même :

  · la fiche annonçait « les trois TP le disent en tête », « les trois QCM, les six
    synthèses et les trois lexiques », « les images des trois TP » ;
  · le manifeste déclarait « la règle n°77 refuse les trois TP » et « les trois TP
    l'annoncent en tête » ;
  · la synthèse professeur écrivait « les images des trois TP » ;
  · `GUIDAGE_PAS_A_PAS.md` titrait « Les trois TP prévus » et n'en listait que trois ;
  · le générateur d'audit, `_outils/build_audit.py`, portait la même phrase EN DUR, et
    la stampait dans `audit_couverture.json`.

**Six endroits.** Et le journal du 30 août disait, la veille : « la fiche disait encore
"les trois TP" — deux lignes remises d'aplomb ». Deux sur six. Corriger l'occurrence
qu'on a sous les yeux, c'est croire qu'il n'y en a qu'une (règle d'or n°261).

Le même jour, la même croissance avait laissé deux autres trous que personne ne
réclamait :

  · le quatrième TP **n'avait pas de relevé de captures** — cinq de ses huit paliers
    n'ont aucune image, et aucun document ne disait lesquelles prendre ;
  · le manifeste déclarait servir `4e_C7.2` sans donner l'adresse où ce code
    s'évalue — et la fiche, elle, la donnait fausse (une séquence au lieu du QCM).

CE QU'IL A LAISSÉ PASSER LE LENDEMAIN, ET CE QUE ÇA A CORRIGÉ
--------------------------------------------------------------
La première version de ce fichier a été livrée le 31/08/2026 et déclarée verte. Une
**septième** occurrence lui a échappé — « exception assumée […] écrite en tête des
trois TP », dans `5e/5e_C7.6/Synthèses/synthese_professeur_5e_C7.6.html` — pour deux
raisons indépendantes, dont chacune aurait suffi :

  · **elle allait à la ligne.** Le texte disait « des trois\\n  TP », et le contrôle
    lisait *ligne par ligne*. Deux recherches `grep` l'avaient manquée pour la même
    raison. Une phrase ne s'arrête pas en fin de ligne (règle d'or n°262) : le texte
    est désormais **aplati** avant lecture, et c'est la phrase, non la ligne, qui est
    citée dans le rapport ;
  · **elle vivait ailleurs.** Le périmètre était le dossier `atelier-cao/` ; la phrase
    était dans un dossier de lot voisin. Ce qui parle d'une ressource vit rarement
    dans son dossier (règle d'or n°263) : le contrôle lit maintenant, en plus, **tout
    fichier du sous-arbre C7 qui nomme Onshape ou l'atelier CAO** — critère déclaré,
    pas deviné. 37 voisins entrent ainsi dans le périmètre ; un seul portait un compte.

CE QUE CE CONTRÔLE FAIT
-----------------------
**1. Les listes déclarées doivent correspondre au dossier.** Le manifeste énumère les
pages élèves, les scénarios, les relevés de captures et les adresses d'évaluation. Ces
listes sont confrontées à ce qui existe : rien de deviné, tout de comparé.

**2. Un nombre écrit à côté du mot « TP » doit valoir le nombre de TP déclarés.** Dans
les pages et les documents de l'atelier, dans les fichiers voisins qui parlent de lui,
et dans les phrases du manifeste lui-même.

CE QU'IL NE VOIT PAS, ET LE DIT
-------------------------------
Il ne lit qu'un **vocabulaire fermé** — « TP » et « relevés de captures ». Tout autre
nom compté en toutes lettres lui échappe, et prétendre le contraire mentirait
(règle d'or n°242).

Il écarte, en le comptant :

  · ce qu'un navigateur ne suit pas — commentaires, `<script>`, `<style>`, blocs de
    code (la fonction `taire()` de `_outils/controle_liens.py`, règle n°253) ;
  · une phrase **datée** : « les seize rendus produits le 11 août 2026 » décrit un
    état passé, pas l'état d'aujourd'hui ;
  · une phrase **restreinte** à un niveau : « les deux TP de 5e » ne parle pas de
    l'atelier entier.

Et il ne connaît pas le nombre **un** : « un TP mené en classe » est un article, pas
un compte. Un atelier qui n'aurait qu'un seul TP échapperait donc à ce contrôle —
c'est le seul angle mort, il est déclaré, et il ne se produira pas.

Usage : python3 verif_effectifs.py
Sortie : 0 si l'atelier se compte juste, 1 sinon.
"""
import json
import pathlib
import re
import sys

A = pathlib.Path(__file__).resolve().parent
MANIFESTE = A / "manifest_cao.json"

# `taire()` vit dans `_outils/` : on la LIT là-bas plutôt que de la recopier ici.
# Une règle de silence recopiée se désynchronise de l'originale sans que personne
# ne le voie (c'est exactement l'erreur que ce fichier existe pour empêcher).
sys.path.insert(0, str(A.parents[2] / "_outils"))
from controle_liens import taire  # noqa: E402

#: les nombres que l'on sait lire. « un » en est absent : c'est un article.
NOMBRES = {"deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7,
           "huit": 8, "neuf": 9, "dix": 10, "onze": 11, "douze": 12}

#: le vocabulaire fermé : un nom compté, et d'où vient son effectif réel
FAMILLES = {
    "TP": "eleve",
    "relevés": "releves_de_captures",
}

_NB = r"(?:\d+|" + "|".join(NOMBRES) + r")"
MOTIFS = {nom: re.compile(r"\b(%s)\s+%s\b" % (_NB, re.escape(nom)), re.I)
          for nom in FAMILLES}

#: une phrase datée décrit un état passé
DATEE = re.compile(r"\b\d{1,2}[/ ](?:\d{1,2}/\d{2,4}|janvier|février|mars|avril|mai|juin"
                   r"|juillet|août|septembre|octobre|novembre|décembre)\b", re.I)

#: une phrase restreinte à un niveau ne parle pas de l'atelier entier
RESTREINTE = re.compile(r"\b(?:de|en|du)\s+(?:5e|4e|3e|niveau)\b", re.I)

#: fichiers de prose de l'atelier (le manifeste est traité à part, phrase par phrase)
PROSE = ("*.md", "*.html", "Synthèses/*.html")

#: Un fichier qui PARLE de l'atelier est tenu par les comptes de l'atelier, où
#: qu'il vive. Le 31/08/2026, la phrase fautive était dans la synthèse professeur
#: de `5e_C7.6` — un dossier voisin, hors de tout périmètre de dossier (n°263).
PARLE_DE_LATELIER = re.compile(r"onshape|atelier[ -]cao", re.I)


def effectifs(manifeste):
    """Les effectifs réels, lus dans le manifeste et non écrits ici."""
    return {nom: len(manifeste.get(cle) or []) for nom, cle in FAMILLES.items()}


def phrases_du_manifeste(manifeste):
    """Toutes les chaînes du manifeste, avec le chemin où on les a trouvées."""
    def descendre(noeud, chemin):
        if isinstance(noeud, str):
            yield chemin, noeud
        elif isinstance(noeud, dict):
            for c, v in noeud.items():
                yield from descendre(v, "%s.%s" % (chemin, c) if chemin else c)
        elif isinstance(noeud, list):
            for i, v in enumerate(noeud):
                yield from descendre(v, "%s[%d]" % (chemin, i))
    return descendre(manifeste, "")


#: la fin d'une phrase — c'est l'unité de lecture, pas la ligne (règle n°262)
FIN_DE_PHRASE = re.compile(r"(?<=[.!?;:])\s")


def phrase_autour(plat, debut, fin):
    """La phrase qui porte l'occurrence, dans le texte aplati."""
    gauche = max((m.end() for m in FIN_DE_PHRASE.finditer(plat, 0, debut)), default=0)
    m = FIN_DE_PHRASE.search(plat, fin)
    return plat[gauche:m.start() + 1 if m else min(len(plat), fin + 160)].strip()


def compter(texte, attendus, ou, ecarts, releve):
    """Confronte chaque nombre écrit à côté d'un nom du vocabulaire à son effectif.

    On lit le texte **aplati**, pas ligne par ligne. Une phrase ne s'arrête pas
    en fin de ligne : le 31/08/2026, « écrite en tête des trois\\n  TP » a
    traversé ce contrôle et deux recherches `grep` sans être vue (n°262).
    """
    plat = re.sub(r"\s+", " ", texte)
    for nom, motif in MOTIFS.items():
        for m in motif.finditer(plat):
            releve["lus"] += 1
            brut = m.group(1).lower()
            dit = int(brut) if brut.isdigit() else NOMBRES[brut]
            phrase = phrase_autour(plat, m.start(), m.end())
            if DATEE.search(phrase):
                releve["datees"] += 1
                continue
            if RESTREINTE.search(plat[m.end():m.end() + 24]):
                releve["restreintes"] += 1
                continue
            if dit != attendus[nom]:
                # On ne s'arrête PAS à la première : c'est tout le sujet. Le
                # 30 août, la même phrase était fausse à six endroits, et n'en
                # corriger qu'un a suffi à croire le travail fait (n°261).
                ecarts.append("%s : « %s » — l'atelier en compte %d\n        %s"
                              % (ou, m.group(0), attendus[nom], phrase[:120]))


def listes_declarees(manifeste, ecarts, racine=None):
    """Les listes du manifeste, confrontées à ce que le dossier contient."""
    racine = racine or A
    pages = manifeste.get("eleve") or []

    # les scénarios : ceux du disque, ceux déclarés
    sur_disque = sorted(p.name for p in (racine / "scenarios").glob("*.json"))
    declares = sorted(manifeste.get("chaine_de_production", {}).get("scenarios") or [])
    if sur_disque != declares:
        ecarts.append("scénarios : le disque en porte %s, le manifeste en déclare %s"
                      % (sur_disque, declares))

    # chaque scénario engendrable doit produire une page déclarée « élève »
    for s in (racine / "scenarios").glob("*.json"):
        sc = json.loads(s.read_text(encoding="utf-8"))
        sortie = sc.get("fichier_sortie", "")
        if "<" in str(sc.get("retour_sequence", "")):
            continue                      # le modèle : il ne s'engendre pas
        if sortie not in pages:
            ecarts.append("%s produit %s, absent de la liste « eleve » du manifeste"
                          % (s.name, sortie))

    # chaque page élève doit exister, et avoir SON relevé de captures
    par_tp = manifeste.get("releve_par_tp") or {}
    releves = manifeste.get("releves_de_captures") or []
    for page in pages:
        if not (racine / page).exists():
            ecarts.append("la page élève %s est déclarée et n'existe pas" % page)
        if page not in par_tp:
            ecarts.append("%s n'a pas de relevé de captures déclaré — un TP dont "
                          "personne ne réclame les images ne les recevra jamais" % page)
            continue
        releve = par_tp[page]
        if not (racine / releve).exists():
            ecarts.append("%s renvoie au relevé %s, qui n'existe pas" % (page, releve))
        elif releve not in releves:
            ecarts.append("le relevé %s existe et manque à « releves_de_captures »" % releve)
    for r in releves:
        if r not in par_tp.values():
            ecarts.append("le relevé %s n'est rattaché à aucun TP" % r)

    # chaque code déclaré servi doit dire OÙ il s'évalue, et l'adresse doit exister
    evaluation = manifeste.get("evaluation") or {}
    for code in manifeste.get("codes_servis") or []:
        adresse = evaluation.get(code)
        if not adresse:
            ecarts.append("%s est déclaré servi et le manifeste ne dit pas où il "
                          "s'évalue (règle n°250)" % code)
        elif not (racine / adresse).exists():
            ecarts.append("%s : l'adresse d'évaluation %s n'existe pas" % (code, adresse))


def main(racine=None):
    racine = racine or A
    manifeste = json.loads((racine / "manifest_cao.json").read_text(encoding="utf-8"))
    attendus = effectifs(manifeste)
    ecarts = []
    releve = dict(lus=0, datees=0, restreintes=0, fichiers=0, tues=0, voisins=0)

    listes_declarees(manifeste, ecarts, racine)

    def lire(chemin, ou):
        releve["fichiers"] += 1
        texte, tues = taire(chemin.read_text(encoding="utf-8", errors="replace"),
                            chemin.suffix)
        releve["tues"] += tues
        compter(texte, attendus, ou, ecarts, releve)
        return texte

    for motif in PROSE:
        for chemin in sorted(racine.glob(motif)):
            lire(chemin, chemin.name)

    # Les voisins qui parlent de l'atelier : ils en héritent les comptes (n°263).
    voisinage = racine.parent
    for chemin in sorted(voisinage.rglob("*")):
        if chemin.is_dir() or chemin.suffix not in (".md", ".html"):
            continue
        if racine in chemin.parents or chemin.parent == racine:
            continue                       # déjà lu au titre de l'atelier
        brut = chemin.read_text(encoding="utf-8", errors="replace")
        if not PARLE_DE_LATELIER.search(brut):
            continue
        releve["voisins"] += 1
        lire(chemin, str(chemin.relative_to(voisinage)))

    for chemin, phrase in phrases_du_manifeste(manifeste):
        compter(phrase, attendus, "manifest_cao.json → %s" % chemin, ecarts, releve)

    print("Effectifs déclarés : %s"
          % " · ".join("%d %s" % (n, nom) for nom, n in sorted(attendus.items())))
    print("%d fichier(s) de prose lus, dont %d voisins qui parlent de l'atelier · "
          "%d zone(s) tues avant lecture"
          % (releve["fichiers"], releve["voisins"], releve["tues"]))
    print("%d nombre(s) rencontrés à côté du vocabulaire (%d écartés comme datés, %d comme "
          "restreints à un niveau)"
          % (releve["lus"], releve["datees"], releve["restreintes"]))

    if ecarts:
        print("\n⛔ %d écart(s) — l'atelier ne se compte plus juste :" % len(ecarts))
        for e in ecarts:
            print("     " + e)
        print("\n     Un nombre écrit dans une prose partagée vieillit tout seul. S'il "
              "n'apporte\n     rien, on l'enlève ; s'il apporte quelque chose, on le "
              "corrige PARTOUT (n°261).")
        return 1
    print("✅ les listes du manifeste décrivent le dossier, et tout nombre écrit à côté "
          "du\n   vocabulaire lu dit le même effectif")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
