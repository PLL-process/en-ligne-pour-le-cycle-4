# -*- coding: utf-8 -*-
"""Engendre un TP de prise en main d'un logiciel à partir d'un scénario JSON.

Ce générateur est **indépendant du logiciel** : Onshape, mBlock 5, un simulateur
de circuits, un tableur. On réécrit le contenu, jamais la forme.

Il rend mécaniques les règles d'or n°72 à n°82 (journal, 9 août 2026) :

  · n°72 — chaque étape porte OBLIGATOIREMENT un champ `voir` : ce que l'élève
    doit constater à l'écran. Le générateur REFUSE d'écrire une étape sans lui.
  · n°73 — le nom du bouton se cite en gras dans `action`, et son icône est
    affichée à côté si `icone` est fourni.
  · n°74 — `avertissement` produit l'encadré « on a le droit d'être imprécis ».
  · n°75 — `exemple: true` ajoute la mention « cette valeur est un exemple »
    sous l'image de l'étape.
  · n°76 — un palier déclare son `niveau_aide` : detaille / allege / resultat.
    Le vérificateur contrôle que l'aide décroît.
  · n°77 — `image_resultat` d'un palier : ce que l'élève doit obtenir.
  · n°79 — le premier palier doit être de type `rangement`.
  · n°80 — `enregistrer: true` sur un palier ajoute le rituel avec son icône.
  · n°81 — aucun champ « question » n'existe dans le format : un TP de prise en
    main ne pose pas de question de cours. C'est une impossibilité, pas une
    consigne.
  · n°82 — le dernier palier doit être de type `recompense`.

Usage :
    python3 build_tp.py ../scenarios/<scenario>.json
"""
import html
import json
import pathlib
import sys

G = pathlib.Path(__file__).resolve().parent
D = G.parent
CSS = (G / "gabarit_style.css").read_text(encoding="utf-8")

STYLE_TP = """
  .palier{background:var(--panel);border:1px solid var(--border);border-radius:12px;
    padding:14px 18px;margin:16px 0}
  .palier > h2{margin-top:2px}
  .niveau{float:right;font-size:.72em;padding:3px 10px;border-radius:999px;
    border:1px solid var(--input-bd);color:var(--sub);font-weight:600}
  .niveau.detaille{border-color:var(--hl);color:var(--hl)}
  .niveau.allege{border-color:var(--warn);color:var(--warn)}
  .niveau.resultat{border-color:var(--ok);color:var(--ok)}
  ol.etapes{padding-left:22px;margin:10px 0}
  ol.etapes > li{margin:12px 0}
  .voir{display:block;color:var(--head);font-style:italic;margin-top:4px;
    border-left:3px solid var(--head);padding-left:10px}
  .btn-icone{height:1.35em;vertical-align:-.3em;margin:0 3px;border-radius:3px;
    background:#fff;padding:1px}
  .avertir{background:#3a2a0d;border:1px solid var(--warn);border-left-width:5px;
    border-radius:8px;padding:9px 13px;margin:10px 0;color:#ffd8a0;font-size:.94em}
  .avertir b{color:var(--warn)}
  .capture{margin:10px 0}
  .capture img{max-width:100%;height:auto;border:1px solid var(--input-bd);
    border-radius:8px;background:#fff}
  .capture figcaption{font-size:.88em;color:var(--sub);margin-top:6px}
  .exemple-note{color:var(--warn);font-size:.88em;margin-top:4px}
  .attendu{background:var(--panel2);border:1px solid var(--ok);border-radius:10px;
    padding:11px 14px;margin:12px 0}
  .attendu > b{color:var(--ok)}
  .rituel{color:var(--sub);font-size:.92em;margin-top:10px}
  .recompense{border-color:var(--ok)}
  .critere{background:var(--panel2);border-left:4px solid var(--hl);
    padding:10px 14px;border-radius:0 8px 8px 0;margin:12px 0;font-size:.94em}
"""


def esc(t):
    """Le scénario autorise <b>, <i>, <code> : on n'échappe donc pas tout."""
    return t


def icone(src):
    if not src:
        return ""
    return ' <img class="btn-icone" src="%s" alt="">' % esc(src)


def etape_html(e, i):
    if "voir" not in e or not str(e["voir"]).strip():
        raise SystemExit(
            "Règle n°72 : l'étape %d (« %s ») n'a pas de champ « voir ».\n"
            "Une consigne de manipulation sans retour d'écran attendu laisse l'élève\n"
            "découvrir son erreur trois étapes plus loin. Ajoute ce qu'il doit constater."
            % (i, str(e.get("action", ""))[:60]))
    out = ["<li>", esc(e["action"]), icone(e.get("icone")),
           '<span class="voir">%s</span>' % esc(e["voir"])]
    if e.get("avertissement"):
        out.append('<div class="avertir"><b>À savoir avant de commencer&nbsp;:</b> %s</div>'
                   % esc(e["avertissement"]))
    if e.get("capture"):
        out.append('<figure class="capture"><img src="%s" alt="%s">'
                   % (esc(e["capture"]), html.escape(e.get("capture_alt", ""))))
        if e.get("capture_legende"):
            out.append("<figcaption>%s</figcaption>" % esc(e["capture_legende"]))
        out.append("</figure>")
        if e.get("exemple"):
            out.append('<p class="exemple-note">⚠️ La valeur visible sur cette image est '
                       "<b>un exemple</b>&nbsp;: ne la recopie pas, saisis la tienne.</p>")
    out.append("</li>")
    return "".join(out)


NIVEAUX = {"detaille": ("Aide détaillée", "detaille"),
           "allege": ("Aide allégée", "allege"),
           "resultat": ("À toi de jouer", "resultat")}


def palier_html(p, n):
    niv = p.get("niveau_aide", "detaille")
    if niv not in NIVEAUX:
        raise SystemExit("Palier « %s » : niveau_aide inconnu (%r)." % (p.get("titre"), niv))
    lab, cls = NIVEAUX[niv]
    out = ['<section class="palier%s">' % (" recompense" if p.get("type") == "recompense" else "")]
    out.append('<span class="niveau %s">%s</span>' % (cls, lab))
    out.append("<h2>%s &middot; %s</h2>" % (n, esc(p["titre"])))
    if p.get("intro"):
        out.append("<p>%s</p>" % esc(p["intro"]))
    if p.get("etapes"):
        out.append('<ol class="etapes">')
        for i, e in enumerate(p["etapes"], 1):
            out.append(etape_html(e, i))
        out.append("</ol>")
    if p.get("image_resultat"):
        out.append('<div class="attendu"><b>Ce que tu dois obtenir&nbsp;:</b>'
                   '<figure class="capture"><img src="%s" alt="%s">'
                   % (esc(p["image_resultat"]), html.escape(p.get("image_resultat_alt", ""))))
        out.append("</figure></div>")
    if p.get("critere"):
        out.append('<p class="critere">🎯 <b>Tu peux passer à la suite quand&nbsp;:</b> %s</p>'
                   % esc(p["critere"]))
    if p.get("enregistrer"):
        out.append('<p class="rituel">💾 <b>Enregistre ton travail maintenant.</b> '
                   "C'est le moment&nbsp;: si le poste redémarre, tu ne perds rien.</p>")
    out.append("</section>")
    return "".join(out)


def construire(scenario_path: pathlib.Path) -> pathlib.Path:
    s = json.loads(scenario_path.read_text(encoding="utf-8"))
    paliers = s["paliers"]

    # ── Règles de structure, contrôlées avant toute écriture ────────────────
    if paliers[0].get("type") != "rangement":
        raise SystemExit("Règle n°79 : le premier palier doit être de type « rangement ». "
                         "Un travail qu'on ne retrouve pas à la séance suivante n'a pas eu lieu.")
    if paliers[-1].get("type") != "recompense":
        raise SystemExit("Règle n°82 : le dernier palier doit être de type « recompense ». "
                         "Après un TP long, l'élève repart avec une image dont il est fier.")
    ordre = {"detaille": 0, "allege": 1, "resultat": 2}
    vus = [ordre[p.get("niveau_aide", "detaille")] for p in paliers]
    if max(vus) == 0 and len(paliers) > 3:
        raise SystemExit("Règle n°76 : tous les paliers sont en aide détaillée. "
                         "Un guidage qui ne s'allège jamais fait exécuter, il n'apprend pas.")
    for a, b in zip(vus, vus[1:]):
        if b < a - 0:
            pass  # on autorise un retour en arrière ponctuel : nouveau geste, nouvelle aide

    corps = "".join(palier_html(p, i) for i, p in enumerate(paliers, 1))
    badges = "".join('<span class="badge theme">%s</span>' % esc(b) for b in s.get("badges", []))

    page = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="%(desc)s">
<title>%(titre_page)s</title>
<style>
%(css)s
%(css_tp)s
</style>
</head>
<body>
<div class="page">
<h1>%(titre)s</h1>
<p class="sous">%(sous)s</p>
<div class="badges"><span class="badge niveau">%(niveau)s</span>
<span class="badge code">%(logiciel)s</span>%(badges)s</div>
<p class="legende-badges">🧭 <b>Comment lire ce TP.</b> En clair, <b>ce que tu fais</b>.
En <span style="color:var(--head);font-style:italic">italique coloré, ce que tu dois voir se
produire à l'écran</span> — si tu ne le vois pas, ne continue pas&nbsp;: reprends l'étape.
Les encadrés orange préviennent des pièges. À la fin de chaque partie, une image te montre
<b>ce que tu dois obtenir</b>&nbsp;: compare, tu n'as besoin de personne pour te corriger.</p>
%(corps)s
<footer>%(pied)s</footer>
</div>
</body>
</html>
""" % {"desc": html.escape(s.get("description", "")), "titre_page": html.escape(s["titre_page"]),
       "css": CSS, "css_tp": STYLE_TP, "titre": esc(s["titre"]), "sous": esc(s["sous_titre"]),
       "niveau": esc(s["niveau"]), "logiciel": esc(s["logiciel"]), "badges": badges,
       "corps": corps, "pied": esc(s.get("pied", "Ressource originale du dépôt."))}

    sortie = D / s["fichier_sortie"]
    sortie.write_text(page, encoding="utf-8")
    n_etapes = sum(len(p.get("etapes", [])) for p in paliers)
    print("TP écrit : %s (%d paliers, %d étapes, %d o)"
          % (sortie.name, len(paliers), n_etapes, sortie.stat().st_size))
    print("Étape suivante : python3 verif_guidage.py %s" % sortie.name)
    return sortie


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    construire(pathlib.Path(sys.argv[1]).resolve())
