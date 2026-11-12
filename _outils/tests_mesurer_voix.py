# -*- coding: utf-8 -*-
"""Banc de mesurer_voix.py : des animations fabriquées (silences de durée connue), et les pannes.

    python3 _outils/tests_mesurer_voix.py        → 0 si tout passe, 1 sinon, 2 si ffmpeg manque (n°299)
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import mesurer_voix as mv   # noqa: E402

if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
    print("❌ EN PANNE : ffmpeg ou ffprobe introuvable, le banc ne peut rien vérifier (règle d'or n°299).")
    sys.exit(2)

res = []
def t(nom, ok, detail=""):
    res.append((nom, bool(ok)))
    if not ok:
        print("  ✘", nom, detail)

def silence(fichier, secondes):
    fichier.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=22050:cl=mono",
                    "-t", str(secondes), "-c:a", "libvorbis", str(fichier)], check=True)

def lot(racine, nom, phrases, durees, prefixe="anim_etape", voix=None, dossier="voix_essai"):
    d = racine / "theme-x" / nom
    g = d / "_generation" / dossier
    g.mkdir(parents=True, exist_ok=True)
    (g / "phrases.json").write_text(json.dumps({"phrases": phrases}, ensure_ascii=False), encoding="utf-8")
    if voix is not None:
        (g / "voix.json").write_text(json.dumps(voix, ensure_ascii=False), encoding="utf-8")
    for i, s in enumerate(durees, 1):
        silence(d / "Audio" / ("%s%d.ogg" % (prefixe, i)), s)
    return d

def jouer(racine, *args):
    r = subprocess.run([sys.executable, str(ICI / "mesurer_voix.py"), str(racine), *args], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr

# ── les mots ──
t("mots : l'apostrophe et le trait d'union ne coupent pas", mv.compter_mots("L'énergie du vélo-cargo") == 3, str(mv.compter_mots("L'énergie du vélo-cargo")))
t("mots : les balises ne comptent pas", mv.compter_mots("le <b>seuil</b> de 40") == 4)
t("mots : un texte vide vaut zéro", mv.compter_mots("") == 0 and mv.compter_mots(None) == 0)

with tempfile.TemporaryDirectory() as tmp:
    racine = pathlib.Path(tmp)
    dix = " ".join(["mot"] * 10)
    # 10 mots en 4 s = 150 mots/min ; 10 mots en 3 s = 200 mots/min
    lot(racine, "lent", [{"n": 1, "dit": dix}, {"n": 2, "dit": dix}], [4, 4], voix={"reglages_piper": {"length_scale": 1.15}})
    lot(racine, "rapide", [{"n": 1, "dit": dix}, {"n": 2, "dit": "affiché autrement", "envoye": dix}], [4, 3],
        voix={"reglages_piper": {"length_scale": 1.0}})
    # une archive ne se lit pas
    lot(racine / "_archive-anciennes-versions", "vieux", [{"n": 1, "dit": dix}], [1])
    sortie = racine / "r.json"
    code, texte = jouer(racine, "--json", str(sortie))
    R = {a["animation"].split("/")[1]: a for a in json.loads(sortie.read_text(encoding="utf-8"))["animations"]}
    t("deux animations mesurées, l'archive ignorée", set(R) == {"lent", "rapide"}, str(sorted(R)))
    t("mesure : sortie 0 même avec une étape rapide (ce n'est pas un contrôle)", code == 0, texte)
    t("10 mots en 4 s : 150 mots/min, à 2 près", abs(R["lent"]["etapes"][0]["debit"] - 150) <= 2, str(R["lent"]["etapes"][0]))
    t("animation lente : aucune étape signalée", R["lent"]["rapides"] == [])
    t("10 mots en 3 s : étape 2 signalée (au-dessus de %d)" % mv.REPERE_DEBIT, R["rapide"]["rapides"] == [2], str(R["rapide"]["rapides"]))
    t("le texte ENVOYÉ à la voix compte, pas le texte affiché", R["rapide"]["etapes"][1]["mots"] == 10, str(R["rapide"]["etapes"][1]))
    t("la vitesse Piper est relevée", R["lent"]["length_scale"] == 1.15 and "1.0, 1.15" in texte, texte[-300:])
    t("la sortie nomme l'étape rapide", "▲ au-dessus de" in texte and "étape(s) 2" in texte, texte)

with tempfile.TemporaryDirectory() as tmp:
    racine = pathlib.Path(tmp)
    # deux groupes de même taille dans Audio/ : voix.json dit lequel
    d = lot(racine, "deux", [{"n": 1, "dit": "un deux trois"}], [2], prefixe="bonne_scene", voix={"scenes": {"1": {"ogg": "Audio/bonne_scene1.ogg"}}})
    silence(d / "Audio" / "autre_scene1.ogg", 9)
    sortie = racine / "r.json"
    code, texte = jouer(racine, "--json", str(sortie), "--muet")
    a = json.loads(sortie.read_text(encoding="utf-8"))["animations"]
    t("deux groupes de sons : celui que voix.json nomme", code == 0 and a and abs(a[0]["etapes"][0]["duree_s"] - 2) < 0.3, texte)

with tempfile.TemporaryDirectory() as tmp:
    racine = pathlib.Path(tmp)
    # PANNE : trois phrases, deux sons
    lot(racine, "troue", [{"n": 1, "dit": "a b"}, {"n": 2, "dit": "c d"}, {"n": 3, "dit": "e f"}], [1, 1])
    code, texte = jouer(racine)
    t("PANNE — une étape sans fichier son : sortie 2, l'animation est nommée", code == 2 and "troue" in texte, texte)

with tempfile.TemporaryDirectory() as tmp:
    code, texte = jouer(tmp)
    t("PANNE — aucune animation : sortie 2", code == 2, texte)
code, texte = jouer(str(pathlib.Path(tempfile.gettempdir()) / "mv-nexiste-pas"))
t("PANNE — dossier absent : sortie 2", code == 2, texte)

ko = [n for n, ok in res if not ok]
print("%d / %d tests réussis" % (len(res) - len(ko), len(res)))
sys.exit(1 if ko else 0)
