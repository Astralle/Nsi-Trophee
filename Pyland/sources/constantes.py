"""
Toutes les constantes nécessaires au projet
"""

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QColor, QFont
from addon_marked_tiles import special
from recall import recall

dico_saved_var = recall()

N_LIGNES = 10
TAILLE_POLICE = 11

FONT_NAME = 'MS Shell Dlg 2'


VIE_MAX = 20

#Noms de fichier
FICHIER_NIVEAUX = "all_texts/fichier_niveaux.txt"
FICHIER_UTILISATEUR = "fichier_utilisateur.py"
FICHIER_CODEX = "all_texts/fichier_codex.txt"
FICHIER_SON_INACCESSIBLE = r'sounds/son_choc.wav'
FICHIER_SON_PRINCIPAL = r"sounds/adventure.mp3"
FICHIER_SON_BATTLE = r"sounds/battle.mp3"
FICHIER_SON_DEATH = r'sounds/death.mp3'
FICHIER_SON_BOSS_FINAL = r'sounds/boss_time.mp3'
FONT_FILE_CODEX = 'fonts/Fondamento.ttf'


BLACKLIST = [QRegExp("(\\b|_)import(\\b|_)"), QRegExp("\\bexec *\\("), QRegExp("\\beval *\\(")]
GRID_WIDTH = 80
GRID_HEIGHT = 80
VIEWPORT_WIDTH = 20
VIEWPORT_HEIGHT = 10
TILE_SIZE = (32, 32)
LISTE_SPECIAL_ACTION = (2, 3, 4, 5, 6, 7, 8, 9, 10)
WIDTH, HEIGHT = VIEWPORT_WIDTH * TILE_SIZE[0], VIEWPORT_HEIGHT * TILE_SIZE[1]

RESTRICTED_TILES = special(GRID_WIDTH, GRID_HEIGHT)
ORIGIN_PLAYER = [dico_saved_var['player_pos_0'],dico_saved_var['player_pos_1']]
ORIGIN_MAP = [dico_saved_var['background_position_0'],dico_saved_var['background_position_1']]

# Feuilles de styles au format CSS
STYLE_DIALOGUE = "border: 6px solid; border-color: rgb(21, 132, 102); border-radius: 5%; background-color: rgb(180, 181, 185); padding: 20%;"
STYLE_BOUTON_PRESSE = "border : 2px solid black;"

MOVES ={Qt.Key_Up : (0, -1), Qt.Key_Down : (0, 1), Qt.Key_Left : (-1, 0), Qt.Key_Right : (1, 0)}

def my_font(taille : int, police : str, gras : bool = False) :
    """
    Défini la police d'écriture de toute l'interface.

    Return
    ------
        QFont : La police
    """
    font = QFont()
    font.setPointSize(taille)
    font.setFamily(police)
    font.setBold(gras)
    return font

POLICE = my_font(TAILLE_POLICE, FONT_NAME)
GRANDE_POLICE = my_font(TAILLE_POLICE + 2, FONT_NAME)
POLICE_COMMENCER = my_font(26, FONT_NAME, True)
POLICE_RESET = my_font(15, FONT_NAME, True)
POLICE_QUITTER = my_font(20, FONT_NAME, True)
