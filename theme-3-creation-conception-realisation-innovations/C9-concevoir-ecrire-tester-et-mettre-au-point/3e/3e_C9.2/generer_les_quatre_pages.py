#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Engendre les QUATRE pages de la séquence à partir de la page tout-en-un.

    python3 generer_les_quatre_pages.py        (depuis ce dossier)

Règle d'or n°116 : une séquence trop dense se découpe en pages reliées, SANS RIEN
PERDRE. Ce script est ce qui garantit le « sans rien perdre » : les quatre pages
ne sont pas maintenues à la main, elles sont ENGENDRÉES depuis un seul fichier
source, `sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html`.

Conséquence pratique, à ne jamais oublier : **on ne modifie jamais les quatre
pages directement.** On modifie la page tout-en-un, puis on relance ce script.
Toute retouche faite dans une page découpée sera écrasée à la prochaine
exécution — et, pire, aura divergé silencieusement en attendant.

Le découpage est vérifié par la suite `tests_3e_C9.2-C8.3.mjs` : union des champs
identique à la page source, et persistance croisée dans les deux sens.
"""
import io, re, sys, pathlib

LOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
SRC = LOT / "sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html"
L = io.open(SRC, encoding="utf-8").read().split("\n")

def seg(a, b):                      # lignes 1-indexées, inclusives
    return "\n".join(L[a-1:b])

def ligne(marque, depuis=0):
    """Numéro (1-indexé) de la première ligne contenant `marque`."""
    for i in range(depuis, len(L)):
        if marque in L[i]:
            return i + 1
    raise SystemExit("repère introuvable : " + marque)

def ferme(depuis, balise):
    """Première ligne qui est EXACTEMENT la balise fermante, sans indentation.
    Comparer après strip() attraperait la première fermeture imbriquée et
    tronquerait le bloc en silence."""
    for i in range(depuis, len(L)):
        if L[i] == balise:      # colonne 0 : on ignore les balises imbriquées
            return i + 1
    raise SystemExit("fermeture introuvable : " + balise)

# Les bornes se cherchent par repères, jamais par numéros figés : la source
# est éditée sans cesse (seuils, figures, corrections) et des numéros en dur
# se décalent en silence.
_style1   = ligne("</style>")
_navcss   = ligne('<style id="navharm-css">')
_body     = ligne("<body>")
_rappel   = ligne('<section class="card rappel-spiralaire"')
_billet   = ligne('aria-labelledby="billet-titre"')
_gestes   = ligne('class="card gestes-outil"')
_badges   = ligne('<div class="badges">')
_identite = ligne('<div class="identite"')
_toolbar  = ligne('<div class="toolbar">')
_progress = ligne('<div class="progress-wrap">')
_situ     = ligne("<h2>📖 Situation déclenchante</h2>") - 1
_tabs     = ligne('<div class="seance-tabs"')
_taches   = ligne('id="tachesBandeau"')
_banc     = ligne('id="bancCard"')
_s1       = ligne('id="s1" role="tabpanel"')
_s2       = ligne('id="s2" role="tabpanel"')
_s3       = ligne('id="s3" role="tabpanel"')
_s4       = ligne('id="s4" role="tabpanel"')
_synth    = ligne("<h2>📝 Synthèse de la séquence") - 1
_bilan    = ligne("<h2>🪞 Mon bilan personnel</h2>") - 1
_pret     = ligne('justify-content:center">🧠') - 1
_bonus    = ligne("🎁 Bonus (facultatif", _pret) - 1
_footer   = ligne("<footer>")
_script   = ligne("<script>", _footer)
_loupe    = ligne("loupe-images-v1") - 1

HEAD        = seg(1, _style1)
NAVCSS      = seg(_navcss, ferme(_navcss, "</style>"))
NAV         = seg(ligne('<nav id="navharm"'), ligne('class="skip-link"'))
H1          = seg(ligne("<h1>"), ligne("<h1>"))
RAPPEL      = seg(_rappel, ferme(_rappel, "</section>"))
BILLET      = seg(_billet - 1, ferme(_billet, "</section>"))
GESTES      = seg(_gestes, ferme(_gestes, "</section>"))
BADGES      = seg(_badges, ferme(_badges, "</div>"))
IDENTITE    = seg(_identite, ferme(_identite, "</div>"))
TOOLBAR     = seg(_toolbar, _progress - 2)
PROGRESS    = seg(_progress, ferme(_progress, "</div>"))
SITUATION   = seg(_situ, _tabs - 1)
TACHES      = seg(_taches, _taches)
BANC        = seg(_banc, ferme(_banc, "</section>"))
S1          = seg(_s1 + 1, ferme(_s1, "</div>") - 1)
S2          = seg(_s2 + 1, ferme(_s2, "</div>") - 1)
S3          = seg(_s3 + 1, ferme(_s3, "</div>") - 1)
S4          = seg(_s4 + 1, ferme(_s4, "</div>") - 1)
SYNTHESE    = seg(_synth, _bilan - 1)
BILAN       = seg(_bilan, _pret - 1)
PRET        = seg(_pret, _bonus - 1)
BONUS       = seg(_bonus, _footer - 1)
FOOTER      = seg(_footer, ferme(_footer, "</footer>"))
SCRIPT      = seg(_script, ferme(_script, "</script>"))
LOUPE       = seg(_loupe, len(L))

# ─────────────────────────── les quatre pages ───────────────────────────
PAGES = [
    dict(n=1, fichier="sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html",
         titre="Besoin et algorithme",
         sous="🎯 Page 1 sur 4 — Comprendre ce que la mairie demande, et écrire l'algorithme AVANT de programmer.",
         corps=[RAPPEL, BILLET, SITUATION, "TABS", TACHES, S1]),
    dict(n=2, fichier="sequence_3e_C9.2-C8.3_station_2_programmer.html",
         titre="Programmer par paliers",
         sous="🎯 Page 2 sur 4 — Traduire l'algorithme en blocs sur Vittascience, palier par palier.",
         corps=[GESTES, "TABS", TACHES, BANC, S2]),
    dict(n=3, fichier="sequence_3e_C9.2-C8.3_station_3_interaction.html",
         titre="L'humain dans la boucle",
         sous="🎯 Page 3 sur 4 — Programmer l'acquittement, lire le code généré, diagnostiquer une panne.",
         corps=["TABS", TACHES, BANC, S3]),
    dict(n=4, fichier="sequence_3e_C9.2-C8.3_station_4_recette.html",
         titre="Protocole et recette",
         sous="🎯 Page 4 sur 4 — Rédiger le protocole de test, l'exécuter, signer le procès-verbal.",
         corps=["TABS", TACHES, BANC, S4, SYNTHESE, BILAN, PRET, BONUS]),
]

def tabs(courante):
    """Les onglets deviennent des liens entre pages, coches ✔ conservées."""
    lignes = ['<nav class="seance-tabs" id="seances" aria-label="Les quatre pages de la séquence">']
    for p in PAGES:
        actif = " active" if p["n"] == courante else ""
        aria = ' aria-current="page"' if p["n"] == courante else ""
        lignes.append(
            f'  <a class="seance-tab{actif}" href="{p["fichier"]}" data-page="{p["n"]}"{aria}>'
            f'Page {p["n"]}<br><small>{p["titre"]}</small>'
            f'<span class="done" id="done-s{p["n"]}"></span></a>')
    lignes.append("</nav>")
    return "\n".join(lignes)

TOUT_EN_UN = "sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html"

REPLI = (
    '<p class="repli-tout-en-un">📄 Réseau capricieux, ou besoin de tout avoir sous la main ? '
    f'<a href="{TOUT_EN_UN}">La séquence entière en une seule page</a> — '
    'mêmes activités, mêmes réponses enregistrées, aucun chargement entre les séances.</p>')

def sans_bouton_seance(bloc):
    """Le bouton « séance suivante » de la page tout-en-un bascule un ONGLET.
    Dans les pages découpées, la navigation se fait par des LIENS : on retire donc
    ce bouton-là, sinon il ferait doublon avec le lien de bas de page — et il
    viserait un onglet qui n'existe pas."""
    return "\n".join(l for l in bloc.split("\n") if 'vers-seance' not in l)

def suivant(n):
    """Règle d'or n°101 — chaque page mène explicitement à la suivante."""
    if n == 4:
        return ""
    p = PAGES[n]      # PAGES[n] = page n+1 (liste 0-indexée)
    return (f'\n<p class="page-suivante">'
            f'<a class="btn" href="{p["fichier"]}">Page {p["n"]} → {p["titre"]} ›</a></p>\n')

CSS_SUP = """
<style id="quatre-pages-css">
/* Découpage en quatre pages (règle d'or n°116) */
.seance-tabs a.seance-tab{text-decoration:none;display:block}
.seance-tabs a.seance-tab:focus-visible{outline:3px solid #ffb300;outline-offset:2px}
.repli-tout-en-un{max-width:940px;margin:0 auto 14px;padding:8px 12px;border-left:3px solid var(--sub);
  background:rgba(155,190,252,.06);border-radius:0 8px 8px 0;font-size:.9em;color:var(--sub)}
.repli-tout-en-un a{color:var(--hl)}
.page-suivante{max-width:940px;margin:22px auto 8px;text-align:right}
.page-suivante .btn{text-decoration:none;display:inline-block}
@media print{.page-suivante{display:none}}
</style>
"""

# ───────────────────── corrections du script commun ─────────────────────
def corriger_script(js, page):
    # 1) collect() FUSIONNE au lieu de remplacer : sans cela, sauvegarder en
    #    page 2 effacerait les réponses de la page 1 (perte silencieuse).
    ancien = """function collect(){
  const o = {inputs:{}, radios:{}, valid: window.__valid || {}, exp: window.__exp || {}};"""
    nouveau = """function collect(){
  /* Découpage en quatre pages : chaque page ne voit QUE ses propres champs.
     On repart donc de ce qui est déjà stocké et on le complète — sinon la
     sauvegarde d'une page effacerait en silence les réponses des autres. */
  let d = {};
  try{ d = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; }catch(e){ d = {}; }
  const o = {inputs: Object.assign({}, d.inputs||{}),
             radios: Object.assign({}, d.radios||{}),
             valid:  Object.assign({}, d.valid||{},  window.__valid || {}),
             exp:    Object.assign({}, d.exp||{},    window.__exp   || {})};"""
    assert js.count(ancien) == 1, "collect() introuvable"
    js = js.replace(ancien, nouveau)

    # 2) window.__valid doit repartir du stockage, pas d'un objet vide
    js = js.replace('window.__exp = window.__exp || {};',
                    'window.__exp = window.__exp || {};\nwindow.__valid = window.__valid || {};')

    # 3) le billet d'entrée n'existe qu'en page 1
    js = js.replace('$("btnBillet").addEventListener("click", ()=>{',
                    'if($("btnBillet")) $("btnBillet").addEventListener("click", ()=>{')

    # 4) les onglets sont devenus des liens : plus de bascule de panneaux
    ancien_tabs = js[js.index('/* ══════ Onglets séances ══════ */'):js.index("/* ══════ Le banc d'essai de la station ══════")]
    js = js.replace(ancien_tabs, """/* ══════ Onglets = liens entre les quatre pages ══════ */
/* Plus de bascule de panneaux : chaque page est un document autonome. */

""")

    # 5) majTaches : la séance courante est celle de la page
    js = js.replace('const onglet = document.querySelector(".seance-tab.active");\n'
                    '  const bloc = TACHES[onglet ? onglet.dataset.panel : ""];',
                    f'const bloc = TACHES["s{page}"];')
    js = re.sub(r'document\.querySelectorAll\("\.seance-tab"\)\.forEach\(t =>\s*\n\s*t\.addEventListener\("click", \(\) ?=> ?setTimeout\(majTaches, 0\)\)\);', '', js)

    # 6) le banc n'est pas sur toutes les pages : ses fonctions et ses
    #    branchements ne touchent le DOM que s'il est là.
    js = js.replace("function simSetVent(v){",
                    "function simSetVent(v){\n  if(!$(\"simVent\")) return;   /* page sans banc d'essai */")
    js = js.replace("function simTick(){",
                    "function simTick(){\n  if(!$(\"simVent\")) return;   /* page sans banc d'essai */")
    for cible in ['$("simVent").addEventListener', '$("simVentNum").addEventListener',
                  '$("btnAcquit").addEventListener', '$("btnChrono").addEventListener']:
        js = js.replace(cible, "if($(" + cible.split('"')[1].join('""') + ")) " + cible) if False else js
    js = re.sub(r'^\$\("(simVent|simVentNum|btnAcquit|btnChrono)"\)\.addEventListener',
                lambda m: 'if($("%s")) $("%s").addEventListener' % (m.group(1), m.group(1)),
                js, flags=re.M)

    # 7) l'hypothèse est saisie en page 1 et rappelée au bilan, en page 4 :
    #    quand le champ est absent, on la relit dans la sauvegarde partagée.
    js = js.replace("""function majHyp(){
  const h = $("hyp1").value.trim();""",
                    """function majHyp(){
  /* Le champ vit en page 1, le rappel en page 4 : quand le champ est absent,
     on relit l'hypothèse dans la sauvegarde partagée. */
  let h = "";
  if($("hyp1")){ h = $("hyp1").value.trim(); }
  else { try{ h = ((JSON.parse(localStorage.getItem(KEY)||"{}")||{}).inputs||{}).hyp1 || ""; }catch(e){ h = ""; } h = h.trim(); }
  if(!$("rappelHyp")) return;""")
    js = js.replace('$("hyp1").addEventListener("input", majHyp);',
                    'if($("hyp1")) $("hyp1").addEventListener("input", majHyp);')
    return js

def garder_banc(js, avec_banc):
    """Le script est le MÊME sur les quatre pages : on ne coupe rien, on
    garde-fou les accès DOM. Une seule version à maintenir, et aucune
    divergence possible entre les pages."""
    return js

# ─────────────────────────────── écriture ───────────────────────────────
for p in PAGES:
    corps = []
    for bloc in p["corps"]:
        corps.append(tabs(p["n"]) if bloc == "TABS" else sans_bouton_seance(bloc))
    js = corriger_script(SCRIPT, p["n"])
    js = garder_banc(js, any(b is BANC for b in p["corps"]))
    h1 = H1.replace("</h1>", f" — {p['titre']}</h1>")
    page = "\n".join([
        HEAD, "<body>", NAVCSS, CSS_SUP, NAV, h1,
        f'<p class="subtitle">{p["sous"]}</p>', REPLI,
        BADGES, IDENTITE, TOOLBAR, PROGRESS,
        "\n".join(corps),
        suivant(p["n"]),
        FOOTER, js, LOUPE,
    ])
    io.open(LOT / p["fichier"], "w", encoding="utf-8").write(page)
    print("écrit :", p["fichier"], len(page) // 1024, "Ko")
