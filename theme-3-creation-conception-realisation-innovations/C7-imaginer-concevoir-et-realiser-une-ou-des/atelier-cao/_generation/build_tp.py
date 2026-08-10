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
  .capture-absente{margin:8px 0;padding:10px 12px;border:1px dashed #6b7a99;
    border-radius:8px;background:rgba(255,255,255,.03);color:#9bbefc;font-size:.9em}
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


MANQUANTES = []


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
        # Une capture annoncée mais absente affiche, dans le navigateur, un cadre
        # blanc cassé : l'élève croit que la page est en panne. On préfère le
        # dire, et le build tient la liste de ce qui manque.
        if not (D / e["capture"]).exists():
            MANQUANTES.append(e["capture"])
            out.append('<div class="capture-absente">📷 <b>Capture à venir</b> — '
                       "l'image de cet écran n'a pas encore été prise. "
                       "Le texte ci-dessus suffit pour agir&nbsp;: %s</div>"
                       % html.escape(e.get("capture_alt", "")))
        else:
            out.append('<figure class="capture"><img src="%s" alt="%s">'
                   % (esc(e["capture"]), html.escape(e.get("capture_alt", ""))))
            if e.get("capture_legende"):
                out.append("<figcaption>%s</figcaption>" % esc(e["capture_legende"]))
            out.append("</figure>")
    ex = e.get("exemple")
    if ex:
        # Une valeur citée dans le TEXTE se recopie aussi aveuglément qu'une
        # valeur lue sur une capture : la mention ne dépend donc pas de l'image.
        # `true` donne la phrase générique ; une chaîne donne l'explication
        # écrite pour cette valeur-là, ce qui vaut toujours mieux.
        txt = (esc(ex) if isinstance(ex, str) else
               "Cette valeur est <b>un exemple</b>&nbsp;: ne la recopie pas "
               "sans réfléchir, choisis la tienne.")
        out.append('<p class="exemple-note">⚠️ %s</p>' % txt)
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
        if not (D / p["image_resultat"]).exists():
            MANQUANTES.append(p["image_resultat"])
            out.append('<div class="capture-absente">📷 <b>Image du résultat à venir</b> — '
                       "voici ce que tu dois obtenir, en attendant la photo&nbsp;: %s</div>"
                       % html.escape(p.get("image_resultat_alt", "")))
        else:
            out.append('<div class="attendu"><b>Ce que tu dois obtenir&nbsp;:</b>'
                       '<figure class="capture"><img src="%s" alt="%s">'
                       % (esc(p["image_resultat"]),
                          html.escape(p.get("image_resultat_alt", ""))))
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

    # Règle d'or n°88 : un TP dans lequel on entre sans pouvoir revenir à sa
    # séquence est une impasse. Le scénario doit dire d'où l'on vient.
    rap = s.get("rappel_spiralaire") or {}
    if s.get("niveau") in ("4e", "3e") and not rap:
        raise SystemExit(
            "Règle n°87 (clé de voûte) : un TP de %s s'appuie sur un prérequis et doit\n"
            "s'ouvrir par un rappel de ce que l'élève a DÉJÀ PRODUIT.\n"
            'Ajoute au JSON : "rappel_spiralaire": {"deja": "…", "change": "…", "filet": "…"}'
            % s["niveau"])
    if rap and not (rap.get("deja") and rap.get("change")):
        raise SystemExit("Règle n°87 : le rappel doit dire ce qui a été FAIT (deja) "
                         "et ce qui CHANGE (change).")
    rappel = ("" if not rap else
              '<section class="card rappel-spiralaire" aria-labelledby="rap-t">\n'
              '  <h2 id="rap-t">&#128260; Ce que tu as déjà fait</h2>\n'
              '  <p class="deja">%s</p>\n  <p class="change">%s</p>\n%s</section>\n'
              % (rap["deja"], rap["change"],
                 ('  <p class="filet">%s</p>\n' % rap["filet"]) if rap.get("filet") else ""))

    retour = str(s.get("retour_sequence", "")).strip()
    if not retour:
        raise SystemExit(
            "Règle n°88 : le scénario n'indique pas « retour_sequence ».\n"
            "Ajoute au JSON, par exemple :\n"
            '    "retour_sequence": "../5e/5e_C7.1/sequence_5e_C7_mini-projet-objet.html"')
    if not (D / retour).exists():
        raise SystemExit("Règle n°88 : « retour_sequence » vise un fichier qui n'existe "
                         "pas : %s" % (D / retour))

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
.rappel-spiralaire{border-left:5px solid var(--accent,#61dafb)}
.rappel-spiralaire .change{margin:.6em 0;padding:.6em .8em;border-radius:8px;
 background:rgba(255,255,255,.04);border:1px dashed #274a8a}
.rappel-spiralaire .filet{font-size:.92em;opacity:.85}
#navharm{display:flex;flex-wrap:wrap;gap:10px;max-width:900px;margin:14px auto 0;padding:0 18px}
#navharm a{padding:6px 12px;border:1.5px solid #274a8a;border-radius:999px;background:#0d2347;
 color:#9bbefc;font-size:.92em;text-decoration:none;line-height:1.2}
#navharm a:hover{border-color:#61dafb;color:#61dafb}
@media print{#navharm{display:none}}
</style>
</head>
<body>
<nav id="navharm" aria-label="Navigation du site">
  <a href="../../../index.html">&#8962; Accueil</a>
  <a href="%(retour)s">&#8592; Revenir à la séquence de %(niveau)s</a>
  <a href="tp_modele_demonstration.html">&#128209; Le modèle de démonstration</a>
</nav>
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
%(rappel)s
%(corps)s

<section class="card et-ensuite">
  <h2>&#10145; Et maintenant&nbsp;?</h2>
  <p>Tu sais ouvrir un plan, esquisser, coter, extruder, enlever de la matière et adoucir une
  arête. <b>C'est tout ce qu'il faut</b> pour dessiner l'objet de ton projet.</p>
  <p><a class="btn" href="%(retour)s">&#8592; Revenir à ta séquence et dessiner ton support</a></p>
  <p class="note">Garde ton document&nbsp;: on repartira de ces gestes-là, en 4e, pour
  <b>assembler</b> deux pièces — et là, une pièce pourra en empêcher une autre de bouger.</p>
</section>
<footer>%(pied)s</footer>
</div>
</body>
</html>
""" % {"desc": html.escape(s.get("description", "")), "titre_page": html.escape(s["titre_page"]),
       "css": CSS, "css_tp": STYLE_TP, "titre": esc(s["titre"]), "sous": esc(s["sous_titre"]),
       "niveau": esc(s["niveau"]), "logiciel": esc(s["logiciel"]), "badges": badges,
       "corps": corps, "pied": esc(s.get("pied", "Ressource originale du dépôt.")),
       "retour": retour, "rappel": rappel}

    sortie = D / s["fichier_sortie"]
    sortie.write_text(page, encoding="utf-8")
    n_etapes = sum(len(p.get("etapes", [])) for p in paliers)
    print("TP écrit : %s (%d paliers, %d étapes, %d o)"
          % (sortie.name, len(paliers), n_etapes, sortie.stat().st_size))
    if MANQUANTES:
        print("\n%d capture(s) annoncée(s) mais absente(s) — la page l'indique "
              "au lieu d'afficher un cadre vide :" % len(MANQUANTES))
        for m in MANQUANTES:
            print("   · %s" % m)
        print("Tant qu'elles manquent, ce TP n'est pas publiable en l'état.")
    print("Étape suivante : python3 verif_guidage.py %s" % sortie.name)
    return sortie


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    construire(pathlib.Path(sys.argv[1]).resolve())
