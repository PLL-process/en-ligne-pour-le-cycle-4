# -*- coding: utf-8 -*-
"""Engendre la voix du dessin animé du vélo-cargo (5e_C3.1, bloc #velo-cargo-pas-a-pas) : une voix de synthèse
neuronale hors ligne (Piper), jamais une voix humaine enregistrée.

    python3 generer.py              # lit phrases.json et voix.json, écrit ../../Audio/velo-cargo_scene1…6 (.ogg et .mp3)
    python3 generer.py --verifier   # vérifie seulement que les phrases dites sont celles de la séquence (rien n'est écrit)

CE QUE LE SCRIPT FAIT
  1. Compare chaque phrase de phrases.json au tableau SCENES de la séquence, mot pour mot (balises et espaces
     insécables ôtés). Une phrase qui a changé dans la séquence sans changer ici arrête tout : l'élève entendrait
     autre chose que ce qu'il lit.
  2. Pour chaque phrase : Piper → WAV ; ffmpeg coupe les silences du début et de la fin, normalise le volume
     (loudnorm, -16 LUFS), puis écrit l'Opus mono 32 kb/s (.ogg) et un MP3 mono 48 kb/s de secours.

CE QU'IL FAUT SUR LE POSTE (rien de tout cela n'est dans le dépôt)
  · `piper-tts` (pip install piper-tts) : la variable PIPER_PYTHON désigne l'interpréteur qui l'a (défaut : celui-ci) ;
  · le modèle `fr_FR-siwis-medium` : la variable PIPER_MODELES désigne son dossier
    (défaut : ~/figures-iso-essais/voix-velo-cargo/modeles) ; s'il y manque, le script le télécharge :
    python -m piper.download_voices --download-dir <dossier> fr_FR-siwis-medium ;
  · ffmpeg avec libopus et libmp3lame (variable FFMPEG, défaut : « ffmpeg »).
Ne jamais copier Piper, espeak-ng ni le modèle dans le dépôt : le moteur est sous GPL-3, le modèle est une donnée à part.
Licence de la voix et attribution : voix.json et SOURCES_MEDIAS.md.

ATTENTION : ce n'est PAS reproductible à l'octet. Piper tire du bruit à chaque prise (noise_scale, noise_w_scale) et le
conteneur Ogg porte un numéro de flux aléatoire : deux générations de la même phrase donnent deux prises un peu différentes
(rythme et intonation voisins). Les fichiers de Audio/ sont donc LA référence : ne régénérer que si une phrase change, et
alors régénérer les six, pour qu'elles gardent le même grain.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
LOT = ICI.parents[1]
PAGE = LOT / "sequence_5e_C3.1-C3.4_shanghai.html"
AUDIO = LOT / "Audio"
PREFIXE = "velo-cargo_scene"


def phrases_de_la_page():
    """Les six phrases de SCENES, telles que l'élève les lit : sans balises, espaces insécables en espaces."""
    html = PAGE.read_text(encoding="utf-8")
    debut = html.index("var SCENES = [")
    bloc = html[debut:html.index("];", debut)]
    brutes = re.findall(r'\bp:\s*("(?:[^"\\]|\\.)*")', bloc)
    sorties = []
    for b in brutes:
        texte = json.loads(b)
        texte = re.sub(r"<[^>]+>", "", texte).replace(" ", " ")
        sorties.append(re.sub(r"\s+", " ", texte).strip())
    return sorties


def verifier(phrases):
    lues = phrases_de_la_page()
    if len(lues) != len(phrases):
        sys.exit("La séquence a %d phrases, phrases.json en a %d." % (len(lues), len(phrases)))
    ecarts = [(p["n"], p["dit"], l) for p, l in zip(phrases, lues) if re.sub(r"\s+", " ", p["dit"]).strip() != l]
    if ecarts:
        for n, dit, lue in ecarts:
            print("Scène %d : phrases.json dit « %s », la séquence écrit « %s »." % (n, dit, lue))
        sys.exit("Les phrases ne sont pas celles de la séquence : rien n'est généré.")
    print("✅ les %d phrases de phrases.json sont celles de la séquence, mot pour mot" % len(lues))


def piper_python():
    cible = os.environ.get("PIPER_PYTHON")
    if cible:
        return cible
    try:
        import piper  # noqa: F401
        return sys.executable
    except ImportError:
        sys.exit("Piper est introuvable : pip install piper-tts, ou PIPER_PYTHON=<interpréteur qui l'a>.")


def modele(voix, py):
    dossier = pathlib.Path(os.environ.get("PIPER_MODELES", pathlib.Path.home() / "figures-iso-essais" / "voix-velo-cargo" / "modeles"))
    onnx = dossier / (voix["modele"] + ".onnx")
    if not onnx.exists():
        dossier.mkdir(parents=True, exist_ok=True)
        subprocess.run([py, "-m", "piper.download_voices", "--download-dir", str(dossier), voix["modele"]], check=True)
    return onnx


def main():
    phrases = json.loads((ICI / "phrases.json").read_text(encoding="utf-8"))["phrases"]
    voix = json.loads((ICI / "voix.json").read_text(encoding="utf-8"))
    verifier(phrases)
    if "--verifier" in sys.argv:
        return
    py = piper_python()
    onnx = modele(voix, py)
    ff = os.environ.get("FFMPEG", "ffmpeg")
    r = voix["reglages_piper"]
    AUDIO.mkdir(exist_ok=True)
    coupe = ("silenceremove=start_periods=1:start_threshold=-45dB:detection=peak,areverse,"
             "silenceremove=start_periods=1:start_threshold=-45dB:detection=peak,areverse,"
             "loudnorm=I=-16:TP=-1.5:LRA=11")
    with tempfile.TemporaryDirectory() as tmp:
        for p in phrases:
            wav = pathlib.Path(tmp) / ("s%d.wav" % p["n"])
            subprocess.run([py, "-m", "piper", "-m", str(onnx), "-f", str(wav), "--length-scale", str(r["length_scale"]),
                            "--noise-scale", str(r["noise_scale"]), "--noise-w-scale", str(r["noise_w_scale"])],
                           input=p["dit"].encode("utf-8"), check=True, capture_output=True,
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
            base = AUDIO / (PREFIXE + str(p["n"]))
            subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(wav), "-af", coupe, "-ac", "1", "-ar", "48000",
                            "-c:a", "libopus", "-b:a", "32k", "-application", "voip", "-map_metadata", "-1",
                            str(base) + ".ogg"], check=True)
            subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(wav), "-af", coupe, "-ac", "1", "-ar", "44100",
                            "-c:a", "libmp3lame", "-b:a", "48k", "-map_metadata", "-1", "-id3v2_version", "0",
                            "-write_xing", "0", str(base) + ".mp3"], check=True)
            print("scène %d : %5.1f Ko (.ogg) · %5.1f Ko (.mp3)" % (
                p["n"], os.path.getsize(str(base) + ".ogg") / 1024, os.path.getsize(str(base) + ".mp3") / 1024))
    print("✅ écrit dans %s" % AUDIO)


if __name__ == "__main__":
    main()
