#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
poser_roles.py — pose le bloc « qui fait quoi, et quand on échange » là où le travail
                 de groupe est nommé, et seulement là.

    python3 poser_roles.py --etat        dit où le bloc manque, ne touche à rien
    python3 poser_roles.py               pose les blocs manquants
    python3 poser_roles.py --racine X    si l'outil n'est pas à sa place habituelle

Pourquoi cet outil existe
-------------------------
Règle n°166 : un travail de groupe sans rôles nommés laisse toujours le même élève tenir
le clavier — et c'est celui qui en avait le moins besoin qui apprend à s'en servir. Le
dépôt nommait le travail de groupe dans sept séquences du Thème 1 et ne nommait de rôle
dans AUCUNE (vérifié : zéro occurrence de « rapporteur », « porte-parole », « gardien du
temps » dans tout le Thème 1).

Deux décisions de conception
----------------------------
1. **Le bloc ne se pose que là où le groupe est nommé.** Ajouter des rôles à une séquence
   qui se fait seul serait du bruit — et un dispositif qui ne sert à rien apprend à ne
   plus lire les dispositifs.
2. **Deux rôles, pas quatre.** Le dépôt dit « à deux » bien plus souvent que « en
   groupe ». Quatre rôles pour deux élèves, c'est une consigne qu'on n'applique pas. Les
   deux autres sont dans un repli, pour les groupes de trois ou quatre.

Et l'échange se fait **à la moitié de la séance**, pas d'une séance à l'autre : le tort
qu'on veut corriger se produit en une heure.
"""

import argparse
import html
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[1]

#: le travail de groupe, tel que le dépôt le nomme réellement
GROUPE = re.compile(r"en group|par group|ton groupe|votre groupe|le groupe|binôme|binome"
                    r"|en équipe|à deux|par deux|chacun son tour", re.I)

CSS = """<style id="roles-css">
/* Bloc « rôles » — posé par poser_roles.py. Ne pas éditer à la main. */
.roles{background:#0a1b3d;border:1px solid #274a8a;border-left:4px solid #81fba1;
  border-radius:12px;padding:14px 18px;margin:16px 0}
.roles-etiq{font-size:.72em;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  color:#81fba1;margin:0 0 6px}
.roles-intro{margin:0 0 10px;color:#e4eaf5}
.roles ul{margin:0 0 10px;padding-left:20px}
.roles li{margin-bottom:5px}
.roles details{margin:0 0 10px}
.roles summary{cursor:pointer;color:#9bbefc;font-size:.92em}
.roles table{border-collapse:collapse;width:100%;max-width:520px;font-size:.9em;margin:6px 0 10px}
.roles th,.roles td{border:1px solid #2f5695;padding:7px 10px;text-align:left}
.roles th{background:#0b1b39;color:#9bbefc;font-weight:600}
.roles td.vide{height:2.1em;background:#050f24}
.roles-note{margin:0;font-size:.9em;color:#ffd66b}
@media print{
  .roles{background:#fff;border:1px solid #666;border-left:4px solid #111;color:#111;
    break-inside:avoid}
  .roles-etiq{color:#111}.roles-intro{color:#111}
  .roles summary{color:#333}
  .roles details{display:block}.roles details>*{display:block}
  .roles th{background:#eee;color:#111}.roles th,.roles td{border-color:#999}
  .roles td.vide{background:#fff}
  .roles-note{color:#111;font-style:italic}
}
</style>
"""

BLOC = """<!-- roles: {cle} -->
<section class="roles" id="roles-{cle}" aria-label="Répartition des rôles dans le groupe">
  <p class="roles-etiq">👥 Qui fait quoi — et quand on échange</p>
  <p class="roles-intro">Deux rôles seulement, et <strong>on échange à la moitié du
  temps</strong>. Un rôle est un tour, pas une étiquette.</p>
  <ul>
    <li><b>Le pilote</b> tient l'outil — le clavier, le capteur, le tableur. Il exécute&nbsp;;
      il ne décide pas seul.</li>
    <li><b>Le vérificateur</b> relit chaque nombre et chaque unité avant qu'on les écrive.
      <em>Il a le droit d'arrêter le groupe.</em></li>
  </ul>
  <details>
    <summary>Si vous êtes trois ou quatre</summary>
    <ul>
      <li><b>Le scribe</b> écrit la trace commune — et note aussi ce que vous n'avez pas su faire.</li>
      <li><b>Le porte-parole</b> explique à la classe. Il ne parle qu'avec ce que le scribe a écrit&nbsp;:
        si la trace ne suffit pas, c'est la trace qu'il faut reprendre.</li>
    </ul>
  </details>
  <table>
    <thead><tr><th>Rôle</th><th>1<sup>re</sup> moitié</th><th>2<sup>e</sup> moitié</th></tr></thead>
    <tbody>
      <tr><th>Pilote</th><td class="vide"></td><td class="vide"></td></tr>
      <tr><th>Vérificateur</th><td class="vide"></td><td class="vide"></td></tr>
    </tbody>
  </table>
  <p class="roles-note">À recopier à chaque séance. Si personne ne change de rôle, c'est
  toujours le même qui apprend à tenir le clavier — et ce n'est pas celui qui en avait le
  plus besoin.</p>
</section>
<!-- /roles: {cle} -->"""


def cle_du_lot(chemin):
    m = re.search(r"/(\d[e]_C\d\.\d)/", str(chemin).replace("\\", "/"))
    return (m.group(1) if m else chemin.parent.name).replace(".", "-")


def sans_script(texte):
    return re.sub(r"<script.*?</script>", " ", texte, flags=re.S)


def premier_groupe(texte):
    """Position de la première mention réelle de travail de groupe (hors script)."""
    m = GROUPE.search(html.unescape(sans_script(texte)))
    if not m:
        return None
    # on retrouve la position dans le texte d'origine par une seconde recherche
    m2 = GROUPE.search(sans_script(texte))
    return m2.start() if m2 else None


def point_d_insertion(texte, ou):
    """Après le titre de la section qui contient la première mention de groupe.

    On remonte au dernier <h2> ou <h3> ouvert avant la mention : le bloc doit se lire
    AVANT que l'élève ne commence l'activité, pas après.
    """
    titres = list(re.finditer(r"<h[23][^>]*>.*?</h[23]>", texte[:ou], re.S))
    if titres:
        return titres[-1].end()
    corps = re.search(r"<body[^>]*>", texte)
    return corps.end() if corps else 0


def poser(page, forcer=False):
    texte = page.read_text(encoding="utf-8")
    cle = cle_du_lot(page)
    ouvre, ferme = "<!-- roles: %s -->" % cle, "<!-- /roles: %s -->" % cle
    bloc = BLOC.format(cle=cle)

    if ouvre in texte and ferme in texte:
        d, f = texte.index(ouvre), texte.index(ferme) + len(ferme)
        neuf = texte[:d] + bloc + texte[f:]
        if neuf == texte:
            return False, "déjà à jour"
        texte = neuf
    else:
        ou = premier_groupe(texte)
        if ou is None and not forcer:
            return None, "aucun travail de groupe nommé — rien à poser"
        i = point_d_insertion(texte, ou if ou is not None else len(texte))
        texte = texte[:i] + "\n" + bloc + texte[i:]

    if 'id="roles-css"' not in texte:
        texte = texte.replace("</head>", CSS + "</head>", 1)
    page.write_text(texte, encoding="utf-8")
    return True, "posé"


def sequences(racine, theme):
    base = racine / theme
    return [s for s in sorted(base.rglob("sequence*.html")) if "_archive" not in str(s)]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--etat", action="store_true", help="ne touche à rien")
    ap.add_argument("--racine", default=None)
    ap.add_argument("--theme", default="theme-1-objets-systemes-usages-interactions")
    a = ap.parse_args()
    racine = pathlib.Path(a.racine).resolve() if a.racine else RACINE

    avec, sans, deja = [], [], []
    for s in sequences(racine, a.theme):
        t = s.read_text(encoding="utf-8")
        cle = cle_du_lot(s)
        if "<!-- roles: %s -->" % cle in t:
            deja.append(s)
        elif premier_groupe(t) is not None:
            avec.append(s)
        else:
            sans.append(s)

    print("\n%s — %d séquence(s)\n" % (a.theme.split("-")[0].capitalize() + " "
          + a.theme.split("-")[1], len(avec) + len(sans) + len(deja)))
    print("  travail de groupe nommé, bloc à poser : %d" % len(avec))
    print("  bloc déjà en place                    : %d" % len(deja))
    print("  aucun travail de groupe nommé         : %d  (on ne pose rien : un dispositif"
          " inutile\n%s apprend à ne plus lire les dispositifs)\n" % (len(sans), " " * 42))

    for s in avec:
        if a.etat:
            print("  ⏳ %s" % cle_du_lot(s))
            continue
        ok, mot = poser(s)
        print("  %s %-10s %s" % ("✅" if ok else "⚠️ ", cle_du_lot(s), mot))
    for s in deja:
        print("  ✔️  %-10s déjà posé" % cle_du_lot(s))
    return 0


if __name__ == "__main__":
    sys.exit(main())
