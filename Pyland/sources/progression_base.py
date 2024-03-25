"""
Comporte toutes les globales relatives à l'avancée en jeu du joueur.
Ligne de save de base : 20/4/3/0/0/False/False/True/False/True/False/False/True/False/True/False/True/False/
"""

dico_progression = {
    'start_game': False,
    # change après le niveau 1
    'ambuscade_gobelin': True,
    # change après le niveau 2, peut importe le lieu de réalisation
    'farore_libre': False,
    # change après le niveau 3
    'araigne_revele': False,
    # change après le niveau 6 part 1 (révélation)
    'araigne_vivante': True,
    # change après le niveau 6 part 2 (combat)
    'scorpion_calme': False,
    # change après le niveau 7
    'undead_revele': False,
    # change après le niveau 4 part 1 (révélation)
    'undead_vivant': True,
    # change après le niveau 4 part 2 (combat)
    'mage_infiltre': False,
    # change après le niveau 10
    'parz_karl_vivant': True,
    # change après le niveau 11 part 1 (combat)
    'mage_teleporte': False,
    # change au début du niveau 11 part 2 (téléportation)
    'aldirien_vivant': True,
    # change après le niveau 12. Jeu terminé.
    'saal_lio_arrive': False,
    # apparition de Saal-lio au début du combat, donc à la fin du dialogue
}
