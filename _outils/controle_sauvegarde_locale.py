# -*- coding: utf-8 -*-
"""controle_sauvegarde_locale.py — une page qui garde les réponses de l'élève dans le
navigateur le dit, s'efface d'un clic, et prévient du poste partagé (audit externe A05).

LE CONSTAT (audit externe du 01/11/2026, point A05, instruit le 08/11/2026)
--------------------------------------------------------------------------
Les séquences annoncent « tes réponses sont enregistrées dans ce navigateur uniquement ».
Dans une salle de techno ou au CDI, le navigateur est partagé : l'élève suivant, sur la même
session Windows, ouvre la page et lit les réponses du précédent. Ce n'est ni une sauvegarde
portable, ni une protection. Deux pages écrivaient même « personne d'autre ne les voit ».
Mesuré le 08/11 : 163 pages écrivent dans `localStorage` ; 9 séquences n'offraient AUCUN
moyen d'effacer (l'une promettait « tu peux tout effacer quand tu veux » sans bouton) ;
aucune ne prévenait du poste partagé.

CE QU'IL MESURE
---------------
Pour chaque page `.html` publiée qui appelle `localStorage.setItem(` :
  1. EFFACEMENT — la page sait effacer ce qu'elle a écrit : `localStorage.removeItem(` ou
     `localStorage.clear(` (ou la fonction `oublier(` du kit des ateliers), ou un bouton
     « Recommencer / Réinitialiser / Effacer… » qui réécrit un état neuf (les QCM).
  2. POSTE PARTAGÉ — une note visible porte `data-note="poste-partage"` (le texte canonique
     est NOTE_POSTE_PARTAGE ci-dessous). Exigée partout depuis le 15/11/2026, QCM compris :
     on les croyait ne garder qu'un score, ils gardent le NOM, le PRÉNOM, la classe, chaque
     réponse et le temps — et « ♻ Recommencer entièrement » efface les réponses mais garde
     le nom. Le QCM du gabarit maison reçoit donc sa note ET un bouton « 🗑 Effacer ma
     sauvegarde » qui retire toute la clé, en deux clics (`demande()`), sous `#savedNote`.
  3. SANS BOÎTE MODALE — aucun `confirm(` : la confirmation se fait en deux clics dans la
     page (`demande()` ou l'armement du bouton), jamais par une boîte du navigateur qui
     bloque la page et échappe au lecteur d'écran. Comptée, pas refusée. Seul le CODE est
     lu (15/11/2026, `sans_modale.code_seul`) : deux QCM étaient comptés pour le mot
     « confirm() » écrit dans un commentaire qui explique `demande`.

`--corriger` répare ce qui suit un gabarit connu, et seulement cela :
  · une séquence dont la barre `.toolbar` porte « Imprimer » mais pas de bouton d'effacement,
    avec `const KEY = "…"` : le bouton « 🗑 Effacer ma sauvegarde » est ajouté, et un script
    autonome l'arme en deux clics (six secondes) puis efface la clé et recharge ;
  · une séquence ou un atelier qui porte un bouton `btnReset` et pas de note poste partagé :
    la note est posée après la note « enregistrées dans ce navigateur » si elle existe, sinon
    après la barre d'outils ;
  · « personne d'autre ne les voit » devient « rien n'est envoyé en ligne » ;
  · un QCM du gabarit maison (`#savedNote`, `const KEY`, `demande()`) sans note : la note
    QCM et le bouton « 🗑 Effacer ma sauvegarde » sont posés sous `#savedNote`, et un script
    l'arme en deux clics, retire la clé et recharge (15/11/2026).
Le reste (pages sans gabarit connu, `confirm(` hors forme reconnue) est listé, pas touché ;
`_outils/sans_modale.py` remplace les `if(confirm("…"))`.

CE QU'IL NE VOIT PAS — et qui le voit
-------------------------------------
Il lit le source : un bouton, un `removeItem`. Il ne sait pas si l'effacement est COMPLET. Le 20/11/2026, un audit
externe du jardin connecté de 4e écrit une phrase dans un exercice incrusté, efface, recharge : la phrase est encore
là. Mesuré le jour même sur les 166 pages à bouton d'effacement : 40 gardaient quelque chose — 24 le travail d'un
exercice incrusté (il a sa propre clé), 27 les étoiles du mode mission, 11 les deux ; aucun QCM. La règle n°322 gagne
donc un quatrième point — « effacer, c'est tout effacer » — et son banc, qui le joue au navigateur, page par page :

    node _outils/banc_effacement.mjs [--muet] [page.html | dossier …]

UNE PRÉFÉRENCE D'AFFICHAGE N'EST PAS UNE RÉPONSE (21/11/2026)
------------------------------------------------------------
Depuis la PR #837, l'index garde sur l'appareil les groupes de l'accès rapide laissés ouverts sur téléphone
(`index:acces-rapide`, décision de Pascal du 21/11 : « le groupe laissé ouvert l'est encore à la visite suivante »).
Aucun nom, aucune réponse : l'élève suivant apprend seulement quel groupe était ouvert. Le contrôle sortait pourtant
à 1 sur `main` (« sans aucun moyen d'effacer », « aucune note poste partagé »). PREFERENCES_SEULES nomme ces pages,
leur clé et ce qu'elle garde. L'exception est étroite et se vérifie à chaque passage : si la page écrit une AUTRE clé
que celle déclarée, elle redevient une page ordinaire et le contrôle la refuse comme avant.

LE MODE MISSION SE LIT À PART (25/11/2026)
------------------------------------------
Depuis que chaque document élève porte le mode mission (`_outils/mode_mission/`), son bloc — le même dans toutes les
pages — contient un `localStorage.setItem(` : lu tel quel, il faisait de sept pages qui n'enregistrent rien (quatre TP
de CAO, le TP mBot2, deux activités) des pages « qui stockent sans moyen d'effacer ». Le bloc est donc retiré avant la
mesure : ce contrôle juge ce que LA PAGE enregistre. Ce que le mode garde, lui, dépend de la page :
  · elle a un bouton d'effacement → le mode garde la progression (écran, étoiles) et l'efface avec elle
    (`banc_effacement.mjs` le joue) ;
  · elle n'en a pas, donc n'enregistre rien → le mode ne garde que le choix d'affichage (mission ou page complète),
    une préférence ; la progression vit le temps de la page, l'écran en cours le temps de l'onglet
    (`mode_mission/banc_defaut.mjs` le joue : rien d'autre que `v` et `on` sous la clé « mission:… »).
Ces pages sont comptées (« ne gardent que le choix d'affichage du mode mission »), pas refusées.

Depuis le 26/11/2026 (Pascal : « tout doit être en mode mission »), les synthèses élève, les lexiques, les panneaux
et la carte des représentations portent eux aussi le mode mission, à la place du « mode lecture » de la veille, retiré ;
`mode_mission/banc_lecture.mjs` joue les documents à lire (L10 : rien que `v` et `on`). Un bloc du mode lecture resté
dans une page est encore lu à part — `controle_mode_mission.py` le refuse (M5).

Usage : python3 _outils/controle_sauvegarde_locale.py [--racine .] [--corriger] [--muet]
Sortie 0 si rien à refuser, 1 s'il reste un écart (effacement ou note manquants sur une
séquence ou un atelier), 2 si aucune page n'a pu être lue (règle d'or n°299).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sans_modale  # noqa: E402  (le code seul : un mot dans un commentaire n'est pas un appel)

EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation"}

NOTE_POSTE_PARTAGE = (
    '<p class="saved-note" data-note="poste-partage">🖥️ <b>Ordinateur partagé</b> (salle de techno, CDI — le centre de documentation et d\'information)&nbsp;: '
    'un autre élève qui ouvre cette page sur la même session verra tes réponses.<br>'
    'Quand tu as fini&nbsp;: imprime en PDF si tu veux garder une trace, puis clique sur '
    '«&nbsp;{bouton}&nbsp;».</p>'
)

#: la note des QCM du gabarit maison (15/11/2026) : ils gardent aussi le nom, et le bouton
#: qui efface TOUT est posé dans la note même, en haut de page, près du nom.
NOTE_QCM = (
    '<p class="saved-note" data-note="poste-partage" style="font-size:.88em;color:var(--sub);'
    'text-align:left;max-width:880px;margin:6px auto 12px">🖥️ <b>Ordinateur partagé</b> (salle de techno, '
    'CDI — le centre de documentation et d\'information)&nbsp;: un autre élève qui ouvre cette page sur la même session verra ton nom et tes réponses.<br>'
    'Quand tu as fini&nbsp;: imprime en PDF si tu veux garder une trace, puis efface ta sauvegarde.<br>'
    '<button class="btn ghost" id="btnEffacer" type="button" title="Effacer de ce navigateur ton nom, '
    'tes réponses et ton temps. Un second clic te sera demandé.">🗑 Effacer ma sauvegarde</button></p>'
    '<style>@media print{[data-note="poste-partage"]{display:none}}</style>'
)

SCRIPT_EFFACER_QCM = (
    '<script>/* Règle d\'or n°322 (15/11/2026) : effacer TOUTE la sauvegarde de ce QCM — le nom, les '
    'réponses, le temps —\n   en deux clics (`demande`), sans boîte modale. « ♻ Recommencer entièrement » '
    'garde le nom : il ne suffit pas sur un poste partagé. */\n'
    'document.getElementById("btnEffacer").addEventListener("click", function () {\n'
    '  if (demande("effacer-sauvegarde", "Effacer de ce navigateur ton nom, tes réponses et ton temps ?")) {\n'
    '    try { localStorage.removeItem(KEY); } catch (e) {}\n'
    '    location.reload();\n'
    '  }\n'
    '});\n</script>\n'
)
#: le bandeau `#savedNote` du gabarit maison des QCM, sous l'identité de l'élève
SAVEDNOTE_QCM = '<p class="saved-note" id="savedNote" role="status" aria-live="polite"></p>'

BOUTON_RESET = ('  <button class="btn ghost" id="btnReset" type="button" '
                'title="Effacer définitivement tes réponses enregistrées dans ce navigateur. '
                'Un second clic te sera demandé.">🗑 Effacer ma sauvegarde</button>\n')

SCRIPT_RESET = '''
<script>
/* Effacement de la sauvegarde locale, en deux clics et sans boîte modale
   (audit externe A05, 08/11/2026 ; posé par _outils/controle_sauvegarde_locale.py). */
(function(){
  "use strict";
  var b = document.getElementById("btnReset"); if (!b) return;
  var cle = %s, arme = 0, texte = b.textContent;
  b.setAttribute("aria-live", "polite");
  b.addEventListener("click", function(){
    var t = Date.now();
    if (arme && t - arme < 6000){ try{ localStorage.removeItem(cle); }catch(e){} location.reload(); return; }
    arme = t; b.textContent = "🗑 Clique encore pour confirmer l'effacement";
    setTimeout(function(){ if (arme === t){ arme = 0; b.textContent = texte; } }, 6000);
  });
})();
</script>
'''

#: les blocs du mode mission et du mode lecture, tels que leur `poser.py` les pose (deux marqueurs chacun)
_MISSION_RE = re.compile(r"<!-- mode-(mission|lecture) [^ ]+ : début.*?<!-- mode-\1 [^ ]+ : fin -->", re.S)


def sans_mission(src):
    """La page sans les blocs du mode mission et du mode lecture : ce contrôle juge ce que la page enregistre elle-même."""
    return _MISSION_RE.sub("", src)


FAUX = [
    ("rien n'est envoyé, personne d'autre ne les voit", "rien n'est envoyé en ligne"),
]


#: page → (clé, ce qu'elle garde). Seulement des préférences d'affichage, jamais une réponse ni un nom.
PREFERENCES_SEULES = {
    "index.html": ("index:acces-rapide", "les groupes de l'accès rapide laissés ouverts sur téléphone (21/11/2026)"),
}


def ecrit_seulement(src, cle):
    """Vrai si chaque `localStorage.setItem(` des scripts écrit la clé `cle` : en clair, ou par une
    variable à laquelle la page donne cette valeur (`var CLE = "…"`). Les arguments se lisent dans
    le script brut (`code_seul` retire les chaînes, donc une clé écrite en clair) ; un appel laissé
    en commentaire compte aussi : l'exception reste du côté le plus strict."""
    js = "\n".join(re.findall(r"<script[^>]*>(.*?)</script>", src, re.S))
    appels = len(re.findall(r"localStorage\.setItem\(", sans_modale.code_seul(src)))
    args = [a.strip() for a in re.findall(r"localStorage\.setItem\(\s*([^,)]*?)\s*,", js)]
    noms = set(re.findall(r"(?:var|let|const)\s+(\w+)\s*=\s*['\"]" + re.escape(cle) + r"['\"]", js))
    return appels > 0 and all(a.strip("'\"`") == cle or a in noms for a in args)


def pages_html(racine):
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [s for s in sous if s not in EXCLUS and not s.startswith(".banc")]
        for f in fichiers:
            if f.lower().endswith(".html"):
                yield os.path.join(dossier, f)


def genre(rel):
    nom = os.path.basename(rel).lower()
    if nom.startswith("qcm") or "/qcm_" in rel.replace("\\", "/"):
        return "qcm"
    if "synthese" in nom:
        return "synthese"
    if nom.startswith("sequence") or "sequence" in nom:
        return "sequence"
    if "atelier" in nom or "cahier" in nom or "tp_" in nom or nom.startswith("tp"):
        return "atelier"
    return "autre"


RESET_IDS = r'(btnReset|btnEffacer|btn-effacer|btnRecommencer|clear)'
RESET_TEXTES = (r"Effacer (ma|ta|la) sauvegarde|Effacer (mes|tes) réponses|Recommencer entièrement|"
                r"Effacer définitivement")


def bouton_reset(src):
    """Le bouton qui efface TOUTE la sauvegarde de la page : (id, texte) ou None.

    Un « Tout effacer » de croquis, un « ↺ Recommencer » de lecteur pas à pas ou un
    « Réinitialiser » de simulateur n'effacent qu'un morceau : ils ne comptent pas.
    """
    m = re.search(r'<button[^>]*id="' + RESET_IDS + r'"[^>]*>(.*?)</button>', src, re.S)
    if m:
        return m.group(1), re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2))).strip()
    m = re.search(r'<button[^>]*?(?:id="([^"]*)")?[^>]*>([^<]*(?:' + RESET_TEXTES + r')[^<]*)</button>', src)
    if m:
        return m.group(1) or "", re.sub(r"\s+", " ", m.group(2)).strip()
    return None


def texte_bouton_reset(src):
    b = bouton_reset(src)
    return b[1] if b else "Effacer ma sauvegarde"


def mesurer_page(src):
    e = {}
    e["stocke"] = "localStorage.setItem(" in src
    # Effacer : retirer la clé, ou un bouton qui remet tout à zéro (les QCM « ♻ Recommencer
    # entièrement » réécrivent un état neuf au lieu de retirer la clé).
    # Un bouton visible qui efface ou remet à zéro (les QCM « ♻ Recommencer entièrement »
    # réécrivent un état neuf au lieu de retirer la clé). Le `oublier(` du kit des ateliers
    # n'efface que le croquis incrusté : il ne compte pas pour la page qui l'accueille.
    e["efface"] = bouton_reset(src) is not None
    e["note"] = 'data-note="poste-partage"' in src
    e["modale"] = len(re.findall(r"\bconfirm\(", sans_modale.code_seul(src)))
    e["faux"] = any(a in src for a, _ in FAUX)
    return e


def mesurer(racine):
    lignes = []
    for p in sorted(pages_html(racine)):
        try:
            src = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            src = open(p, encoding="utf-8", errors="replace").read()
        brut, src = src, sans_mission(src)
        rel = os.path.relpath(p, racine).replace("\\", "/")
        if "localStorage.setItem(" not in src:
            if "localStorage.setItem(" in brut:
                lignes.append({"rel": rel, "genre": genre(rel), "mission_seule": True})
            continue
        e = mesurer_page(src)
        e["rel"], e["genre"] = rel, genre(rel)
        pref = PREFERENCES_SEULES.get(rel)
        e["preference"] = pref[1] if pref and ecrit_seulement(src, pref[0]) else None
        lignes.append(e)
    return lignes


def corriger_page(src):
    """Rend (source corrigée, liste des gestes faits). N'invente rien hors gabarit connu."""
    gestes = []
    for a, b in FAUX:
        if a in src:
            src = src.replace(a, b); gestes.append("formule « personne d'autre ne les voit » corrigée")
    e = mesurer_page(src)
    # 1. Le bouton d'effacement, sur le gabarit « toolbar + btnPrint + const KEY ».
    if not e["efface"] and 'id="btnReset"' not in src:
        mk = re.search(r'const KEY\s*=\s*(["\'][^"\']+["\'])', src)
        tb = re.search(r'(<div class="toolbar"[^>]*>\s*\n?(?:\s*<button[^>]*>[^<]*</button>\n?)*?)'
                       r'(\s*<button class="btn(?: ghost)?" id="btnPrint"[^>]*>[^<]*</button>\n?)', src)
        if mk and tb and "</body>" in src and "localStorage.setItem(KEY" in src:
            src = src[:tb.end()] + BOUTON_RESET + src[tb.end():]
            src = src.replace("</body>", SCRIPT_RESET % mk.group(1) + "</body>", 1)
            gestes.append("bouton « Effacer ma sauvegarde » et son script en deux clics ajoutés")
    # 1 bis. Le QCM du gabarit maison : sa note et son bouton qui efface tout (nom compris).
    if ('data-note="poste-partage"' not in src and src.count(SAVEDNOTE_QCM) == 1
            and re.search(r"\bconst KEY\s*=", src) and "function demande(" in src
            and 'id="btnEffacer"' not in src and "</body>" in src):
        i = src.index(SAVEDNOTE_QCM) + len(SAVEDNOTE_QCM)
        src = src[:i] + "\n" + NOTE_QCM + src[i:]
        j = src.rindex("</body>")
        src = src[:j] + SCRIPT_EFFACER_QCM + src[j:]
        gestes.append("QCM : note poste partagé et bouton « Effacer ma sauvegarde » (nom compris) posés")
    # 2. La note poste partagé, là où la page a un bouton d'effacement nommé.
    if 'data-note="poste-partage"' not in src and bouton_reset(src):
        note = NOTE_POSTE_PARTAGE.format(bouton=texte_bouton_reset(src))
        m = re.search(r'<p class="saved-note">[^<]*(?:navigateur|enregistr)[^<]*(?:<b>[^<]*</b>[^<]*)*</p>', src)
        if m:
            src = src[:m.end()] + "\n" + note + src[m.end():]
            gestes.append("note poste partagé posée après la note de sauvegarde")
        else:
            tb = re.search(r'<div class="toolbar"[^>]*>.*?</div>\s*\n?', src, re.S)
            if tb:
                src = src[:tb.end()] + note + "\n" + src[tb.end():]
                gestes.append("note poste partagé posée après la barre d'outils")
    return src, gestes


def main(argv):
    racine, corrige, muet = ".", False, False
    i = 0
    while i < len(argv):
        if argv[i] == "--racine":
            racine = argv[i + 1]; i += 2
        elif argv[i] == "--corriger":
            corrige = True; i += 1
        elif argv[i] == "--muet":
            muet = True; i += 1
        else:
            print("argument inconnu :", argv[i]); return 2
    lignes = mesurer(racine)
    if not [e for e in lignes if not e.get("mission_seule")]:
        print("⛔ aucune page lue sous %s : rien n'a été vérifié (sortie 2)" % racine); return 2

    if corrige:
        faits = 0
        for e in lignes:
            if e.get("mission_seule"):
                continue
            p = os.path.join(racine, e["rel"])
            src = open(p, encoding="utf-8").read()
            src2, gestes = corriger_page(src)
            if gestes:
                open(p, "w", encoding="utf-8").write(src2); faits += 1
                if not muet:
                    print("✎ %s\n    %s" % (e["rel"], "\n    ".join(gestes)))
        print("— %d page(s) corrigée(s), mesure à nouveau —" % faits)
        lignes = mesurer(racine)

    refus = []
    comptes = {"qcm_sans_note": [], "modale": [], "faux": [], "preference": []}
    mission_seule = [e["rel"] for e in lignes if e.get("mission_seule")]
    lignes = [e for e in lignes if not e.get("mission_seule")]
    for e in lignes:
        if e.get("preference"):
            comptes["preference"].append((e["rel"], e["preference"]))
            continue
        if not e["efface"]:
            refus.append((e["rel"], "stocke dans le navigateur sans aucun moyen d'effacer"))
        if not e["note"]:
            if e["genre"] in ("sequence", "atelier", "autre", "qcm"):
                refus.append((e["rel"], "aucune note « ordinateur partagé » (data-note=\"poste-partage\")"))
            else:
                comptes["qcm_sans_note"].append(e["rel"])
        if e["modale"]:
            comptes["modale"].append(e["rel"])
        if e["faux"]:
            refus.append((e["rel"], "affirme « personne d'autre ne les voit » : faux sur un poste partagé"))

    n = len(lignes)
    if not muet:
        for rel, raison in refus:
            print("✘ %s — %s" % (rel, raison))
        if comptes["modale"]:
            print("ℹ %d page(s) ouvrent une boîte modale confirm() (à ramener en deux clics dans la page ; "
                  "source principale : kit.js des ateliers de représentation) :" % len(comptes["modale"]))
            for rel in comptes["modale"]:
                print("    · " + rel)
        for rel, quoi in comptes["preference"]:
            print("ℹ %s — garde seulement une préférence d'affichage : %s (aucune réponse, pas de refus)" % (rel, quoi))
        if comptes["qcm_sans_note"]:
            print("ℹ %d QCM gardent un score dans le navigateur sans note poste partagé (décision, pas un refus)"
                  % len(comptes["qcm_sans_note"]))
        if mission_seule:
            print("ℹ %d page(s) n'enregistrent rien d'elles-mêmes et ne gardent que le choix d'affichage du mode "
                  "mission (joué par banc_defaut.mjs et banc_lecture.mjs ; pas de refus)" % len(mission_seule))
    print("%d page(s) lues qui écrivent dans localStorage · %d refus · %d confirm() · %d QCM sans note"
          % (n, len(refus), len(comptes["modale"]), len(comptes["qcm_sans_note"])))
    if refus:
        print("✘ une page qui garde les réponses de l'élève doit savoir les effacer et prévenir du poste partagé")
        return 1
    print("✅ chaque page qui garde les réponses (séquence, atelier, QCM) sait les effacer et prévient du poste partagé")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
