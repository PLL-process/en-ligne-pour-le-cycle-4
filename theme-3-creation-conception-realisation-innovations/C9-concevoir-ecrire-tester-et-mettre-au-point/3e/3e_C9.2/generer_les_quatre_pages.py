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

Séances de 55 min (décision de Pascal du 24/10/2026) : la page tout-en-un compte
HUIT séances (onglets s1 à s8). Les quatre pages gardent leurs noms de fichier —
aucun lien du dépôt ne casse — et deviennent une page par GRANDE ÉTAPE, chacune
portant deux séances de 55 min, annoncées en tête de page et séparées par un
en-tête « Séance N » et un bouton qui mène à la séance suivante (règle n°101) :

    page 1 · besoin et algorithme       séances 1 et 2  (activités 1, 2)
    page 2 · programmer par paliers     séances 3 et 4  (activité 3, en deux parties)
    page 3 · l'humain dans la boucle    séances 5 et 6  (activités 4, 5)
    page 4 · protocole et recette       séances 7 et 8  (activités 6, 7, clôture)

Le découpage est vérifié par la suite `tests_3e_C9.2-C8.3.mjs` : union des champs
identique à la page source, et persistance croisée dans les deux sens.

Réparé le 24/10/2026 (le script ne tournait plus sur la source) : le Bonus est
passé AVANT le bilan (règle n°301) et la clôture comme l'échauffement
Vittascience vivent DANS leur panneau de séance — on prend donc les panneaux
entiers, sans recoller ces blocs une seconde fois ; la situation s'arrête avant
le banc d'essai, qui n'est pas sur la page 1.
"""
import io, re, sys, json, pathlib

LOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

# La fiche papier (impression en fiche d'élève, décision de Pascal du 25/10/2026) se pose par SA source unique,
# `_outils/impression_papier/poser.py` : une page engendrée la reçoit à jour, exactement comme la pose à la main.
import importlib.util
_racine = next((d for d in pathlib.Path(__file__).resolve().parents if (d / "_outils" / "impression_papier" / "poser.py").is_file()), None)
if _racine is None:
    raise SystemExit("_outils/impression_papier/poser.py introuvable au-dessus de ce script : la fiche papier ne peut pas être posée")
_spec = importlib.util.spec_from_file_location("poser_papier", _racine / "_outils" / "impression_papier" / "poser.py")
FICHE_PAPIER = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(FICHE_PAPIER)
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
NB_SEANCES = 8
_style1   = ligne("</style>")
_navcss   = ligne('<style id="navharm-css">')
_rappel   = ligne('<section class="card rappel-spiralaire"')
_billet   = ligne('aria-labelledby="billet-titre"')
_badges   = ligne('<div class="badges">')
_identite = ligne('<div class="identite"')
_toolbar  = ligne('<div class="toolbar">')
_progress = ligne('<div class="progress-wrap">')
_situ     = ligne("<h2>📖 Situation déclenchante</h2>") - 1
_tabs     = ligne('<div class="seance-tabs"')
_taches   = ligne('id="tachesBandeau"')
_banc     = ligne('id="bancCard"')
_s        = {n: ligne(f'id="s{n}" role="tabpanel"') for n in range(1, NB_SEANCES + 1)}
_footer   = ligne("<footer>")
_script   = ligne("<script>", _footer)
_loupe    = ligne("loupe-images-v2") - 1

assert _situ < _banc < _tabs, "la situation, le banc puis les onglets : l'ordre de la source a changé"

HEAD        = seg(1, _style1)
NAVCSS      = seg(_navcss, ferme(_navcss, "</style>"))
NAV         = seg(ligne('<nav id="navharm"'), ligne('class="skip-link"'))
H1          = seg(ligne("<h1>"), ligne("<h1>"))
RAPPEL      = seg(_rappel, ferme(_rappel, "</section>"))
BILLET      = seg(_billet - 1, ferme(_billet, "</section>"))
BADGES      = seg(_badges, ferme(_badges, "</div>"))
IDENTITE    = seg(_identite, ferme(_identite, "</div>"))
TOOLBAR     = seg(_toolbar, _progress - 2)
PROGRESS    = seg(_progress, ferme(_progress, "</div>"))
SITUATION   = seg(_situ, _banc - 1)          # le banc a sa place à part (pages 2 à 4)
TACHES      = seg(_taches, _taches)
BANC        = seg(_banc, ferme(_banc, "</section>"))
# Le panneau entier : l'échauffement Vittascience est dans s3, la clôture
# (synthèse → Bonus → bilan → QCM) dans s8.
S           = {n: seg(_s[n] + 1, ferme(_s[n], "</div>") - 1) for n in _s}
FOOTER      = seg(_footer, ferme(_footer, "</footer>"))
SCRIPT      = seg(_script, ferme(_script, "</script>"))
LOUPE       = seg(_loupe, len(L))

# Le nom de chaque séance, tel que la source l'écrit sur son bouton « séance
# suivante » (règle n°101) : une seule écriture, aucune divergence possible.
NOM_SEANCE = {}
for n in range(2, NB_SEANCES + 1):
    m = re.search(rf'<button class="btn vers-seance" data-vers="s{n}">(.*?)</button>', S[n - 1])
    if not m:
        raise SystemExit(f"bouton vers la séance {n} introuvable dans le panneau s{n-1}")
    NOM_SEANCE[n] = m.group(1)

# ─────────────────────────── les quatre pages ───────────────────────────
PAGES = [
    dict(n=1, fichier="sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html",
         titre="Besoin et algorithme", seances=(1, 2),
         but="Comprendre ce que la mairie demande, et écrire l'algorithme AVANT de programmer.",
         avant=[RAPPEL, BILLET, SITUATION, "TABS", TACHES]),
    dict(n=2, fichier="sequence_3e_C9.2-C8.3_station_2_programmer.html",
         titre="Programmer par paliers", seances=(3, 4),
         but="Traduire l'algorithme en blocs sur Vittascience, palier par palier.",
         avant=["TABS", TACHES, BANC]),
    dict(n=3, fichier="sequence_3e_C9.2-C8.3_station_3_interaction.html",
         titre="L'humain dans la boucle", seances=(5, 6),
         but="Programmer l'acquittement, lire le code généré, diagnostiquer une panne.",
         avant=["TABS", TACHES, BANC]),
    dict(n=4, fichier="sequence_3e_C9.2-C8.3_station_4_recette.html",
         titre="Protocole et recette", seances=(7, 8),
         but="Rédiger le protocole de test, l'exécuter, signer le procès-verbal.",
         avant=["TABS", TACHES, BANC]),
]
assert sorted(s for p in PAGES for s in p["seances"]) == list(range(1, NB_SEANCES + 1)), \
    "chaque séance doit figurer sur une page, et une seule"

def les_seances(p):
    a, b = p["seances"]
    return f"séances {a} et {b}"

def tabs(courante):
    """Les onglets deviennent des liens entre pages, coches ✔ conservées."""
    lignes = ['<nav class="seance-tabs" id="seances" aria-label="Les quatre pages de la séquence">']
    for p in PAGES:
        actif = " active" if p["n"] == courante else ""
        aria = ' aria-current="page"' if p["n"] == courante else ""
        lignes.append(
            f'  <a class="seance-tab{actif}" href="{p["fichier"]}" data-page="{p["n"]}"{aria}>'
            f'Page {p["n"]}<br><small>{p["titre"]} · {les_seances(p)}</small>'
            f'<span class="done" id="done-p{p["n"]}"></span></a>')
    lignes.append("</nav>")
    return "\n".join(lignes)

TOUT_EN_UN = "sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html"

REPLI = (
    '<p class="repli-tout-en-un">📄 Réseau capricieux, ou besoin de tout avoir sous la main ? '
    f'<a href="{TOUT_EN_UN}">La séquence entière en une seule page</a> — '
    'mêmes activités, mêmes réponses enregistrées, aucun chargement entre les séances.</p>')

BOUTON = re.compile(r'<button class="btn vers-seance" data-vers="s(\d+)">(.*?)</button>')

def boutons_de_seance(bloc, page):
    """Le bouton « séance suivante » de la page tout-en-un bascule un ONGLET.
    Dans une page découpée, il devient un LIEN vers l'en-tête de la séance
    suivante quand celle-ci est sur la même page ; sinon on le retire, car le
    lien de bas de page (« Page N+1 ») mène déjà à la suite — et un bouton
    viserait un onglet qui n'existe pas."""
    out = []
    for l in bloc.split("\n"):
        m = BOUTON.search(l)
        if not m:
            out.append(l)
            continue
        cible = int(m.group(1))
        if cible in page["seances"]:
            out.append(BOUTON.sub(
                lambda mm: f'<a class="btn lien-seance" href="#seance-{mm.group(1)}">{mm.group(2)}</a>', l))
    return "\n".join(out)

def bloc_seance(n, page):
    """Une séance de 55 min dans sa page : un conteneur ancré (#seance-N), son
    contenu, et — si la suivante est sur la même page — le lien qui y mène."""
    return (f'<div class="seance-bloc" id="seance-{n}">\n'
            + boutons_de_seance(S[n], page)
            + "\n</div>")

def suivant(n):
    """Règle d'or n°101 — chaque page mène explicitement à la suivante."""
    if n == len(PAGES):
        return ""
    p = PAGES[n]      # PAGES[n] = page n+1 (liste 0-indexée)
    return (f'\n<p class="page-suivante">'
            f'<a class="btn" href="{p["fichier"]}">Page {p["n"]} → {p["titre"]}, {les_seances(p)} ›</a></p>\n')

CSS_SUP = """
<style id="quatre-pages-css">
/* Découpage en quatre pages (règle d'or n°116), deux séances de 55 min par page */
.seance-tabs a.seance-tab{text-decoration:none;display:block}
.seance-tabs a.seance-tab:focus-visible{outline:3px solid #ffb300;outline-offset:2px}
.repli-tout-en-un{max-width:940px;margin:0 auto 14px;padding:8px 12px;border-left:3px solid var(--sub);
  background:rgba(155,190,252,.06);border-radius:0 8px 8px 0;font-size:.9em;color:var(--sub)}
.repli-tout-en-un a{color:var(--hl)}
.page-suivante{max-width:940px;margin:22px auto 8px;text-align:right}
.page-suivante .btn{text-decoration:none;display:inline-block}
.seance-bloc{scroll-margin-top:56px}
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

    # 5) majTaches : les tâches de la page sont celles de SES deux séances
    a, b = page["seances"]
    titre = json.dumps(f"Séances {a} et {b} — {page['titre']}", ensure_ascii=False)
    ancien_bloc = ('const onglet = document.querySelector(".seance-tab.active");\n'
                   '  const bloc = TACHES[onglet ? onglet.dataset.panel : ""];')
    assert js.count(ancien_bloc) == 1, "majTaches() introuvable"
    js = js.replace(ancien_bloc,
                    f'const bloc = {{titre: {titre}, taches: [].concat(TACHES["s{a}"].taches, TACHES["s{b}"].taches)}};')
    js = re.sub(r'document\.querySelectorAll\("\.seance-tab"\)\.forEach\(t =>\s*\n\s*t\.addEventListener\("click", \(\) ?=> ?setTimeout\(majTaches, 0\)\)\);', '', js)

    # 6) le banc n'est pas sur toutes les pages : ses fonctions et ses
    #    branchements ne touchent le DOM que s'il est là.
    js = js.replace("function simSetVent(v){",
                    "function simSetVent(v){\n  if(!$(\"simVent\")) return;   /* page sans banc d'essai */")
    js = js.replace("function simTick(){",
                    "function simTick(){\n  if(!$(\"simVent\")) return;   /* page sans banc d'essai */")
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

def selecteur_parcours_utile(toolbar, corps_assemble):
    """Règle d'or n°136 — un sélecteur ne vaut que par ce qu'il sélectionne.

    Les pages 3 et 4 ne portent AUCUN bloc `data-parcours` : le sélecteur
    🅰/🅱/🅲 s'y affichait, changeait la classe du body, écrivait sa note — et
    ne masquait rien. Mécanisme complet, branché sur rien, exactement ce que
    la règle n°136 décrit. On le retire donc des pages qui n'ont rien à
    filtrer, en disant à l'élève où son choix a été fait et qu'il est retenu.
    """
    if "data-parcours" in corps_assemble:
        return toolbar
    lignes, dedans, out = toolbar.split("\n"), False, []
    for l in lignes:
        if "choix-parcours-boutons" in l:
            dedans = True
            continue
        if dedans:
            if "</div>" in l:
                dedans = False
            continue
        if 'id="parcoursNote"' in l:
            # id DIFFÉRENT de « parcoursNote » : le script commun réécrit cette
            # note à chaque affichage (« Parcours affiché : … »). Lui laisser le
            # même identifiant, c'est voir notre phrase remplacée au chargement —
            # trouvé par le test, pas par la relecture.
            out.append('<p class="saved-note" id="parcoursRappel" role="status" style="text-align:center">'
                       'Ton parcours 🅰/🅱/🅲 se choisit en <b>page 1</b> : il est retenu pour toute la '
                       'séquence. Cette page-ci ne contient aucun bloc propre à un parcours.</p>')
            continue
        out.append(l)
    return "\n".join(out)


# ─────────────────────────────── écriture ───────────────────────────────
for p in PAGES:
    corps = [tabs(p["n"]) if bloc == "TABS" else bloc for bloc in p["avant"]]
    corps += [bloc_seance(n, p) for n in p["seances"]]
    corps_assemble = "\n".join(corps)
    toolbar = selecteur_parcours_utile(TOOLBAR, corps_assemble)
    js = corriger_script(SCRIPT, p)
    h1 = H1.replace("</h1>", f" — {p['titre']}</h1>")
    a, b = p["seances"]
    sous = (f'<p class="subtitle">🎯 Page {p["n"]} sur {len(PAGES)} · {les_seances(p)} '
            f'(2 séances de 55 min) — {p["but"]}</p>')
    page = "\n".join([
        HEAD, "<body>", NAVCSS, CSS_SUP, NAV, h1, sous, REPLI,
        BADGES, IDENTITE, toolbar, PROGRESS,
        corps_assemble,
        suivant(p["n"]),
        FOOTER, js, LOUPE,
    ])
    page = FICHE_PAPIER.poser(page)     # la fiche papier, source unique (_outils/impression_papier/)
    io.open(LOT / p["fichier"], "w", encoding="utf-8").write(page)
    print("écrit :", p["fichier"], len(page) // 1024, "Ko")
