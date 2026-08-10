# -*- coding: utf-8 -*-
"""Le diagramme de Gantt comme OBJET À LIRE — rendu SVG, méthode Fable.

Ce n'est pas un joli graphique : c'est un support d'enseignement. Chaque trait
répond à une question que l'élève doit apprendre à se poser.

  • barre pleine colorée  → tâche du CHEMIN CRITIQUE (marge exactement nulle)
  • barre pleine neutre   → tâche à marge : elle a du jeu
  • rectangle pointillé   → la FENÊTRE de la tâche : elle aurait pu être placée
                            n'importe où là-dedans sans retarder le projet
  • barre fantôme         → la même tâche placée au plus tard
  • losange               → jalon (durée nulle)
  • flèche                → « celle-ci doit finir avant que celle-là commence »

L'unité de temps est la SÉANCE (1 h 30 par semaine), pas le jour ouvré.

Entrée  : taches_projets_c7_simulees.csv  (projet;niveau;id;tache;duree_seances;anteriorite;nature;qui)
Sorties : gantt_<projet>.svg  +  corrige_<projet>.json  (écrit puis RELU, règle n°71)
"""
import csv, json, sys
from pathlib import Path

# ── Palette : lisible en couleur, lisible en noir et blanc, lisible daltonien ──
C_CRIT   = "#c2410c"   # orange brûlé — le chemin critique
C_CRIT_L = "#fed7aa"
C_LIBRE  = "#0f766e"   # sarcelle — les tâches à marge
C_LIBRE_L= "#ccfbf1"
C_FEN    = "#94a3b8"   # la fenêtre de flottement
C_GRILLE = "#e2e8f0"
C_TEXTE  = "#0f172a"
C_FOND   = "#ffffff"

TITRES = {
    "indicateur-rangement-hall": "L'indicateur de rangement du hall",
    "jardin-connecte-brooklyn": "Le jardin connecté de la cour",
    "capteur-confort-ny": "Le capteur de confort de la salle 214",
}

PX_SEANCE = 62      # largeur d'une séance
H_LIGNE   = 40
X_LIB     = 340     # largeur de la colonne des libellés
MARGE_H   = 28
MARGE_B   = 96      # place pour la légende


def lire(csv_path):
    projets = {}
    with open(csv_path, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            p = projets.setdefault(r["projet"], {"niveau": r["niveau"], "taches": {}})
            p["taches"][r["id"]] = {
                "id": r["id"], "nom": r["tache"],
                "duree": int(r["duree_seances"]),
                "preds": [x for x in r["anteriorite"].split(",") if x],
                "jalon": r["nature"] == "jalon", "qui": r["qui"],
            }
    return projets


def ordonnancer(T):
    """Aller-retour : dates au plus tôt, au plus tard, marge. Tolérance ZÉRO."""
    ordre, vus = [], set()

    def visiter(i):
        if i in vus:
            return
        vus.add(i)
        for p in T[i]["preds"]:
            visiter(p)
        ordre.append(i)

    for i in T:
        visiter(i)

    for i in ordre:                                   # aller
        t = T[i]
        t["tot_debut"] = max([T[p]["tot_fin"] for p in t["preds"]], default=0)
        t["tot_fin"] = t["tot_debut"] + t["duree"]
    fin = max(t["tot_fin"] for t in T.values())

    for i in reversed(ordre):                         # retour
        t = T[i]
        succs = [s for s in T.values() if i in s["preds"]]
        t["tard_fin"] = min([s["tard_debut"] for s in succs], default=fin)
        t["tard_debut"] = t["tard_fin"] - t["duree"]
        t["marge"] = t["tard_debut"] - t["tot_debut"]
        t["critique"] = (t["marge"] == 0)             # exactement zéro, jamais < 1

    # contrôle de bon sens : les durées du chemin critique font la durée du projet
    chemin = [t for t in T.values() if t["critique"]]
    somme = sum(t["duree"] for t in chemin)
    assert somme == fin, f"chemin critique incohérent : {somme} ≠ {fin}"
    return fin


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def svg(nom_projet, niveau, T, fin):
    ids = sorted(T, key=lambda i: (T[i]["tot_debut"], i))
    W = X_LIB + fin * PX_SEANCE + 150
    H = MARGE_H + 74 + len(ids) * H_LIGNE + MARGE_B
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" font-family="system-ui,Segoe UI,Roboto,sans-serif" '
         f'role="img" aria-labelledby="t d">']
    o.append(f'<title id="t">Diagramme de Gantt — {esc(nom_projet)} ({niveau})</title>')
    o.append(f'<desc id="d">Le projet dure {fin} séances. Les tâches du chemin '
             f'critique sont en orange plein ; les tâches à marge sont en sarcelle, '
             f'avec un rectangle pointillé qui montre la fenêtre dans laquelle elles '
             f'auraient pu être placées.</desc>')
    o.append(f'<rect width="{W}" height="{H}" fill="{C_FOND}"/>')
    o.append('<defs><marker id="fl" markerWidth="9" markerHeight="7" refX="8" refY="3.5" '
             f'orient="auto"><path d="M0,0 L9,3.5 L0,7 z" fill="{C_FEN}"/></marker></defs>')

    y0 = MARGE_H + 62
    # ── en-tête ───────────────────────────────────────────────────────────────
    o.append(f'<text x="{MARGE_H}" y="{MARGE_H + 18}" font-size="21" font-weight="700" '
             f'fill="{C_TEXTE}">{esc(TITRES.get(nom_projet, nom_projet))}</text>')
    o.append(f'<text x="{MARGE_H}" y="{MARGE_H + 40}" font-size="13.5" fill="#475569">'
             f'{niveau} · {len(ids)} tâches · le projet tient en <tspan font-weight="700" '
             f'fill="{C_CRIT}">{fin} séances</tspan></text>')

    # ── grille des séances ────────────────────────────────────────────────────
    for s in range(fin + 1):
        x = X_LIB + s * PX_SEANCE
        o.append(f'<line x1="{x}" y1="{y0 - 22}" x2="{x}" y2="{y0 + len(ids) * H_LIGNE}" '
                 f'stroke="{C_GRILLE}" stroke-width="1"/>')
        if s < fin:
            o.append(f'<text x="{x + PX_SEANCE/2}" y="{y0 - 8}" font-size="11.5" '
                     f'text-anchor="middle" fill="#64748b">séance {s+1}</text>')

    pos = {i: k for k, i in enumerate(ids)}
    for i in ids:
        t, k = T[i], pos[i]
        y = y0 + k * H_LIGNE
        cy = y + H_LIGNE / 2
        if k % 2:
            o.append(f'<rect x="0" y="{y}" width="{W}" height="{H_LIGNE}" fill="#f8fafc"/>')

        # libellé
        lib = t["nom"] if len(t["nom"]) <= 44 else t["nom"][:42] + "…"
        o.append(f'<text x="{MARGE_H}" y="{cy + 4}" font-size="13" fill="{C_TEXTE}">'
                 f'<tspan font-weight="700">{t["id"]}</tspan>  {esc(lib)}</text>')

        xa = X_LIB + t["tot_debut"] * PX_SEANCE
        xt = X_LIB + t["tard_debut"] * PX_SEANCE

        if t["jalon"]:
            o.append(f'<path d="M{xa},{cy-11} L{xa+11},{cy} L{xa},{cy+11} L{xa-11},{cy} z" '
                     f'fill="{C_CRIT if t["critique"] else C_LIBRE}"/>')
            o.append(f'<text x="{xa+18}" y="{cy+4}" font-size="12" font-weight="700" '
                     f'fill="{C_CRIT if t["critique"] else C_LIBRE}">jalon</text>')
            continue

        w = t["duree"] * PX_SEANCE
        if t["critique"]:
            o.append(f'<rect x="{xa}" y="{y+9}" width="{w}" height="{H_LIGNE-18}" rx="5" '
                     f'fill="{C_CRIT}"/>')
            o.append(f'<text x="{xa+w/2}" y="{cy+4}" font-size="11.5" text-anchor="middle" '
                     f'fill="#fff" font-weight="700">{t["duree"]}</text>')
        else:
            # LA FENÊTRE : du plus tôt au plus tard. « Elle aurait pu être là-dedans. »
            wf = (t["tard_fin"] - t["tot_debut"]) * PX_SEANCE
            o.append(f'<rect x="{xa}" y="{y+5}" width="{wf}" height="{H_LIGNE-10}" rx="6" '
                     f'fill="none" stroke="{C_FEN}" stroke-width="1.4" '
                     f'stroke-dasharray="5 4"/>')
            # la même tâche, placée au plus tard : le fantôme
            o.append(f'<rect x="{xt}" y="{y+9}" width="{w}" height="{H_LIGNE-18}" rx="5" '
                     f'fill="{C_LIBRE_L}" stroke="{C_LIBRE}" stroke-width="1" '
                     f'stroke-dasharray="3 3"/>')
            o.append(f'<rect x="{xa}" y="{y+9}" width="{w}" height="{H_LIGNE-18}" rx="5" '
                     f'fill="{C_LIBRE}"/>')
            o.append(f'<text x="{xa+w/2}" y="{cy+4}" font-size="11.5" text-anchor="middle" '
                     f'fill="#fff" font-weight="700">{t["duree"]}</text>')
            o.append(f'<text x="{xa+wf+9}" y="{cy+4}" font-size="11.5" fill="{C_LIBRE}">'
                     f'marge {t["marge"]}</text>')

    # ── flèches de liaison ────────────────────────────────────────────────────
    for i in ids:
        t = T[i]
        for p in t["preds"]:
            a, b = T[p], t
            x1 = X_LIB + a["tot_fin"] * PX_SEANCE
            y1 = y0 + pos[p] * H_LIGNE + H_LIGNE / 2
            x2 = X_LIB + b["tot_debut"] * PX_SEANCE
            y2 = y0 + pos[i] * H_LIGNE + H_LIGNE / 2
            if x2 - x1 < 14:
                # le successeur enchaîne immédiatement : simple descente
                dy = 13 if y2 > y1 else -13
                d = f'M{x1},{y1} V{y2-dy}'
            else:
                mx = x2 - 10
                d = f'M{x1},{y1} H{mx} V{y2} H{x2-4}'
            o.append(f'<path d="{d}" fill="none" stroke="{C_FEN}" stroke-width="1.3" '
                     f'marker-end="url(#fl)"/>')

    # ── la légende : c'est elle qui enseigne ──────────────────────────────────
    ly = y0 + len(ids) * H_LIGNE + 26
    o.append(f'<line x1="{MARGE_H}" y1="{ly-12}" x2="{W-MARGE_H}" y2="{ly-12}" '
             f'stroke="{C_GRILLE}"/>')
    o.append(f'<rect x="{MARGE_H}" y="{ly}" width="30" height="13" rx="4" fill="{C_CRIT}"/>')
    o.append(f'<text x="{MARGE_H+38}" y="{ly+11}" font-size="12" fill="{C_TEXTE}">'
             f'<tspan font-weight="700">chemin critique</tspan> — aucun jeu : un jour de '
             f'retard ici, c\'est un jour de retard sur tout le projet.</text>')
    o.append(f'<rect x="{MARGE_H}" y="{ly+22}" width="30" height="13" rx="4" fill="{C_LIBRE}"/>')
    o.append(f'<text x="{MARGE_H+38}" y="{ly+33}" font-size="12" fill="{C_TEXTE}">'
             f'<tspan font-weight="700">tâche à marge</tspan> — elle a du jeu ; le '
             f'rectangle pointillé montre où elle aurait pu être placée sans rien retarder.</text>')
    o.append(f'<rect x="{MARGE_H}" y="{ly+44}" width="30" height="13" rx="4" fill="none" '
             f'stroke="{C_FEN}" stroke-dasharray="4 3"/>')
    o.append(f'<text x="{MARGE_H+38}" y="{ly+55}" font-size="12" fill="{C_TEXTE}">'
             f'<tspan font-weight="700">la fenêtre</tspan> — allonge une tâche à marge '
             f'jusqu\'à remplir son rectangle : elle devient critique, et le chemin change.</text>')
    o.append('</svg>')
    return "\n".join(o)


def main(csv_path, sortie):
    sortie = Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    projets = lire(csv_path)
    for nom, p in projets.items():
        T = p["taches"]
        fin = ordonnancer(T)
        (sortie / f"gantt_{nom}.svg").write_text(
            svg(nom, p["niveau"], T, fin), encoding="utf-8")

        corr = {"projet": nom, "niveau": p["niveau"], "duree_totale_seances": fin,
                "chemin_critique": sorted(i for i in T if T[i]["critique"]),
                "taches": {i: {k: T[i][k] for k in
                               ("tot_debut", "tot_fin", "tard_debut", "tard_fin",
                                "marge", "critique")} for i in T}}
        f = sortie / f"corrige_{nom}.json"
        f.write_text(json.dumps(corr, ensure_ascii=False, indent=2), encoding="utf-8")

        # règle n°71 : on RELIT ce qu'on vient d'écrire et on revérifie l'invariant
        relu = json.loads(f.read_text(encoding="utf-8"))
        assert all(relu["taches"][i]["marge"] == 0 for i in relu["chemin_critique"]), \
            "le fichier écrit contredit le calcul"
        assert sum(T[i]["duree"] for i in relu["chemin_critique"]) == relu["duree_totale_seances"]
        print(f"{nom:32s} {p['niveau']}  {fin} séances  "
              f"critique = {'-'.join(relu['chemin_critique'])}  (relu, vérifié)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "/home/claude/gantt_out")
