#!/usr/bin/env python3
"""audit_aeration.py — le texte que lit l'élève est-il aéré ? (08/11/2026, skill `texte-clair-et-aere`)

Pascal, le 08/11/2026 : « des skills qui ordonnent et aèrent mieux certains paragraphes, notamment quant aux textes
au-dessous des images ; bien souvent un retour à la ligne est nécessaire, dans les corrections, etc. »

CE QUI EST MESURÉ, dans le texte des pages (sans navigateur) :
  L1  légende-bloc        une légende (<figcaption>) de plus de 35 mots d'un seul tenant, sans retour à la ligne ;
  L2  légende-collée      dans une légende, une partie qui devrait commencer une ligne la suit sans retour :
                          « Puis : », la note en italique, la mention « Image générée par IA », un repère ②, ③… ;
  C1  correction-bloc     dans une correction (classes correction, correction-bloc, corrige-bonus, feedback), un
                          bloc de plus de 45 mots d'un seul tenant ;
  C2  correction-cousue   dans une correction, un bloc où deux « ; » ou plus cousent des idées, ou qui enchaîne
                          plus de trois « → » ou « · » : chaque idée veut sa ligne. Une ligne de vérification
                          (« objet → critère ✔ → critère ✘ → verdict ») est exemptée : elle se lit comme un tableau.
Un « bloc » est le texte entre deux frontières : début ou fin d'un paragraphe, d'un item de liste, d'une cellule de
tableau, d'un titre, ou un <br>. Les tableaux sont donc lus cellule par cellule.

Usage :
  python3 _outils/audit_aeration.py                     # tout le site : le relevé par page, puis les totaux
  python3 _outils/audit_aeration.py <page.html>…        # quelques pages, chaque écart cité
  python3 _outils/audit_aeration.py --strict <page>…    # sortie 1 s'il reste un écart dans ces pages (pages pilotes)
Sans --strict, c'est une mesure (sortie 0) ; sortie 2 si aucune page n'a pu être lue (n°299).
"""
import glob
import html
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEUIL_LEGENDE, SEUIL_CORRECTION = 35, 45
FRONTIERE = re.compile(r"<br\s*/?>|</?(?:p|li|td|th|tr|h[1-6]|div|ul|ol|dl|dt|dd|table|summary|details|figure)\b[^>]*>", re.I)
CLASSES_CORRECTION = re.compile(r'class="[^"]*\b(correction|correction-bloc|corrige-bonus|feedback)\b')


def texte(fragment):
    t = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


# un schéma SVG (son <title>, son <desc> : ce que lit un lecteur d'écran), un script, une feuille de style ne sont pas
# du texte qui s'affiche en paragraphe : ils ne comptent pas (08/11/2026, révision des trois thèmes — la description
# d'une carte mentale dans une correction comptait 197 mots « d'un seul tenant »)
INVISIBLE = re.compile(r"<(svg|script|style|template)\b.*?</\1\s*>", re.S | re.I)


def blocs(fragment):
    return [b for b in (texte(x) for x in FRONTIERE.split(INVISIBLE.sub(" ", fragment))) if b]


def mots(t):
    return len(t.split())


def element(s, debut):
    """le contenu de l'élément ouvert en `debut`, imbrications comprises (div dans div)"""
    m = re.match(r"<(\w+)", s[debut:])
    nom = m.group(1).lower()
    profondeur, i = 0, debut
    motif = re.compile(r"<(/?)%s\b[^>]*>" % nom, re.I)
    for t in motif.finditer(s, debut):
        profondeur += -1 if t.group(1) else 1
        if profondeur == 0:
            return s[s.index(">", debut) + 1:t.start()]
    return s[s.index(">", debut) + 1:]


def legende_collee(cap):
    """les parties d'une légende qui devraient ouvrir une ligne et suivent du texte sans retour"""
    ecarts = []
    # la note en italique est celle qui FINIT la légende (« <i>5E1 est un exemple.</i> ») ; un mot en italique au
    # milieu d'une phrase n'est pas une note
    marqueurs = [(r"<b>\s*Puis(?:&nbsp;|\s)*:", "« Puis : »"),
                 (r"<i\b[^>]*>(?:(?!</?i\b).)*Image générée par IA", "la mention « Image générée par IA »"),
                 (r"<i\b[^>]*>(?:(?!</?i\b)(?!Image générée par IA).)*</i>\s*$", "la note en italique"),
                 (r"(?<![①②③④⑤⑥⑦⑧⑨])[②③④⑤⑥⑦⑧⑨](?:&nbsp;|\s)*[A-Za-zÀ-ÿ«(<]", "un repère numéroté")]
    cap = cap.strip()
    for motif, nom in marqueurs:
        for m in re.finditer(motif, cap, re.S):
            avant = cap[:m.start()]
            dernier = max(avant.rfind("<br"), 0)
            if texte(avant[dernier:]):
                ecarts.append(nom)
                break
    return ecarts


def mesurer(chemin):
    s = open(chemin, encoding="utf-8", errors="ignore").read()
    ecarts = []
    for m in re.finditer(r"<figcaption\b[^>]*>(.*?)</figcaption>", s, re.S | re.I):
        cap = m.group(1)
        for b in blocs(cap):
            if mots(b) > SEUIL_LEGENDE:
                ecarts.append(("L1", "%d mots d'un seul tenant · « %s… »" % (mots(b), b[:70])))
        for nom in legende_collee(cap):
            ecarts.append(("L2", "%s suit le texte sans retour · « %s… »" % (nom, texte(cap)[:60])))
    for m in re.finditer(r"<(div|p|section|details|aside)\b[^>]*%s[^>]*>" % CLASSES_CORRECTION.pattern[0:], s):
        contenu = element(s, m.start())
        for b in blocs(contenu):
            if mots(b) > SEUIL_CORRECTION:
                ecarts.append(("C1", "%d mots d'un seul tenant · « %s… »" % (mots(b), b[:70])))
            # une ligne de vérification (« objet → critère ✔ → critère ✘ → verdict ») se lit comme une ligne de
            # tableau : ses flèches sont voulues
            elif b.count(";") >= 2 or ((b.count("→") > 3 or b.count(" · ") > 3) and not re.search("[✔✘]", b)):
                ecarts.append(("C2", "idées cousues (« ; », « → » ou « · ») · « %s… »" % b[:70]))
    return ecarts


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    cibles = [a for a in args if not a.startswith("--")]
    os.chdir(DEPOT)
    if cibles:
        pages = cibles
    else:
        pages = sorted(p for p in glob.glob("theme-*/**/*.html", recursive=True)
                       if "_archive" not in p and not os.path.basename(p).startswith(("qcm_", "lexique_")))
    lues, totaux, par_page = 0, {"L1": 0, "L2": 0, "C1": 0, "C2": 0}, []
    for p in pages:
        if not os.path.exists(p):
            print("✘ introuvable : " + p)
            continue
        e = mesurer(p)
        lues += 1
        for code, _ in e:
            totaux[code] += 1
        if e:
            par_page.append((len(e), p, e))
    if not lues:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    detail = bool(cibles)
    for n, p, e in sorted(par_page, reverse=True):
        compte = {c: sum(1 for x, _ in e if x == c) for c in totaux}
        print("── %s · L1 %d · L2 %d · C1 %d · C2 %d" % (p, compte["L1"], compte["L2"], compte["C1"], compte["C2"]))
        if detail:
            for code, msg in e:
                print("   ✘ %s %s" % (code, msg))
    print("%d page(s) lues · L1 légende-bloc : %d · L2 légende-collée : %d · C1 correction-bloc : %d · C2 correction-cousue : %d"
          % (lues, totaux["L1"], totaux["L2"], totaux["C1"], totaux["C2"]))
    if strict:
        if sum(totaux.values()):
            print("✘ texte à aérer dans les pages demandées")
            return 1
        print("✅ chaque légende et chaque correction des pages demandées est aérée")
    return 0


if __name__ == "__main__":
    sys.exit(main())
