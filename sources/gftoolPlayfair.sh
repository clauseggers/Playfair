#!/bin/sh
# This script generates the Variable Font TTFs for the Playfair typeface.

# Checks if the `gftools_ttf` directory exists, if not it creates it.
if [ ! -d "gftools_ttf" ]; then
  mkdir -p "gftools_ttf"
  chmod -R 755 "gftools_ttf"
fi

gftools builder config.yaml

# EOF
