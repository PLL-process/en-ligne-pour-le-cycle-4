#!/bin/sh
# Construit ../objet3d.js depuis objet3d.src.js : three.js et la vue en UN script classique (IIFE), lisible en file://.
# La licence MIT de three.js est recopiée en fin de fichier (--legal-comments=eof). node_modules/ n'entre pas au dépôt.
set -e
cd "$(dirname "$0")"
npm install --no-audit --no-fund
npx esbuild objet3d.src.js --bundle --minify --format=iife --legal-comments=eof --outfile=../objet3d.js
ls -l ../objet3d.js
