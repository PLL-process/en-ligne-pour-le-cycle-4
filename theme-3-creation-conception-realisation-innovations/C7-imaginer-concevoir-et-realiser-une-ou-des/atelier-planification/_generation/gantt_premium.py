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
H_LIGNE   = 48      # n°315 : 16 unités d'air entre les fenêtres de deux lignes voisines
EC_FEN    = 8       # la fenêtre pointillée : 8 unités sous le haut de sa ligne (32 de haut)
EC_BARRE  = 13      # la barre et son fantôme : 13 unités sous le haut de sa ligne (22 de haut)
EC_MARGE  = 20      # le mot « marge N » : 20 unités après sa fenêtre, un couloir pour une flèche
AIR       = 8       # air minimal entre une flèche et une barre, une fenêtre, un losange ou un mot
X_LIB     = 340     # largeur de la colonne des libellés
MARGE_H   = 28
MARGE_B   = 96      # place pour la légende
ORDRE     = "calcule"   # ordre des lignes : "calcule" (flèches les plus simples) ou "plus_tot"


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


# ── Les flèches : un tracé qui ne traverse rien (règle d'or n°315) ─────────────
# Le 29/10/2026, le contrôle des schémas (`_outils/controle_schemas.mjs`) relève
# 19 défauts dans les trois Gantt : des flèches qui traversent une barre, une
# fenêtre pointillée, le mot « marge 1 » ; et les bandes grisées d'une ligne sur
# deux, qui portent le nom de la tâche, sont des cadres que toute flèche
# descendante coupe. Les bandes sont retirées (la grille des séances reste), et
# chaque flèche cherche son tracé, du plus simple au plus long :
#   • tomber du bout de la barre sur le coin de la suivante (dessin d'origine) ;
#   • descendre, puis entrer dans la suivante par la gauche ;
#   • descendre, puis se poser sur le dessus de la barre suivante ;
#   • les mêmes, en longeant un couloir entre deux lignes.
# Un tracé est refusé s'il passe à moins de AIR unités d'une barre, d'une
# fenêtre, d'un fantôme, d'un losange ou d'un mot qui ne sont pas les siens.
# Les barres restent sur la grille des séances : rien de ce qui est daté ne bouge.

def occupations(T, ids, pos):
    """Par ligne, les intervalles horizontaux occupés : (x0, x1, tâche, nature)."""
    occ = [[] for _ in ids]
    for i in ids:
        t, k = T[i], pos[i]
        xa = X_LIB + t["tot_debut"] * PX_SEANCE
        if t["jalon"]:
            occ[k] += [(xa - 11, xa + 11, i, "jalon"), (xa + 18, xa + 18 + 38, i, "mot")]
            continue
        w = t["duree"] * PX_SEANCE
        occ[k].append((xa, xa + w, i, "barre"))
        if not t["critique"]:
            xt = X_LIB + t["tard_debut"] * PX_SEANCE
            xf = X_LIB + t["tard_fin"] * PX_SEANCE
            mot = f"marge {t['marge']}"
            occ[k] += [(xa, xf, i, "fenetre"), (xt, xt + w, i, "fantome"),
                       (xf + EC_MARGE, xf + EC_MARGE + 7 * len(mot), i, "mot")]
    return occ


def _libre_v(x, ya, yb, occ, y0, permis):
    """Un trait vertical en x, de ya à yb, passe-t-il loin de tout ce qui n'est pas permis ?"""
    ya, yb = min(ya, yb), max(ya, yb)
    for k, L in enumerate(occ):
        b0 = y0 + k * H_LIGNE + EC_FEN
        b1 = y0 + (k + 1) * H_LIGNE - EC_FEN
        if b1 <= ya or b0 >= yb:
            continue
        for a, b, i, n in L:
            if (i, n) not in permis and a - AIR < x < b + AIR:
                return False
    return True


def _libre_h(xa, xb, ligne, permis):
    """Un trait horizontal au milieu d'une ligne, de xa à xb."""
    lo, hi = min(xa, xb), max(xa, xb)
    return all((i, n) in permis or not (a - AIR < hi and b + AIR > lo) for a, b, i, n in ligne)


def _longueur(pts):
    return sum(abs(pts[j + 1][0] - pts[j][0]) + abs(pts[j + 1][1] - pts[j][1])
               for j in range(len(pts) - 1))


def tracer(T, pos, occ, y0, p, i):
    """Le tracé le plus simple de la flèche p → i : (coût, points), ou None."""
    a, b = T[p], T[i]
    rp, rs = pos[p], pos[i]
    xa = X_LIB + a["tot_debut"] * PX_SEANCE
    xe = X_LIB + a["tot_fin"] * PX_SEANCE
    xs = X_LIB + b["tot_debut"] * PX_SEANCE
    ws = 0 if b["jalon"] else b["duree"] * PX_SEANCE
    yp = y0 + rp * H_LIGNE + H_LIGNE / 2
    ys = y0 + rs * H_LIGNE + H_LIGNE / 2
    x_in = xs - 13 if b["jalon"] else xs - 4      # la pointe touche la barre (le losange) par la gauche
    y_top = ys - 13                                # … ou son dessus
    soi = {(p, "barre"), (p, "fenetre")}
    permis = soi | {(i, "barre"), (i, "fenetre"), (i, "jalon")}
    sous = permis | {(p, "fantome")}               # sous la barre, son fantôme est caché par elle
    # départs : (points, x de la descente, y où elle commence, ce qui est permis)
    departs = []
    x1 = xe + 12
    while x1 <= xs + ws and _libre_h(xe, x1, occ[rp], soi):
        departs.append(([(xe, yp), (x1, yp)], x1, yp, permis))
        x1 += 2
    for x1 in range(int(xe - 10), int(xa + 8) - 1, -2):
        departs.append(([(x1, yp + 11)], x1, yp + 11, sous))
    if xs == xe:
        departs.append(([(xe, yp)], xe, yp, permis))
    # arrivées : (x de la dernière descente, y où elle finit, points de fin, pénalité)
    arrivees = [(x2, ys, [(x_in, ys)], 0.0)
                for x2 in range(int(x_in - 12), int(x_in - 12 - 4 * PX_SEANCE), -2)]
    if ws:
        arrivees += [(x2, y_top, [], 0.3) for x2 in range(int(xs + 10), int(xs + ws - 10) + 1, 2)]
    if xs == xe:
        arrivees.append((xs, y_top, [], 0.0))
    meilleur = None

    def garder(pts, c):
        nonlocal meilleur
        c += len(pts) + _longueur(pts) / 600
        if meilleur is None or c < meilleur[0]:
            meilleur = (c, pts)

    couloirs = [y0 + k * H_LIGNE for k in range(rp + 1, rs + 1)]   # entre deux lignes
    for pts0, x1, y1, perm1 in departs:                 # pts0 finit en (x1, y1)
        bas = []                                         # les couloirs que la descente atteint
        for yb in couloirs:
            if not _libre_v(x1, y1, yb, occ, y0, perm1):
                break
            bas.append(yb)
        for x2, y2, fin, pen in arrivees:
            if x2 == x1:                                 # une seule descente
                if _libre_v(x1, y1, y2, occ, y0, perm1):
                    garder(pts0 + [(x1, y2)] + fin, pen)
                continue
            for yb in bas:                               # descente, couloir, descente
                if y2 - yb >= 12 and _libre_v(x2, yb, y2, occ, y0, permis):
                    garder(pts0 + [(x1, yb), (x2, yb), (x2, y2)] + fin, pen + 1.5)
                    break
    return meilleur


def ordre_des_lignes(T):
    """Les lignes, de haut en bas. « plus_tot » : par date au plus tôt. « calcule » :
    parmi les ordres où chaque tâche est sous celles qu'elle attend, celui dont les
    flèches sont les plus simples et ne partagent aucun trait entre elles."""
    plus_tot = sorted(T, key=lambda i: (T[i]["tot_debut"], i))
    if ORDRE == "plus_tot":
        return plus_tot
    ordres = []

    def suite(pref, reste):
        if not reste:
            ordres.append(list(pref))
            return
        for i in sorted(reste):
            if all(q in pref for q in T[i]["preds"]):
                suite(pref + [i], reste - {i})

    suite([], set(T))
    meilleur = None
    for ids in ordres:
        c = cout_ordre(T, ids)
        if c is not None and (meilleur is None or c < meilleur[0]):
            meilleur = (c, ids)
    return meilleur[1] if meilleur else plus_tot


def _segments(pts):
    return [(pts[j], pts[j + 1]) for j in range(len(pts) - 1)]


def _voisins(s, t, ecart):
    """Deux segments parallèles, à moins de `ecart` unités l'un de l'autre, sur plus d'une unité ?"""
    (ax, ay), (bx, by) = s
    (cx, cy), (dx, dy) = t
    if ax == bx and cx == dx and abs(ax - cx) < ecart:
        return min(max(ay, by), max(cy, dy)) - max(min(ay, by), min(cy, dy)) > 1
    if ay == by and cy == dy and abs(ay - cy) < ecart:
        return min(max(ax, bx), max(cx, dx)) - max(min(ax, bx), min(cx, dx)) > 1
    return False


def liaisons(T, ids, y0):
    pos = {i: k for k, i in enumerate(ids)}
    occ = occupations(T, ids, pos)
    return [(p, i, tracer(T, pos, occ, y0, p, i)) for i in ids for p in T[i]["preds"]]


def cout_ordre(T, ids):
    L = liaisons(T, ids, 0)
    if any(r is None for _, _, r in L):
        return None
    c = sum(r[0] for _, _, r in L)
    for u in range(len(L)):
        for v in range(u + 1, len(L)):
            (p, i, r), (q, j, s) = L[u], L[v]
            if p == q:
                continue                    # deux flèches d'une même tâche partent ensemble : un faisceau
            paires = [(x, y) for x in _segments(r[1]) for y in _segments(s[1])]
            if i != j and any(_voisins(x, y, 3) for x, y in paires):
                c += 10                     # un trait commun à deux liaisons sans rapport : illisible
            elif any(_voisins(x, y, 16) for x, y in paires):
                c += 3                      # deux traits parallèles serrés : on ne sait plus lequel suivre
    return c


def svg(nom_projet, niveau, T, fin):
    ids = ordre_des_lignes(T)
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
    # Pointe en pixels (markerUnits="userSpaceOnUse") : 9 x le trait de 1,3 = 11,7 px de long, 9,1 de haut.
    # Elle tient dans le dernier segment de chaque tracé, long de 12 px au moins (décision de Pascal du
    # 24/10/2026 : on allonge le segment plutôt que de rapetisser la pointe).
    o.append('<defs><marker id="fl" viewBox="0 0 9 7" markerWidth="11.7" markerHeight="9.1" '
             'refX="8" refY="3.5" markerUnits="userSpaceOnUse" '
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
    hb = H_LIGNE - 2 * EC_BARRE                         # hauteur d'une barre
    for i in ids:
        t, k = T[i], pos[i]
        y = y0 + k * H_LIGNE
        cy = y + H_LIGNE / 2

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
            o.append(f'<rect x="{xa}" y="{y+EC_BARRE}" width="{w}" height="{hb}" rx="5" '
                     f'fill="{C_CRIT}"/>')
            o.append(f'<text x="{xa+w/2}" y="{cy+4}" font-size="11.5" text-anchor="middle" '
                     f'fill="#fff" font-weight="700">{t["duree"]}</text>')
        else:
            # LA FENÊTRE : du plus tôt au plus tard. « Elle aurait pu être là-dedans. »
            wf = (t["tard_fin"] - t["tot_debut"]) * PX_SEANCE
            o.append(f'<rect x="{xa}" y="{y+EC_FEN}" width="{wf}" height="{H_LIGNE-2*EC_FEN}" rx="6" '
                     f'fill="none" stroke="{C_FEN}" stroke-width="1.4" '
                     f'stroke-dasharray="5 4"/>')
            # la même tâche, placée au plus tard : le fantôme
            o.append(f'<rect x="{xt}" y="{y+EC_BARRE}" width="{w}" height="{hb}" rx="5" '
                     f'fill="{C_LIBRE_L}" stroke="{C_LIBRE}" stroke-width="1" '
                     f'stroke-dasharray="3 3"/>')
            o.append(f'<rect x="{xa}" y="{y+EC_BARRE}" width="{w}" height="{hb}" rx="5" '
                     f'fill="{C_LIBRE}"/>')
            o.append(f'<text x="{xa+w/2}" y="{cy+4}" font-size="11.5" text-anchor="middle" '
                     f'fill="#fff" font-weight="700">{t["duree"]}</text>')
            # un halo couleur du fond : la ligne de grille de la séance suivante passe sous le mot
            o.append(f'<text x="{xa+wf+EC_MARGE}" y="{cy+4}" font-size="11.5" fill="{C_LIBRE}" '
                     f'stroke="{C_FOND}" stroke-width="3" paint-order="stroke">'
                     f'marge {t["marge"]}</text>')

    # ── flèches de liaison ────────────────────────────────────────────────────
    for p, i, r in liaisons(T, ids, y0):
        assert r is not None, f"aucun tracé libre pour la flèche {p} → {i}"
        pts = r[1]
        d = f'M{pts[0][0]:g},{pts[0][1]:g}' + ''.join(
            f' H{x2:g}' if y2 == y1 else f' V{y2:g}'
            for (x1, y1), (x2, y2) in zip(pts, pts[1:]))
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
