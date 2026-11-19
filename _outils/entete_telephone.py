# -*- coding: utf-8 -*-
"""entete_telephone.py — au téléphone, dès la séance 2, l'en-tête se replie : la séance prend le premier écran.

LE CONSTAT
----------
Le banc de la n°311 de `4e_C7.1` est rouge depuis des semaines (journal du 18/11/2026) : à 390 px, en séance 2, les
onglets des séances tombent sous le premier écran (bas à 1 063 px pour 844). L'en-tête a grandi depuis la n°311 : nom
et classe (96 px), boutons de la page (72 px), note « Ordinateur partagé » (99 px), choix du parcours (122 px). Mesuré
le 19/11/2026 sur les 63 pages à onglets : 27 pages au-delà du premier écran. Le journal l'annonçait : « un en-tête qui
se replie au téléphone à partir de la séance 2, comme « Où j'en suis » ».

LA DÉCISION
-----------
Pascal, le 19/11/2026 : « Je te donne carte blanche. Choisis ce qui est meilleur pour l'élève. » Au téléphone, l'élève
de séance 2 veut retrouver sa séance ; le nom s'écrit une fois, le parcours se choisit une fois, imprimer ou effacer
servent en fin de séance, et la note « Ordinateur partagé » ne parle pas d'un téléphone. Ces réglages restent à un
appui, et ce qu'ils disent reste lisible : le nom de l'élève sur le bouton, « 💾 Sauvegardé » et « Parcours affiché ».
La règle n°311 (« un outil n'est pas du décor ») est précisée en conséquence : un outil reste hors du volet « Rappel »
et visible — ou, au téléphone dès la séance 2, à un appui derrière « ⚙️ » ; les bancs communs le vérifient.

CE QUE POSE L'OUTIL
-------------------
Un petit bloc (style et script), entre deux marqueurs, avant `</body>`, sur chaque page à onglets de séance (des
onglets qui sont des liens — une séquence découpée en pages — ne sont pas touchés) :
  · les RÉGLAGES sont les blocs, frères de la barre d'onglets et placés avant le volet « 📖 Rappel » (ou avant les
    onglets), qui portent le nom et la classe (`#identite`), les boutons de la page (`.toolbar`), le choix du
    parcours (`.choix-parcours-boutons`), la note « Ordinateur partagé » (`data-note="poste-partage"`) et l'aide du
    mode essentiel (`#aide-essentiel`) ;
  · une ZONE D'ÉTAT ne se replie jamais (`#savedNote`, `role=status`, `aria-live`, hors boutons) : `#parcoursNote` reste,
    et dans un bloc qui en porte une (« 💾 Sauvegardé » dans le bloc du nom), seule la zone reste visible — les messages
    de la page s'y écrivent (`_outils/sans_modale.py` : « le message doit être vu ») ;
  · sur un écran de 600 px au plus, dès que la séance ouverte n'est pas la première, les réglages se replient derrière
    un seul bouton « ⚙️ Mon nom, mon parcours, mes réglages », qui porte le nom écrit par l'élève (ou « ✏️ Ton nom
    n'est pas encore écrit ») et les rouvre (et les replie) d'un appui ;
  · séance 1, grand écran, impression : rien ne change. Rien n'est retiré de la page : les blocs sont seulement
    masqués, les scripts de la page les trouvent toujours.
La séance ouverte se lit sur l'onglet (`.active` ou `aria-selected`) et se suit par un MutationObserver : un clic,
le mode mission ou la séance rouverte au chargement replient l'en-tête de la même façon.

v2 (19/11/2026, les 14 pages qui restaient) :
  · un cadre d'en-tête (`div.container` d'une page plus ancienne) qui porte les réglages : ses enfants directs comptent ;
  · l'INVITATION AU MODE MISSION (« 🎮 Mode mission », « ⏸️ Figer les animations ») est un réglage, où qu'elle soit
    avant les onglets ; le petit bouton flottant « 🎮 Mode mission » (Pascal, 16/11/2026 : revenir en mission doit
    rester visible) reste ;
  · une CARTE DE TÊTE — `section.card` ou `div.card` posée avant les onglets, hors réglages et hors « Où j'en suis » :
    le banc d'essai, l'éditeur de programme, « Où en suis-je ? », l'ouverture d'un atelier — se replie en une ligne
    « ▸ son titre court » ; des cartes qui se suivent se replient ensemble (la seconde ligne nomme les autres). Un appui
    l'ouvre sous le doigt. Repliée, elle garde sa largeur (un simulateur se dessine à la bonne taille) et elle est
    inerte ; une carte courte (moins de deux fois et demie la hauteur du bouton) ne se replie pas ;
  · le titre de la séquence passe à 1,3 em (ses marges restent : une barre de navigation fixe le recouvrirait).
Mesure à 390 px, séance 2, page complète : onglets sous le premier écran sur 27 pages sur 63 avant la v1, 14 après la
v1, **1** après la v2 (`3e_C9.2`, huit onglets : bas à 859 px, la première rangée se voit).

  python3 _outils/entete_telephone.py [--ecrire] [page.html | dossier …]   (sans chemin : les trois thèmes)

Sortie : 0 rien à poser ou tout posé · 1 une page reste à poser (sans --ecrire) · 2 rien lu (n°299).
"""
from __future__ import annotations

import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUT = "<!-- entete-telephone v2 : début — en-tête replié au téléphone dès la séance 2 ; source unique : _outils/entete_telephone.py -->"
FIN = "<!-- entete-telephone v2 : fin -->"
BLOC_RE = re.compile(r"<!-- entete-telephone v\d+ : début.*?<!-- entete-telephone v\d+ : fin -->\n?", re.S)
BLOC_CORPS = r"""<style>
.entete-bascule,.entete-carte-bascule{display:none}
@media screen and (max-width:600px){
  body.entete-pliable .entete-bascule,body.entete-pliable .entete-carte-bascule{display:block;width:100%;margin:8px 0;padding:9px 14px;
    font:inherit;font-weight:600;text-align:left;color:inherit;background:transparent;border:1px solid currentColor;border-radius:10px;
    cursor:pointer;min-height:44px}
  .entete-bascule small,.entete-carte-bascule small{display:block;font-weight:400;opacity:.85;margin-top:2px}
  .entete-carte-bascule[hidden]{display:none!important}
  /* le titre de la séquence reste, en plus petit : la séance prend le premier écran */
  body.entete-pliable h1{font-size:1.3em!important;line-height:1.25!important}   /* ses marges restent : une barre de navigation fixe le recouvrirait */
  body.entete-replie .entete-reglage{display:none!important}
  body.entete-replie .entete-reglage-partiel{display:block!important;margin:2px 0!important;padding:0!important;border:0!important;background:none!important}
  body.entete-replie .entete-reglage-partiel > :not(.entete-garde){display:none!important}
  /* l'invitation au mode mission : ses boutons passent derrière « ⚙️ » ; le petit bouton flottant « 🎮 Mode mission »
     (Pascal, 16/11/2026 : revenir en mission doit rester visible) reste */
  body.entete-replie .entete-invite{margin:0!important}
  body.entete-replie .entete-invite > :not(.ms-revenir){display:none!important}
  /* une carte de tête repliée garde sa largeur (un simulateur, un éditeur se dessinent à la bonne taille) : elle est
     seulement écrasée, et rendue inerte */
  body.entete-pliable .entete-carte.entete-carte-pliee{max-height:0!important;overflow:hidden!important;margin:0!important;
    padding-top:0!important;padding-bottom:0!important;border:0!important;box-shadow:none!important}
}
</style>
<script>
(function(){
  "use strict";
  /* posé après le mode mission : on attend que la page ait construit ses boutons (l'invitation au mode mission naît au
     chargement du document) */
  function preparer(){
  var onglets = [].slice.call(document.querySelectorAll(".seance-tab"));
  /* des onglets qui sont des liens mènent à d'autres pages (séquence découpée) : rien à replier ici */
  if (onglets.length < 2 || onglets.some(function(o){ return o.matches("a[href]"); })) return;
  var barre = onglets[0].closest(".seance-tabs") || onglets[0].parentElement;
  var parent = barre.parentElement; if (!parent) return;
  var REGLAGES = "#identite, .identite, .toolbar, .choix-parcours-boutons, [data-note=poste-partage], #aide-essentiel";
  var ETAT = "#savedNote, [role=status]:not(button), [aria-live]:not(button)";   /* un bouton qui parle (« clique encore ») n'est pas une zone d'état */
  var CARTE = "section.card, div.card";
  var reglages = [], cartes = [], groupe = null, rappel = false;
  function reglage(c){
    if (c.matches(ETAT)) return;                                                   /* une zone d'état reste toujours visible */
    var etats = c.querySelectorAll(ETAT);
    if (etats.length){
      /* un bloc qui porte une zone d'état (« 💾 Sauvegardé » dans le bloc du nom) : seule la zone reste */
      c.classList.add("entete-reglage-partiel");
      [].forEach.call(etats, function(e){ while (e.parentElement && e.parentElement !== c) e = e.parentElement; e.classList.add("entete-garde"); });
    } else c.classList.add("entete-reglage");
    reglages.push(c);
  }
  for (var c = parent.firstElementChild; c && c !== barre; c = c.nextElementSibling){
    if (c.id === "ouverture" || c.classList.contains("rappel-ouverture")){ rappel = true; groupe = null; continue; }
    /* une CARTE DE TÊTE (v2) : un outil ou un texte de toutes les séances, posé avant les onglets — le banc d'essai,
       l'éditeur, « Où en suis-je ? », l'ouverture d'un atelier. Des cartes qui se suivent se replient ensemble */
    if (c.matches(CARTE) && !c.classList.contains("ou-jen-suis") && !c.matches(REGLAGES)){
      if (!groupe){ groupe = []; cartes.push(groupe); }
      groupe.push(c); continue;
    }
    if (c.getClientRects().length) groupe = null;
    if (rappel) continue;                                                          /* après le volet « Rappel », pas de réglage */
    if (c.matches(REGLAGES)) reglage(c);
    /* un cadre d'en-tête (`div.container`) qui porte les réglages : on regarde ses enfants directs */
    else if (c.matches("div, header") && !c.matches(CARTE)) [].forEach.call(c.children, function(k){ if (k.matches(REGLAGES)) reglage(k); });
  }
  var invites = [].filter.call(document.querySelectorAll(".ms-invite"), function(m){
    return (m.compareDocumentPosition(barre) & Node.DOCUMENT_POSITION_FOLLOWING) && !m.closest("#ouverture");
  });
  invites.forEach(function(m){ m.classList.add("entete-invite"); });
  if (!reglages.length && !invites.length && !cartes.length) return;
  var mq = window.matchMedia("(max-width: 600px)"), ouvert = false, bouton = null;
  if (reglages.length || invites.length){
    bouton = document.createElement("button");
    bouton.type = "button"; bouton.className = "entete-bascule"; bouton.setAttribute("aria-expanded", "false");
    var premier = reglages[0] || invites[0];
    premier.parentNode.insertBefore(bouton, premier);
  }
  var champs = [].slice.call(document.querySelectorAll("#identite input, .identite input")).filter(function(i){ return reglages.some(function(r){ return r.contains(i); }); });
  function libelle(){
    if (!bouton) return;
    var qui = champs.map(function(i){ return String(i.value || "").trim(); }).filter(Boolean).join(" ");
    bouton.innerHTML = "⚙️ Mon nom, mon parcours, mes réglages"
      + (champs.length ? "<small>" + (qui ? "👤 " + qui.replace(/[&<>"]/g, "") : "✏️ Ton nom n'est pas encore écrit") + "</small>" : "");
  }
  function titre(carte){
    var h = carte.querySelector("h2, h3, summary");
    /* le titre court : sans sa parenthèse ni sa précision après un tiret (« Le banc d'essai de la station (version 🅱 …) ») */
    var t = h ? h.textContent.replace(/\s+/g, " ").trim() : "Une carte de la séquence";
    return t.replace(/\s*\(.*$/, "").replace(/\s+[—–]\s.*$/, "") || t;
  }
  var volets = cartes.map(function(g){
    var b = document.createElement("button");
    b.type = "button"; b.className = "entete-carte-bascule"; b.setAttribute("aria-expanded", "false");
    var noms = g.map(titre), autres = noms.slice(1);
    /* une ligne pour une carte (« ▸ » dit qu'elle s'ouvre) ; pour un groupe, la seconde ligne nomme les autres cartes */
    b.innerHTML = "▸ " + noms[0].replace(/[&<>"]/g, "")
      + (autres.length ? "<small>et " + autres.length + " autre" + (autres.length > 1 ? "s" : "") + " carte" + (autres.length > 1 ? "s" : "")
        + " : " + autres.join(" · ").replace(/[&<>"]/g, "") + "</small>" : "");
    b.setAttribute("aria-label", noms.join(", ") + " : " + (g.length > 1 ? "ces cartes servent" : "cette carte sert") + " à toutes les séances ; un appui les ouvre ou les replie");
    g[0].parentNode.insertBefore(b, g[0]);
    g.forEach(function(x){ x.classList.add("entete-carte"); });
    var v = { b: b, g: g, ouvert: false, utile: null };
    b.addEventListener("click", function(){ v.ouvert = !v.ouvert; maj(); });   /* la carte s'ouvre sous le bouton, qui reste sous le doigt */
    return v;
  });
  function seance(){
    for (var i = 0; i < onglets.length; i++)
      if (onglets[i].classList.contains("active") || onglets[i].getAttribute("aria-selected") === "true") return i;
    return 0;
  }
  function maj(){
    var pliable = mq.matches && seance() > 0;
    document.body.classList.toggle("entete-pliable", pliable);
    document.body.classList.toggle("entete-replie", pliable && !ouvert);
    if (bouton) bouton.setAttribute("aria-expanded", String(!pliable || ouvert));
    volets.forEach(function(v){
      /* une carte courte ne se replie pas : le bouton prendrait autant de place qu'elle (mesurée dépliée, au téléphone) */
      if (pliable && v.utile === null){
        var h = 0; v.g.forEach(function(x){ h += x.getBoundingClientRect().height; }); v.utile = h > 2.5 * (v.b.getBoundingClientRect().height || 70);
      }
      var plie = pliable && v.utile === true && !v.ouvert;
      v.b.hidden = !(pliable && v.utile === true);
      v.b.setAttribute("aria-expanded", String(!plie));
      v.b.firstChild.nodeValue = (plie ? "▸ " : "▾ ") + v.b.firstChild.nodeValue.slice(2);
      v.g.forEach(function(x){ x.classList.toggle("entete-carte-pliee", plie); x.inert = plie; });
    });
  }
  if (bouton) bouton.addEventListener("click", function(){ ouvert = !ouvert; maj(); });
  champs.forEach(function(i){ i.addEventListener("input", libelle); });
  new MutationObserver(maj).observe(barre, { subtree:true, attributes:true, attributeFilter:["class", "aria-selected"] });
  if (mq.addEventListener) mq.addEventListener("change", maj); else if (mq.addListener) mq.addListener(maj);
  libelle(); maj();
  /* la sauvegarde remet le nom au chargement : le libellé le suit */
  window.addEventListener("load", function(){ setTimeout(libelle, 0); });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", preparer); else preparer();
})();
</script>"""
BLOC = DEBUT + "\n" + BLOC_CORPS + "\n" + FIN + "\n"


def a_poser(s: str) -> bool:
    return 'class="seance-tab' in s


def poser(s: str) -> str:
    if BLOC_RE.search(s):
        return BLOC_RE.sub(lambda _: BLOC, s, count=1)
    if not a_poser(s):
        return s
    i = s.rfind("</body>")
    if i < 0:
        return s
    return s[:i] + BLOC + s[i:]


def pages(chemins):
    out = []
    for c in chemins or [os.path.join(DEPOT, t) for t in sorted(os.listdir(DEPOT)) if t.startswith("theme-")]:
        if os.path.isfile(c):
            out.append(c)
            continue
        for d, _, fs in os.walk(c):
            if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d or "_generation" in d:
                continue
            out += [os.path.join(d, f) for f in sorted(fs) if f.endswith(".html")]
    return sorted(out)


def main(argv):
    ecrire = "--ecrire" in argv
    ps = pages([a for a in argv if not a.startswith("--")])
    if not ps:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    avec = poses = reste = 0
    for p in ps:
        s = open(p, encoding="utf-8").read()
        if not a_poser(s):
            continue
        avec += 1
        u = poser(s)
        if u != s:
            if ecrire:
                open(p, "w", encoding="utf-8").write(u)
                poses += 1
            else:
                reste += 1
                print("  ⚠ %s — l'en-tête ne se replie pas au téléphone" % os.path.relpath(p, DEPOT))
    print("%d page(s) lues · %d à onglets de séance · %d posée(s) · %d à poser" % (len(ps), avec, poses, reste))
    return 1 if (reste and not ecrire) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
