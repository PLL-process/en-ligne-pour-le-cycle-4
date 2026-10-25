# -*- coding: utf-8 -*-
"""Engendre la voix de l'animation des trois principes (5e_C1.1, activité 1, bloc #trois-principes-pas-a-pas) :
une voix de synthèse neuronale hors ligne (Piper), jamais une voix humaine enregistrée. Même voix, mêmes réglages et
même chaîne audio que le dessin animé du vélo-cargo (5e_C3.1).

    python3 generer.py              # lit phrases.json et voix.json, écrit ../../Audio/trois-principes_scene1…11 (.ogg et .mp3)
    python3 generer.py --verifier   # vérifie seulement que les phrases dites sont celles de la séquence (rien n'est écrit)
    python3 generer.py --scene 4    # nouvelle prise de la seule scène 4, les autres fichiers restent inchangés

CE QUE LE SCRIPT FAIT
  1. Compare chaque « dit » de phrases.json au tableau SCENES de la séquence, mot pour mot (balises et espaces
     insécables ôtés). Une phrase qui a changé dans la séquence sans changer ici arrête tout : l'élève entendrait
     autre chose que ce qu'il lit.
  2. Pour chaque phrase : Piper → WAV. La voix reçoit « envoye » s'il existe (sinon « dit ») ; si « phonemes » existe,
     ces phonèmes (espeak-ng corrigé à la main, une chaîne par phrase) remplacent la phonétisation automatique.
     Puis ffmpeg coupe les silences du début et de la fin, normalise le volume (loudnorm, -16 LUFS), et écrit
     l'Opus mono 32 kb/s (.ogg) et un MP3 mono 48 kb/s de secours.

CE QU'IL FAUT SUR LE POSTE (rien de tout cela n'est dans le dépôt)
  · `piper-tts` (pip install piper-tts ; 1.8.0 ici) ;
  · le modèle SIWIS medium : la variable PIPER_MODELE désigne le fichier .onnx (son .onnx.json à côté) ; sinon le
    script cherche fr_FR-siwis-medium.onnx puis fr-siwis-medium.onnx dans PIPER_MODELES
    (défaut : ~/figures-iso-essais/voix-velo-cargo/modeles). Voir voix.json « modele_utilise » pour celui des fichiers actuels.
  · ffmpeg avec libopus et libmp3lame (variable FFMPEG, défaut : « ffmpeg »).
Ne jamais copier Piper, espeak-ng ni le modèle dans le dépôt : le moteur est sous GPL-3, le modèle est une donnée à part.

AVERTISSEMENT — UNE PRISE PRODUITE N'EST PAS UNE PRISE VALIDÉE. Seule l'écoute de Pascal valide une prise ; voix.json
« prises » dit, scène par scène, ce qui a été écouté (les onze prises de Audio/ : validées le 25/10/2026). Toute
régénération exige une nouvelle écoute de Pascal. Piper tire du bruit à chaque prise et Ogg porte un numéro de flux
aléatoire : ce n'est PAS reproductible à l'octet. Les fichiers de Audio/ sont la référence : ne régénérer que si une
phrase change, avec --scene N pour garder les autres prises.
"""
import argparse
import hashlib
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
PAGE = LOT / "sequence_5e_C1.1-C1.6_chengdu_air.html"
AUDIO = LOT / "Audio"
PREFIXE = "trois-principes_scene"


def propre(texte):
    texte = re.sub(r"<[^>]+>", "", texte).replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", texte).strip()


def phrases_de_la_page():
    """Les phrases de SCENES (bloc #trois-principes-pas-a-pas), telles que l'élève les lit."""
    html = PAGE.read_text(encoding="utf-8")
    debut = html.index("trois_principes_pas_a_pas (script) : début")
    debut = html.index("var SCENES = [", debut)
    bloc = html[debut:html.index("];", debut)]
    return [propre(json.loads(b)) for b in re.findall(r'\bp:\s*("(?:[^"\\]|\\.)*")', bloc)]


def verifier(phrases):
    lues = phrases_de_la_page()
    if len(lues) != len(phrases):
        sys.exit("La séquence a %d phrases, phrases.json en a %d." % (len(lues), len(phrases)))
    ecarts = [(p["n"], p["dit"], l) for p, l in zip(phrases, lues) if propre(p["dit"]) != l]
    if ecarts:
        for n, dit, lue in ecarts:
            print("Scène %d : phrases.json dit « %s », la séquence écrit « %s »." % (n, dit, lue))
        sys.exit("Les phrases ne sont pas celles de la séquence : rien n'est généré.")
    print("✅ les %d phrases de phrases.json sont celles de la séquence, mot pour mot" % len(lues))


def modele():
    direct = os.environ.get("PIPER_MODELE")
    if direct:
        return pathlib.Path(direct)
    dossier = pathlib.Path(os.environ.get("PIPER_MODELES", pathlib.Path.home() / "figures-iso-essais" / "voix-velo-cargo" / "modeles"))
    for nom in ("fr_FR-siwis-medium.onnx", "fr-siwis-medium.onnx"):
        if (dossier / nom).exists():
            return dossier / nom
    sys.exit("Modèle SIWIS medium introuvable : PIPER_MODELE=<fichier .onnx> ou PIPER_MODELES=<dossier> (voir l'en-tête).")


def main():
    parser = argparse.ArgumentParser(description="Voix des trois principes : vérifier les textes ou produire une prise à écouter.")
    parser.add_argument("--verifier", action="store_true")
    parser.add_argument("--scene", type=int, help="Ne régénérer que cette scène.")
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
    onnx = modele()
    print("modèle :", onnx, "— sha256", hashlib.sha256(onnx.read_bytes()).hexdigest())
    v = PiperVoice.load(str(onnx))
    r = voix["reglages_piper"]
    config = SynthesisConfig(length_scale=r["length_scale"], noise_scale=r["noise_scale"], noise_w_scale=r["noise_w_scale"])
    phonetiser = v.phonemize
    ff = os.environ.get("FFMPEG", "ffmpeg")
    AUDIO.mkdir(exist_ok=True)
    coupe = ("silenceremove=start_periods=1:start_threshold=-45dB:detection=peak,areverse,"
             "silenceremove=start_periods=1:start_threshold=-45dB:detection=peak,areverse,"
             "loudnorm=I=-16:TP=-1.5:LRA=11")
    with tempfile.TemporaryDirectory() as tmp:
        for p in phrases:
            if args.scene is not None and p["n"] != args.scene:
                continue
            texte = p.get("envoye", p["dit"])
            if "phonemes" in p:
                v.phonemize = lambda _t, ph=p["phonemes"]: [list(s) for s in ph]
            else:
                v.phonemize = phonetiser
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
            print("scène %2d : %5.1f Ko (.ogg) · %5.1f Ko (.mp3)%s" % (
                p["n"], os.path.getsize(str(base) + ".ogg") / 1024, os.path.getsize(str(base) + ".mp3") / 1024,
                " · phonèmes corrigés" if "phonemes" in p else ""))
    v.phonemize = phonetiser
    print("✅ écrit dans %s" % AUDIO)


if __name__ == "__main__":
    main()
