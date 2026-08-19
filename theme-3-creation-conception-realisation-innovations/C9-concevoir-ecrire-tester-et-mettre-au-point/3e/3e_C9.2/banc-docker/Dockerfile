# Banc de compilation Arduino — usage ENSEIGNANT uniquement (compte Docker requis)
# Vérifie que les programmes du lot compilent pour arduino:avr:uno.
FROM ubuntu:24.04
RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://github.com/arduino/arduino-cli/releases/download/v1.5.1/arduino-cli_1.5.1_Linux_64bit.tar.gz \
    | tar -xz -C /usr/local/bin arduino-cli
RUN arduino-cli core update-index && arduino-cli core install arduino:avr \
 && arduino-cli lib install "Grove - LCD RGB Backlight"
WORKDIR /sketchs
ENTRYPOINT ["arduino-cli", "compile", "--fqbn", "arduino:avr:uno", "--warnings", "all"]
