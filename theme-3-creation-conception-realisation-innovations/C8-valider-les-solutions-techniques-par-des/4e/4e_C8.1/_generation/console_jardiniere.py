# -*- coding: utf-8 -*-
"""La console de la jardinière — ce que la simulation de 4e_C8.1 calcule, et l'activité qui la fait régler.

Pourquoi ce fichier (audit du 22/11/2026, #867, chantier 6 ; décision de Pascal du 22/11, « 1 oui ») :
le code 4e_C8.1 demande de PARAMÉTRER une simulation fournie pour valider la TENUE MÉCANIQUE D'UN MATÉRIAU.
Le lot n'avait qu'un banc de comportement (l'arrosage sous la pluie, le gel, la LED) : ni matériau, ni charge,
ni déformation. Cette activité comble ce manque, sur le modèle de 5e_C8.1 (la patère du hall) — en 5e, la
simulation arrive réglée ; en 4e, c'est l'élève qui entre les valeurs (fiche de 5e_C8.1, « spirale C8 »).

Un seul endroit décide des chiffres : ce modèle (règle d'or n°233). Les matériaux viennent du modèle de la
patère de 5e (`5e_C8.1/patere.py`) : les mêmes limites, d'un niveau à l'autre. La page reçoit les matériaux en
JSON ; le banc `tests_simulation_4e_C8.1.mjs` interroge la page et vérifie qu'elle dit exactement ce que ce
modèle calcule, pour toute la grille des cas.

La console est une poutre encastrée dans le muret, chargée à son extrémité (le milieu de la jardinière) :

    contrainte de flexion   σ = F · L / (I/v),   F = m · g,   I/v = b · e² / 6   (section rectangulaire)
    coefficient de sécurité k = σ_e / σ           (sur la LIMITE ÉLASTIQUE : au-delà, la console plie pour toujours)

Depuis le 25/11/2026, le même modèle écrit aussi l'activité 2 ter (4e_C8.2) : le protocole de l'essai RÉEL de la
console, que l'élève propose — la charge d'essai (3 × 11 kg), les paliers, la flèche que le calcul prévoit
(f = F·L³ / 3EI, tant que la console reste élastique) et le critère.

    python3 console_jardiniere.py            # imprime le tableau, et vérifie que la page est à jour (sortie 1 sinon)
    python3 console_jardiniere.py --ecrire   # écrit l'activité dans la séquence, et les attendus du banc
"""

import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
LOT = os.path.dirname(ICI)
SEQUENCE = os.path.join(LOT, "sequence_4e_C8_jardin-validation.html")
SYNTHESE = os.path.join(LOT, "synthese_eleve_4e_C8.html")
ATTENDUS = os.path.join(ICI, "console_attendus.json")
PATERE = os.path.normpath(os.path.join(LOT, "..", "..", "5e", "5e_C8.1"))

sys.path.insert(0, PATERE)
import patere as P  # noqa: E402  — les matériaux de la patère de 5e : une seule source

# ── la situation ───────────────────────────────────────────────────────────────────────────────────────
TERRE = 16             #: kg — la jardinière de 60 cm pleine de terre mouillée
NEIGE = 6              #: kg — la neige d'une tempête de janvier, à New York, sur la jardinière
CONSOLES = 2           #: consoles sous chaque jardinière
CHARGE = (TERRE + NEIGE) / CONSOLES   #: 11 kg par console — le cas le plus défavorable
LARGEUR = 30.0         #: mm — la largeur de la console (b)
LONGUEUR = 150.0       #: mm — du muret au milieu de la jardinière (L), là où le poids s'applique
COEF_EXIGE = 3         #: le cahier des charges : la console tient trois fois la charge la plus lourde
G = P.G                #: N/kg
PROPOSITION = ("PLA imprimé en 3D", 6)   #: la console du club : ce que l'imprimante fait vite
EPAISSEURS = [6, 8, 10, 12, 15, 20]       #: mm — les épaisseurs que l'élève essaie

# Les matériaux et ce qu'un toit leur fait (le soleil d'été, le gel, la pluie) : la simulation ne le calcule
# pas, l'élève le lit à côté du résultat. Les limites mécaniques, elles, viennent du modèle de 5e.
TOIT = {
    "Bois (pin)": "gonfle et pourrit si l'eau reste : sur un toit, il faut le traiter.",
    "PLA imprimé en 3D": "ramollit vers 55 degrés Celsius : au soleil d'été, sur un toit, une console sombre peut y arriver.",
    "PVC rigide": "ne craint pas l'eau ; devient cassant au froid et après quelques années de soleil.",
    "Aluminium": "ne rouille pas : sa couche d'oxyde le protège toute seule.",
    "Acier doux": "rouille sous la pluie s'il n'est pas galvanisé.",
}
MATERIAUX = [m for m in P.MATERIAUX]


def contrainte(sigma_e_inutile, epaisseur, longueur, charge):
    """σ en MPa (N/mm²) pour une console de largeur LARGEUR."""
    module = LARGEUR * epaisseur ** 2 / 6.0
    return charge * G * longueur / module


def calcul(nom, epaisseur, longueur=LONGUEUR, charge=CHARGE):
    m = P.PAR_NOM[nom]
    s = contrainte(None, epaisseur, longueur, charge)
    k = m.sigma_e / s if s > 0 else float("inf")
    if s > m.sigma_r:
        etat = "casse"
    elif s > m.sigma_e:
        etat = "plie"
    elif k < COEF_EXIGE:
        etat = "tient-insuffisant"
    else:
        etat = "valide"
    return {"materiau": nom, "epaisseur": epaisseur, "longueur": longueur, "charge": charge,
            "sigma": arrondi(s, 1), "k": arrondi(k, 2), "etat": etat}


def arrondi(x, d):
    """L'arrondi de la page (Math.round : la moitié monte), et non celui de Python (au pair le plus proche)."""
    import math
    f = 10 ** d
    return math.floor(x * f + 0.5) / f


def plus_petite_epaisseur(nom):
    for e in EPAISSEURS:
        if calcul(nom, e)["etat"] == "valide":
            return e
    return None


def nombre(x, dec=1):
    """Écriture française : virgule décimale."""
    return ("%." + str(dec) + "f") % x if dec else "%d" % round(x)


def fr(x, dec=1):
    return nombre(x, dec).replace(".", ",")


# ── les attendus, pour la page et pour le banc ──────────────────────────────────────────────────────────
def attendus():
    grille = []
    for m in MATERIAUX:
        for e in EPAISSEURS + [7, 25]:
            for L in (100, 150, 200):
                for c in (8, 11, 16, 22):
                    grille.append(calcul(m.nom, e, L, c))
    return {
        "_lire": "Écrit par _generation/console_jardiniere.py --ecrire : ce que la simulation de l'activité 2 bis "
                 "doit afficher, cas par cas. Le banc tests_simulation_4e_C8.1.mjs compare la page à ces valeurs.",
        "charge": CHARGE, "longueur": LONGUEUR, "largeur": LARGEUR, "coef_exige": COEF_EXIGE,
        "proposition": calcul(*PROPOSITION),
        "plus_petites": {m.nom: plus_petite_epaisseur(m.nom) for m in MATERIAUX},
        "grille": grille,
        "protocole": protocole_attendu(),
    }


def protocole_attendu():
    """Ce que l'activité 2 ter doit dire (25/11/2026) : le banc tests_protocole_4e_C8.1.mjs le compare à la page."""
    e = plus_petite_epaisseur(MATIERE)
    return {"materiau": MATIERE, "epaisseur": e, "charge_essai": CHARGE_ESSAI, "paliers": PALIERS, "sac": SAC,
            "fleches": [arrondi(fleche(MATIERE, e, c), 1) for c in PALIERS],
            "sigma_essai": calcul(MATIERE, e, LONGUEUR, CHARGE_ESSAI)["sigma"],
            "sigma_e": P.PAR_NOM[MATIERE].sigma_e, "tenue_min": TENUE_MIN, "retour_max": RETOUR_MAX,
            "eprouvettes": EPROUVETTES}


# ── le schéma : la console vue de côté, les quatre réglages nommés ─────────────────────────────────────
SVG = """<svg viewBox="0 0 660 330" role="img" aria-labelledby="consT consD" class="schema-console">
<title id="consT">La console de la jardinière, vue de côté, et les quatre réglages de la simulation</title>
<desc id="consD">À gauche, le muret du toit. Une console horizontale sort du muret ; la jardinière est posée dessus.
Son poids s'applique au milieu de la jardinière, à 150 millimètres du muret : c'est la longueur L. La console a une
épaisseur e, vue de côté, et une largeur de 30 millimètres. Les quatre réglages sont le matériau, l'épaisseur,
la longueur et la charge.</desc>
<defs><marker id="consFl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="9" markerHeight="9" orient="auto">
<path d="M0 0 10 5 0 10z" fill="currentColor"/></marker>
<pattern id="consMur" width="22" height="14" patternUnits="userSpaceOnUse"><rect width="22" height="14" fill="#12305e"/>
<path d="M0 7h22M11 0v7M0 14h22" stroke="#274a8a" stroke-width="1.4"/></pattern></defs>
<rect x="20" y="40" width="80" height="270" fill="url(#consMur)"/>
<text x="60" y="30" text-anchor="middle" fill="#9bbefc" font-size="20">muret</text>
<rect x="100" y="196" width="330" height="20" rx="3" fill="#ffd66b"/>
<text x="360" y="242" text-anchor="middle" fill="#ffd66b" font-size="20" font-weight="bold">la console</text>
<path d="M140 120h250l-14 72H154z" fill="#3aa76d" stroke="#81fba1" stroke-width="2"/>
<path d="M160 120q22-16 44 0M326 120q22-16 44 0" fill="none" stroke="#81fba1" stroke-width="3"/>
<text x="265" y="152" text-anchor="middle" fill="#fff" font-size="20" font-weight="bold">jardinière</text>
<text x="265" y="176" text-anchor="middle" fill="#e4eaf5" font-size="16">terre, et neige l'hiver</text>
<line x1="265" y1="30" x2="265" y2="112" stroke="#ff7b88" stroke-width="4" marker-end="url(#consFl)" color="#ff7b88"/>
<text x="277" y="52" fill="#ff7b88" font-size="20" font-weight="bold">charge (kg)</text>
<line x1="100" y1="282" x2="263" y2="282" stroke="#61dafb" stroke-width="2.5" marker-end="url(#consFl)" color="#61dafb"/>
<line x1="100" y1="274" x2="100" y2="290" stroke="#61dafb" stroke-width="2.5"/>
<line x1="265" y1="226" x2="265" y2="288" stroke="#61dafb" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="106" y="312" fill="#61dafb" font-size="20" font-weight="bold">longueur L = 150 mm</text>
<line x1="460" y1="196" x2="460" y2="216" stroke="#c68ef2" stroke-width="2.5"/>
<line x1="440" y1="196" x2="480" y2="196" stroke="#c68ef2" stroke-width="1.5"/>
<line x1="440" y1="216" x2="480" y2="216" stroke="#c68ef2" stroke-width="1.5"/>
<text x="490" y="203" fill="#c68ef2" font-size="20" font-weight="bold">épaisseur e</text>
<text x="490" y="224" fill="#c68ef2" font-size="17">(largeur : 30 mm)</text>
<text x="490" y="262" fill="#e4eaf5" font-size="20" font-weight="bold">+ le matériau</text>
</svg>"""


def tableau_correction():
    """Le tableau du PLA, épaisseur par épaisseur — engendré, jamais recopié."""
    lignes = []
    for e in EPAISSEURS:
        r = calcul("PLA imprimé en 3D", e)
        verdict = {"casse": "✘ casse", "plie": "✘ plie pour toujours",
                   "tient-insuffisant": "⚠ tient, mais k &lt; 3", "valide": "✔ validée"}[r["etat"]]
        lignes.append("<tr%s><td>%d mm</td><td>%s MPa</td><td>%s</td><td>%s</td></tr>"
                      % (' class="choisie"' if e == plus_petite_epaisseur("PLA imprimé en 3D") else "",
                         e, fr(r["sigma"]), fr(r["k"], 2), verdict))
    return "\n".join(lignes)


def tableau_materiaux():
    """Une ligne par matériau (une liste, pas un tableau : elle se lit sur un téléphone sans défiler de côté)."""
    lignes = []
    for m in MATERIAUX:
        e = plus_petite_epaisseur(m.nom)
        lignes.append("<li><b>%s</b> — plie au-dessus de %d MPa&nbsp;; validé à partir de <b>%s</b>.<br>Sur un toit&nbsp;: %s</li>"
                      % (html.escape(m.nom), m.sigma_e, ("%d mm" % e) if e else "plus de 20 mm",
                         html.escape(TOIT[m.nom], quote=False)))
    return "\n".join(lignes)


def options_radio(nom, propositions, bonne):
    """Un groupe de boutons radio (n°300) ; la place de la bonne réponse est fixée ici, jamais toujours la même."""
    sortie = []
    for i, p in enumerate(propositions, 1):
        sortie.append('  <div class="qcm-option"><input type="radio" name="%s" id="%s__%d" value="%s">'
                      '<label for="%s__%d">%s</label></div>' % (nom, nom, i, html.escape(p, quote=True), nom, i, p))
    assert bonne in propositions
    return "\n".join(sortie)


def fragment():
    prop = calcul(*PROPOSITION)
    min_pla = plus_petite_epaisseur("PLA imprimé en 3D")
    pla8 = calcul("PLA imprimé en 3D", 8)
    pla12 = calcul("PLA imprimé en 3D", 12)
    pla15 = calcul("PLA imprimé en 3D", 15)
    toute = calcul(PROPOSITION[0], PROPOSITION[1], LONGUEUR, TERRE + NEIGE)
    mats = [{"nom": m.nom, "se": m.sigma_e, "sr": m.sigma_r} for m in MATERIAUX]
    puces = "\n".join(
        '  <label class="puce-mat"><input type="radio" name="simMat" value="%s"%s> %s</label>'
        % (html.escape(m.nom, quote=True), " checked" if m.nom == PROPOSITION[0] else "", html.escape(m.nom))
        for m in MATERIAUX)
    Q1 = ["16 kg", "22 kg", "11 kg", "8 kg"]
    Q2 = ["k = %s : elle tient, mais k est plus petit que 3" % fr(calcul(PROPOSITION[0], 10)["k"], 2),
          "k = %s : elle casse" % fr(prop["k"], 2),
          "k = %s : elle casse" % fr(toute["k"], 2),
          "k = %s : elle est validée" % fr(pla15["k"], 2)]
    Q3 = ["8 mm", "10 mm", "12 mm", "%d mm" % min_pla, "20 mm"]
    Q4 = ["Pour savoir quel réglage a changé le résultat",
          "Parce que la simulation refuse deux changements à la fois",
          "Pour faire moins de calculs à la main",
          "Pour que le coefficient de sécurité monte plus vite"]
    a = {"Q1": Q1, "Q2": Q2, "Q3": Q3, "Q4": Q4}
    bonnes = {"Q1": "11 kg", "Q2": Q2[1], "Q3": "%d mm" % min_pla, "Q4": Q4[0]}
    js_bonnes = json.dumps({"a6q1": bonnes["Q1"], "a6q2": html.unescape(bonnes["Q2"]),
                            "a6q3": bonnes["Q3"], "a6q4": bonnes["Q4"]}, ensure_ascii=False)
    return """<!-- debut:act-simulation — engendré par _generation/console_jardiniere.py, ne pas éditer à la main -->
<style>
#act2bis .schema-console{width:100%%;max-width:620px;height:auto;display:block;margin:10px auto;background:#081b3a;border-radius:10px}
#act2bis .simu{background:#081733;border:1.5px solid var(--hl);border-radius:12px;padding:14px;margin:12px 0;text-align:left}
#act2bis .simu h4{margin:0 0 8px;color:var(--hl)}
#act2bis .parametres-mat{border:1px solid var(--border);border-radius:10px;padding:8px 10px;margin:8px 0}
#act2bis .parametres-mat{display:flex;flex-wrap:wrap;gap:4px 14px;text-align:left}
#act2bis .parametres-mat legend{padding:0 4px}
#act2bis .puce-mat{display:inline-flex;align-items:center;gap:6px;margin:4px 0;font-size:.95em;white-space:nowrap}
#act2bis .cmd{display:grid;grid-template-columns:max-content minmax(90px,140px);gap:8px 12px;align-items:center;justify-content:start;margin:8px 0}
#act2bis .cmd input[type=number]{width:100%%;font-size:16px}
#act2bis .sortie-simu{margin:10px 0;padding:10px 12px;border-radius:10px;line-height:1.55}
#act2bis .sortie-simu:empty{display:none}
#act2bis .sortie-simu.ok{background:rgba(129,251,161,.12);border-left:4px solid var(--ok)}
#act2bis .sortie-simu.ko{background:rgba(255,123,136,.10);border-left:4px solid var(--err)}
#act2bis table.releve{width:100%%;border-collapse:collapse;font-size:.86em;margin:8px 0}
#act2bis table.releve th,#act2bis table.releve td{border:1px solid var(--border);padding:5px 7px;text-align:left}
#act2bis #simReleve{font-size:.85em}
#act2bis #simReleve th,#act2bis #simReleve td{padding:4px 6px;white-space:nowrap}
/* sur téléphone, chaque essai tient sur ses lignes : rien ne défile de côté (n°364) */
@media(max-width:600px){
  #act2bis #simReleve,#act2bis #simReleve tbody{display:block;overflow:visible;width:100%%}
  #act2bis #simReleve thead{display:none}
  #act2bis #simReleve caption{display:block;width:100%%;text-align:left}
  #act2bis #simReleve tr{display:block;border:1px solid var(--border);border-radius:8px;margin:6px 0;padding:4px 6px}
  #act2bis #simReleve td{display:inline-block;border:0;padding:2px 8px 2px 0}
  #act2bis #simReleve td[data-l]::before{content:attr(data-l)}
  #act2bis #simReleve td[data-u]::after{content:attr(data-u)}
}
#act2bis table.releve th{background:#173666;color:var(--hl)}
#act2bis table.releve caption{text-align:left;color:var(--sub);font-size:.95em;padding:4px 0}
#act2bis table.releve tr.ok td{background:rgba(129,251,161,.10)}
#act2bis table.releve tr.ko td{background:rgba(255,123,136,.08)}
#act2bis table.releve tr.choisie td{outline:2px solid var(--ok)}
#act2bis .ecart{border-left:4px solid var(--warn);background:rgba(255,214,102,.08);padding:9px 13px;border-radius:0 10px 10px 0;margin:10px 0}
#act2bis .petit{font-size:.88em;color:var(--sub)}
#act2bis .materiaux-toit li{margin:6px 0}
@media(max-width:520px){#act2bis .cmd{grid-template-columns:1fr}}
@media print{#act2bis .simu,#act2bis .sortie-simu{background:#fff!important;color:#111!important}#act2bis .schema-console{background:#081b3a}}
</style>
<section class="card" id="act2bis">
<h2>🧮 Activité 2 bis — La console tiendra-t-elle&nbsp;? Paramétrer une simulation (C8.1) <span class="chrono">⏱ ~15 min</span></h2>
<div class="exo">
<p>Sur le toit, le club veut accrocher ses jardinières au muret.
<br>Chaque jardinière est posée sur <b>deux consoles</b> (une console&nbsp;: une barre fixée au mur, qui porte une charge en avançant dans le vide).</p>
<p>Avant d'en imprimer quarante, on vérifie qu'elles tiennent — sans en casser une seule&nbsp;: on <b>simule</b>.
<br>La simulation est fournie&nbsp;: c'est toi qui la <b>règles</b>.</p>
<div class="ecart"><b>Le cahier des charges</b>&nbsp;: chaque console tient <b>3 fois</b> la charge la plus lourde qu'elle portera.
<br>On l'écrit avec un nombre, le <b>coefficient de sécurité k</b>&nbsp;: il doit valoir <b>3 ou plus</b>.</div>
<p><b>Les données</b>&nbsp;:
<br>· la jardinière pleine de terre mouillée pèse <b>%(terre)d kg</b>&nbsp;;
<br>· après une tempête de janvier, la neige posée dessus pèse <b>%(neige)d kg</b> de plus&nbsp;;
<br>· la console proposée par le club&nbsp;: <b>PLA imprimé en 3D, %(e0)d mm d'épaisseur</b> — c'est ce que l'imprimante fait le plus vite.</p>
%(svg)s
<p><b>Q1 — Quelle charge entres-tu dans la simulation, pour UNE console&nbsp;?</b>
<br>Fais le calcul sur une feuille de brouillon avant de choisir.</p>
<fieldset class="qcm-groupe" id="a6q1">
  <legend>Q1 — La charge d'une console, dans le cas le plus lourd</legend>
%(q1)s
</fieldset>

<div class="simu" id="simuConsole">
<h4>🧮 La simulation fournie — règle-la, puis lance-la</h4>
<p class="petit">Le schéma ci-dessus nomme les quatre réglages.</p>
<fieldset class="parametres-mat"><legend>① Le matériau</legend>
%(puces)s
</fieldset>
<div class="cmd">
<label for="simEp">② L'épaisseur e (millimètres)</label> <input type="number" id="simEp" min="2" max="40" step="1" value="%(e0)d" inputmode="numeric">
<label for="simLong">③ La longueur L (millimètres)</label> <input type="number" id="simLong" min="50" max="400" step="10" value="%(L)d" inputmode="numeric">
<label for="simCharge">④ La charge (kilogrammes)</label> <input type="number" id="simCharge" min="1" max="60" step="1" value="" placeholder="ta réponse à Q1" inputmode="numeric">
</div>
<button class="btn" id="simLancer" type="button">▶ Lancer la simulation</button>
<div id="simSortie" class="sortie-simu" role="status" aria-live="polite"></div>
<table class="releve" id="simReleve" aria-label="Le relevé de tes essais"><caption>Le relevé de tes essais (le dernier en haut)</caption>
<thead><tr><th>Matériau</th><th>e (millimètres, mm)</th><th>L (millimètres, mm)</th><th>charge (kilogrammes, kg)</th><th>σ (mégapascals, MPa)</th><th>k</th><th>Résultat</th></tr></thead><tbody></tbody></table>
<p class="petit"><b>Ce que la simulation suppose</b>&nbsp;: une console neuve, fixée solidement dans le muret, le poids posé au milieu de la jardinière, à température ordinaire.
<br>Elle ne dit rien du soleil, de l'eau ou du gel&nbsp;: ça, c'est à toi de le lire à côté.
<br>σ (sigma) est la <b>contrainte</b>&nbsp;: l'effort que supporte chaque millimètre carré de la console, en MPa (mégapascals).
<br>La <b>limite élastique</b> d'un matériau est la contrainte au-delà de laquelle il plie pour toujours.</p>
</div>

<p><b>Q2 — Règle la simulation sur la console du club</b> (PLA imprimé en 3D, %(e0)d mm, %(L)d mm, et ta charge de Q1), lance-la. Que lis-tu&nbsp;?</p>
<fieldset class="qcm-groupe" id="a6q2">
  <legend>Q2 — Ce que dit la simulation pour la console du club</legend>
%(q2)s
</fieldset>

<p><b>Q3 — Le club garde le PLA. Change UN SEUL réglage&nbsp;: l'épaisseur.</b>
<br>Essaie au moins trois épaisseurs, puis réponds&nbsp;: quelle est la plus petite épaisseur qui respecte le cahier des charges&nbsp;?</p>
<fieldset class="qcm-groupe" id="a6q3">
  <legend>Q3 — La plus petite épaisseur de PLA validée</legend>
%(q3)s
</fieldset>

<p><b>Q4 — Pourquoi ne change-t-on qu'un seul réglage à la fois&nbsp;?</b></p>
<fieldset class="qcm-groupe" id="a6q4">
  <legend>Q4 — Un seul réglage à la fois</legend>
%(q4)s
</fieldset>

<p><b>Q5 — Ta décision, en une ou deux phrases</b>&nbsp;: valides-tu la console du club&nbsp;? Que proposes-tu&nbsp;? Donne le nombre qui le prouve.</p>
<textarea id="a6dec" rows="3" placeholder="Je ne valide pas la console de … mm, parce que k = … Je propose …" aria-label="Q5 — ta décision, avec le nombre qui la prouve"></textarea>
<button class="btn check" data-check="6" type="button">✅ Vérifier l'activité 2 bis</button>
<p class="feedback" id="fb6" role="status"></p>
<details class="correction"><summary>📖 Correction complète (à ouvrir APRÈS tes essais)</summary><div>
<p><b>Q1 — 11 kg.</b>
<br>Le cahier des charges parle de la charge <b>la plus lourde</b>&nbsp;: c'est l'hiver, terre ET neige, %(terre)d + %(neige)d = %(total)d kg.
<br>Deux consoles se partagent la jardinière&nbsp;: chacune porte la moitié, %(total)d ÷ 2 = <b>11 kg</b>.
<br>· 16 kg oublie la neige&nbsp;; · 22 kg oublie que les consoles sont deux&nbsp;; · 8 kg partage la terre et oublie la neige.</p>
<p><b>Q2 — k = %(kprop)s&nbsp;: elle casse.</b>
<br>Réglages&nbsp;: PLA, e = %(e0)d mm, L = %(L)d mm, charge = 11 kg.
<br>La simulation donne σ = %(sprop)s MPa.
<br>Le PLA plie pour toujours au-dessus de %(se_pla)d MPa et casse au-dessus de %(sr_pla)d MPa&nbsp;: à %(sprop)s MPa, la console <b>casse</b>.
<br>k = %(se_pla)d ÷ %(sprop)s = <b>%(kprop)s</b>&nbsp;: bien moins que 3.
<br>Avec 22 kg (une seule console pour toute la jardinière), on lirait k = %(ktout)s&nbsp;: c'est le résultat d'un mauvais réglage, pas de la console du club.</p>
<p><b>Q3 — %(min_pla)d mm.</b> Le relevé, en ne changeant que l'épaisseur (PLA, 150 mm, 11 kg)&nbsp;:</p>
<table class="releve"><thead><tr><th>Épaisseur e (en millimètres, mm)</th><th>Contrainte σ (en mégapascals, MPa)</th><th>Coefficient k</th><th>Résultat</th></tr></thead><tbody>
%(tab_pla)s
</tbody></table>
<p>À %(e8)d mm, σ = %(s8)s MPa&nbsp;: %(etat8)s (k = %(k8)s).
<br>À 12 mm, elle tient (k = %(k12)s), mais k &lt; 3&nbsp;: le cahier des charges n'est pas respecté.
<br>À %(min_pla)d mm, k = %(k15)s&nbsp;: c'est la plus petite épaisseur validée.
<br>Remarque&nbsp;: doubler l'épaisseur rend la console quatre fois plus résistante (l'épaisseur compte « au carré »).</p>
<p><b>Q4 — Pour savoir quel réglage a changé le résultat.</b>
<br>Si tu changes l'épaisseur ET le matériau à la fois, et que k monte, tu ne sais pas lequel des deux l'a fait monter.
<br>La simulation accepte tous les changements&nbsp;; c'est le <b>raisonnement</b> qui demande d'en changer un seul.</p>
<p><b>Q5 — Une réponse attendue</b>&nbsp;: «&nbsp;Je ne valide pas la console de %(e0)d mm en PLA&nbsp;: la simulation donne k = %(kprop)s, elle casserait sous la neige. Je propose %(min_pla)d mm de PLA (k = %(k15)s), ou un autre matériau.&nbsp;»
<br>Toute décision juste <b>donne le nombre</b> (k) et le <b>compare à 3</b>.</p>
<p><b>Et les autres matériaux&nbsp;?</b> La plus petite épaisseur validée, à 150 mm et 11 kg, puis ce qu'un toit leur fait (la simulation ne le calcule pas)&nbsp;:</p>
<ul class="materiaux-toit">
%(tab_mat)s
</ul>
<p>Le PLA validé à %(min_pla)d mm reste un pari l'été&nbsp;: il ramollit vers 55&nbsp;°C (degrés Celsius). C'est pourquoi on fera, après la simulation, un <b>essai réel</b>&nbsp;: la simulation prépare l'essai, elle ne le remplace pas.</p>
</div></details>
<div class="retenir"><strong>À retenir&nbsp;:</strong> paramétrer une simulation, c'est entrer les <b>vraies valeurs du cas le plus défavorable</b> (matériau, dimensions, charge), lire le résultat, le <b>comparer au cahier des charges</b> (k ≥ 3), et ne changer qu'<b>un réglage à la fois</b>.</div>
</div>
<script>
/* La simulation de la console (4e_C8.1) — les matériaux et la formule viennent de _generation/console_jardiniere.py ;
   le banc tests_simulation_4e_C8.1.mjs vérifie que la page calcule exactement comme le modèle. */
(function(){
  "use strict";
  var MAT = %(mats)s, LARGEUR = %(b)s, G = %(g)s, COEF = %(coef)d;
  var BONNES = %(bonnes)s;
  window.__bonnesSimu = BONNES;
  function simuConsole(nom, e, L, charge){
    var m = MAT.filter(function(x){ return x.nom === nom; })[0];
    if(!m || !(e > 0) || !(L > 0) || !(charge > 0)) return null;
    var s = charge * G * L / (LARGEUR * e * e / 6), k = m.se / s;
    var etat = s > m.sr ? "casse" : (s > m.se ? "plie" : (k < COEF ? "tient-insuffisant" : "valide"));
    return {sigma: Math.round(s * 10) / 10, k: Math.round(k * 100) / 100, etat: etat};
  }
  window.simuConsole = simuConsole;
  var $ = function(id){ return document.getElementById(id); };
  var fr = function(x, d){ return x.toFixed(d).replace(".", ","); };
  var COURT = {"Bois (pin)": "Bois", "PLA imprimé en 3D": "PLA", "PVC rigide": "PVC", "Aluminium": "Alu", "Acier doux": "Acier"};
  var BREF = {"casse": "✘ casse", "plie": "✘ plie", "tient-insuffisant": "⚠ k < 3", "valide": "✔ validée"};
  var TEXTE = {
    "casse": "✘ La console CASSE : σ dépasse la contrainte de rupture du matériau.",
    "plie": "✘ La console PLIE pour toujours : σ dépasse la limite élastique.",
    "tient-insuffisant": "⚠ La console tient, mais k est plus petit que 3 : le cahier des charges n'est pas respecté.",
    "valide": "✔ Validée : k vaut 3 ou plus."
  };
  function lignes(){
    var t = $("simReleve"); if(!t) return;
    var essais = ((window.__exp || {}).simu) || [];
    t.tBodies[0].innerHTML = essais.slice().reverse().map(function(x){
      var r = simuConsole(x.m, x.e, x.L, x.c); if(!r) return "";
      var td = function(v, l, u){ return "<td" + (l ? " data-l=\\"" + l + "\\"" : "") + (u ? " data-u=\\"" + u + "\\"" : "") + ">" + v + "</td>"; };
      return "<tr class=\\"" + (r.etat === "valide" ? "ok" : "ko") + "\\">" + td(COURT[x.m] || x.m) + td(x.e, "e = ", " mm") +
             td(x.L, "L = ", " mm") + td(x.c, "", " kg") + td(fr(r.sigma, 1), "σ = ", " MPa") + td(fr(r.k, 2), "k = ") + td(BREF[r.etat]) + "</tr>";
    }).join("");
  }
  window.__lignesSimu = lignes;
  $("simLancer").addEventListener("click", function(){
    var coche = document.querySelector('input[name="simMat"]:checked');
    var nom = coche ? coche.value : "", e = parseFloat($("simEp").value), L = parseFloat($("simLong").value), c = parseFloat($("simCharge").value);
    var r = simuConsole(nom, e, L, c), out = $("simSortie");
    if(!r){ out.className = "sortie-simu ko"; out.textContent = "Il manque un réglage : choisis le matériau, et entre l'épaisseur, la longueur et la charge (des nombres plus grands que zéro)."; return; }
    var m = MAT.filter(function(x){ return x.nom === nom; })[0];
    out.className = "sortie-simu " + (r.etat === "valide" ? "ok" : "ko");
    out.innerHTML = "Contrainte dans la console : <b>σ = " + fr(r.sigma, 1) + " MPa</b> (mégapascals)" +
      "<br>Le " + nom + " plie pour toujours au-dessus de " + m.se + " MPa et casse au-dessus de " + m.sr + " MPa." +
      "<br>Coefficient de sécurité : <b>k = " + m.se + " ÷ " + fr(r.sigma, 1) + " = " + fr(r.k, 2) + "</b>" +
      "<br><b>" + TEXTE[r.etat] + "</b>";
    window.__exp = window.__exp || {};
    var essais = window.__exp.simu = window.__exp.simu || [];
    var cle = nom + "|" + e + "|" + L + "|" + c;
    if(!essais.some(function(x){ return x.m + "|" + x.e + "|" + x.L + "|" + x.c === cle; })) essais.push({m: nom, e: e, L: L, c: c});
    lignes();
    if(typeof window.__sauverSequence === "function") window.__sauverSequence();
  });
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", function(){ setTimeout(lignes, 0); }); else setTimeout(lignes, 0);
})();
</script>
</section>
<!-- fin:act-simulation -->""" % {
        "terre": TERRE, "neige": NEIGE, "total": TERRE + NEIGE, "e0": PROPOSITION[1], "L": LONGUEUR,
        "svg": SVG, "q1": options_radio("a6q1", a["Q1"], bonnes["Q1"]),
        "q2": options_radio("a6q2", a["Q2"], bonnes["Q2"]), "q3": options_radio("a6q3", a["Q3"], bonnes["Q3"]),
        "q4": options_radio("a6q4", a["Q4"], bonnes["Q4"]), "puces": puces,
        "kprop": fr(prop["k"], 2), "sprop": fr(prop["sigma"]), "se_pla": P.PAR_NOM["PLA imprimé en 3D"].sigma_e,
        "sr_pla": P.PAR_NOM["PLA imprimé en 3D"].sigma_r, "ktout": fr(toute["k"], 2), "min_pla": min_pla,
        "tab_pla": tableau_correction(), "e8": 8,
        "etat8": {"casse": "plus que les %d MPa de rupture du PLA, la console casse encore" % P.PAR_NOM["PLA imprimé en 3D"].sigma_r,
                  "plie": "plus que la limite de %d MPa, la console plie pour toujours" % P.PAR_NOM["PLA imprimé en 3D"].sigma_e,
                  "tient-insuffisant": "la console tient, mais k reste plus petit que 3",
                  "valide": "la console est déjà validée"}[pla8["etat"]], "s8": fr(pla8["sigma"]), "k8": fr(pla8["k"], 2),
        "k12": fr(pla12["k"], 2), "k15": fr(pla15["k"], 2), "tab_mat": tableau_materiaux(),
        "mats": json.dumps(mats, ensure_ascii=False), "b": repr(LARGEUR), "g": repr(G), "coef": COEF_EXIGE,
        "bonnes": js_bonnes,
    }


# ══ L'essai réel : le protocole que l'élève propose (4e_C8.2, 25/11/2026) ══════════════════════════════════
# Pourquoi (audit #867, note de 4e_C8.2 ; décision de Pascal du 25/11, « continue ») : le code 4e_C8.2 demande de
# PROPOSER un protocole de test pour valider la TENUE MÉCANIQUE D'UN MATÉRIAU. Le lot ne le faisait que sur le
# comportement du système (pluie, gel, LED). La simulation de l'activité 2 bis a dit quelle épaisseur de PLA tient ;
# l'activité 2 ter fait proposer l'essai réel qui le confirmera, avant de poser quarante consoles sur le toit.
# En 5e (5e_C8.2), l'élève SUIVAIT un protocole fourni, et cassait l'éprouvette ; en 4e, il le PROPOSE, et ne casse
# rien : on prouve que la vraie pièce tient ce que le cahier des charges exige, et qu'elle revient en place.

CHARGE_ESSAI = COEF_EXIGE * CHARGE                          #: 33 kg — ce que le cahier des charges exige
SAC = CHARGE / 2                                            #: 5,5 kg — un sac de sable pesé ; deux sacs = un palier
PALIERS = [CHARGE * i for i in range(1, COEF_EXIGE + 1)]    #: 11, 22 puis 33 kg, sur la même console
TENUE_MIN = 5            #: min — la charge d'essai reste posée cinq minutes
RETOUR_MAX = 1           #: mm — déchargée, le bout revient à 1 mm près de sa position de départ
EPROUVETTES = 3          #: consoles essayées, imprimées de la même façon (et qui n'iront pas sur le toit)
MATIERE = "PLA imprimé en 3D"


def fleche(nom, epaisseur, charge, longueur=LONGUEUR):
    """Flèche au bout d'une console encastrée, chargée à son extrémité, en mm : f = F·L³ / (3·E·I), I = b·e³/12.
    Vraie tant que la console reste élastique (σ ≤ σe) : la flèche grandit alors exactement comme la charge."""
    m = P.PAR_NOM[nom]
    return charge * G * longueur ** 3 / (3.0 * m.E * (LARGEUR * epaisseur ** 3 / 12.0))


def mm(x):
    """Une flèche en millimètres, au dixième, écrite à la française."""
    return fr(arrondi(x, 1))


SVG_BANC = """<svg viewBox="0 0 520 420" role="img" aria-labelledby="bancT bancD" class="schema-console schema-banc">
<title id="bancT">Le banc d'essai de la console : vue de côté</title>
<desc id="bancD">À gauche, un montant en bois serré à l'établi, où la console est vissée comme sur le muret du toit. La
console avance de 150 millimètres dans le vide. À son bout pend un crochet qui porte les sacs de sable : deux sacs de
5,5 kilogrammes par palier. Sous la charge, la console se courbe un peu (en pointillés) : son bout descend. Une règle
graduée est fixée debout juste à côté du bout : on y lit de combien le bout descend, la flèche. Un bac attend sous les
sacs, à 10 centimètres : si la console casse, la charge tombe dedans.</desc>
<defs><marker id="bancFl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M0 0 10 5 0 10z" fill="currentColor"/></marker>
<pattern id="bancBois" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="16" height="16" fill="#5a3d22"/>
<path d="M0 4q8-3 16 0M0 12q8-3 16 0" stroke="#7a5532" stroke-width="1.5" fill="none"/></pattern></defs>
<text x="8" y="40" fill="#e8c9a0" font-size="22">montant</text>
<rect x="12" y="56" width="48" height="310" fill="url(#bancBois)"/>
<rect x="4" y="366" width="150" height="16" fill="#3b4a66"/>
<line x1="60" y1="112" x2="322" y2="112" stroke="#61dafb" stroke-width="2.5" marker-start="url(#bancFl)" marker-end="url(#bancFl)" color="#61dafb"/>
<text x="191" y="98" text-anchor="middle" fill="#61dafb" font-size="24" font-weight="bold">150 mm</text>
<path d="M60 150Q200 152 330 192v20Q200 172 60 170z" fill="none" stroke="#ffd66b" stroke-width="2" stroke-dasharray="6 5" opacity=".8"/>
<rect x="60" y="150" width="270" height="20" rx="3" fill="#ffd66b"/>
<circle cx="76" cy="160" r="4.5" fill="#5a3d22"/><circle cx="98" cy="160" r="4.5" fill="#5a3d22"/>
<text x="76" y="220" fill="#ffd66b" font-size="22" font-weight="bold">console PLA</text>
<line x1="322" y1="170" x2="322" y2="238" stroke="#e4eaf5" stroke-width="3"/>
<rect x="286" y="238" width="72" height="34" rx="6" fill="#c9a66b" stroke="#e8c9a0" stroke-width="1.5"/>
<rect x="286" y="278" width="72" height="34" rx="6" fill="#c9a66b" stroke="#e8c9a0" stroke-width="1.5"/>
<text x="322" y="261" text-anchor="middle" fill="#2a1d0e" font-size="18" font-weight="bold">5,5 kg</text>
<text x="322" y="301" text-anchor="middle" fill="#2a1d0e" font-size="18" font-weight="bold">5,5 kg</text>
<text x="76" y="266" fill="#e8c9a0" font-size="22">2 sacs</text>
<text x="76" y="298" fill="#e8c9a0" font-size="22">par palier</text>
<line x1="336" y1="150" x2="398" y2="150" stroke="#81fba1" stroke-width="2" stroke-dasharray="5 4"/>
<line x1="336" y1="202" x2="398" y2="202" stroke="#81fba1" stroke-width="2" stroke-dasharray="5 4"/>
<line x1="384" y1="154" x2="384" y2="198" stroke="#81fba1" stroke-width="2.5" marker-start="url(#bancFl)" marker-end="url(#bancFl)" color="#81fba1"/>
<rect x="402" y="104" width="24" height="200" fill="#e4eaf5" rx="2"/>
<path d="M402 124h9M402 144h15M402 164h9M402 184h15M402 204h9M402 224h15M402 244h9M402 264h15M402 284h9" stroke="#081b3a" stroke-width="2"/>
<text x="436" y="128" fill="#e4eaf5" font-size="22" font-weight="bold">règle</text>
<text x="436" y="154" fill="#e4eaf5" font-size="20">(mm)</text>
<text x="436" y="230" fill="#81fba1" font-size="22" font-weight="bold">flèche</text>
<text x="436" y="262" fill="#81fba1" font-size="22" font-weight="bold">f</text>
<path d="M270 346h110v24H270z" fill="none" stroke="#ff7b88" stroke-width="2.5"/>
<text x="394" y="366" fill="#ff7b88" font-size="22" font-weight="bold">bac</text>
</svg>
<ul class="legende-banc">
<li><b>Le montant</b>&nbsp;: une planche serrée à l'établi&nbsp;; la console y est vissée comme sur le muret du toit.</li>
<li><b>La console</b>&nbsp;: en PLA, %(e)d&nbsp;mm d'épaisseur&nbsp;; elle dépasse de %(L)d&nbsp;mm (son porte-à-faux).</li>
<li><b>Les sacs</b>&nbsp;: du sable pesé, 5,5&nbsp;kg par sac, 2 sacs par palier&nbsp;: 11, puis 22, puis 33&nbsp;kg.</li>
<li><b>La règle graduée</b>&nbsp;: en millimètres, fixée debout juste à côté du bout de la console.</li>
<li><b>La flèche f</b>&nbsp;: de combien le bout descend sous la charge (en pointillés, la console chargée).</li>
<li><b>Le bac</b>&nbsp;: 10&nbsp;cm sous les sacs — si la console casse, la charge tombe dedans.</li>
</ul>"""


def fragment_protocole():
    e = plus_petite_epaisseur(MATIERE)
    r33 = calcul(MATIERE, e, LONGUEUR, CHARGE_ESSAI)
    se = P.PAR_NOM[MATIERE].sigma_e
    # le protocole ne casse rien : à la charge d'essai, la console validée reste sous sa limite élastique
    assert r33["sigma"] <= se, "à %g kg la console de %d mm dépasse la limite élastique" % (CHARGE_ESSAI, e)
    f = [fleche(MATIERE, e, c) for c in PALIERS]
    kg = lambda x: fr(x, 0) if float(x).is_integer() else fr(x, 1)
    Q = {
        "a7q1": ["La simulation calcule une pièce pleine ; une console imprimée a des couches et un remplissage.",
                 "La simulation ne connaît pas le poids de la neige : il faut le peser sur le toit.",
                 "Pour trouver à quelle charge exacte la console casse : la simulation ne le dit pas.",
                 "Une simulation se trompe toujours de moitié : on divise son résultat par deux."],
        "a7q2": ["%s kg : la charge la plus lourde qu'elle portera vraiment sur le toit" % kg(CHARGE),
                 "%s kg : trois fois la charge la plus lourde, comme le cahier des charges" % kg(CHARGE_ESSAI),
                 "jusqu'à ce qu'elle casse, en notant la charge de rupture, comme en 5e",
                 "%s kg : la terre et la neige de toute la jardinière, sur une seule console" % kg(TERRE + NEIGE)],
        "a7q3": ["les %s kg d'un coup, pour voir tout de suite si la console tient" % kg(CHARGE_ESSAI),
                 "%s kg sur la première console, %s kg sur la deuxième, %s kg sur la troisième" % tuple(kg(c) for c in PALIERS),
                 "en ajoutant les sacs au hasard, jusqu'à ce que la console ait l'air de plier",
                 "par paliers, sur la même console : %s, %s puis %s kg, une mesure à chaque fois" % tuple(kg(c) for c in PALIERS)],
        "a7q4": ["la masse de la console, avec une balance, pour voir si elle a perdu de la matière",
                 "la température de la console, avec un thermomètre posé dessus",
                 "la flèche — de combien le bout descend — avec une règle graduée fixée debout",
                 "la longueur de la console, avec un mètre ruban, avant et après"],
        "a7q5": ["%s mm" % mm(f[0]), "%s mm" % mm(f[1]), "%s mm" % mm(f[2]), "%s mm" % mm(9 * f[0])],
        "a7q6": ["À %s kg, la console ne casse pas et ne se fissure pas, même au bout de %d minutes." % (kg(CHARGE_ESSAI), TENUE_MIN),
                 "À %s kg tenus %d min : aucune fissure ; déchargée, le bout revient à %d mm près." % (kg(CHARGE_ESSAI), TENUE_MIN, RETOUR_MAX),
                 "La console tient bien, ne fait pas de bruit et ne bouge presque pas sous les sacs.",
                 "La flèche à %s kg est la plus petite des trois consoles, et aucune ne casse." % kg(CHARGE_ESSAI)],
        "a7q7": ["trois, imprimées de la même façon : une seule peut être bonne ou mauvaise par hasard",
                 "une seule : si elle tient, celles imprimées de la même façon tiendront aussi",
                 "cinq : une de chaque matériau, pour comparer le PLA au bois, au PVC et aux métaux",
                 "deux : une pour chaque console qui portera la jardinière sur le toit"],
    }
    B = {"a7q1": Q["a7q1"][0], "a7q2": Q["a7q2"][1], "a7q3": Q["a7q3"][3], "a7q4": Q["a7q4"][2],
         "a7q5": Q["a7q5"][2], "a7q6": Q["a7q6"][1], "a7q7": Q["a7q7"][0]}
    LEG = {"a7q1": "Q1 — Pourquoi un essai réel après la simulation",
           "a7q2": "Q2 — La charge d'essai, pour une console",
           "a7q3": "Q3 — Comment poser la charge",
           "a7q4": "Q4 — Ce qu'on mesure, et avec quoi",
           "a7q5": "Q5 — La flèche attendue à %s kg" % kg(CHARGE_ESSAI),
           "a7q6": "Q6 — Le critère qui permet de décider",
           "a7q7": "Q7 — Combien de consoles essayer"}
    groupes = {k: '<fieldset class="qcm-groupe" id="%s">\n  <legend>%s</legend>\n%s\n</fieldset>'
               % (k, LEG[k], options_radio(k, Q[k], B[k])) for k in Q}
    js_bonnes = json.dumps({k: html.unescape(v) for k, v in B.items()}, ensure_ascii=False)
    d = {"e": e, "L": LONGUEUR, "kg_s": kg(CHARGE), "kg_e": kg(CHARGE_ESSAI), "kg_t": kg(TERRE + NEIGE),
         "sac": kg(SAC), "p1": kg(PALIERS[0]), "p2": kg(PALIERS[1]), "p3": kg(PALIERS[2]),
         "f1": mm(f[0]), "f2": mm(f[1]), "f3": mm(f[2]), "f9": mm(9 * f[0]), "tenue": TENUE_MIN, "retour": RETOUR_MAX,
         "n": EPROUVETTES, "s33": fr(r33["sigma"]), "se": se, "coef": COEF_EXIGE, "svg": SVG_BANC % {"e": e, "L": LONGUEUR},
         "bonnes": js_bonnes}
    d.update(groupes)
    page = """<!-- debut:act-protocole — engendré par _generation/console_jardiniere.py, ne pas éditer à la main -->
<style>
#act2ter .ecart{border-left:4px solid var(--warn);background:rgba(255,214,102,.08);padding:9px 13px;border-radius:0 10px 10px 0;margin:10px 0}
#act2ter .petit{font-size:.88em;color:var(--sub)}
#act2ter .schema-console{width:100%%;max-width:560px;height:auto;display:block;margin:10px auto;background:#081b3a;border-radius:10px}
#act2ter ul.legende-banc{margin:6px 0 12px;padding-left:1.2em;font-size:.93em;line-height:1.5}
#act2ter ul.legende-banc li{margin:4px 0}
#act2ter ol.protocole-modele li{margin:6px 0;line-height:1.5}
#act2ter .grille-soi{border:1px solid var(--border);border-radius:10px;padding:8px 12px;margin:10px 0}
#act2ter .grille-soi label{display:flex;gap:8px;align-items:flex-start;margin:6px 0}
@media print{#act2ter .schema-console{background:#081b3a}}
</style>
<section class="card" id="act2ter">
<h2>📐 Activité 2 ter — Proposer le protocole de l'essai réel (C8.2) <span class="chrono">⏱ ~20 min</span></h2>
<div class="exo">
<p>La simulation a parlé&nbsp;: en PLA, la console tient à partir de <b>%(e)d mm</b>.
<br>Mais une simulation est un <b>modèle</b>&nbsp;: avant de visser quarante consoles sur le toit, le club en imprime quelques-unes et les <b>essaie pour de vrai</b>.</p>
<p>Ta mission&nbsp;: <b>proposer le protocole</b> de cet essai — ce qu'on fait, dans quel ordre, ce qu'on mesure, et à quoi on reconnaîtra que la console est validée.</p>
<div class="ecart"><b>Rappel de 5e</b>&nbsp;: avec la patère du hall, tu suivais un protocole fourni et tu <b>cassais</b> l'éprouvette, pour comparer des matériaux.
<br>Ici, le matériau est choisi&nbsp;: on veut prouver que <b>cette pièce</b> tient ce que le cahier des charges exige — %(coef)d fois %(kg_s)s kg — et qu'elle revient en place.</div>
<p>Le banc que le club peut monter, vu de côté&nbsp;:</p>
%(svg)s

<p><b>Q1 — La simulation dit que la console de %(e)d mm tient. Pourquoi faire quand même un essai réel&nbsp;?</b></p>
%(a7q1)s

<p><b>Q2 — Jusqu'à quelle charge l'essai va-t-il, pour une console&nbsp;?</b>
<br>Relis le cahier des charges de l'activité 2 bis.</p>
%(a7q2)s

<p><b>Q3 — Comment poser la charge&nbsp;?</b></p>
%(a7q3)s

<p><b>Q4 — Qu'est-ce qu'on mesure à chaque palier, et avec quoi&nbsp;?</b>
<br>Un <b>palier</b>&nbsp;: une étape où l'on ajoute de la charge, puis où l'on attend et l'on mesure.</p>
%(a7q4)s

<p><b>Q5 — À %(p1)s kg, la console de %(e)d mm descend de %(f1)s mm (c'est le calcul qui le prévoit).</b>
<br>Tant qu'elle reste <b>élastique</b> (elle reviendrait en place si on la déchargeait), sa flèche grandit <b>comme la charge</b>.
<br>De combien doit-elle descendre à %(kg_e)s kg&nbsp;? Fais le calcul sur une feuille de brouillon.</p>
%(a7q5)s

<p><b>Q6 — Le critère s'écrit AVANT l'essai. Lequel permet de décider, sans discussion&nbsp;?</b></p>
%(a7q6)s

<p><b>Q7 — Combien de consoles faut-il essayer&nbsp;?</b></p>
%(a7q7)s

<p><b>Q8 — Écris ton protocole</b>, en six lignes, une idée par ligne&nbsp;:</p>
<ol class="protocole-plan">
<li>la pièce essayée&nbsp;;</li>
<li>le montage&nbsp;;</li>
<li>la charge, par paliers&nbsp;;</li>
<li>la mesure, et avec quoi&nbsp;;</li>
<li>le critère, écrit avant l'essai&nbsp;;</li>
<li>la sécurité.</li>
</ol>
<textarea id="a7prot" rows="7" placeholder="① On essaie … ② On fixe … ③ On charge … ④ À chaque palier, on mesure … ⑤ La console est validée si … ⑥ Sécurité : …" aria-label="Q8 — ton protocole, en six lignes"></textarea>
<details class="etayage">
  <summary>🪜 Version étayée — des phrases à compléter</summary>
  <p>Le niveau attendu est <b>exactement le même</b> qu'avec la consigne libre&nbsp;: ces débuts de phrases retirent l'obstacle de la rédaction, pas l'exigence.</p>
  <ul>
    <li>① On essaie ____ consoles en ____ , de ____ mm, imprimées ____ .</li>
    <li>② On visse chaque console sur ____ , comme ____ .</li>
    <li>③ On accroche au bout ____ , par paliers de ____ kg, jusqu'à ____ kg, tenus ____ minutes.</li>
    <li>④ À chaque palier, on mesure ____ avec ____ .</li>
    <li>⑤ La console est validée si ____ , et si, une fois déchargée, ____ .</li>
    <li>⑥ Sécurité&nbsp;: ____ .</li>
  </ul>
</details>
<div class="grille-soi" role="group" aria-label="Je relis mon protocole">
<p class="petit" style="margin:0"><b>Je relis mon protocole</b> (pour toi, sans note — coche ce qui est vrai)&nbsp;:</p>
<label><input type="checkbox" id="a7g1"> Mon critère a un nombre et une unité, et il est écrit avant l'essai.</label>
<label><input type="checkbox" id="a7g2"> Une seule chose change pendant l'essai&nbsp;: la charge.</label>
<label><input type="checkbox" id="a7g3"> Une autre classe pourrait refaire l'essai sans moi&nbsp;: la pièce, le montage, la mesure et la sécurité sont dits.</label>
</div>
<button class="btn check" data-check="7" type="button">✅ Vérifier l'activité 2 ter</button>
<p class="feedback" id="fb7" role="status"></p>
<details class="correction"><summary>📖 Correction complète (à ouvrir APRÈS avoir écrit ton protocole)</summary><div>
<p><b>Q1 — La simulation calcule une pièce pleine, faite d'une seule matière.</b>
<br>Une console imprimée est faite de <b>couches</b> collées les unes sur les autres, et d'un <b>remplissage</b> (l'intérieur n'est pas plein)&nbsp;: elle peut être plus faible que le modèle.
<br>La simulation connaît la neige (c'est elle qui fait %(kg_s)s kg par console)&nbsp;; elle ne se trompe pas «&nbsp;de moitié&nbsp;» — elle suppose une pièce idéale.
<br>Et on ne cherche pas la charge de rupture&nbsp;: on veut prouver que la pièce tient ce qui est exigé.</p>
<p><b>Q2 — %(kg_e)s kg</b>&nbsp;: le cahier des charges demande que chaque console tienne <b>%(coef)d fois</b> la charge la plus lourde, %(coef)d × %(kg_s)s = <b>%(kg_e)s kg</b>.
<br>· %(kg_s)s kg prouverait seulement qu'elle tient un jour de tempête, sans aucune marge&nbsp;;
<br>· %(kg_t)s kg, c'est toute la jardinière sur une seule console&nbsp;: ce n'est pas le cas réel, et ce n'est pas l'exigence&nbsp;;
<br>· aller jusqu'à la casse, c'est le protocole de 5e, fait pour comparer des matériaux&nbsp;; ici le matériau est choisi.</p>
<p><b>Q3 — Par paliers, sur la même console&nbsp;: %(p1)s, puis %(p2)s, puis %(p3)s kg</b> (2 sacs de %(sac)s kg à chaque palier), une mesure à chaque fois.
<br>Les %(kg_e)s kg d'un coup donneraient un <b>choc</b>&nbsp;: la console pourrait casser sous un à-coup qu'elle ne subira jamais sur le toit.
<br>Une charge différente sur chaque console change deux choses à la fois (la console ET la charge)&nbsp;: on ne saurait plus ce qui explique le résultat.</p>
<p><b>Q4 — La flèche</b>&nbsp;: de combien le bout de la console descend, en millimètres, lue sur une règle graduée fixée debout juste à côté du bout.
<br>La masse, la température ou la longueur de la console ne disent rien de sa tenue sous la charge.</p>
<p><b>Q5 — %(f3)s mm.</b>
<br>La charge est multipliée par %(coef)d (%(p1)s → %(kg_e)s kg)&nbsp;: si la console reste élastique, la flèche aussi, %(f1)s × %(coef)d ≈ <b>%(f3)s mm</b>.
<br>Le calcul prévoit&nbsp;: %(f1)s mm à %(p1)s kg, %(f2)s mm à %(p2)s kg, %(f3)s mm à %(p3)s kg.
<br>Si la vraie console descend <b>beaucoup plus</b>, ou si sa flèche grandit plus vite que la charge, elle commence à plier&nbsp;: c'est un signal d'arrêt, avant même la fin de l'essai.
<br>· %(f1)s mm, c'est oublier que la charge a triplé&nbsp;; · %(f2)s mm, c'est la flèche à %(p2)s kg&nbsp;; · %(f9)s mm, c'est multiplier par 9 au lieu de 3.</p>
<p><b>Q6 — «&nbsp;À %(kg_e)s kg tenus %(tenue)d min&nbsp;: aucune fissure&nbsp;; déchargée, le bout revient à %(retour)d mm près.&nbsp;»</b>
<br>Ce critère a des nombres et des unités, et il dit les deux façons dont une console échoue&nbsp;:
<br>· elle <b>casse</b> ou se fissure&nbsp;;
<br>· elle <b>plie pour toujours</b> — elle a dépassé sa limite élastique, et elle ne revient pas en place.
<br>«&nbsp;Ne casse pas&nbsp;» oublie le second cas&nbsp;; «&nbsp;tient bien&nbsp;» ne se mesure pas&nbsp;; «&nbsp;la plus petite flèche des trois&nbsp;» compare les consoles entre elles, pas au cahier des charges.
<br>À %(kg_e)s kg, le calcul donne σ = %(s33)s MPa (mégapascals), sous les %(se)d MPa de la limite élastique du PLA&nbsp;: une console imprimée comme le modèle doit donc revenir en place.</p>
<p><b>Q7 — Trois consoles, imprimées de la même façon.</b>
<br>Une seule pièce peut être bonne ou mauvaise par hasard (une couche mal collée)&nbsp;: trois essais qui passent montrent que l'impression est <b>régulière</b>.
<br>Comparer les cinq matériaux, c'était le travail de la simulation&nbsp;; et le nombre de consoles du toit ne dit pas combien il faut en essayer.
<br>Les consoles d'essai ont porté %(kg_e)s kg&nbsp;: elles ne vont pas sur le toit, on en imprime de neuves.</p>
<p><b>Q8 — Un protocole attendu</b>&nbsp;:</p>
<ol class="protocole-modele">
<li><b>La pièce</b>&nbsp;: %(n)d consoles en PLA de %(e)d mm, imprimées avec les mêmes réglages que celles du toit.</li>
<li><b>Le montage</b>&nbsp;: chaque console est vissée sur un montant serré à l'établi, avec les mêmes vis que sur le muret, et dépasse de %(L)d mm.</li>
<li><b>La charge</b>&nbsp;: au bout, un crochet&nbsp;; on y accroche des sacs de sable pesés de %(sac)s kg, 2 par palier&nbsp;: %(p1)s, %(p2)s, puis %(p3)s kg, sans à-coup. On laisse %(kg_e)s kg pendant %(tenue)d minutes.</li>
<li><b>La mesure</b>&nbsp;: avant de charger, on lit la position du bout sur la règle graduée fixée debout&nbsp;; puis la flèche à chaque palier&nbsp;; puis la position du bout une fois les sacs retirés. Tout est noté dans un tableau.</li>
<li><b>Le critère, écrit avant</b>&nbsp;: la console est validée si, à %(kg_e)s kg tenus %(tenue)d minutes, elle n'a aucune fissure, et si, déchargée, son bout revient à %(retour)d mm près de sa position de départ. Le calcul prévoit environ %(f1)s, %(f2)s et %(f3)s mm de flèche&nbsp;: une flèche bien plus grande arrête l'essai. Les %(n)d consoles doivent passer.</li>
<li><b>La sécurité</b>&nbsp;: lunettes de protection&nbsp;; un bac sous les sacs, à 10 cm&nbsp;; personne sous la charge&nbsp;; c'est un adulte qui accroche les sacs, et on recule d'un pas avant de les lâcher.</li>
</ol>
<p><b>Et si une console échoue&nbsp;?</b> On ne la pose pas&nbsp;: on note ce qui a cédé (une couche qui s'ouvre, le bout qui reste bas), on change <b>une</b> chose (l'épaisseur, le remplissage), et on rejoue l'essai — c'est la boucle de l'activité 1.</p>
</div></details>
<div class="retenir"><strong>À retenir&nbsp;:</strong> proposer un protocole d'essai pour un matériau, c'est dire <b>la pièce</b>, <b>le montage</b>, <b>la charge</b> (par paliers, jusqu'à ce que le cahier des charges exige), <b>la mesure</b> (avec quoi), et <b>le critère chiffré, écrit avant</b>&nbsp;: elle ne casse pas, et elle revient en place. Une simulation prépare l'essai&nbsp;; l'essai, sur plusieurs pièces, le confirme.</div>
</div>
<script>
/* Les bonnes réponses de l'activité 2 ter : écrites par _generation/console_jardiniere.py, depuis le même modèle. */
window.__bonnesProtocole = %(bonnes)s;
</script>
</section>
<!-- fin:act-protocole -->""" % d
    return insecables(page)


def insecables(fragment):
    """Une espace insécable entre un nombre et son unité (« 150 mm » ne se coupe plus en fin de ligne), dans le texte
    lu — jamais dans les groupes de réponses, dont les valeurs sont comparées aux bonnes réponses du modèle."""
    morceaux = re.split(r'(<fieldset class="qcm-groupe".*?</fieldset>|<script>.*?</script>|<style>.*?</style>)', fragment, flags=re.S)
    unite = re.compile(r'(\d) (mm|kg|cm|min|minutes|MPa)\b')
    for k in range(0, len(morceaux), 2):
        morceaux[k] = re.sub(r'>[^<]+', lambda m: unite.sub('\\1&nbsp;\\2', m.group(0)), morceaux[k])
    return "".join(morceaux)


DEBUT_P, FIN_P = "<!-- debut:act-protocole", "<!-- fin:act-protocole -->"

DEBUT, FIN = "<!-- debut:act-simulation", "<!-- fin:act-simulation -->"
DEBUT_S, FIN_S = "<!-- debut:synthese-simulation", "<!-- fin:synthese-simulation -->"


def fragment_synthese():
    """La partie 7 de la synthèse élève : les mêmes nombres que l'activité, tirés du même modèle (n°233)."""
    prop = calcul(*PROPOSITION)
    e_min = plus_petite_epaisseur(PROPOSITION[0])
    ok = calcul(PROPOSITION[0], e_min)
    return """<!-- debut:synthese-simulation — engendré par _generation/console_jardiniere.py, ne pas éditer à la main -->
<div class="bloc savoir">
  <a class="retour-carte" href="#carte-titre">↑ La carte</a>
  <h2 id="partie-7" style="margin-top:0">7. Comment savoir si une pièce tiendra, sans la casser&nbsp;?</h2>
  <p>La console du club, en plastique imprimé de %(e0)d&nbsp;mm&nbsp;: k = %(k0)s, elle casserait&nbsp;; à %(e1)d&nbsp;mm, k = %(k1)s.</p>
  <p class="retenir">🧠 <b>À retenir</b>&nbsp;: on <b>simule</b> le cas le plus lourd&nbsp;; le <b>coefficient de sécurité</b> k doit
  valoir <b>3 ou plus</b>. Un <b>essai réel</b> le confirme (%(n)d consoles, %(kg_e)s&nbsp;kg, retour en place).</p>
  <p class="piege">⚠️ <b>Le piège</b>&nbsp;: régler la charge d'un jour calme, sans la neige.</p>
</div>
<!-- fin:synthese-simulation -->""" % {"e0": PROPOSITION[1], "k0": fr(prop["k"], 2), "e1": e_min, "k1": fr(ok["k"], 2),
                                       "n": EPROUVETTES, "kg_e": fr(CHARGE_ESSAI, 0)}


def synthese_avec(src):
    i, j = src.find(DEBUT_S), src.find(FIN_S)
    if i < 0 or j < 0:
        raise SystemExit("marqueurs %s … %s introuvables dans la synthèse" % (DEBUT_S, FIN_S))
    sys.path.insert(0, os.path.join(LOT, "..", "..", "..", "..", "_outils"))
    from expliquer_sigles import infobuller
    return infobuller(src[:i] + fragment_synthese() + src[j + len(FIN_S):])


def page_avec(src):
    i, j = src.find(DEBUT), src.find(FIN)
    if i < 0 or j < 0:
        raise SystemExit("marqueurs %s … %s introuvables dans la séquence" % (DEBUT, FIN))
    # les sigles expliqués (n°44, complément du 22/11/2026) : « Pour un générateur : page = infobuller(page) »
    sys.path.insert(0, os.path.join(LOT, "..", "..", "..", "..", "_outils"))
    from expliquer_sigles import infobuller
    page = src[:i] + fragment() + src[j + len(FIN):]
    i, j = page.find(DEBUT_P), page.find(FIN_P)
    if i < 0 or j < 0:
        raise SystemExit("marqueurs %s … %s introuvables dans la séquence" % (DEBUT_P, FIN_P))
    page = infobuller(page[:i] + fragment_protocole() + page[j + len(FIN_P):])
    # le pourquoi de chaque mauvaise proposition (mode mission) : écrit par l'outil commun, depuis le fichier du lot,
    # pour que `enrichir.py --verifier` trouve la page à jour après chaque régénération
    sys.path.insert(0, os.path.join(LOT, "..", "..", "..", "..", "_outils", "mode_mission"))
    from enrichir import poser_pourquoi
    mission = json.load(open(os.path.join(LOT, "mission_4e_C8.1.json"), encoding="utf-8"))
    for ident in ("a6q1", "a6q2", "a6q3", "a6q4", "a7q1", "a7q2", "a7q3", "a7q4", "a7q5", "a7q6", "a7q7"):
        if ident in mission.get("pourquoi", {}):
            page = poser_pourquoi(page, ident, mission["pourquoi"][ident])
    return page


if __name__ == "__main__":
    print("Console : largeur %g mm, longueur %g mm, charge %g kg par console (%d + %d kg sur %d consoles)"
          % (LARGEUR, LONGUEUR, CHARGE, TERRE, NEIGE, CONSOLES))
    for m in MATERIAUX:
        print("  %-20s σe %3d MPa  →  plus petite épaisseur validée : %s"
              % (m.nom, m.sigma_e, plus_petite_epaisseur(m.nom)))
    p = calcul(*PROPOSITION)
    print("Proposition du club (%s, %d mm) : σ = %.1f MPa, k = %.2f → %s" % (PROPOSITION + (p["sigma"], p["k"], p["etat"])))
    src = open(SEQUENCE, encoding="utf-8").read()
    neuf = page_avec(src)
    src_s = open(SYNTHESE, encoding="utf-8").read()
    neuf_s = synthese_avec(src_s)
    att = json.dumps(attendus(), ensure_ascii=False, indent=1) + "\n"
    if "--ecrire" in sys.argv:
        open(SEQUENCE, "w", encoding="utf-8").write(neuf)
        open(SYNTHESE, "w", encoding="utf-8").write(neuf_s)
        open(ATTENDUS, "w", encoding="utf-8").write(att)
        print("écrit :", ", ".join(os.path.relpath(f, LOT) for f in (SEQUENCE, SYNTHESE, ATTENDUS)))
    else:
        a_jour = (neuf == src and neuf_s == src_s and os.path.exists(ATTENDUS)
                  and open(ATTENDUS, encoding="utf-8").read() == att)
        print("✅ la page et les attendus sont à jour" if a_jour else "✘ la page ou les attendus ne sont pas à jour : relancer avec --ecrire")
        sys.exit(0 if a_jour else 1)
