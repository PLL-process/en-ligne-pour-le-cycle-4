# -*- coding: utf-8 -*-
"""controle_medias.py — d'où vient chaque image, et laquelle ne sert à personne.

LE CONSTAT QUI A DONNÉ CE CONTRÔLE
----------------------------------
Le 31/08/2026, le manifeste du lot « Programmer le lampadaire » annonçait deux
questions illustrées et deux images ; le lot en portait trois depuis le LOT 12.
En cherchant s'il y avait d'autres manifestes dans ce cas, la question s'est
déplacée.

Le champ `fichiers.images` d'un manifeste **n'est pas**, dans ce dépôt, un
inventaire exhaustif : douze lots sur trente-deux y nomment les originaux
notables, pas tout ce que le dossier contient. Lui imposer un sens qu'il n'a
jamais eu, ce serait inventer une règle plutôt qu'en mesurer une (règle d'or
n°248 — un contrôle qui signale du correct finit ignoré).

Ce qui compte vraiment, pour un dépôt scolaire publié, c'est **d'où vient chaque
image**. Mesure faite ce jour-là sur les **276 fichiers médias** du dépôt :

  · **0** image déclarée par un manifeste et absente du disque — sur
    **111 promesses** vérifiées ;
  · **11** médias posés dans un dossier ne portant **aucun** `SOURCES_MEDIAS.md` :
    leur licence n'était écrite nulle part. Neuf ont été payés par la PR #321,
    deux par celle qui livre ce fichier — le contrôle part donc de zéro ;
  · **88** médias sous un lot qui a bien un `SOURCES_MEDIAS.md`, mais que ce
    fichier ne nomme pas — dette comptée, pas refusée ;
  · **38** images présentes sur le disque qu'**aucune page n'affiche** et
    qu'aucun manifeste ne nomme. La recherche a aussi sorti de l'ombre
    `image_extraite_08.png` — un extrait de manuel scolaire dont les sept
    fichiers frères avaient été retirés pour ce motif, et qui avait été oublié
    (retiré par la PR #321) ;
  · **2** images inemployées mais **nommées** par leur manifeste, sous
    `herite_conserve` : gardées exprès, comptées à part.

Ces cinq nombres sont ceux du 31/08/2026 ; ils bougeront. Le relevé que le
contrôle imprime est la version à jour, celle-ci en est la date de naissance.

CE QU'IL REFUSE
---------------
**1. Un média dont la provenance n'est écrite nulle part** : un fichier image
dans un dossier qui ne porte aucun `SOURCES_MEDIAS.md`. On ne peut rien dire de
sa licence, et la règle images v2 du dépôt exige qu'on le puisse.

**2. Une image promise et absente** : un manifeste qui nomme dans
`fichiers.images` un fichier qui n'est pas sur le disque. C'est la forme
« promesse fausse » déjà refusée pour les scripts de test (règle n°259).

CE QU'IL COMPTE SANS REFUSER, ET POURQUOI
-----------------------------------------
**Les médias qu'un `SOURCES_MEDIAS.md` existant ne nomme pas.** Les payer tous
d'un coup demanderait d'écrire quatre-vingt-huit affirmations de licence en
une séance — et une licence écrite pour rendre un contrôle vert est pire que le
trou qu'elle bouche. La dette est donc nommée, lot par lot, pour être payée là
où quelqu'un sait ce qu'il écrit.

**Les images orphelines** — sur le disque, affichées par aucune page. Un fichier
inemployé est une dette, pas un mensonge : ou bien le schéma a perdu son emploi
et se retire, ou bien son câblage dans la séquence a été oublié et c'est une
image-objet qui manque à l'élève. Les deux se tranchent, ils ne se devinent pas.

**Les orphelines qu'un manifeste NOMME quand même**, comptées à part et non
mélangées aux précédentes. `5e_C1.2` range deux SVG sous `herite_conserve` :
quelqu'un a écrit qu'ils restaient. Une décision écrite n'est pas un oubli
(règle d'or n°271).

CE QU'IL NE FAIT PAS
--------------------
Il ne juge ni le poids, ni le format, ni la qualité d'une image, et ne vérifie
pas qu'une image citée par une page existe — c'est l'affaire de
`controle_liens.py`. Il ne lit pas non plus les nombres qu'un manifeste annonce
sur sa banque : `controle_effectifs_qcm.py` s'en charge, `questions_illustrees`
compris.

Un **nom de fichier nu** dans une phrase — « deux SVG originaux
(`schema_chaines_arrosage.svg`, …) » — n'est pas compté comme un emploi : c'est
une mention, pas un affichage, et rien ne dit laquelle des images d'un dépôt
porte ce nom. Seul le chemin tel qu'on l'écrirait pour l'afficher compte.

Usage :
    python3 _outils/controle_medias.py           # rapport complet
    python3 _outils/controle_medias.py --muet    # seulement les refus
Sortie : 0 si toute image a une provenance écrite et si rien n'est promis en
vain, 1 sinon.
"""

import collections
import json
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

#: les extensions d'image que ce dépôt emploie. Un outil qui reconnaît les
#: fichiers par leur extension doit connaître toutes celles du dépôt
#: (règle d'or n°269) : `.jpeg` et `.webp` y figurent même sans occurrence
#: aujourd'hui, parce que l'oubli ne se voit pas — il se traduit par un silence.
IMAGES = (".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif")

#: une page qui peut afficher une image. Les fiches et rapports en `.md` en
#: citent aussi : ce qui parle d'une ressource vit rarement dans son dossier
#: d'images (règle d'or n°263), et une image citée par la seule fiche
#: pédagogique n'est pas orpheline.
PORTEUSES = (".html", ".md", ".py", ".mjs", ".js")

#: LES DEUX DOCUMENTS QUI DÉCRIVENT SANS EMPLOYER. Un `SOURCES_MEDIAS.md` nomme
#: une image pour en dire la licence ; un manifeste la nomme pour l'inventorier.
#: Ni l'un ni l'autre ne l'affiche. Les compter comme un emploi rendrait toute
#: image invisible dès qu'on la documente — c'est-à-dire exactement au moment où
#: on s'en occupe. Ce piège s'est refermé le 31/08/2026 : deux orphelines de
#: `5e_C1.2` ont disparu du relevé parce que je venais d'écrire leur ligne de
#: licence (règle d'or n°263, prise par l'autre bout).
INVENTAIRES = re.compile(r"^(SOURCES_MEDIAS\.md|manifest.*\.json)$", re.I)

#: `Images/nom.svg` ou `../5e_C4.1/Images/nom.svg`, où qu'il apparaisse : dans un
#: `src=`, dans une parenthèse Markdown, **et entre accents graves** — une fiche
#: pédagogique qui écrit « voir `Images/x.svg` » présente bien l'image au
#: professeur. Énumérer les délimiteurs, c'est en oublier un : on borne donc par
#: « pas un caractère de chemin » d'un côté, par l'extension de l'autre.
#: Construite depuis IMAGES : deux listes d'extensions qui se recopient finissent
#: par diverger, et c'est la seconde qu'on oublie de compléter (règle n°269).
CITATION = re.compile(r"(?<![\w./\-])((?:[\w.\-]+/)*Images/[\w.\-]+?\.(?:%s))\b"
                      % "|".join(e[1:] for e in IMAGES), re.I)


def dossiers_medias(racine):
    """Les dossiers `Images/` qui portent au moins un fichier image."""
    for dossier, _, fichiers in os.walk(racine):
        if any(e in dossier for e in ECARTES):
            continue
        if os.path.basename(dossier) != "Images":
            continue
        noms = sorted(f for f in fichiers if f.lower().endswith(IMAGES))
        if noms:
            yield os.path.dirname(dossier), noms


def citees(lot):
    """Les images que les fichiers du lot désignent, en noms relatifs au lot."""
    vues = set()
    for dossier, _, fichiers in os.walk(lot):
        if any(e in dossier for e in ECARTES) or os.path.basename(dossier) == "Images":
            continue
        for f in fichiers:
            if not f.lower().endswith(PORTEUSES) or INVENTAIRES.match(f):
                continue
            chemin = os.path.join(dossier, f)
            try:
                texte = open(chemin, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for u in CITATION.findall(texte):
                absolu = os.path.normpath(os.path.join(dossier, u))
                vues.add(os.path.relpath(absolu, lot).replace(os.sep, "/"))
    return vues


def declarees(lot):
    """Les images que les manifestes du lot promettent, en noms relatifs au lot."""
    promises = set()
    for f in sorted(os.listdir(lot)):
        if not re.match(r"manifest.*\.json$", f, re.I):
            continue
        try:
            donnees = json.load(open(os.path.join(lot, f), encoding="utf-8")) or {}
        except (ValueError, OSError):
            continue
        fichiers = donnees.get("fichiers")
        if not isinstance(fichiers, dict):
            continue
        for i in fichiers.get("images") or []:
            if isinstance(i, str):
                promises.add((f, i))
    return promises


def nommees_par_un_manifeste(lot):
    """Toute image qu'un manifeste du lot nomme, où que ce soit dans son texte.

    `fichiers.images` n'est pas le seul endroit : `5e_C1.2` range deux SVG sous
    `herite_conserve`, c'est-à-dire « hérités, gardés exprès ». Une image que le
    manifeste nomme n'est pas oubliée — quelqu'un a décidé qu'elle restait, même
    si aucune page ne l'affiche encore. La distinguer d'une image que rien ne
    mentionne, c'est la différence entre une décision et un oubli.
    """
    nommees = set()
    for f in sorted(os.listdir(lot)):
        if not re.match(r"manifest.*\.json$", f, re.I):
            continue
        try:
            texte = open(os.path.join(lot, f), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        nommees.update(CITATION.findall(texte))
    return nommees


def main(muet=False):
    refus, dettes, orphelines, gardees = [], [], [], []
    releve = collections.Counter()

    for lot, noms in dossiers_medias(DEPOT):
        nom_lot = os.path.relpath(lot, DEPOT)
        releve["lots"] += 1
        releve["medias"] += len(noms)

        # ── 1. la provenance : un SOURCES_MEDIAS.md, ou rien ────────────────
        source = os.path.join(lot, "SOURCES_MEDIAS.md")
        if not os.path.exists(source):
            refus.append("%s\n     porte %d média(s) — %s — et AUCUN SOURCES_MEDIAS.md :\n"
                         "     leur licence n'est écrite nulle part"
                         % (nom_lot, len(noms), ", ".join(noms[:4])
                            + (" …" if len(noms) > 4 else "")))
            continue
        texte = open(source, encoding="utf-8", errors="replace").read()
        muettes = [n for n in noms if n not in texte]
        releve["documentes"] += len(noms) - len(muettes)
        if muettes:
            dettes.append((len(muettes), nom_lot, muettes))

        # ── 2. la promesse : une image déclarée doit être sur le disque ─────
        for manifeste, promise in sorted(declarees(lot)):
            releve["promesses"] += 1
            if not os.path.exists(os.path.join(lot, promise)):
                refus.append("%s\n     %s promet `%s`, absent du disque"
                             % (nom_lot, manifeste, promise))

        # ── 3. l'emploi : compté, jamais refusé ────────────────────────────
        vues = citees(lot)
        inventaire = nommees_par_un_manifeste(lot)
        seules = [n for n in noms if "Images/" + n not in vues]
        muettes_du_lot = sorted(n for n in seules if "Images/" + n not in inventaire)
        declarees_du_lot = sorted(n for n in seules if "Images/" + n in inventaire)
        if muettes_du_lot:
            orphelines.append((len(muettes_du_lot), nom_lot, muettes_du_lot))
        if declarees_du_lot:
            gardees.append((len(declarees_du_lot), nom_lot, declarees_du_lot))

    if not muet:
        print("%d lot(s) portent des images · %d fichier(s) média · %d nommés par leur "
              "SOURCES_MEDIAS.md · %d promesse(s) de manifeste vérifiées"
              % (releve["lots"], releve["medias"], releve["documentes"], releve["promesses"]))
        if dettes:
            total = sum(n for n, _, _ in dettes)
            print("\n%d lot(s) portent %d média(s) que leur SOURCES_MEDIAS.md ne nomme pas.\n"
                  "     Ce n'est pas une faute : le fichier existe, la charte est connue, et\n"
                  "     la ligne reste à écrire par qui sait ce qu'il écrit. Les plus fournis "
                  "d'abord :" % (len(dettes), total))
            for n, nom, quoi in sorted(dettes, reverse=True)[:10]:
                print("     %4d  %s\n           %s" % (n, nom, ", ".join(quoi[:3])
                                                       + (" …" if len(quoi) > 3 else "")))
        if orphelines:
            total = sum(n for n, _, _ in orphelines)
            print("\n%d lot(s) portent %d image(s) qu'aucune page n'affiche et qu'AUCUN "
                  "manifeste\n     ne nomme. À trancher, pas à deviner : schéma sans emploi "
                  "à retirer, ou\n     image-objet dont le câblage dans la séquence a été "
                  "oublié." % (len(orphelines), total))
            for n, nom, quoi in sorted(orphelines, reverse=True)[:10]:
                print("     %4d  %s\n           %s" % (n, nom, ", ".join(quoi[:3])
                                                       + (" …" if len(quoi) > 3 else "")))
        if gardees:
            total = sum(n for n, _, _ in gardees)
            print("\n     (%d image(s) dans %d lot(s) ne sont affichées par aucune page mais "
                  "sont NOMMÉES\n     par leur manifeste — `herite_conserve` et semblables : "
                  "gardées exprès, pas\n     oubliées. Une décision écrite n'est pas un oubli.)"
                  % (total, len(gardees)))
            for n, nom, quoi in sorted(gardees, reverse=True)[:6]:
                print("     %4d  %s — %s" % (n, nom, ", ".join(quoi[:3])
                                             + (" …" if len(quoi) > 3 else "")))
        print("\n     NON LU : le poids, le format et la qualité d'une image ; qu'une image\n"
              "     citée par une page existe (c'est `controle_liens.py`) ; les nombres\n"
              "     qu'un manifeste annonce (c'est `controle_effectifs_qcm.py`).")

    if refus:
        print("\n⛔ %d dossier(s) en défaut de provenance ou de promesse :" % len(refus))
        for r in refus:
            print("  " + r)
        print("\n     Une image peut n'être employée nulle part — on le dit alors. Ce qu'elle\n"
              "     ne peut pas faire, c'est exister sans que rien ne dise d'où elle vient.")
        return 1
    print("\n✅ chaque image du dépôt a une provenance écrite, et aucune n'est promise en vain")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
