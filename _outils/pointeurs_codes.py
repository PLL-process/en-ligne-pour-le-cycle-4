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

Usage : python3 pointeurs.py [--etat]
"""
import os
import pathlib
import sys

DEPOT = pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent
sys.path.insert(0, str(DEPOT / "_outils"))
import data_competences as DC

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
             "elle-même qui travaille ce code, du croquis au prototype.", True),
 "3e_C7.2": (C7 + "/3e/3e_C7.2", "../3e_C7.1/sequence_3e_C7_capteur-confort-ny.html",
             "Séquence 3e — Le capteur de confort",
             "La séquence conçoit un ensemble de solutions pour un OST nouveau : le capteur de "
             "confort de la salle, de la proposition au prototype.", True),
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
 "5e_C8.1": (C8 + "/5e/5e_C8.1", "../../../" + C7.split("/", 1)[1] + "/5e/5e_C7.1/sequence_5e_C7_mini-projet-objet.html",
             "Séquence 5e — Le mini-projet d'objet",
             "La validation par un protocole de test simple y est travaillée comme étape du "
             "mini-projet, avec l'indicateur de place.", True),
 "3e_C8.1": (C8 + "/3e/3e_C8.1", "../../../" + C7.split("/", 1)[1] + "/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html",
             "Séquence 3e — Le capteur de confort",
             "La validation par protocole de test y est travaillée sur l'alerte de température "
             "et l'îlot de chaleur.", True),
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
écrit que si la ressource cible existe réellement sur le disque.*
"""

EVALUE = ("**Ce code y est évalué.** La ressource porte un QCM et une production d'élève qui "
          "permettent de le positionner.")
ENSEIGNE = ("**Ce code y est enseigné, et il n'y est pas évalué.** L'atelier CAO ne pose aucune "
            "question de cours : on y apprend l'outil, et la notion s'évalue dans les séquences "
            "de niveau (règle d'or n°81). Le statut du code reste donc « à vérifier par "
            "l'enseignant » : c'est à vous de dire où vous l'évaluez.")


def formulation(code):
    niveau, c = code.split("_")
    for cc, f, socle in sum(DC.COMP_BY_LEVEL[niveau].values(), []):
        if cc == c:
            return f, socle
    raise KeyError(code)


def main(etat=False):
    ecrits, refuses, deja = [], [], []
    for code, (dossier, cible, lien_titre, quoi, evalue) in sorted(POINTEURS.items()):
        d = DEPOT / dossier
        if not d.is_dir():
            refuses.append("%s : dossier absent" % code)
            continue
        if not (d / cible).resolve().exists():
            refuses.append("%s : cible absente — %s" % (code, cible))
            continue
        f, socle = formulation(code)
        texte = MODELE.format(code=code, titre=f.rstrip("."), formulation=f, socle=socle,
                              lien_titre=lien_titre, cible=cible, quoi=quoi,
                              evaluation=EVALUE if evalue else ENSEIGNE)
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
    if refuses:
        print("⛔ %d refusé(s) — un pointeur vers une cible absente n'est pas écrit :" % len(refuses))
        for r in refuses:
            print("     " + r)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--etat" in sys.argv))
