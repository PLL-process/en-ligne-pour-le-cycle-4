# -*- coding: utf-8 -*-
"""controle_ordre_propositions.py — la bonne réponse ne se devine pas à sa place.

LE CONSTAT (audit externe, point « boutons Vérifier », 08/11/2026)
------------------------------------------------------------------
Dans les dix séquences du thème 1 écrites au gabarit de la règle d'or n°300 (groupes de
boutons radio, valeur = texte de la proposition), la table des réponses attendues
(`const att = {…}`) a été comparée à l'ordre des propositions dans la page : sur
256 groupes appariés, la bonne réponse était **256 fois la première proposition**. Un
élève qui coche toujours la première ligne a tout juste, sans lire. Le contrôle
`controle_longueurs.py` juge la longueur de la bonne réponse dans les QCM ; personne ne
jugeait sa PLACE dans les séquences. Quatre pages mélangent déjà leurs propositions au
chargement (script) : elles ne sont pas concernées.

CE QU'IL MESURE
---------------
Pour chaque page (hors QCM, synthèses, archive) qui porte des `<fieldset class="qcm-groupe">`
ET une table `const att = { id: "texte attendu", … }` :
  · la position (1, 2, 3…) de la proposition attendue dans chaque groupe apparié ;
  · la page est REFUSÉE si au moins 6 groupes sont appariés et que plus de 60 % des bonnes
    réponses occupent la même position — ou si la page ne mélange pas et qu'un seul rang
    porte toutes les bonnes réponses. Une page qui mélange ses propositions au chargement
    (`shuffle`, `mélanger`, `sort(() => Math.random`) est lue comme saine.

`--corriger` réordonne les blocs `<div class="qcm-option">` de chaque groupe, de façon
DÉTERMINISTE (graine = nom de la page + id du groupe, donc rejouable), en gardant chaque
`input` avec son `label` et ses identifiants. La valeur transmise étant le TEXTE de la
proposition (n°300), les tables de réponses attendues et les bancs qui cochent `#id__n`
ne changent pas. Après mélange, la page est remesurée : si une position dépasse encore 50 %,
la graine est incrémentée et on recommence. Un groupe dont une proposition dit « aucune
des … », « toutes les … » ou « les deux » garde cette proposition en dernier.

LA PLACE PAR LONGUEUR — UNE MESURE, PAS UN REFUS (veille du 15/11/2026)
-----------------------------------------------------------------------
Mélanger les propositions ne cache pas la bonne réponse si elle est toujours la PLUS LONGUE : l'élève
qui coche la ligne la plus longue s'en tire sans lire (règle d'or n°144, mesurée dans les QCM le
27/08/2026 ; « 32 fois sur 40 la plus longue » dans une séquence, #690). Le contrôle range donc aussi,
pour chaque groupe d'au moins trois propositions, la bonne réponse par sa LONGUEUR (caractères du texte,
sans balises) : strictement la plus longue, strictement la plus courte, ou au milieu.

  · Cible écrite : 15 / 15 / 70 — la plus longue dans 15 % des questions, la plus courte dans 15 %,
    au milieu sinon. Idée prise d'un skill de QCM pour Moodle (`danielcregg/moodle-mcq`, licence MIT),
    réécrite ici de zéro.
  · Signalement ⚠ d'une page dès 6 groupes appariés si la bonne réponse y est la plus longue dans plus
    de 40 % des groupes. Pourquoi 40 % et non les 30 % proposés par la veille : avec quatre
    propositions, le hasard seul en donne 25 % ; sur 30 groupes écrits au hasard, 30 % est dépassé
    une fois sur cinq, 40 % une fois sur vingt. Le signalement désigne une habitude d'écriture, pas
    un hasard.
  · Mesuré le 15/11/2026 sur `main` : 569 groupes de 3 propositions ou plus dans 25 pages, la bonne
    réponse est la plus longue dans 70 % des groupes, la plus courte dans 3 % ; 17 pages sur 23
    dépassent 40 %. C'est un vrai défaut, à reprendre page par page à la révision (la correction est
    une réécriture des propositions, pas un réordonnancement : `--corriger` n'y touche pas).

Le signalement ne change pas la sortie. `--longueur` détaille les pages, de la pire à la meilleure.

Usage : python3 _outils/controle_ordre_propositions.py [--racine .] [--corriger] [--longueur] [--muet]
Sortie 0 si rien à refuser, 1 s'il reste une page où la place trahit la réponse, 2 si aucune
page n'a pu être lue (règle d'or n°299).
"""
import collections
import html
import os
import random
import re
import sys

EXCLUS = {"_archive-anciennes-versions", ".git", "node_modules", "__pycache__", "_exports", "_generation", "_outils"}
SEUIL_GROUPES = 6
SEUIL_PART = 0.60
# 11/11/2026 : « m[ée]lange » seul reconnaissait le mot dans un commentaire, un texte ou une fonction de couleurs
# (`melange(a, b, f)` du lampadaire de 5e) et lisait la page comme saine : six pages passaient ainsi sans être
# mesurées, dont celle où Pascal a vu « les bonnes réponses toujours les premières ». On ne reconnaît plus qu'un
# mélange fait par un script au chargement.
MELANGE = re.compile(r"shuffle\s*\(|Fisher-Yates|sort\(\(\)\s*=>\s*Math\.random", re.I)
# l'ordre de ces groupes est une légende ou une échelle : on les mesure, on ne les réordonne pas
FIXES = ("qcm-grille", "qcm-rangee", "positionnement")
DERNIER = re.compile(r"\b(aucune? des|toutes? (les|ces)|les deux|ni l'un ni l'autre)\b", re.I)
# le groupe peut porter d'autres classes (qcm-grille, qcm-rangee) et d'autres attributs (data-melange, posé par
# melanger_propositions.py) : sans cela, un groupe déjà mélangé n'était plus lu du tout.
FIELDSET = re.compile(r'<fieldset class="(qcm-groupe[^"]*)" id="([^"]+)"([^>]*)>(.*?)</fieldset>', re.S)
OPTION = re.compile(r'(\s*<div class="qcm-option">.*?</div>)', re.S)
VALEUR = re.compile(r'<input type="radio"[^>]*value="([^"]*)"')
ATT = re.compile(r"const att\s*=\s*\{(.*?)\};", re.S)
PAIRE = re.compile(r'(\w+)\s*:\s*"((?:[^"\\]|\\.)*)"')


def pages_html(racine):
    for dossier, sous, fichiers in os.walk(racine):
        sous[:] = [s for s in sous if s not in EXCLUS and not s.startswith(".banc")]
        for f in fichiers:
            nom = f.lower()
            if nom.endswith(".html") and not nom.startswith("qcm") and "synthese" not in nom:
                yield os.path.join(dossier, f)


def attendus(src):
    att = {}
    for m in ATT.finditer(src):
        for k, v in PAIRE.findall(m.group(1)):
            att[k] = v.replace('\\"', '"')
    return att


def groupes(src):
    out = {}
    for m in FIELDSET.finditer(src):
        vals = [html.unescape(v) for v in VALEUR.findall(m.group(4))]
        out[m.group(2)] = vals
    return out


def positions(src):
    """Counter des positions (1-based) de la bonne réponse, pour les groupes appariés."""
    att, grp = attendus(src), groupes(src)
    pos = collections.Counter()
    for k, v in att.items():
        if k in grp and v in grp[k]:
            pos[grp[k].index(v) + 1] += 1
    return pos


SEUIL_LONGUEUR = 0.40      # part de groupes où la bonne réponse est la plus longue, au-delà : ⚠


def longueur(valeur):
    """la longueur que l'élève voit : le texte de la proposition, sans balises ni blancs répétés"""
    return len(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", valeur))).strip())


def rangs_longueur(src):
    """Counter {'longue', 'courte', 'milieu'} : la bonne réponse rangée par sa longueur, groupes de 3 propositions
    ou plus (à deux, la plus longue a une chance sur deux : la mesure ne dirait rien)"""
    att, grp = attendus(src), groupes(src)
    rangs = collections.Counter()
    for k, v in att.items():
        if k not in grp or v not in grp[k] or len(grp[k]) < 3:
            continue
        i = grp[k].index(v)
        L = [longueur(x) for x in grp[k]]
        autres = L[:i] + L[i + 1:]
        rangs["longue" if L[i] > max(autres) else "courte" if L[i] < min(autres) else "milieu"] += 1
    return rangs


def verdict(src, pos):
    n = sum(pos.values())
    if n == 0:
        return None
    scripts = " ".join(re.findall(r"<script[^>]*>(.*?)</script>", src, re.S))
    if MELANGE.search(scripts):
        return "mélange au chargement"
    pire, part = pos.most_common(1)[0]
    if n >= SEUIL_GROUPES and part / n > SEUIL_PART:
        return "REFUS : %d groupes sur %d ont la bonne réponse en position %d" % (part, n, pire)
    return "ok"


def melanger_page(src, nom_page):
    def melange_fieldset(m):
        classes, fid, attrs, corps = m.group(1), m.group(2), m.group(3), m.group(4)
        if any(c in classes.split() for c in FIXES):
            return m.group(0)
        blocs = OPTION.findall(corps)
        if len(blocs) < 2 or "".join(blocs) != corps.rstrip() and "".join(blocs).strip() != corps.strip():
            # le corps porte autre chose que des options (légende, aide) : on ne réordonne que la
            # suite des options, à leur place.
            debut = corps.find(blocs[0]) if blocs else -1
            if debut < 0:
                return m.group(0)
            fin = corps.rfind(blocs[-1]) + len(blocs[-1])
            avant, apres = corps[:debut], corps[fin:]
        else:
            avant, apres = "", corps[len("".join(blocs)):]
        graine = nom_page + "|" + fid + "|" + str(melange_fieldset.tour)
        ordre = list(range(len(blocs)))
        random.Random(graine).shuffle(ordre)
        # « aucune des… », « toutes les… », « les deux » restent en dernier
        derniers = [i for i in ordre if DERNIER.search(re.sub(r"<[^>]+>", " ", blocs[i]))]
        ordre = [i for i in ordre if i not in derniers] + derniers
        return '<fieldset class="%s" id="%s"%s>%s%s%s</fieldset>' % (classes, fid, attrs, avant, "".join(blocs[i] for i in ordre), apres)
    melange_fieldset.tour = 0
    for tour in range(1, 8):
        melange_fieldset.tour = tour
        out = FIELDSET.sub(melange_fieldset, src)
        pos = positions(out)
        n = sum(pos.values())
        if n == 0 or pos.most_common(1)[0][1] / n <= 0.5:
            return out, tour
    return out, tour


def main(argv):
    racine, corrige, muet, detail_longueur = ".", False, False, False
    i = 0
    while i < len(argv):
        if argv[i] == "--racine":
            racine = argv[i + 1]; i += 2
        elif argv[i] == "--corriger":
            corrige = True; i += 1
        elif argv[i] == "--muet":
            muet = True; i += 1
        elif argv[i] == "--longueur":
            detail_longueur = True; i += 1
        else:
            print("argument inconnu :", argv[i]); return 2

    lus, apparies, refus, sains = 0, 0, [], 0
    rangs_site, longues = collections.Counter(), []
    for p in sorted(pages_html(racine)):
        try:
            src = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        if 'class="qcm-groupe"' not in src:
            continue
        lus += 1
        rel = os.path.relpath(p, racine).replace("\\", "/")
        pos = positions(src)
        v = verdict(src, pos)
        if v is None:
            continue
        apparies += sum(pos.values())
        if v.startswith("REFUS") and corrige:
            src2, tours = melanger_page(src, os.path.basename(p))
            open(p, "w", encoding="utf-8").write(src2)
            pos = positions(src2)
            v = verdict(src2, pos)
            if not muet:
                print("✎ %s — propositions réordonnées (%d tour(s)) : positions %s"
                      % (rel, tours, dict(sorted(pos.items()))))
        if v.startswith("REFUS"):
            refus.append((rel, v, dict(sorted(pos.items()))))
        else:
            sains += 1
        rg = rangs_longueur(src)
        rangs_site += rg
        n = sum(rg.values())
        if n >= SEUIL_GROUPES and rg["longue"] / n > SEUIL_LONGUEUR:
            longues.append((rg["longue"] / n, rel, rg["longue"], n))

    if lus == 0:
        print("⛔ aucune page à groupes radio lue sous %s (sortie 2)" % racine); return 2
    if not muet:
        for rel, v, pos in refus:
            print("✘ %s — %s · positions %s" % (rel, v, pos))
    n = sum(rangs_site.values())
    if n:
        if detail_longueur:
            for part, rel, k, m in sorted(longues, reverse=True):
                print("⚠ %s — la bonne réponse est la plus longue dans %d groupe(s) sur %d (%.0f %%)" % (rel, k, m, 100 * part))
        print("⚠ place par longueur (mesure, hors refus) : sur %d groupe(s) de 3 propositions ou plus, la bonne réponse est "
              "la plus longue %.0f %%, la plus courte %.0f %%, au milieu %.0f %% (cible 15 / 15 / 70) · %d page(s) au-delà "
              "de %.0f %% de « la plus longue »%s"
              % (n, 100 * rangs_site["longue"] / n, 100 * rangs_site["courte"] / n, 100 * rangs_site["milieu"] / n,
                 len(longues), 100 * SEUIL_LONGUEUR, "" if detail_longueur or not longues else " (--longueur : la liste)"))
    print("%d page(s) à groupes radio lues · %d groupe(s) appariés à une réponse attendue · %d page(s) saines · %d refus"
          % (lus, apparies, sains, len(refus)))
    if refus:
        print("✘ dans %d page(s), la place de la proposition trahit la bonne réponse" % len(refus))
        return 1
    print("✅ nulle part la bonne réponse ne se devine à sa place")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
