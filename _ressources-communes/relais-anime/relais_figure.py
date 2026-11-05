#!/usr/bin/env python3
"""relais_figure.py — le relais qui claque, vu en coupe et animé : une seule figure, posée dans les pages.

Pascal, le 05/11/2026, sur la situation déclenchante de 4e_C7.4 (« le capteur lit l'humidité, la carte décide, le relais
claque, la pompe arrose ») : « le relais claque, il faudrait vulgariser ou expliquer ce terme ; il manque aussi des images
réalistes ou des schémas ou une animation ».

La figure est écrite EN HTML dans la page (un SVG au repos, lisible sans JavaScript et à l'impression), entre deux marques :
    <!-- relais-anime:debut --> … <!-- relais-anime:fin -->
`relais-anime.js` l'anime (boutons, son facultatif, compteur) ; `relais-anime.css` l'habille.

Usage :
    python3 _ressources-communes/relais-anime/relais_figure.py            # vérifie que chaque page est à jour
    python3 _ressources-communes/relais-anime/relais_figure.py --ecrire   # réécrit la figure dans chaque page

Chaque page est décrite dans PAGES : son chemin, et son titre de figure (la phrase de la page qui a besoin d'elle).
"""
import os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(os.path.dirname(ICI))
T3 = "theme-3-creation-conception-realisation-innovations/"

PAGES = {
    T3 + "C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.4/sequence_4e_C7.4_energie-du-jardin.html":
        "🔎 « Le relais claque » : ce qui se passe dans le boîtier",
    T3 + "C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.5/sequence_4e_C7.5_jardin-incomplet.html":
        "🔎 « Le relais doit claquer » : ce qui se passe dans le boîtier",
    T3 + "C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html":
        "🔎 « Le relais claque » : ce que la pompe qui s'affole fait au relais",
}

DEBUT, FIN = "<!-- relais-anime:debut -->", "<!-- relais-anime:fin -->"


def ressort(x, y0, longueur, spires=7, largeur=9):
    """Un ressort en zigzag, vertical, de (x, y0) vers le bas, sur `longueur`."""
    pas = longueur / (spires * 2 + 2)
    pts = ["M%.1f %.1f" % (x, y0), "L%.1f %.1f" % (x, y0 + pas)]
    for k in range(spires * 2):
        pts.append("L%.1f %.1f" % (x + (largeur if k % 2 == 0 else -largeur), y0 + pas * (k + 1.5)))
    pts.append("L%.1f %.1f" % (x, y0 + longueur - pas))
    pts.append("L%.1f %.1f" % (x, y0 + longueur))
    return " ".join(pts)


def svg(pid):
    """Le relais au repos (ordre coupé). Toutes les mesures sont dans le repère 760 × 340."""
    R = ressort(430, 96, 74)                     # attaché en haut du boîtier (430, 96) ; la feuille de style l'étire
    return f'''<svg class="ra-svg" viewBox="0 0 760 340" role="img" aria-labelledby="{pid}-t {pid}-d">
  <title id="{pid}-t">Le relais, vu en coupe : la carte commande une bobine, la bobine attire une lame, la lame ferme le circuit de la pompe</title>
  <desc id="{pid}-d">En haut, le chemin de l'ordre : le capteur mesure, la carte décide, le relais distribue, la pompe arrose.
  À gauche, la carte et le circuit de la carte, où passe un tout petit courant, jusqu'à la bobine du relais. Au milieu,
  l'intérieur du relais : une lame de métal tourne autour d'un axe ; un ressort la tire vers le haut ; sous elle, la bobine.
  À droite, le circuit de la pompe, avec son alimentation. Au repos, la lame est levée : le circuit de la pompe est ouvert,
  la pompe est arrêtée. Quand la carte envoie l'ordre, la bobine devient un aimant et attire la lame : la lame touche le
  contact avec un bruit sec, « clac », le circuit de la pompe se ferme et la pompe tourne. Quand la carte coupe l'ordre,
  le ressort relève la lame : « clac » encore, et la pompe s'arrête.</desc>
  <!-- le chemin de l'ordre -->
  <g class="ra-chaine">
    <rect class="ra-pastille" x="16" y="6" width="150" height="30" rx="15"/><text x="91" y="26">Le capteur mesure</text>
    <rect class="ra-pastille" x="206" y="6" width="150" height="30" rx="15"/><text x="281" y="26">La carte décide</text>
    <rect class="ra-pastille ra-pastille-relais" x="396" y="6" width="166" height="30" rx="15"/><text x="479" y="26">Le relais distribue</text>
    <rect class="ra-pastille ra-pastille-pompe" x="602" y="6" width="142" height="30" rx="15"/><text x="673" y="26">La pompe arrose</text>
    <path class="ra-fleche-chaine" d="M170 21 H200 M194 16 L201 21 L194 26 M360 21 H390 M384 16 L391 21 L384 26 M566 21 H596 M590 16 L597 21 L590 26"/>
  </g>
  <text class="ra-titre-coupe" x="385" y="70">dans le boîtier du relais, vu en coupe</text>
  <rect class="ra-boitier" x="250" y="80" width="270" height="222" rx="12"/>
  <!-- ② le circuit de la pompe -->
  <path class="ra-fil ra-fil-pompe" d="M300 190 H240 V50 H600 V150 H642 M698 150 H735 V262 H712 M650 262 H560 V202 H495"/>
  <path class="ra-courant ra-courant-pompe" d="M300 190 H240 V50 H600 V150 H642 M698 150 H735 V262 H712 M650 262 H560 V202 H495"/>
  <g class="ra-pile"><line x1="712" y1="246" x2="712" y2="278"/><line x1="700" y1="252" x2="700" y2="272"/>
    <line x1="688" y1="246" x2="688" y2="278"/><line x1="676" y1="252" x2="676" y2="272"/><line x1="676" y1="262" x2="650" y2="262"/>
    <line x1="700" y1="262" x2="688" y2="262"/></g>
  <text class="ra-etiquette" x="681" y="298">l'alimentation</text>
  <text class="ra-etiquette" x="681" y="313">de la pompe</text>
  <circle class="ra-pompe" cx="670" cy="150" r="28"/>
  <g class="ra-rotor"><path d="M670 150 L670 130 M670 150 L687.3 160 M670 150 L652.7 160"/><circle cx="670" cy="150" r="4"/></g>
  <text class="ra-etiquette" x="670" y="198">la pompe</text>
  <text class="ra-titre-circuit ra-titre-pompe" x="612" y="92">② le circuit de la pompe</text>
  <text class="ra-etiquette ra-sous-titre" x="612" y="108">un courant fort</text>
  <!-- ① le circuit de la carte -->
  <rect class="ra-carte" x="26" y="196" width="168" height="78" rx="8"/>
  <text class="ra-carte-texte" x="110" y="226">la carte</text>
  <text class="ra-etiquette" x="110" y="246">broche D4</text>
  <text class="ra-ordre" x="110" y="264">ordre : 0 (coupé)</text>
  <path class="ra-fil ra-fil-carte" d="M194 222 H330 M194 252 H330"/>
  <path class="ra-courant ra-courant-carte" d="M194 222 H330 M330 252 H194"/>
  <text class="ra-titre-circuit ra-titre-carte" x="26" y="300">① le circuit de la carte</text>
  <text class="ra-etiquette ra-sous-titre" x="26" y="316">un tout petit courant</text>
  <!-- l'intérieur du relais -->
  <g class="ra-champ"><path d="M406 214 Q426 237 406 260"/><path d="M406 208 Q442 237 406 266"/></g>
  <rect class="ra-bobine" x="330" y="205" width="70" height="64" rx="5"/>
  <path class="ra-spires" d="M330 214 H400 M330 224 H400 M330 234 H400 M330 244 H400 M330 254 H400 M330 264 H400"/>
  <text class="ra-etiquette" x="365" y="290">la bobine</text>
  <rect class="ra-contact" x="468" y="198" width="27" height="8" rx="2"/>
  <text class="ra-etiquette" x="481" y="222">le contact</text>
  <g class="ra-ressort-groupe"><path class="ra-ressort" d="{R}"/></g>
  <text class="ra-etiquette ra-etiquette-gauche" x="445" y="122">le ressort</text>
  <g class="ra-lame-groupe">
    <line class="ra-lame" x1="300" y1="190" x2="480" y2="190"/>
    <circle class="ra-plot" cx="480" cy="194" r="4"/>
  </g>
  <circle class="ra-axe" cx="300" cy="190" r="6"/>
  <text class="ra-etiquette" x="335" y="174">la lame</text>
  <text class="ra-clac" x="512" y="168">clac&nbsp;!</text>
</svg>'''


def figure(pid, titre):
    return f'''{DEBUT}
<!-- Généré par _ressources-communes/relais-anime/relais_figure.py : ne pas modifier à la main (relancer le script). -->
<figure class="relais-anime" id="{pid}" aria-labelledby="{pid}-titre">
  <p class="ra-titre" id="{pid}-titre">{titre}</p>
  <p class="ra-explique">Un <b>relais</b>, c'est un <b>interrupteur que la carte actionne toute seule</b>. La carte ne peut envoyer qu'un tout petit courant, bien trop faible pour faire tourner la pompe. Ce petit courant passe dans une <b>bobine</b> (un fil enroulé)&nbsp;: elle devient un <b>aimant</b>, attire une <b>lame</b> de métal, et la lame vient toucher un <b>contact</b>&nbsp;: le circuit de la pompe est fermé, la pompe tourne. Ce mouvement fait un petit bruit sec, «&nbsp;clac&nbsp;»&nbsp;: c'est ça, <b>«&nbsp;le relais claque&nbsp;»</b>. Quand la carte coupe l'ordre, un <b>ressort</b> relève la lame&nbsp;: «&nbsp;clac&nbsp;» encore, et la pompe s'arrête.</p>
  {svg(pid)}
  <div class="ra-commandes" hidden>
    <button type="button" class="btn ra-btn ra-envoyer">▶ La carte envoie l'ordre (D4 = 1)</button>
    <button type="button" class="btn ra-btn ra-couper">⏹ La carte coupe l'ordre (D4 = 0)</button>
    <button type="button" class="btn ra-btn ra-battre">🔁 Faire battre 6 fois</button>
    <button type="button" class="btn ra-btn ra-son" aria-pressed="false">🔇 Son coupé</button>
  </div>
  <p class="ra-etat" role="status" aria-live="polite" hidden></p>
  <figcaption class="ra-legende"><b>Ce que tu dois voir&nbsp;:</b> au repos, la lame est levée et la pompe arrêtée. Clique «&nbsp;La carte envoie l'ordre&nbsp;»&nbsp;: la bobine attire la lame, «&nbsp;clac&nbsp;», le courant passe dans le circuit de la pompe. <b>Chaque «&nbsp;clac&nbsp;» use un peu les contacts&nbsp;:</b> un relais s'use au nombre de fois qu'il bascule, pas au nombre d'années. «&nbsp;Faire battre 6 fois&nbsp;» montre ce que fait une pompe qui s'affole.</figcaption>
</figure>
{FIN}'''


def ecrire(chemin, titre, verifier):
    p = os.path.join(DEPOT, chemin)
    s = open(p, encoding="utf-8").read()
    pid = "relais-anime"
    neuf = figure(pid, titre)
    m = re.search(re.escape(DEBUT) + r".*?" + re.escape(FIN), s, re.S)
    if not m:
        print("✘ pas de marque relais-anime :", chemin); return False
    if m.group(0) == neuf:
        print("✓ à jour :", chemin.split("/")[-1]); return True
    if verifier:
        print("✘ pas à jour :", chemin.split("/")[-1]); return False
    s = s[:m.start()] + neuf + s[m.end():]
    open(p, "w", encoding="utf-8").write(s)
    print("écrit :", chemin.split("/")[-1]); return True


if __name__ == "__main__":
    ok = all([ecrire(c, t, "--ecrire" not in sys.argv) for c, t in PAGES.items()])
    sys.exit(0 if ok else 1)
