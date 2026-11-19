# -*- coding: utf-8 -*-
"""entete_telephone.py — au téléphone, dès la séance 2, l'en-tête des réglages se replie en une ligne.

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
Mesure à 390 px, séance 2, page complète : onglets sous le premier écran sur 27 pages sur 63 avant, 14 après (des pages
où un grand bloc précède les onglets : banc d'essai, ateliers de planification, bandeau des tâches déplié).

  python3 _outils/entete_telephone.py [--ecrire] [page.html | dossier …]   (sans chemin : les trois thèmes)

Sortie : 0 rien à poser ou tout posé · 1 une page reste à poser (sans --ecrire) · 2 rien lu (n°299).
"""
from __future__ import annotations

import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUT = "<!-- entete-telephone v1 : début — en-tête replié au téléphone dès la séance 2 ; source unique : _outils/entete_telephone.py -->"
FIN = "<!-- entete-telephone v1 : fin -->"
BLOC_RE = re.compile(r"<!-- entete-telephone v\d+ : début.*?<!-- entete-telephone v\d+ : fin -->\n?", re.S)
BLOC_CORPS = r"""<style>
.entete-bascule{display:none}
@media screen and (max-width:600px){
  body.entete-pliable .entete-bascule{display:block;width:100%;margin:8px 0;padding:9px 14px;font:inherit;font-weight:600;
    text-align:left;color:inherit;background:transparent;border:1px solid currentColor;border-radius:10px;cursor:pointer;min-height:44px}
  .entete-bascule small{display:block;font-weight:400;opacity:.85;margin-top:2px}
  body.entete-replie .entete-reglage{display:none!important}
  body.entete-replie .entete-reglage-partiel{display:block!important;margin:2px 0!important;padding:0!important;border:0!important;background:none!important}
  body.entete-replie .entete-reglage-partiel > :not(.entete-garde){display:none!important}
}
</style>
<script>
(function(){
  "use strict";
  var onglets = [].slice.call(document.querySelectorAll(".seance-tab"));
  /* des onglets qui sont des liens mènent à d'autres pages (séquence découpée) : rien à replier ici */
  if (onglets.length < 2 || onglets.some(function(o){ return o.matches("a[href]"); })) return;
  var barre = onglets[0].closest(".seance-tabs") || onglets[0].parentElement;
  var parent = barre.parentElement; if (!parent) return;
  var REGLAGES = "#identite, .identite, .toolbar, .choix-parcours-boutons, [data-note=poste-partage], #aide-essentiel";
  var ETAT = "#savedNote, [role=status]:not(button), [aria-live]:not(button)";   /* un bouton qui parle (« clique encore ») n'est pas une zone d'état */
  var reglages = [];
  for (var c = parent.firstElementChild; c && c !== barre; c = c.nextElementSibling){
    if (c.id === "ouverture" || c.classList.contains("rappel-ouverture")) break;   /* le volet « Rappel » et la suite restent */
    if (!c.matches(REGLAGES) || c.matches(ETAT)) continue;                         /* une zone d'état reste toujours visible */
    var etats = c.querySelectorAll(ETAT);
    if (etats.length){
      /* un bloc qui porte une zone d'état (« 💾 Sauvegardé » dans le bloc du nom) : seule la zone reste */
      c.classList.add("entete-reglage-partiel");
      [].forEach.call(etats, function(e){ while (e.parentElement && e.parentElement !== c) e = e.parentElement; e.classList.add("entete-garde"); });
    } else c.classList.add("entete-reglage");
    reglages.push(c);
  }
  if (!reglages.length) return;
  var bouton = document.createElement("button");
  bouton.type = "button"; bouton.className = "entete-bascule"; bouton.setAttribute("aria-expanded", "false");
  reglages[0].parentNode.insertBefore(bouton, reglages[0]);
  var champs = [].slice.call(document.querySelectorAll("#identite input, .identite input")).filter(function(i){ return reglages.some(function(r){ return r.contains(i); }); });
  function libelle(){
    var qui = champs.map(function(i){ return String(i.value || "").trim(); }).filter(Boolean).join(" ");
    bouton.innerHTML = "⚙️ Mon nom, mon parcours, mes réglages"
      + (champs.length ? "<small>" + (qui ? "👤 " + qui.replace(/[&<>"]/g, "") : "✏️ Ton nom n'est pas encore écrit") + "</small>" : "");
  }
  var ouvert = false, mq = window.matchMedia("(max-width: 600px)");
  function seance(){
    for (var i = 0; i < onglets.length; i++)
      if (onglets[i].classList.contains("active") || onglets[i].getAttribute("aria-selected") === "true") return i;
    return 0;
  }
  function maj(){
    var pliable = mq.matches && seance() > 0;
    document.body.classList.toggle("entete-pliable", pliable);
    document.body.classList.toggle("entete-replie", pliable && !ouvert);
    bouton.setAttribute("aria-expanded", String(!pliable || ouvert));
  }
  bouton.addEventListener("click", function(){ ouvert = !ouvert; maj(); });
  champs.forEach(function(i){ i.addEventListener("input", libelle); });
  new MutationObserver(maj).observe(barre, { subtree:true, attributes:true, attributeFilter:["class", "aria-selected"] });
  if (mq.addEventListener) mq.addEventListener("change", maj); else if (mq.addListener) mq.addListener(maj);
  libelle(); maj();
  /* la sauvegarde remet le nom au chargement : le libellé le suit */
  window.addEventListener("load", function(){ setTimeout(libelle, 0); });
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
