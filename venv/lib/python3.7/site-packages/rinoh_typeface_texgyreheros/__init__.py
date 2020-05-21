from os import path

from rinoh.font import Typeface
from rinoh.font.style import REGULAR, BOLD, ITALIC, CONDENSED
from rinoh.font.opentype import OpenTypeFont


__all__ = ['typeface']


def otf(style, variant=''):
    filename = 'texgyreheros{}-{}.otf'.format(variant, style)
    return path.join(path.dirname(__file__), filename)


typeface = Typeface('TeX Gyre Heros',
                    OpenTypeFont(otf('regular'), weight=REGULAR),
                    OpenTypeFont(otf('italic'), weight=REGULAR, slant=ITALIC),
                    OpenTypeFont(otf('bold'), weight=BOLD),
                    OpenTypeFont(otf('bolditalic'), weight=BOLD, slant=ITALIC),
                    OpenTypeFont(otf('regular', 'cn'),
                                 width=CONDENSED, weight=REGULAR),
                    OpenTypeFont(otf('italic', 'cn'),
                                 width=CONDENSED, weight=REGULAR, slant=ITALIC),
                    OpenTypeFont(otf('bold', 'cn'),
                                 width=CONDENSED, weight=BOLD),
                    OpenTypeFont(otf('bolditalic', 'cn'),
                                 width=CONDENSED, weight=BOLD, slant=ITALIC))
