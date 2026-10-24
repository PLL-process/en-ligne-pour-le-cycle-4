# -*- coding: utf-8 -*-
"""controle_regles_visibles.py — l'élève lit le savoir, pas la fabrique (règle d'or n°309).

LE CONSTAT
----------
Une page, un SVG ou un QCM lu par un élève laissait voir la démarche qui l'avait fabriqué : « (règle n°8 : le bon
outil pour la bonne question) » sous un plan de métro, « convention du dépôt » dans la légende d'un schéma, « v1 Grok
— v2 mise en conformité règles 11/13/14 (Fable, 01/08/2026) » dans un pied de page, « recopié, pas reformulé » dans le
titre de vingt et une séquences, « les archives du dépôt » dans une phrase de cours. Mesuré le 21/10/2026 sur `main` à
`2d250ee1` : 56 numéros de règle visibles dans 18 fichiers, et une centaine d'autres traces. Un élève de 5e ne sait pas
ce qu'est « la règle n°18 », ni « le dépôt » ; la phrase le renvoie vers un document qu'il n'ouvrira jamais, et lui dit
au passage que cette page est un produit, pas un savoir.

LA RÈGLE
--------
Dans toute page, tout SVG ou tout QCM lu par un élève : aucune trace de la démarche de conception — ni numéro de règle,
ni « convention du dépôt », ni « décision de Pascal », ni nom d'agent, de lot ou de vague. Une explication utile à
l'élève se dit en mots d'élève, sans renvoi. Permis : les commentaires HTML, CSS et JavaScript, le journal, les fiches
pédagogiques, les synthèses professeur.

CE QU'IL LIT
------------
Dans chaque .html et .svg du dépôt (les fichiers suivis par Git ; à défaut, tout l'arbre), hors `_archive-anciennes-versions`,
`_outils`, `_generation`, `captures`, hors synthèses professeur, fiches (pédagogiques, de maths pour les collègues) et rapports de tests :
le texte que l'élève peut lire ou entendre — corps, attributs (`title`, `alt`, `aria-label`, `<desc>`), chaînes de
JavaScript qui s'affichent (banques de QCM) — SANS les commentaires HTML, CSS et JavaScript, ni le contenu des <style>.

CE QU'IL REFUSE (le texte vu, et la ligne)
  · un numéro de règle : « règle n°12 », « règle d'or n°18 », « règles n°72 à n°82 », « (règle 18) », « CRCN règle 7 » ;
  · « du dépôt », « ce dépôt » — le dépôt est l'atelier, pas le cours ;
  · un nom d'agent ou d'outil de fabrication : Fable, Grok ; « décision de Pascal » ; « journal des décisions » ;
    « garde-périmètre » ;
  · un lot ou une vague : « lot 3e_C9.2 », « LOT 04 », « vague 2 », « Lot Shanghai » ;
  · « recopié, pas reformulé » ; « mise en conformité règles … ».
Ce qu'il laisse : « Règle d'or du schéma », « la règle du jeu », « règle de trois » — des règles de métier enseignées à
l'élève, qui n'ont pas de numéro de fabrique.

EXEMPTIONS NOMMÉES (EXEMPTES) : une phrase exacte, dans un fichier nommé, avec la raison. Au 21/10/2026 :
  · `memoire_boites_etiquetees.svg` : « Règle n°1 / 2 / 3 » sont les trois règles de la mémoire de l'ordinateur — du
    cours, pas de la fabrique ;
  · `activite-bonus-cyber-immersive-2fa.html` : « ChatGPT » y est un objet d'étude, cité par son nom.
FICHIERS EXEMPTÉS (MODELES) : `tp_modele_demonstration.html` est le modèle de scénario destiné aux auteurs de TP ; aucun
élève ne l'ouvre (il n'est ni dans l'index ni dans une séquence).

NON LU : une trace dite sans mot-clé (« comme on l'a décidé avec l'inspection »), une image dont le texte est dans les
pixels (une capture), et le sens d'une phrase : le contrôle cherche des marques, il ne juge pas si une explication est
claire. La relecture reste humaine.

Usage :
    python3 _outils/controle_regles_visibles.py           # rapport complet
    python3 _outils/controle_regles_visibles.py --muet    # seulement les refus
Sortie : 0 si aucune trace n'est visible, 1 sinon, 2 si rien n'a pu être lu (règle d'or n°299).
"""
import os
import re
import subprocess
import sys

import panne

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "_generation", "captures",
           "__pycache__", ".playwright-mcp"}
#: pages que l'élève n'ouvre pas : le nom suffit (début du nom de fichier, jamais « contient »).
PROFESSEUR = re.compile(r"^(synthese_professeur|fiche_|rapport_tests)", re.I)
#: fichiers dont aucun élève n'est lecteur, nommés un à un, avec la raison.
MODELES = {
    "tp_modele_demonstration.html": "modèle de scénario pour les auteurs de TP : ni dans l'index, ni dans une séquence",
}
#: phrases exactes tolérées dans un fichier nommé : (fin du chemin, phrase) -> raison.
EXEMPTES = {
    ("memoire_boites_etiquetees.svg", "Règle n°1"): "règle de la mémoire de l'ordinateur : du cours",
    ("memoire_boites_etiquetees.svg", "Règle n°2"): "règle de la mémoire de l'ordinateur : du cours",
    ("memoire_boites_etiquetees.svg", "Règle n°3"): "règle de la mémoire de l'ordinateur : du cours",
}
#: (nom du grief, motif)
MOTIFS = [
    ("un numéro de règle", re.compile(r"\br[èe]gles?\s+(?:d['’]or\s+)?n\s?°\s?\d"
                                      r"|(?:\(\s*|\bCRCN\s+|\bcompl[ée]t[ée]e?\s+)r[èe]gles?\s+\d", re.I)),
    ("« du dépôt » / « ce dépôt »", re.compile(r"\b(?:du|de ce|ce|dans ce|à ce)\s+dépôt\b|\bdépôt\s+en-ligne-pour-le-cycle-4", re.I)),
    ("un nom d'agent de fabrication", re.compile(r"\b(?:Fable|Grok)\b")),
    ("« décision de Pascal »", re.compile(r"\bd[ée]cisions?\s+de\s+Pascal\b", re.I)),
    ("le journal ou la garde du dépôt", re.compile(r"journal\s+des\s+d[ée]cisions|garde-p[ée]rim[èe]tre", re.I)),
    ("un lot ou une vague", re.compile(r"\blot\s+(?:\d|[345]e_C)|\bLOT\s*\d|\bvague\s+\d")),
    ("un lot nommé (« Lot Shanghai »)", re.compile(r"\bLot\s+[A-ZÉ]")),
    ("« recopié, pas reformulé »", re.compile(r"recopi[ée],?\s+pas\s+reformul", re.I)),
    ("« mise en conformité règles … »", re.compile(r"mise\s+en\s+conformit[ée]\s+r[èe]gles?", re.I)),
]
EXTENSIONS = (".html", ".svg")


def masque(t):
    """Le texte, à longueur égale, sans ce que l'élève ne lit pas : commentaires HTML, <style>, commentaires CSS/JS."""
    sortie = list(t)

    def effacer(a, b):
        for i in range(a, b):
            if sortie[i] not in "\r\n":
                sortie[i] = " "
    for m in re.finditer(r"<!--.*?-->", t, re.S):
        effacer(*m.span())
    for m in re.finditer(r"<style\b.*?</style>", t, re.S | re.I):
        effacer(*m.span())
    for m in re.finditer(r"<script\b.*?</script>", t, re.S | re.I):
        a, b = m.span()
        s = t[a:b]
        for c in re.finditer(r"/\*.*?\*/", s, re.S):
            effacer(a + c.start(), a + c.end())
        for c in re.finditer(r"(?m)(?:^|(?<=[\s;{}]))//[^\n\r]*", s):
            effacer(a + c.start(), a + c.end())
    return "".join(sortie)


def fichiers(racine):
    """Les fichiers suivis par Git ; à défaut (arbre sans dépôt), tout l'arbre."""
    try:
        r = subprocess.run(["git", "-C", racine, "ls-files", "-z"], capture_output=True, timeout=60)
        suivis = [x for x in r.stdout.decode("utf-8", "replace").split("\0") if x] if r.returncode == 0 else []
    except (OSError, subprocess.SubprocessError):
        suivis = []
    if suivis:
        for rel in suivis:
            if rel.lower().endswith(EXTENSIONS) and not (set(rel.split("/")[:-1]) & ECARTES):
                yield os.path.join(racine, rel)
        return
    for dossier, sous, noms in os.walk(racine):
        sous[:] = [d for d in sous if d not in ECARTES]
        for nom in noms:
            if nom.lower().endswith(EXTENSIONS):
                yield os.path.join(dossier, nom)


def griefs(rel, texte):
    """[(ligne, grief, extrait)] — vide si la page ne laisse voir aucune trace de fabrique."""
    visible = masque(texte)
    trouves = []
    for nom, motif in MOTIFS:
        for m in motif.finditer(visible):
            if any(rel.endswith(fin) and m.group(0).startswith(phrase) for (fin, phrase) in EXEMPTES):
                continue
            ligne = visible.count("\n", 0, m.start()) + 1
            a, b = max(0, m.start() - 50), min(len(visible), m.end() + 50)
            extrait = re.sub(r"\s+", " ", visible[a:b]).strip()
            trouves.append((ligne, nom, extrait))
    return sorted(set(trouves))


def main(muet=False):
    lus, refuses, griefs_total = 0, [], 0
    for chemin in fichiers(DEPOT):
        nom = os.path.basename(chemin)
        rel = os.path.relpath(chemin, DEPOT).replace(os.sep, "/")
        if PROFESSEUR.match(nom) or nom in MODELES:
            continue
        try:
            texte = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        lus += 1
        g = griefs(rel, texte)
        if g:
            refuses.append((rel, g))
            griefs_total += len(g)
    if not lus:
        return panne.rien_vu("aucun .html ni .svg lisible sous %s" % DEPOT)
    if not muet:
        print("%d page(s) et SVG lus · %d trace(s) de fabrique visible(s) · %d fichier(s) en refus"
              % (lus, griefs_total, len(refuses)))
        print("     NON LU : une trace dite sans mot-clé, le texte porté par les pixels d'une capture, et la clarté\n"
              "     d'une explication : le contrôle cherche des marques, il ne juge pas le sens.")
        print("     EXEMPTÉS : %s." % "; ".join("%s (%s)" % (n, r) for n, r in MODELES.items()))
    if refuses:
        print("\n⛔ l'élève lit la fabrique dans %d fichier(s) (règle d'or n°309 : l'élève lit le savoir, pas la fabrique) :"
              % len(refuses))
        for rel, g in refuses:
            print("  %s" % rel)
            for ligne, nom, extrait in g:
                print("     ligne %d · %s : … %s …" % (ligne, nom, extrait))
        print("\n     Dis-le en mots d'élève, sans renvoi — ou retire la phrase. Le numéro de règle va au journal.")
        return 1
    print("\n✅ aucune page lue par un élève ne laisse voir la fabrique (règle d'or n°309)")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
