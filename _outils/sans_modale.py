#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sans_modale.py — retirer d'une page les boîtes qui bloquent le navigateur.

RÈGLE D'OR N°188 : une page d'élève ne s'arrête pas pour parler.

Une boîte modale (`alert`, `confirm`, `prompt`) fige le navigateur, vole le
focus, ne s'annonce pas aux lecteurs d'écran comme un message de la page, et sur
une page qui enregistre à chaque frappe elle coûte une phrase à celui qui écrit.

CE QUE CET OUTIL A APPRIS, ET POURQUOI IL EXISTE
------------------------------------------------
La règle n°188 a été écrite le 26/08. Elle a d'abord été appliquée à une page,
puis aux `alert()` des QCM produits ensuite — et **on s'est arrêté là, en
déclarant le sujet traité**. Le 29/08, une mesure a montré que le gabarit de QCM
maison ouvre aussi **deux boîtes de confirmation** que personne n'avait
comptées : la validation d'une question sans réponse, et la remise à zéro. Sept
QCM produits « sans boîte modale » en portaient toujours deux chacun, et le test
qui l'affirmait ne passait jamais par ces deux chemins-là.

Puis l'outil lui-même a produit deux défauts, gardés ici en mémoire :

* il posait ses deux fonctions d'un bloc, sous la garde d'une seule ; une page
  qui portait déjà `signale` recevait des appels à `demande` sans la fonction ;
* il comptait les mots `alert(`, `confirm(`, `prompt(` **dans les commentaires
  et les chaînes de caractères**, et refusait donc les pages où sa propre
  documentation citait le mot.

D'où quatre principes, tenus ici :

1. **On ne compte que du code.** Le texte est découpé en code / chaînes /
   commentaires ; seul le code est mesuré et transformé. Un mot dans un
   commentaire n'est pas un appel.

2. **On ne transforme pas ce qu'on n'a pas lu.** L'outil connaît une liste
   fermée de motifs. Devant une confirmation qu'il ne reconnaît pas, il REFUSE
   le fichier au lieu de bricoler. Un remplacement automatique qui se trompe sur
   une confirmation destructive est pire que le défaut.

3. **Une confirmation ne se supprime pas, elle se remplace.** Elle pose une
   question dont la réponse change le comportement : l'effacer, c'est valider en
   silence ce que l'élève n'a pas confirmé. On la remplace par une confirmation
   **en deux temps** — un premier clic annonce, un second dans les six secondes
   exécute — annoncée par le bandeau `aria-live` de la page.

4. **Une fonction appelée doit exister.** L'outil pose chaque helper
   indépendamment, et il répare aussi une page qui n'ouvre plus aucune boîte
   mais appelle un helper qu'elle ne définit pas.

USAGE
    python3 _outils/sans_modale.py <fichier.html> [autres…]
    python3 _outils/sans_modale.py --etat <dossier>       # compter sans modifier
    python3 _outils/sans_modale.py --controle <fichiers…> # vérifier l'invariant
"""

import pathlib
import re
import sys

#: appels bloquants, hors `.alert(`, `$prompt(`, etc.
MODALE = re.compile(r"(?<![\w.$])(alert|confirm|prompt)\s*\(")
ALERTE = re.compile(r"(?<![\w.$])alert\s*\(")

#: les helpers, posés une seule fois, juste après la définition de `$`
ANCRE = "const $=id=>document.getElementById(id);"

#: (marqueur de définition, marqueur d'appel, code à poser). Chacun est posé
#: indépendamment : une page peut déjà porter l'un sans l'autre.
HELPERS = [
    ("function signale(", "signale(", """
/* Règle d'or n°188 : on informe sans bloquer. `signale` écrit dans le bandeau
   #savedNote, qui porte déjà role="status" et aria-live="polite". */
let _signalTimer=null;
function signale(msg){
  const z=$("savedNote"); if(!z){ return; }
  z.textContent=msg; z.classList.add("show");
  clearTimeout(_signalTimer);
  _signalTimer=setTimeout(()=>{ z.textContent=""; z.classList.remove("show"); }, 6000);
}"""),
    ("function demande(", "demande(", """
/* `demande` remplace une boîte de confirmation : le premier clic annonce, le
   second dans les six secondes exécute. On ne supprime jamais une confirmation
   destructive — on la rend non bloquante. */
let _demandes={};
function demande(cle,msg){
  const t=Date.now();
  if(_demandes[cle] && t-_demandes[cle] < 6000){ _demandes[cle]=0; return true; }
  _demandes[cle]=t;
  signale(msg + " — clique une seconde fois pour confirmer.");
  return false;
}"""),
]

#: (motif exact reconnu, remplacement). Liste FERMÉE : tout le reste est refusé.
CONNUS = [
    ('if(!confirm("Tu n\'as choisi aucune réponse. Valider quand même '
     '(compte comme non répondu) ?")) return;',
     'if(!demande("valider","Tu n\'as choisi aucune réponse : elle comptera comme '
     'non répondue.")) return;'),
    ('if(confirm("Recommencer entièrement ? Toutes tes réponses et ton temps seront '
     'effacés (l\'identité est conservée)."))',
     'if(demande("recommencer","Recommencer entièrement ? Toutes tes réponses et ton '
     'temps seront effacés."))'),
]


# --------------------------------------------------------------------------
# Découpage : on ne mesure jamais un mot écrit dans un commentaire ou une chaîne
# --------------------------------------------------------------------------

class Illisible(Exception):
    """Le fichier ne se laisse pas découper de façon sûre : on ne le touche pas."""


def segments(js):
    """Découpe du JavaScript en (nature, texte), nature ∈ code/chaine/commentaire."""
    out, i, debut, n = [], 0, 0, len(js)
    while i < n:
        c = js[i]
        if c in "\"'`":
            out.append(("code", js[debut:i]))
            j, ferme = i + 1, False
            while j < n:
                if js[j] == "\\":
                    j += 2
                    continue
                if js[j] == c:
                    j += 1
                    ferme = True
                    break
                j += 1
            if not ferme:
                raise Illisible("chaîne non fermée")
            out.append(("chaine", js[i:j]))
            i = debut = j
        elif js.startswith("/*", i):
            out.append(("code", js[debut:i]))
            j = js.find("*/", i + 2)
            if j < 0:
                raise Illisible("commentaire /* non fermé")
            out.append(("commentaire", js[i:j + 2]))
            i = debut = j + 2
        elif js.startswith("//", i):
            out.append(("code", js[debut:i]))
            j = js.find("\n", i)
            j = n if j < 0 else j
            out.append(("commentaire", js[i:j]))
            i = debut = j
        else:
            i += 1
    out.append(("code", js[debut:]))
    return out


def code_seul(texte):
    """Le code JavaScript de la page, commentaires et chaînes retirés."""
    js = "\n".join(re.findall(r"<script[^>]*>(.*?)</script>", texte, re.S))
    return "".join(s for nature, s in segments(js) if nature == "code")


def remplacer_dans_code(texte, motif, remplacement):
    """Applique une substitution au seul code des blocs <script>."""
    def par_script(m):
        return m.group(1) + "".join(
            motif.sub(remplacement, s) if nature == "code" else s
            for nature, s in segments(m.group(2))
        ) + m.group(3)
    return re.sub(r"(<script[^>]*>)(.*?)(</script>)", par_script, texte, flags=re.S)


def compter(chemin):
    return len(MODALE.findall(code_seul(
        pathlib.Path(chemin).read_text(encoding="utf-8", errors="replace"))))


def traiter(chemin):
    p = pathlib.Path(chemin)
    origine = t = p.read_text(encoding="utf-8")
    try:
        avant = len(MODALE.findall(code_seul(t)))
    except Illisible as e:
        return 0, 0, "REFUSÉ — %s" % e

    faits = 0
    for motif, remplacement in CONNUS:
        if motif in t:
            faits += t.count(motif)
            t = t.replace(motif, remplacement)

    # ce qui reste : les alert() simples, transformables sans risque
    n_alert = len(ALERTE.findall(code_seul(t)))
    if n_alert:
        t = remplacer_dans_code(t, ALERTE, "signale(")
        faits += n_alert

    # ce qui reste ENCORE est un motif qu'on n'a pas lu : on refuse.
    reste = code_seul(t)
    restant = MODALE.findall(reste)
    if restant:
        extraits = re.findall(r".{0,60}(?<![\w.$])(?:confirm|prompt)\s*\(.{0,60}", reste)
        return avant, 0, ("REFUSÉ — %d appel(s) non reconnu(s) : %s"
                          % (len(restant), " | ".join(x.strip() for x in extraits[:2])))

    # Chaque helper est posé INDÉPENDAMMENT, et seulement s'il est appelé.
    # Les poser ensemble a déjà produit le défaut suivant : une page qui portait
    # déjà `signale` (posée par un générateur précédent) recevait des appels à
    # `demande` sans la fonction — donc une erreur JS au premier clic.
    poses = []
    for cle, appel, corps in HELPERS:
        if appel in reste and cle not in t:
            if ANCRE not in t:
                return avant, 0, "REFUSÉ — ancre du moteur introuvable"
            t = t.replace(ANCRE, ANCRE + corps, 1)
            poses.append(cle[9:-1])

    if t == origine:
        return avant, 0, "rien à faire" + (" (aucune boîte modale)" if not avant else "")

    p.write_text(t, encoding="utf-8")
    bilan = []
    if faits:
        bilan.append("%d boîte(s) remplacée(s)" % faits)
    if poses:
        bilan.append("fonction%s %s posée%s" % ("s" if len(poses) > 1 else "",
                                                " et ".join(poses),
                                                "s" if len(poses) > 1 else ""))
    return avant, faits, " · ".join(bilan)


def controler(chemin):
    """L'invariant, en deux points : aucune boîte, et rien d'appelé sans exister.

    Le second point n'est pas décoratif : c'est exactement le défaut que cet
    outil a produit le 29/08 (des appels à `demande` posés dans cinq pages qui
    ne définissaient pas la fonction). Un outil qui répare doit savoir dire si
    ce qu'il a réparé tient.
    """
    t = pathlib.Path(chemin).read_text(encoding="utf-8", errors="replace")
    try:
        reste = code_seul(t)
    except Illisible as e:
        return ["illisible : %s" % e]
    torts = []
    for nom in sorted(set(MODALE.findall(reste))):
        torts.append("%s() encore ouvert" % nom)
    for cle, appel, _ in HELPERS:
        if appel in reste and cle not in reste:
            torts.append("%s appelée sans être définie" % appel[:-1])
    return torts


def main(argv):
    if "--controle" in argv:
        code = 0
        for chemin in [a for a in argv[1:] if not a.startswith("--")]:
            torts = controler(chemin)
            print("%s %-52s %s" % ("⛔" if torts else "✔",
                                   pathlib.Path(chemin).name[:52],
                                   " · ".join(torts) if torts else
                                   "aucune boîte modale, aucune fonction manquante"))
            if torts:
                code = 1
        return code

    if "--etat" in argv:
        racine = pathlib.Path([a for a in argv[1:] if not a.startswith("--")][0])
        for motif, nom in (("**/qcm*.html", "QCM"), ("**/sequence*.html", "séquences")):
            tot = touche = appels = 0
            for f in sorted(racine.glob(motif)):
                if "_archive" in str(f):
                    continue
                tot += 1
                try:
                    n = compter(f)
                except Illisible:
                    print("  ⚠ illisible : %s" % f)
                    continue
                if n:
                    touche += 1
                    appels += n
            print("%-11s %3d fichiers · %3d en ouvrent · %4d appels" % (nom, tot, touche, appels))
        return 0

    code = 0
    for chemin in argv[1:]:
        avant, faits, msg = traiter(chemin)
        marque = "⛔" if msg.startswith("REFUSÉ") else ("·" if msg.startswith("rien") else "✔")
        print("%s %-52s %s" % (marque, pathlib.Path(chemin).name[:52], msg))
        if msg.startswith("REFUSÉ"):
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
