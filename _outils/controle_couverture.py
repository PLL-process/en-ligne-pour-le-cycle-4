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

    ÉVALUÉ      au moins SEUIL_EVALUABLE questions du QCM du lot se rattachent
                à ce code, et à lui seul — la couverture est mesurable
    PARTAGÉ     le seuil est atteint, mais par un groupe de questions que le
                code partage avec d'autres (« Information — C4.4 · C4.5 · C4.6 »)
    CITÉ        le code est écrit dans une pièce qui enseigne ou qui atteste
                (séquence, fiche, matrice, synthèse) mais aucune question ne
                le porte en nombre suffisant
    RENVOI      le code n'apparaît que dans une pièce d'orientation — README,
                manifeste, lexique. Le lot dit où aller, il ne montre rien.
    NON NOMMÉ   le lot porte des fichiers et ne nomme jamais son propre code
    VIDE        rien à lire

Deux distinctions font tout le travail, et l'outil est né sans elles.

**RENVOI / CITÉ.** Depuis que `pointeurs_codes.py` écrit un README dans chaque
dossier, *tout* code est « nommé » quelque part. Compter ces README comme des
preuves rendait l'outil aveugle le jour de sa naissance : il validait la trace
de l'outil de la veille. D'où la séparation entre les pièces qui enseignent ou
attestent et celles qui orientent.

**L'étiquette et sa légende.** Le gabarit maison n'écrit pas le code dans le
champ `c:` de chaque question : il écrit un mot de groupe (`PAR`, `SIM`, `ID`)
et le rattache à son code dans le dictionnaire `COMP_LABELS` de la banque. La
première version de cet outil ne lisait que `c:` et a conclu que sept banques
ne nommaient aucun code. Elles le nommaient toutes, une ligne plus haut. Un
instrument qui ne regarde pas là où la chose est écrite ne mesure pas une
absence : il mesure sa propre myopie (règle d'or n°242).

Une légende peut aussi ne nommer AUCUN code du programme — `"SEU":"CRCN 3.4 ·
1.3 · 5.1"`. Ce groupe déclare travailler hors référentiel ; c'est une
information sur le lot, pas un manque, et l'outil le range à part.

Enfin, un code mutualisé ne porte pas ses questions : elles vivent dans la
banque du lot qui l'enseigne. L'outil indexe donc TOUTES les banques du dépôt
et sait dire, pour chaque renvoi, où il est effectivement évalué — ou qu'il ne
l'est nulle part.

Règle d'or n°237 : compter les pièces n'est pas vérifier la couverture.
Règle d'or n°238 : la preuve d'une couverture est une ligne, pas un dossier.
Règle d'or n°242 : un instrument ne prouve une absence que là où il a regardé.

Usage :
    python3 _outils/controle_couverture.py             # rapport complet
    python3 _outils/controle_couverture.py --muets     # les seuls cas litigieux
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


def legende_de_banque(chemin):
    """Le dictionnaire `COMP_LABELS` d'une banque : étiquette → libellé affiché.

    C'est là que le gabarit maison écrit à quel code chaque groupe se rattache —
    `"PAR":"4e_C8.1 — Paramétrer la simulation"`. Une première version de cet
    outil ne lisait que le champ `c:` et concluait que sept banques ne nommaient
    aucun code. Elles le nommaient toutes, dans leur légende : l'instrument
    regardait à côté (règle d'or n°242).
    """
    t = _texte(chemin)
    m = re.search(r"COMP_LABELS\s*=\s*\{", t)
    if not m:
        return {}
    fin = t.find("}", m.end())
    if fin < 0:
        return {}
    return dict(re.findall(r'"([^"]+)"\s*:\s*"([^"]*)"', t[m.end():fin]))


def codes_de_letiquette(etiquette, libelle, niveau):
    """Les codes qu'une étiquette revendique — par elle-même ou par sa légende.

    Une légende peut en nommer plusieurs (« Information — 4e_C4.4 · C4.5 · C4.6 ») :
    les questions du groupe sont alors PARTAGÉES, jamais comptées en plein pour
    chacun. Une légende peut aussi n'en nommer aucun (« CRCN 3.4 · 1.3 · 5.1 ») :
    le groupe déclare alors travailler hors du référentiel du programme, et c'est
    une information, pas un manque.
    """
    trouves = re.findall(r"(?<![A-Za-z0-9.])(?:%s[ _-])?(C\d\.\d)(?!\d)"
                         % re.escape(niveau), "%s %s" % (etiquette, libelle))
    return sorted(set(trouves))


def questions_portant(chemin, niveau, code):
    """(questions exclusives, questions partagées) portées par une banque.

    Exclusives : le groupe ne revendique que ce code. Partagées : le groupe
    revendique ce code avec d'autres — la couverture est réelle mais diluée.
    """
    mot = _motif(niveau, code)
    legende = legende_de_banque(chemin)
    seul = partage = 0
    for etiquette, n in etiquettes_de_banque(chemin).items():
        codes = codes_de_letiquette(etiquette, legende.get(etiquette, ""), niveau)
        if not codes:
            # pas de légende exploitable : on s'en tient à l'étiquette elle-même
            if mot.search(etiquette):
                seul += n
            continue
        if code not in codes:
            continue
        if len(codes) == 1:
            seul += n
        else:
            partage += n
    return seul, partage


NIVEAUX = ("5e", "4e", "3e")


def _niveau_du_chemin(chemin):
    for part in chemin.replace(os.sep, "/").split("/"):
        if part in NIVEAUX:
            return part
    return ""


def banques_du_depot():
    """Où, dans TOUT le dépôt, chaque code est-il évalué ?

    Un code mutualisé ne porte pas ses questions : elles vivent dans la banque du
    lot qui l'enseigne. Ne regarder que son propre dossier ferait dire « aucune
    preuve » d'un renvoi parfaitement tenu. On indexe donc les banques une fois,
    et chaque renvoi devient vérifiable au lieu d'être seulement présent.

    Renvoie {(niveau, code): [(chemin relatif, n questions, partagé), …]}.
    """
    index = {}
    for racine, sous, noms in os.walk(RACINE):
        sous[:] = [d for d in sous if d not in IGNORES and not d.startswith(".")]
        for nom in noms:
            if not (nom.lower().startswith("qcm") and nom.lower().endswith(".html")):
                continue
            chemin = os.path.join(racine, nom)
            compte = etiquettes_de_banque(chemin)
            if not compte:
                continue
            niveau_dossier = _niveau_du_chemin(chemin)
            legende = legende_de_banque(chemin)
            rel = os.path.relpath(chemin, RACINE).replace(os.sep, "/")
            for etiquette, n in compte.items():
                source = "%s %s" % (etiquette, legende.get(etiquette, ""))
                trouves = re.findall(r"(?<![A-Za-z0-9.])(?:(5e|4e|3e)[ _-])?(C\d\.\d)(?!\d)",
                                     source)
                codes = sorted({(niv or niveau_dossier, c) for niv, c in trouves})
                for cle in codes:
                    if not cle[0]:
                        continue
                    index.setdefault(cle, []).append((rel, n, len(codes) > 1))
    return index


def examiner(niveau, code, dossier_absolu):
    """Où ce lot nomme-t-il son propre code ? Renvoie un dictionnaire de faits."""
    fichiers = _fichiers_du_lot(dossier_absolu)
    if not fichiers:
        return dict(etat="VIDE", questions=0, partagees=0, ou=[], renvois=[],
                    etiquettes={}, hors_referentiel={}, fichiers=0)

    mot = _motif(niveau, code)
    pieces = pieces_du_lot(dossier_absolu)

    questions = partagees = 0
    etiquettes, hors = {}, {}
    for nom in pieces["qcm"] + pieces["qcm_herite"]:
        chemin = os.path.join(dossier_absolu, nom)
        seul, part = questions_portant(chemin, niveau, code)
        questions += seul
        partagees += part
        legende = legende_de_banque(chemin)
        for e, n in etiquettes_de_banque(chemin).items():
            codes = codes_de_letiquette(e, legende.get(e, ""), niveau)
            if not codes and not mot.search(e):
                # aucune légende, ou une légende qui ne nomme aucun code
                cible = hors if e in legende else etiquettes
                cible.setdefault(nom, {})[e] = n

    ou, renvois = [], []
    for chemin in fichiers:
        if not mot.search(_texte(chemin)):
            continue
        rel = os.path.relpath(chemin, dossier_absolu).replace(os.sep, "/")
        (renvois if ORIENTATION.search(rel) else ou).append(rel)

    if questions >= SEUIL_EVALUABLE:
        etat = "ÉVALUÉ"
    elif questions + partagees >= SEUIL_EVALUABLE:
        etat = "PARTAGÉ"
    elif ou:
        etat = "CITÉ"
    elif renvois:
        etat = "RENVOI"
    else:
        etat = "NON NOMMÉ"

    return dict(etat=etat, questions=questions, partagees=partagees,
                ou=ou, renvois=renvois, etiquettes=etiquettes,
                hors_referentiel=hors, fichiers=len(fichiers))


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
    index = banques_du_depot()
    lignes = []
    for niveau, comp in COMP_BY_LEVEL.items():
        for parent, sous in comp.items():
            for code, texte, _dom in sous:
                dossier = os.path.abspath(os.path.join(RACINE, code_dir(parent, niveau, code)))
                fait = examiner(niveau, code, dossier)
                propre = code_dir(parent, niveau, code).replace(os.sep, "/")
                ailleurs = [(rel, n, part) for rel, n, part in index.get((niveau, code), [])
                            if not rel.startswith(propre + "/")]
                fait.update(niveau=niveau, code=code, parent=parent,
                            libelle="%s_%s" % (niveau, code),
                            statut=statut_tenu(niveau, code, dossier),
                            ailleurs=ailleurs,
                            questions_ailleurs=sum(n for _r, n, _p in ailleurs),
                            texte=texte)
                lignes.append(fait)
    return lignes


ORDRE = {"ÉVALUÉ": 0, "PARTAGÉ": 1, "CITÉ": 2, "RENVOI": 3,
         "NON NOMMÉ": 4, "VIDE": 5}

#: états qui ne portent aucune preuve dans le lot lui-même
SANS_PREUVE = ("RENVOI", "NON NOMMÉ")

#: états où la couverture d'un code est démontrée par des questions
MESURABLES = ("ÉVALUÉ", "PARTAGÉ")


def main():
    muets_seuls = "--muets" in sys.argv
    lignes = parcourir()

    if not muets_seuls:
        for l in sorted(lignes, key=lambda l: (l["niveau"], l["parent"], l["code"])):
            if l["etat"] == "VIDE":
                continue
            q = ("%d question(s)" % l["questions"]) if l["questions"] else "aucune question"
            if l["partagees"]:
                q += " + %d partagée(s)" % l["partagees"]
            print("%-9s %-9s %s" % (l["libelle"], l["etat"], q))
            if l["ou"]:
                print("            écrit dans : %s" % ", ".join(l["ou"][:4]))
            elif l["renvois"]:
                print("            renvoi seul : %s" % ", ".join(l["renvois"][:4]))
            if l["ailleurs"]:
                print("            évalué ailleurs : %s" % " · ".join(
                    "%s (%d%s)" % (rel.split("/")[-1], n, " partagées" if part else "")
                    for rel, n, part in l["ailleurs"][:3]))

    muets = [l for l in lignes
             if l["etat"] not in MESURABLES and "VALIDABLE" in (l["statut"] or "")]
    print("\n%d code(s) tenu(s) pour complets dont la couverture n'est pas "
          "démontrée par des questions :" % len(muets))
    for l in sorted(muets, key=lambda l: l["libelle"]):
        preuve = (l["ou"] or l["renvois"] or ["—"])[0]
        print("  %-9s %-7s %d question(s)  → %s"
              % (l["libelle"], l["etat"], l["questions"], preuve))
        for banque, tags in l["etiquettes"].items():
            detail = " ".join("%s:%d" % (e, n) for e, n in sorted(tags.items()))
            print("            %s → %s" % (banque, detail))

    orphelins = [l for l in lignes if l["etat"] in SANS_PREUVE
                 and not l["questions_ailleurs"] and l["statut"]
                 and "MUTUALIS" in l["statut"]]
    print("\n%d renvoi(s) que rien n'évalue nulle part :" % len(orphelins))
    for l in sorted(orphelins, key=lambda l: l["libelle"]):
        print("  %-9s %s" % (l["libelle"], l["texte"][:78]))

    etrangeres = [l for l in lignes if l["etiquettes"]]
    if etrangeres:
        print("\nÉtiquettes sans code ET sans légende qui en nomme un :")
        for l in sorted(etrangeres, key=lambda l: l["libelle"]):
            for banque, tags in l["etiquettes"].items():
                detail = " ".join("%s:%d" % (e, n) for e, n in sorted(tags.items()))
                print("  %-9s %-46s %s" % (l["libelle"], banque[:46], detail))

    hors = [l for l in lignes if l["hors_referentiel"]]
    if hors:
        print("\nGroupes que leur propre légende déclare HORS du référentiel :")
        for l in sorted(hors, key=lambda l: l["libelle"]):
            for banque, tags in l["hors_referentiel"].items():
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
