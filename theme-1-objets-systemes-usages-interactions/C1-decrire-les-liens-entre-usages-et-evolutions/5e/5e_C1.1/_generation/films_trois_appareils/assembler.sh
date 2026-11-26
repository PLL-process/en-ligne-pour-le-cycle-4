#!/usr/bin/env bash
# Tire des rendus de generer.py les fichiers légers de la page (5e_C1.1, films « en 3D » des trois principes).
#
#     bash assembler.sh DOSSIER_DES_RENDUS
#
# Écrit, dans le dossier du lot :
#   Films/trois-principes_<nom>.mp4                 le film : H.264, 960 × 676, 4,5 s, muet, lisible dès le début du téléchargement
#   Films/trois-principes_<nom>.webm                le même en VP9, pour les navigateurs qui ne lisent pas le H.264
#   Images/trois-principes_<nom>_3d.jpg             sa dernière image, fond de la page : l'affiche du film (n°176)
#   Images/trois-principes_<nom>_3d_impression.jpg  la même sur fond clair (n°102) : la bande imprimée sous la planche
# Il faut ffmpeg avec libx264 (variable FFMPEG, défaut : « ffmpeg »).
set -euo pipefail
rendus="${1:?dossier des rendus de generer.py}"
lot="$(cd "$(dirname "$0")/../.." && pwd)"
ffmpeg="${FFMPEG:-ffmpeg}"
mkdir -p "$lot/Films" "$lot/Images"
for nom in p1_lumiere p2_pesee p3_rayonnement; do
  "$ffmpeg" -v error -y -i "$rendus/${nom}_maitre.mp4" -an -c:v libx264 -preset veryslow -crf 23 -pix_fmt yuv420p \
    -profile:v main -level 3.1 -g 24 -movflags +faststart -map_metadata -1 -fflags +bitexact -flags:v +bitexact \
    "$lot/Films/trois-principes_${nom}.mp4"
  "$ffmpeg" -v error -y -i "$rendus/${nom}_maitre.mp4" -an -c:v libvpx-vp9 -crf 34 -b:v 0 -deadline good -cpu-used 1 -row-mt 1 \
    -pix_fmt yuv420p -g 24 -map_metadata -1 -fflags +bitexact "$lot/Films/trois-principes_${nom}.webm"
  "$ffmpeg" -v error -y -i "$rendus/${nom}_sombre.png" -q:v 3 -map_metadata -1 "$lot/Images/trois-principes_${nom}_3d.jpg"
  "$ffmpeg" -v error -y -i "$rendus/${nom}_clair.png" -q:v 3 -map_metadata -1 "$lot/Images/trois-principes_${nom}_3d_impression.jpg"
done
ls -l "$lot"/Films/trois-principes_* "$lot"/Images/trois-principes_*_3d*.jpg
