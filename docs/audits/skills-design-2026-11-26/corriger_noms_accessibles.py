#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""corriger_noms_accessibles.py — donne un nom aux champs et aux boutons que le crible a trouvés sans nom.

Audit du 26/11/2026 (better-accessibility : « A placeholder is never a label »). Ne change RIEN de ce que voit
l'élève : seuls des attributs sont ajoutés (`for`, `id`, `aria-label`, `aria-labelledby`, `role`, `tabindex`).

  1. `<label>…</label><input id="x">` sur la même ligne, sans `for` : le label reçoit `for="x"`.
  2. Champ seul sous sa question (`<p>…</p>` à la ligne d'avant) : le paragraphe reçoit un `id`, le champ `aria-labelledby`.
  3. Champ d'un tableau de relevé : `aria-label` = « en-tête de colonne — libellé de la ligne ».
  4. Bouton « ▶ » d'un banc d'essai : `aria-label` = « Lancer le test <libellé de la ligne> ».
  5. Croix de fermeture en `<span onclick>` : `role="button"`, `tabindex="0"`, `aria-label="Fermer"`, Entrée et Espace.

Usage : python3 corriger_noms_accessibles.py <racine> <crible.json> [--ecrire]
Sans --ecrire, rien n'est écrit : le script dit ce qu'il ferait. Code de sortie : 0 fait · 1 des cas restent · 2 panne.
"""
import html, json, re, sys
from pathlib import Path

BALISE = re.compile(r"<[^>]+>")

# Champs sans texte voisin qui puisse servir d'étiquette : le nom est écrit ici, à la main.
PARTICULIERS = {"tp_mbot2_python.html": {"q4": "Nombre de secondes de la pause", "q5a": "Valeur de speed", "q5b": "Valeur de run_time"}}


def clair(s):
    return " ".join(html.unescape(BALISE.sub(" ", s)).split()).strip(" :")


def attr(s):
    return html.escape(s, quote=True)[:160]


def nomme(balise):
    return re.search(r'\b(aria-label|aria-labelledby|title)\s*=', balise) is not None


def cellules(s):
    return re.findall(r"<t[dh]\b[^>]*>.*?</t[dh]>", s, flags=re.DOTALL)


def corriger(chemin, lignes_a6, lignes_a7b, lignes_a2, ecrire):
    texte = chemin.read_text(encoding="utf-8")
    L = texte.split("\n")
    fors = set(re.findall(r'<label\b[^>]*\bfor="([^"]+)"', texte))
    faits, restes = [], []

    for n in sorted(set(lignes_a6)):
        i = n - 1
        ligne = L[i]
        avant = ligne
        # 1. label sans for, sur la même ligne
        m = re.search(r"<label>((?:(?!</label>).)*)</label>\s*<input\b([^>]*)\bid=\"([^\"]+)\"", ligne)
        if m and m.group(3) not in fors:
            ligne = ligne.replace("<label>" + m.group(1) + "</label>", f'<label for="{m.group(3)}">' + m.group(1) + "</label>", 1)
            fors.add(m.group(3))
        # 3. champ d'un tableau
        if "<td" in ligne or "</td>" in ligne:
            j = i
            while j > 0 and "<tr" not in L[j] and i - j < 8:
                j -= 1
            rang = "\n".join(L[j:i + 1])
            cel = cellules(rang[rang.find("<tr"):] if "<tr" in rang else rang)
            k = j - 1
            entetes = []
            while k >= 0 and "<table" not in L[k] and j - k < 40:
                if "<th" in L[k] and "<input" not in L[k]:
                    entetes = [clair(c) for c in cellules(L[k])]
                    break
                k -= 1
            def nommer(mo):
                balise = mo.group(0)
                ident = re.search(r'\bid="([^"]+)"', balise)
                if nomme(balise) or (ident and ident.group(1) in fors) or re.search(r'type="(hidden|submit|button)"', balise):
                    return balise
                idx = next((x for x, c in enumerate(cel) if balise in c), None)
                rangee = clair(cel[0]) if cel and idx not in (None, 0) and "<input" not in cel[0] else ""
                col = entetes[idx] if idx is not None and idx < len(entetes) else ""
                nom = " — ".join(x for x in (col, rangee) if x)
                return balise if not nom else balise.replace("<input", f'<input aria-label="{attr(nom)}"', 1)
            ligne = re.sub(r"<(?:input|select|textarea)\b[^>]*>", nommer, ligne)
        # 2. champ seul sous sa question
        m = re.match(r"^(\s*)<(input|textarea|select)\b([^>]*)>\s*$", ligne)
        if m and not nomme(ligne):
            ident = re.search(r'\bid="([^"]+)"', ligne)
            k = i - 1
            while k >= 0 and not L[k].strip():
                k -= 1
            # la question peut tenir sur plusieurs lignes : remonter jusqu'à son <p
            d = k
            if k >= 0 and L[k].rstrip().endswith("</p>"):
                while d > 0 and not re.match(r"^\s*<p\b", L[d]) and k - d < 8:
                    d -= 1
            p = re.match(r"^(\s*)<p\b([^>]*)>", L[d]) if k >= 0 and L[k].rstrip().endswith("</p>") else None
            lab = re.match(r"^(\s*)<label>(.*)</label>\s*$", L[k]) if k >= 0 else None
            if ident and ident.group(1) not in fors and lab:
                L[k] = L[k].replace("<label>", f'<label for="{ident.group(1)}">', 1)
                fors.add(ident.group(1)); faits.append((n, "label de la ligne d'avant"))
            elif ident and ident.group(1) not in fors and p and clair("\n".join(L[d:k + 1])):
                pid = re.search(r'\bid="([^"]+)"', p.group(2))
                if not pid:
                    nouvel = "lib-" + ident.group(1)
                    L[d] = L[d].replace("<p", f'<p id="{nouvel}"', 1)
                else:
                    nouvel = pid.group(1)
                ligne = ligne.replace(f"<{m.group(2)}", f'<{m.group(2)} aria-labelledby="{nouvel}"', 1)
        for ident, nom in PARTICULIERS.get(chemin.name, {}).items():
            cible = f'id="{ident}"'
            if cible in ligne and "aria-label" not in ligne.split(cible)[0].rsplit("<", 1)[-1] + ligne.split(cible)[1].split(">", 1)[0]:
                ligne = ligne.replace(cible, f'{cible} aria-label="{attr(nom)}"', 1)
        if ligne != avant:
            L[i] = ligne
            faits.append((n, "champ"))
        if re.search(r"<(input|select|textarea)\b(?![^>]*(aria-label|aria-labelledby|title)=)[^>]*>", ligne):
            sans = [b for b in re.findall(r"<(?:input|select|textarea)\b[^>]*>", ligne)
                    if not nomme(b) and not ((re.search(r'\bid="([^"]+)"', b) or [None, None])[1] in fors) and 'type="hidden"' not in b]
            if sans:
                restes.append((n, sans[0][:90]))

    for n in sorted(set(lignes_a7b)):
        i = n - 1
        cel = cellules(L[i])
        def nommer_bouton(mo):
            b = mo.group(0)
            if nomme(b) or not cel:
                return b
            return b.replace("<button", f'<button aria-label="{attr("Lancer le test " + clair(cel[0]))}"', 1)
        nouvelle = re.sub(r"<button\b[^>]*>(?=\s*▶\s*</button>)", nommer_bouton, L[i])
        if nouvelle != L[i]:
            L[i] = nouvelle; faits.append((n, "bouton ▶"))
        else:
            restes.append((n, L[i].strip()[:90]))

    for n in sorted(set(lignes_a2)):
        i = n - 1
        nouvelle = re.sub(r'<span class="close" onclick=',
                          '<span class="close" role="button" tabindex="0" aria-label="Fermer" '
                          'onkeydown="if(event.key===\'Enter\'||event.key===\' \'){event.preventDefault();this.click();}" onclick=', L[i], count=1)
        if nouvelle != L[i] and 'role="button"' not in L[i]:
            L[i] = nouvelle; faits.append((n, "croix de fermeture"))
        else:
            restes.append((n, L[i].strip()[:90]))

    if ecrire and faits:
        chemin.write_text("\n".join(L), encoding="utf-8")
    return faits, restes


def principal():
    if len(sys.argv) < 3:
        print(__doc__); return 2
    racine, crible = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    ecrire = "--ecrire" in sys.argv
    total, reste = 0, 0
    for r in crible["detail"]:
        a6 = [l for k, v in r["hits"].items() if k.startswith("A6") for l, _ in v]
        a7b = [l for k, v in r["hits"].items() if k.startswith("A7b") for l, _ in v]
        a2 = [l for k, v in r["hits"].items() if k.startswith("A2") for l, _ in v]
        if not (a6 or a7b or a2):
            continue
        faits, restes = corriger(racine / r["page"], a6, a7b, a2, ecrire)
        total += len(faits); reste += len(restes)
        print(f"{'✎' if ecrire else '·'} {r['page'].rsplit('/', 1)[-1][:58]:<58} {len(faits):>3} ligne(s) corrigée(s)" + (f" · {len(restes)} restante(s)" if restes else ""))
        for n, quoi in restes[:6]:
            print(f"      reste ligne {n} : {quoi}")
    print(f"\n{total} ligne(s) {'corrigées' if ecrire else 'à corriger'} · {reste} cas restant(s)")
    return 1 if reste else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(principal())
