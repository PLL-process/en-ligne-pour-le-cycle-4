# -*- coding: utf-8 -*-
"""controle_statut.py — le statut « COMPLET ET VALIDABLE » doit se mériter.

Jusqu'ici, ce statut était **déclaré** code par code dans l'OVERLAY de
`build_audit.py`. Une déclaration ne se trompe jamais : elle se contente d'être
fausse en silence. Trois audits externes du Thème 2 ont tous dit, chacun à sa
manière, « la gouvernance de validation est trop généreuse ». Aucun n'a pu dire
*de combien* — parce qu'aucun ne comptait.

Ici, on compte. Pour chaque code qui revendique « COMPLET ET VALIDABLE », on
regarde ce que son dossier porte vraiment :

    séquence · QCM (avec une vraie banque) · fiche pédagogique ·
    matrice de couverture · synthèses · rapport de tests

Un code qui ne peut pas montrer ces six pièces ne perd pas son contenu : il perd
son étiquette. Deux issues, selon ce que dit l'OVERLAY :

  - il porte `mutualise_avec` → il est reclassé « COUVERT PAR UNE SÉQUENCE
    MUTUALISÉE », ce qu'il est réellement ;
  - sinon → « À VÉRIFIER PAR L'ENSEIGNANT », avec la liste des pièces absentes
    écrite noir sur blanc dans la matrice.

Règle d'or n°187 : une note qui compte quelque chose se calcule.
Règle d'or n°190 : un statut qu'aucun contrôle ne peut retirer n'est pas un
statut, c'est une décoration.

Le QCM est le cas intéressant : trois fichiers du dépôt s'appellent `qcm_*.html`
sans porter de banque de questions (`qcm_algorigrammes_domotique`, qui est un TP,
`qcm_jardin_connecte` et `qcm_ecall_chaine_information`). Compter les fichiers
dont le nom commence par « qcm » aurait validé les trois. On lit donc la banque,
pas le nom — règle d'or n°184.
"""

import os
import re

VALIDABLE = "COMPLET ET VALIDABLE"
MUTUALISE = "COUVERT PAR UNE SÉQUENCE MUTUALISÉE"
A_VERIFIER = "À VÉRIFIER PAR L’ENSEIGNANT"

#: nombre minimal de questions pour qu'un fichier « qcm_… » soit un QCM
QUESTIONS_MINIMUM = 10


def _texte(chemin):
    try:
        with open(chemin, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except OSError:
        return ""


def banque_de_questions(chemin):
    """Nombre de questions portées par un QCM AU GABARIT MAISON (banque JS)."""
    t = _texte(chemin)
    m = re.search(r"const QUESTIONS\s*=\s*\[", t)
    if not m:
        return 0
    return len(re.findall(r"\bq:\s*\"", t[m.end():]))


def questions_heritees(chemin):
    """Nombre approximatif de questions d'un QCM écrit à l'ancienne, sans banque.

    Un QCM codé en dur — un `<input type="radio">` par option — est un vrai QCM :
    il n'est simplement pas au gabarit. Le confondre avec « pas de QCM » a produit
    une phrase fausse dans la matrice : `4e_C6.2` était annoncé sans QCM alors
    qu'il en porte un de 24 questions. On compte donc les deux, séparément.
    """
    if banque_de_questions(chemin):
        return 0
    t = _texte(chemin)
    radios = len(re.findall(r'type="radio"', t))
    return radios // 4 if radios >= 8 else 0


def _liste(dossier):
    try:
        return sorted(os.listdir(dossier))
    except OSError:
        return []


def pieces_du_lot(dossier_absolu):
    """Ce que le dossier d'un code porte vraiment, pièce par pièce."""
    noms = _liste(dossier_absolu)
    trouve = {}

    trouve["sequence"] = [n for n in noms
                          if re.match(r"s[ée]quence", n, re.I) and n.lower().endswith(".html")]
    candidats = [n for n in noms if re.match(r"qcm", n, re.I) and n.lower().endswith(".html")]
    trouve["qcm"] = [n for n in candidats
                     if banque_de_questions(os.path.join(dossier_absolu, n)) >= QUESTIONS_MINIMUM]
    trouve["qcm_herite"] = [n for n in candidats
                           if questions_heritees(os.path.join(dossier_absolu, n)) >= QUESTIONS_MINIMUM]
    trouve["fiche"] = [n for n in noms if re.match(r"fiche_pedagogique", n, re.I)]
    trouve["matrice"] = [n for n in noms if re.match(r"matrice", n, re.I)]
    trouve["tests"] = [n for n in noms if re.search(r"rapport.*test|^tests?_", n, re.I)]

    synth = []
    for racine, _, fichiers in os.walk(dossier_absolu):
        synth += [f for f in fichiers if re.search(r"synth", f, re.I)]
    trouve["synthese"] = synth

    return trouve


#: ordre d'affichage, et libellé lisible dans la matrice
LIBELLES = [
    ("sequence", "séquence"),
    ("qcm", "QCM au gabarit maison"),
    ("fiche", "fiche pédagogique"),
    ("matrice", "matrice de couverture"),
    ("synthese", "synthèses"),
    ("tests", "rapport de tests"),
]


def verdict(statut_declare, dossier_absolu, mutualise_avec=""):
    """Renvoie (statut_tenu, pièces manquantes, phrase à écrire dans la matrice).

    N'agit que sur les codes qui revendiquent « COMPLET ET VALIDABLE » : on ne
    promeut jamais, on ne fait que refuser une revendication non tenue.
    """
    if statut_declare != VALIDABLE:
        return statut_declare, [], ""

    pieces = pieces_du_lot(dossier_absolu)
    absents = [libelle for cle, libelle in LIBELLES if not pieces[cle]]
    if not absents:
        return VALIDABLE, [], ""

    # Un QCM hérité n'ouvre pas le statut, mais il change ce qu'on a le droit
    # d'écrire : « pas de QCM au gabarit » n'est pas « pas de QCM ».
    if "QCM au gabarit maison" in absents and pieces.get("qcm_herite"):
        i = absents.index("QCM au gabarit maison")
        absents[i] = "QCM au gabarit maison (un QCM hérité est présent : %s)" % (
            ", ".join(pieces["qcm_herite"]))

    if mutualise_avec:
        phrase = ("Reclassé par contrôle : le dossier ne porte pas %s. "
                  "Le geste est porté ailleurs (voir « %s »)." % (", ".join(absents), mutualise_avec))
        return MUTUALISE, absents, phrase

    phrase = ("Reclassé par contrôle : « complet et validable » revendiqué, mais "
              "le dossier ne porte pas %s." % ", ".join(absents))
    return A_VERIFIER, absents, phrase
