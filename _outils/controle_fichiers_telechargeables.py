# -*- coding: utf-8 -*-
"""controle_fichiers_telechargeables.py — un fichier nommé est un fichier qu'on peut prendre.

LA RÈGLE
--------
Pascal, le 07/09/2026 : « Lors d'une séquence, si un élève a besoin d'un fichier nommé
par exemple Fichier HF.csv, qu'il ait la possibilité de cliquer sur le lien afin de
télécharger ce fichier. Il serait souhaitable de vérifier, pour tous les fichiers
existants et toutes les séquences existantes, et d'établir une règle d'or. »

Règle d'or n°289 : **un fichier nommé dans une page est un fichier qu'on peut
prendre** — chaque mention porte un lien `<a href download>` vers lui, et le fichier
existe dans le lot. Un nom de fichier écrit en toutes lettres, sans lien, oblige
l'élève à le chercher ; un élève de cycle 4 ne le cherche pas, il lève la main.

CE QU'IL MESURE
---------------
Dans chaque séquence, TP et atelier, il lit le texte visible (hors `<script>` et
`<style>`) et y relève les noms de fichiers de DONNÉES — ce qu'un élève ouvre dans
un tableur, un éditeur, Onshape ou l'IDE Arduino : csv, txt, py, ino, stl, step,
3mf, gcode, dxf, sb3, json, xlsx, ods, zip, hex, uf2, pdf, scad, obj. Les pages
HTML sont des liens, pas des fichiers à prendre ; les images s'affichent, elles ne
se téléchargent pas : ni les unes ni les autres ne sont regardées.

Pour chaque nom relevé, trois cas :

  · le fichier EXISTE dans le lot et CHAQUE mention est enveloppée d'un lien
    `<a href="…" download>` qui pointe vers lui → conforme ;
  · le fichier EXISTE dans le lot et une mention au moins n'a pas ce lien → REFUSÉ ;
  · le fichier N'EXISTE PAS dans le lot. Si la phrase le PROMET (« fourni », « ouvre
    le fichier », « télécharge », « importe ») → REFUSÉ : une promesse sans fichier
    est pire qu'un nom sans lien. Sinon — `truc.csv`, `finalV2 (copie).csv`, les
    noms d'un dossier en désordre que la séquence de 5e_C1.1 donne en EXEMPLE — le
    nom est du récit, pas un fichier : COMPTÉ, jamais refusé.

Un lien `<a href>` SANS `download` est refusé aussi : pour un `.csv`, un `.py` ou un
`.ino`, enregistrer ou afficher dépend alors du navigateur et du serveur — et un
élève devant une page de chiffres bruts ne sait pas quoi en faire. `download` rend
le geste le même partout : un clic, un fichier.

CE QU'IL NE FAIT PAS
--------------------
Il ne juge pas le CONTENU du fichier, ni que la séquence en ait besoin. Il ne voit
pas un fichier désigné sans son nom (« le tableau de relevés ») — celui-là est du
ressort de la relecture. Et il ne lit que le texte visible : un nom dans un `alt`
ou un `title` n'est pas une mention.

Usage :
    python3 _outils/controle_fichiers_telechargeables.py           # rapport complet
    python3 _outils/controle_fichiers_telechargeables.py --muet    # seulement les refus
Sortie : 0 si chaque fichier nommé se prend d'un clic, 1 sinon.
"""

import glob
import html
import os
import re
import sys
from urllib.parse import unquote

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

#: ce qu'un élève ouvre ailleurs que dans le navigateur
EXTENSIONS = ("csv", "txt", "py", "ino", "stl", "step", "stp", "3mf", "gcode", "dxf",
              "sb3", "json", "xlsx", "ods", "zip", "hex", "uf2", "pdf", "scad", "obj")
NOM = re.compile(r"(?<![\w/.\-])([\w\-\.]{2,}\.(?:%s))(?![\w/])" % "|".join(EXTENSIONS), re.I)
#: les verbes qui promettent un fichier — dans les 70 caractères autour du nom
PROMESSE = re.compile(r"fourni|t[ée]l[ée]charg|ouvre|ouvrir|importe|charge[rz]?\b|"
                      r"enregistr|r[ée]cup[èe]r", re.I)
LIEN = re.compile(r"<a\b([^>]*)>(.*?)</a>", re.I | re.S)
HREF = re.compile(r'href="([^"#]+)"', re.I)

#: les pages écartées, chacune avec sa raison. Cette liste ne doit que RÉTRÉCIR
#: (règle d'or n°273).
TOLEREES = {
    # Vide au 08/09/2026, et c'est un fait mesuré : `de_50.step`, seule promesse sans
    # fichier du dépôt, a été engendré et livré le même jour (PR « de_50.step existe »).
}


def pages(racine):
    motifs = ("**/sequence*.html", "**/tp_*.html", "**/atelier_*.html")
    vus = set()
    for m in motifs:
        for f in glob.glob(os.path.join(racine, m), recursive=True):
            if any(e in f for e in ECARTES):
                continue
            vus.add(f)
    return sorted(vus)


def _visible(texte):
    corps = texte.split("<body", 1)[-1]
    return re.sub(r"<(script|style)\b.*?</\1>", "", corps, flags=re.S | re.I)


def _texte_nu(fragment):
    return html.unescape(re.sub(r"<[^>]+>", " ", fragment))


def juger(chemin):
    """(refus, comptes) — `refus` est une liste de phrases, `comptes` un dict."""
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    dossier = os.path.dirname(chemin)
    vis = _visible(texte)
    comptes = {"mentions": 0, "recit": 0}
    refus = []

    # 1. ce que chaque lien couvre : les noms de fichiers dont le texte du lien porte
    #    la mention, avec la cible et la présence de `download`
    couverts = []          # (début, fin, cible, download)
    for m in LIEN.finditer(vis):
        h = HREF.search(m.group(1))
        cible = unquote(h.group(1)) if h else ""
        couverts.append((m.start(), m.end(), cible, "download" in m.group(1).lower()))

    # 2. chaque nom du texte visible, hors balises
    positions = []  # (nom, début dans vis)
    for m in NOM.finditer(vis):
        # à l'intérieur d'une balise (href, src, alt…) : ce n'est pas une mention
        ouvert = vis.rfind("<", 0, m.start())
        ferme = vis.rfind(">", 0, m.start())
        if ouvert > ferme:
            continue
        positions.append((m.group(1), m.start(), m.end()))

    vus = set()
    for nom, deb, fin in positions:
        comptes["mentions"] += 1
        existants = glob.glob(os.path.join(dossier, "**", nom), recursive=True)
        existants = [e for e in existants if not any(x in e for x in ECARTES)]
        lien = next((c for c in couverts if c[0] <= deb and fin <= c[1]), None)
        cle = (nom, lien is not None, lien[3] if lien else None)
        if not existants:
            autour = _texte_nu(vis[max(0, deb - 70):fin + 70])
            if PROMESSE.search(autour):
                if ("promesse", nom) not in vus:
                    vus.add(("promesse", nom))
                    refus.append("« %s » est promis (« %s ») et n'existe pas dans le lot"
                                 % (nom, re.sub(r"\s+", " ", autour.strip())[:80]))
            else:
                comptes["recit"] += 1
            continue
        if lien is None:
            if ("sans lien", nom) not in vus:
                vus.add(("sans lien", nom))
                refus.append("« %s » existe (%s) et une mention au moins n'a pas de lien"
                             % (nom, os.path.relpath(existants[0], dossier)))
            continue
        cible_abs = os.path.normpath(os.path.join(dossier, lien[2]))
        if os.path.basename(cible_abs).lower() != nom.lower() or not os.path.exists(cible_abs):
            if ("cible", nom) not in vus:
                vus.add(("cible", nom))
                refus.append("« %s » : le lien qui l'enveloppe pointe ailleurs (%s)" % (nom, lien[2]))
            continue
        if not lien[3]:
            if ("download", nom) not in vus:
                vus.add(("download", nom))
                refus.append("« %s » : lien sans `download` — sans lui, enregistrer ou afficher "
                             "dépend du navigateur" % nom)
    return refus, comptes


def main(muet=False):
    conformes, ecarts, tolerees_vues = 0, [], []
    mentions = recit = 0
    for f in pages(DEPOT):
        refus, comptes = juger(f)
        rel = os.path.relpath(f, DEPOT).replace(os.sep, "/")
        mentions += comptes["mentions"]
        recit += comptes["recit"]
        if not refus:
            conformes += 1
        elif rel in TOLEREES:
            tolerees_vues.append(rel)
        else:
            ecarts.append((rel, refus))
    fantomes = [t for t in TOLEREES if t not in tolerees_vues]
    if not muet:
        print("%d page(s) lues · %d nom(s) de fichier dans le texte visible · %d page(s) "
              "en écart · %d tolérée(s)" % (conformes + len(ecarts) + len(tolerees_vues),
                                            mentions, len(ecarts), len(tolerees_vues)))
        print("     %d nom(s) de fichier qui sont du récit (n'existent pas, ne sont pas promis) :"
              "\n     comptés, jamais refusés — « truc.csv » dans un dossier en désordre est un "
              "exemple,\n     pas un fichier." % recit)
        for t in tolerees_vues:
            print("     tolérée : %s\n        %s" % (t, TOLEREES[t]))
        print("     NON LU : le contenu des fichiers, et les fichiers désignés sans leur nom\n"
              "     (« le tableau de relevés ») — ceux-là relèvent de la relecture.")
    if fantomes:
        print("\n⚠ %d page(s) tolérée(s) sont désormais conformes — leur ligne peut sortir de "
              "TOLEREES :" % len(fantomes))
        for t in fantomes:
            print("  " + t)
    if ecarts:
        print("\n⛔ %d page(s) nomment un fichier que l'élève ne peut pas prendre d'un clic "
              "(règle n°289) :" % len(ecarts))
        for rel, refus in ecarts:
            print("  %s" % rel)
            for r in refus:
                print("     · %s" % r)
        return 1
    print("\n✅ chaque fichier nommé dans une séquence se prend d'un clic")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
