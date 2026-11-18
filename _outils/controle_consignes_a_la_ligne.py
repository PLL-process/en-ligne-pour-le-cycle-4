#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Règle d'or n°342 (18/11/2026) : chaque consigne à la ligne — une action par ligne, numérotée.

Demande de Pascal : « "Chaque consigne doit être à la ligne." Une règle d'or doit être établie. » Une consigne qui
demande plusieurs actions les donne chacune sur sa ligne (①, ②… ou a), b)…), dans l'ordre où l'élève les fait, jamais
enchaînées dans une même phrase par « ; », « , puis » ou « et ensuite ». Une phrase de contexte peut ouvrir la
consigne, sur sa propre ligne.

Ce qui est lu : dans chaque page d'élève des thèmes (hors archives, QCM et lexiques), chaque élément dont une classe
nomme la consigne (`consigne`, `consigne-grille`, `verif-consigne`…) et chaque paragraphe qui commence par
« Consigne ». Une ligne est ce qui se lit entre deux retours (`<br>`, paragraphe, élément de liste…). Un listing
(`<pre>`) et le code en ligne (`<code>`) ne sont pas lus : ce sont des choses à recopier, pas des actions.

Ce qui est relevé, ligne par ligne :
  N1 ✘ deux étapes numérotées sur la même ligne (« ① Lis le programme. ② Classe… » sans retour entre les deux) ;
  N2 ✘ deux actions enchaînées sur la même ligne, par « ; », « puis », « ensuite » ou deux phrases à l'impératif
       (« Lis le programme ; classe chaque donnée », « compare…, puis choisis… ») ;
  N3 ⚠ deux actions jointes par « et » (« lis le programme et réponds ») — à juger : « observe et décris » se lit
       d'un coup, « recopie le tableau et complète-le avec tes mesures » se coupe.

Une action est un verbe à l'impératif en tête de segment, après « puis », ou après une virgule ou un deux-points
(« Pour chaque essai, compare… ») ; « le programme », « la classe » ne sont pas des actions (le mot n'est pas en
tête). La liste des impératifs est celle de `audit_aeration.py`, complétée ici.

Usage :
  python3 _outils/controle_consignes_a_la_ligne.py                    # tout le site : le relevé par page, les totaux
  python3 _outils/controle_consignes_a_la_ligne.py <page.html>…       # ces pages, chaque écart cité
  python3 _outils/controle_consignes_a_la_ligne.py --strict <page>…   # sortie 1 s'il reste un N1 ou un N2
  python3 _outils/controle_consignes_a_la_ligne.py --json <f.json>    # écrit aussi le relevé en JSON
Sans --strict, c'est une mesure (sortie 0) ; sortie 2 si aucune page n'a pu être lue (n°299).
Banc : `python3 _outils/tests_controle_consignes_a_la_ligne.py`.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_aeration import FRONTIERE, IMPERATIFS, INVISIBLE, element, texte  # noqa: E402

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# impératifs que les consignes du site emploient et que la liste d'`audit_aeration.py` n'a pas (relevés le 18/11/2026)
IMPERATIFS_EN_PLUS = set("""donne trouve recopie surligne implémente implemente analyse dis précise precise déduis deduis
conclus représente represente schématise schematise résume resume rends envoie dépose depose partage montre joue
double-clique transfère transfere exporte importe remplace corrige formule attribue raye barre encadre numérote numerote
lie fixe règle regle ajuste branche installe télécharge telecharge démarre demarre arrête arrete oriente pointe vise
dépose fabrique conçois concois modélise modelise simule estime évalue evalue argumente rédige redige surveille
relance réessaie reessaie active désactive desactive tourne pousse tire lève leve baisse soulève souleve pèse pese
filme photographie capture dicte prononce lis-le lis-la franchis déroule deroule reporte prédis predis
réexécute reexecute résous resous""".split())
VERBES = IMPERATIFS | IMPERATIFS_EN_PLUS

MOT = r"([a-zàâäçéèêëîïôöùûüÿœ]+(?:-[a-zàâäçéèêëîïôöùûüÿœ]+)?)"
# le verbe en tête du segment, après « puis » / « ensuite », ou après une virgule, un deux-points, une parenthèse
TETE = re.compile(r"(?:^|[,:(]\s*)(?:(?:puis|ensuite|enfin)\s+)?" + MOT, re.I)
# ce qui sépare deux actions sur une même ligne
SEPARATEUR = re.compile(r"\s*;\s*|,?\s+puis\s+|,?\s+et\s+ensuite\s+|,\s*ensuite\s*,?\s+|(?<=[.!?…])\s+(?=[«(\"A-ZÀ-Ý①-⑳])")
ET = re.compile(r"\s+et\s+(?=%s\b)" % MOT, re.I)
# ce qui ouvre une ligne sans être une action : l'étiquette « Consigne : », un repère numéroté, une puce
ETIQUETTE = re.compile(r"^(?:[^\wÀ-ÿ①-⑳]*\s*)?(?:consigne[^:.—–-]{0,40}?(?:\s*[:.—–-]\s*|$))?", re.I)
REPERE = re.compile(r"^\s*(?:[①-⑳]|\(?[a-h]\)|\(?[1-9][0-9]?[.)])\s*")
NUMEROS = re.compile(r"[①-⑳]")
LETTRES = re.compile(r"(?:^|\s)\(?([a-h])\)\s")
CLASSE_CONSIGNE = re.compile(r'<(div|p|section|aside|li|td|span|header|details|figcaption)\b[^>]*\bclass="([^"]*)"', re.I)
PARAGRAPHE_CONSIGNE = re.compile(r"<(p|div)\b[^>]*>\s*(?:<(?:b|strong)\b[^>]*>)?\s*Consigne", re.I)
CODE = re.compile(r"<code\b[^>]*>.*?</code\s*>", re.S | re.I)


def verbe(mot):
    mot = mot.lower()
    base = re.sub(r"-(?:toi|le|la|les|lui|leur|en|y|moi|nous|vous)$", "", mot)
    return mot in VERBES or base in VERBES


def est_action(segment):
    """le segment commence-t-il par une action (un impératif en tête, ou juste après sa virgule d'ouverture) ?"""
    s = REPERE.sub("", ETIQUETTE.sub("", segment.strip(), count=1)).strip()
    m = TETE.match(s)
    if m and verbe(m.group(1)):
        return True
    # « Pour chaque essai, compare… » : le circonstant d'ouverture, puis le verbe
    m = re.match(r"^[^,:;]{1,60}?[,:]\s*" + MOT, s)
    return bool(m and verbe(m.group(1)))


def verbe_en_tete(segment):
    """le segment commence-t-il directement par un impératif (sans circonstant) ?"""
    m = re.match(r"\s*(?:(?:puis|ensuite|enfin)\s+)?" + MOT, segment, re.I)
    return bool(m and verbe(m.group(1)))


def ecarts_ligne(ligne):
    """[(code, message)] pour une ligne de consigne (texte brut)"""
    out = []
    if len(NUMEROS.findall(ligne)) >= 2:
        out.append(("N1", "deux étapes numérotées sur une ligne"))
    elif len(set(LETTRES.findall(ligne))) >= 2:
        out.append(("N1", "deux étapes a), b)… sur une ligne"))
    segments = [x for x in SEPARATEUR.split(ligne) if x and x.strip()]
    actions = [x for x in segments if est_action(x)]
    # une virgule suivie d'un impératif enchaîne aussi (« ouvre le fichier, regarde la ligne 3 ») ; un circonstant
    # (« Pour chaque essai, compare ») n'en est pas un : seul ce qui SUIT une action compte
    suite = []
    for x in actions:
        parts = re.split(r",\s+", REPERE.sub("", ETIQUETTE.sub("", x.strip(), count=1)).strip())
        i = 0 if verbe_en_tete(parts[0]) else 1
        suite += [y for y in parts[i + 1:] if verbe_en_tete(y)]
    actions = actions + suite
    if len(actions) >= 2 and not out:
        out.append(("N2", "%d actions enchaînées sur une ligne" % len(actions)))
    if not out:
        for x in segments:
            parts = ET.split(x)
            if len(parts) >= 2 and est_action(parts[0]) and any(verbe(re.match(MOT, p.strip(), re.I).group(1))
                                                                 for p in parts[1:] if re.match(MOT, p.strip(), re.I)):
                out.append(("N3", "deux actions jointes par « et »"))
                break
    return out


def consignes(corps):
    """les fragments HTML des consignes de la page, sans doublon ni consigne imbriquée dans une autre"""
    zones = []
    for m in CLASSE_CONSIGNE.finditer(corps):
        jetons = m.group(2).split()
        if any(re.fullmatch(r"(?:[a-z]+-)*consigne(?:-[a-z]+)*", j) for j in jetons):
            zones.append(m.start())
    for m in PARAGRAPHE_CONSIGNE.finditer(corps):
        zones.append(m.start())
    vus, frags = [], []
    for debut in sorted(set(zones)):
        if any(a <= debut < b for a, b in vus):
            continue
        contenu = element(corps, debut)
        fin = corps.index(contenu, debut) + len(contenu) if contenu else debut
        vus.append((debut, fin))
        frags.append(contenu)
    return frags


def lignes(fragment):
    propre = CODE.sub(" «code» ", INVISIBLE.sub(" ", fragment))
    return [t for t in (texte(x) for x in FRONTIERE.split(propre)) if t]


def mesurer(chemin):
    s = open(chemin, encoding="utf-8", errors="ignore").read()
    m = re.search(r"<body\b.*?</body>", s, re.S | re.I)
    corps = re.sub(r"<(script|style|template)\b.*?</\1\s*>", " ", m.group(0) if m else s, flags=re.S | re.I)
    nb, ecarts = 0, []
    for frag in consignes(corps):
        nb += 1
        for ligne in lignes(frag):
            for code, msg in ecarts_ligne(ligne):
                ecarts.append((code, "%s · « %s »" % (msg, ligne[:110] + ("…" if len(ligne) > 110 else ""))))
    return nb, ecarts


def pages_du_site():
    return sorted(p for p in glob.glob("theme-*/**/*.html", recursive=True)
                  if "_archive" not in p and not os.path.basename(p).startswith(("qcm_", "lexique_")))


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    sortie_json = None
    if "--json" in args:
        i = args.index("--json")
        sortie_json = args[i + 1] if i + 1 < len(args) else None
        del args[i:i + 2]
    cibles = [a for a in args if not a.startswith("--")]
    racine = os.getcwd()
    os.chdir(DEPOT)
    pages = [os.path.relpath(os.path.join(racine, c), DEPOT) if not os.path.isabs(c) else c for c in cibles] \
        if cibles else pages_du_site()
    lues, nb_consignes, totaux, releve = 0, 0, {"N1": 0, "N2": 0, "N3": 0}, []
    for p in pages:
        if not os.path.exists(p):
            print("✘ introuvable : " + p)
            continue
        n, e = mesurer(p)
        lues += 1
        nb_consignes += n
        for code, _ in e:
            totaux[code] += 1
        if e:
            releve.append((p, n, e))
    if not lues:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    for p, n, e in sorted(releve, key=lambda r: -sum(1 for c, _ in r[2] if c != "N3")):
        compte = {c: sum(1 for x, _ in e if x == c) for c in totaux}
        print("── %s · %d consigne(s) · N1 %d · N2 %d · N3 %d" % (p, n, compte["N1"], compte["N2"], compte["N3"]))
        if cibles:
            for code, msg in e:
                print("   %s %s %s" % ("⚠" if code == "N3" else "✘", code, msg))
    pages_a_reprendre = sum(1 for _, _, e in releve if any(c != "N3" for c, _ in e))
    print("%d page(s) lues · %d consigne(s) · N1 étapes numérotées sur une ligne : %d · N2 actions enchaînées : %d · "
          "N3 actions jointes par « et » (à juger) : %d · %d page(s) à reprendre"
          % (lues, nb_consignes, totaux["N1"], totaux["N2"], totaux["N3"], pages_a_reprendre))
    if sortie_json:
        with open(os.path.join(racine, sortie_json), "w", encoding="utf-8") as f:
            json.dump({"pages_lues": lues, "consignes": nb_consignes, "totaux": totaux,
                       "pages": [{"page": p, "consignes": n, "ecarts": [{"code": c, "texte": t} for c, t in e]}
                                 for p, n, e in releve]}, f, ensure_ascii=False, indent=1)
    if strict:
        if totaux["N1"] + totaux["N2"]:
            print("✘ une consigne des pages demandées donne plusieurs actions sur une ligne (règle d'or n°342)")
            return 1
        print("✅ chaque consigne des pages demandées donne une action par ligne (règle d'or n°342)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
