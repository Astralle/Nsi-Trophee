"""
Toutes les fonctions ayant un lien avec l'interface.
"""

# imports
# =======
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QProgressBar, QMessageBox
from PyQt5.QtGui import QTextCharFormat, QFont, QKeyEvent, QTextCursor
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtCore import Qt

# constants
from constantes import VIE_MAX, dico_saved_var
from constante_son import SON_INACCESSIBLE
from coloration import *

# globals
from fonctions_globales import *

targets = {}
sources = {}
vie_joueur = dico_saved_var['player_hp']

# functions
# =========
def indenter(zone_texte : QTextEdit, texte : str) -> None:
    """
    Ajoute une indentation dans l'éditeur de texte du jeu lorsqu'il le faut.

    Params
    ------
    zone_texte (QTextEdit): La zone de texte
    texte (str): Le texte de la zone de texte
    """
    curseur = zone_texte.textCursor()
    i = curseur.position() - 2
    while is_exist(texte, i, ' '):
        i -= 1
    if is_exist(texte, i, ":"):
        curseur.insertText('\t')
    lignes = texte.split('\n')
    curseur.insertText('\t' * lignes[curseur.blockNumber() - 1].count('\t'))

def mort(interface : dict) :
    changer_son(interface["son_principal"], interface["son_death"])
    changer_son(interface["son_boss_final"], interface["son_death"])
    message = QMessageBox()
    message.setText('\nNarrateur - Vous sentez une insoutenable douleur vous submerger, et soudain tout devient noir.\n\n'
                   'Mais de toute évidence, les divinités de Pyland ont encore besoin de vous, car dans le noir, un chuchotement se fait entendre...\n\n'
                   'Vous ne comprenez rien aux paroles discrètes, qui semblent venir de partout autour de vous.\n\n'
                   'Soudain, le monde réapparaît et les couleurs le remplissent petit à petit, passant d\'un noir et blanc peut contrasté à un tableau coloré.\n\n'
                   'Vous vous dites que vous avez mal abordé votre situation. Peut-être que votre Codex vous aidera a mieux la résoudre ?\n\n'
                   'Onyx - Je le sens qui revient.\n\n'
                   'Agath - Bonne chance à toi, joueur.\n')
    message.setStandardButtons(QMessageBox.Ok)
    message.exec_()
    changer_son(interface['son_death'], interface['son_principal'])
    interface['timer_vie'].start()


def perdre_vie(points_perdus : int, interface : dict) :
    """
    diminue la vie du jueur
    """
    SON_INACCESSIBLE.play()
    barre_vie = interface["barre_vie"]
    terminal = interface["terminal"]
    vie_actuelle = barre_vie.value()
    nouv_vie = vie_actuelle - points_perdus
    barre_vie.setValue(max(nouv_vie, 0))
    print_terminal(terminal, f"Votre sort échoue, vous subissez {points_perdus} dégâts.", f"Il ne vous reste plus que {nouv_vie}PV", couleur = QColor(255, 0, 0), sep='\n')
    if nouv_vie <= 0 :
        mort(interface)


def colorer(zone_texte : QTextEdit, texte : str, interface : dict) -> None:
    """
    Colore les mots clés d'un texte en fonction de HIGHLIGHTING_RULES

    params
    ------
    texte (str): Le texte que l'utilisateur a écrit
    """
    curseur = zone_texte.textCursor()
    curseur.setPosition(0)
    curseur.movePosition(curseur.Right, curseur.KeepAnchor, len(zone_texte.toPlainText()))
    char_format = QTextCharFormat()
    char_format.setForeground(Qt.black)
    char_format.setFontWeight(QFont.Normal)
    char_format.setUnderlineStyle(QTextCharFormat.NoUnderline)
    curseur.mergeCharFormat(char_format)
    for expression, couleur, epaisseur in HIGHLIGHTING_RULES :
        index = expression.indexIn(texte)
        while index != -1:
            length = expression.matchedLength()
            curseur.setPosition(index)
            curseur.movePosition(curseur.Right, curseur.KeepAnchor, length)
            char_format = QTextCharFormat()
            if epaisseur :
                char_format.setFontWeight(QFont.Bold)
            if couleur == "rouge" :
                # Le rouge étant utilisé pour indiquer une erreur, le texte sera également souligné par des vaguelettes
                char_format.setUnderlineStyle(QTextCharFormat.WaveUnderline)
            else :
                char_format.setUnderlineStyle(QTextCharFormat.NoUnderline)
            char_format.setForeground(COULEURS[couleur]) 
            curseur.mergeCharFormat(char_format)
            index = expression.indexIn(texte, index + length)
    expression = HIGHLIGHTING_NIVEAU.get(niveau_act(interface), False)
    if expression :
        index = expression.indexIn(texte)
        while index != -1:
            length = expression.matchedLength()
            curseur.setPosition(index)
            curseur.movePosition(curseur.Right, curseur.KeepAnchor, length)
            char_format = QTextCharFormat()
            char_format.setForeground(COULEURS["cyan"])
            curseur.mergeCharFormat(char_format)
            index = expression.indexIn(texte, index + length)


def autocompletion(zone_texte : QTextEdit, event : QKeyEvent) :
    """
    Complète automatiquement les parenthèses, les crochets, les accolades et les guillemets
    quand celui de gauche est ajouté.

    Params
    ------
    zone_texte (QTextEdit): La zone d'édition dans laquelle écrit le joueur
    event (QKeyEvent) : L'événement provoqué par le joueur
    """
    cle = event.key()
    curseur = zone_texte.textCursor()
    ajout = False
    if not event.text().isdigit() :
        if cle == Qt.Key_ParenLeft :
            curseur.insertText(')')
            ajout = True
        elif cle == Qt.Key_BracketLeft :
            curseur.insertText(']')
            ajout = True
        elif cle == Qt.Key_BraceLeft :
            curseur.insertText('}')
            ajout = True
        elif cle == Qt.Key_QuoteDbl :
            curseur.insertText('"')
            ajout = True
        elif cle == Qt.Key_Apostrophe :
            curseur.insertText("'")
            ajout = True
    if ajout :
        curseur = zone_texte.textCursor()
        curseur.setPosition(curseur.position() - 1)
        zone_texte.setTextCursor(curseur)

def ajout_double(element : str, curseur : QTextCursor) :
    position_debut = curseur.selectionStart()
    position_fin = curseur.selectionEnd() + 1
    texte = curseur.selectedText()
    curseur.setPosition(position_debut)
    curseur.insertText(element[0])
    curseur.setPosition(position_fin)
    curseur.insertText(element[1])
    curseur.setPosition(position_debut + 1)
    curseur.movePosition(curseur.Right, curseur.KeepAnchor, len(texte))

def entourer(zone_texte : QTextEdit, event : QKeyEvent) :
    cle = event.key()
    curseur = zone_texte.textCursor()
    ajout = False
    if not event.text().isdigit() :
        if cle == Qt.Key_ParenLeft :
            ajout_double('()', curseur)
            ajout = True
        elif cle == Qt.Key_BracketLeft :
            ajout_double('[]', curseur)
            ajout = True
        elif cle == Qt.Key_BraceLeft :
            ajout_double('{}', curseur)
            ajout = True
        elif cle == Qt.Key_QuoteDbl :
            ajout_double('""', curseur)
            ajout = True
        elif cle == Qt.Key_Apostrophe :
            ajout_double("''", curseur)
            ajout = True
    if ajout :
        #curseur.setPosition(curseur.position() - 1)
        zone_texte.setTextCursor(curseur)
    else :
        zone_texte.super_keyPressEvent(event)

def text_modifier(zone_texte : QTextEdit, event : QKeyEvent, interface : dict) -> None:
    """
    Est appelé quand le texte est modifié.
    Écrit ce que l'utilisateur tappe sur le clavier, ajoute l'indentation et la coloration et autocomplète.

    Params
    ------
    zone_texte (QTextEdit): La zone d'édition dans laquelle écrit le joueur
    event (QKeyEvent) : L'événement provoqué par le joueur
    """
    
    curseur = zone_texte.textCursor()
    if curseur.hasSelection() :
        entourer(zone_texte, event)
    else :
        zone_texte.super_keyPressEvent(event) # La méthode de base des zones de texte
        if not curseur.hasSelection() :
            autocompletion(zone_texte, event)
    if not (event.key() == 16777219): # Ne s'applique pas lorsque l'on efface
        texte = zone_texte.toPlainText()
        if event.text() in ('\n', '\r', ' ') :
            colorer(zone_texte, texte, interface)
        if event.text() in ('\n', '\r') :
            indenter(zone_texte, texte)
        


def niveau_act(interface : dict) -> int :
    """
    Renvoie le numéro du niveau actuel.
    Peut sembler identique à la fonction niveau_actuel du fichier principal.
    Cependant cette fonction renvoie le niveau affiché dans le coin supérieur droite,
    alors que la fonction niveau_actuel renvoie le niveau présent sur la case où se
    trouve le joueur. Ces deux résultats peuvent être identiques mais aussi complètement
    différents.
    Attention : cette fonction ne renvoie le numéro du niveau qu'une fois qu'il a été affiché dans le coin supérieur droit
    Attention : le premier niveau est 1 et non 0.

    Param
    ------
    pile_niveaux (QStackedWidget) : La pile contenant les niveaux
    
    Return
    ------
    int : Le niveau actuellement en cours
    """
    return interface["pile_niveaux"].currentIndex()


def changement_niveau(niveau : int, interface : dict) -> None :
    """
    Change le niveau dans la partie supérieur droite
    Attention : le premier niveau est 1 et non 0.

    params
    ------
    niveau (int) : Le niveau demandé
    interface (dict) : Le dictionnaire contenant tous les éléments de l'interface
    """
    interface["pile_niveaux"].setCurrentIndex(niveau)


def print_terminal(terminal : QTextEdit, * textes, couleur : QColor = QColor(255, 255, 255), sep : str = ' ', end : str = '\n', recursif : bool = False) -> None:
    """
    Imite la fonction print dans le terminal de l'interface.
    Le code d'échappement ANSI ne fonctionnant pas dans un QTextEdit, il est remplacé par le paramètre couleur.

    Params
    ------
    terminal (QTextEdit) : Le terminal de l'interface dans lequel s'affiche le texte
    *textes (Any) : Ce qui sera affiché
    couleur (Qcolor) = QColor(255, 255, 255) : La couleur dans laquelle est affiché le texte. La couleur par défaut est blanc.
    sep (str) = ' ' : La chaîne de caractère séparant chaque élément à afficher. Par défaut, il s'agit d'un espace.
    end (str) = '\n' : La chaîne de caractère finale. Par défaut, il s'agit d'un saut de ligne.
    recursif (bool) = False : Argument à ne spécifier qu'au sein de cette fonction.
                            Permet de mettre des guillemets autour des chaînes de caractères
                            uniquement si elles sont incluses dans un autre élément.
    """
    char_format = QTextCharFormat()
    char_format.setForeground(couleur)
    curseur = terminal.textCursor()
    curseur.movePosition(QTextCursor.End) # Force le curseur à retourner à la fin du terminal
    for element, i in zip(textes, range(len(textes))):
        el_type = type(element)
        if el_type == tuple :
            curseur.insertText('(', char_format)
            print_terminal(terminal, *element, sep = ', ', end = '', recursif = True, couleur = couleur)
            curseur.insertText(')', char_format)
        elif el_type == str :
            curseur.insertText(element, char_format)
        elif el_type in (int, float, complex, type) :
            s = str(element)
            curseur.insertText(s, char_format)
        elif el_type == list :
            curseur.insertText('[', char_format)
            print_terminal(terminal, *element, sep = ', ', end = '', recursif = True, couleur = couleur)
            curseur.insertText(']', char_format)
        elif el_type == set :
            if len(element) :
                curseur.insertText('{', char_format)
                print_terminal(terminal, *element, sep = ', ', end = '', recursif = True, couleur = couleur) 
                curseur.insertText('}', char_format)
            else :
                curseur.insertText('set()', char_format)
        elif el_type == bool :
            if element :
                curseur.insertText('True', char_format)
            else :
                curseur.insertText('False', char_format)
        elif el_type == dict :
            curseur.insertText('{', char_format)
            for cle, valeur, i in zip(element.keys(), element.values(), range(len(element))) :
                print_terminal(terminal, cle, end = ' : ', recursif = True, couleur = couleur)
                if i < len(element) - 1:
                    print_terminal(terminal, valeur, end = ', ', recursif = True, couleur = couleur)
                else :
                    print_terminal(terminal, valeur, end = '', recursif = True, couleur = couleur)
            curseur.insertText('}', char_format)
        if i < len(textes) - 1 :
            curseur.insertText(sep, char_format)
    curseur.insertText(end, char_format)


def acceder_element(disposition : QVBoxLayout, element : str) -> QWidget:
    """Renvoie l'élément demandé de la zone de dialogue.

    Params
    ------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    element (str) : L'élément demandé. Doit êter inclu dans cette liste :
                        - label
                        - spin_box
                        - bouton
                    Sinon le label est renvoyé par défaut.

    Return :
    QLabel|QSpinBox|QPushButton : L'élément demandé
    """
    if element == 'label' :
        return disposition.itemAt(0).widget().layout().itemAt(1).widget()
    correspondances = {'spin_box' : 1, 'bouton' : 2}
    return disposition.itemAt(correspondances.get(element, 1)).layout().itemAt(1).widget()

def changer_dialogue(disposition : QVBoxLayout, texte : str) -> None :
    """Actualise le dialogue avec le texte donné.
    
    Params
    -------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    texte (str) : Le texte à afficher
    """
    label = acceder_element(disposition, 'label')
    label.setText(texte)
    
def montrer_dialogue(disposition : QVBoxLayout) -> None :
    """Affiche certains éléments du dialogue : le texte et le bouton.

    Param
    ------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    """
    # Affiche le label
    acceder_element(disposition, 'label').setVisible(True)
    # Affiche le bouton
    acceder_element(disposition, 'bouton').setVisible(True)

def cacher_dialogue(disposition : QVBoxLayout) -> None :
    """Cache tous les éléments du dialogue.

    Param
    ------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    """
    # Cache le label
    acceder_element(disposition, 'label').setVisible(False)
    # Cache la spin_box
    acceder_element(disposition, 'spin_box').setVisible(False)
    # Cache le bouton
    acceder_element(disposition, 'bouton').setVisible(False)

def montrer_spin_box(disposition : QVBoxLayout, max : int) -> None:
    """Affiche la spin box et met à jour sa plage de valeur.

    Params
    -------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    min (int) : La valeur minimale de la plage de valeur voulue
    max (int) : La valeur maximale de la plage de valeur voulue
    """
    spin_box = acceder_element(disposition, 'spin_box')
    spin_box.setRange(1, max)
    spin_box.setVisible(True)

def cacher_spin_box(disposition : QVBoxLayout) -> None:
    """Cache la spin box.

    Param
    -------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    """
    spin_box = acceder_element(disposition, 'spin_box')
    spin_box.setVisible(False)

def changer_son(ancien : QMediaPlayer, nouveau : QMediaPlayer) -> None:
    """Arrête le son en train de jouer et lance le deuxième.

    Params
    -------
    ancien (QMediaPlayer) : Le son en train d'être joué
    nouveau (QMediaPlayer) : Le son qui est lancé
    """
    ancien.stop()
    nouveau.play()

def bouton_panneau(disposition : QVBoxLayout) -> None :
    """Adapte le texte du bouton du dialogue pour afficher 'OK' lorsque le dialogue
    concerne un panneau. (condition non gérée par cette fonction)

    Param
    -------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    """
    bouton = acceder_element(disposition, 'bouton')
    bouton.setText('OK')

def bouton_pnj(disposition : QVBoxLayout) -> None :
    """Adapte le texte du bouton du dialogue pour afficher 'Suite' lorsque le dialogue
    concerne un pnj. (condition non gérée par cette fonction)

    Param
    -------
    disposition (QVBoxLayout) : La disposition contenant le dialogue
    """
    bouton = acceder_element(disposition, 'bouton')
    bouton.setText('Suite')