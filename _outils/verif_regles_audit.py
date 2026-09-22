#!/usr/bin/env python3
"""Vérificateur des règles d'or mécanisables du dépôt.

PÉRIMÈTRE DE CE CONTRÔLE (règle n°47 — un contrôle déclare ce qu'il regarde).

Mécanisé, donc établi : n°23, n°26, n°29, n°30, n°31, n°33, n°34, n°42, n°47,
n°51, n°53, n°54, n°67 et n°298 — la liste exacte est imprimée en fin d'exécution.

NON mécanisable, donc NON couvert, et à faire à l'œil : la justesse pédagogique
des contenus et des corrigés, la progressivité réelle, l'ergonomie en classe, et
les règles n°24, n°25, n°27, n°28 et n°32 qui relèvent du jugement.

Une règle qu'on ne peut pas vérifier est une règle qui meurt. Ce script contrôle,
sur toute séquence HTML du dépôt, les règles mécanisables :

  n°23  durée annoncée ≥ somme des durées d'activités (+ marge de service)
  n°26  diagnostic d'entrée sans note quand la page invoque l'année précédente
  n°29  mode essentiel présent
  n°30  bandeau/tableau de bord des tâches quand il y a plusieurs tâches
  n°31  version étayée proposée pour chaque production écrite exigée
  n°33  aération : pas de pavé de texte trop long dans un même bloc
  n°34  accessibilité statique : étiquettes de select, alternatives d'images,
        pas de signalement par la seule couleur, champs de rédaction suffisants
  n°42  formulations du référentiel recopiées — lues dans la synthèse professeur du
        lot depuis la n°298 (15/09/2026), et encore sur la page tant qu'elle n'est pas migrée
  n°51  le titre AFFICHÉ ne porte aucune trace du lot d'origine du gabarit
  n°53  une notion à voisine proche n'est pas définie par sa voisine
  n°54  un nombre annoncé sur un autre fichier correspond au fait
  n°67  une consigne de production s'accompagne d'un champ de saisie
  n°298 la page élève ne porte ni le référentiel « en toutes lettres » ni la légende
        des étiquettes : ils vont dans la synthèse professeur

Les règles n°24, n°25, n°27, n°28 et n°32 relèvent du jugement pédagogique :
le script les SIGNALE pour relecture humaine, il ne les tranche pas. Il ne dit
jamais « conforme » sur ce qu'il n'a pas réellement mesuré (barre qualité du dépôt).

Usage :
    python _outils/verif_regles_audit.py                  # tout le dépôt
    python _outils/verif_regles_audit.py theme-2-*/       # un sous-arbre
    python _outils/verif_regles_audit.py --json           # sortie machine
"""
from __future__ import annotations

import html
import json
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import data_competences as dc  # noqa: E402  (le chemin doit être posé avant)
import panne  # noqa: E402

RACINE = pathlib.Path(__file__).resolve().parent.parent

# Marge de service : lancement du logiciel, transitions, synthèse, bilan.
# L'audit reproche précisément de l'avoir oubliée.
MARGE_SERVICE_MIN = 10

SEUIL_PAVE_MOTS = 110  # au-delà, un <p> mérite d'être scindé (règle n°33)
SEUIL_PAVE_SIGNAL = 3  # nombre de pavés toléré avant de lever l'alerte


def texte_visible(src: str) -> str:
    sans_script = re.sub(r"<(script|style)\b.*?</\1>", " ", src, flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", sans_script)))


def duree_annoncee(src: str) -> int | None:
    """Minutes disponibles d'après le badge « N séances de M min »."""
    m = re.search(r"(\d+)\s*s[ée]ances?\s+de\s+(\d+)\s*min", texte_visible(src), re.I)
    return int(m.group(1)) * int(m.group(2)) if m else None


def durees_activites(src: str) -> list[int]:
    """Minutes annoncées activité par activité (~45 min, 30 min, 5 min…)."""
    return [int(x) for x in re.findall(r"[(~≈]\s*(\d+)\s*min", texte_visible(src))]


def regle_23(src: str) -> tuple[str, str]:
    dispo, parts = duree_annoncee(src), durees_activites(src)
    if dispo is None:
        return "INCONNU", "aucun badge « N séances de M min » trouvé"
    if not parts:
        return "INCONNU", "aucune durée d'activité annoncée"
    total = sum(parts)
    detail = f"{total} min annoncés (+{MARGE_SERVICE_MIN} de service) pour {dispo} disponibles"
    if total + MARGE_SERVICE_MIN > dispo:
        return "ECHEC", detail + f" — dépassement de {total + MARGE_SERVICE_MIN - dispo} min"
    return "OK", detail


ORDRE_NIVEAUX = {"6e": 0, "5e": 1, "4e": 2, "3e": 3}


def texte_de_consigne(src: str) -> str:
    """Texte réellement lu par l'élève dans le fil de la page.

    On retire ce qui n'est pas de la consigne : les `option` (ce sont des distracteurs,
    souvent faux par construction) et les corrections repliées (elles commentent APRÈS
    coup, et disent volontiers « en 5e c'était fourni, en 3e tu l'élabores »).
    Corrigé le 08/08/2026 : sans ce filtre, la règle n°26 signalait cinq séquences dont
    quatre n'invoquaient rien du tout.
    """
    t = re.sub(r"<option\b.*?</option>", " ", src, flags=re.S | re.I)
    t = re.sub(r'<details class="correction".*?</details>', " ", t, flags=re.S | re.I)
    return texte_visible(t)


def regle_26(src: str, niveau: str | None = None) -> tuple[str, str]:
    t = texte_de_consigne(src)
    rang = ORDRE_NIVEAUX.get(niveau or "", 99)
    # On ne retient QUE les niveaux antérieurs à celui de la séquence : citer son propre
    # niveau (« en 4e, on ne reçoit plus le protocole ») n'est pas invoquer un prérequis,
    # et citer un niveau postérieur (« tu la reverras en 3e ») encore moins.
    anterieurs = [n for n, r in ORDRE_NIVEAUX.items() if r < rang]
    motif = "|".join([rf"\ben {n}\b" for n in anterieurs] + [r"l'an dernier", r"l'année dernière"])
    if not anterieurs or not re.search(motif, t, re.I):
        return "SANS OBJET", "la page ne s'appuie pas sur une année antérieure"
    a_diag = ("passeport" in t.lower() or "billet d'entrée" in t.lower()) and "sans note" in t.lower()
    return ("OK", "diagnostic d'entrée sans note présent") if a_diag else (
        "ECHEC", "la page invoque une année antérieure sans diagnostic d'entrée sans note")


def regle_29(src: str) -> tuple[str, str]:
    if 'id="btnEssentiel"' not in src:
        return "ECHEC", "pas de bouton « mode essentiel »"
    if "body.essentiel" not in src:
        return "ECHEC", "bouton présent mais aucune règle CSS body.essentiel"
    return "OK", "mode essentiel présent et câblé"


def regle_30(src: str) -> tuple[str, str]:
    n_act = len(re.findall(r'data-check="\d+"', src))
    if n_act < 2:
        return "SANS OBJET", "moins de deux tâches vérifiées"
    if re.search(r'id="tachesBandeau"|class="[^"]*taches-bandeau', src):
        return "OK", "tableau de bord des tâches présent"
    return "ECHEC", f"{n_act} tâches enchaînées sans tableau de bord"


def regle_31(src: str) -> tuple[str, str]:
    """Version étayée pour chaque production écrite exigée.

    RETOURNEMENT du 09/08/2026 : cette règle passait « SANS OBJET » — donc au
    vert — devant une page sans la moindre zone de rédaction. Une séquence vide
    se notait ainsi mieux qu'une séquence imparfaite. Or une page qui n'exige
    aucune production n'est pas dispensée de la règle : elle est en défaut sur
    la n°67, et on le dit ici plutôt que de se taire."""
    n_textarea = len(re.findall(r"<textarea\b", src))
    if n_textarea == 0:
        if re.search(VERBES_PRODUCTION, norm(texte_visible(src))):
            return "ECHEC", ("aucune zone de rédaction, alors que la page annonce une production "
                             "— voir aussi n°67")
        return "SANS OBJET", "aucune production écrite exigée (et aucune annoncée)"
    n_etaye = len(re.findall(r"[Vv]ersion étayée", src))
    if n_etaye == 0:
        return "ECHEC", f"{n_textarea} zone(s) de rédaction, aucune version étayée"
    return "OK", f"{n_etaye} version(s) étayée(s) pour {n_textarea} zone(s) de rédaction"


def regle_33(src: str) -> tuple[str, str]:
    pavés = []
    for m in re.finditer(r"<p\b[^>]*>(.*?)</p>", src, re.S | re.I):
        mots = len(texte_visible(m.group(1)).split())
        if mots > SEUIL_PAVE_MOTS:
            pavés.append(mots)
    if not pavés:
        return "OK", "aucun pavé au-delà du seuil"
    if len(pavés) <= SEUIL_PAVE_SIGNAL:
        return "ALERTE", f"{len(pavés)} pavé(s) longs ({', '.join(map(str, sorted(pavés, reverse=True)))} mots)"
    return "ECHEC", f"{len(pavés)} pavés de plus de {SEUIL_PAVE_MOTS} mots — texte à aérer"


def regle_34(src: str) -> tuple[str, str]:
    manques = []
    ids_labels = set(re.findall(r'<label[^>]*\bfor=["\']([^"\']+)["\']', src))
    # TOUT select / textarea est jugé, qu'il ait un id ou non (22/09/2026, n°306) : la règle
    # sautait les champs sans id — elle était aveugle à ceux-là, et 42 zones de 3e_C1.5 sans
    # étiquette ne lui sont apparues qu'une fois leurs ids figés (#421). Quatre façons d'être
    # étiqueté : label for (si id), label englobant, aria-label, aria-labelledby.
    # Les scripts et commentaires sont masqués : un « <textarea> » écrit dans une chaîne JS
    # n'est pas un champ de la page.
    visible = re.sub(r"<script\b.*?</script>|<!--.*?-->", lambda m: " " * len(m.group(0)), src, flags=re.S | re.I)
    # La balise ENTIÈRE est nécessaire : aria-label peut suivre l'attribut id.
    # (Corrigé le 08/08/2026 : l'expression s'arrêtait à id= et signalait comme
    #  « sans étiquette » des champs qui portaient bien un aria-label.)
    for m in re.finditer(r"<(select|textarea)\b[^>]*>", visible, re.I):
        balise = m.group(0)
        ident = re.search(r'\bid=["\']([^"\']+)["\']', balise)
        if ident and ident.group(1) in ids_labels:
            continue
        if re.search(r'\baria-label(?:ledby)?\s*=\s*["\'][^"\']', balise):
            continue
        avant = visible[:m.start()].lower()
        if avant.rfind("<label") > avant.rfind("</label>"):
            continue                                   # label englobant
        nom = f"{m.group(1)}#{ident.group(1)}" if ident else f"{m.group(1)} sans id (ligne {src.count(chr(10), 0, m.start()) + 1})"
        manques.append(f"{nom} sans étiquette")
    for m in re.finditer(r"<img\b[^>]*>", src):
        if not re.search(r'\balt="[^"]+"', m.group(0)):
            manques.append("image sans alternative textuelle")
    if re.search(r"\.ok\s*\{[^}]*color", src) and "✔" not in src and "✓" not in src:
        manques.append("réussite signalée par la seule couleur")
    if not manques:
        return "OK", "étiquettes, alternatives et signalement non chromatique en place"
    return "ECHEC", " · ".join(manques[:4]) + (f" (+{len(manques) - 4})" if len(manques) > 4 else "")


# Règles de jugement : on signale, on ne tranche pas.
def signalements(src: str) -> list[str]:
    t = texte_visible(src)
    out = []
    if re.search(r"\b0\s*%\s*loss\b", t) and "de ce test" not in t and "pendant ce ping" not in t:
        out.append("n°27 : « 0 % loss » sans bornage au test en cours")
    if re.search(r"mesures? réelles?", t) and "réellement observ" not in t:
        out.append("n°27 : « mesures réelles » — préciser qu'il s'agit d'une simulation")
    if re.search(r"\b\d+\s*bonnes? réponses?\b", t) and "situation" not in t.lower():
        out.append("n°28 : critère de réussite exprimé en nombre de bonnes réponses")
    if "Add Simple PDU" in t or "IP Configuration" in t:
        if len(re.findall(r"<img\b", src)) < 6:
            out.append("n°32 : gestes logiciels peu illustrés (triptyque où/quoi/observer)")
    return out


# ── Règle n°42 : la formulation d'une compétence se recopie, elle ne se reformule pas ──
#
# Second volet de la règle n°36. Le premier volet interdit de faire passer un code de
# classement interne pour une nomenclature officielle ; celui-ci interdit de réécrire le
# TEXTE d'une compétence. La reformulation est plus discrète, et plus profonde : le lot
# 5e_C2 a enseigné « esthétique » là où le programme dit « développement durable », et
# quarante-trois tests l'ont laissé passer.
#
# Ce qu'on coupe en premier, c'est la parenthèse — et c'est souvent la parenthèse qui fixe
# le niveau : « à partir d'un protocole DONNÉ » (4e) contre « DÉFINIR un protocole » (3e).

FORMULATIONS = {}
for _niv, _table in (("5e", dc.COMP_5E), ("4e", dc.COMP_4E), ("3e", dc.COMP_3E)):
    for _parent, _lignes in _table.items():
        for _code, _texte, _socle in _lignes:
            FORMULATIONS[(_niv, _code)] = _texte

# Mots que la carte peut légitimement ne pas reprendre : le dépôt développe « OST » en
# « objet ou système technique », ce qui est une explicitation, pas une reformulation.
MOTS_TOLERES = {"technique", "techniques", "systeme", "systemes", "objet", "objets"}


def _pivot(t: str) -> set[str]:
    """Mots porteurs de sens d'un texte, accents et balises retirés."""
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[’']", "'", t).lower()
    return set(re.findall(r"[a-z]{5,}", t))


def _synthese_professeur(chemin: pathlib.Path | None) -> pathlib.Path | None:
    if chemin is None:
        return None
    d = chemin.parent
    c = sorted(d.glob("Synth*/synthese_professeur*.html")) + sorted(d.glob("synthese_professeur*.html"))
    return c[0] if len(c) == 1 else None


def regle_42(src: str, chemin: pathlib.Path | None = None) -> tuple[str, str]:
    # Depuis la règle d'or n°298 (15/09/2026), le référentiel vit dans la synthèse
    # professeur, dans un bloc `referentiel-eleve`. Une page pas encore migrée est
    # encore lue sur place — et la n°298 la signale.
    m = re.search(r"referentiel-card.*?</table>", src, re.S)
    ou = "carte"
    if not m:
        synth = _synthese_professeur(chemin)
        if synth is not None:
            m = re.search(r"referentiel-eleve.*?</table>", synth.read_text(encoding="utf-8"), re.S)
            ou = "synthèse professeur"
    if not m:
        return "SANS OBJET", "ni la page ni sa synthèse professeur ne portent de tableau de référentiel"
    ecarts, lus = [], 0
    for tr in re.findall(r"<tr>(?!\s*<th).*?</tr>", m.group(0), re.S):
        cm = re.search(r"\b(\de)_(C\d+\.\d+)\b", tr)
        if not cm:
            continue
        cle = (cm.group(1), cm.group(2))
        if cle not in FORMULATIONS:
            continue
        cellules = re.findall(r"<td>(.*?)</td>", tr, re.S)
        if len(cellules) < 2:
            continue
        lus += 1
        manque = _pivot(FORMULATIONS[cle]) - _pivot(cellules[1]) - MOTS_TOLERES
        if manque:
            ecarts.append(f"{cm.group(0)} (absents : {', '.join(sorted(manque))})")
    if not lus:
        return "SANS OBJET", f"aucun code reconnu dans le référentiel ({ou})"
    if ecarts:
        return "ECHEC", f"formulation réécrite ou tronquée ({ou}) — " + " ; ".join(ecarts)
    return "OK", f"les {lus} formulation(s) du référentiel ({ou}) sont celles du programme"


# ── Règle n°298 : la page élève ne se lit pas comme un référentiel ──
#
# Constat de Pascal, le 15/09/2026, après expérimentation en classe : les élèves se
# perdent. La légende « Ce que disent ces étiquettes » et le référentiel « en toutes
# lettres » ajoutaient une lecture de codes et d'étiquettes à des lecteurs fragiles, sans
# rien leur apprendre. La page élève garde la ligne d'étiquettes sous le titre (avec leurs
# infobulles) ; le référentiel part, tel quel, dans la synthèse professeur. La n°298
# remplace sur la page élève les n°35, n°36, n°42 et le troisième élément de la n°44.

# Le référentiel a trois habits dans le dépôt : un titre « Référentiel… », un titre « Ce que dit le
# programme… » ou « … compétences travaillées — en toutes lettres », et la classe `referentiel-card`
# que le gabarit pose sur l'un ou l'autre. Mesuré le 15/09/2026 : 22 pages par le seul premier habit,
# 9 de plus par les deux autres. Un contrôle qui n'en regarde qu'un laisse passer le tiers du problème.
REFERENTIEL_ELEVE = re.compile(
    r'class="[^"]*(?<![\w-])referentiel-card(?![\w-])'
    r'|<(?:section|div)\b[^>]*class="[^"]*\b(?:card|carte|panel)\b[^"]*"[^>]*>\s*<h2[^>]*>[^<]*'
    r'(?:[Rr]éférentiel|Ce que dit le programme|Compétences\s*(?:&amp;|&)\s*connaissances|compétences travaillées\s*—\s*en toutes lettres)', re.S)


def regle_298(src: str) -> tuple[str, str]:
    trouve = []
    if REFERENTIEL_ELEVE.search(src):
        trouve.append("le référentiel « en toutes lettres »")
    if 'class="legende-badges"' in src:
        trouve.append("la légende des étiquettes")
    if trouve:
        return "ECHEC", "la page élève porte " + " et ".join(trouve) + " : à déplacer dans la synthèse professeur"
    return "OK", "ni référentiel ni légende des étiquettes sur la page élève"


#: Un champ de question posé par une liste déroulante. On ne cherche pas à
#: distinguer « liste de question » et « liste d'interface » : mesuré le
#: 20/09/2026 sur les 60 séquences du dépôt, il n'existe AUCUNE liste
#: d'interface — les 1 492 `<select>` relevés portaient tous une question, y
#: compris les douze qui n'avaient pas d'étiquette rattachable (ils vivaient
#: dans des cellules de tableau, avec des propositions pour options). Si une
#: liste d'interface légitime apparaissait un jour, elle serait signalée par ce
#: contrôle, et c'est très bien ainsi : elle mérite d'être discutée, pas
#: exemptée d'avance par une échappatoire que personne n'aurait relue.
LISTE_DEROULANTE = re.compile(r"<select\b[^>]*>", re.I)
IDENTIFIANT_SELECT = re.compile(r'<select\b[^>]*\bid="([^"]+)"', re.I)


def regle_300(src: str) -> tuple[str, str]:
    """n°300 — une question ne se pose pas par un contrôle qui se dessine par-dessus la page.

    Une liste déroulante native n'est pas dessinée dans la page : le système la
    dessine PAR-DESSUS, ancrée au champ, et elle recouvre ce qui l'entoure —
    donc l'énoncé, qui la précède. Un groupe de boutons radio occupe le flux :
    il pousse le contenu au lieu de le couvrir.

    Ce contrôle ne juge QUE la forme du champ. Il ne vérifie ni que l'énoncé est
    dans une <legend>, ni que la valeur transmise est le texte de la
    proposition : ces deux points se lisent à l'œil et au banc du lot, et un
    contrôle qui prétendrait les établir par expression régulière mentirait.
    """
    listes = LISTE_DEROULANTE.findall(src)
    if not listes:
        return "OK", "aucune liste déroulante : les questions occupent le flux de la page"
    ids = IDENTIFIANT_SELECT.findall(src)
    apercu = ", ".join(ids[:6]) + (" …" if len(ids) > 6 else "")
    return "ECHEC", (
        f"{len(listes)} question(s) posée(s) par une liste déroulante"
        + (f" ({apercu})" if ids else "")
        + " — le menu natif se dessine par-dessus l'énoncé ; à convertir en"
        " groupe de boutons radio (gabarit du pilote 3e_C1.1)")




# ═══════════════════ Règles mécanisées le 09/08/2026 ═══════════════════
# Écrites au journal les 8 et 9 août, vérifiées à la main jusqu'ici. Une règle
# qu'on ne peut pas vérifier est une règle qui meurt.

def norm(t: str) -> str:
    """Minuscules, apostrophes droites, accents retirés.

    Le premier jet d'un contrôle cherchait « t'entraîner » avec une apostrophe
    droite et déclarait absents des blocs présents. On normalise une fois pour
    toutes, ici."""
    t = t.replace("\u2019", "'").replace("\u00a0", " ")
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if not unicodedata.combining(c)).lower()


VERBES_PRODUCTION = (r"production attendue|complete le tableau|redige|recense|"
                     r"ecris (?:un|une|le|la|les|deux|trois|quatre|cinq|six|huit)|"
                     r"propose (?:un|une|ton|ta)|justifie|argumentaire de")

# Traces des lots dont le gabarit a été emprunté (règle n°51). Six QCM de
# Thème 1 ont affiché « SOS serre » et Packet Tracer jusqu'au 08/08/2026.
TRACES_GABARIT = ("sos serre", "packet tracer", "adresse ip fixe")

# Notions à voisine proche (règle n°53). La clé est la notion ; la valeur, la
# définition de sa VOISINE — celle qu'il ne faut pas lui donner.
VOISINES = [
    ("fonction technique", r"a quoi (?:cela |ca |il |elle )?sert|dit a quoi (?:ca |cela )?sert",
     "c'est la fonction d'usage : la fonction technique dit ce que l'objet doit FAIRE"),
]


def regle_51(src: str, chemin: pathlib.Path | None = None) -> tuple[str, str]:
    """Ce que l'élève voit en premier annonce le bon niveau et le bon lot.

    Première version fautive : une liste noire de mots (« SOS serre »,
    « Packet Tracer »). Elle accusait les lots qui parlent légitimement de
    Packet Tracer — dont celui qui s'appelle « SOS serre ». Une liste de mots
    ne distingue pas un reste de gabarit d'un sujet réel. On compare donc le
    titre au niveau et aux codes du fichier lui-même."""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", src, re.S | re.I)
    if not m:
        return "ECHEC", "aucun <h1> : la page ne dit pas ce qu'elle est"
    if chemin is None:
        return "SANS OBJET", "chemin inconnu, comparaison impossible"

    attendu = None
    for part in chemin.parts:
        mm = re.fullmatch(r"([345]e)", part)
        if mm:
            attendu = mm.group(1)
    if attendu is None:
        mm = re.search(r"([345]e)_C\d", chemin.name)
        attendu = mm.group(1) if mm else None
    if attendu is None:
        return "SANS OBJET", "niveau du lot indéterminable depuis le chemin"

    tete = texte_visible(m.group(1))
    sub = re.search(r'<p class="(?:subtitle|sous|subtitle-mission)"[^>]*>(.*?)</p>', src, re.S | re.I)
    zone = tete + " " + (texte_visible(sub.group(1)) if sub else "")
    niveaux = set(re.findall(r"\b([345]e)\b", zone))
    intrus = niveaux - {attendu}
    if intrus:
        return "ECHEC", ("le titre affiché annonce %s alors que le lot est en %s"
                         % (", ".join(sorted(intrus)), attendu))
    codes = set(re.findall(r"([345]e)_C\d", zone))
    if codes and codes != {attendu}:
        return "ECHEC", "le titre affiché porte des codes d'un autre niveau : " + ", ".join(sorted(codes))
    return "OK", "titre affiché cohérent avec le niveau du lot (%s)" % attendu


def regle_53(src: str) -> tuple[str, str]:
    """Une notion à voisine proche n'est pas définie par sa voisine."""
    n = norm(texte_visible(src))
    for notion, motif, explication in VOISINES:
        for m in re.finditer(notion + r"[^.]{0,70}", n):
            if re.search(motif, m.group(0)):
                return "ECHEC", "« %s » définie par sa voisine — %s" % (notion, explication)
    return "OK", "aucune notion définie par sa voisine"


def regle_54(src: str, dossier: pathlib.Path | None = None) -> tuple[str, str]:
    """Un nombre annoncé d'un AUTRE fichier correspond au fait."""
    m = re.search(r"(\d+)\s*(?:</b>\s*)?illustr[ée]e", texte_visible(src), re.I)
    if not m or dossier is None:
        return "SANS OBJET", "aucun nombre d'illustrées annoncé"
    annonce = int(m.group(1))
    qcms = [f for f in dossier.glob("qcm_*.html")]
    if not qcms:
        return "ALERTE", "%d illustrées annoncées, aucun QCM dans le dossier" % annonce
    reels = max(len(re.findall(r"img:\{", f.read_text(encoding="utf-8", errors="ignore")))
                for f in qcms)
    if reels == 0:
        return "ALERTE", "%d illustrées annoncées, le QCM n'expose pas ses images au format attendu" % annonce
    if reels != annonce:
        return "ECHEC", "%d illustrées annoncées, %d dans le QCM" % (annonce, reels)
    return "OK", "%d illustrées annoncées, %d dans le QCM" % (annonce, reels)


def regle_67(src: str) -> tuple[str, str]:
    """Une consigne de production s'accompagne d'un champ où produire."""
    n = norm(texte_visible(src))
    if not re.search(VERBES_PRODUCTION, n):
        return "SANS OBJET", "aucune production annoncée"
    champs = len(re.findall(r"<(?:textarea|select|input)\b", src))
    if champs == 0:
        return "ECHEC", "la page annonce une production et n'offre aucun champ de saisie"
    return "OK", "%d champ(s) de saisie pour les productions annoncées" % champs


#: Le bilan qui clôt une séquence. Trois écritures coexistent dans le dépôt : un
#: titre « Je me positionne », un titre « Mon auto-positionnement », et des lots
#: où la phrase ne vit que dans l'invite des champs de positionnement. Les trois
#: valent bilan — c'est la fonction qui compte, pas le libellé. Ne chercher que
#: la première en manquait NEUF sur quarante.
BILAN = re.compile(r"je me positionne|auto[-\s]?positionnement|je me situe|bilan personnel", re.I)

#: Le titre d'un bloc Bonus, quelle que soit sa décoration.
TITRE_BONUS = re.compile(r"<h[1-4][^>]*>(?:(?!</h[1-4]>).)*?\bbonus\b", re.I | re.S)

#: ── Le bilan reconnu à sa FONCTION, et non à ses mots ────────────────────────
#:
#: Un bilan fait une chose : il demande à l'élève de SE SITUER sur les
#: compétences de la séquence. Cela s'écrit toujours de la même façon, quels que
#: soient les mots de l'échelle — émojis, « je sais / pas encore », « maîtrise
#: fragile » :
#:
#:     un groupe de choix mutuellement exclusifs
#:     dont l'intitulé a pour SUJET un code du référentiel
#:     et qui offre au moins trois options.
#:
#: Aucune liste de mots n'entre ici. Chercher « Maîtrise insuffisante » aurait
#: marché aujourd'hui et cassé au premier lot qui écrit son échelle autrement.
#:
#: « Pour sujet » est le point délicat, et il est MESURÉ : deux questions de
#: CONTENU du dépôt citent un code au passage — « Le banc de 3e_C8.2 retenait
#: déjà celui-là », « En 4e_C7, tu as choisi un matériau ». Elles nomment un
#: code sans porter sur lui, et feraient un bilan fantôme. Le discriminant n'est
#: donc pas la présence du code mais sa POSITION SYNTAXIQUE : dans un
#: auto-positionnement le code est suivi d'un tiret, d'un deux-points, d'une
#: parenthèse ou de la fin de l'intitulé ; dans une question de contenu, d'une
#: virgule ou d'un verbe.
_CODE_REF = r"[345]e_C\d+(?:\.\d+)?(?![\d.])"

#: `(?![\d.])` ferme le code. Sans lui, « 3e_C8.2 retenait » se lirait « 3e_C8 »
#: suivi d'un point — et la question de contenu passerait pour un positionnement.
SUJET_CODE = re.compile(
    r"\b" + _CODE_REF
    + r"(?:\s*[·,]\s*C\d+(?:\.\d+)?(?![\d.]))*"
    + r"(?!\s*[,\w])")

GROUPE_CHOIX = re.compile(
    r"<fieldset\b[^>]*>(.*?)</fieldset>|<select\b[^>]*>(.*?)</select>", re.I | re.S)
LEGENDE = re.compile(r"<legend\b[^>]*>(.*?)</legend>", re.I | re.S)
UN_RADIO = re.compile(r'<input[^>]*type="radio"', re.I)
UNE_OPTION = re.compile(r"<option\b", re.I)


def _texte_nu(fragment: str) -> str:
    """Le texte d'un fragment, balises ôtées et entités rendues.

    Les entités comptent : tant que « 5e_C1.2&nbsp;— comparer » n'est pas
    déséchappé, ce qui suit le code est un « & », et la lecture tient du hasard.
    """
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def _corps_lisible(src: str) -> str:
    """La page sans ses scripts, ses styles ni ses commentaires."""
    for motif in (r"<script.*?</script>", r"<style.*?</style>", r"<!--.*?-->"):
        src = re.sub(motif, " ", src, flags=re.S)
    return src


def positionnements(corps: str) -> list[int]:
    """Les positions des groupes d'auto-positionnement de la page.

    `corps` est attendu DÉJÀ nettoyé par `_corps_lisible`.
    """
    trouves = []
    for m in GROUPE_CHOIX.finditer(corps):
        dedans = m.group(1) if m.group(1) is not None else m.group(2)
        if m.group(1) is not None:
            leg = LEGENDE.search(dedans)
            titre = _texte_nu(leg.group(1)) if leg else ""
            options = len(UN_RADIO.findall(dedans))
        else:
            aria = re.search(r'aria-label="([^"]*)"', m.group(0))
            ident = re.search(r'id="([^"]+)"', m.group(0))
            titre = _texte_nu(aria.group(1)) if aria else ""
            if ident and not titre:
                lab = re.search(
                    r'<label[^>]*for="%s"[^>]*>(.*?)</label>' % re.escape(ident.group(1)),
                    corps, re.S)
                titre = _texte_nu(lab.group(1)) if lab else ""
            options = len(UNE_OPTION.findall(dedans))
        if options >= 3 and SUJET_CODE.search(titre):
            trouves.append(m.start())
    return trouves


def marque_du_bilan(src: str) -> tuple[int | None, str]:
    """Où la séquence établit son bilan, et par quoi on l'a reconnu.

    Le « ou » est une nécessité mesurée, pas une prudence : sur les 60
    séquences, 53 portent le libellé, 20 portent la fonction, et les deux
    ensemble en reconnaissent 54. Remplacer le libellé par la fonction en
    perdrait 34 ; garder le libellé seul en perd une — celle qui a rouvert le
    sujet.
    """
    corps = _corps_lisible(src)
    m = BILAN.search(corps)
    groupes = positionnements(corps)
    if m and groupes:
        return min(m.start(), groupes[0]), "au libellé et à sa fonction"
    if m:
        return m.start(), "au libellé"
    if groupes:
        return groupes[0], "à sa fonction (auto-positionnement sur %d code(s))" % len(groupes)
    return None, ""


def regle_301(src: str) -> tuple[str, str]:
    """n°301 — le bilan clôt la séquence ; un Bonus est un travail, il le précède.

    DEUX choses se jugent ici, parce que deux seulement se lisent sûrement dans
    la source : qu'un bilan EXISTE, et qu'aucun Bonus ne vienne APRÈS lui.

    Le bilan se reconnaît à son LIBELLÉ **ou** à sa FONCTION — voir
    `marque_du_bilan`. Chercher le seul libellé accusait à tort
    `4e_C1.1-C1.3_tsinghua_feux`, qui porte un bilan complet sous un simple
    titre « Bilan » : trois groupes de positionnement, un par code, douze
    niveaux à choisir et trois légendes « 📍 ».

    Ce qui n'est PAS jugé ici, et pourquoi :
      · « le Bonus porte-t-il un champ de réponse ? » — il faudrait délimiter le
        bloc du Bonus, donc analyser l'arbre. Une expression régulière qui s'en
        approche fait des faux : essayée, elle attribuait au Bonus les quinze
        champs de la section qui l'accueille dans `4e_C4.1_book-train`. Ce grief
        est mesuré par `audit_cloture_sequence.mjs`, qui lit le DOM.
      · la QUALITÉ d'un corrigé — qu'il traite la question posée, qu'il soit
        juste, qu'il soit utile. Cela se lit.
    """
    ou_bilan, comment = marque_du_bilan(src)
    m_bonus = TITRE_BONUS.search(_corps_lisible(src))

    griefs = []
    if ou_bilan is None:
        griefs.append("aucun bilan : la séquence ne se termine par rien")
    if m_bonus and ou_bilan is not None and m_bonus.start() > ou_bilan:
        griefs.append("le Bonus vient APRÈS le bilan — du travail demandé après la clôture")

    if griefs:
        return "ECHEC", " · ".join(griefs)
    return "OK", ("bilan reconnu %s" % comment
                  + (", et le Bonus le précède" if m_bonus else ", pas de Bonus"))


#: Les éléments où la troisième personne n'a jamais sa place dans une page
#: élève : un titre, un en-tête de colonne, un repli, une légende de groupe, une
#: légende de tableau ou de figure. Le CORPS de la page n'y est pas : la prose
#: demande un jugement, et ce contrôle ne juge que le cas non ambigu.
INTITULE = re.compile(
    r"<(h[1-6]|th|summary|legend|caption|figcaption)\b[^>]*>(.*?)</\1>", re.I | re.S)

#: « l'élève » sous ses deux apostrophes — le dépôt porte la droite (U+0027) ET
#: la typographique (U+2019). N'en chercher qu'une en manquait vingt-cinq.
PARLE_DE_LUI = re.compile(r"[Ll][’']\s?élèves?\b|\b[Ll]es\s+élèves\b", re.I)
#: Le vouvoiement, exclu par mesure : le dépôt tutoie à 23 contre 1.
VOUVOIEMENT = re.compile(r"\b(vous|votre|vos)\b", re.I)


#: ── n°304 : le bloc d'ouverture ────────────────────────────────────────────
#:
#: LE BLOC SE RECONNAÎT À SA FONCTION, pas à un titre — quatre comptes par
#: libellé se sont déjà trompés dans ce dépôt. Mesuré : il s'écrit sous CINQ
#: titres au moins (« Ce que tu as déjà fait », « Ce que tu sais déjà faire —
#: et ce qu'on ne refera pas », « D'où tu viens — la spirale … », « Avant de
#: commencer : à quoi ça sert ? », et une variante en 🔁), et compter le seul
#: paragraphe `.deja` en manquait DIX-NEUF sur cinquante-trois.
#:
#: Deux marques, donc, et la première est structurelle :
#:   · un conteneur de classe `rappel-spiralaire` ;
#:   · à défaut, un titre de la famille 🔄/🔁 qui annonce un retour en arrière,
#:     posé dans la première moitié de la page.
OUVERTURE_CLASSE = re.compile(r'<(section|div|aside)\b[^>]*class="[^"]*rappel-spiralaire', re.I)
OUVERTURE_TITRE = re.compile(
    r"<h[1-4][^>]*>[^<]*[\U0001f504\U0001f501][^<]*"
    r"(?:d\u00e9j\u00e0|d'o\u00f9 tu viens|d\u2019o\u00f9 tu viens|spirale|avant de commencer)",
    re.I)

#: Ce que le bloc ne doit JAMAIS affirmer : une année antérieure…
#: `(?:6|5|4|3)\s*e` et non `6e` : les pages \u00e9crivent souvent \u00ab 5<sup>e</sup> \u00bb,
#: et le texte nu rend alors \u00ab 5 e \u00bb. Le motif strict laissait passer deux blocs
#: qui annon\u00e7aient bel et bien une ann\u00e9e ant\u00e9rieure \u2014 trouv\u00e9 en LISANT les trois
#: blocs que la r\u00e8gle acceptait, pas en relisant le motif.
ANNEE_ANTERIEURE = re.compile(
    # \u00ab l'an dernier \u00bb s'\u00e9crit au MASCULIN : le motif demandait \u00ab derni\u00e8re \u00bb,
    # et ne reconnaissait donc pas la formule la plus courante du d\u00e9p\u00f4t.
    r"\b[Ee]n\s+(?:6|5|4|3)\s*e\b|l['\u2019]an\s+derni(?:er|\u00e8re)|"
    r"depuis la\s+(?:6|5|4)\s*e|ann\u00e9e derni\u00e8re|au cycle\s+3|en cycle\s+3|"
    r"^(?:6|5|4|3)\s*e\s+[\u2014-]", re.I | re.M)

#: … ni ce que l'élève A FAIT, même dans l'année en cours : un élève arrivé en
#: cours d'année ne l'a pas fait non plus.
#: Les participes en `-\u00e9` ne suffisent pas : \u00ab tu as SUIVI la s\u00e9quence \u00bb n'y
#: entre pas, et le cas du banc qui devait \u00e9prouver l'exemption du conditionnel
#: passait pour cette raison-l\u00e0 \u2014 pas pour la bonne. Trouv\u00e9 par MUTATION : en
#: retirant l'exemption, le banc restait vert. Les participes irr\u00e9guliers du
#: domaine sont donc nomm\u00e9s un par un, plut\u00f4t qu'un motif large qui prendrait
#: \u00ab tu as envie \u00bb pour un participe.
DEJA_FAIT = re.compile(
    r"\btu\s+(?:as|avais)\s+(?:d\u00e9j\u00e0\s+)?"
    r"(?:[a-z\u00e0-\u00ff]+\u00e9e?s?|fait|vu|pris|mis|compris|su|appris|construit|"
    r"\u00e9crit|d\u00e9couvert|suivi|choisi|d\u00e9crit|rendu|lu|v\u00e9cu|produit|"
    r"obtenu|retenu|conduit|d\u00e9fini|r\u00e9ussi)\b", re.I)

#: L'affirmation ne prend pas toujours « tu » pour sujet : « le banc de la cour
#: t'a appris que… » dit tout autant ce que l'élève a vécu.
APPRIS_A_TOI = re.compile(
    r"t['’]a\s+(?:appris|montré|entraîné|permis|fait)\b", re.I)

#: Le conditionnel est la forme AUTORISÉE : « si tu l'as suivie… » ne dit pas
#: que l'élève l'a suivie, il lui laisse la question.
CONDITIONNEL = re.compile(r"\b(?:si|au cas o\u00f9|s'il|s\u2019il)\b", re.I)


def bloc_ouverture(corps: str) -> tuple[int, int, str] | None:
    """(début, fin, par quoi on l'a reconnu, position de la marque), ou None."""
    m = OUVERTURE_CLASSE.search(corps)
    marque = "la classe rappel-spiralaire"
    if not m:
        m = OUVERTURE_TITRE.search(corps)
        marque = "un titre de la famille \u2b6f"
        if not m or m.start() > len(corps) * 0.55:
            return None
    # Les BORNES comptent autant que la reconnaissance. Remonter jusqu'au
    # `<section` le plus proche marche sur les pages structurées et avale, sur
    # les pages plates, l'en-tête entier de la page : on citait alors la barre
    # de navigation comme si elle était le bloc, et on aurait pu refuser une
    # page pour une phrase écrite ailleurs. Le conteneur n'est donc retenu que
    # s'il commence PRÈS de la marque ; sinon on part de la marque elle-même.
    debut = corps.rfind("<section", 0, m.start())
    if debut < 0 or m.start() - debut > 1200:
        alt = corps.rfind("<div", 0, m.start())
        debut = alt if alt >= 0 and m.start() - alt <= 1200 else m.start()
    fin = corps.find("</section>", m.start())
    if fin < 0:
        fin = corps.find("</div>", m.start())
    if fin < 0:
        fin = len(corps)
    return debut, min(fin, m.start() + 2500), marque, m.start()


def regle_304(src: str) -> tuple[str, str]:
    """n°304 — le bloc d'ouverture dit ce qui DEVRAIT être en place.

    Pascal change d'établissement chaque année : il n'hérite jamais d'une
    classe qui a suivi ses séquences. « En 4e, à Tsinghua, tu as estimé puis
    comparé » est donc faux pour presque tous ses élèves. Et quand c'est vrai,
    l'affirmation met en défaut celui qui ne l'a pas fait.

    DEUX griefs, et deux seulement, parce que deux seulement se lisent
    sûrement :
      · un marqueur d'ANNÉE ANTÉRIEURE (« En 4e », « L'an dernier »…) ;
      · une affirmation de ce que l'élève A FAIT (« tu as estimé »), sauf au
        conditionnel (« si tu l'as suivie »), qui est la forme autorisée.

    CE QUE CE CONTRÔLE NE VOIT PAS, et ne prétend pas voir :
      · la PERTINENCE des compétences choisies — qu'elles servent vraiment au
        début de cette séquence-là se juge, cela ne se compte pas ;
      · l'EXISTENCE RÉELLE du moyen de rattrapage : un lien vers un lexique
        peut exister et ne rien contenir d'utile ;
      · la JUSTESSE des codes cités : `controle_formulations.py` lit les
        formulations, personne ne lit encore la pertinence d'un code ici ;
      · le NIVEAU visé : qu'une 5e renvoie au cycle 3 et non à la 6e du
        collège relève de la relecture.
    """
    corps = _corps_lisible(src)
    trouve = bloc_ouverture(corps)
    if trouve is None:
        return "OK", "pas de bloc d'ouverture \u2014 rien \u00e0 v\u00e9rifier ici"
    debut, fin, marque, _marque_pos = trouve
    brut = corps[debut:fin]

    # Le TITRE et le TEXTE se jugent s\u00e9par\u00e9ment, et le grief dit lequel parle.
    # \u00ab \ud83d\udd04 Ce que tu as d\u00e9j\u00e0 fait \u00bb est \u00e0 lui seul une affirmation : le confondre
    # avec le corps rendait la mesure tautologique \u2014 une page au corps
    # irr\u00e9prochable aurait \u00e9t\u00e9 refus\u00e9e pour son en-t\u00eate, sans qu'on puisse le
    # savoir. Mesur\u00e9 une fois s\u00e9par\u00e9s : AUCUNE s\u00e9quence n'est refus\u00e9e pour son
    # seul titre, 22 pour leur seul texte, 23 pour les deux.
    #
    # Le titre du bloc est le DERNIER titre qui pr\u00e9c\u00e8de la marque, pas le
    # premier du conteneur : sur les pages structur\u00e9es, la section qui accueille
    # le bloc porte souvent d\u00e9j\u00e0 un `<h2>` de s\u00e9quence, et c'est lui qu'on
    # citait \u00e0 tort.
    titres = [x for x in re.finditer(r"<h[1-4][^>]*>(.*?)</h[1-4]>", brut, re.S)]
    mt = None
    for x in titres:
        if x.start() <= (trouve[3] - debut) + 220:
            mt = x
    if mt is None and titres:
        mt = titres[0]
    titre = _texte_nu(mt.group(1)) if mt else ""
    texte = _texte_nu(brut[mt.end():] if mt else brut)

    def griefs_de(ou: str, t: str) -> list[str]:
        out = []
        m = ANNEE_ANTERIEURE.search(t)
        if m:
            out.append("%s : affirme une ann\u00e9e ant\u00e9rieure \u2014 \u00ab %s \u00bb" % (ou, _extrait(t, m)))
        m = DEJA_FAIT.search(t) or APPRIS_A_TOI.search(t)
        if m and not CONDITIONNEL.search(t[max(0, m.start() - 60):m.start()]):
            out.append("%s : affirme ce que l'\u00e9l\u00e8ve a fait \u2014 \u00ab %s \u00bb" % (ou, _extrait(t, m)))
        return out

    griefs = griefs_de("le titre", titre) + griefs_de("le texte", texte)

    if griefs:
        return "ECHEC", " \u00b7 ".join(griefs)
    return "OK", ("bloc d'ouverture reconnu par %s, sans affirmation sur ce que "
                  "l'\u00e9l\u00e8ve a fait" % marque)


def _extrait(texte: str, m) -> str:
    """La phrase autour d'une trouvaille, bornée pour rester lisible."""
    d = texte.rfind(".", 0, m.start()) + 1
    f = texte.find(".", m.end())
    bout = texte[d:f + 1 if f > 0 else len(texte)].strip()
    return (bout[:120] + "\u2026") if len(bout) > 120 else bout


#: Les exceptions à la n°302, NOMMÉES une par une — jamais une catégorie.
#:
#: Tranché par Pascal le 20/09/2026 : le « vous » de « La mairie vous appelle »
#: est entre guillemets et attribué à un tiers nommé. C'est une PAROLE
#: RAPPORTÉE, pas la voix de la page. La n°302 vise le « vous » institutionnel,
#: celui qui met l'élève à distance ; ici l'élève est DANS la scène.
#:
#: Exprimées par FICHIER + PHRASE, jamais par numéro de ligne : la phrase
#: apparaît aussi dans un <button> d'onglet et dans une chaîne JavaScript de ces
#: mêmes fichiers, et la prochaine édition décalerait les lignes.
#:
#: UNE EXCEPTION QUI GROSSIT EST UN SIGNAL. Si cette liste dépasse CINQ entrées,
#: c'est la règle qu'il faudra revoir — pas la liste qu'il faudra rallonger.
EXCEPTIONS_302 = {
    "sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html": ["La mairie vous appelle"],
    "sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html": ["La mairie vous appelle"],
}

assert sum(len(v) for v in EXCEPTIONS_302.values()) <= 5, (
    "la liste d'exceptions de la n°302 dépasse cinq entrées : c'est la règle "
    "qu'il faut revoir, pas la liste qu'il faut rallonger")


def regle_302(src: str, chemin: pathlib.Path | None = None) -> tuple[str, str]:
    """n°302 — dans une page que l'élève lit, on ne parle jamais de lui.

    On lui parle à la deuxième personne, ou on le fait parler à la première.
    Jamais de troisième personne dans un intitulé : parler DE l'élève, c'est
    écrire pour ses parents ou pour l'inspection, et l'élève le sent.

    CE QUE CE CONTRÔLE VOIT — et rien de plus : les INTITULÉS, c'est-à-dire
    `h1`–`h6`, `th`, `summary`, `legend`, `caption`, `figcaption`. C'est le cas
    non ambigu, celui où la troisième personne n'a aucune excuse.

    CE QU'IL NE VOIT PAS, et qu'il faut dire (règle d'or n°242) :
      · la PROSE du corps de la page — elle demande un jugement au cas par cas ;
        `audit_personne_eleve.mjs` l'inventorie et propose un verdict, sans
        trancher ;
      · les PROPOSITIONS et ÉNONCÉS de QCM — « l'élève » peut y être un
        personnage du scénario, et c'est légitime. La `<legend>` d'un groupe de
        questions est donc exemptée ici ;
      · les TEXTES ALTERNATIFS des images, le contenu des SVG, et tout ce qu'un
        script écrit à l'exécution.

    Les pages PROFESSEUR sont hors sujet par convention de nom : ce contrôle ne
    lit que des `sequence*.html`, qui sont des pages élèves par définition.
    """
    # Le style, les scripts et les commentaires sont retirés AVANT de chercher :
    # un commentaire CSS qui cite « <legend> » — il y en a un depuis la n°300 —
    # ouvrait sinon une balise que le moteur refermait sur la première vraie,
    # et l'intitulé rapporté n'était alors la légende de personne.
    lisible = re.sub(r"<!--.*?-->", " ", src, flags=re.S)
    lisible = re.sub(r"<script\b.*?</script>", " ", lisible, flags=re.S | re.I)
    lisible = re.sub(r"<style\b.*?</style>", " ", lisible, flags=re.S | re.I)

    tolerees = EXCEPTIONS_302.get(chemin.name, []) if chemin is not None else []

    fautifs = []
    for m in INTITULE.finditer(lisible):
        balise, contenu = m.group(1).lower(), m.group(2)
        texte = re.sub(r"<[^>]+>", " ", contenu)
        # la <legend> d'un groupe de questions est un ÉNONCÉ, pas un titre
        if balise == "legend" and "qcm-groupe" in lisible[max(0, m.start() - 300):m.start()]:
            continue
        propre = " ".join(texte.split())
        # une phrase nommément tolérée pour CE fichier : parole rapportée
        if any(t in propre for t in tolerees):
            continue
        if PARLE_DE_LUI.search(texte):
            fautifs.append("<%s> « %s »" % (balise, propre[:70]))
        elif VOUVOIEMENT.search(texte):
            fautifs.append("<%s> vouvoiement « %s »" % (balise, propre[:70]))

    if fautifs:
        return "ECHEC", ("%d intitulé(s) parlent de l'élève au lieu de lui parler : "
                         % len(fautifs)) + " · ".join(fautifs[:4]) + (
                             " …" if len(fautifs) > 4 else "")
    return "OK", "aucun intitulé ne parle de l'élève à la troisième personne"


REGLES = [
    ("n°23 durée", regle_23),
    ("n°26 diagnostic d'entrée", regle_26),
    ("n°29 mode essentiel", regle_29),
    ("n°30 tableau de bord", regle_30),
    ("n°31 version étayée", regle_31),
    ("n°33 aération", regle_33),
    ("n°34 accessibilité", regle_34),
    ("n°42 formulation du référentiel", regle_42),
    ("n°51 titre affiché", regle_51),
    ("n°53 notion et sa voisine", regle_53),
    ("n°54 nombre annoncé ailleurs", regle_54),
    ("n°67 consigne sans champ", regle_67),
    ("n°298 page élève allégée", regle_298),
    ("n°300 question dans le flux", regle_300),
    ("n°301 le bilan clôt", regle_301),
    ("n°302 on parle À l'élève", regle_302),  # reçoit le chemin : voir EXCEPTIONS_302
    ("n°304 l'ouverture ne dit pas le passé", regle_304),
]

SYMBOLE = {"OK": "✔", "ECHEC": "✘", "ALERTE": "▲", "SANS OBJET": "·", "INCONNU": "?"}


def analyser(chemin: pathlib.Path) -> dict:
    src = chemin.read_text(encoding="utf-8")
    m = re.match(r"sequence_(\de)", chemin.name)
    niveau = m.group(1) if m else None
    res = {}
    for nom, fn in REGLES:
        if fn is regle_26:
            sortie = fn(src, niveau)
        elif fn is regle_54:
            sortie = fn(src, chemin.parent)   # la n°54 compare deux fichiers
        elif fn is regle_302:
            sortie = fn(src, chemin)          # la n°302 consulte EXCEPTIONS_302 par nom de fichier
        elif fn is regle_51 or fn is regle_42:
            sortie = fn(src, chemin)          # la n°51 compare le titre au chemin ; la n°42 lit la synthèse
        else:
            sortie = fn(src)
        res[nom] = dict(zip(("etat", "detail"), sortie))
    return {"fichier": str(chemin.relative_to(RACINE)), "regles": res,
            "signalements": signalements(src)}


def main(argv: list[str]) -> int:
    sortie_json = "--json" in argv
    cibles = [a for a in argv[1:] if not a.startswith("--")]
    racines = [RACINE / c for c in cibles] if cibles else [RACINE]
    # Le motif "sequence_*.html" laissait échapper toutes les séquences nommées avec des
    # traits d'union — dont la plus grosse du dépôt (121 ko, 4e_C1.4). Six fichiers de
    # séquence n'ont jamais été analysés depuis la création de cet outil : ils n'avaient
    # pas d'anomalie, ils étaient invisibles. Un contrôle ne vérifie que ce qu'il regarde.
    # Les archives sont gardées comme trace, pas comme ressource vivante : les
    # juger produit des manquements qu'on ne corrigera jamais.
    fichiers = sorted({f for r in racines
                       for motif in ("**/sequence_*.html", "**/sequence-*.html", "**/sequence.html")
                       for f in r.glob(motif)
                       if "_archive-anciennes-versions" not in f.parts})

    # Règle d'or n°299 : une cible mal écrite en argument, ou un dépôt à moitié
    # cloné, donnait « 0 séquence(s) analysée(s) » suivi d'une sortie 0 — la
    # forme exacte d'un contrôle qui n'a rien vu et se déclare content.
    if not fichiers:
        return panne.rien_vu("aucune séquence sous %s (motifs : sequence_*.html, "
                             "sequence-*.html, sequence.html)"
                             % " · ".join(str(r) for r in racines))

    rapports = [analyser(f) for f in fichiers]
    if sortie_json:
        print(json.dumps(rapports, ensure_ascii=False, indent=1))
        return 0

    echecs = 0
    for r in rapports:
        print(f"\n── {r['fichier']}")
        for nom, v in r["regles"].items():
            print(f"   {SYMBOLE[v['etat']]} {nom:<26} {v['detail']}")
            echecs += v["etat"] == "ECHEC"
        for s in r["signalements"]:
            print(f"   ⚑ à relire — {s}")
    print(f"\n{len(fichiers)} séquence(s) analysée(s) · {echecs} manquement(s) mécaniquement établi(s)")
    # Règle d'or n°47 — un contrôle déclare son périmètre, y compris ce qu'il ignore.
    print("\nPÉRIMÈTRE DE CE CONTRÔLE")
    print("  Vérifié mécaniquement : " + " · ".join(nom.split()[0] for nom, _ in REGLES))
    print("  Jugement humain requis : n°24, n°25, n°27, n°28, n°32 — voir les ⚑ ci-dessus.")
    print("  n°302 : seuls les INTITULÉS sont lus — h1-h6, th, summary, legend, caption.")
    print("  NON VU : la prose du corps, les propositions et énoncés de QCM (où « l'élève »")
    print("  peut être un personnage), les textes alternatifs, les SVG, et ce qu'un script")
    print("  écrit à l'exécution. `audit_personne_eleve.mjs` inventorie la prose sans trancher.")
    print("  n°301 : seuls l'EXISTENCE du bilan et l'ORDRE des blocs sont jugés ici. Qu'un")
    print("  Bonus porte des champs demande de délimiter son bloc, donc d'analyser l'arbre :")
    print("  `audit_cloture_sequence.mjs` le mesure. La QUALITÉ d'un corrigé ne se mesure pas.")
    print("  n°300 : seule la FORME du champ est lue. Que l'énoncé soit dans une <legend>")
    print("  et que la valeur transmise soit le texte de la proposition se vérifient au banc")
    print("  du lot et à l'œil — pas par expression régulière.")
    print("  NON couvert : justesse pédagogique des contenus et des corrigés, qualité des")
    print("  explications, progressivité réelle, ergonomie en classe, rendu à l'impression.")
    print("  Fichiers regardés : sequence_*.html, sequence-*.html, sequence.html — un QCM,")
    print("  une synthèse ou une fiche n'est PAS analysé ici.")
    print("  Exclu : _archive-anciennes-versions/ — une archive est une trace, pas une ressource.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
