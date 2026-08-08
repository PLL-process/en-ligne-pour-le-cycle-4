#!/usr/bin/env python3
"""Vérificateur des règles d'or n°23 à n°34 (nées de l'audit externe du 08/08/2026).

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
    n_textarea = len(re.findall(r"<textarea\b", src))
    if n_textarea == 0:
        return "SANS OBJET", "aucune production écrite exigée"
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
    ids_labels = set(re.findall(r'<label[^>]*\bfor="([^"]+)"', src))
    # La balise ENTIÈRE est nécessaire : aria-label peut suivre l'attribut id.
    # (Corrigé le 08/08/2026 : l'expression s'arrêtait à id= et signalait comme
    #  « sans étiquette » des champs qui portaient bien un aria-label.)
    for m in re.finditer(r"<(select|textarea)\b[^>]*>", src):
        balise = m.group(0)
        ident = re.search(r'\bid="([^"]+)"', balise)
        if not ident:
            continue
        if ident.group(1) not in ids_labels and "aria-label" not in balise:
            manques.append(f"{m.group(1)}#{ident.group(1)} sans étiquette")
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


REGLES = [
    ("n°23 durée", regle_23),
    ("n°26 diagnostic d'entrée", regle_26),
    ("n°29 mode essentiel", regle_29),
    ("n°30 tableau de bord", regle_30),
    ("n°31 version étayée", regle_31),
    ("n°33 aération", regle_33),
    ("n°34 accessibilité", regle_34),
]

SYMBOLE = {"OK": "✔", "ECHEC": "✘", "ALERTE": "▲", "SANS OBJET": "·", "INCONNU": "?"}


def analyser(chemin: pathlib.Path) -> dict:
    src = chemin.read_text(encoding="utf-8")
    m = re.match(r"sequence_(\de)", chemin.name)
    niveau = m.group(1) if m else None
    res = {}
    for nom, fn in REGLES:
        res[nom] = dict(zip(("etat", "detail"),
                            fn(src, niveau) if fn is regle_26 else fn(src)))
    return {"fichier": str(chemin.relative_to(RACINE)), "regles": res,
            "signalements": signalements(src)}


def main(argv: list[str]) -> int:
    sortie_json = "--json" in argv
    cibles = [a for a in argv[1:] if not a.startswith("--")]
    racines = [RACINE / c for c in cibles] if cibles else [RACINE]
    fichiers = sorted({f for r in racines for f in r.glob("**/sequence_*.html")})

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
    print("Les règles n°24, n°25, n°27, n°28 et n°32 relèvent du jugement : voir les ⚑.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
