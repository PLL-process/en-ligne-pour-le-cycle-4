# Banc Docker — vérification de compilation (enseignant)

Rôle : garantir le critère du skill `arduino-grove-college` — « le programme
compile pour la carte annoncée » (`arduino:avr:uno`) — de façon reproductible,
sans rien installer d'autre que Docker Desktop.

⚠️ Réservé à l'enseignant : Docker Desktop exige un compte (adresse mail).
Les élèves n'en ont pas besoin : ils utilisent ArduBlock Éducation 1.7,
qui embarque sa propre chaîne de téléversement.

## Utilisation (Docker Desktop 4.87.0, Windows)

```powershell
cd banc-docker
docker compose build          # une fois (télécharge arduino-cli + noyau AVR + lib Grove LCD)
docker compose run --rm compile station_alerte_cyclonique
```

Sortie attendue : `Sketch uses ~6800 bytes` et aucun avertissement bloquant.

## Vérification déjà effectuée hors Docker (19/08/2026)

Chaîne avr-gcc 7.3 + noyau ArduinoCore-avr + Grove_LCD_RGB_Backlight :
`text 6764 · data 176 · bss 393` → **compilation OK** pour atmega328p.
Le banc Docker refait la même preuve avec la chaîne officielle arduino-cli.
