"""
Toutes les fonctions n'ayant pas de liens avec l'interface et pouvant être utilisé n'importe où.
Ne pose aucun problème d'importation dans les autres fichiers expecté dans les fichiers
'constantes' et 'addon_marked_tiles.py'

programme : Lou Schanen
dernière version : 01/03/2024 10:15
"""
from constantes import *
from math import ceil
TEXT = "Narrateur\n\nVous attendez devant ce feu de camp depuis quelque instant, lorsqu'un vieil homme approche. Il s'agit de votre mentor, celui que vous appelez Master Aldirien.\nMaster Aldirien\n\nSalut a toi, jeune apprenti{0}. Voyons si tu a en mémoire ce que nous avons appris dans la bibliothèque.\nMaster Aldirien\n\nPour lancer des sorts, tu dois écrire du code python dans l'encadré blanc à ta droite.\nMaster Aldirien\n\nTu en aura besoin a chaque fois qu'un niveau va démarrer. Lorsque ce sera le cas, l'énoncé expliquant ce que tu dois faire s'affichera au dessus de l'encadré blanc.\nMaster Aldirien\n\nLe résultat de tes sorts se voit sur notre monde, mais aussi dans le plan arcanique du terminal. C'est l'encadré noir sous la carte. Tu y verra les retours concrets de tes sorts, dont les explications si ça ne marche pas."


def is_legal(texte : str) -> bool :
    """Renvoie si l'utilisateur a ou non respecté les restrictions que lui sont imposées.

    Args:
        texte (str): Le code de l'utilisateur

    Returns:
        bool : Si le code de l'utilisateur respecte les restrictions ou non
    """
    for interdit in BLACKLIST :
        if interdit.indexIn(texte) != -1:
            print("NON")
            return False
    return True

def is_exist(iterable, index: int, *tests : str) -> bool :
    """Regarde si iterable[index] existe et s'il est un des strings tests

    Args:
        iterable (liste/tuple/iterable): la liste itérable
        index (int): l'indice
        *tests (str): Les différentes valeurs de iterable[index] possible

    Returns:
        bool: iterable[index] in test
    """
    if index < 0 :
        if -len(iterable) <= index:
            return iterable[index] in tests
    else :
        if len(iterable) > index:
            return iterable[index] in tests
    return False

def can_move_to(position : tuple[int,int]) -> bool :
    """
    check if the position is not marked on the grid as 1 and so if the player can move to that position
    :param position: the position to test
    :return: a boolean indicating whether the position is marked or not
    """
    alpha, beta = position
    blocked_case = (0 <= alpha < GRID_WIDTH and 0 <= beta < GRID_HEIGHT and RESTRICTED_TILES[beta][alpha] != -1)
    if not blocked_case:
        print("Player tried to move to a blocked tile " + str(position))
    return blocked_case

def taille_prochain_mot(reste : str) -> int:
    for i in range(len(reste)) :
        if reste[i] in (' ', '\n') :
            return i
    return len(reste)

def multi_split(texte : str, taille : int, *sep : str) -> list[str]:
    liste = []
    ligne = ''
    compte = 0
    for i in range(len(texte)) :
        taille_mot = 0
        if texte[i] == ' ' :
            taille_mot = taille_prochain_mot(texte[i+1:])
        if texte[i] in sep or texte[i] == '\n' or compte + taille_mot >= taille :
            liste.append(ligne + '\n')
            ligne = ''
            compte = 0
        elif compte == taille or i + 1 == len(texte):
            ligne += texte[i]
            liste.append(ligne + '\n')
            ligne = ''
            compte = 0
        else :
            ligne += texte[i]
            compte += 1
    return liste