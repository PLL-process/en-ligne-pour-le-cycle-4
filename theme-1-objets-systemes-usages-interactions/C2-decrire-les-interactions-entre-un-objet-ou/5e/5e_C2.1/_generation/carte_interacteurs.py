"""Engendre `Images/interacteurs_de_la_station.svg` — la carte des interacteurs de la station (activité 1).

    python3 carte_interacteurs.py        (depuis ce dossier)

Version « premium » du 28/10/2026, à la demande de Pascal : l'ancienne carte posait les deux repères (« toujours
extérieur », « interacteur ≠ exigence ») AU MILIEU des familles, sur le trajet des flèches — ils avaient l'air
d'interacteurs, et les cadres se touchaient. Ici :
  · les quatre familles et la station sont séparées (44 px au moins entre deux cadres) ;
  · chaque famille est reliée à la station par UNE flèche à double sens, qui ne touche ni ne traverse aucun cadre ;
  · les deux repères vivent SOUS le schéma, à part, sans flèche ;
  · ce n'est pas encore un diagramme pieuvre, et la figure le dit.
On modifie ce script, puis on le relance : on ne retouche pas le SVG à la main.
"""
import pathlib
import sys
W = 900
CW, CH = 248, 140            # cartes des familles
X_G, X_D = 32, W - 32 - CW   # colonnes
Y_H, Y_B = 108, 292          # rangées (écart vertical 44)
SW, SH = 196, 84             # la station
SX, SY = (W - SW) // 2, (Y_H + CH + Y_B) // 2 - SH // 2
NOTES_Y = Y_B + CH + 46
NOTE_H = 78
BANDE_Y = NOTES_Y + NOTE_H + 18
H = BANDE_Y + 38 + 24

FAMILLES = [
    ("👤 Les usagers", "#c9a2ff", "#1f1638", "#7c5cc4", X_G, Y_H,
     ["le cycliste abonné", "le touriste de passage", "l'agent de maintenance"], "ceux qu'on cite en premier"),
    ("💾 Les données", "#ffd08a", "#2a200c", "#c98a2e", X_D, Y_H,
     ["l'identifiant de l'abonné", "l'état «&#160;disponible&#160;» du vélo", "le paiement, le n° de borne"],
     "celles qu'on oublie toujours"),
    ("📱 Les autres objets", "#9cc2ff", "#0c1f40", "#3f6bb5", X_G, Y_B,
     ["le vélo", "le smartphone", "le serveur de la ville"], "avec qui la station échange"),
    ("🌧️ L'environnement", "#8fe8b0", "#0b2a1b", "#3f9a68", X_D, Y_B,
     ["la pluie, le soleil", "le sel marin, la température", "le trottoir, la circulation"],
     "ce qui agit sans qu'on l'appelle"),
]

o = []
a = o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ti di"\n'
  '     font-family="Segoe UI, system-ui, sans-serif" font-size="14">')
a("""  <title id="ti">Les quatre familles d'interacteurs extérieurs autour de la station de vélos</title>
  <desc id="di">Au centre, la station de vélos, l'objet que l'on étudie. Autour d'elle, bien séparées les unes des
  autres et d'elle, les quatre familles d'interacteurs extérieurs nommées par le programme, présentées comme
  également importantes. Les usagers : le cycliste abonné qui prend et rend un vélo, le touriste de passage,
  l'agent de maintenance qui répare. Les données : l'identifiant de l'abonné, l'état « disponible » d'un vélo, le
  paiement, le numéro de la borne — rien de tout cela ne se voit, et sans elles la station ne débloque aucun vélo.
  Les autres objets : le vélo, le smartphone qui transmet l'identifiant, le serveur de la ville. Les éléments de
  l'environnement : la pluie, le soleil, le sel de l'air marin qui attaque les métaux, la température, le trottoir
  sur lequel la station est fixée, la circulation. Chaque famille est reliée à la station par une flèche à double
  sens : la relation va dans les deux sens. Une ligne, sous le titre, prévient que ce n'est pas encore un diagramme
  pieuvre : c'est la liste des interacteurs, rangée par familles, sans fonction écrite sur les traits. Sous le
  schéma, à part et sans flèche, deux repères. Le premier : un interacteur est toujours extérieur à l'objet ; la
  couleur du cadre n'en est pas un, c'est une caractéristique de l'objet. Le second : un interacteur n'est pas une
  exigence ; une règle de la ville n'échange rien avec la station, elle impose une condition à celui qui la
  conçoit. Une bande de conclusion rappelle que la famille la plus souvent oubliée est celle des données, parce
  qu'elle ne se voit pas.</desc>""")
a(f"""  <defs>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#61dafb" stop-opacity=".22"/>
      <stop offset="1" stop-color="#61dafb" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="voile" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity=".06"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <marker id="fi" markerWidth="10" markerHeight="10" refX="8.5" refY="5" orient="auto-start-reverse"
            markerUnits="userSpaceOnUse" viewBox="0 0 10 10">
      <path d="M0 0 L10 5 L0 10 Z" fill="#61dafb"/></marker>
  </defs>
  <style>
    text{{fill:#e4eaf5}}
    .ti{{font-size:17px;font-weight:600}}
    .lb{{fill:#9bbefc;font-size:12.5px}}
    .pied{{font-size:12.5px;font-style:italic}}
    .fl{{stroke:#61dafb;stroke-width:2;fill:none;stroke-linecap:round;marker-start:url(#fi);marker-end:url(#fi)}}
  </style>
  <rect width="{W}" height="{H}" fill="#050f24"/>
  <text x="32" y="40" font-size="19" font-weight="600">Ce qui entre en relation avec la station</text>
  <text class="lb" x="32" y="63" font-size="13">Quatre familles. Aucune n'est plus «&#160;technique&#160;» que les autres.</text>
  <text x="32" y="86" font-size="13" style="fill:#ffd08a"><tspan font-weight="600">Pas encore un diagramme pieuvre</tspan>&#160;: c'est la liste des interacteurs, rangée par familles — aucune fonction sur les traits.</text>
""")
# halo et station
cx, cy = SX + SW / 2, SY + SH / 2
a(f'  <ellipse cx="{cx}" cy="{cy}" rx="150" ry="96" fill="url(#halo)"/>')
# flèches : de la carte à la station, courbes douces, extrémités à distance des bords (rien ne se touche)
G = 7
for (_t, _c, _f, _s, x, y, _i, _p) in FAMILLES:
    gauche = x < W / 2
    x0 = x + CW + G if gauche else x - G
    y0 = y + CH - 36 if y == Y_H else y + 36      # du bas de la carte du haut, du haut de la carte du bas
    x1 = SX - G if gauche else SX + SW + G
    y1 = SY + 22 if y == Y_H else SY + SH - 22
    mx = (x0 + x1) / 2
    a(f'  <path class="fl" d="M{x0} {y0} C {mx} {y0}, {mx} {y1}, {x1} {y1}"/>')
a(f'  <rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="20" fill="#10284d" stroke="#61dafb" stroke-width="2.5"/>')
a(f'  <rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="20" fill="url(#voile)"/>')
a(f'  <text class="ti" x="{cx}" y="{SY + 37}" text-anchor="middle" style="fill:#61dafb" font-size="19">La station</text>')
a(f'  <text class="lb" x="{cx}" y="{SY + 61}" text-anchor="middle">l\'objet que l\'on étudie</text>')
# cartes
for (titre, ct, fond, bord, x, y, items, pied) in FAMILLES:
    a("")
    a(f'  <rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="16" fill="{fond}" stroke="{bord}" stroke-width="1.8"/>')
    a(f'  <rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="16" fill="url(#voile)"/>')
    a(f'  <text class="ti" x="{x + 20}" y="{y + 34}" style="fill:{ct}">{titre}</text>')
    for k, it in enumerate(items):
        a(f'  <text x="{x + 20}" y="{y + 62 + 23 * k}">· {it}</text>')
    a(f'  <text class="lb pied" x="{x + 20}" y="{y + CH - 13}">{pied}</text>')
# les deux repères, à part
a("")
a(f'  <line x1="32" y1="{NOTES_Y - 22}" x2="{W - 32}" y2="{NOTES_Y - 22}" stroke="#1e3a66" stroke-width="1"/>')
a(f'  <text class="lb" x="32" y="{NOTES_Y - 6}" font-size="12" letter-spacing="1.5">DEUX REPÈRES POUR LIRE LE SCHÉMA</text>')
NW = (W - 64 - 20) / 2
REPERES = [
    ("Toujours EXTÉRIEUR à l'objet", "#ffd08a", "#ffb454",
     ["La couleur du cadre n'en est pas un&#160;:", "c'est une caractéristique de l'objet."]),
    ("Interacteur ≠ exigence", "#ff9aa4", "#ff7b88",
     ["Une règle de la ville n'échange rien avec la station&#160;:", "elle impose une condition à celui qui la conçoit."]),
]
for k, (t, ct, acc, lignes) in enumerate(REPERES):
    x = 32 + k * (NW + 20)
    y = NOTES_Y + 6
    a(f'  <rect x="{x}" y="{y}" width="{NW}" height="{NOTE_H - 6}" rx="12" fill="#0b1a33" stroke="#1e3a66" stroke-width="1"/>')
    a(f'  <rect x="{x}" y="{y + 12}" width="4" height="{NOTE_H - 30}" rx="2" fill="{acc}"/>')
    a(f'  <text x="{x + 20}" y="{y + 24}" font-size="14" font-weight="600" style="fill:{ct}">{t}</text>')
    for j, l in enumerate(lignes):
        a(f'  <text x="{x + 20}" y="{y + 45 + 18 * j}" font-size="13">{l}</text>')
# la bande
a("")
a(f'  <rect x="32" y="{BANDE_Y}" width="{W - 64}" height="38" rx="10" fill="#10284d" stroke="#3f6bb5" stroke-width="1.5"/>')
a(f'  <text x="50" y="{BANDE_Y + 24}" font-size="13"><tspan font-weight="600" style="fill:#ffd08a">La famille qu\'on oublie, c\'est celle des données</tspan> — parce qu\'elle ne se voit pas. Sans l\'identifiant, la borne ne débloque rien.</text>')
a("</svg>")
import re
svg = "\n".join(o) + "\n"
# Une taille posée en attribut perd contre une règle CSS de classe : on la passe en style, fusionné au style existant.
def en_style(m):
    tag = m.group(0)
    t = re.search(r' font-size="([\d.]+)"', tag)
    if not t or tag.startswith("<svg"):
        return tag
    tag = tag.replace(t.group(0), "")
    if ' style="' in tag:
        return tag.replace(' style="', f' style="font-size:{t.group(1)}px;', 1)
    return tag.replace("<text", f'<text style="font-size:{t.group(1)}px"', 1)
svg = re.sub(r"<text[^>]*>", en_style, svg)
sortie = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / "Images" / "interacteurs_de_la_station.svg"
sortie.write_text(svg, encoding="utf-8")
print("écrit :", sortie, f"({W} × {H})")
