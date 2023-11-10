#!/bin/sh
# This script generates the Variable Font TTFs for the Playfair typeface.

# Checks if the `variable_ttf` directory exists, if not it creates it.
if [ ! -d "variable_ttf" ]; then
  mkdir -p "variable_ttf"
  chmod -R 755 "variable_ttf"
fi

fontmake Playfair-2_2-Roman.glyphs -o variable \
  --output-path 'variable_ttf/PlayfairRomanVF.ttf' --verbose WARNING
fontmake Playfair-2_2-Italic.glyphs -o variable \
  --output-path 'variable_ttf/PlayfairItalicVF.ttf' --verbose WARNING

# EOF
