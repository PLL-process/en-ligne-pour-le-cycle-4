#!/usr/bin/env python3
"""Audit de conformité aux règles d'or RC-1..RC-6 — dépôt en-ligne-pour-le-cycle-4.
Usage : python3 audit_conformite.py <racine_du_depot> > AUDIT_GLOBAL.md
Réexécutable après chaque correction (l'audit est un outil, pas un événement)."""
import re, sys, os
from pathlib import Path

RACINE = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
ANCIEN_CODE = re.compile(r'[3-6]e[_ ]?C\d\.\d')            # 4e_C4.1, 5e C4.1…
CODE_NU     = re.compile(r'(?<![3-6CA-Za-z])C\d\.\d')       # C4.1 sans niveau
BON_CODE    = re.compile(r'\b[3-6]C\d\.\d')                 # 4C4.1
REF_SPATIALE= re.compile(r'ci-dessus|ci-dessous|Fig\.|figure|schéma|document de référence|récit|tableau ci|image ci', re.I)

def audit_html(p):
    t = p.read_text(errors="ignore")
    res = {}
    # RC-1 navigation
    res["RC1"] = "✅" if (re.search(r'href="#\w', t) and re.search(r'btn-haut|retour en haut|↑', t)) else ("⚠️" if re.search(r'href="#\w', t) else "❌")
    # RC-2 compétences affichées (codes présents + libellé long)
    codes = len(BON_CODE.findall(t)) + len(ANCIEN_CODE.findall(t))
    res["RC2"] = "✅" if (codes and re.search(r'competence-visee|—\s*(Identifier|Repérer|Associer|Élaborer|Décrire|Analyser)', t)) else ("⚠️" if codes else "❌")
    # RC-3 consignes référencées
    consignes = re.findall(r'class="consigne"[^>]*>(.{0,320}?)</div>', t, re.S) or re.findall(r'[Cc]onsigne[^<]{0,60}</strong>(.{0,300})', t, re.S)
    if consignes:
        sans_ref = sum(1 for c in consignes if not REF_SPATIALE.search(c))
        res["RC3"] = "✅" if sans_ref == 0 else (f"⚠️{sans_ref}" if sans_ref < len(consignes) else f"❌{sans_ref}")
    else:
        res["RC3"] = "–"
    # RC-4 lisibilité (blocs denses sans structure)
    denses = [m for m in re.findall(r'class="(?:pieges|retenir|a-retenir)"[^>]*>(.*?)</div>', t, re.S)
              if len(re.sub(r'<[^>]+>', '', m)) > 420 and '<li>' not in m and '<br' not in m and '<p>' not in m]
    res["RC4"] = "✅" if not denses else f"❌{len(denses)}"
    # RC-5 nommage fichiers élèves
    saves = re.findall(r'(?:nomme|enregistre|sauvegarde|exporte)[^<]{0,100}?\.(odp|drawio|ods|odt|png|svg|pptx)', t, re.I)
    if saves:
        ok = re.search(r'_NOM_Prenom|_nom_prenom', t)
        res["RC5"] = "✅" if ok else f"❌{len(saves)}"
    else:
        res["RC5"] = "–"
    # RC-6 notation
    anciens, nus = len(ANCIEN_CODE.findall(t)), len(set(CODE_NU.findall(t)))
    res["RC6"] = "✅" if not anciens else f"❌{anciens}"
    if anciens == 0 and nus and not BON_CODE.search(t): res["RC6"] = f"⚠️{nus} nus"
    return res

def audit_md(p):
    t = p.read_text(errors="ignore")
    anciens = len(ANCIEN_CODE.findall(t))
    return {"RC6": "✅" if not anciens else f"❌{anciens}"}

htmls, mds = [], []
for p in sorted(RACINE.rglob("*")):
    if "lot_book-train_PR" in str(p): continue   # dossier égaré de la PR #112, à supprimer
    if "_archive" in str(p) or "/node_modules" in str(p): continue  # archives : hors périmètre de rectification
    if p.suffix == ".html": htmls.append(p)
    elif p.suffix == ".md": mds.append(p)

print("# AUDIT GLOBAL — règles d'or RC-1 à RC-6\n")
print(f"Périmètre : {len(htmls)} HTML · {len(mds)} Markdown (hors `lot_book-train_PR/`, à supprimer de main).\n")
print("Légende : ✅ conforme · ⚠️ partiel · ❌ non conforme (+nombre) · – non applicable\n")

print("## Fichiers HTML\n")
print("| Fichier | RC1 nav | RC2 comp. | RC3 consignes | RC4 lisib. | RC5 nommage | RC6 notation |")
print("|---|---|---|---|---|---|---|")
stats = {k: {"✅":0,"⚠️":0,"❌":0,"–":0} for k in ["RC1","RC2","RC3","RC4","RC5","RC6"]}
for p in htmls:
    r = audit_html(p)
    for k,v in r.items():
        cle = "✅" if v.startswith("✅") else "⚠️" if v.startswith("⚠") else "–" if v == "–" else "❌"
        stats[k][cle] += 1
    rel = str(p.relative_to(RACINE))
    print(f"| {rel} | {r['RC1']} | {r['RC2']} | {r['RC3']} | {r['RC4']} | {r['RC5']} | {r['RC6']} |")

print("\n## Markdown (notation RC-6 uniquement)\n")
md_ko = [(str(p.relative_to(RACINE)), audit_md(p)["RC6"]) for p in mds]
md_ko = [x for x in md_ko if x[1] != "✅"]
if md_ko:
    print("| Fichier | RC6 |"); print("|---|---|")
    for f, v in md_ko: print(f"| {f} | {v} |")
else:
    print("Tous conformes.")

print("\n## Synthèse HTML\n")
print("| Règle | ✅ | ⚠️ | ❌ | – |")
print("|---|---|---|---|---|")
for k in ["RC1","RC2","RC3","RC4","RC5","RC6"]:
    s = stats[k]; print(f"| {k} | {s['✅']} | {s['⚠️']} | {s['❌']} | {s['–']} |")
print(f"\nMarkdown non conformes RC-6 : {len(md_ko)} / {len(mds)}")
