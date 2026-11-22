# -*- coding: utf-8 -*-
"""poser_entrainement_melange.py — un mode « 🔀 Entraînement mélangé » dans chaque QCM du gabarit (règle d'or n°371).

POURQUOI (audit du 22/11/2026, PR #867)
---------------------------------------
69 QCM sur 70 posent leurs questions par blocs de compétence. Mélanger des compétences voisines aide l'élève à les
distinguer (Rohrer et Taylor, 2007 ; Brunmair et Richter, 2019). Le parcours complet garde son ordre, parfois voulu ;
on AJOUTE un mode qui alterne les compétences, dans un ordre fixe (pas de hasard : deux voisins et l'enseignant voient
la même chose). C'est l'ordre de `mesurer_entrelacement.ordre_entrelace()`, recalculé dans la page.

CE QU'IL FAIT
-------------
Dans chaque `qcm*.html` qui porte le moteur du gabarit (le bouton `data-mode="dix"` et la branche
`else if(mode==="dix"){`) : il pose, une fois, le bouton après « 10 questions » et la branche du mode avant celle de
« 10 questions ». Une page qui l'a déjà n'est pas touchée (idempotent). Une page sans ce moteur est laissée, et dite.

Usage :
    python3 _outils/poser_entrainement_melange.py [chemins…]          # écrit
    python3 _outils/poser_entrainement_melange.py --verifier [chemins…]  # n'écrit rien : 1 si une page n'a pas le mode
Sortie : 0 · 1 (--verifier, au moins une page sans le mode) · 2 EN PANNE (aucun QCM lu, n°299).
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORES = {".git", "node_modules", "_archive-anciennes-versions", "_outils", "_exports"}
MARQUE = 'data-mode="melange"'
BOUTON_DIX = re.compile(r'(<button class="btn"[^>]*data-mode="dix"[^>]*>[^<]*</button>)')
BOUTON = ('\n    <button class="btn" data-mode="melange" title="Les compétences alternent : on apprend à les distinguer">'
          '🔀 Entraînement mélangé</button>')
BRANCHE_DIX = 'else if(mode==="dix"){'
BRANCHE = ('else if(mode==="melange"){\n'
           '    /* Règle d\'or n°371 (en essai) : un tour par compétence, tant qu\'il en reste ; ordre fixe, sans hasard. */\n'
           '    const files={}, ordre=[];\n'
           '    QUESTIONS.forEach((q,i)=>{ const c=q.c||"—"; if(!files[c]){ files[c]=[]; ordre.push(c); } files[c].push(i); });\n'
           '    const suite=[]; let reste=true;\n'
           '    while(reste){ reste=false; ordre.forEach(c=>{ if(files[c].length){ suite.push(files[c].shift()); reste=true; } }); }\n'
           '    etat.sousListe=suite;\n'
           '  }\n  ')


def qcms(departs):
    for depart in departs:
        if os.path.isfile(depart):
            yield depart
            continue
        for dossier, sous, noms in os.walk(depart):
            sous[:] = sorted(d for d in sous if d not in IGNORES and not d.startswith("."))
            for nom in sorted(noms):
                if nom.startswith("qcm") and nom.endswith(".html"):
                    yield os.path.join(dossier, nom)


def poser(texte):
    """Rend (texte, statut) — statut : « posé », « déjà », « sans moteur »."""
    if MARQUE in texte:
        return texte, "déjà"
    if not BOUTON_DIX.search(texte) or texte.count(BRANCHE_DIX) != 1:
        return texte, "sans moteur"
    texte = BOUTON_DIX.sub(lambda m: m.group(1) + BOUTON, texte, count=1)
    texte = texte.replace(BRANCHE_DIX, BRANCHE + BRANCHE_DIX, 1)
    return texte, "posé"


def main(argv):
    verifier = "--verifier" in argv
    departs = [a for a in argv if not a.startswith("--")] or [RACINE]
    compte = {"posé": [], "déjà": [], "sans moteur": []}
    lus = 0
    for chemin in qcms(departs):
        try:
            texte = open(chemin, encoding="utf-8").read()
        except OSError:
            continue
        lus += 1
        neuf, statut = poser(texte)
        rel = os.path.relpath(chemin, RACINE)
        if verifier and statut == "posé":
            statut = "à poser"
            compte.setdefault("à poser", []).append(rel)
            continue
        compte[statut].append(rel)
        if statut == "posé":
            open(chemin, "w", encoding="utf-8").write(neuf)
    if not lus:
        print("⛔ EN PANNE : aucun QCM lu (n°299).")
        return 2
    for rel in compte["sans moteur"]:
        print("· sans le moteur du gabarit (laissé) :", rel)
    print(f"{lus} QCM lus · {len(compte['posé'])} posé(s) · {len(compte['déjà'])} déjà · "
          f"{len(compte.get('à poser', []))} à poser · {len(compte['sans moteur'])} sans moteur")
    if verifier and compte.get("à poser"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
