#!/usr/bin/env bash
# Tire des rendus de generer.py les fichiers légers de la page (5e_C1.2, les trois freins en 3D).
#
#     bash assembler.sh DOSSIER_DES_RENDUS [DOSSIER_DE_TRAVAIL]
#
# 1. habiller.py assemble la vue large, la loupe et les pastilles (dans le dossier de travail).
# 2. Ce script encode, dans le dossier du lot :
#   Films/trois-freins_<frein>.mp4                 le film : H.264, 960 × 676, 4,5 s, muet, lisible dès le début du téléchargement
#   Films/trois-freins_<frein>.webm                le même en VP9, pour les navigateurs qui ne lisent pas le H.264
#   Images/trois-freins_<frein>_3d.jpg             sa dernière image, sur le fond du film : l'affiche (n°176)
#   Images/trois-freins_<frein>_3d_impression.jpg  la même sur fond clair (n°102), en 720 × 507 : 55 mm de large sur le papier
# Il faut python3 avec Pillow, et ffmpeg avec libx264 et libvpx-vp9 (variable FFMPEG, défaut : « ffmpeg »).
set -euo pipefail
rendus="${1:?dossier des rendus de generer.py}"
ici="$(cd "$(dirname "$0")" && pwd)"
lot="$(cd "$ici/../.." && pwd)"
travail="${2:-$(mktemp -d)}"
ffmpeg="${FFMPEG:-ffmpeg}"
mkdir -p "$lot/Films" "$lot/Images"
python3 "$ici/habiller.py" "$rendus" "$travail"
for frein in patins disque tambour; do
  "$ffmpeg" -v error -y -i "$travail/${frein}_compose.mp4" -an -c:v libx264 -preset veryslow -crf 23 -pix_fmt yuv420p \
    -profile:v main -level 3.1 -g 24 -movflags +faststart -map_metadata -1 -fflags +bitexact -flags:v +bitexact \
    "$lot/Films/trois-freins_${frein}.mp4"
  "$ffmpeg" -v error -y -i "$travail/${frein}_compose.mp4" -an -c:v libvpx-vp9 -crf 34 -b:v 0 -deadline good -cpu-used 1 -row-mt 1 \
    -pix_fmt yuv420p -g 24 -map_metadata -1 -fflags +bitexact "$lot/Films/trois-freins_${frein}.webm"
  "$ffmpeg" -v error -y -i "$travail/${frein}_complet_sombre.png" -q:v 3 -map_metadata -1 "$lot/Images/trois-freins_${frein}_3d.jpg"
  "$ffmpeg" -v error -y -i "$travail/${frein}_complet_clair.png" -vf scale=720:507:flags=lanczos -q:v 4 -map_metadata -1 \
    "$lot/Images/trois-freins_${frein}_3d_impression.jpg"
done
ls -l "$lot"/Films/trois-freins_* "$lot"/Images/trois-freins_*_3d*.jpg
