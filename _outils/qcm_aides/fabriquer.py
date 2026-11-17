# -*- coding: utf-8 -*-
"""fabriquer.py — écrire le `qcm_aides_<lot>.json` d'un QCM à partir des NUMÉROS de ses questions (lot 3, 17/11/2026).

Les pièges d'un QCM se pensent en lisant ses questions numérotées (`indices_creux.mjs <qcm> --liste`) ; on les écrit
par numéros, et cet outil recopie les notions mot pour mot (une notion mal recopiée ferait un piège vide), vérifie que
chaque question est dans un piège et un seul, que chaque piège en a au moins trois et qu'il y en a 4 à 8, met les
espaces insécables de la typographie française (« ? », « : », « ; », « ! », « » ») et écrit le JSON à côté du QCM.

Le plan, en JSON :
  {"lot": "4e_C6.2_arrosage",                       ← facultatif : le nom du fichier si le dossier a plusieurs QCM
   "avant_de_commencer": {"revoir": [...], "savoir_faire": [...],
                          "reussir": ["…", "@std"]},  ← « @std » : les deux conseils communs (indice, puis modes)
   "pieges": {"cle": ["Libellé, la question que l'élève doit se poser", [1, 4, 7]], …},
   "bilan_remarquable": "…"}                         ← facultatif (n°338, N3)

  python3 _outils/qcm_aides/fabriquer.py <qcm.html> <plan.json>      puis : poser.py <qcm> <qcm_aides_….json>

Sortie : 0 écrit · 1 le plan ne couvre pas le QCM (question hors piège, en double, piège trop petit) · 2 QCM illisible.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
STD = ["Si tu te trompes, lis l'indice et réessaie avant d'ouvrir la correction.",
       "Commence par «&nbsp;10 questions&nbsp;»&nbsp;; finis par «&nbsp;Uniquement mes erreurs&nbsp;»."]


def notions(qcm: str):
    js = ("import { questions } from %s; const Q = questions(process.argv[1]); "
          "process.stdout.write(JSON.stringify(Q ? Q.map(q => q.n) : null));") % json.dumps(os.path.join(ICI, "indices_creux.mjs"))
    r = subprocess.run(["node", "--input-type=module", "-e", js, qcm], capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout else None


def typo(s: str) -> str:
    return re.sub(r" ([?!:;»])", lambda m: " " + m.group(1), s).replace("« ", "« ")


def fabriquer(qcm: str, plan: dict):
    ns = notions(qcm)
    if not ns:
        return None, ["QCM illisible (pas de const QUESTIONS)"]
    adc = dict(plan["avant_de_commencer"])
    adc["reussir"] = [y for x in adc["reussir"] for y in (STD if x == "@std" else [x])]
    out = {"qcm": os.path.basename(qcm), "avant_de_commencer": adc, "pieges": {}}
    vus, erreurs = [], []
    for k, (lib, idx) in plan["pieges"].items():
        if len(idx) < 3:
            erreurs.append("piège « %s » : %d question(s), il en faut 3 au moins" % (k, len(idx)))
        hors = [i for i in idx if not 1 <= i <= len(ns)]
        if hors:
            erreurs.append("piège « %s » : numéro(s) hors du QCM %s" % (k, hors))
        out["pieges"][k] = {"libelle": typo(lib), "notions": [ns[i - 1] for i in idx if 1 <= i <= len(ns)]}
        vus += idx
    if not 4 <= len(plan["pieges"]) <= 8:
        erreurs.append("%d pièges : il en faut de 4 à 8" % len(plan["pieges"]))
    sans = [i for i in range(1, len(ns) + 1) if i not in vus]
    doubles = sorted({i for i in vus if vus.count(i) > 1})
    if sans:
        erreurs.append("question(s) dans aucun piège : %s" % sans)
    if doubles:
        erreurs.append("question(s) dans deux pièges : %s" % doubles)
    if plan.get("bilan_remarquable"):
        out["bilan_remarquable"] = plan["bilan_remarquable"]
    return out, erreurs


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    qcm, plan = argv[0], json.load(open(argv[1], encoding="utf-8"))
    out, erreurs = fabriquer(qcm, plan)
    if out is None:
        print("✘ " + erreurs[0])
        return 2
    if erreurs:
        for e in erreurs:
            print("✘ " + e)
        return 1
    nom = plan.get("lot") or os.path.basename(os.path.dirname(os.path.abspath(qcm)))
    dest = os.path.join(os.path.dirname(qcm), "qcm_aides_%s.json" % nom)
    json.dump(out, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("✍ %s · %d pièges · chaque question dans un piège" % (dest, len(out["pieges"])))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
