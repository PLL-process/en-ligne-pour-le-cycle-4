#!/usr/bin/env python3
"""generer_lexique.py — le lexique qui manque à nos séquences est déjà écrit.

LE CONSTAT QUI A DONNÉ CETTE IDÉE
---------------------------------
Une mesure des 41 séquences du dépôt a montré qu'AUCUNE ne porte de lexique.
Et le même jour, une autre mesure a montré que nos 40 QCM portent 1 206
questions, dont 1 206 nomment une NOTION (`n`) et 1 176 portent un « à
retenir » d'une ligne (`ret`) — déjà rédigés, déjà relus, déjà mesurés.

    « La moyenne qui ne décrit personne » → « Une moyenne décrit un milieu,
    pas une personne. »

Ce lexique existe donc. Il est simplement enfermé dans les corrections d'un
QCM, que seul lit l'élève qui se trompe — et jamais celui qui révise.

CE QUE CE SCRIPT FAIT
---------------------
Il ouvre les QCM d'un lot, en extrait les couples (notion, à retenir), les
range par compétence, et écrit une page `lexique_<code>.html` autonome :
imprimable, hors ligne, sans compte, lisible en noir et blanc.

Il n'INVENTE rien. Chaque ligne vient d'un QCM du même lot, mot pour mot. Si
une notion n'a pas de « à retenir », elle est signalée comme telle plutôt que
comblée — un lexique qui bouche ses trous ment sur ce qu'il contient
(règle n°146).

LES MOTS DES SÉANCES (23/09/2026)
---------------------------------
Les notions des QCM ne sont pas les seuls mots qui arrêtent un élève : il y a
aussi ceux du texte même de la séance — « caduc », un terme technique posé
sans explication. Ceux-là, aucun QCM ne les définit.

S'il existe, à côté de la séquence, un fichier `vocabulaire_<lot>.json` :

    [{"mot": "caduc", "formes": ["caduc", "caduque"],
      "definition": "…", "seance": "s1", "source": "TLFi, « caduc »"}]

le lexique s'ouvre sur une section par séance, « 📚 Séance N — les mots de la
séance » (ancre `#seance-sN`, où la séquence renvoie), chaque définition suivie
de sa source ; les notions des QCM suivent, comme avant. Sans ce fichier, la
page est la même qu'avant, octet pour octet.

Les mots de base de la séquence — « objet technique », « système technique » —
se rangent sous `"seance": "ouverture"` : ils doivent figurer dans la zone
d'ouverture de la séquence (tout ce qui précède la barre d'onglets : « Avant de
commencer », situation, problématique…), et le lexique commence alors par
« 🔄 Avant de commencer — les mots de base » (ancre `#ouverture`), dans
l'ordre du fichier — les mots de base en tête —, quand les séances sont rangées
par ordre alphabétique.

Le script REFUSE alors le lot (sortie ≠ 0, le mot nommé, lexique non écrit) :
  · un mot dont aucune forme n'apparaît dans le texte de sa zone — le panneau
    `#sN`, ou l'ouverture —, accents et casse ignorés : on ne définit pas un mot
    absent, et un mot d'ouverture qui ne figure que dans une séance est refusé ;
  · une entrée sans source ;
  · un mot qui est aussi une notion de QCM, avec une autre définition que son
    « à retenir » : l'élève lirait deux vérités pour un même mot.

LE VOCABULAIRE COMMUN (24/09/2026)
----------------------------------
Les mots de base — objet technique, objet naturel, système technique, OST —
reviennent dans chaque lot. Ils sont définis UNE fois, dans
`_outils/vocabulaire_commun.json` ({mot, formes[], definition, source}). Un lot
y renvoie :

    {"mot": "objet technique", "commun": true, "seance": "ouverture",
     "exemple": "Les jumelles de la vigie…"}

et le lexique écrit la définition commune, puis l'exemple du lot, avec la source
commune. REFUS : une entrée « commun » qui redéfinit le mot (`definition` ou
`source` à elle), un mot absent du fichier commun, un mot absent de sa zone.

CE QUE LE SCRIPT N'ÉCRASE PAS (24/09/2026)
------------------------------------------
Régénérer tout le dépôt modifiait 4 lexiques : deux perdaient un `id` posé à la
main (des séquences y renvoient), deux autres, écrits à la main, auraient été
remplacés. Désormais :
  · les ids que des pages visent vivent ICI, dans IDS_POSES ;
  · les lexiques écrits à la main sont exclus par leur nom, dans EXCLUS, avec la
    raison ;
  · et pour tout autre, le script refuse d'écraser un fichier qu'il n'a pas
    produit (sans sa signature), ou qui porte un id qu'il ne reposerait pas — et
    le dit, sortie ≠ 0.

USAGE
    python3 generer_lexique.py <dossier du lot> [autres…]
    python3 generer_lexique.py --tous theme-1-*      # tous les lots d'un thème
"""
import glob
import html
import json
import os
import re
import sys
import unicodedata
from html.parser import HTMLParser

CHAMP = lambda bloc, nom: (
    m.group(1) if (m := re.search(r'"?\b%s"?\s*:\s*"((?:[^"\\]|\\.)*)"' % nom, bloc)) else ""
)
DEBUTS = ["const QUESTIONS = [", "const QUESTIONS=[", "const Q = [", "const Q=["]


def blocs_questions(src):
    """Découpe la banque en blocs `{…}`, en ignorant les accolades des chaînes."""
    for motif in DEBUTS:
        i = src.find(motif)
        if i >= 0:
            deb = i + len(motif) - 1
            break
    else:
        return []
    prof, cur, dans_txt, ech, blocs = 0, "", False, False, []
    for k in range(deb, len(src)):
        ch = src[k]
        if dans_txt:
            cur += ch
            if ech: ech = False
            elif ch == "\\": ech = True
            elif ch == '"': dans_txt = False
            continue
        if ch == '"' and prof:
            dans_txt = True; cur += ch; continue
        if ch == "{": prof += 1
        if prof: cur += ch
        if ch == "}":
            prof -= 1
            if prof == 0:
                blocs.append(cur); cur = ""
        if ch == "]" and prof == 0 and blocs:
            break
    return blocs


def sans_balises(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def cle_tri(t):
    """Tri alphabétique qui ignore les accents et l'article initial."""
    t = re.sub(r"^(l'|la |le |les |un |une |des |d')", "", t.lower())
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if unicodedata.category(c) != "Mn")


#: le bouton « ouvrir le QCM » d'une séquence — un <a class="btn …"> vers un qcm_*.html
BOUTON_QCM = re.compile(r'<a\b[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*href="([^"]*qcm[^"]*\.html)"'
                        r'|<a\b[^>]*href="([^"]*qcm[^"]*\.html)"[^>]*class="[^"]*\bbtn\b', re.I)


def qcm_du_lot(dossier):
    """Les QCM du lot, tels que ses séquences les DÉSIGNENT.

    Première version : tous les `qcm_*.html` du dossier. Sur le Thème 2, le lot
    `4e_C4.7` en porte quatre — le sien plus trois ressources d'entraînement — et
    produisait un lexique de 120 notions. Un lexique de 120 entrées n'est pas un
    outil de révision, c'est un annuaire.

    On suit donc le BOUTON de la séquence : « un seul bouton QCM » est déjà la
    règle d'or n°4, et c'est un fait écrit dans la page, pas une convention de
    nommage à deviner. Les renvois « pour aller plus loin » du bilan, qui ne sont
    pas des boutons, ne comptent pas.

    Repli : s'il n'y a aucune séquence ou aucun bouton, on reprend tous les QCM
    du dossier — mieux vaut un lexique trop large que pas de lexique.
    """
    vises = []
    for s in sorted(glob.glob(os.path.join(dossier, "sequence*.html"))):
        src = open(s, encoding="utf-8", errors="ignore").read()
        for m in BOUTON_QCM.finditer(src):
            cible = m.group(1) or m.group(2)
            chemin = os.path.normpath(os.path.join(dossier, cible))
            if os.path.isfile(chemin) and chemin not in vises:
                vises.append(chemin)
    return vises or sorted(glob.glob(os.path.join(dossier, "qcm_*.html")))


def lire_lot(dossier):
    """Rend {competence: [(notion, a_retenir, fichier), …]} pour un dossier."""
    par_comp = {}
    for f in qcm_du_lot(dossier):
        src = open(f, encoding="utf-8", errors="ignore").read()
        for b in blocs_questions(src):
            n = sans_balises(CHAMP(b, "n"))
            if not n:
                continue
            comp = sans_balises(CHAMP(b, "c")) or "—"
            ret = sans_balises(CHAMP(b, "ret") or CHAMP(b, "t"))
            par_comp.setdefault(comp, []).append((n, ret, os.path.basename(f)))
    return par_comp


GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lexique — {titre}</title>
<style>
  :root{{ --bg:#050f24; --panel:#0d2347; --border:#274a8a; --title:#81aaff;
          --sub:#9bbefc; --head:#c68ef2; --text:#e4eaf5; --hl:#61dafb; }}
  *{{box-sizing:border-box}}
  body{{background:var(--bg);color:var(--text);margin:0;padding:0 16px 60px;line-height:1.55;
       font-family:system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif}}
  h1{{font-size:1.45em;text-align:center;margin:22px 0 4px;color:var(--title)}}
  .sub{{text-align:center;color:var(--sub);margin-bottom:14px;font-size:.95em}}
  main{{max-width:880px;margin:0 auto}}
  section{{background:var(--panel);border:1px solid var(--border);border-radius:14px;
           padding:14px 20px;margin-bottom:16px}}
  h2{{color:var(--head);font-size:1.05em;margin:.2em 0 .6em}}
  dl{{margin:0}}
  dt{{font-weight:700;color:var(--hl);margin-top:.7em}}
  dd{{margin:.15em 0 0 0}}
  dd.vide{{color:var(--sub);font-style:italic}}
  .compte{{color:var(--sub);font-size:.85em}}
  nav a{{color:var(--hl)}}
  footer{{max-width:880px;margin:20px auto 0;color:var(--sub);font-size:.85em;text-align:center}}
{style_vocab}  @media print{{
    body{{background:#fff;color:#000;padding:0}}
    section{{background:#fff;border:1px solid #666;break-inside:avoid}}
    h1,h2,dt{{color:#000}} dd.vide{{color:#444}} nav,footer{{display:none}}
    /* — impression : fond blanc, couleurs conservées (décision de Pascal, 02/09/2026).
       Cette règle vit ICI, dans le générateur : la campagne du 02/09 l'avait écrite dans
       les 59 lexiques engendrés, et la première régénération l'a effacée (règle n°283). — */
    .compte,.sub{{color:#1a6af8}}
{style_vocab_impr}  }}
</style>
</head>
<body>
<nav style="padding-top:12px"><a href="{retour}">← Revenir à la séquence</a></nav>
<h1>📖 Lexique — {titre}</h1>
<p class="sub">{sous_titre} · imprimable · fonctionne hors ligne</p>
<main>
{corps}
</main>
<footer>
{pied}
</footer>
</body>
</html>
"""

# overflow-wrap : une source porte souvent son adresse web, d'un seul tenant ; sans coupure,
# elle élargissait la page à 543 px sur un téléphone de 390 (mesuré sur 3e_C1.1, 23/09/2026).
STYLE_VOCAB = ("  small.source{display:block;color:var(--sub);font-size:.8em;margin-top:.1em;"
               "overflow-wrap:anywhere}\n")
STYLE_VOCAB_IMPR = "    small.source{color:#444}\n"
SOUS_TITRE = "{compte} notions, tirées mot pour mot des QCM du lot"
PIED = ("  Chaque ligne provient d'une question de {sources}. Rien n'a été réécrit ici :\n"
        "  ce lexique rassemble ce que les corrections disaient déjà, une par une.")
PIED_VOCAB = ("  Les mots des séances viennent de {fichier} : chacun porte sa source, et chacun\n"
              "  figure dans le texte de sa séance (ou de l'ouverture, pour les mots de base).\n"
              "  Les notions viennent mot pour mot des QCM ({sources}) : rien n'a été réécrit ici,\n"
              "  ce lexique rassemble ce que les corrections disaient déjà, une par une.")


#: ids d'ancre qu'une page vise — {lot: {notion: id}}. Posés d'abord à la main dans le lexique,
#: ils sautaient à chaque régénération : le lien arrivait en haut de page, sans erreur.
IDS_POSES = {
    # visé par 3e_C1.1 (rappel « pas encore sûr·e ? »)
    "4e_C1.1": {"Justifier une évolution": "justifier-une-evolution"},
    # visé par 3e_C1.5 (rappel « pas encore sûr·e ? »)
    "4e_C1.4": {"Reconnaître une donnée personnelle": "reconnaitre-une-donnee-personnelle"},
}

#: lexiques écrits à la main, que le script ne régénère jamais — {lot: raison}
EXCLUS = {
    lot: "écrit à la main le 30/08/2026 (tableau « Mot / Ce qu'il veut dire », définitions "
         "rédigées) : le générateur y mettrait les « à retenir » du QCM à la place "
         "(journal du 09/09/2026, règle n°279). Pour le faire rentrer dans le rang, faire entrer "
         "ses définitions dans un vocabulaire_%s.json, pas l'effacer." % lot
    for lot in ("3e_C8.1", "5e_C8.1")
}

#: ce qui signe une page produite par ce script (pied de page, sans ou avec vocabulaire)
SIGNATURES = ("Chaque ligne provient d'une question de", "Les notions viennent mot pour mot des QCM")

OUVERTURE = "ouverture"

#: les mots de base, définis une fois pour tous les lots
CHEMIN_COMMUN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vocabulaire_commun.json")


class RefusVocabulaire(Exception):
    """Une entrée de vocabulaire_<lot>.json que le lexique ne peut pas publier."""


class LexiqueProtege(Exception):
    """Un lexique que le script ne doit pas écraser. `exclu` : exception nommée (non fautive)."""
    def __init__(self, msg, exclu=False):
        super().__init__(msg)
        self.exclu = exclu


def pli(t):
    """Texte comparable : sans accents, minuscules, apostrophes et espaces unifiés."""
    t = "".join(c for c in unicodedata.normalize("NFD", t.lower())
                if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", t.replace("’", "'")).strip()


class _TextePanneau(HTMLParser):
    """Recueille le texte de l'élément `id=cible` et de tout ce qu'il contient."""
    VIDES = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
             "param", "source", "track", "wbr"}

    def __init__(self, cible):
        super().__init__(convert_charrefs=True)
        self.cible, self.prof, self.trouve, self.muet, self.morceaux = cible, 0, False, 0, []

    def handle_starttag(self, tag, attrs):
        if tag in self.VIDES:
            return
        if self.prof:
            self.prof += 1
        elif not self.trouve and dict(attrs).get("id") == self.cible:
            self.prof, self.trouve = 1, True
        if self.prof and tag in ("script", "style"):
            self.muet += 1

    def handle_endtag(self, tag):
        if tag in self.VIDES or not self.prof:
            return
        if tag in ("script", "style") and self.muet:
            self.muet -= 1
        self.prof -= 1

    def handle_data(self, data):
        if self.prof and not self.muet:
            self.morceaux.append(data)


def texte_panneau(src, cible):
    """Le texte du panneau `#cible` d'une séquence, ou None s'il n'existe pas."""
    p = _TextePanneau(cible)
    p.feed(src)
    return " ".join(p.morceaux) if p.trouve else None


class _TexteOuverture(HTMLParser):
    """Recueille le texte du <body> jusqu'à la barre d'onglets (role="tablist"), hors <nav>."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.corps, self.fini, self.barre, self.muet, self.morceaux = False, False, False, 0, []

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.corps = True
        elif self.corps and not self.fini and dict(attrs).get("role") == "tablist":
            self.fini = self.barre = True
        elif tag in ("script", "style", "nav") and tag not in _TextePanneau.VIDES:
            self.muet += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav") and self.muet:
            self.muet -= 1

    def handle_data(self, data):
        if self.corps and not self.fini and not self.muet:
            self.morceaux.append(data)


def texte_ouverture(src):
    """Le texte de la zone d'ouverture (avant la barre d'onglets), ou None sans barre d'onglets."""
    p = _TexteOuverture()
    p.feed(src)
    return " ".join(p.morceaux) if p.barre else None


def lire_commun(chemin=None):
    """{mot plié: entrée} du vocabulaire commun ; {} s'il n'existe pas. Chaque entrée y est
    complète (mot, définition, source), sinon RefusVocabulaire."""
    chemin = chemin or CHEMIN_COMMUN
    if not os.path.isfile(chemin):
        return {}
    nom = os.path.basename(chemin)
    try:
        entrees = json.load(open(chemin, encoding="utf-8"))
    except ValueError as e:
        raise RefusVocabulaire("%s illisible : %s" % (nom, e))
    commun = {}
    for e in entrees if isinstance(entrees, list) else [None]:
        if not isinstance(e, dict) or not all(sans_balises(str(e.get(k) or "")) for k in
                                              ("mot", "definition", "source")):
            raise RefusVocabulaire("%s : chaque entrée porte mot, définition et source (%r)" % (nom, e))
        commun[pli(e["mot"])] = e
    return commun


def lire_vocabulaire(dossier, code, retour, par_comp, commun=None):
    """Lit vocabulaire_<code>.json s'il existe ; rend (nom du fichier, {n° de séance: [entrées]}).

    La clé 0 porte les mots de l'ouverture. Une entrée `"commun": true` prend sa définition
    et sa source dans le vocabulaire commun, et y ajoute son `exemple`. Lève RefusVocabulaire
    au premier défaut, en nommant le mot."""
    nom = "vocabulaire_%s.json" % code
    chemin = os.path.join(dossier, nom)
    if not os.path.isfile(chemin):
        return None, {}
    try:
        entrees = json.load(open(chemin, encoding="utf-8"))
    except ValueError as e:
        raise RefusVocabulaire("%s illisible : %s" % (nom, e))
    if not isinstance(entrees, list):
        raise RefusVocabulaire("%s doit être une liste d'entrées" % nom)
    src = open(os.path.join(dossier, retour), encoding="utf-8", errors="ignore").read()
    rets = {}
    for lignes in par_comp.values():
        for n, ret, _ in lignes:
            rets.setdefault(pli(n), set()).add(ret)
    panneaux, par_seance = {}, {}
    for e in entrees:
        mot = str(e.get("mot") or "").strip() if isinstance(e, dict) else ""
        if not mot:
            raise RefusVocabulaire("%s : une entrée sans « mot »" % nom)
        if e.get("commun"):
            if e.get("definition") or e.get("source"):
                raise RefusVocabulaire("« %s » renvoie au vocabulaire commun et le redéfinit : une "
                                       "entrée « commun » ne porte ni definition ni source, seulement "
                                       "son exemple" % mot)
            if commun is None:
                commun = lire_commun()
            c = commun.get(pli(mot))
            if c is None:
                raise RefusVocabulaire("« %s » renvoie au vocabulaire commun, qui ne le contient pas "
                                       "(%s)" % (mot, os.path.basename(CHEMIN_COMMUN)))
            exemple = sans_balises(str(e.get("exemple") or ""))
            e = dict(e, definition=(sans_balises(c["definition"]) + " " + exemple).strip(),
                     source=c["source"], formes=e.get("formes") or c.get("formes") or [mot])
        definition = sans_balises(str(e.get("definition") or ""))
        source = sans_balises(str(e.get("source") or ""))
        seance = str(e.get("seance") or "").strip()
        if not definition:
            raise RefusVocabulaire("« %s » : pas de définition" % mot)
        if not source:
            raise RefusVocabulaire("« %s » : pas de source — une définition non sourcée "
                                   "n'entre pas au lexique" % mot)
        m = re.fullmatch(r"s(\d+)", seance)
        if not m and seance != OUVERTURE:
            raise RefusVocabulaire("« %s » : séance %r, attendu \"ouverture\", \"s1\", \"s2\"…"
                                   % (mot, seance))
        zone = "l'ouverture" if seance == OUVERTURE else "#" + seance
        if seance not in panneaux:
            t = texte_ouverture(src) if seance == OUVERTURE else texte_panneau(src, seance)
            panneaux[seance] = None if t is None else pli(t)
        texte = panneaux[seance]
        if texte is None:
            raise RefusVocabulaire("« %s » : la séquence %s n'a pas %s" % (
                mot, retour, "de barre d'onglets, donc pas de zone d'ouverture"
                if seance == OUVERTURE else "de panneau #" + seance))
        formes = [str(f) for f in (e.get("formes") or [mot])]
        if not any(re.search(r"(?<![a-z0-9])%s(?![a-z0-9])" % re.escape(pli(f)), texte)
                   for f in formes if pli(f)):
            raise RefusVocabulaire("« %s » : aucune de ses formes (%s) n'apparaît dans le "
                                   "texte de %s" % (mot, ", ".join(formes), zone))
        autres = rets.get(pli(mot), set()) - {definition}
        if autres:
            raise RefusVocabulaire("« %s » est aussi une notion du QCM, et sa définition diffère "
                                   "de son « à retenir » : %r" % (mot, sorted(autres)[0]))
        par_seance.setdefault(int(m.group(1)) if m else 0, []).append((mot, definition, source))
    return nom, par_seance


def sections_vocabulaire(par_seance):
    """L'ouverture (<section id="ouverture">), puis une <section id="seance-sN"> par séance ;
    dans chaque séance, les mots dans l'ordre alphabétique.

    L'ouverture, elle, garde l'ORDRE DU FICHIER (Pascal, 24/09/2026) : ses mots de base —
    objet technique, objet naturel, système technique, OST — doivent venir en tête, et
    l'alphabet mettait « ADEME » devant eux."""
    corps = []
    for num in sorted(par_seance):
        mots = par_seance[num] if num == 0 else sorted(par_seance[num], key=lambda x: cle_tri(x[0]))
        lignes = ["  <dt>%s</dt>\n  <dd>%s <small class=\"source\">Source : %s</small></dd>"
                  % (html.escape(mot), html.escape(d), html.escape(s))
                  for mot, d, s in mots]
        ancre, titre = (("ouverture", "🔄 Avant de commencer — les mots de base") if num == 0 else
                        ("seance-s%d" % num, "📚 Séance %d — les mots de la séance" % num))
        corps.append("<section id=\"%s\">\n <h2>%s "
                     "<span class=\"compte\">· %d mot%s</span></h2>\n <dl>\n%s\n </dl>\n</section>"
                     % (ancre, titre, len(lignes), "s" if len(lignes) > 1 else "", "\n".join(lignes)))
    return corps


def garde_ecrasement(sortie, page):
    """Refuse d'écraser un lexique que ce script n'a pas produit, ou dont il perdrait un id."""
    if not os.path.isfile(sortie):
        return
    ancien = open(sortie, encoding="utf-8", errors="ignore").read()
    nom = os.path.basename(sortie)
    if not any(sig in ancien for sig in SIGNATURES):
        raise LexiqueProtege("%s n'a pas été produit par ce script (sa signature manque) : "
                             "écrit à la main ? Il n'est pas écrasé. Pour l'exclure, l'inscrire "
                             "dans EXCLUS avec la raison." % nom)
    perdus = sorted(set(re.findall(r'<dt id="([^"]+)"', ancien)) - set(re.findall(r'<dt id="([^"]+)"', page)))
    if perdus:
        raise LexiqueProtege("%s porte un id posé à la main que la régénération effacerait (%s) : "
                             "l'inscrire dans IDS_POSES." % (nom, ", ".join(perdus)))


def ecrire_lexique(dossier, titre, retour, commun=None):
    code = re.sub(r"[^A-Za-z0-9._-]", "_", titre)[:60]
    if code in EXCLUS:
        raise LexiqueProtege(EXCLUS[code], exclu=True)
    ids_poses = IDS_POSES.get(code, {})
    par_comp = lire_lot(dossier)
    total = sum(len(v) for v in par_comp.values())
    if not total:
        return None
    corps, sources = [], set()
    for comp in sorted(par_comp):
        vus, lignes = set(), []
        for n, ret, f in sorted(par_comp[comp], key=lambda x: cle_tri(x[0])):
            if n in vus:
                continue
            vus.add(n); sources.add(f)
            dt = "<dt id=\"%s\">" % ids_poses[n] if n in ids_poses else "<dt>"
            if ret:
                lignes.append("  %s%s</dt>\n  <dd>%s</dd>"
                              % (dt, html.escape(n), html.escape(ret)))
            else:
                lignes.append("  %s%s</dt>\n  <dd class=\"vide\">"
                              "(cette question ne porte pas de « à retenir » — à écrire)</dd>"
                              % (dt, html.escape(n)))
        corps.append("<section>\n <h2>%s <span class=\"compte\">· %d notions</span></h2>\n"
                     " <dl>\n%s\n </dl>\n</section>"
                     % (html.escape(comp), len(vus), "\n".join(lignes)))
    fichier_vocab, par_seance = lire_vocabulaire(dossier, code, retour, par_comp, commun)
    sources = ", ".join(sorted(sources))
    if fichier_vocab:
        nb = sum(len(v) for v in par_seance.values())
        page = GABARIT.format(
            titre=html.escape(titre), retour=html.escape(retour),
            style_vocab=STYLE_VOCAB, style_vocab_impr=STYLE_VOCAB_IMPR,
            sous_titre="%d mot%s %s, puis %s" % (
                nb, "s" if nb > 1 else "",
                "de l'ouverture et des séances" if 0 in par_seance else "des séances",
                SOUS_TITRE.format(compte=total)),
            corps="\n".join(sections_vocabulaire(par_seance) + corps),
            pied=PIED_VOCAB.format(fichier=html.escape(fichier_vocab), sources=sources))
    else:
        page = GABARIT.format(titre=html.escape(titre), retour=html.escape(retour),
                              style_vocab="", style_vocab_impr="",
                              sous_titre=SOUS_TITRE.format(compte=total),
                              corps="\n".join(corps), pied=PIED.format(sources=sources))
    sortie = os.path.join(dossier, "lexique_%s.html" % code)
    garde_ecrasement(sortie, page)
    open(sortie, "w", encoding="utf-8").write(page)
    return sortie, total


def page_de_retour(dossier):
    """Vers quelle page le lexique doit-il ramener l'élève ?

    La séquence du lot, quand le lot en porte une. Mais un lot peut vivre autour
    d'une ressource **mutualisée** : les trois lots de l'atelier CAO n'ont pas de
    séquence propre, ils tournent autour d'un TP commun, dont chaque dossier de
    code porte la page de renvoi (`tp_*.html`).

    La première version ne cherchait que `sequence*.html` et, faute d'en trouver,
    **sautait le dossier en silence** : le lexique n'était pas écrit, et rien ne
    le disait. Un outil qui ne trouve pas sa cible doit le dire, pas s'abstenir
    (règle d'or n°183).
    """
    for motif in ("sequence*.html", "tp_*.html"):
        trouves = sorted(glob.glob(os.path.join(dossier, motif)))
        if trouves:
            return os.path.basename(trouves[0])
    return ""


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tous = "--tous" in sys.argv
    dossiers = []
    for a in args:
        if tous:
            dossiers += sorted({os.path.dirname(f)
                                for f in glob.glob(a + "/**/sequence*.html", recursive=True)})
        else:
            dossiers.append(a)
    refus = 0
    for d in dossiers:
        titre = os.path.basename(d)
        retour = page_de_retour(d)
        if not retour:
            print("%-58s  ni séquence ni TP dans ce dossier — NON GÉNÉRÉ" % titre[:56])
            continue
        try:
            r = ecrire_lexique(d, titre, retour)
        except RefusVocabulaire as e:
            print("%-58s  REFUSÉ — %s" % (titre[:56], e))
            refus += 1
            continue
        except LexiqueProtege as e:
            if e.exclu:
                print("%-58s  EXCLU — %s" % (titre[:56], e))
            else:
                print("%-58s  REFUSÉ — %s" % (titre[:56], e))
                refus += 1
            continue
        if r:
            print("%-58s %3d notions → %s" % (titre[:56], r[1], os.path.basename(r[0])))
        else:
            print("%-58s  aucun QCM lisible dans ce dossier — NON GÉNÉRÉ" % titre[:56])
    if refus:
        print("\n%d lexique(s) refusé(s) : rien n'a été écrit pour eux." % refus)
        sys.exit(1)
