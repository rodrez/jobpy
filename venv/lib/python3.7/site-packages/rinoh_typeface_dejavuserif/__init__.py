from os import path

from rinoh.font import Typeface
from rinoh.font.style import REGULAR, BOLD, ITALIC, CONDENSED
from rinoh.font.opentype import OpenTypeFont


__all__ = ['typeface']


def otf(style):
    filename = 'DejaVuSerif{}.ttf'.format(style)
    return path.join(path.dirname(__file__), filename)


typeface = Typeface('DejaVu Serif',
                    OpenTypeFont(otf(''), weight=REGULAR),
                    OpenTypeFont(otf('-Italic'), weight=REGULAR, slant=ITALIC),
                    OpenTypeFont(otf('-Bold'), weight=BOLD),
                    OpenTypeFont(otf('-BoldItalic'), weight=BOLD, slant=ITALIC),
                    OpenTypeFont(otf('Condensed'), weight=REGULAR,
                                 width=CONDENSED),
                    OpenTypeFont(otf('Condensed-Italic'), weight=REGULAR,
                                 slant=ITALIC, width=CONDENSED),
                    OpenTypeFont(otf('Condensed-Bold'), weight=BOLD,
                                 width=CONDENSED),
                    OpenTypeFont(otf('Condensed-BoldItalic'), weight=BOLD,
                                 slant=ITALIC, width=CONDENSED))
