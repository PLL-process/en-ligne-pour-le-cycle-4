# -*- coding: utf-8 -*-
"""controle_formulations.py — « le programme dit » doit dire ce que le programme dit.

Nos séquences ouvrent par un encadré qui promet : **« Ce que dit le programme —
recopié, pas reformulé »**. Nos fiches titrent « Formulation du référentiel
(2024) ». Nos README de pointeurs citent le libellé officiel en exergue. Trois
promesses, faites à un collègue qui ne lira pas le Bulletin officiel derrière
nous.

Elles ont été tenues de mémoire, et la mémoire a fauté quatre fois en deux jours :

  · `5e_C3.1` portait, dans une séquence, la formulation de la **4e** ;
  · `3e_C3.4` en portait une reformulation ;
  · la fiche de l'atelier CAO donnait pour `C7.2` et `C7.6` deux phrases
    **absentes du programme**, et identiques aux trois niveaux — ce qui effaçait
    la différenciation que ces codes portent (fabriquer → proposer et fabriquer
    → proposer un ensemble).

Aucune de ces quatre erreurs n'était visible : une formulation fausse ressemble
beaucoup à une formulation juste. Il faut comparer, caractère par caractère, à
`data_competences.py` — seule autorité du dépôt sur le référentiel.

Règle d'or n°245 : une formulation « recopiée » se recopie depuis le référentiel.
Règle d'or n°247 : une formulation identique à tous les niveaux doit éveiller
le soupçon.

Ce que l'outil sait lire
------------------------
Il ne devine pas : il reconnaît les **conventions d'écriture du dépôt**, celles
où un code et sa formulation se suivent — quatre, listées dans `FORMES`,
et signalées à chaque exécution.
Tout le reste lui échappe, et il le dit : un outil qui prétendrait tout voir
mentirait à son tour (règle d'or n°242).

Ce qu'il signale, et ce qu'il ne signale pas
--------------------------------------------
Une phrase courte à côté d'un code est un **titre**, pas une citation : on ne la
compare pas. Une phrase longue qui ressemble à la formulation officielle sans
lui être identique est le cas dangereux — c'est celui qu'on signale :

    AUTRE CODE  c'est une formulation officielle — celle d'un AUTRE code. La
                plus difficile à voir : chaque mot en est juste.
    ÉTRANGÈRE   elle ne ressemble à AUCUNE formulation du référentiel, alors
                qu'elle est écrite là où une citation est promise
    FAUSSE      elle ressemble à la formulation officielle et en diffère
    TRONQUÉE    elle en est un début exact, et s'arrête avant la fin

Usage :
    python3 _outils/controle_formulations.py            # rapport complet
    python3 _outils/controle_formulations.py --muet     # seulement les écarts
Sortie : 0 si aucune formulation fausse, 1 sinon.
"""

import difflib
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_competences import COMP_BY_LEVEL  # noqa: E402

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

#: dossiers dont le contenu ne fait plus foi
IGNORES = ("_archive-anciennes-versions", "archive", "anciennes-versions",
           ".git", "_outils")

#: En deçà, on ne compare rien : le texte est trop court pour être une citation.
#: Le seuil doit rester SOUS la plus courte formulation du référentiel —
#: « Modéliser une forme voulue. » fait 26 caractères, et une version antérieure
#: de cet outil la laissait passer, fût-elle rangée sous le mauvais code.
LONGUEUR_MINIMALE = 20

#: En deçà, on ne DÉNONCE pas : un texte court qui ne ressemble à rien
#: d'officiel est un titre de colonne, pas une citation inventée. On sait
#: reconnaître une phrase officielle courte ; on ne se permet pas d'accuser une
#: phrase courte inconnue.
LONGUEUR_ACCUSATION = 30

#: au-delà, deux phrases se ressemblent assez pour que l'une prétende être l'autre
RESSEMBLANCE = 0.55


def officielles():
    """{(niveau, code): formulation} — le référentiel, seule autorité."""
    out = {}
    for niveau, comp in COMP_BY_LEVEL.items():
        for sous in comp.values():
            for code, texte, _dom in sous:
                out[(niveau, code)] = texte
    return out


OFFICIELLES = officielles()


def normaliser(t):
    """Deux écritures d'une même phrase doivent se comparer égales.

    Les apostrophes typographiques, les entités HTML, les retours à la ligne du
    gabarit et le point final ne sont pas du texte : ce sont des accidents de
    mise en page. Le reste compte, y compris les majuscules.
    """
    t = html.unescape(t)
    t = t.replace("’", "'").replace("‘", "'").replace(" ", " ")
    t = re.sub(r"<[^>]+>", " ", t)
    # un exergue Markdown se plie sur plusieurs lignes « > » : c'est la MÊME
    # phrase. Un contrôle qui dépend de l'endroit où la ligne est pliée ne
    # contrôle pas le contenu.
    t = re.sub(r"(?m)^\s*>\s?", " ", t)
    # Le gras et l'italique de Markdown mettent en valeur une citation, ils ne
    # la modifient pas : « **Réaliser et mettre au point** un programme… » cite
    # exactement le programme. Les compter comme un écart serait reprocher une
    # mise en forme.
    t = re.sub(r"[*`]{1,3}", "", t)   # pas le souligné : il vit dans « 5e_C9.1 »
    t = re.sub(r"\s+", " ", t).strip()
    # Convention du dépôt : l'exergue d'un README fait suivre la citation d'un
    # rappel « Programme 2024 · cycle 4 · thème N · socle … ». Ce rappel n'est
    # pas la citation. Certains README l'écrivent sans ligne « > » de
    # séparation, et le lire comme la suite de la phrase faisait crier à
    # l'erreur cinq fois de suite — sur cinq citations parfaitement exactes.
    t = re.split(r"\s*Programme\s+20\d\d\s*·", t)[0]
    return t.rstrip(" .")


#: (nom de la forme, motif) — le groupe `niv`, `code` et `texte` sont exigés.
#: Chaque forme est une convention réelle du dépôt, pas une devinette.
FORMES = [
    ("ligne de tableau HTML",
     # `<(?!/?td)` : les balises intérieures autorisées sont celles de mise en
     # forme (<b>, <i>, <code>…), jamais une fin ou un début de cellule. Sans
     # cette précaution le motif franchissait les cellules et appariait un code
     # avec le texte d'une ligne située bien plus bas — c'est ainsi que
     # « 7,4 Wh/jour » a été pris pour une citation du programme.
     re.compile(r"<td[^>]*>\s*(?P<niv>5e|4e|3e)_(?P<code>C\d\.\d)\b[^<]*"
                r"(?:<(?!/?td)[^>]*>[^<]*)*</td>\s*<td[^>]*>"
                r"(?P<texte>[^<]{10,400})</td>", re.S)),
    ("sous-titre de page d'orientation",
     re.compile(r'<p class="sous">\s*(?:5e|4e|3e)\s*·\s*(?P<niv>5e|4e|3e)_'
                r"(?P<code>C\d\.\d)\s*[—-]\s*(?P<texte>[^<]{10,400})</p>")),
    ("ligne de tableau Markdown",
     re.compile(r"^\|[^|\n]*\*{0,2}(?P<niv>5e|4e|3e)_(?P<code>C\d\.\d)\*{0,2}[^|\n]*\|"
                r"\s*(?P<texte>[^|\n]{10,400}?)\s*\|", re.M)),
    # Un TITRE de README n'est pas une citation : « # 3e_C9.1 — Atelier
    # "Variables, types et systèmes" » est un nom de lot, et le comparer au
    # programme ne produirait que du bruit. C'est l'EXERGUE qui promet la
    # formulation officielle, et lui seul est lu.
    # L'exergue s'arrête à la ligne « > » seule : ce qui suit est un second
    # paragraphe (le rappel du socle), pas la suite de la citation.
    ("exergue de README",
     re.compile(r"^#\s+(?P<niv>5e|4e|3e)_(?P<code>C\d\.\d)[^\n]*\n+"
                r"(?P<texte>>[ \t]*\S[^\n]{9,400}(?:\n>[ \t]*\S[^\n]*)*)", re.M)),
]

LISIBLES = (".html", ".md")

#: Fichiers qu'un collègue ou un élève lit COMME RÉFÉRENCE. Un journal, un
#: rapport de migration ou un plan de travail citent les formulations en les
#: abrégeant sciemment : les leur reprocher serait du bruit.
REFERENCE = re.compile(r"^(sequence|fiche_pedagogique|README|synthese|lexique|qcm|tp)",
                       re.I)

#: Une colonne ne promet une citation que si son en-tête le dit. Sans cette
#: exigence, l'outil compare la colonne « notion » d'une matrice au programme et
#: crie à l'erreur là où personne n'a rien promis — c'est ainsi qu'un contrôle
#: neuf « trouve » des dizaines de fautes qui n'existent pas (règle d'or n°242).
PROMESSE = re.compile(r"formulation|ce que dit le programme|programme\s*2024|"
                      r"r[ée]f[ée]rentiel|libell[ée]\s+officiel|recopi[ée]|"
                      r"codes, en toutes lettres", re.I)


def fichiers():
    for racine, sous, noms in os.walk(RACINE):
        sous[:] = [d for d in sous if d not in IGNORES and not d.startswith(".")]
        for n in sorted(noms):
            if n.lower().endswith(LISIBLES):
                yield os.path.join(racine, n)


def juger(niveau, code, texte):
    """Renvoie (verdict, officielle) — ou (None, …) si ce n'est pas une citation."""
    officielle = OFFICIELLES.get((niveau, code))
    if officielle is None:
        return None, None
    lu, vrai = normaliser(texte), normaliser(officielle)
    if not lu or len(lu) < LONGUEUR_MINIMALE:
        return None, officielle          # un titre, pas une citation
    if lu == vrai or vrai in lu:
        # `vrai in lu` : un README de lot mutualisé cite les trois formulations
        # à la suite. La nôtre y est, entière : rien à reprocher.
        return "JUSTE", officielle
    if vrai.startswith(lu):
        return "TRONQUÉE", officielle
    ratio = difflib.SequenceMatcher(None, lu.lower(), vrai.lower()).ratio()
    if ratio >= RESSEMBLANCE:
        return "FAUSSE", officielle
    # ressemble-t-elle à la formulation d'un AUTRE code ? c'est le cas le plus
    # traître : la phrase est officielle, mais elle n'est pas celle-là.
    for (n2, c2), autre in OFFICIELLES.items():
        if (n2, c2) == (niveau, code):
            continue
        vautre = normaliser(autre)
        # `startswith` avant le ratio : « Identifier les caractéristiques à
        # prendre en compte dans le choix d'un OST » est le DÉBUT EXACT de la
        # formulation de 4e_C3.1, tout en n'ayant qu'un ratio de 0,82 avec elle
        # — trop bas pour un seuil, et pourtant sans ambiguïté aucune.
        if vautre.startswith(lu) or difflib.SequenceMatcher(
                None, lu.lower(), vautre.lower()).ratio() >= 0.85:
            return "AUTRE CODE (%s_%s)" % (n2, c2), officielle
    # Elle ne ressemble à AUCUNE formulation du référentiel — et pourtant elle
    # est écrite là où une citation est promise. C'est le cas de la fiche CAO,
    # qui annonçait « Formulation du référentiel (2024) » au-dessus de deux
    # phrases inventées. Une première version de cet outil se taisait ici : elle
    # n'aurait pas vu l'erreur qui l'a fait naître.
    if len(lu) < LONGUEUR_ACCUSATION:
        return None, officielle
    return "ÉTRANGÈRE", officielle


def entete_promet(texte, position):
    """Cette ligne est-elle DANS un endroit qui promet une citation ?

    Deux itérations précédentes ont échoué, et de la même façon : elles
    cherchaient la promesse trop loin. La première remontait au dernier en-tête
    rencontré, fût-il d'un autre tableau ; la seconde acceptait tout tableau
    dont la première ligne contenait le mot « formulation ». Toutes deux
    signalaient « 7,4 Wh/jour pour 6,04 consommés » comme une citation fautive
    du programme.

    On exige donc les deux : le **titre de section** qui précède doit promettre
    (« 🎯 Ce que dit le programme », « Formulation du référentiel »), ET la
    ligne d'en-tête du tableau doit le promettre aussi. Là où les deux
    coïncident, il n'y a pas d'ambiguïté possible.
    """
    # ── le titre de section qui précède ──────────────────────────────────
    titres = list(re.finditer(r"<h[1-4][^>]*>[^<]{0,200}|^#{1,4}[ \t]+[^\n]{0,200}",
                              texte[:position], re.M))
    if not titres or not PROMESSE.search(titres[-1].group(0)):
        return False

    # ── la ligne d'en-tête du tableau qui contient la position ───────────
    ouvre = texte.rfind("<table", 0, position)
    if ouvre != -1 and texte.find("<table", ouvre + 1, position) == -1:
        ferme = texte.find("</table>", position)
        if ferme == -1:
            return False
        premiere = re.search(r"<tr[^>]*>[\s\S]*?</tr>", texte[ouvre:ferme])
        return bool(premiere and PROMESSE.search(premiere.group(0)))

    lignes = texte[:position].split("\n")
    i = len(lignes) - 1
    while i > 0 and lignes[i - 1].lstrip().startswith("|"):
        i -= 1
    return bool(PROMESSE.search(lignes[i]))


#: formes dont la promesse est structurelle : elles n'existent QUE pour citer
STRUCTURELLES = {"sous-titre de page d'orientation", "exergue de README"}


def parcourir():
    trouvailles = []
    for chemin in fichiers():
        if not REFERENCE.match(os.path.basename(chemin)):
            continue
        try:
            with open(chemin, encoding="utf-8", errors="ignore") as f:
                t = f.read()
        except OSError:
            continue
        for nom_forme, motif in FORMES:
            for m in motif.finditer(t):
                if nom_forme not in STRUCTURELLES and not entete_promet(t, m.start()):
                    continue
                niveau, code = m.group("niv"), m.group("code")
                verdict, officielle = juger(niveau, code, m.group("texte"))
                if verdict is None:
                    continue
                trouvailles.append(dict(
                    fichier=os.path.relpath(chemin, RACINE).replace(os.sep, "/"),
                    forme=nom_forme, libelle="%s_%s" % (niveau, code),
                    verdict=verdict, lu=normaliser(m.group("texte")),
                    officielle=normaliser(officielle)))
    return trouvailles


#: du plus grave au plus bénin. « AUTRE CODE » ouvre la liste : une formulation
#: officielle placée sous le mauvais code est l'erreur la plus difficile à voir,
#: parce que chaque mot en est juste.
ORDRE = {"AUTRE CODE": 0, "ÉTRANGÈRE": 1, "FAUSSE": 2, "TRONQUÉE": 3, "JUSTE": 4}


def rang(v):
    return ORDRE.get(v.split(" (")[0], 2)


def benin(v):
    """Une troncature est un défaut de recopie, pas une contre-vérité."""
    return v == "TRONQUÉE"


def main():
    muet = "--muet" in sys.argv
    trouvailles = parcourir()
    ecarts = [t for t in trouvailles if t["verdict"] != "JUSTE"]

    if not muet:
        for t in sorted(trouvailles, key=lambda t: (rang(t["verdict"]), t["fichier"])):
            if t["verdict"] == "JUSTE":
                print("✅ %-9s %s" % (t["libelle"], t["fichier"]))

    for t in sorted(ecarts, key=lambda t: (rang(t["verdict"]), t["fichier"])):
        marque = "⚠️" if benin(t["verdict"]) else "❌"
        print("%s %-9s %-11s %s" % (marque, t["libelle"], t["verdict"], t["fichier"]))
        print("     forme    : %s" % t["forme"])
        print("     écrit    : %s" % t["lu"][:150])
        print("     programme: %s" % t["officielle"][:150])

    justes = len(trouvailles) - len(ecarts)
    print("\n%d citation(s) reconnue(s) · %d juste(s) · %d écart(s)"
          % (len(trouvailles), justes, len(ecarts)))
    print("Formes lues : %s." % ", ".join(nom for nom, _m in FORMES))
    print("Toute autre façon d'écrire une formulation échappe à ce contrôle.")

    graves = [t for t in ecarts if not benin(t["verdict"])]
    if graves:
        print("%d formulation(s) à corriger — une citation fausse est pire "
              "qu'une citation absente." % len(graves))
    return 1 if graves else 0


if __name__ == "__main__":
    sys.exit(main())
