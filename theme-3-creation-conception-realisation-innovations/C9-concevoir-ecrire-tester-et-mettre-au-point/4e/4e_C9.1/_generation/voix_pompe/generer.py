# -*- coding: utf-8 -*-
"""Engendre la voix de l'animation « la pompe qui s'affole » (4e_C9.1, activité 5 b, bloc #pompe-pas-a-pas) :
une voix de synthèse neuronale hors ligne (Piper), jamais une voix humaine enregistrée. Même voix, mêmes réglages et
même chaîne audio que le jardin (4e_C8.1, _generation/voix_situation/), le vélo-cargo (5e_C3.1) et les trois
principes (5e_C1.1).

    python3 generer.py              # lit phrases.json et voix.json, écrit ../../Audio/pompe_etape1…9 (.ogg et .mp3)
    python3 generer.py --verifier   # vérifie seulement que les phrases dites sont celles de la séquence (rien n'est écrit)
    python3 generer.py --scene 4    # nouvelle prise de la seule étape 4, les autres fichiers restent inchangés

CE QUE LE SCRIPT FAIT
  1. Compare chaque « dit » de phrases.json au tableau SCENES de la séquence, mot pour mot (balises ôtées, entités
     HTML lues — « &lt; » est « < » —, espaces insécables ramenés à l'espace). Une phrase qui a changé dans la séquence
     sans changer ici arrête tout : l'élève entendrait autre chose que ce qu'il lit.
  2. Pour chaque phrase : Piper → WAV. La voix reçoit « envoye » s'il existe (sinon « dit »). Puis ffmpeg coupe les
     silences du début et de la fin, normalise le volume (loudnorm, -16 LUFS), et écrit l'Opus mono 32 kb/s (.ogg) et
     un MP3 mono 48 kb/s de secours.
  3. Note dans voix.json (clé « prises ») l'empreinte et la durée de chaque prise, et qu'elle n'est PAS écoutée.

CE QU'IL FAUT SUR LE POSTE (rien de tout cela n'est dans le dépôt)
  · `piper-tts` (pip install piper-tts ; 1.8.0 ici) ;
  · le modèle SIWIS medium : la variable PIPER_MODELE désigne le fichier .onnx (son .onnx.json à côté) ; sinon le
    script cherche fr_FR-siwis-medium.onnx dans PIPER_MODELES. Empreinte attendue : voix.json « modele_utilise ».
  · ffmpeg avec libopus et libmp3lame (variable FFMPEG, défaut : « ffmpeg »).
Ne jamais copier Piper, espeak-ng ni le modèle dans le dépôt : le moteur est sous GPL-3, le modèle est une donnée à part.

AVERTISSEMENT — UNE PRISE PRODUITE N'EST PAS UNE PRISE VALIDÉE. Seule l'écoute de Pascal valide une prise. Piper tire du
bruit à chaque prise et Ogg porte un numéro de flux aléatoire : ce n'est PAS reproductible à l'octet. Les fichiers de
Audio/ sont la référence : ne régénérer que si une phrase change, avec --scene N pour garder les autres prises.
"""
import argparse
import datetime
import hashlib
import html
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import wave

ICI = pathlib.Path(__file__).resolve().parent
LOT = ICI.parents[1]
PAGE = LOT / "sequence_4e_C9_jardin-programme.html"
AUDIO = LOT / "Audio"
PREFIXE = "pompe_etape"


def espaces(texte):
    return re.sub(r"\s+", " ", texte.replace(" ", " ").replace(" ", " ")).strip()


def propre(texte):
    """Le texte d'une phrase de la page (HTML) : balises ôtées, entités lues (« &lt; » est « < »)."""
    return espaces(html.unescape(re.sub(r"<[^>]+>", "", texte)))


def phrases_de_la_page():
    """Les phrases de SCENES (bloc #pompe-pas-a-pas), telles que l'élève les lit."""
    page = PAGE.read_text(encoding="utf-8")
    debut = page.index("pompe_pas_a_pas (script) : début")
    debut = page.index("var SCENES = [", debut)
    bloc = page[debut:page.index("];", debut)]
    return [propre(json.loads(b)) for b in re.findall(r'\bp:\s*("(?:[^"\\]|\\.)*")', bloc)]


def verifier(phrases):
    lues = phrases_de_la_page()
    if len(lues) != len(phrases):
        sys.exit("La séquence a %d phrases, phrases.json en a %d." % (len(lues), len(phrases)))
    # « dit » est du texte : ses < et > ne sont pas des balises
    ecarts = [(p["n"], p["dit"], l) for p, l in zip(phrases, lues) if espaces(p["dit"]) != l]
    if ecarts:
        for n, dit, lue in ecarts:
            print("Étape %d : phrases.json dit « %s », la séquence écrit « %s »." % (n, dit, lue))
        sys.exit("Les phrases ne sont pas celles de la séquence : rien n'est généré.")
    print("✅ les %d phrases de phrases.json sont celles de la séquence, mot pour mot" % len(lues))


def modele(voix):
    direct = os.environ.get("PIPER_MODELE")
    if direct:
        onnx = pathlib.Path(direct)
    else:
        onnx = pathlib.Path(os.environ.get("PIPER_MODELES", ".")) / "fr_FR-siwis-medium.onnx"
    if not onnx.exists():
        sys.exit("Modèle SIWIS medium introuvable : PIPER_MODELE=<fichier .onnx> ou PIPER_MODELES=<dossier> (voir l'en-tête).")
    empreinte = hashlib.sha256(onnx.read_bytes()).hexdigest()
    if empreinte != voix["modele_utilise"]["sha256_onnx"]:
        sys.exit("Le modèle %s n'est pas celui de voix.json (sha256 %s…)." % (onnx, empreinte[:16]))
    return onnx


def main():
    parser = argparse.ArgumentParser(description="Voix de l'animation de la pompe : vérifier les textes ou produire une prise à écouter.")
    parser.add_argument("--verifier", action="store_true")
    parser.add_argument("--scene", type=int, help="Ne régénérer que cette étape.")
    args = parser.parse_args()
    phrases = json.loads((ICI / "phrases.json").read_text(encoding="utf-8"))["phrases"]
    voix = json.loads((ICI / "voix.json").read_text(encoding="utf-8"))
    verifier(phrases)
    if args.verifier:
        return
    print("ATTENTION : une prise produite n'est pas validée ; elle doit être écoutée (voix.json « prises »).")
    try:
        from piper import PiperVoice, SynthesisConfig
    except ImportError:
        sys.exit("Piper est introuvable : pip install piper-tts.")
    onnx = modele(voix)
    print("modèle :", onnx, "— empreinte conforme à voix.json")
    v = PiperVoice.load(str(onnx))
    r = voix["reglages_piper"]
    config = SynthesisConfig(length_scale=r["length_scale"], noise_scale=r["noise_scale"], noise_w_scale=r["noise_w_scale"])
    ff = os.environ.get("FFMPEG", "ffmpeg")
    AUDIO.mkdir(exist_ok=True)
    coupe = ("silenceremove=start_periods=1:start_threshold=-45dB:detection=peak,areverse,"
             "silenceremove=start_periods=1:start_threshold=-45dB:detection=peak,areverse,"
             "loudnorm=I=-16:TP=-1.5:LRA=11")
    prises = voix.setdefault("prises", {}).setdefault("etapes", {})
    jour = datetime.date.today().strftime("%d/%m/%Y")
    with tempfile.TemporaryDirectory() as tmp:
        for p in phrases:
            if args.scene is not None and p["n"] != args.scene:
                continue
            texte = p.get("envoye", p["dit"])
            wav = pathlib.Path(tmp) / ("s%d.wav" % p["n"])
            with wave.open(str(wav), "wb") as w:
                v.synthesize_wav(texte, w, syn_config=config)
            base = AUDIO / (PREFIXE + str(p["n"]))
            subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(wav), "-af", coupe, "-ac", "1", "-ar", "48000",
                            "-c:a", "libopus", "-b:a", "32k", "-application", "voip", "-map_metadata", "-1",
                            str(base) + ".ogg"], check=True)
            subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(wav), "-af", coupe, "-ac", "1", "-ar", "44100",
                            "-c:a", "libmp3lame", "-b:a", "48k", "-map_metadata", "-1", "-id3v2_version", "0",
                            "-write_xing", "0", str(base) + ".mp3"], check=True)
            duree = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                          str(base) + ".ogg"], check=True, capture_output=True, text=True).stdout.strip() or 0)
            prises[str(p["n"])] = {
                "ogg": "Audio/%s%d.ogg" % (PREFIXE, p["n"]),
                "sha256_ogg": hashlib.sha256(pathlib.Path(str(base) + ".ogg").read_bytes()).hexdigest()[:16],
                "duree_s": round(duree, 2),
                "ecoute": "produite le %s, NON écoutée : à faire écouter à Pascal" % jour,
            }
            print("étape %d : %5.1f Ko (.ogg) · %5.1f Ko (.mp3) · %.2f s" % (
                p["n"], os.path.getsize(str(base) + ".ogg") / 1024, os.path.getsize(str(base) + ".mp3") / 1024, duree))
    voix["prises"]["etat"] = "produites, non écoutées : seule l'écoute de Pascal les validera"
    (ICI / "voix.json").write_text(json.dumps(voix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("✅ écrit dans %s ; empreintes et durées notées dans voix.json" % AUDIO)


if __name__ == "__main__":
    main()
