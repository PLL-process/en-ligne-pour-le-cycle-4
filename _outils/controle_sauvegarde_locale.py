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
     est NOTE_POSTE_PARTAGE ci-dessous). Exigée pour les séquences et les ateliers, qui
     gardent des réponses rédigées ; seulement comptée pour les QCM, qui ne gardent qu'un
     score (décision à prendre, pas un défaut).
  3. SANS BOÎTE MODALE — aucun `confirm(` : la confirmation se fait en deux clics dans la
     page (`demande()` ou l'armement du bouton), jamais par une boîte du navigateur qui
     bloque la page et échappe au lecteur d'écran. Comptée, pas refusée : 52 pages la
     tiennent du `kit.js` des ateliers de représentation (incrustations), à corriger à la
     source par le skill `ateliers-representations-depot`.

`--corriger` répare ce qui suit un gabarit connu, et seulement cela :
  · une séquence dont la barre `.toolbar` porte « Imprimer » mais pas de bouton d'effacement,
    avec `const KEY = "…"` : le bouton « 🗑 Effacer ma sauvegarde » est ajouté, et un script
    autonome l'arme en deux clics (six secondes) puis efface la clé et recharge ;
  · une séquence ou un atelier qui porte un bouton `btnReset` et pas de note poste partagé :
    la note est posée après la note « enregistrées dans ce navigateur » si elle existe, sinon
    après la barre d'outils ;
  · « personne d'autre ne les voit » devient « rien n'est envoyé en ligne ».
Le reste (QCM, pages sans gabarit connu, `confirm(` du kit) est listé, pas touché.

Usage : python3 _outils/controle_sauvegarde_locale.py [--racine .] [--corriger] [--muet]
Sortie 0 si rien à refuser, 1 s'il reste un écart (effacement ou note manquants sur une
séquence ou un atelier), 2 si aucune page n'a pu être lue (règle d'or n°299).
"""
import os
import re
import sys

EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation"}

NOTE_POSTE_PARTAGE = (
    '<p class="saved-note" data-note="poste-partage">🖥️ <b>Ordinateur partagé</b> (salle de techno, CDI)&nbsp;: '
    'un autre élève qui ouvre cette page sur la même session verra tes réponses.<br>'
    'Quand tu as fini&nbsp;: imprime en PDF si tu veux garder une trace, puis clique sur '
    '«&nbsp;{bouton}&nbsp;».</p>'
)

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

FAUX = [
    ("rien n'est envoyé, personne d'autre ne les voit", "rien n'est envoyé en ligne"),
]


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
    e["modale"] = len(re.findall(r"\bconfirm\(", src))
    e["faux"] = any(a in src for a, _ in FAUX)
    return e


def mesurer(racine):
    lignes = []
    for p in sorted(pages_html(racine)):
        try:
            src = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            src = open(p, encoding="utf-8", errors="replace").read()
        if "localStorage.setItem(" not in src:
            continue
        rel = os.path.relpath(p, racine).replace("\\", "/")
        e = mesurer_page(src)
        e["rel"], e["genre"] = rel, genre(rel)
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
    if not lignes:
        print("⛔ aucune page lue sous %s : rien n'a été vérifié (sortie 2)" % racine); return 2

    if corrige:
        faits = 0
        for e in lignes:
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
    comptes = {"qcm_sans_note": [], "modale": [], "faux": []}
    for e in lignes:
        if not e["efface"]:
            refus.append((e["rel"], "stocke dans le navigateur sans aucun moyen d'effacer"))
        if not e["note"]:
            if e["genre"] in ("sequence", "atelier", "autre"):
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
        if comptes["qcm_sans_note"]:
            print("ℹ %d QCM gardent un score dans le navigateur sans note poste partagé (décision, pas un refus)"
                  % len(comptes["qcm_sans_note"]))
    print("%d page(s) lues qui écrivent dans localStorage · %d refus · %d confirm() · %d QCM sans note"
          % (n, len(refus), len(comptes["modale"]), len(comptes["qcm_sans_note"])))
    if refus:
        print("✘ une page qui garde les réponses de l'élève doit savoir les effacer et prévenir du poste partagé")
        return 1
    print("✅ chaque séquence et atelier qui garde les réponses sait les effacer et prévient du poste partagé")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
