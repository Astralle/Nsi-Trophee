"""
S'occupe de creer la police du codex
"""

from PyQt5.QtGui import QFontDatabase, QFont
from constantes import FONT_FILE_CODEX

font_id = QFontDatabase.addApplicationFont(FONT_FILE_CODEX)

def font_codex(taille : int, souligne : bool, gras : bool) :
    """

    Parameters
    ----------
    taille : un int pour la taille de la police
    souligne : un booleen pour savoir si la police est soulignée ou non
    gras : un booleen pour savoir si la police est en gras ou non

    Returns une police
    -------

    """
    font = QFont(QFontDatabase.applicationFontFamilies(font_id)[0])
    font.setPointSize(taille)
    font.setUnderline(souligne)
    font.setBold(gras)
    return font


FONT_TITRE_CODEX = font_codex(25, True, True)
FONT_SOUS_TITRE_CODEX = font_codex(18, True, False)
FONT_CODEX = font_codex(12, False, False)