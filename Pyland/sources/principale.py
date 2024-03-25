"""
Programme principal, celui qui sera exécuté.
"""

# imports
# =======
from interface_pyqt5 import creer_interface, app
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QRectF
import io, contextlib

# constants
from constante_son import *
from pnj import dico_pnj

# load
import progression_base

# globals imports
from fonctions_liens import *
from niveaux import liste_niveaux
from dialogues import dico_dialogue

# globals
# =======
background_position = ORIGIN_MAP
player_pos = ORIGIN_PLAYER
etat_dialogue = {'niveau' : 0, 'option' : 0, 'avancement' : 0}

level = {
    "current": {},
    "finished": False,
    "player in": False
}


# functions
# =========

def niveau_actuel() :
    """Renvoie le niveau lié à la case sur laquelle se trouve le joueur
    """
    return RESTRICTED_TILES[player_pos[1]][player_pos[0]]

def executer(interface : dict) -> None :
    """
    Exécute le code écrit par l'utilisateur en cas de niveau, de combat ou juste normalement

    Args:
        zone_texte (QTextEdit): La zone d'édition où l'utilisateur a écrit du code
        terminal (QTextEdit): Le terminal dans lequel on affiche les résultats
    """
    if level["player in"]:
        executer_en_level(interface)
    else:
        executer_par_defaut(interface)


def executer_par_defaut(interface : dict) -> None :
    """
    Exécute le code écrit par l'utilisateur sans niveau.

    Params
    ------
    zone_texte (QTextEdit) : La zone d'édition où l'utilisateur a écrit du code
    terminal (QTextEdit): Le terminal dans lequel on affiche les résultats
    """
    terminal = interface['terminal']
    print_terminal(terminal, "Aldirien vous avait déjà dit qu'il était inutile de lancer des sorts quand on a pas de problème a résoudre.", couleur = QColor(255, 0, 0))
    texte = interface['zone_texte'].toPlainText()
    if is_legal(texte) :
        try:
            # On renvoie stdout dans un StringIO buffer
            stdout_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer):
                exec(texte, {})
            output = stdout_buffer.getvalue()
        except Exception as e:
            # ERREUR !!!
            pass
        else:
            print_terminal(terminal, output.strip(), couleur = QColor(255, 255, 255))
    print_terminal(terminal, "Fin du sort.", couleur = QColor(255, 0, 0))
    print_terminal(terminal, "\n")


def executer_en_level(interface : dict) -> None:
    """
    Exécute le code écrit par l'utilisateur pendant les niveaux.

    Param
    ------
    zone_texte (QTextEdit) : La zone d'édition où l'utilisateur a écrit du code
    """
    zone_texte = interface['zone_texte']
    terminal = interface['terminal']
    texte = zone_texte.toPlainText()
    for i in range(len(level["current"]['tests'])):
        test_script = texte + '\n' + level["current"]['tests'][i]
        fonctionne, output = return_executer(test_script)
        if fonctionne:
            if output == level["current"]['réponses'][i]:
                continue
            else:
                texte_terminal = f"""Votre sort est incorrect, il ne renvoie pas la bonne valeur !
Test : {level["current"]['tests'][i]}
Résultat : {output}
Résultat attendu : {level["current"]['réponses'][i]}"""
                print_terminal(terminal, texte_terminal, couleur= QColor(255, 0, 0))
                perdre_vie(2, interface)
                break
        else:
            if output == "":
                print_terminal(terminal, "Vous avez utlisé des formules interdites !\nimport, exec() et open() sont interdits.", couleur = QColor(255, 0, 0))
                perdre_vie(1, interface)
            else:
                print_terminal(terminal, f"Erreur: \n{output}", couleur = QColor(255, 0, 0))
                perdre_vie(1, interface)
            break
    else:
        # Si tout est bon
        print_terminal(terminal, f"\nBravo ! Vous avez réussi !\npressez escape pour quitter le niveau.", couleur = QColor(0, 255, 0))
        zone_texte.clear()
        level["finished"] = True
    print_terminal(terminal, "\n")

def return_executer(texte_python : str) -> tuple[bool, str]:
    """Exécute le code python donné.

    Args:
        texte_python (str): Le texte en python à exécuter

    Returns:
        bool: Si le code s'est bien exécuter
        str: L'output si il s'est exécuter
        Exception à la place de str: Quand le code cause une erreur
    """
    if is_legal(texte_python) :
        try:
            # On renvoie stdout dans un StringIO buffer
            stdout_buffer = io.StringIO()
            with contextlib.redirect_stdout(stdout_buffer):
                exec(texte_python, {})
            output = stdout_buffer.getvalue()
        except Exception as e:
            return (False, e)
        else:
            return (True, output.strip())
    return (False, "")


def redessiner(interface : dict, images : dict) -> None :
    """
    Gère l'affichage de la carte et du personnage.
    
    Params
    ------
    jeu (QWidget) : La zone de jeu où s'affiche la carte
    images (dict[str : QPixmap]) : Le dictionnaire contenant les QPixmap du background et du player
    """
    width = VIEWPORT_WIDTH * TILE_SIZE[0]
    height = VIEWPORT_HEIGHT * TILE_SIZE[1]
    taille = interface["jeu"].width()
    ratio = height/width
    targets["background"] = QRectF(0, 0, taille, ratio * taille)
    sources["background"] = QRectF(background_position[0] * width, background_position[1]*height, width, height)
    pos_x = player_pos[0] % VIEWPORT_WIDTH
    pos_y = player_pos[1] % VIEWPORT_HEIGHT
    tile_affichee = taille / VIEWPORT_WIDTH
    targets["player"] = QRectF(pos_x * tile_affichee, pos_y * tile_affichee, tile_affichee, tile_affichee)
    sources["player"] = QRectF(0.0, 0.0, images["player"].width(), images["player"].height())
    painter = QPainter(interface["jeu"])
    painter.drawPixmap(targets["background"], images["background"], sources["background"])
    painter.drawPixmap(targets["player"], images["player"], sources["player"])
    painter.drawPixmap(targets["background"], images["calque"], sources["background"])
    # affichage des pnj
    for pos, pnj in dico_pnj.items():
        if pos[0] // VIEWPORT_WIDTH == background_position[0] \
        and pos[1] // VIEWPORT_HEIGHT == background_position[1] \
        and pnj["condition"]:
            if pos == (0, 0): continue
            pnj_x = pos[0] % VIEWPORT_WIDTH
            pnj_y = pos[1] % VIEWPORT_HEIGHT
            pnj_target = QRectF(pnj_x * tile_affichee, pnj_y * tile_affichee, tile_affichee, tile_affichee)
            painter.drawPixmap(pnj_target, pnj["image"], sources["player"])


def movement(event : QKeyEvent, disposition : QVBoxLayout) -> None :
    """
    Interprète les évènements provoqués par l'utilisateur sur la zone de jeu et change
    les la position du joueur et du fond en conséquence.

    Params
    ------
    event (QKeyEvent) : L'évènement provoqué par l'utilisateur
    """
    action = MOVES.get(event.key(), False)
    if action :
        if can_move_to((player_pos[0] + action[0], player_pos[1] + action[1])) :
            player_pos[0] += action[0]
            player_pos[1] += action[1]
            viewport = (VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
            background_position[0] = player_pos[0] // viewport[0]
            background_position[1] = player_pos[1] // viewport[1]
            niveau = niveau_actuel()
            if niveau > 0 or niveau < -1:
                commencer_dialogue(disposition, niveau)
        else :
            SON_INACCESSIBLE.play()


def trigger_niveau(event : QKeyEvent, interface : dict) -> None:
    """
    Quand l'utilisateur appuie sur la touche entrée, le niveau de la case
    sur laquelle il se trouve est lancé

    Params
    ------
    event (QKeyEvent) : L'évènement provoqué l'utilisateur
    interface (dict) : Le dictionnaire contenant tous les éléments de l'interface
    """
    if event.key() != Qt.Key_Escape:
        niveau = search_level_on_current(player_pos, interface)
        if not level["player in"] and 1 <= niveau <= len(liste_niveaux) and liste_niveaux[niveau]['condition'] :
            changer_son(interface["son_principal"], interface["son_battle"])
            level["player in"] = True
            level["current"] = liste_niveaux[niveau]
            print("Le joueur est rentré dans un niveau", player_pos)
            changement_niveau(level["current"]['message_id'], interface)

def sortir_niveau(event, interface) :
    if event.key() == Qt.Key_Escape:
        if level["player in"] and level["finished"]:
            changer_son(interface["son_battle"], interface["son_principal"])
            print("Le joueur a fini le niveau !")
            update_condition_niveau(level['current']['message_id'])
            update_condition_pnj(level['current']['message_id'] +100) # on rajoute 100 lorsqu'on déclenche en fin de niveau et non en fin de dialogue (cf pnj.py)
            level["player in"] = False
            level["finished"] = False
            changement_niveau(0, interface)
            save_all()
            if dico_dialogue.get(level['current']['message_id'] + 20, False):
                commencer_dialogue(interface['dialogue'], level['current']['message_id'] + 20)
            print(level['current']['message_id'] in (4, 6, 12, 13, 14, 15))
            if level['current']['message_id'] in (4, 6, 12, 13, 14, 15):
                trigger_suite_niveau(interface, level['current']['message_id'])

def trigger_suite_niveau(interface, niveau):
    """
    semblable a trigger_niveau, mais concue pour lancer uniquement les niveaux en suivant d'autre. Elle n'est donc appelée
    qu'à la fin d'un précédent niveau et non durant les déplacements du joueur, et prends comme paramètre supplémentaire
    niveau (int) : le niveau qui demande le lancement d'une suite.
    De plus, le paramètre event est retiré.
    """
    # assignement du niveau suivant correspondant
    if niveau in (12, 13, 14, 15):
        niveau += 1
    elif niveau == 4:
        niveau = 17
    elif niveau == 6:
        niveau = 18
    # lancement du niveau demandé
    if not level["player in"] and liste_niveaux[niveau]['condition'] :
        changer_son(interface['son_principal'], interface['son_battle'])
        level['player in'] = True
        level['current'] = liste_niveaux[niveau]
        changement_niveau(level['current']['message_id'], interface)
    # problème sur le changment de condition de pnj a l'issue de ces niveaux

def update_condition_niveau(niveau : int):
    """
    change les conditions suivantes
    - affichage dialogues
    - déclenchement niveaux
    - conditions du dico_progression de progression_base

    params
    ------
    niveau (int) : le niveau qui cause l'update
    """
    # update condition niveau
    liste_niveaux[niveau]['condition'] = False
    progression_change = liste_niveaux[niveau]['progression']
    if progression_change != 'aucune':
        progression_base.dico_progression[progression_change] = not(progression_base.dico_progression[progression_change])
    # transformation des niveaux suivis en dialogues suivis
    if niveau == 17: # suite niveau 4
        niveau = 24
    elif niveau == 18: # suite niveau 6
        niveau = 24
    elif niveau == 16: # suite niveau 12 (dernière de ses 4 suites)
        niveau == 32
    # update condition dialogue
    dico_dialogue[niveau]['condition'] = False

def update_condition_pnj(niveau : int):
    """
    change les conditions suivantes
    - affichage pnj
    - conditions du dico_progression de progression_base

    params
    ------
    niveau (int) : le niveau qui cause l'update
    """
    for pnj_coord in dico_pnj.keys():
        if niveau in dico_pnj[pnj_coord]['niveau']:
            dico_pnj[pnj_coord]['condition'] = not(dico_pnj[pnj_coord]['condition'])

def search_level_on_current(player_pos, interface):
    """

    """
    if (level_id := RESTRICTED_TILES[player_pos[1]][player_pos[0]]) < 1:
        level_id = 0
    if level_id == 1 and liste_niveaux[1]['condition']:
        zone_texte = interface["zone_texte"]
        zone_texte.clear()
        zone_texte.setText("""def est_creature(chose):
    return 0 #Le code ne fonctionne pas, à vous de le changer""")
    return level_id

def action_utilisateur(event : QKeyEvent, interface : dict) -> None :
    """
    Toutes les touches pressées par l'utilisateur passent par cette fonction
    et ces évènements sont redirigés vers le bon élément de l'interface en fonction
    du focus.

    Params
    ------
    event (QKeyEvent) : L'évènement provoqué par l'utilisateur c'est à dire la touche qui a été pressée
    interface (dict) : Le dictionnaire contenant tous les éléments de l'interface
    """
    if interface["zone_texte"].hasFocus() or level["player in"]:
        interface["zone_texte"].keyPressEvent(event)
    else:
        movement(event, interface['dialogue'])
        interface["jeu"].update()
        trigger_niveau(event, interface)
    sortir_niveau(event, interface)


def creer_liens(interface : dict) -> None:
    """
    Lie des évènements à des actions spécifiques.

    params
    ------
    interface (dict) : Le dictionnaire contenant tous les éléments de l'interface
    """
    interface["fenêtre"].keyPressEvent = lambda event: action_utilisateur(event, interface)
    images = {"background" : QPixmap(r'images/background.png'),
              "player" : QPixmap(r'encounters/player_f.png'),
              "calque" : QPixmap(r'images/foreground.png')}
    interface["jeu"].paintEvent = lambda event : redessiner(interface, images)
    interface["bouton_lancer"].clicked.connect(lambda : executer(interface))
    acceder_element(interface["dialogue"], 'bouton').clicked.connect(lambda : suite_dialogue(interface["dialogue"], interface["jeu"]))
    interface["jeu"].super_mousePressEvent = interface['jeu'].mousePressEvent
    

def trouver_choix(selected_dialogue : dict, spin_box : QSpinBox) -> int:
    """
    Renvoie l'option sélectionnée

    Params
    -------
    selected_dialogue (dict) : Le dictionnaire contenant le dialogue en cours et toutes les inforamtions le concernant.
    spin_box (QSpinBox) : La spin box dans laquelle l'utilisateur choisit l'option qu'il souhaite
    
    Return
    -------
    int : Le numéro de l'option choisit par le joueur
    """
    if selected_dialogue['type_choix'] == 'spin_box' :
        return spin_box.value()
    else :
        return 1

def suite_dialogue(disposition : QVBoxLayout, jeu : QWidget) -> None :
    """
    Continue le dialogue. Appelé lorsque le bouton 'Suite' est cliqué.
    
    Param
    -------
    disposition (QHBoxLayout) : La disposition contenant tous les éléments pour dialoguer
    """
    selected_dialogue = dico_dialogue[etat_dialogue['niveau']]
    dialogue = selected_dialogue['dialogue']
    if len(dialogue[etat_dialogue["option"]]) > etat_dialogue['avancement'] + 1 :
        etat_dialogue['avancement'] += 1
        texte = dialogue[etat_dialogue["option"]][etat_dialogue['avancement']]
        changer_dialogue(disposition, texte)
    elif etat_dialogue["option"] == 0 and selected_dialogue["nb_options"]:
        etat_dialogue["option"] = trouver_choix(selected_dialogue, acceder_element(disposition, 'spin_box'))
        etat_dialogue["avancement"] = 0
        texte = dialogue[etat_dialogue["option"]][etat_dialogue['avancement']]
        changer_dialogue(disposition, texte)
        cacher_spin_box(disposition)
    else :
        cacher_dialogue(disposition)
        update_condition_pnj(etat_dialogue['niveau'])
        save_all()
        jeu.setFocus()
    # Si le dialogue en est au moment ou le joueur doit faire un choix
    if selected_dialogue['nb_options'] and not etat_dialogue["option"] and etat_dialogue["avancement"] == len(dialogue[etat_dialogue["option"]]) - 1 :
        if selected_dialogue['type_choix'] == 'spin_box' :
            montrer_spin_box(disposition, selected_dialogue['nb_options'])

def commencer_dialogue(disposition : QVBoxLayout, niveau : int):
    """
    Commence le dialogue correspondant à la case sur laquelle se trouve le joueur.

    Param
    ------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    niveau (int) : Le niveau du dialogue a lancer
    """    
    num_dialogue = niveau
    if dico_dialogue[num_dialogue]['condition']:
        if num_dialogue < -1 :
            bouton_panneau(disposition)
        else :
            bouton_pnj(disposition)
        texte = dico_dialogue[num_dialogue]['dialogue'][0][0]
        etat_dialogue['niveau'] = num_dialogue
        etat_dialogue['option'] = 0
        etat_dialogue['avancement'] = 0
        changer_dialogue(disposition, texte)
        montrer_dialogue(disposition)


def save_all():
    save = open("all_texts/save.txt", "w") # augmente les performances
    separator = "/"
    temp = (
            str(vie_joueur) +
            str(separator) +
            str(player_pos[0]) +
            str(separator) +
            str(player_pos[1]) +
            str(separator) +
            str(background_position[0]) +
            str(separator) +
            str(background_position[1]) +
            str(separator) +
            str(progression_base.dico_progression['start_game']) +
            str(separator) +
            str(progression_base.dico_progression["ambuscade_gobelin"]) +
            str(separator) +
            str(progression_base.dico_progression["farore_libre"]) +
            str(separator) +
            str(progression_base.dico_progression["araigne_revele"]) +
            str(separator) +
            str(progression_base.dico_progression["araigne_vivante"]) +
            str(separator) +
            str(progression_base.dico_progression["scorpion_calme"]) +
            str(separator) +
            str(progression_base.dico_progression["undead_revele"]) +
            str(separator) +
            str(progression_base.dico_progression["undead_vivant"]) +
            str(separator) +
            str(progression_base.dico_progression["mage_infiltre"]) +
            str(separator) +
            str(progression_base.dico_progression["parz_karl_vivant"]) +
            str(separator) +
            str(progression_base.dico_progression["mage_teleporte"]) +
            str(separator) +
            str(progression_base.dico_progression["aldirien_vivant"]) +
            str(separator) +
            str(progression_base.dico_progression["saal_lio_arrive"]) +
            str(separator)
    )
    #print(temp)
    save.write(temp)
    save.close() # pour réduire les performances

# main
def main() :
    """La fonction principale du jeu. Elle lance l'exécution."""
    interface = creer_interface()
    creer_liens(interface)
    app.exec_()


main()
