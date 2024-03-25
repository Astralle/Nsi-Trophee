"""
fonction permettant de définir l'état de certaines cases de la carte
"""

# functions
# =========
def special(grid_width, grid_height):
    """
    Make some tiles do certain action:

    0 (not calling the tiles) : You can move freely on the tile
    de 1 à 12 : niveaux
    de 21 à 32 : suite niveaux (niveau +20)
    de 40 à 44 : dialogues hors niveau (40 et +)
    -2 : maisons vides
    de -3 à -15 : pancartes

    params
    ------
    grid_width (int) : width of the 2D plane
    grid_height (int) : height of the 2D plane
    
    return
    ------
    a 2D plane with special action applied
    """
    #create the 2D plan
    marked_tiles = [[0] * grid_width for _ in range(grid_height)]

    # définit les tuiles bloquées, menant à un batiment ou permettant d'interagir avec un panneau
    with open('all_texts/special_tiles.txt') as definitions :
        exec(definitions.read())
        definitions.close()

    return marked_tiles
