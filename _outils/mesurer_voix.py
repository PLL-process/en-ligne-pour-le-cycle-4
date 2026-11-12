# -*- coding: utf-8 -*-
"""mesurer_voix.py — à quelle vitesse parlent les voix des animations pas à pas.

    python3 _outils/mesurer_voix.py [racine] [--muet] [--json fichier]

D'OÙ VIENT CETTE MESURE
-----------------------
Le 30/10/2026, une revue des dix-huit prises de deux animations (lampadaire de 5e, pompe de 4e) a mesuré un
débit de 150 à 210 mots par minute, « rapide pour des élèves qui lisent mal » ; le 08/11, Pascal a fait
ralentir ces deux lots (`length_scale` 1.15, visée : 140 à 170 mots par minute). La mesure avait été faite à
la main, une fois, sur deux lots sur cinq ; les trois autres (vélo-cargo, trois principes, jardin) sont restés
à la vitesse d'origine, et le journal du 08/11 laisse la question à Pascal. Cet outil rejoue la mesure sur
TOUTES les animations, à chaque fois qu'on le lance.

CE QU'IL MESURE
---------------
Pour chaque dossier `_generation/<voix>/` qui porte un `phrases.json` : étape par étape, le nombre de mots
PRONONCÉS (le champ « envoye » quand il existe, sinon « dit »), la durée du fichier `.ogg` de l'étape (lue par
ffprobe, dans le dossier `Audio/` du lot), et le débit en mots par minute. Il nomme les étapes au-dessus de
REPERE_DEBIT, et donne pour chaque animation le débit moyen, l'étendue, la durée totale et l'étape la plus longue.

CE QU'IL NE MESURE PAS, ET LE DIT
---------------------------------
  · La durée est celle du FICHIER : les lots refaits le 08/11 portent 0,5 s de silence (0,2 devant, 0,3
    derrière). Leur débit réel, voix seule, est un peu plus élevé que le chiffre donné — de 4 à 5 % sur une
    étape de dix secondes.
  · Il ne dit pas si la voix est juste, ni si elle est agréable : seule l'écoute de Pascal valide une prise.
  · REPERE_DEBIT (170) est le haut de la fourchette visée le 08/11 ; ce n'est pas un seuil mesuré en classe.
  · Une idée lue pendant la veille du 11/11/2026 — signaler plus de quatre secondes de voix sans changement à
    l'écran — vient de la vidéo et ne s'applique pas telle quelle : dans le lecteur pas à pas, l'écran change
    une fois par étape, puis la voix dit sa phrase. L'outil donne donc la durée de l'étape la plus longue,
    sans la juger.

Sortie : 0 mesure faite (ce n'est pas un contrôle : il ne refuse rien) · 2 EN PANNE — ffprobe introuvable,
aucune animation trouvée, ou une étape sans fichier son (règle d'or n°299).
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys

REPERE_DEBIT = 170          # mots par minute : haut de la fourchette visée le 08/11/2026 (140 à 170)
IGNORES = {"_archive-anciennes-versions", "node_modules", ".git", "_exports"}
MOT = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+(?:['’-][0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+)*")


def compter_mots(texte):
    """Les mots prononcés : « l'énergie » et « vélo-cargo » comptent pour un mot chacun."""
    return len(MOT.findall(re.sub(r"<[^>]+>", " ", texte or "")))


def duree(fichier):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                        "default=noprint_wrappers=1:nokey=1", str(fichier)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def sons_de(lot, n, indice):
    """Les n fichiers .ogg de l'animation, dans l'ordre : le groupe de Audio/ numéroté de 1 à n.
    `indice` (le texte de voix.json) départage deux groupes de même taille."""
    audio = lot / "Audio"
    if not audio.is_dir():
        return None
    groupes = {}
    for f in audio.glob("*.ogg"):
        m = re.match(r"^(.*?)(\d+)$", f.stem)
        if m:
            groupes.setdefault(m.group(1), {})[int(m.group(2))] = f
    bons = [(p, g) for p, g in groupes.items() if sorted(g) == list(range(1, n + 1))]
    if len(bons) > 1:
        cites = [(p, g) for p, g in bons if p in indice]
        bons = cites or bons
    if len(bons) != 1:
        return None
    return [bons[0][1][i] for i in range(1, n + 1)]


def mesurer(racine):
    animations, pannes = [], []
    for phrases in sorted(racine.rglob("phrases.json")):
        if IGNORES & set(phrases.relative_to(racine).parts) or phrases.parent.parent.name != "_generation":
            continue
        try:
            liste = json.loads(phrases.read_text(encoding="utf-8")).get("phrases")
        except (ValueError, AttributeError):
            liste = None
        nom = phrases.parent.relative_to(racine).as_posix()
        if not isinstance(liste, list) or not liste:
            pannes.append((nom, "phrases.json sans liste « phrases »"))
            continue
        lot = phrases.parent.parent.parent
        voix = phrases.parent / "voix.json"
        indice = voix.read_text(encoding="utf-8") if voix.is_file() else ""
        sons = sons_de(lot, len(liste), indice)
        if not sons:
            pannes.append((nom, "pas de groupe de %d fichiers .ogg numérotés dans %s/Audio" % (len(liste), lot.name)))
            continue
        vitesse = None
        try:
            vitesse = json.loads(indice).get("reglages_piper", {}).get("length_scale")
        except ValueError:
            pass
        etapes = []
        for i, (ph, son) in enumerate(zip(liste, sons), 1):
            d = duree(son)
            if not d:
                pannes.append((nom, "durée illisible : %s" % son.name))
                etapes = None
                break
            mots = compter_mots(ph.get("envoye") or ph.get("dit"))
            etapes.append({"etape": i, "mots": mots, "duree_s": round(d, 2), "debit": round(60 * mots / d)})
        if etapes:
            total_mots, total_s = sum(e["mots"] for e in etapes), sum(e["duree_s"] for e in etapes)
            animations.append({"animation": nom, "length_scale": vitesse, "etapes": etapes,
                               "debit_moyen": round(60 * total_mots / total_s), "duree_totale_s": round(total_s, 1),
                               "rapides": [e["etape"] for e in etapes if e["debit"] > REPERE_DEBIT]})
    return animations, pannes


def main(argv):
    muet = "--muet" in argv
    sortie = argv[argv.index("--json") + 1] if "--json" in argv and argv.index("--json") + 1 < len(argv) else None
    libres = [a for i, a in enumerate(argv) if not a.startswith("--") and not (i and argv[i - 1] == "--json")]
    racine = pathlib.Path(libres[0]).resolve() if libres else pathlib.Path(__file__).resolve().parent.parent
    if not shutil.which("ffprobe"):
        print("❌ EN PANNE : ffprobe est introuvable (il vient avec ffmpeg) — règle d'or n°299.")
        return 2
    if not racine.is_dir():
        print("❌ EN PANNE : « %s » n'est pas un dossier (règle d'or n°299)." % racine)
        return 2
    animations, pannes = mesurer(racine)
    if sortie:
        pathlib.Path(sortie).write_text(json.dumps({"repere_debit": REPERE_DEBIT, "animations": animations,
                                                    "pannes": pannes}, ensure_ascii=False, indent=1), encoding="utf-8")
    for a in animations:
        debits = [e["debit"] for e in a["etapes"]]
        longue = max(a["etapes"], key=lambda e: e["duree_s"])
        print("%s %s" % ("▲" if a["rapides"] else "·", a["animation"]))
        print("    %d étapes · %d mots/min en moyenne (de %d à %d) · %.0f s en tout · étape la plus longue : n°%d, %.1f s%s"
              % (len(a["etapes"]), a["debit_moyen"], min(debits), max(debits), a["duree_totale_s"], longue["etape"],
                 longue["duree_s"], "" if a["length_scale"] is None else " · vitesse Piper %s" % a["length_scale"]))
        if a["rapides"]:
            print("    ▲ au-dessus de %d mots/min : étape(s) %s" % (REPERE_DEBIT, ", ".join(
                "%d (%d)" % (e["etape"], e["debit"]) for e in a["etapes"] if e["debit"] > REPERE_DEBIT)))
        if not muet:
            for e in a["etapes"]:
                print("       étape %2d : %3d mots · %5.1f s · %3d mots/min" % (e["etape"], e["mots"], e["duree_s"], e["debit"]))
    for nom, raison in pannes:
        print("⚠ non mesurée : %s — %s" % (nom, raison))
    if not animations:
        print("❌ EN PANNE : aucune animation mesurée (règle d'or n°299).")
        return 2
    rapides = [a for a in animations if a["rapides"]]
    vitesses = sorted({a["length_scale"] for a in animations if a["length_scale"] is not None})
    print("\n%d animation(s) mesurée(s) · %d avec au moins une étape au-dessus de %d mots/min%s"
          % (len(animations), len(rapides), REPERE_DEBIT,
             " · vitesses Piper sur le site : %s" % ", ".join(str(v) for v in vitesses) if vitesses else ""))
    print("ℹ Mesure, pas contrôle : la durée est celle du fichier (silences compris) ; seule l'écoute valide une prise.")
    if pannes:
        print("❌ EN PANNE : %d animation(s) non mesurée(s) (règle d'or n°299)." % len(pannes))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
