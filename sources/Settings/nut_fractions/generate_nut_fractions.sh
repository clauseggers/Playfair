#!/usr/bin/env sh

# Generates the static OT-feature code for the positioning of proportional
# stacking- or nut fractions.
# https://fez.readthedocs.io/en/latest/optionalverbs.html#fractions

fez2fea ../../Playfair-2_1-Roman.glyphs nut_fractions.fez > Roman_static_nut_fractions.fez.fea
fez2fea ../../Playfair-2_1-Italic.glyphs nut_fractions.fez > Italic_static_nut_fractions.fez.fea

#EOF
