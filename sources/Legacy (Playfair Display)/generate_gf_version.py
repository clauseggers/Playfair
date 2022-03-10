"""
Generate the ttf fonts for Google Fonts.

Will change the upm and vertical metrics so the line height
visually matches the version hosted on Google Fonts.
"""
import shutil
from glob import glob
import os
from fontTools.ttLib import TTFont


def update_upm(ttfont):
    ttfont['head'].unitsPerEm = 1000


def update_vert_metrics(ttfont):
    ttfont['hhea'].ascent = 1082
    ttfont['hhea'].descent = -251
    ttfont['hhea'].lineGap = 0

    ttfont['OS/2'].sTypoAscender = 1082
    ttfont['OS/2'].sTypoDescender = -251
    ttfont['OS/2'].sTypoLineGap = 0

    ttfont['OS/2'].usWinAscent = 1201
    ttfont['OS/2'].usWinDescent = 251



def main():
    file_dir = os.path.dirname(__file__)
    fonts_dir = os.path.join(file_dir, '..', 'fonts')
    ttf_dir = os.path.join(fonts_dir, 'TTF')
    gf_ttf_dir = os.path.join(fonts_dir, 'GF_TTF')

    print 'Copying fonts to gf_ttf_dir'
    source_fonts = glob(ttf_dir + '/*.ttf')
    if not os.path.isdir(gf_ttf_dir):
        os.mkdir(gf_ttf_dir)

    print 'Changing upm and setting vert metrics'
    ttfonts = [TTFont(f) for f in source_fonts]
    map(update_upm, ttfonts)
    map(update_vert_metrics, ttfonts)

    print 'Saving fonts'
    for ttfont, path in zip(ttfonts, source_fonts):
        dest_filename = os.path.basename(path)
        dest_path = os.path.join(gf_ttf_dir, dest_filename)
        ttfont.save(dest_path)


if __name__ == '__main__':
    main()
