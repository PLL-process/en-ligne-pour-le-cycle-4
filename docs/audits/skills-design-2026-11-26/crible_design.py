#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""crible_design.py — les motifs de détection des skills externes de design, joués sur le CODE des pages.

Audit du 26/11/2026 (Pascal : « lancer directement tout sur toutes les séquences »). Les règles viennent des
tableaux « Before you finish » de better-accessibility, better-layout, better-typography, better-writing,
better-ui, des « Web Interface Guidelines » de Vercel et des déclencheurs de review-animations.

Ce crible lit le code, il ne regarde pas la page : une règle qui dépend du rendu est mesurée par
`mesures_rendu.py`, pas ici. Il ne corrige rien. Chaque règle donne le nombre de pages et d'occurrences,
par famille de pages, et quelques exemples `fichier:ligne`.

Usage : python3 crible_design.py <racine du dépôt> [--json sortie.json] [--exemples N]
Code de sortie (n°299) : 0 crible fait · 2 aucune page lue.
"""
import argparse, json, re, sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

NATIFS = {"a", "button", "input", "select", "textarea", "summary", "label", "option", "area", "details", "audio", "video"}
HORS_TEXTE = {"script", "style", "code", "pre", "kbd", "samp", "textarea", "svg", "template", "noscript"}
LIENS_VAGUES = {"ici", "cliquez ici", "clique ici", "cliquer ici", "ce lien", "lien", "en savoir plus", "lire la suite", "voir", "suite"}
EMOJI_SEUL = re.compile(r"^[\W\d_]*$", re.UNICODE)


def famille(nom):
    for prefixe, f in (("synthese_professeur", "synthèse prof"), ("synthese_eleve", "synthèse élève"), ("synthese", "synthèse"),
                       ("sequence", "séquence"), ("qcm", "QCM"), ("lexique", "lexique"), ("atelier", "atelier"), ("tp", "TP")):
        if nom.startswith(prefixe):
            return f
    return "autre"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.styles, self.scripts, self.elements, self.textes = [], [], [], []
        self.pile, self._tampon, self._debut = [], None, None
        self.labels_for, self.ids = set(), set()

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        ligne = self.getpos()[0]
        e = dict(tag=tag, attrs=a, ligne=ligne, texte="", parents=[p["tag"] for p in self.pile], dans_label=any(p["tag"] == "label" for p in self.pile),
                 img_alt=[])
        self.elements.append(e)
        if tag == "label" and a.get("for"):
            self.labels_for.add(a["for"])
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "img":
            for p in self.pile:
                p["img_alt"].append(a.get("alt", ""))
        if tag in ("style", "script"):
            self._tampon, self._debut = [], ligne
        if tag not in ("br", "img", "input", "meta", "link", "hr", "source", "area", "base", "col", "embed", "track", "wbr"):
            self.pile.append(e)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.pile and self.pile[-1]["tag"] == tag and tag not in ("style", "script"):
            self.pile.pop()

    def handle_endtag(self, tag):
        if tag in ("style", "script") and self._tampon is not None:
            (self.styles if tag == "style" else self.scripts).append((self._debut, "".join(self._tampon)))
            self._tampon = None
        for i in range(len(self.pile) - 1, -1, -1):
            if self.pile[i]["tag"] == tag:
                del self.pile[i:]
                break

    def handle_data(self, data):
        if self._tampon is not None:
            self._tampon.append(data)
            return
        for p in self.pile:
            p["texte"] += data
        if data.strip() and not any(p["tag"] in HORS_TEXTE for p in self.pile):
            self.textes.append((self.getpos()[0], data, [p["tag"] for p in self.pile], [p["attrs"].get("class", "") for p in self.pile]))


def regles_css(css, ligne0):
    """Rend (sélecteur, contexte [@règles englobantes], {propriété: valeur}, ligne) pour chaque bloc de déclarations."""
    css = re.sub(r"/\*.*?\*/", lambda m: "\n" * m.group(0).count("\n"), css, flags=re.DOTALL)
    out, pile, i, debut, n = [], [], 0, 0, len(css)
    while i < n:
        c = css[i]
        if c in "\"'":
            j = i + 1
            while j < n and css[j] != c:
                j += 2 if css[j] == "\\" else 1
            i = j + 1
            continue
        if c == "{":
            prelude = css[debut:i].strip()
            ligne = ligne0 + css.count("\n", 0, debut + (len(css[debut:i]) - len(css[debut:i].lstrip())))
            j, prof = i + 1, 1
            # bloc feuille (déclarations) ou bloc conteneur (@media, @supports, @keyframes) ?
            k = i + 1
            feuille = True
            while k < n:
                if css[k] == "{":
                    feuille = False; break
                if css[k] == "}":
                    break
                k += 1
            if feuille:
                corps = css[i + 1:k]
                decl = {}
                for d in corps.split(";"):
                    if ":" in d:
                        p, v = d.split(":", 1)
                        decl[p.strip().lower()] = v.strip().lower()
                out.append((prelude, list(pile), decl, ligne))
                i = k + 1
                debut = i
                continue
            pile.append(prelude)
            i += 1
            debut = i
            continue
        if c == "}":
            if pile:
                pile.pop()
            i += 1
            debut = i
            continue
        if c == ";" and not pile:
            debut = i + 1
        i += 1
    return out


def temps(valeur):
    """Durées (en s) d'une valeur de transition/animation : la première de chaque partie séparée par des virgules."""
    res = []
    for partie in valeur.split(","):
        m = re.search(r"(?<![\w.-])(\d*\.?\d+)(ms|s)\b", partie)
        if m:
            res.append(float(m.group(1)) / (1000 if m.group(2) == "ms" else 1))
    return res


def analyser(chemin, racine):
    texte = chemin.read_text(encoding="utf-8", errors="replace")
    p = Page()
    try:
        p.feed(texte)
    except Exception as e:  # une page illisible se dit, elle ne passe pas pour propre
        return None, f"analyse impossible : {e}"
    rel = str(chemin.relative_to(racine))
    hits = defaultdict(list)

    def note(regle, ligne, extrait):
        hits[regle].append((ligne, " ".join(str(extrait).split())[:110]))

    css = []
    for ligne0, bloc in p.styles:
        css += regles_css(bloc, ligne0)
    for e in p.elements:
        st = e["attrs"].get("style")
        if st:
            decl = {}
            for d in st.split(";"):
                if ":" in d:
                    a, b = d.split(":", 1)
                    decl[a.strip().lower()] = b.strip().lower()
            css.append(("[style]", [], decl, e["ligne"]))
    tout_css = "\n".join(b for _, b in p.styles)
    tout_js = "\n".join(b for _, b in p.scripts)
    reduit = "prefers-reduced-motion" in tout_css or "prefers-reduced-motion" in tout_js
    a_mouvement = False
    lecteur = re.compile(r"lpp|data-des|data-de\b|pas-a-pas|\.anim|keyframes", re.I)

    for sel, ctx, decl, ligne in css:
        contexte = " ".join(ctx).lower()
        dans_keyframes = "@keyframes" in contexte
        tr = decl.get("transition", "")
        an = decl.get("animation", "")
        if tr or an or "transition-duration" in decl or "animation-name" in decl:
            a_mouvement = True
        # --- mouvement (review-animations, Vercel)
        if tr and tr not in ("none", "initial", "unset", "inherit"):
            for partie in tr.split(","):
                jet = partie.split()
                if not jet:
                    continue
                if jet[0] == "all" or re.match(r"^[\d.]+m?s$", jet[0]):
                    note("M1 transition sur toutes les propriétés (« all » dit ou sous-entendu)", ligne, f"{sel} {{ transition: {tr} }}")
                    break
            if re.search(r"\b(width|height|top|left|right|bottom|margin[\w-]*|padding[\w-]*)\b", re.sub(r"max-height|min-height", "", tr)):
                note("M5 transition d'une propriété de mise en page (width, height, top, left, margin, padding)", ligne, f"{sel} {{ transition: {tr} }}")
        if decl.get("transition-property", "") == "all":
            note("M1 transition sur toutes les propriétés (« all » dit ou sous-entendu)", ligne, f"{sel} {{ transition-property: all }}")
        for prop in ("transition", "animation", "transition-timing-function", "animation-timing-function"):
            if re.search(r"\bease-in\b(?!-)", decl.get(prop, "")):
                note("M2 courbe ease-in sur un élément d'interface", ligne, f"{sel} {{ {prop}: {decl[prop]} }}")
        if not dans_keyframes and not lecteur.search(sel):
            d = temps(tr) + temps(decl.get("transition-duration", ""))
            if d and max(d) > 0.3:
                note("M4 transition d'interface de plus de 300 ms (hors lecteur pas à pas)", ligne, f"{sel} {{ transition: {tr or decl.get('transition-duration')} }}")
        if re.search(r"scale\(\s*0\s*\)", decl.get("transform", "")):
            note("M3 entrée depuis scale(0)", ligne, f"{sel} {{ transform: {decl['transform']} }}")
        if "infinite" in an or decl.get("animation-iteration-count", "") == "infinite":
            note("M8 animation en boucle infinie", ligne, f"{sel} {{ animation: {an or 'iteration-count infinite'} }}")
        # --- finitions (better-ui)
        if ":hover" in sel and "hover: hover" not in contexte and "hover:hover" not in contexte.replace(" ", ""):
            note("U1 règle :hover hors de @media (hover: hover)", ligne, sel)
        # --- accessibilité
        if re.match(r"^(none|0)\b", decl.get("outline", "")) or decl.get("outline-style", "") == "none":
            remplace = any(k in decl for k in ("box-shadow", "border", "border-color", "background", "background-color"))
            if not remplace:
                note("A1 outline supprimé sans remplacement dans la même règle", ligne, f"{sel} {{ outline: {decl.get('outline', 'none')} }}")
        # --- typographie
        lh = decl.get("line-height", "")
        if re.search(r"\d(px|rem|pt)\b", lh):
            note("T1 line-height avec une unité fixe (px, rem, pt)", ligne, f"{sel} {{ line-height: {lh} }}")
        if re.search(r"\dpx\b", decl.get("letter-spacing", "")):
            note("T2 letter-spacing en px", ligne, f"{sel} {{ letter-spacing: {decl['letter-spacing']} }}")
        fs = decl.get("font-size", "")
        if re.search(r"\dpx\b", fs) and re.search(r"(^|[\s,}])(html|body|:root)\s*($|[,{])", sel + "{"):
            note("T3 taille du texte de base en px (html, body)", ligne, f"{sel} {{ font-size: {fs} }}")
        m = re.match(r"^(\d*\.?\d+)px", fs)
        if m and float(m.group(1)) < 12:
            note("T8 texte déclaré sous 12 px", ligne, f"{sel} {{ font-size: {fs} }}")
        if decl.get("text-align", "") == "justify":
            note("T5 texte justifié", ligne, sel)
        if decl.get("font-weight", "") in ("100", "200", "300", "lighter"):
            note("T4 graisse fine (100 à 300)", ligne, f"{sel} {{ font-weight: {decl['font-weight']} }}")
        if decl.get("user-select", decl.get("-webkit-user-select", "")) == "none":
            note("T13 user-select: none", ligne, sel)
        # --- mise en page
        for prop, v in decl.items():
            if "100vw" in v and prop in ("width", "min-width", "max-width"):
                note("L1 largeur en 100vw", ligne, f"{sel} {{ {prop}: {v} }}")
            if re.search(r"\b100vh\b", v) and prop in ("height", "min-height", "max-height"):
                note("L2 hauteur en 100vh (100dvh suit la barre du téléphone)", ligne, f"{sel} {{ {prop}: {v} }}")
        if decl.get("flex-direction", "").endswith("-reverse") or re.match(r"^-?\d+$", decl.get("order", "")):
            note("L5 ordre visuel différent de l'ordre du code (order, *-reverse)", ligne, f"{sel} {{ {'order: ' + decl['order'] if 'order' in decl else 'flex-direction: ' + decl.get('flex-direction', '')} }}")

    if a_mouvement and not reduit:
        note("M6 page animée sans « prefers-reduced-motion »", 1, "aucune requête prefers-reduced-motion dans la page")
    a_collant = re.search(r"position\s*:\s*(sticky|fixed)", tout_css)
    if a_collant and 'href="#' in texte and not re.search(r"scroll-(padding|margin)", tout_css):
        note("L4 barre collante sans scroll-padding / scroll-margin (ancres et focus cachés dessous)", 1, "position sticky ou fixed, liens d'ancre, aucun scroll-padding ni scroll-margin")

    # --- éléments
    a_champ = False
    for e in p.elements:
        t, a, ligne = e["tag"], e["attrs"], e["ligne"]
        if "onclick" in a and t not in NATIFS:
            clavier = any(k in a for k in ("onkeydown", "onkeyup", "onkeypress"))
            if not ("tabindex" in a and clavier):
                note("A2 élément cliquable non natif (onclick) sans accès clavier", ligne, f"<{t} onclick=…> tabindex={'oui' if 'tabindex' in a else 'non'} clavier={'oui' if clavier else 'non'}")
        if re.match(r"^[1-9]", a.get("tabindex", "")):
            note("A3 tabindex positif", ligne, f"<{t} tabindex={a['tabindex']}>")
        if t == "img":
            if "alt" not in a:
                note("A4 image sans attribut alt", ligne, a.get("src", "")[-70:])
            if not ("width" in a and "height" in a) and not a.get("src", "").startswith("data:image/svg"):
                note("V1 image sans width ni height (la page saute au chargement)", ligne, a.get("src", "")[-70:])
        if t == "meta" and a.get("name") == "viewport" and re.search(r"user-scalable\s*=\s*no|maximum-scale\s*=\s*1(\.0)?\b", a.get("content", "")):
            note("A5 zoom bloqué dans la balise viewport", ligne, a.get("content"))
        if t in ("input", "select", "textarea") and a.get("type", "text") not in ("hidden", "submit", "button", "reset", "image"):
            a_champ = True
            etiquete = (a.get("id") in p.labels_for) or e["dans_label"] or any(k in a for k in ("aria-label", "aria-labelledby", "title"))
            if not etiquete:
                note("A6 champ sans étiquette (ni label, ni aria-label, ni title)", ligne, f"<{t} type={a.get('type', '')} id={a.get('id', '')} placeholder={a.get('placeholder', '')[:30]}>")
            if t in ("input", "textarea") and a.get("type", "text") in ("text", "number", "search", "") and "autocomplete" not in a:
                note("V6 champ de réponse sans autocomplete (le navigateur propose les réponses déjà tapées sur ce poste)", ligne, f"<{t} id={a.get('id', '')} name={a.get('name', '')}>")
        if "autofocus" in a:
            note("V3 autofocus", ligne, f"<{t}>")
        if a.get("aria-hidden") == "true" and (t in ("a", "button", "input", "select", "textarea") or "tabindex" in a) and a.get("tabindex") != "-1":
            note("A8 aria-hidden sur un élément qui prend le focus", ligne, f"<{t}>")
        if t in ("video", "audio") and "autoplay" in a:
            note("A10 média en lecture automatique", ligne, f"<{t} autoplay>")
    for e in p.elements:
        t, a = e["tag"], e["attrs"]
        nom = " ".join(e["texte"].split())
        if t == "button" or (t == "a" and "href" in a):
            nomme = any(a.get(k) for k in ("aria-label", "aria-labelledby", "title")) or any(e["img_alt"])
            if not nom and not nomme:
                note("A7 bouton ou lien sans nom accessible", e["ligne"], f"<{t} class={a.get('class', '')[:40]} id={a.get('id', '')}>")
            elif nom and EMOJI_SEUL.match(nom) and not nomme:
                note("A7b bouton ou lien nommé par un symbole seul (emoji, flèche), sans aria-label", e["ligne"], f"<{t}>{nom[:20]}</{t}>")
        if t == "a" and nom.lower().strip(" .:→»›") in LIENS_VAGUES:
            note("W1 lien au texte vague (« ici », « en savoir plus »)", e["ligne"], nom[:60])
        if t == "button" and nom.lower().strip(" .!") in ("ok", "oui", "non", "d'accord"):
            note("W2 bouton « OK », « Oui » ou « Non »", e["ligne"], nom)
    if a_champ and not re.search(r"pointer\s*:\s*coarse", tout_css):
        note("T12 page à champs sans la règle « 16 px au toucher » (zoom d'iOS)", 1, "aucun @media (pointer:coarse)")

    # --- textes
    fam = famille(chemin.name)
    eleve = fam not in ("synthèse prof",)
    for ligne, data, parents, classes in p.textes:
        if re.search(r"(?<!\.)\.\.\.(?!\.)", data):
            note("T6 trois points « ... » au lieu de « … »", ligne, data.strip()[:80])
        if re.search(r"\b[Oo]ups\b|[Uu]ne erreur est survenue", data):
            note("W3 message d'erreur sans cause ni remède (« Oups », « Une erreur est survenue »)", ligne, data.strip()[:80])
        if re.search(r"avec succès", data):
            note("W5 « avec succès »", ligne, data.strip()[:80])
        if eleve and re.search(r"\b([Cc]liquez|[Vv]euillez|[Aa]ppuyez|[Ss]électionnez|[Ss]aisissez|[Ee]ntrez votre|[Vv]os réponses|[Vv]otre réponse)\b", data):
            note("W6 vouvoiement dans une page élève (n°302 : « tu »)", ligne, data.strip()[:80])
        if eleve and re.search(r"\b[Cc]lique(r|s)?\b|\bclic\b", data) and not re.search(r"clic droit|double-clic|souris", data, re.I):
            note("W7 « clique » dans une page lue aussi au doigt", ligne, data.strip()[:80])
    # --- scripts
    for ligne0, js in p.scripts:
        for m in re.finditer(r"(?<![\w.$])(alert|confirm|prompt)\s*\(\s*([\"'`])(.{0,90})", js):
            note(f"J1 boîte native {m.group(1)}()", ligne0 + js.count("\n", 0, m.start()), m.group(3))
        if re.search(r"paste[\"']?\s*,[^)]{0,200}preventDefault|onpaste\s*=", js):
            note("V4 collage bloqué", ligne0, "paste + preventDefault")
    return dict(page=rel, famille=fam, hits={k: v for k, v in hits.items()}), None


def principal():
    ap = argparse.ArgumentParser()
    ap.add_argument("racine")
    ap.add_argument("--json", default="")
    ap.add_argument("--exemples", type=int, default=3)
    args = ap.parse_args()
    racine = Path(args.racine)
    pages = sorted(f for f in racine.rglob("*.html")
                   if not any(part.startswith(("_archive", ".git", "node_modules", "_outils", "docs")) for part in f.relative_to(racine).parts))
    if not pages:
        print("PANNE — aucune page lue (code 2)"); return 2
    resultats, pannes = [], []
    for f in pages:
        r, err = analyser(f, racine)
        (resultats.append(r) if r else pannes.append((str(f.relative_to(racine)), err)))
    fams = defaultdict(int)
    for r in resultats:
        fams[r["famille"]] += 1
    print(f"{len(resultats)} pages lues ({', '.join(f'{k} {v}' for k, v in sorted(fams.items(), key=lambda x: -x[1]))}) · {len(pannes)} illisible(s)")
    for f, e in pannes:
        print(f"  ✘ {f} : {e}")
    regles = defaultdict(lambda: dict(pages=0, occurrences=0, familles=defaultdict(int), exemples=[]))
    for r in resultats:
        for regle, liste in r["hits"].items():
            x = regles[regle]
            x["pages"] += 1; x["occurrences"] += len(liste); x["familles"][r["famille"]] += 1
            if len(x["exemples"]) < args.exemples:
                x["exemples"].append(f"{r['page']}:{liste[0][0]} — {liste[0][1]}")
    print(f"\n{'règle':<96} pages   occ.")
    for regle, x in sorted(regles.items()):
        print(f"{regle[:95]:<96} {x['pages']:>5} {x['occurrences']:>6}  [{', '.join(f'{k} {v}' for k, v in sorted(x['familles'].items(), key=lambda y: -y[1]))}]")
    if args.json:
        Path(args.json).write_text(json.dumps(dict(pages=len(resultats), familles=fams, pannes=pannes, regles=regles, detail=resultats),
                                              ensure_ascii=False, indent=1, default=dict), encoding="utf-8")
        print(f"\nDétail écrit : {args.json}")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(principal())
