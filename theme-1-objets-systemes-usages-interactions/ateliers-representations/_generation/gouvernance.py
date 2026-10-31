# -*- coding: utf-8 -*-
"""Les pièces de gouvernance de chaque atelier, tirées de ses données — jamais recopiées à la main.

    python3 gouvernance.py                # tous les ateliers construits, puis le README du dossier
    python3 gouvernance.py interacteurs   # un ou plusieurs modules

Pour chaque atelier, dans son dossier :
  - fiche_pedagogique_<slug>.md   codes en toutes lettres, déroulé par niveau, différenciation, évaluation, sources ;
  - matrice_couverture_<slug>.csv les colonnes de la règle d'or n°124 ;
  - README.md                     ce que contient le dossier, et où chaque code est servi ;
  - manifest_<slug>.json          la liste des fichiers et des chiffres ;
  - rapport_tests_<slug>.md       le banc et les contrôles du dépôt RÉELLEMENT exécutés à l'instant (n°299 : un contrôle
                                  qui n'a rien vérifié est en panne) — avec leur dernière ligne et leur code de sortie.
"""
import csv
import datetime
import html
import importlib
import io
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import build  # noqa: E402
import moteur  # noqa: E402

DEPOT = moteur.DEPOT
AUJOURDHUI = datetime.date.today().isoformat()
SCRATCH = pathlib.Path(tempfile.mkdtemp(prefix="banc_ateliers_"))   # résultats bruts du banc, hors du dépôt


def brut(h):
    """Le texte d'un fragment HTML, sans balises ni entités."""
    t = re.sub(r"<br\s*/?>", " ", h or "")
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def verbe_officiel(code):
    f = moteur.formulation(code)
    m = re.match(r"\s*([A-ZÉÈÀÂÎÔÛa-zéèêàâîôûç'’-]+(?:\s+(?:la|le|les|l'|des|un|une)?\s*liste)?)", f)
    return (m.group(1) if m else f.split()[0]).strip()


def questions_par_code(at):
    try:
        q = importlib.import_module("q_" + at.MODULE)
    except ModuleNotFoundError:
        return {}
    par = {}
    for i, x in enumerate(q.Q, 1):
        par.setdefault(x["c"], []).append(i)
    return par


def niveau_cognitif(ex):
    types = {w["type"] for w in ex["widgets"]}
    if "croquis" in types:
        return "créer — dessin libre, relu avec une liste"
    if "texte" in types or "liste" in types:
        return "produire — l'élève formule seul (texte ou liste libre)"
    if "slots" in types or "classer" in types or "tableau" in types:
        return "appliquer — compléter, classer"
    return "comprendre — choisir et justifier"


def production_seul(ex):
    types = {w["type"] for w in ex["widgets"]}
    seul = types & {"texte", "liste", "croquis"}
    return ("✍ conçoit seul : " if seul else "") + brut(ex.get("production", ""))


def fiche(at):
    L = ["# Fiche pédagogique — Atelier « %s » (%s)" % (brut(at.TITRE), brut(at.TITRE_COMPLET)), ""]
    nivs = list(at.NIVEAUX)
    L += ["**Niveaux** : %s — une page par niveau, la même ressource." % ", ".join(nivs),
          "**Thème** : 1 — Objets, systèmes, usages et interactions (représentation transversale : elle sert aussi les "
          "thèmes 2 et 3 quand ses codes l'y conduisent).",
          "**Générée** le %s par `_generation/gouvernance.py` à partir de `donnees_%s.py` : on corrige la donnée, pas la fiche."
          % (AUJOURDHUI, at.MODULE), ""]
    L += ["## Deux noms", "", brut(at.DEUX_NOMS), ""]
    L += ["## Les codes, en toutes lettres", "", "| Niveau | Code | Compétence du référentiel |", "|---|---|---|"]
    for niv, N in at.NIVEAUX.items():
        for c in N["codes"]:
            L.append("| %s | %s | %s |" % (niv, c, moteur.formulation(c)))
    L += ["", "## Où elle se place dans la démarche", "", brut(at.CHAINE), ""]
    if getattr(at, "VERBES", None):
        L += ["## Les verbes, niveau par niveau", ""]
        for niv, v in at.VERBES.items():
            L.append("- **%s** : %s" % (niv, brut(v)))
        L.append("")
    for niv, N in at.NIVEAUX.items():
        total = sum(e["duree"] for e in N["exercices"])
        L += ["## %s — %s (≈ %d min)" % (niv, brut(N.get("mission", "")), total), ""]
        if N.get("question"):
            L += ["**Question de départ** : %s" % brut(N["question"]), ""]
        L += ["| Exercice | Code | Durée | Objectif | Production |", "|---|---|---|---|---|"]
        for i, e in enumerate(N["exercices"], 1):
            L.append("| %d. %s | %s | %d min | %s | %s |" % (i, brut(e["titre"]), e["code"], e["duree"],
                                                            brut(e["objectif"]), production_seul(e)))
        L += ["", "**À retenir** : " + brut(N.get("a_retenir", "")), ""]
    L += ["## Différenciation", "",
          "- Deux aides par exercice : l'aide 1 oriente, l'aide 2 donne le raisonnement ; puis un **exercice jumeau** à "
          "valeurs différentes, avec sa correction.",
          "- Chaque champ libre a sa **version étayée** (débuts de phrase) ; le croquis peut se décrire en mots.",
          "- Chaque exercice se vérifie seul (retour gradué, encoches ✔ / ✘ / ○ doublées d'un mot) et a sa **correction "
          "exhaustive**, même quand tout est juste.",
          "- La sauvegarde est locale et partagée : l'élève retrouve son travail dans l'atelier, le cahier de niveau et la "
          "séquence où l'exercice est inséré.", ""]
    n = build.compte_qcm(at)
    L += ["## Évaluation", "",
          "- Positionnement de l'élève, en fin de page, sur chaque code (quatre niveaux, formulation du référentiel mot pour mot).",
          "- QCM d'entraînement : %s questions fixes, dont %s illustrées, chaque distracteur réfuté." % ((n or ("—", "—"))[0], (n or ("—", "—"))[1]),
          "- Aucun corrigé d'évaluation sommative dans le dépôt.", ""]
    L += ["## Notes et sources", "", brut(at.NOTES_PROF), ""]
    return "\n".join(L)


def matrice(at):
    par = questions_par_code(at)
    out = io.StringIO()
    w = csv.writer(out, delimiter=";", lineterminator="\n")
    w.writerow(["code", "verbe_officiel", "activite", "production_attendue", "questions_qcm", "niveau_cognitif",
                "socle", "crcn", "critere_de_reussite"])
    for niv, N in at.NIVEAUX.items():
        for i, e in enumerate(N["exercices"], 1):
            qs = par.get(e["code"], [])
            w.writerow([e["code"], verbe_officiel(e["code"]),
                        "Atelier %s, exercice %d — %s (%d min)" % (niv, i, brut(e["titre"]), e["duree"]),
                        production_seul(e),
                        ("Q" + ", Q".join(str(x) for x in qs)) if qs else "—",
                        niveau_cognitif(e),
                        "D1.3 (langages scientifiques : lire et produire une représentation) · D4 (systèmes techniques)",
                        "— (aucun CRCN déclaré : la règle n°7 exige compétence, niveau, repère, action et trace)",
                        brut(e.get("critere", ""))])
    return out.getvalue()


def ou_servi(at):
    lignes = []
    for niv, N in at.NIVEAUX.items():
        for c in N["codes"]:
            d = moteur.dossier_code(c)
            seq = moteur.sequence_du_code(c)
            lignes.append("| %s | %s | %s | %s |" % (
                niv, c,
                ("`%s/atelier_%s.html`" % (d.relative_to(DEPOT).as_posix(), build.nom_panneau(at))) if d else "—",
                ("`%s`" % seq.relative_to(DEPOT).as_posix()) if seq else "—"))
    return lignes


def incrustations_de(at):
    try:
        import incrustations_table as table
    except ModuleNotFoundError:
        return []
    return [i for i in table.INCRUSTATIONS if i["module"] == at.MODULE]


def readme(at):
    d = build.dossier(at)
    L = ["# Atelier « %s » — %s" % (brut(at.TITRE), brut(at.TITRE_COMPLET)), "",
         brut(at.DEUX_NOMS), "",
         "## Les pages", "", "| Page | Rôle |", "|---|---|"]
    for niv in at.NIVEAUX:
        L.append("| `%s` | l'atelier de %s |" % (build.page_niveau(at, niv).relative_to(d).as_posix(), niv))
    L += ["| `%s` | le QCM (30 questions fixes) |" % build.qcm(at).relative_to(d).as_posix(),
          "| `%s` | la synthèse élève (deux pages A4 : la carte « Ce que je dois retenir », les parties, le lexique) |" % build.synthese_eleve(at).relative_to(d).as_posix(),
          "| `%s` | la synthèse professeur |" % build.synthese_prof(at).relative_to(d).as_posix(),
          "| `fiche_pedagogique_%s.md`, `matrice_couverture_%s.csv` | gouvernance |" % (at.SLUG, at.SLUG),
          "| `rapport_tests_%s.md`, `manifest_%s.json` | tests exécutés, inventaire |" % (at.SLUG, at.SLUG),
          "| `Images/`, `SOURCES_MEDIAS.md` | schémas SVG originaux et leur provenance |", "",
          "## Où chaque code est servi", "", "| Niveau | Code | Page-pointeur | Séquence du code |", "|---|---|---|---|"]
    L += ou_servi(at)
    inc = incrustations_de(at)
    if inc:
        L += ["", "## Exercices insérés dans des séquences", "", "| Séquence | Niveau | Exercices |", "|---|---|---|"]
        for i in inc:
            L.append("| `%s` | %s | %s |" % (i["sequence"], i["niveau"], ", ".join(i["exos"])))
    L += ["", "Ne pas modifier ces pages à la main : elles sont produites par `../_generation/` "
          "(`python3 build.py %s`, `python3 build_qcm.py %s`, `python3 gouvernance.py %s`)." % (at.MODULE, at.MODULE, at.MODULE), ""]
    return "\n".join(L)


def lancer(cmd):
    r = subprocess.run(cmd, cwd=DEPOT, capture_output=True, text=True)
    sortie = (r.stdout + r.stderr).strip().splitlines()
    return r.returncode, (sortie[-1] if sortie else "(aucune sortie)")


def rapport(at):
    d = build.dossier(at).relative_to(DEPOT).as_posix()
    js = SCRATCH / ("banc_%s.json" % at.MODULE)
    code_banc, fin_banc = lancer([sys.executable, str(ICI / "banc_ateliers.py"), at.MODULE, "--json", str(js)])
    tests = json.loads(js.read_text(encoding="utf-8")) if js.exists() else []
    controles = [
        ("controle_longueurs.py", [sys.executable, "_outils/controle_longueurs.py", d]),
        ("controle_hierarchie.py", [sys.executable, "_outils/controle_hierarchie.py", d]),
        ("controle_regles_visibles.py", [sys.executable, "_outils/controle_regles_visibles.py", d]),
        ("controle_medias.py", [sys.executable, "_outils/controle_medias.py", d]),
        ("controle_liens.py", [sys.executable, "_outils/controle_liens.py", d]),
        ("verif_qcm_coherence.mjs", ["node", "_outils/verif_qcm_coherence.mjs", build.qcm(at).relative_to(DEPOT).as_posix()]),
    ]
    L = ["# Rapport de tests — atelier « %s »" % brut(at.TITRE), "",
         "Écrit le %s par `_generation/gouvernance.py`, **à partir des exécutions faites à l'instant** : rien n'y est "
         "déclaré qui n'ait tourné (règle d'or n°299 : un contrôle qui n'a rien vérifié est en panne)." % AUJOURDHUI, "",
         "## Banc de l'atelier (`banc_ateliers.py %s`, Chromium, 390 px)" % at.MODULE, "",
         "Code de sortie : **%d** — %s" % (code_banc, fin_banc), ""]
    for t in tests:
        L.append("- %s %s" % ("✔" if t["ok"] else "✘", t["test"]))
    L += ["", "## Contrôles du dépôt", "", "| Contrôle | Code | Dernière ligne |", "|---|---|---|"]
    for nom, cmd in controles:
        c, fin = lancer(cmd)
        L.append("| `%s` | %d | %s |" % (nom, c, fin.replace("|", "/")))
    L += ["", "## Non exécuté ici", "",
          "- La relecture humaine des dessins (captures PNG regardées à la production, non rejouées par ce script).",
          "- Les bancs des séquences qui accueillent des exercices insérés : ils se lancent dans le dossier de chaque séquence.", ""]
    return "\n".join(L), code_banc


def manifest(at):
    d = build.dossier(at)
    fichiers = sorted(p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file())
    n = build.compte_qcm(at) or (0, 0)
    return json.dumps({
        "lot": "Thème 1 — Ateliers des représentations : %s" % brut(at.TITRE_COMPLET),
        "atelier": brut(at.TITRE), "slug": at.SLUG, "module": at.MODULE,
        "niveaux": list(at.NIVEAUX),
        "codes": [c for N in at.NIVEAUX.values() for c in N["codes"]],
        "exercices": {niv: [{"id": e["id"], "titre": brut(e["titre"]), "code": e["code"], "duree_min": e["duree"]}
                            for e in N["exercices"]] for niv, N in at.NIVEAUX.items()},
        "qcm": {"questions": n[0], "illustrees": n[1]},
        "insertions": [{"sequence": i["sequence"], "niveau": i["niveau"], "exercices": i["exos"]} for i in incrustations_de(at)],
        "branche": "fable/ateliers-representations",
        "date_production": AUJOURDHUI,
        "source_inspiration": "cahier « 123 Techno » (Bordas 2021), mécaniques seulement — décision de Pascal du 24/10/2026",
        "fichiers": fichiers,
    }, ensure_ascii=False, indent=2) + "\n"


def readme_general(ateliers):
    L = ["# Les ateliers des représentations", "",
         "Une représentation technique par atelier, des exercices en spirale de la 5e à la 3e quand le référentiel le "
         "permet, un QCM de 30 questions, une synthèse élève (deux pages A4) et une synthèse professeur. Les cahiers de "
         "niveau (`cahiers/`) rassemblent tous les ateliers d'un niveau. Certains exercices sont aussi insérés dans les "
         "séquences des codes qu'ils servent : la sauvegarde est la même partout.", "",
         "| Atelier | Niveaux | Codes | Exercices |", "|---|---|---|---|"]
    for at in ateliers:
        codes = sorted({c for N in at.NIVEAUX.values() for c in N["codes"]})
        nb = sum(len(N["exercices"]) for N in at.NIVEAUX.values())
        L.append("| [%s](%s/README.md) — %s | %s | %s | %d |" % (brut(at.TITRE), at.SLUG, brut(at.ETIQUETTE_COURTE),
                                                            ", ".join(at.NIVEAUX), ", ".join(codes), nb))
    L += ["", "Fabrication : `_generation/` (lire `CONSIGNES_REDACTION.md` avant d'écrire un atelier). "
          "Assembler : `build.py`, `build_qcm.py`, `incrustations.py` ; tester : `banc_ateliers.py` ; "
          "gouvernance : `gouvernance.py`.", ""]
    return "\n".join(L)


def main(modules):
    ateliers = [at for at in build.charger(modules or None)
                if all(build.page_niveau(at, niv).exists() for niv in at.NIVEAUX)]
    if not ateliers:
        print("Aucun atelier construit.")
        return 2
    pire = 0
    for at in ateliers:
        d = build.dossier(at)
        (d / ("fiche_pedagogique_%s.md" % at.SLUG)).write_text(fiche(at), encoding="utf-8")
        (d / ("matrice_couverture_%s.csv" % at.SLUG)).write_text(matrice(at), encoding="utf-8")
        (d / "README.md").write_text(readme(at), encoding="utf-8")
        texte, code = rapport(at)
        (d / ("rapport_tests_%s.md" % at.SLUG)).write_text(texte, encoding="utf-8")
        (d / ("manifest_%s.json" % at.SLUG)).write_text(manifest(at), encoding="utf-8")
        pire = max(pire, code)
        print("%-24s fiche · matrice · README · rapport (banc : %d) · manifest" % (at.SLUG, code))
    if not modules:
        tous = [at for at in build.charger() if all(build.page_niveau(at, n).exists() for n in at.NIVEAUX)]
        (build.RACINE / "README.md").write_text(readme_general(tous), encoding="utf-8")
        print("README général écrit (%d ateliers)" % len(tous))
    return pire


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
