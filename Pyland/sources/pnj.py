"""
dictionnaire de pnj contenant
- en clé la position des pnj
- en valeur un dictinnaire avec image et condition d'affichage
"""
from constantes import dico_saved_var
from PyQt5.QtGui import QPixmap

# 1 à 12 et 21 à 31 déclenchement à la fin d'un dialogue
# 36 déclenchement à la fin du dialogue du dernier niveau (coupé en 5 parties de 12 à 16)
# on rajoute 100 lorsqu'on veut déclencher à la fin d'un niveau.
# attention : les suites des niveau 4 et 6 sont 17 et 18.

dico_pnj = { # aldirien - camp du début
    (5, 2) : {
        'image' : QPixmap('encounters/npc/aldirien.png'),
        'condition' : not(dico_saved_var['start_game']),
        'niveau': (21,) # fin du dialogue suite 1
    }, # gobelins sud
    (7, 24) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['ambuscade_gobelin'],
        'niveau': (102,) # fin du niveau 2
    },
    (13, 25) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['ambuscade_gobelin'],
        'niveau': (102,) # fin du niveau 2
    },
    (14, 22) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['ambuscade_gobelin'],
        'niveau': (102,) # fin du niveau 2
    }, # gobelins est
    (29, 3) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['ambuscade_gobelin'],
        'niveau': (102,) # fin du niveau 2
    },
    (36, 4) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['ambuscade_gobelin'],
        'niveau': (102,) # fin du niveau 2
    },
    (33, 0) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['ambuscade_gobelin'],
        'niveau': (102,) # fin du niveau 2
    }, # Farore - sous les briques
    (15, 33) : {
        'image' : QPixmap('encounters/npc/farore_pierre.png'),
        'condition' : not(dico_saved_var['farore_libre']),
        'niveau': (103,) # fin du niveau 3
    }, # Farore - libre
    (14, 33) : {
        'image' : QPixmap('encounters/npc/farore.png'),
        'condition' : dico_saved_var['farore_libre'],
        'niveau': (23,)  # fin du dialogue suite 3
    }, # Balmac
    (14, 45) : {
        'image' : QPixmap('encounters/npc/balmac.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # Gurun
    (14, 42) : {
        'image' : QPixmap('encounters/npc/gurun.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # Kheïa - forêt de Darkwod
    (35, 42) : {
        'image' : QPixmap('encounters/npc/kheia.png'),
        'condition' : dico_saved_var['undead_vivant'],
        'niveau': (37,) # fin du dialogue suite de suite 4
    }, # squelettes Darkwod
    (36, 40) : {
        'image' : QPixmap('encounters/creatures/undead.png'),
        'condition' : dico_saved_var['undead_revele'] and dico_saved_var['undead_vivant'],
        'niveau': (24, 117) # fin du dialogue suite 4 et fin niveau suite 4
    },
    (31, 44) : {
        'image' : QPixmap('encounters/creatures/undead2.png'),
        'condition' : dico_saved_var['undead_revele'] and dico_saved_var['undead_vivant'],
        'niveau': (24, 117) # fin du dialogue suite 4 et fin niveau suite 4
    },
    (24, 43) : {
        'image' : QPixmap('encounters/creatures/undead2.png'),
        'condition' : dico_saved_var['undead_revele'] and dico_saved_var['undead_vivant'],
        'niveau': (24, 117) # fin du dialogue suite 4 et fin niveau suite 4
    },
    (28, 46) : {
        'image' : QPixmap('encounters/creatures/undead.png'),
        'condition' : dico_saved_var['undead_revele'] and dico_saved_var['undead_vivant'],
        'niveau': (24, 117) # fin du dialogue suite 4 et fin niveau suite 4
    }, # elementaire de feu
    (2, 64) : {
        'image' : QPixmap('encounters/creatures/fire_elemental.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    },
    (4, 65) : {
        'image' : QPixmap('encounters/creatures/fire_elemental.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # Felria
    (41, 37) : {
        'image' : QPixmap('encounters/npc/felria.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # Parz-Karl et les orcs
    (67, 67) : {
        'image' : QPixmap('encounters/npc/parz_karl.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    },
    (61, 67) : {
        'image' : QPixmap('encounters/creatures/orc.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    },
    (68, 61) : {
        'image' : QPixmap('encounters/creatures/orc.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    },
    (69, 60) : {
        'image' : QPixmap('encounters/creatures/orc.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    },
    (71, 63) : {
        'image' : QPixmap('encounters/creatures/orc.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    },
    (67, 69) : {
        'image' : QPixmap('encounters/creatures/orc.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    },
    (63, 69) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    },
    (72, 61) : {
        'image' : QPixmap('encounters/creatures/gobelin.png'),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'niveau': (111,) # fin du niveau 11
    }, # Aldirien - dans la bibliothèque
    (9, 74) : {
        'image' : QPixmap('encounters/npc/aldirien.png'),
        'condition' : dico_saved_var['aldirien_vivant'],
        'niveau': (36,) # fin du dialogue suite 12
    }, # le mage - chemin vers la vallée orc
    (64, 60) : {
        'image' : QPixmap('encounters/npc/mage.png'),
        'condition' : not(dico_saved_var['mage_infiltre']),
        'niveau': (110,) # fin du niveau 10
    }, # le mage - devant Parz-Karl
    (69, 65) : {
        'image' : QPixmap('encounters/npc/mage.png'),
        'condition' : dico_saved_var['mage_infiltre'] and not(dico_saved_var['mage_teleporte']), #vaut false and not(false) au début, pourtant le mage est affiché. Si on relance le jeu, le bug n'apparaît plus.
        'niveau': (110, 31) # fin du dialogue suite 11
    }, # le mage - téléporté dans la bibliothèque
    (10, 72) : {
        'image' : QPixmap('encounters/npc/mage.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # Olkin
    (28, 15) : {
        'image' : QPixmap('encounters/npc/olkin.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # Endal
    (74, 15) : {
        'image' : QPixmap('encounters/npc/endal.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # Malone
    (65, 68) : {
        'image' : QPixmap('encounters/npc/malone.png'),
        'condition' : not(dico_saved_var['mage_teleporte']),
        'niveau': (31,) # fin du dialogue suite 11
    }, # l'entraineur
    (22, 78) : {
        'image' : QPixmap('encounters/npc/trainer.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # le spectre
    (44, 3) : {
        'image' : QPixmap('encounters/creatures/ghost.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # le scorpion
    (64, 41) : {
        'image' : QPixmap('encounters/creatures/scorpion.png'),
        'condition' : True,
        'niveau': (0,) # jamais
    }, # l'araignée
    (42, 7) : {
        'image' : QPixmap('encounters/creatures/spider.png'),
        'condition' : dico_saved_var['araigne_revele'] and dico_saved_var['araigne_vivante'],
        'niveau': (26, 118) # fin dialogue suite 6 et fin niveau suite 6
    }, # Saal-lio forme draconique
    (11, 74) : {
        'image' : QPixmap('encounters/npc/saal_lio_dragon.png'),
        'condition' : dico_saved_var['saal_lio_arrive'] and dico_saved_var['aldirien_vivant'],
        'niveau': (12, 116), # fin dialogue 12 et fin niveau 12
        'nb_tiles_largeur' : 3, # le nombre de tiles que prend le dragon
        'nb_tiles_hauteur' : 3, # il est le seul à avoir besoin de plus d'une tile donc à avoir ces 2 propriétés
    }, # pylinarium - ouvert
    (10, 75) : {
        'image' : QPixmap('encounters/artefacts/open_pylinarium.png'),
        'condition' : dico_saved_var['aldirien_vivant'],
        'niveau': (36,) # fin dialogue suite 12
    }, # pylinarium - fermé
    (10, 76) : {
        'image' : QPixmap('encounters/artefacts/closed_pylinarium.png'),
        'condition' : not(dico_saved_var['aldirien_vivant']),
        'niveau': (36,) # fin dialogue suite 12
    },
    (9, 45) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (11, 42) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (16, 43) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (5, 42) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (74, 10) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (78, 12) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (68, 13) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (70, 14) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (66, 18) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (64, 16) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (63, 12) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (58, 17) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (76, 18) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
    (70, 17) : {
        'image' : QPixmap('encounters/creatures/peasant.png'),
        'condition' : True,
        'niveau' : (0,) # jamais
    },
}