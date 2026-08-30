#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Donne un README à tout dossier de code qui n'en a pas — ou qui n'indique pas le chemin.

Le constat qui a donné cet outil
--------------------------------
Dix dossiers de codes ne portaient aucune pièce. Deux seulement (`4e_C9.2` et
`4e_C9.3`) portaient un README avec des liens qui marchent. Cinq étaient
**entièrement muets** : ni fichier, ni README, rien. Trois portaient un README
qui annonce « COUVERT » et donne un chemin **dans un bloc de code**, que
personne ne peut cliquer.

Un dossier muet apprend à ne plus ouvrir les dossiers, exactement comme un
bouton qui ne mène nulle part apprend à ne plus cliquer (règle d'or n°183).

Ce que ce script écrit — et ce qu'il n'écrit pas
------------------------------------------------
Il écrit un README qui dit trois choses : **la formulation officielle du code**
(recopiée de `_outils/data_competences.py`, seule autorité du dépôt), **où le
geste est réellement travaillé**, et **ce que la ressource cible fait ou ne fait
pas** de ce code. Il ne promet aucune couverture qu'il n'a pas vérifiée : quand
la ressource enseigne sans évaluer, le README le dit, et le statut du code ne
bouge pas.

Chaque cible est vérifiée sur le disque avant écriture. Un pointeur vers un
fichier absent n'est pas écrit du tout.

Ce que la première version promettait sans le vérifier
------------------------------------------------------
Le champ « évalue-t-elle le code ? » était un **booléen écrit à la main**, et la
phrase « **Ce code y est évalué** » en découlait. Exactement comme le statut de
l'audit avant qu'on le contrôle : une déclaration ne se trompe jamais, elle se
contente d'être fausse en silence.

`controle_couverture.py` a mesuré. Trois pointeurs sur dix promettaient une
évaluation qui n'existe nulle part : `5e_C7.2` et `3e_C7.2` (les mini-projets
étiquettent leurs groupes en C7.1, C8.3 et C9.3 — jamais en C7.2) et `5e_C8.1`
(dont les questions n'existaient pas encore).

Le booléen reste écrit, mais il n'est plus cru : il est **confronté** au nombre
de questions que la banque de la cible porte réellement pour ce code. En cas de
désaccord, le README n'est pas écrit et l'outil sort en erreur. Règle d'or
n°242 : un instrument ne prouve une absence que là où il a regardé — et ici,
c'est la banque de la cible qu'il faut regarder.

Un dossier qui porte SON PROPRE lot n'est jamais écrasé par un pointeur : la
phrase « ce dossier ne porte aucune ressource propre » est vérifiable, donc
elle est vérifiée. Deux cas s'y cachent, et ils n'ont pas la même gravité :

  · le dossier a **grandi** — il porte son lot ET un README qui n'est plus le
    pointeur engendré. La table est simplement en retard : on le dit, on invite
    à retirer l'entrée, et on sort en 0. C'est le cas des trois codes de
    l'atelier CAO le jour où ils ont reçu leur QCM ;
  · le dossier porte un lot **derrière un renvoi** — son README est encore le
    pointeur engendré, qui affirme « ce dossier ne porte aucune ressource
    propre » alors que c'est faux. Là, on refuse.

La deuxième erreur de la première version : la phrase « la notion s'évalue
ailleurs » ne disait pas OÙ, et n'avait rien regardé pour l'affirmer. Elle ne
comptait que dans la banque de la cible. Le jour où `3e_C7.2` a reçu dix
questions dans la banque du boîtier, le README a continué de dire « c'est à vous
de dire où vous l'évaluez ». C'est encore la règle d'or n°242, sur un autre
instrument : on regarde donc maintenant **tout le dépôt** avant de renvoyer
l'enseignant à lui-même, et on nomme la banque quand elle existe.

Usage : python3 pointeurs_codes.py [--etat]
"""
import os
import pathlib
import sys

DEPOT = pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent
sys.path.insert(0, str(DEPOT / "_outils"))
import data_competences as DC
from controle_couverture import SEUIL_EVALUABLE, banques_du_depot
from controle_statut import pieces_du_lot

T3 = "theme-3-creation-conception-realisation-innovations"
C7 = T3 + "/C7-imaginer-concevoir-et-realiser-une-ou-des"
C8 = T3 + "/C8-valider-les-solutions-techniques-par-des"
C9 = T3 + "/C9-concevoir-ecrire-tester-et-mettre-au-point"

#: code → (dossier, cible relative, titre du lien, ce que la cible fait de ce code,
#:         évalue-t-elle le code ? — un README ne promeut jamais un statut)
POINTEURS = {
 "5e_C7.2": (C7 + "/5e/5e_C7.2", "../5e_C7.1/sequence_5e_C7_mini-projet-objet.html",
             "Séquence 5e — Le mini-projet d'objet",
             "Le mini-projet propose et fabrique une solution : c'est l'activité de conception "
             "elle-même qui travaille ce code, du croquis au prototype.", False),
 "3e_C7.2": (C7 + "/3e/3e_C7.2", "../3e_C7.1/sequence_3e_C7_capteur-confort-ny.html",
             "Séquence 3e — Le capteur de confort",
             "La séquence conçoit un ensemble de solutions pour un OST nouveau : le capteur de "
             "confort de la salle, de la proposition au prototype.", False),
 "4e_C7.2": (C7 + "/4e/4e_C7.2", "../4e_C7.1/sequence_4e_C7_jardin-conception.html",
             "Séquence 4e — Le jardin connecté, conception",
             "L'activité 2 de la séquence est consacrée à ce code : deux solutions proposées et "
             "justifiées. La matrice de couverture du lot le relie aux questions 3, 8, 9 et 13 "
             "du QCM.", True),
 "5e_C7.6": (C7 + "/5e/5e_C7.6", "../../atelier-cao/tp_5e_de_onshape.html",
             "TP 5e — Le dé (atelier CAO)",
             "Le TP met en œuvre les moyens de modélisation selon une procédure fournie : "
             "esquisser, coter, extruder, enlever, adoucir.", False),
 "4e_C7.6": (C7 + "/4e/4e_C7.6", "../../atelier-cao/tp_4e_socle_assemblage.html",
             "TP 4e — Le dé sur son socle (atelier CAO)",
             "Le TP modifie une forme à l'aide d'une modélisation : la révolution, puis "
             "l'assemblage et les contraintes.", False),
 "3e_C7.6": (C7 + "/3e/3e_C7.6", "../../atelier-cao/tp_3e_boitier_etanche.html",
             "TP 3e — Le boîtier étanche (atelier CAO)",
             "Le TP modélise une forme voulue : la coque, la rainure, le passage de câble, la "
             "vue en coupe. C'est ce boîtier que 3e_C7.7 produit ensuite.", False),
 "4e_C9.2": (C9 + "/4e/4e_C9.2", "../4e_C9.1/sequence_4e_C9_jardin-programme.html",
             "Séquence 4e — Le jardin connecté se programme",
             "L'activité 3 lui est consacrée : l'algorigramme devient un programme, en blocs "
             "puis en Python. Le QCM du lot y consacre 10 de ses 30 questions.", True),
 "4e_C9.3": (C9 + "/4e/4e_C9.3", "../4e_C9.1/sequence_4e_C9_jardin-programme.html",
             "Séquence 4e — Le jardin connecté se programme",
             "Trois activités lui sont consacrées : le jeu d'essais, le clignotement corrigé par "
             "hystérésis, et le réinvestissement sans modèle. Le QCM du lot y consacre 10 de ses "
             "30 questions.", True),
}

MODELE = """# {code} — {titre}

> {formulation}
>
> Programme 2024 · cycle 4 · thème 3 · socle {socle}

**Ce dossier ne porte aucune ressource propre.** Le geste de ce code est travaillé ici :

➡ **[{lien_titre}]({cible})**

{quoi}

{evaluation}

---

*Formulation recopiée de `_outils/data_competences.py`, seule autorité du dépôt sur les
libellés du référentiel. Ce README est engendré par `_outils/pointeurs_codes.py` : il n'est
écrit que si la ressource cible existe réellement sur le disque, et la phrase sur l'évaluation
est **mesurée** dans la banque de cette ressource, jamais déclarée.*
"""

EVALUE = ("**Ce code y est évalué.** La banque de la ressource porte {n} questions étiquetées "
          "`{code}` ({banques}) : le score se reporte.")
ENSEIGNE = ("**Ce code y est enseigné, et il n'y est pas évalué.** Aucune question de la banque "
            "de la ressource ne porte `{code}` : on y apprend le geste, et la notion s'évalue "
            "ailleurs (règle d'or n°81). Le statut du code reste donc « à vérifier par "
            "l'enseignant » : c'est à vous de dire où vous l'évaluez.")
ENSEIGNE_AILLEURS = (
    "**Ce code y est enseigné, et il n'y est pas évalué — mais il l'est ailleurs.** Aucune "
    "question de la banque de la ressource ne porte `{code}` : on y apprend le geste (règle "
    "d'or n°81). {n} question(s) l'évaluent dans une autre banque du dépôt ({banques}) : "
    "c'est de là que le score se reporte.")
SOUS_SEUIL = ("**Ce code y est effleuré.** La banque de la ressource ne porte que {n} question(s) "
              "étiquetée(s) `{code}` ({banques}), pour un seuil d'évaluabilité de "
              "{seuil} : c'est trop peu pour reporter un score. Le statut du code reste « à "
              "vérifier par l'enseignant ».")

#: la phrase qui signe un README engendré — elle sert à savoir si un dossier a
#: reçu son propre README, ou s'il porte encore le renvoi
SIGNATURE = "Ce README est engendré par `_outils/pointeurs_codes.py`"


def formulation(code):
    niveau, c = code.split("_")
    for cc, f, socle in sum(DC.COMP_BY_LEVEL[niveau].values(), []):
        if cc == c:
            return f, socle
    raise KeyError(code)


def mesure(code, dossier, cible, index):
    """Combien de questions la banque de la CIBLE porte-t-elle pour ce code ?

    C'est la seule question qui décide de la phrase « ce code y est évalué ».
    On ne compte pas les questions d'ailleurs dans le dépôt : le README parle
    d'une ressource précise, il ne doit promettre que ce qu'elle contient.
    """
    niveau, c = code.split("_")
    cible_dir = os.path.dirname(os.path.normpath(os.path.join(dossier, cible)))
    dedans = [(rel, n) for rel, n, _partage in index.get((niveau, c), [])
              if rel.startswith(cible_dir + "/")]
    return sum(n for _rel, n in dedans), [rel.split("/")[-1] for rel, _n in dedans]


def mesure_ailleurs(code, dossier, cible, index):
    """Combien de questions évaluent ce code AILLEURS dans le dépôt, et où ?

    On ne le demande qu'après avoir constaté que la banque de la cible n'en
    porte pas : le README parle d'abord de sa ressource. Mais renvoyer
    l'enseignant à lui-même (« c'est à vous de dire où vous l'évaluez ») alors
    qu'une banque du dépôt évalue le code est une absence non vérifiée.
    """
    niveau, c = code.split("_")
    cible_dir = os.path.dirname(os.path.normpath(os.path.join(dossier, cible)))
    dehors = [(rel, n) for rel, n, _partage in index.get((niveau, c), [])
              if not rel.startswith(cible_dir + "/")]
    return sum(n for _rel, n in dehors), [rel.split("/")[-1] for rel, _n in dehors]


def porte_son_lot(dossier_absolu):
    """Ce dossier porte-t-il sa propre séquence ou son propre QCM ?

    Un pointeur affirme « ce dossier ne porte aucune ressource propre ». Le jour
    où c'est faux, l'écraser remplacerait un lot complet par un renvoi. La
    phrase est vérifiable : on la vérifie.
    """
    pieces = pieces_du_lot(str(dossier_absolu))
    return bool(pieces["sequence"] or pieces["qcm"])


def main(etat=False):
    ecrits, refuses, deja, promus = [], [], [], []
    index = banques_du_depot()
    for code, (dossier, cible, lien_titre, quoi, evalue) in sorted(POINTEURS.items()):
        d = DEPOT / dossier
        if not d.is_dir():
            refuses.append("%s : dossier absent" % code)
            continue
        if not (d / cible).resolve().exists():
            refuses.append("%s : cible absente — %s" % (code, cible))
            continue
        if porte_son_lot(d):
            readme = d / "README.md"
            propre = readme.exists() and SIGNATURE not in readme.read_text(encoding="utf-8")
            if propre:
                promus.append("%s : ce dossier porte désormais SON PROPRE lot et son propre "
                              "README — l'entrée de POINTEURS peut être retirée." % code)
            else:
                refuses.append("%s : ce dossier porte un lot DERRIÈRE un renvoi — le README "
                               "engendré affirme « aucune ressource propre », et c'est faux. "
                               "Retirer l'entrée de POINTEURS et écrire le README du lot."
                               % code)
            continue
        n, banques = mesure(code, dossier, cible, index)
        if bool(evalue) != (n >= SEUIL_EVALUABLE):
            refuses.append("%s : la déclaration dit « %s » et la mesure dit %d question(s) "
                           "dans la banque de la cible (seuil %d)"
                           % (code, "évalué" if evalue else "non évalué", n, SEUIL_EVALUABLE))
            continue
        if n >= SEUIL_EVALUABLE:
            phrase = EVALUE.format(n=n, code=code, banques=", ".join("`%s`" % b for b in banques))
        elif n:
            phrase = SOUS_SEUIL.format(n=n, code=code, seuil=SEUIL_EVALUABLE,
                                       banques=", ".join("`%s`" % b for b in banques))
        else:
            ailleurs, ou = mesure_ailleurs(code, dossier, cible, index)
            if ailleurs >= SEUIL_EVALUABLE:
                phrase = ENSEIGNE_AILLEURS.format(
                    code=code, n=ailleurs, banques=", ".join("`%s`" % b for b in ou))
            else:
                phrase = ENSEIGNE.format(code=code)
        f, socle = formulation(code)
        texte = MODELE.format(code=code, titre=f.rstrip("."), formulation=f, socle=socle,
                              lien_titre=lien_titre, cible=cible, quoi=quoi,
                              evaluation=phrase)
        readme = d / "README.md"
        if readme.exists() and readme.read_text(encoding="utf-8") == texte:
            deja.append(code)
            continue
        if not etat:
            readme.write_text(texte, encoding="utf-8")
        ecrits.append(code + (" (réécrit)" if readme.exists() else ""))
    print("%d README %s : %s" % (len(ecrits), "à écrire" if etat else "écrits", ", ".join(ecrits) or "aucun"))
    if deja:
        print("%d déjà à jour : %s" % (len(deja), ", ".join(deja)))
    if promus:
        print("%d dossier(s) qui ont grandi — la table est en retard, rien n'est faux :"
              % len(promus))
        for p in promus:
            print("     " + p)
    if refuses:
        print("⛔ %d refusé(s) — un pointeur n'est écrit que si sa cible existe, si le "
              "dossier ne porte pas son propre lot, et si la mesure confirme la "
              "déclaration :" % len(refuses))
        for r in refuses:
            print("     " + r)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--etat" in sys.argv))
