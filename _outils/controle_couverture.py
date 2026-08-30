# -*- coding: utf-8 -*-
"""controle_couverture.py — un lot nomme-t-il le code qu'il prétend couvrir ?

`controle_statut.py` compte les **pièces** d'un lot : séquence, QCM, fiche,
matrice, synthèses, rapport de tests. Six pièces présentes, statut tenu. C'est
utile, et c'est insuffisant : six pièces peuvent parler d'autre chose que du
code sous lequel elles sont rangées. Le dossier serait plein, la matrice
verte — et la preuve de couverture, nulle part.

Règle d'or n°237 : compter les pièces n'est pas vérifier la couverture.
Règle d'or n°238 : la preuve d'une couverture est une ligne, pas un dossier.

Cet outil ne juge rien et ne modifie rien. Il ouvre les fichiers d'un lot et
répond à une question de fait : **le code y est-il écrit, et où ?**

    ÉVALUÉ      le QCM du lot porte au moins SEUIL_EVALUABLE questions
                étiquetées de ce code — la couverture est mesurable
    CITÉ        le code est écrit dans une pièce qui enseigne ou qui atteste
                (séquence, fiche, matrice, synthèse) mais aucune question ne
                le porte en nombre suffisant
    RENVOI      le code n'apparaît que dans une pièce d'orientation — README,
                manifeste, lexique. Le lot dit où aller, il ne montre rien.
    NON NOMMÉ   le lot porte des fichiers et ne nomme jamais son propre code
    VIDE        rien à lire

La distinction RENVOI / CITÉ n'est pas un détail de vocabulaire : depuis que
`pointeurs_codes.py` écrit un README dans chaque dossier, *tout* code est
« nommé » quelque part. Compter ces README comme des preuves rendrait l'outil
aveugle le jour même de sa naissance.

Le cas « NON NOMMÉ » n'accuse personne : la plupart de ces banques étiquettent
leurs questions par un mot de thème (ELA, SIM, SEU…) au lieu du code. L'outil
le dit aussi, en listant pour chaque banque les étiquettes qui ne sont pas des
codes. C'est ce relevé qui permet de décider, question par question, quel code
chaque groupe travaille réellement — décision pédagogique qui n'appartient pas
à un script.

Usage :
    python3 _outils/controle_couverture.py             # rapport complet
    python3 _outils/controle_couverture.py --muets     # les seuls sans preuve
    python3 _outils/controle_couverture.py --json x.json

Le code de sortie est toujours 0 : un diagnostic n'a pas de verdict.
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_audit import OVERLAY, RACINE, code_dir  # noqa: E402
from controle_statut import pieces_du_lot, verdict  # noqa: E402
from data_competences import COMP_BY_LEVEL  # noqa: E402

#: en deçà, un code cité par le QCM n'est pas évaluable (même seuil que
#: controle_echantillonnage.py — deux outils, une seule définition)
SEUIL_EVALUABLE = 5

#: fichiers d'un lot qu'on ouvre pour y chercher le code
LISIBLES = (".html", ".md", ".csv", ".json", ".py", ".txt")

#: dossiers qu'on n'ouvre jamais : ce qui y dort ne prouve plus rien
IGNORES = ("_archive-anciennes-versions", "archive", "anciennes-versions")

#: pièces d'orientation : elles disent où aller, elles n'enseignent pas.
#: Un code qui n'apparaît que là n'est pas couvert par ce lot — il y est cité.
ORIENTATION = re.compile(r"(^|/)(README|manifest|manifeste|lexique|SOURCES_MEDIAS|"
                         r"PLAN_LOT|JOURNAL|NOTES?)[^/]*$", re.I)


def _texte(chemin):
    try:
        with open(chemin, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except OSError:
        return ""


def _fichiers_du_lot(dossier):
    """Tous les fichiers lisibles d'un lot, archives exclues."""
    out = []
    for racine, sous, noms in os.walk(dossier):
        sous[:] = [d for d in sous if d not in IGNORES]
        for n in noms:
            if n.lower().endswith(LISIBLES):
                out.append(os.path.join(racine, n))
    return sorted(out)


def _motif(niveau, code):
    """« C7.1 » écrit seul, ou préfixé du niveau, jamais « C7.10 » par accident.

    Le souligné compte comme une séparation : `synthese_eleve_5e_C4.1.html` nomme
    bien le code. Le point aussi : `matrice_5e_C7.4.csv` également. Ce qui est
    interdit devant, c'est une lettre ou un chiffre ; derrière, un chiffre.
    """
    nu = re.escape(code)
    pref = re.escape(niveau)
    return re.compile(r"(?<![A-Za-z0-9.])(?:%s[ _-])?%s(?!\d)" % (pref, nu))


def etiquettes_de_banque(chemin):
    """Les valeurs du champ `c:` d'une banque au gabarit maison, comptées.

    On lit la banque, pas le nom du fichier (règle d'or n°184) : trois fichiers
    du dépôt s'appellent `qcm_…` sans porter la moindre question.
    """
    t = _texte(chemin)
    m = re.search(r"const QUESTIONS\s*=\s*\[", t)
    if not m:
        return {}
    compte = {}
    for c in re.findall(r'\bc\s*:\s*"([^"]*)"', t[m.end():]):
        compte[c] = compte.get(c, 0) + 1
    return compte


def questions_portant(chemin, niveau, code):
    """Combien de questions d'une banque sont étiquetées de ce code."""
    mot = _motif(niveau, code)
    return sum(n for e, n in etiquettes_de_banque(chemin).items() if mot.search(e))


def examiner(niveau, code, dossier_absolu):
    """Où ce lot nomme-t-il son propre code ? Renvoie un dictionnaire de faits."""
    fichiers = _fichiers_du_lot(dossier_absolu)
    if not fichiers:
        return dict(etat="VIDE", questions=0, ou=[], renvois=[],
                    etiquettes={}, fichiers=0)

    mot = _motif(niveau, code)
    pieces = pieces_du_lot(dossier_absolu)

    questions, etiquettes = 0, {}
    for nom in pieces["qcm"] + pieces["qcm_herite"]:
        chemin = os.path.join(dossier_absolu, nom)
        questions += questions_portant(chemin, niveau, code)
        for e, n in etiquettes_de_banque(chemin).items():
            if not mot.search(e):
                etiquettes[nom] = etiquettes.get(nom, {})
                etiquettes[nom][e] = n

    ou, renvois = [], []
    for chemin in fichiers:
        if not mot.search(_texte(chemin)):
            continue
        rel = os.path.relpath(chemin, dossier_absolu).replace(os.sep, "/")
        (renvois if ORIENTATION.search(rel) else ou).append(rel)

    if questions >= SEUIL_EVALUABLE:
        etat = "ÉVALUÉ"
    elif ou:
        etat = "CITÉ"
    elif renvois:
        etat = "RENVOI"
    else:
        etat = "NON NOMMÉ"

    return dict(etat=etat, questions=questions, ou=ou, renvois=renvois,
                etiquettes=etiquettes, fichiers=len(fichiers))


def statut_tenu(niveau, code, dossier_absolu):
    """Le statut que le code tient RÉELLEMENT, contrôle de pièces appliqué.

    Lire l'OVERLAY seul ferait dire à cet outil qu'un code est « complet » alors
    que `build_audit.py` l'a déjà reclassé faute de pièces. Deux instruments qui
    mesurent la même chose doivent donner le même chiffre — règle d'or n°228.
    """
    fiche = OVERLAY.get("%s_%s" % (niveau, code)) or {}
    tenu, _absents, _phrase = verdict(fiche.get("statut", ""), dossier_absolu,
                                      fiche.get("mutualise_avec", ""))
    return tenu


def parcourir():
    lignes = []
    for niveau, comp in COMP_BY_LEVEL.items():
        for parent, sous in comp.items():
            for code, texte, _dom in sous:
                dossier = os.path.abspath(os.path.join(RACINE, code_dir(parent, niveau, code)))
                fait = examiner(niveau, code, dossier)
                fait.update(niveau=niveau, code=code, parent=parent,
                            libelle="%s_%s" % (niveau, code),
                            statut=statut_tenu(niveau, code, dossier),
                            texte=texte)
                lignes.append(fait)
    return lignes


ORDRE = {"ÉVALUÉ": 0, "CITÉ": 1, "RENVOI": 2, "NON NOMMÉ": 3, "VIDE": 4}

#: états qui ne portent aucune preuve dans le lot lui-même
SANS_PREUVE = ("RENVOI", "NON NOMMÉ")

#: le seul état où la couverture d'un code est mesurable
MESURABLE = "ÉVALUÉ"


def main():
    muets_seuls = "--muets" in sys.argv
    lignes = parcourir()

    if not muets_seuls:
        for l in sorted(lignes, key=lambda l: (l["niveau"], l["parent"], l["code"])):
            if l["etat"] == "VIDE":
                continue
            q = ("%d question(s)" % l["questions"]) if l["questions"] else "aucune question"
            print("%-9s %-9s %s" % (l["libelle"], l["etat"], q))
            if l["ou"]:
                print("            écrit dans : %s" % ", ".join(l["ou"][:4]))
            elif l["renvois"]:
                print("            renvoi seul : %s" % ", ".join(l["renvois"][:4]))

    muets = [l for l in lignes
             if l["etat"] != MESURABLE and "VALIDABLE" in (l["statut"] or "")]
    print("\n%d code(s) tenu(s) pour complets dont la couverture n'est pas "
          "mesurable dans le lot :" % len(muets))
    for l in sorted(muets, key=lambda l: l["libelle"]):
        preuve = (l["ou"] or l["renvois"] or ["—"])[0]
        print("  %-9s %-7s %d question(s)  → %s"
              % (l["libelle"], l["etat"], l["questions"], preuve))
        for banque, tags in l["etiquettes"].items():
            detail = " ".join("%s:%d" % (e, n) for e, n in sorted(tags.items()))
            print("            %s → %s" % (banque, detail))

    etrangeres = [l for l in lignes if l["etiquettes"] and l["etat"] != "ÉVALUÉ"]
    if etrangeres:
        print("\nBanques dont les étiquettes ne sont pas des codes :")
        for l in sorted(etrangeres, key=lambda l: l["libelle"]):
            for banque, tags in l["etiquettes"].items():
                detail = " ".join("%s:%d" % (e, n) for e, n in sorted(tags.items()))
                print("  %-9s %-46s %s" % (l["libelle"], banque[:46], detail))

    from collections import Counter
    stats = Counter(l["etat"] for l in lignes)
    print("\n%d codes : %s" % (len(lignes), "  ".join(
        "%s %d" % (e, stats[e]) for e in sorted(stats, key=lambda e: ORDRE[e]))))

    for i, arg in enumerate(sys.argv):
        if arg == "--json" and i + 1 < len(sys.argv):
            with open(sys.argv[i + 1], "w", encoding="utf-8") as f:
                json.dump(lignes, f, ensure_ascii=False, indent=2)
            print("écrit : %s" % sys.argv[i + 1])

    return 0


if __name__ == "__main__":
    sys.exit(main())
