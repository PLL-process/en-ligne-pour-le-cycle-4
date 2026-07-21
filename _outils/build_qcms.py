# -*- coding: utf-8 -*-
import os, re, sys, pickle, html, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qcm_generator import build_qcm, sanity_check, card
import banks_a, banks_b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

T1C1 = "theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions"
T2C4 = "theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation"
T2C6 = "theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe"
T3C9 = "theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point"
ARCH = "_archive-anciennes-versions"

JOBS = [
    (banks_a.ECALL, f"{T2C4}/4e/4e_C4.4/qcm_ecall_chaine_information.html",
     "QCM XXL (40 questions) — eCall : la chaîne d'information d'une voiture — 4e (2024)",
     "Les questions ciblent 4e_C4.4 (constituants de la chaîne d'information d'un objet réel), avec des liens vers C4.1 et C6.2."),
    (banks_a.CYBER, f"{T1C1}/4e/4e_C1.4/qcm_cybersecurite_usage_raisonne.html",
     "QCM (24 questions) — Cybersécurité & usage raisonné du numérique — 4e (2024)",
     "Les questions ciblent 4e_C1.4 (usage raisonné, identité numérique), en croisement avec 5e_C1.5 et 5e_C1.6."),
    (banks_a.JARDIN, f"{T2C6}/4e/4e_C6.2/qcm_jardin_connecte.html",
     "QCM (24 questions) — Jardin connecté : programmer l'arrosage automatique — 4e (2024)",
     "Les questions ciblent 4e_C6.2 (compléter un programme), avec des liens vers C4.1, C4.5 et C1.4. À faire après la séquence Jardin connecté."),
    (banks_a.ALGO_DNB, f"{T2C6}/3e/3e_C6.2/qcm_algorigrammes_dnb.html",
     "QCM (24 questions) — Algorigrammes & logique, spécial DNB — 3e (2024)",
     "Les questions ciblent 3e_C6.2 (modifier et tester un programme), en préparation de l'épreuve de sciences du brevet."),
    (banks_b.DONNEES_5E, f"{T1C1}/5e/5e_C1.1/qcm_donnees_tableur.html",
     "QCM (24 questions) — Collecter, trier et analyser des données — 5e (2024)",
     "Les questions ciblent 5e_C1.1, en lien direct avec la séquence tableur et les fichiers d'exercices du dossier."),
    (banks_b.PRINCIPES_5E, f"{T1C1}/5e/5e_C1.2/qcm_principes_techniques.html",
     "QCM (24 questions) — Comparer des principes techniques — 5e (2024)",
     "Les questions ciblent 5e_C1.2 : une même fonction, plusieurs principes, des critères pour comparer."),
    (banks_b.SI_5E, f"{T1C1}/5e/5e_C1.3/qcm_systemes_information_donnees.html",
     "QCM (24 questions) — Systèmes d'information & gestion des données — 5e (2024)",
     "Les questions ciblent 5e_C1.3 et 5e_C1.4 (SI, arborescence, stockage), en accompagnement de la séquence du dossier."),
    (banks_b.NUM_SOCIETE_3E, f"{T1C1}/3e/3e_C1.5/qcm_numerique_societe.html",
     "QCM (24 questions) — Numérique, société, environnement & santé — 3e (2024)",
     "Les questions ciblent 3e_C1.5 (rôle stratégique du numérique dans la société), en accompagnement de la séquence du dossier."),
    (banks_b.PYTHON_3E, f"{T3C9}/3e/3e_C9.1/qcm_python_variables.html",
     "QCM (24 questions) — Python : variables, types et programmes — 3e (2024)",
     "Les questions ciblent 3e_C9.1, en accompagnement de la page Vittascience et du TP mBot2 du dossier."),
]

# 0) archiver l'ancienne ébauche eCall
old_ecall = f"{T2C4}/4e/4e_C4.4/qcm_ecall_chaine_information.html"
if os.path.isfile(old_ecall):
    dst = f"{ARCH}/t3-modelisation-simulation-objets-systemes-techniques-msost/QCM_ecall_ebauche_5questions.html"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(old_ecall, dst)
    print("Ébauche eCall archivée")

# 1) générer les 9 QCM
total_q = 0
for bank, path, title, note in JOBS:
    n = build_qcm(title, note, bank, path)
    total_q += n
    nsec, missing = sanity_check(path)
    status = "OK" if nsec == n and not missing else f"⚠️ sections={nsec}/{n} manquants={missing}"
    print(f"{n:>3} q -> {os.path.basename(path):45} {status}")
print("Total questions générées:", total_q)

# 2) fusion : insérer les questions LAN/WLAN/Zigbee dans le XXL fixed3
XXL = f"{T2C4}/4e/4e_C4.7/qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee.html"
LAN = f"{T2C4}/4e/4e_C4.7/qcm_reseaux_lan_wlan_zigbee.html"
data = pickle.load(open("/tmp/lanwlan_questions.pkl", "rb"))
all_lan = data["DATA_QCM1"] + data["DATA_QCM2"]
DUPES = {5, 6, 23}  # switch, routeur, fréquence Zigbee : déjà dans le XXL
keep = [q for i, q in enumerate(all_lan) if i not in DUPES]

t = open(XXL, encoding="utf-8").read()
cards = []
idx = 41
for q in keep:
    item = ("m", "4e_C4.7", q["q"], q["opts"], q["good"], q["help"])
    cards.append(card(idx, item))
    idx += 1
insert_html = ('\n    <div class="card"><p class="q-title" style="counter-increment:none">'
               '</p><strong>🧩 Partie 2 — fusion du QCM « LAN / WLAN / Hub / Switch / Routeur / Zigbee »'
               f' ({len(keep)} questions, doublons retirés)</strong></div>\n' + "".join(cards))
# retirer le pseudo q-title du bandeau (il ne doit pas compter comme question)
insert_html = insert_html.replace('<p class="q-title" style="counter-increment:none"></p>', '')
i = t.find('<div class="footer">')
assert i > 0
t = t[:i] + insert_html + "\n    " + t[i:]
new_total = 40 + len(keep)
t = t.replace("QCM XXL (40 questions) — Réseaux, IP, NFC, RFID, Zigbee — Cycle 4 (2024)",
              f"QCM XXL ({new_total} questions) — Réseaux, IP, NFC, RFID, Zigbee — Cycle 4 (2024) — fusion")
t = t.replace("QCM XXL (40) — Réseaux, IP, NFC, RFID, Zigbee — Cycle 4 (2024)",
              f"QCM XXL ({new_total}) — Réseaux, IP, NFC, RFID, Zigbee — Cycle 4 (2024)")
open(XXL, "w", encoding="utf-8").write(t)
nsec, missing = sanity_check(XXL)
print(f"Fusion : {new_total} questions attendues, {nsec} sections détectées, manquants={missing}")

# 3) archiver le fichier fusionné
dst = f"{ARCH}/C1_C3_Les-objets-et-les-systèmes-techniques/qcm_reseaux_lan_wlan_zigbee_fusionne-dans-XXL.html"
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.move(LAN, dst)
print("qcm_reseaux_lan_wlan_zigbee.html archivé (contenu fusionné dans le XXL)")
