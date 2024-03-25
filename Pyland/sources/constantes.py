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



ROUGE = QColor(255, 0, 0)
ROUGE_FONCE = QColor(144, 12, 40)
CYAN = QColor(28, 195, 173)
VIOLET = QColor(141, 29, 117)
GRIS = QColor(153, 153, 153)
BLEU_FONCE = QColor(38, 21, 232)
VERT = QColor(0, 197, 6)
DORE = QColor(232, 171, 29)
ORANGE = QColor(210, 100, 40)
VERT_POMME = QColor(37, 142, 0)
COULEURS = {"rouge" : ROUGE, "rouge_fonce" : ROUGE_FONCE, "cyan" : CYAN, "violet" : VIOLET, "gris" : GRIS, "bleu_fonce" : BLEU_FONCE,
            "vert" : VERT, "dore" : DORE, "orange" : ORANGE, "vert_pomme" : VERT_POMME}
HIGHLIGHTING_RULES : tuple[tuple[QRegExp, QColor, bool]] = (
                      (QRegExp("\\bfor\\b"), "rouge_fonce", True),
                      (QRegExp("\\bwhile\\b"), "rouge_fonce", True),
                      (QRegExp("\\bin\\b"), "rouge_fonce", True),
                      (QRegExp("\\bdef\\b"), "bleu_fonce", True),
                      (QRegExp("\\breturn\\b"), "bleu_fonce", True),
                      (QRegExp("\\bdel\\b"), "bleu_fonce", True),
                      (QRegExp("\\bclass\\b"), "bleu_fonce", True),
                      (QRegExp("\\bif\\b"), "rouge_fonce", True),
                      (QRegExp("\\belif\\b"), "rouge_fonce", True),
                      (QRegExp("\\belse\\b"), "rouge_fonce", True),
                      (QRegExp("\\bwith\\b"), "rouge_fonce", True),
                      (QRegExp("\\bas\\b"), "rouge_fonce", True),
                      (QRegExp("\\band\\b"), "vert", True),
                      (QRegExp("\\bor\\b"), "vert", True),
                      (QRegExp("\\bnot\\b"), "vert", True),
                      (QRegExp("\\bis\\b"), "violet", False),
                      (QRegExp("\\bNone\\b"), "violet", False),
                      (QRegExp("\\bTrue\\b"), "violet", False),
                      (QRegExp("\\bFalse\\b"), "violet", False),
                      (QRegExp("\\brange\\b"), "cyan", False),
                      (QRegExp("\\bprint\\b"), "cyan", False),
                      (QRegExp("\\bsplit\\b"), "cyan", False),
                      (QRegExp("\\binsert\\b"), "cyan", False),
                      (QRegExp("\\bcount\\b"), "cyan", False),
                      (QRegExp("\\bremove\\b"), "cyan", False),
                      (QRegExp("\\bextend\\b"), "cyan", False),
                      (QRegExp("\\bappend\\b"), "cyan", False),
                      (QRegExp("\\bindex\\b"), "cyan", False),
                      (QRegExp("\\bclear\\b"), "cyan", False),
                      (QRegExp("\\bopen\\b"), "cyan", False),
                      (QRegExp("\\bclose\\b"), "cyan", False),
                      (QRegExp("\\bcopy\\b"), "cyan", False),
                      (QRegExp("\\bsort\\b"), "cyan", False),
                      (QRegExp("\\bpop\\b"), "cyan", False),
                      (QRegExp("\\breverse\\b"), "cyan", False),
                      (QRegExp("\\binput\\b"), "cyan", False),
                      (QRegExp("\\bzip\\b"), "cyan", False),
                      (QRegExp("\\bget\\b"), "cyan", False),
                      (QRegExp("\\babs\\b"), "cyan", False),
                      (QRegExp("\\ball\\b"), "cyan", False),
                      (QRegExp("\\bany\\b"), "cyan", False),
                      (QRegExp("\\bbin\\b"), "cyan", False),
                      (QRegExp("\\bcallable\\b"), "cyan", False),
                      (QRegExp("\\bcapitalize\\b"), "cyan", False),
                      (QRegExp("\\bisaplpha\\b"), "cyan", False),
                      (QRegExp("\\bchoice\\b"), "cyan", False),
                      (QRegExp("\\bendswith\\b"), "cyan", False),
                      (QRegExp("\\bstartswith\\b"), "cyan", False),
                      (QRegExp("\\bisdigit\\b"), "cyan", False),
                      (QRegExp("\\bisupper\\b"), "cyan", False),
                      (QRegExp("\\bislower\\b"), "cyan", False),
                      (QRegExp("\\bistitle\\b"), "cyan", False),
                      (QRegExp("\\bisspace\\b"), "cyan", False),
                      (QRegExp("\\blower\\b"), "cyan", False),
                      (QRegExp("\\bupper\\b"), "cyan", False),
                      (QRegExp("\\bfind\\b"), "cyan", False),
                      (QRegExp("\\bjoin\\b"), "cyan", False),
                      (QRegExp("\\blstrip\\b"), "cyan", False),
                      (QRegExp("\\brstrip\\b"), "cyan", False),
                      (QRegExp("\\bstrip\\b"), "cyan", False),
                      (QRegExp("\\bisdecimal\\b"), "cyan", False),
                      (QRegExp("\\bformat\\b"), "cyan", False),
                      (QRegExp("\\bmap\\b"), "cyan", False),
                      (QRegExp("\\benumerate\\b"), "cyan", False),
                      (QRegExp("\\bexec\\b"), "cyan", False),
                      (QRegExp("\\beval\\b"), "cyan", False),
                      (QRegExp("[=-\*\+/%]"), "gris", False),
                      (QRegExp("[0-9_]+"), "dore", False),
                      (QRegExp("=="), "gris", False),
                      (QRegExp("<="), "gris", False),
                      (QRegExp(">="), "gris", False),
                      (QRegExp(">"), "gris", False),
                      (QRegExp("<"), "gris", False),
                      (QRegExp("!="), "gris", False),
                      (QRegExp("\[|\]|\(|\)|\{|\}"), "vert_pomme", False),
                      (QRegExp("#[^\\n]*"),"gris", False),
                      (QRegExp("={3,}|[-+*%]{2,}|/{3,}"), "rouge", False),  # à partir d'ici, il s'agit d'erreurs
                      (QRegExp("=[<>!-*+\\\/%]+"), "rouge", False),
                      (QRegExp("[<>!/%-+*\]+=="), "rouge", False),
                      (QRegExp("[^a-zA-Z]+\\d+[a-zA-Z]+"), "rouge", False),
                      (QRegExp("(\([^)\"']*(\]|\}))|((\[|\{)[^(\"']*\))"), "rouge", False),
                      (QRegExp("(\[[^\]\"']*\})|(\{[^\[\"']*\])"), "rouge", False),
                      (QRegExp("\\brange\\b\( *\)"), "rouge", False),
                      (QRegExp("\\brange\\b\(\".*\)"), "rouge", False),
                      (QRegExp("(?\\bdef\\b)[^a\\n:]*a(\\n|\\r)"), "rouge", False),
                      (QRegExp("\"[^\"]*\""), "orange", False),             # sauf ces deux dernières expressions
                      (QRegExp("\'[^\']*\'"), "orange", False),             # qui gèrent la coloration des strings
                      )

HIGHLIGHTING_NIVEAU = {
    1 : QRegExp("\\b(est_creature)\\b"),
    2 : QRegExp("\\b(evaluation_gobelin)\\b"),
    3 : QRegExp("\\b(pierre_cassable)\\b"),
    4 : QRegExp("\\b(trouver_squelette)\\b"),
    5 : QRegExp("\\b(inverse_dialogue)\\b"),
    6 : QRegExp("\\b(araignee_euler)\\b"),
    7 : QRegExp("\\b(est_pangramme)\\b"),
    8 : QRegExp("\\b(mystere)\\b"),
    9 : QRegExp("\\b(decrypte_cesar)\\b"),
    10 : QRegExp("\\b(passage_possible)\\b"),
    11 : QRegExp("\\b(nombre_riposte)\\b"),
    12 : QRegExp("\\b(bloque_anagramme)\\b"),
    13 : QRegExp("\\b(melange)\\b"),
    14 : QRegExp("\\b(is_fibonacci)\\b"),
    15 : QRegExp("\\b(retourne_sort)\\b")
}

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