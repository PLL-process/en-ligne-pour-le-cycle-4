# -*- coding: utf-8 -*-
"""Calcule et vérifie les plannings des trois projets, à partir du seul CSV.

Le corrigé de l'atelier s'appuie sur ces résultats : ils doivent donc être
calculés, jamais recopiés à la main (règle n°48, et n°54 pour les nombres).

Première version fautive : la date au plus tard était initialisée à la durée
totale pour toutes les tâches, et la relaxation oubliait de retrancher la durée
de la tâche elle-même. Résultat : toutes les tâches semblaient avoir une marge,
y compris celles du chemin critique — c'est-à-dire l'inverse de ce qu'on veut
enseigner. C'était le CALCUL qui avait tort, pas les données (règle n°50).
"""
import csv
import json
import pathlib
import sys

D = pathlib.Path(__file__).resolve().parent


def charger(csv_path: pathlib.Path) -> dict:
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8"), delimiter=";"))
    projets = {}
    for p in dict.fromkeys(r["projet"] for r in rows):
        t = {r["id"]: r for r in rows if r["projet"] == p}
        projets[p] = {
            "taches": t,
            "duree": {i: int(r["duree_seances"]) for i, r in t.items()},
            "ant": {i: [x for x in r["anteriorite"].split(",") if x] for i, r in t.items()},
            "niveau": next(r["niveau"] for r in t.values()),
        }
    return projets


def planifier(p: dict) -> dict:
    t, dur, ant = p["taches"], p["duree"], p["ant"]
    for i, a in ant.items():
        for x in a:
            if x not in t:
                raise SystemExit("antériorité inconnue : %s → %s" % (i, x))

    # ── au plus tôt
    tot, pere = {}, {}
    for _ in range(len(t) + 1):
        for i in t:
            c = [(tot.get(a, 0) + dur[a], a) for a in ant[i]]
            tot[i], pere[i] = max(c) if c else (0, None)
    fin = max(tot[i] + dur[i] for i in t)

    # ── au plus tard : début au plus tard = (min des débuts au plus tard des
    #    successeurs) − durée de la tâche. C'est le « − dur[i] » qui manquait.
    tard = {i: fin - dur[i] for i in t}
    succ = {i: [s for s in t if i in ant[s]] for i in t}
    for _ in range(len(t) + 1):
        for i in t:
            if succ[i]:
                tard[i] = min(tard[s] for s in succ[i]) - dur[i]

    marge = {i: tard[i] - tot[i] for i in t}
    critiques = [i for i in sorted(t) if marge[i] == 0]

    # ── le chemin le plus long, remonté depuis la dernière tâche
    dernier = max(t, key=lambda i: (tot[i] + dur[i], i))
    chemin, cur = [], dernier
    while cur:
        chemin.append(cur)
        cur = pere.get(cur)
    chemin.reverse()
    return {"fin": fin, "debut": tot, "marge": marge, "critiques": critiques, "chemin": chemin}


def main() -> int:
    projets = charger(D / "taches_projets_c7_simulees.csv")
    ok = True
    corrige = {}
    for nom, p in projets.items():
        r = planifier(p)
        t, dur = p["taches"], p["duree"]
        corrige[nom] = {
            "niveau": p["niveau"],
            "duree_totale": r["fin"],
            "chemin": r["chemin"],
            "marges": r["marge"],
            "debut_au_plus_tot": r["debut"],
            "fin_au_plus_tot": {i: r["debut"][i] + dur[i] for i in t},
            "duree_tache": dur,
            "anteriorite": p["ant"],
            "libelle": {i: t[i]["tache"] for i in t},
            "nature": {i: t[i]["nature"] for i in t},
        }
        print("── %-26s (%s) · %d entrées · %d séances"
              % (nom, p["niveau"], len(t), r["fin"]))
        print("   chemin le plus long : %s" % " → ".join(r["chemin"]))
        print("   critiques (marge 0) : %s" % ", ".join(r["critiques"]))
        hors = [i for i in sorted(t) if r["marge"][i] > 0]
        print("   avec marge : %s" % (", ".join("%s (+%d)" % (i, r["marge"][i]) for i in hors) or "aucune"))
        # cohérence : le chemin doit être exactement l'ensemble des critiques
        if set(r["chemin"]) != set(r["critiques"]):
            print("   ✘ INCOHÉRENT : le chemin le plus long et les tâches de marge nulle diffèrent")
            print("     chemin=%s critiques=%s" % (r["chemin"], r["critiques"]))
            ok = False
        else:
            print("   ✔ le chemin le plus long est exactement l'ensemble des tâches de marge nulle")

    # Le corrigé n'est écrit QUE si tous les contrôles passent : un fichier de
    # corrigé produit à partir d'un calcul incohérent est pire que pas de fichier.
    if ok:
        (D / "_corrige_calcule.json").write_text(
            json.dumps(corrige, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("→ _corrige_calcule.json réécrit à partir du CSV")
        # garde-fou : le fichier écrit doit redonner marge 0 exactement sur le chemin
        relu = json.loads((D / "_corrige_calcule.json").read_text(encoding="utf-8"))
        for nom, c in relu.items():
            nulles = {i for i, m in c["marges"].items() if m == 0}
            if nulles != set(c["chemin"]):
                print("   ✘ %s : le fichier écrit ne redonne pas le bon chemin" % nom)
                ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
