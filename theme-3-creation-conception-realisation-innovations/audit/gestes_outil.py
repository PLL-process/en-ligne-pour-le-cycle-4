# -*- coding: utf-8 -*-
"""Règle d'or n°93 — poser, dans chaque séquence qui met un logiciel entre les
mains de l'élève, l'encart des quatre gestes : ouvrir · nommer · retrouver ·
sortir.

    python3 audit/gestes_outil.py <dossier de thème>

L'encart est rédigé pour quelqu'un qui n'a JAMAIS vu le logiciel. Aucune
formule du type « comme tu l'as vu en 5e » : c'est exactement ce que la règle
interdit, puisque l'année précédente n'a pas toujours eu lieu — professeur
muté, emploi du temps amputé, élève arrivé d'un autre collège.

Il se pose après le rappel spiralaire quand il y en a un (la continuité
d'abord, le filet ensuite), sinon après le bandeau de badges.

CE QUE CE SCRIPT REFUSE DE FAIRE
  · écrire deux fois dans la même page (marqueur GESTES_MARQUEUR) ;
  · toucher un QCM, un gabarit, une synthèse ou une archive ;
  · inventer un texte pour un logiciel qu'il ne connaît pas : si le logiciel
    n'est pas dans le tableau ci-dessous, la page est SIGNALÉE, pas modifiée.
"""
import pathlib
import re
import sys

GESTES_MARQUEUR = "gestes-outil-v1"

# Un texte par logiciel, écrit pour qui ne l'a jamais ouvert.
# Chaque entrée : (ouvrir, nommer, retrouver, sortir).
FICHES = {
    "Vittascience": (
        "Ouvre <b>Vittascience</b> dans le navigateur et connecte-toi avec le "
        "compte de la classe.",
        "Clique sur le titre du projet, en haut, et remplace-le par "
        "<code>NIVEAU-SUJET-TON&nbsp;NOM</code>. Un projet sans nom est "
        "introuvable la semaine suivante.",
        "Ton projet est enregistré dans ton compte&nbsp;: tu le retrouveras "
        "depuis n'importe quel poste en te reconnectant, dans la liste de tes "
        "projets. Vérifie-le tout de suite&nbsp;: reviens à la liste, puis "
        "rouvre ton projet.",
        "Pour garder une trace hors ligne&nbsp;: <b>Fichier → Exporter</b>, ou "
        "une capture d'écran du programme collée dans ton compte rendu.",
    ),
    "Onshape": (
        "Ouvre <b>Onshape</b> dans le navigateur et connecte-toi avec le compte "
        "de la classe, puis <b>Créer → Document…</b>",
        "Dans <b>Nom du document</b>, saisis <code>NIVEAU-SUJET-TON&nbsp;NOM</code> "
        "(sans accent). Le gris pâle <i>Document sans titre</i> n'est pas un nom.",
        "Il n'y a <b>pas</b> de bouton Enregistrer&nbsp;: Onshape écrit chaque "
        "geste au moment où tu le fais. Vérifie-le&nbsp;: clique sur le logo "
        "Onshape en haut à gauche, la page Documents s'affiche, tu rouvres ton "
        "document, tout est là.",
        "Pour imprimer en 3D&nbsp;: clic droit sur la pièce → <b>Exportateur…</b> "
        "→ format <b>STL</b>, unités <b>Millimètre</b>, et l'option qui "
        "<b>stocke le fichier dans un nouvel onglet</b> du document.",
    ),
    "Packet Tracer": (
        "Ouvre <b>Packet Tracer</b> depuis le bureau, puis <b>Fichier → "
        "Nouveau</b>.",
        "<b>Fichier → Enregistrer sous…</b> dès le début, dans ton dossier "
        "personnel, sous le nom <code>NIVEAU-SUJET-TON&nbsp;NOM.pkt</code>.",
        "Packet Tracer n'enregistre <b>pas</b> tout seul&nbsp;: reprends "
        "<kbd>Ctrl</kbd>+<kbd>S</kbd> à chaque étape importante. Un réseau perdu "
        "se refait, mais il prend la séance entière.",
        "Le fichier <code>.pkt</code> est ton rendu. Ajoutes-y une capture "
        "d'écran de la topologie si le compte rendu la demande.",
    ),
    "Filius": (
        "Ouvre <b>Filius</b> depuis le bureau. Un réseau vide s'affiche.",
        "<b>Fichier → Enregistrer sous…</b> immédiatement, dans ton dossier "
        "personnel, sous <code>NIVEAU-SUJET-TON&nbsp;NOM</code>.",
        "Filius n'enregistre pas tout seul&nbsp;: enregistre à chaque étape. "
        "Pour retrouver ton travail, rouvre le fichier depuis ton dossier.",
        "Ton fichier de simulation est le rendu&nbsp;; une capture d'écran du "
        "réseau complète le compte rendu.",
    ),
    "Scratch": (
        "Ouvre <b>Scratch</b> et démarre un nouveau projet.",
        "Donne un nom au projet en haut de la page&nbsp;: "
        "<code>NIVEAU-SUJET-TON&nbsp;NOM</code>.",
        "Selon la version, Scratch enregistre dans ton compte ou pas du tout&nbsp;: "
        "vérifie-le en fermant puis en rouvrant ton projet, dès le début de la "
        "séance. Si le projet n'y est plus, utilise <b>Fichier → Enregistrer sur "
        "ton ordinateur</b> à chaque étape.",
        "<b>Fichier → Enregistrer sur ton ordinateur</b> produit un fichier "
        "<code>.sb3</code>&nbsp;: c'est lui qu'on rend.",
    ),
    "Arduino": (
        "Ouvre l'éditeur (<b>Arduino</b> ou <b>mBlock</b>) et crée un nouveau "
        "programme.",
        "<b>Fichier → Enregistrer sous…</b> dans ton dossier personnel, sous "
        "<code>NIVEAU-SUJET-TON&nbsp;NOM</code>.",
        "Le programme vit sur le disque du poste, pas dans la carte&nbsp;: "
        "enregistre avant de téléverser, et rouvre ton fichier pour vérifier "
        "qu'il est bien là.",
        "Le fichier du programme est le rendu. La carte, elle, sera reprogrammée "
        "par la classe suivante&nbsp;: elle ne garde rien pour toi.",
    ),
    "GanttProject": (
        "Ouvre <b>GanttProject</b> depuis le bureau, puis <b>Projet → "
        "Nouveau</b>.",
        "<b>Projet → Enregistrer sous…</b> dès le début, sous "
        "<code>NIVEAU-SUJET-TON&nbsp;NOM.gan</code>, dans ton dossier personnel.",
        "GanttProject n'enregistre pas tout seul. Enregistre après chaque tâche "
        "ajoutée, et rouvre ton fichier en début de séance suivante.",
        "Pour rendre le planning&nbsp;: <b>Projet → Exporter</b> en <b>PNG</b> "
        "ou en <b>PDF</b>, à joindre au compte rendu.",
    ),
    "Tableur": (
        "Ouvre le tableur (<b>LibreOffice Calc</b>) et crée un classeur.",
        "<b>Fichier → Enregistrer sous…</b> tout de suite, sous "
        "<code>NIVEAU-SUJET-TON&nbsp;NOM</code>, dans ton dossier personnel.",
        "Le tableur n'enregistre pas tout seul&nbsp;: "
        "<kbd>Ctrl</kbd>+<kbd>S</kbd> après chaque série de saisies. Rouvre ton "
        "fichier au début de la séance suivante pour vérifier qu'il est complet.",
        "Le classeur est le rendu. Un graphique se copie dans le compte rendu, "
        "ou s'exporte en image par un clic droit.",
    ),
}

LOGICIELS = {
    "Onshape":       r"Onshape",
    "GanttProject":  r"GanttProject|\.gan\b",
    "Vittascience":  r"Vittascience",
    "Filius":        r"Filius",
    "Packet Tracer": r"Packet\s*Tracer",
    "Scratch":       r"Scratch",
    "Arduino":       r"Arduino|mBlock",
    "Tableur":       r"LibreOffice Calc|tableur.{0,40}(ouvr|saisis|classeur|feuille de calcul)",
}

# L'ordre décide du logiciel PRINCIPAL quand une séquence en cite plusieurs :
# celui que l'élève manipule vraiment passe avant celui qui est mentionné.
PRIORITE = ["Onshape", "Vittascience", "Packet Tracer", "Filius", "GanttProject",
            "Scratch", "Arduino", "Tableur"]

IGNORE = re.compile(r"(^|/)(_archive[^/]*|_modele|_generation)/|gabarit|/qcm_|synthese", re.I)

CSS = """
<style>
  .gestes-outil{border:1px solid var(--border,#2a3550);border-left:4px solid #ffb300;
    border-radius:10px;padding:1rem 1.15rem;margin:1.1rem 0;background:var(--panel,#0e1730)}
  .gestes-outil h2{margin:0 0 .35rem;font-size:1.05em}
  .gestes-outil .pourquoi{margin:.2rem 0 .8rem;opacity:.85;font-size:.95em}
  .gestes-outil ol{margin:0;padding-left:1.3rem}
  .gestes-outil li{margin:.45rem 0}
  .gestes-outil li b:first-child{color:#ffb300}
</style>
"""

GABARIT = """<!-- %(marqueur)s : règle d'or n°93 — les gestes d'outil, réenseignés à chaque niveau. -->
<section class="card gestes-outil" aria-labelledby="gestes-%(cle)s">
  <h2 id="gestes-%(cle)s">🧰 Avant de commencer — les quatre gestes de %(logiciel)s</h2>
  <p class="pourquoi">Quatre gestes à faire une fois, au début, et ta séance ne
  se perdra pas. Tu les as peut-être déjà faits une autre année&nbsp;: refais-les,
  c'est court. Et si tu ne les as jamais faits, tout est écrit ici — tu n'as
  besoin de rien d'autre.</p>
  <ol>
    <li><b>Ouvrir.</b> %(ouvrir)s</li>
    <li><b>Nommer.</b> %(nommer)s</li>
    <li><b>Retrouver.</b> %(retrouver)s</li>
    <li><b>Sortir.</b> %(sortir)s</li>
  </ol>
</section>
"""


def logiciel_principal(texte):
    trouves = [n for n, m in LOGICIELS.items() if re.search(m, texte, re.I)]
    for n in PRIORITE:
        if n in trouves:
            return n, trouves
    return None, trouves


def point_d_insertion(html):
    """Après le rappel spiralaire s'il existe, sinon après les badges."""
    m = re.search(r'<section class="card rappel-spiralaire".*?</section>', html, re.S)
    if m:
        return m.end()
    m = re.search(r'<div class="badges">.*?</div>', html, re.S)
    if m:
        return m.end()
    m = re.search(r"</h1>", html)
    return m.end() if m else None


def main(racine):
    pages = [p for p in sorted(pathlib.Path(racine).rglob("sequence*.html"))
             if not IGNORE.search(str(p))]
    faits, deja, inconnus, sans_ancre, sans_logiciel = [], [], [], [], []

    for p in pages:
        html = p.read_text(encoding="utf-8")
        if GESTES_MARQUEUR in html:
            deja.append(p); continue
        texte = re.sub(r"<[^>]+>", " ", html)
        principal, tous = logiciel_principal(texte)
        if not principal:
            sans_logiciel.append(p); continue
        if principal not in FICHES:
            inconnus.append((p, principal)); continue
        pos = point_d_insertion(html)
        if pos is None:
            sans_ancre.append(p); continue

        o, n, r, s = FICHES[principal]
        bloc = GABARIT % {"marqueur": GESTES_MARQUEUR,
                          "cle": re.sub(r"\W", "", principal).lower(),
                          "logiciel": principal,
                          "ouvrir": o, "nommer": n, "retrouver": r, "sortir": s}
        style = "" if ".gestes-outil{" in html else CSS
        p.write_text(html[:pos] + "\n" + style + bloc + html[pos:], encoding="utf-8")
        faits.append((p, principal, tous))

    print("ENCART DES GESTES D'OUTIL — règle d'or n°93")
    print("=" * 64)
    print("%d séquence(s) équipée(s), %d déjà équipée(s), %d sans logiciel."
          % (len(faits), len(deja), len(sans_logiciel)))
    for p, principal, tous in faits:
        autres = [t for t in tous if t != principal]
        print("  ✔ %-58s %s%s" % (p.name[:58], principal,
                                  (" (aussi : %s)" % ", ".join(autres)) if autres else ""))
    for p, l in inconnus:
        print("  ✘ %s — logiciel « %s » sans fiche : à écrire à la main." % (p.name, l))
    for p in sans_ancre:
        print("  ✘ %s — aucun point d'insertion trouvé." % p.name)

    print("""
PÉRIMÈTRE DE CE SCRIPT
  Vérifié mécaniquement : un seul encart par page, posé après le rappel
  spiralaire quand il existe, et le choix du logiciel PRINCIPAL quand la
  page en cite plusieurs.
  NON couvert : la justesse du texte pour la version installée au collège.
  Les menus changent d'une version à l'autre — cela se constate en salle,
  en déroulant la séance sur un poste élève, jamais dans un script.""")
    return 1 if (inconnus or sans_ancre) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
