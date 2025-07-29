#!/bin/bash
set -u

# TTF to WOFF2 conversion script for Playfair fonts
fonttools ttLib.woff2 compress PlayfairRomanVF.ttf -o ../VF-WOFF2/PlayfairRomanVF.woff2 -v
fonttools ttLib.woff2 compress PlayfairItalicVF.ttf -o ../VF-WOFF2/PlayfairItalicVF.woff2 -v

# EOF
