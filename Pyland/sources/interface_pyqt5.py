"""
gère l'interface du jeu
"""


# imports
# =======
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QApplication, QTextEdit, QHBoxLayout, QProgressBar, QStackedWidget, QSpinBox, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon, QFontMetrics, QPainter
from PyQt5.QtCore import Qt,  QSize, QRectF, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSoundEffect
from fonctions_liens import text_modifier, cacher_dialogue
from fonctions_globales import multi_split
from math import ceil
from addon_interface import *




# constantes
from constantes import *

app = QApplication([])

from chargement_police import FONT_CODEX, FONT_SOUS_TITRE_CODEX, FONT_TITRE_CODEX


# functions
# =========
def precedente(bouton : QPushButton, sec_bouton : QPushButton, pile : QStackedWidget) -> None:
    """
    Permet de passer à la page précédente de l'affichage des énoncés de niveaux.

    Params :
    bouton (QPushButton) : Le bouton qui est préssé (bouton gauche)
    secbouton (QPushButton) : Le bouton qui n'est pas préssé (bouton droit)
    """
    widget : QStackedWidget = pile.currentWidget()
    index = max(0, widget.currentIndex() - 1)
    widget.setCurrentIndex(index)
    if not index :
        bouton.setDisabled(True)
    if index < widget.count() :
        sec_bouton.setEnabled(True)

def suivante(bouton : QPushButton, sec_bouton : QPushButton, pile : QStackedWidget) -> None :
    """
    Permet de passer à la page suivante de l'affichage des énoncés de niveaux.

    Params :
    bouton (QPushButton) : Le bouton qui n'est pas préssé (bouton droit)
    secbouton (QPushButton) : Le bouton qui est préssé (bouton gauche)
    """
    widget : QStackedWidget = pile.currentWidget()
    nombre_widgets = widget.count() - 1
    index = min(nombre_widgets, widget.currentIndex() + 1)
    widget.setCurrentIndex(index)
    if index :
        sec_bouton.setEnabled(True)
    if index == nombre_widgets :
        bouton.setDisabled(True)

def creer_niveaux(largeur : int) -> tuple[QVBoxLayout, QStackedWidget]:
    """
    Crée les énoncés des niveaux, au dessus de la zone de code éditable à droite.
    Chaque page affiche 10 lignes.

    Returns
    -------
    QVBoxLayout : La disposition contenant toutes la partie des niveaux
    QStackedWidget : La pile contenant les niveaux
    """
    largeur -= 64
    conteneur = QHBoxLayout()
    conteneur.setContentsMargins(0, 2, 0, 2)
    pile_niveaux = QStackedWidget()
    pile_niveaux.setFont(POLICE)
    pile_niveaux.setFixedHeight(QFontMetrics(pile_niveaux.font()).lineSpacing() * N_LIGNES)
    # contenu de la boite et affichage par pages
    with open(FICHIER_NIVEAUX, encoding="utf-8") as fichier:
        texte = fichier.read()
        niveaux = texte.split('\n\n')
        for niveau in niveaux :
            pile_pages = QStackedWidget()
            lignes = multi_split(niveau, largeur // pile_niveaux.fontMetrics().width("a"))
            for n in range(ceil(len(lignes)/N_LIGNES)) :
                label = QLabel("".join(lignes[n*N_LIGNES : min((n + 1) * N_LIGNES, len(lignes))]))
                label.setTextInteractionFlags(label.textInteractionFlags() | Qt.TextSelectableByMouse)
                label.setAlignment(Qt.AlignTop)
                pile_pages.addWidget(label)
            pile_niveaux.addWidget(pile_pages)

    # taille des deux boutons qui suivent
    largeur = 30
    hauteur = 70

    # bouton pour revenir a la page précédente
    bouton_precedent = QPushButton("<")
    bouton_precedent.setFixedSize(largeur, hauteur)
    bouton_precedent.clicked.connect(lambda : precedente(bouton_precedent, bouton_suivant, pile_niveaux))

    # bouton pour aller a la page suivante
    bouton_suivant = QPushButton(">")
    bouton_suivant.setFixedSize(largeur, hauteur)
    bouton_suivant.clicked.connect(lambda : suivante(bouton_suivant, bouton_precedent, pile_niveaux))
    conteneur.addWidget(bouton_precedent)
    conteneur.addWidget(pile_niveaux)
    conteneur.addWidget(bouton_suivant)

    return conteneur, pile_niveaux


def creer_zone_texte(interface : dict) -> QTextEdit :
    """
    Créé la zone de texte éditable pour entrer le code.

    Return
    -------
    QTextEdit : La zone de texte
    """
    zone_texte = QTextEdit()
    zone_texte.setFixedWidth(int(interface["pile"].width() * 2 /5))
    zone_texte.setTabStopWidth(25)
    zone_texte.super_keyPressEvent = zone_texte.keyPressEvent # La méthode keyPressEvent est enregistré dans la méthode super_keyPressEvent
    zone_texte.keyPressEvent = lambda event : text_modifier(zone_texte, event, interface)
    
    return zone_texte


def creer_bouton_lancer(barre_cote : QVBoxLayout) -> QPushButton :
    """
    Créé le bouton permettant de lancer le code écrit en zone éditable.

    Param
    -----
    barre_cote (QVBoxLayout) : La disposition appliquée à la barre droite de l'interface

    Return
    -------
    QPushButton : Le bouton qui lance le code
    """
    bouton = QPushButton("Lancer")
    style_sheet = "background-color : rgb(0, 255, 0); border-radius : 15%;"
    bouton.setStyleSheet(style_sheet)
    bouton.setFont(POLICE)
    bouton.pressed.connect(lambda : bouton.setStyleSheet(style_sheet + STYLE_BOUTON_PRESSE))
    bouton.released.connect(lambda : bouton.setStyleSheet(style_sheet))
    bouton.enterEvent = lambda event : bouton.setFont(GRANDE_POLICE)
    bouton.leaveEvent = lambda event : bouton.setFont(POLICE)
    bouton.setFixedSize(QSize(bouton.fontMetrics().width("Lancer") + 50, bouton.fontMetrics().height() + 20))
    conteneur = QHBoxLayout()
    conteneur.setContentsMargins(0, 5, 0, 5)
    conteneur.setAlignment(Qt.AlignCenter)
    conteneur.addWidget(bouton)
    barre_cote.addLayout(conteneur)

    return bouton

def creer_barre_cote(interface : dict) -> tuple[QWidget, QTextEdit, QStackedWidget, QPushButton] :
    """
    Créé la partie droite de l'interface contenant
    - les textes de niveau (au dessus de la zone éditable blanche)          [créés dans creer_niveaux()]
    - la zone de lancement de code (zone éditable blanche)                  [créée dans creer_zone_texte()]
        - dont le bouton de lancement                                       [créé dans creer_bouton_lancer()]
    - les boutons techniques de la barre du haut (coin en haut à droite)    [créés ici]

    Param
    -------
    interface (dict) : Tous les éléments de l'interface

    Returns
    -------
    QWidget : La barre sur le côté
    QTextEdit : La zone d'édition
    QStackedWidget : La pile contenant les niveaux
    QPushButton : Le bouton permettant de lancer l'interface
    """
    # partie droite de l'interface
    widget = QWidget()
    # calcul et application de la taille de la barre (2/5 de la largeur de l'écran et toute la hauteur)
    widget.setFixedSize(QSize(int(interface["pile"].width()*2/5) - 20, interface["pile"].height() - 10))
    barre = QVBoxLayout()
    barre.setAlignment(Qt.AlignHCenter)
    barre.setContentsMargins(5, 5, 5, 5)
    widget.setLayout(barre)
    # barre contenant les boutons techniques
    barre_outils = QHBoxLayout()
    barre_outils.setAlignment(Qt.AlignRight)

    # bouton accueil
    bouton_accueil = QPushButton('Accueil')
    style_sheet_acc = "background-color : rgb(255, 235, 138); border-radius : 15%;"
    bouton_accueil.setStyleSheet(style_sheet_acc)
    bouton_accueil.setFont(POLICE)
    bouton_accueil.pressed.connect(lambda : bouton_accueil.setStyleSheet(style_sheet_acc + STYLE_BOUTON_PRESSE))
    bouton_accueil.released.connect(lambda : bouton_accueil.setStyleSheet(style_sheet_acc))
    bouton_accueil.enterEvent = lambda event : bouton_accueil.setFont(GRANDE_POLICE)
    bouton_accueil.leaveEvent = lambda event : bouton_accueil.setFont(POLICE)
    bouton_accueil.clicked.connect(lambda: interface["pile"].setCurrentIndex(0))
    largeur_acc = bouton_accueil.fontMetrics().width('Accuiel') * 2
    hauteur_acc = bouton_accueil.fontMetrics().lineSpacing() + 3
    bouton_accueil.setFixedSize(QSize(largeur_acc, hauteur_acc))
    barre_outils.addWidget(bouton_accueil)
    barre.addLayout(barre_outils)
    
    # bouton quitter
    bouton_quitter = QPushButton('Quitter')
    style_sheet_quit = "background-color : rgb(255, 100, 100); border-radius : 15%;"
    bouton_quitter.setStyleSheet(style_sheet_quit)
    bouton_quitter.setFont(POLICE)
    bouton_quitter.pressed.connect(lambda : bouton_quitter.setStyleSheet(style_sheet_quit + STYLE_BOUTON_PRESSE))
    bouton_quitter.released.connect(lambda : bouton_quitter.setStyleSheet(style_sheet_quit))
    bouton_quitter.enterEvent = lambda event : bouton_quitter.setFont(GRANDE_POLICE)
    bouton_quitter.leaveEvent = lambda event : bouton_quitter.setFont(POLICE)
    hauteur_quit = bouton_quitter.fontMetrics().lineSpacing() + 3
    largeur_quit = bouton_quitter.fontMetrics().width('Quitter') * 2
    bouton_quitter.setFixedSize(QSize(largeur_quit, hauteur_quit))
    barre_outils.addWidget(bouton_quitter)
    bouton_quitter.clicked.connect(app.quit)

    # textes de niveau
    conteneur, niveaux = creer_niveaux(widget.width())
    barre.addLayout(conteneur)

    # zone de lancement de code
    zone_texte = creer_zone_texte(interface)
    barre.addWidget(zone_texte)


    # bouton de lancement
    bouton_lancer = creer_bouton_lancer(barre)

    return widget, zone_texte, niveaux, bouton_lancer

def creer_barre_inf(pile_principale : QStackedWidget) -> tuple[QHBoxLayout, QTextEdit]:
    """
    Créé la partie basse à gauche de l'interface comportant :
    - le terminal (retours code du joueur)  [créé ici]
    - le bouton du codex (livre de connaissances du joueur)
    """

    # partie basse à gauche de l'interface
    disposition = QHBoxLayout()

    #terminal
    terminal = QTextEdit()
    terminal.setStyleSheet("background-color : black;")
    terminal.setFont(POLICE)
    terminal.setTextColor(Qt.white)
    terminal.setTabStopWidth(25) # Défini la taille d'une tabulation (trop grand par défaut)
    terminal.setReadOnly(True) # Désactivation de la possibilité d'écrire dans le terminal
    terminal.setToolTip('Terminal')
    disposition.addWidget(terminal)

    #crée le bouton permettant d'accéder au codex
    bouton_codex = QPushButton()
    bouton_codex.setFixedSize(200, 200)
    bouton_codex.setIconSize(QSize(200,200))
    icon = QIcon(QPixmap("images/livre_ferme.png"))
    bouton_codex.setIcon(icon)
    bouton_codex.clicked.connect(lambda : pile_principale.setCurrentIndex(2)) # pour ouvrir le codex
    disposition.addWidget(bouton_codex)

    return disposition, terminal

def placer_centre(disposition : QVBoxLayout, element : QWidget, margin_top : int = 5) :
    """
    Permet de centrer

    Params
    ------

    """
    conteneur = QHBoxLayout()
    conteneur.setContentsMargins(0, margin_top, 0, 5)
    conteneur.addStretch()
    conteneur.addWidget(element)
    conteneur.addStretch()
    disposition.addLayout(conteneur)

def creer_dialogue(disposition : QVBoxLayout, jeu : QWidget) :
    """
    Créer toute la partie de l'interface concernant les dialogues.
    Les dialogues s'afficheront sur la zone de jeu.

    Params :
    dispositon (QVBoxLayout) : La disposition qui contiendra tous les éléments du dialogue
    jeu (QWidget) : La zone de jeu
    """
    widget = QWidget()
    widget.setStyleSheet("border : none")
    label = QLabel()
    label.setFixedWidth(int(jeu.width()* 3/5))
    policy = QSizePolicy()
    policy.setHorizontalPolicy(QSizePolicy.Fixed)
    policy.setVerticalPolicy(QSizePolicy.Maximum)
    label.setSizePolicy(policy)
    label.setWordWrap(True)
    label.setStyleSheet(STYLE_DIALOGUE)
    label.setFont(POLICE)
    label.setAlignment(Qt.AlignJustify)
    layout = QHBoxLayout()
    layout.addStretch()
    layout.addWidget(label)
    layout.addStretch()
    widget.setLayout(layout)
    spin_box = QSpinBox()
    spin_box.setFixedSize(spin_box.fontMetrics().width("Votre réponse : 9") + 50, spin_box.sizeHint().height())
    spin_box.setPrefix("Votre réponse : ")
    spin_box.setRange(1, 2)
    bouton = QPushButton("Suite")
    bouton.setStyleSheet('background-color : rgb(0, 255, 0); border-radius : 15%; border : 0px;')
    bouton.setFont(POLICE)
    bouton.setFixedSize(spin_box.width() + 50, bouton.sizeHint().height())
    disposition.addWidget(widget)
    placer_centre(disposition, spin_box)
    placer_centre(disposition, bouton)
    widget.setFixedHeight(jeu.height() - bouton.height() - spin_box.height())

def recuperer_vie(barre_vie : QProgressBar, timer : QTimer) :
    vie = barre_vie.value() + 1
    barre_vie.setValue(vie)
    if vie == barre_vie.maximum() :
        timer.stop()

def creer_barre_jeu(pile : QStackedWidget) -> tuple[QVBoxLayout, QWidget, QTextEdit, QVBoxLayout]:
    """
    Gère l'agencement de la partie gauche de l'interface :
    - écran de jeu (carte)                                               [créé ici]
    - cadre de dialogue (par dessus la carte)                            [créé ici]
    - barre de vie (en bleu sous la carte)                               [créée ici]
    - terminal et codex (écran noir et image livre sous la barre de vie) [créés dans creer_barre_inf()]
    Parameters
    ----------
    pile : la pile pricipale du jeu

    Returns
    -------
    le jeu en gros
    """
    # partie gauche de l'interface
    widget = QWidget()
    widget.setFixedSize(QSize(int(pile.width()*3/5), pile.height()-10))
    barre = QVBoxLayout()
    barre.setContentsMargins(5, 5, 5, 5)
    widget.setLayout(barre)

    # barre de vie
    vie = QHBoxLayout()
    label_vie = QLabel("Vie : ")
    vie.addWidget(label_vie)
    barre_vie = QProgressBar()
    barre_vie.setMaximum(VIE_MAX)
    barre_vie.setValue(VIE_MAX)
    vie.addWidget(barre_vie)
    barre.addLayout(vie)
    timer = QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(lambda : recuperer_vie(barre_vie, timer))

    # écran de jeu dont affichage dialogue
    jeu = QWidget()
    jeu.setFixedSize(QSize(int(pile.width()*3/5), int(pile.width()*3/10)))
    jeu.setStyleSheet("border : 3px solid white;")

    #   # dialogue
    cadre_dialogue = QVBoxLayout()
    creer_dialogue(cadre_dialogue, jeu)
    cacher_dialogue(cadre_dialogue)
    jeu.setLayout(cadre_dialogue)

    barre.addWidget(jeu)

    # terminal et codex
    codex_terminal, terminal = creer_barre_inf(pile) # création du terminal avec cette fonction
    barre.addLayout(codex_terminal)

    return widget, jeu, terminal, cadre_dialogue, barre_vie, timer


def creer_fenetre(pile : QStackedWidget) -> QWidget :
    """
    fenetre principale du jeu, qui contient l'interface.
    Parameters
    ----------
    pile : la pile principale du jeu

    Returns
    -------
    la fenetre du jeu
    """
    fenetre = QWidget()
    fenetre.setFixedSize(pile.size())
    fenetre.setFocusPolicy(Qt.StrongFocus)
    fenetre.setFont(POLICE)
    pile.addWidget(fenetre)
    return fenetre

def creer_layout(interface : dict) -> QHBoxLayout :
    """
    Renvoie le layout global de la fenêtre principale

    Parameters
    ------
    interface (dict) : les éléments de l'interface
    """
    layout = QHBoxLayout()
    layout.addWidget(interface["barre_jeu"])
    layout.addWidget(interface["barre_côté"])
    layout.setContentsMargins(0, 0, 0, 0)
    return layout

def creer_label_titre(texte : str, hauteur_restante : int) :
    """
    Creer un label pour les titres dans le codex
    Parameters
    ----------
    texte : le texte qui ferat le titre
    hauteur_restante : la hauteur restante dans le codex

    Returns
    -------

    """
    if texte.startswith('--t--') :
        label = QLabel()
        label.setFont(FONT_TITRE_CODEX)
        hauteur_titre = label.fontMetrics().lineSpacing()
        if hauteur_restante > hauteur_titre + 10 :
            texte = texte.removeprefix('--t--')
            titre, texte = texte.split('\n', 1)
            label.setText(titre)
            label.setFixedHeight(hauteur_titre)
            label.setContentsMargins(0, 5, 0, 5)
            label.setAlignment(Qt.AlignCenter)
            return label, hauteur_restante - hauteur_titre - 10, texte
    return None, hauteur_restante, texte


def creer_label_sous_titre(texte : str, hauteur_restante : int) :
    """
    Creer un label pour les sous-titres dans le codex
    Parameters
    ----------
    texte : le texte qui ferat le sous-titre
    hauteur_restante : la hauteur restante dans le codex

    Returns
    -------

    """
    if texte.startswith('--st--') :
        label = QLabel()
        label.setFont(FONT_SOUS_TITRE_CODEX)
        hauteur_sous_titre = label.fontMetrics().lineSpacing()
        if hauteur_restante > hauteur_sous_titre + 6 :
            texte = texte.removeprefix('--st--')
            sous_titre, texte = texte.split('\n', 1)
            label.setText(sous_titre)
            label.setFixedHeight(hauteur_sous_titre)
            label.setContentsMargins(0, 3, 0, 3)
            label.setAlignment(Qt.AlignCenter)
            return label, hauteur_restante - hauteur_sous_titre - 6, texte
    return None, hauteur_restante, texte


def reste_texte(texte : str, texte_utilise : str) :
    """
    (Honnetemnt je fais les docs après et si qql avait pas coder ça en i , j , ect j'aurais essayer de comprendre)
    donne le reste du texte a afficher
    Parameters
    ----------
    texte : le texte total
    texte_utilise : le texte deja utilisé

    Returns
    -------
    le texte qu'il reste
    """
    i = 0
    j = 0
    while i < len(texte) and j < len(texte_utilise) :
        if texte[i] == texte_utilise[j] :
            i += 1
            j += 1
        elif texte_utilise[j] == '\n' :
            j += 1
        elif texte[i] == ' ' :
            i += 1
        else :
            return texte[i:]
    return texte[i:]


def creer_label_liste(texte : str, hauteur_restante : int, largeur : int) :
    """
    Creer les labels pour les listes
    Parameters
    ----------
    texte : le texte a mettre en liste
    hauteur_restante : la hauteur restantre dans le codex
    largeur : la largeur du codex

    Returns
    -------

    """
    block = ''
    lignes = texte.split('\n')
    n = 0
    label = QLabel()
    label.setFont(FONT_CODEX)
    label.setContentsMargins(20, 0, 0, 0)
    label.setAlignment(Qt.AlignJustify)
    hauteur_ligne = label.fontMetrics().lineSpacing()
    taille_caractere = label.fontMetrics().width("azertyuiopqsdfghjklmwxcvbn") / 26
    sous_lignes = multi_split(lignes[0], largeur//taille_caractere)
    nb_lignes = 0
    while lignes[n].startswith('· ') and hauteur_ligne * (nb_lignes + len(sous_lignes)) <= hauteur_restante :
        nb_lignes += len(sous_lignes)
        sous_lignes = multi_split(lignes[n], largeur // taille_caractere)
        if hauteur_ligne * nb_lignes <= hauteur_restante :
            block += ''.join(sous_lignes)
        n += 1
    if block :
        label.setText(block)
        label.setFixedSize(QSize(largeur, hauteur_ligne * nb_lignes))
        return label, hauteur_restante -  hauteur_ligne * (nb_lignes), reste_texte(texte, block)
    else :
        return None, hauteur_restante, texte
    

def creer_block_texte(texte : str, hauteur_restante : int, largeur : int) -> tuple[QLabel, int, list[str]]:
    """
    Creer les blocs de textes dans le codex
    Parameters
    ----------
    texte : le texte a mettre
    hauteur_restante : la hauteur restantre dans le codex
    largeur : la largeur du codex

    Returns
    -------

    """
    block = ''
    n = 0
    label = QLabel()
    label.setFont(FONT_CODEX)
    taille_caractere = ceil(label.fontMetrics().width("azertyuiopqsdfghjklmwxcvbn") / 26)
    lignes = multi_split(texte, largeur//taille_caractere)
    label.setContentsMargins(0, 0, 0, 0)
    label.setAlignment(Qt.AlignJustify)
    hauteur_ligne = label.fontMetrics().lineSpacing()
    while not lignes[n%len(lignes)].startswith(('--t--', '--st--', '· ')) and hauteur_ligne * (n+2) <= hauteur_restante and n < len(lignes):
        block += lignes[n]
        n += 1
    if block :
        label.setText(block)
        label.setFixedSize(QSize(largeur, hauteur_ligne * (n+1)))
        return label, hauteur_restante - hauteur_ligne * (n+1), reste_texte(texte, block)
    else :
        return None, hauteur_restante, texte

def creer_page(texte : str, hauteur : int, largeur : int) -> tuple[QWidget, list[str]] :
    """
     Creer les pages du codex
    Parameters
    ----------
    texte : le texte des pages
    hauteur
    largeur

    Returns
    -------

    """
    page = QWidget()
    layout = QVBoxLayout()
    page.setLayout(layout)
    fonctions = (
        lambda texte, hauteur_res: creer_label_titre(texte, hauteur_res),
        lambda texte, hauteur_res: creer_label_sous_titre(texte, hauteur_res),
        lambda texte, hauteur_res: creer_label_liste(texte, hauteur_res , largeur - 20),
        lambda texte, hauteur_res: creer_block_texte(texte, hauteur_res, largeur)
    )
    num = 0
    suite = 0
    while hauteur and texte and suite < 4 :
        label, hauteur, texte = fonctions[num](texte, hauteur)
        if label :
            suite = 0
            layout.addWidget(label)
        else :
            suite += 1
        num += 1
        if num == 4 :
            num = 0
    layout.addStretch()
    return page, texte

def creer_pages_codex(gauche : QStackedWidget, droite : QStackedWidget, pile : QStackedWidget, bouton : QPushButton) -> None:
    """
    créé l'affichage du codex ouvert et son contenu
    Parameters
    ----------
    gauche : la bande gauche de l'écran en QStackWidget
    droite : la bande droite de l'écran en QStackWidget
    pile : la pile principale du jeu
    bouton : les bouton à mettre

    Returns
    -------

    """

    # affichage des lignes
    gauche.setFont(FONT_CODEX)
    droite.setFont(FONT_CODEX)
    largeur = (pile.width() - 210)//2
    gauche.setFixedWidth(largeur)
    droite.setFixedWidth(largeur)
    gauche.setContentsMargins(50, 25, 50, 10)
    droite.setContentsMargins(50, 25, 50, 10)
    # 55 -> l'addition de toutes les marges concernées
    hauteur = pile.height() - 55 - bouton.height()

    # contenu du codex
    with open(FICHIER_CODEX, 'r', encoding='utf-8') as fichier :
        texte = fichier.read()
    parties = texte.split('--p--')

    n = 0
    for partie in parties :
        while partie :
            page, partie = creer_page(partie, hauteur, largeur)
            if not n % 2 :
                gauche.addWidget(page)
            else :
                droite.addWidget(page)
            n += 1

    if gauche.count() != droite.count() :
        droite.addWidget(QLabel())


def aller_page(page_gauche : QStackedWidget, page_droite : QStackedWidget, changement : int) -> None :
    """
    permet de passer d'une page du codex a l'autre
    Parameters
    ----------
    page_gauche : la page de gauche du codex
    page_droite : la page de droite du codex
    changement : la nouvelle page à afficher

    Returns
    -------

    """
    page_gauche.setCurrentIndex(page_gauche.currentIndex() + changement)
    page_droite.setCurrentIndex(page_droite.currentIndex() + changement)


def fond_codex(codex : QWidget, pile_principale : QStackedWidget) -> None :
    """
    affiche l'arrière-plan lors de l'ouvrerture du codex
    Parameters
    ----------
    codex : le codex entier
    pile_principale : la pile principale du jeu

    Returns
    -------

    """
    painter = QPainter(codex)
    fond = QPixmap("images/fond_codex.png")
    p_largeur = pile_principale.width()
    p_hauteur = pile_principale.height()
    f_largeur = fond.width()
    f_hauteur = fond.height()
    ratio =  f_hauteur / f_largeur
    t_hauteur = p_largeur * ratio
    target = QRectF(0, (p_hauteur-t_hauteur)/2, p_largeur, t_hauteur)
    source = QRectF(0, 0, f_largeur, f_hauteur)
    painter.drawPixmap(target, fond, source)


def creer_codex(pile_principale : QStackedWidget) -> QWidget :
    """
    Crée la page du codex
    
    Params
    ------
    pile_principale (QStackedWidget) : La pile qui contiendra le codex
    """
    # codex
    codex = QWidget()
    palette = QPalette()
    palette.setColor(QPalette.Active, QPalette.WindowText, Qt.black)
    codex.setPalette(palette)
    codex.setFixedSize(pile_principale.size())

    # arrrière-plan
    codex.paintEvent = lambda event : fond_codex(codex, pile_principale)
    pile_principale.addWidget(codex)

    # boite portant tout le contenu
    layout = QVBoxLayout()
    layout.setContentsMargins(5, 10, 5, 10)
    codex.setLayout(layout)

    # bouton pour fermer le codex
    bouton_retour = QPushButton('<- Retour')
    styleSheet = "background-color : rgb(0, 158, 255); border-radius : 15%;"
    bouton_retour.setStyleSheet(styleSheet)
    bouton_retour.setFont(POLICE)
    bouton_retour.pressed.connect(lambda : bouton_retour.setStyleSheet(styleSheet + STYLE_BOUTON_PRESSE))
    bouton_retour.released.connect(lambda : bouton_retour.setStyleSheet(styleSheet))
    bouton_retour.enterEvent = lambda event : bouton_retour.setFont(GRANDE_POLICE)
    bouton_retour.leaveEvent = lambda event : bouton_retour.setFont(POLICE)
    mesures = bouton_retour.fontMetrics()
    taille = QSize(mesures.width('<-  Retour') + 60, mesures.lineSpacing() + 3)
    bouton_retour.setFixedSize(taille)
    bouton_retour.clicked.connect(lambda : pile_principale.setCurrentIndex(1))
    layout.addWidget(bouton_retour)

    # boite contenant les boutons de changement de page et les pages
    sous_layout = QHBoxLayout()
    layout.addLayout(sous_layout)

    # crée les deux pages du codex, à droite et a gauche
    page_gauche = QStackedWidget()
    page_droite = QStackedWidget()
    creer_pages_codex(page_gauche, page_droite, pile_principale, bouton_retour)

    # bouton pour aller à la page précédente
    bouton_precedent = QPushButton("<")
    bouton_precedent.setFixedWidth(100)
    bouton_precedent.clicked.connect(lambda : aller_page(page_gauche, page_droite, -1))

    # bouton pour aller à la page suivante
    bouton_suivant =  QPushButton(">")
    bouton_suivant.setFixedWidth(100)
    bouton_suivant.clicked.connect(lambda : aller_page(page_gauche, page_droite, +1))

    # ajout des différents éléments dans à la page
    sous_layout.addWidget(bouton_precedent)
    sous_layout.addWidget(page_gauche)
    sous_layout.addWidget(page_droite)
    sous_layout.addWidget(bouton_suivant)


def creer_pile(interface : dict) -> QStackedWidget :
    """
    défini la couleur d'arrière-plan et
    créé une pile d'affichage différenciant l'affichage de l'interface de jeu et l'affichage du codex ouvert.
    Parameters
    ----------
    interface : l'interface du jeu

    Returns
    -------
    pile : la pile du jeu entiere
    """
    pile = QStackedWidget()
    page_accueil = creer_accueil(interface)
    pile.addWidget(page_accueil)

    # couleurs sur la pile
    palette = QPalette()
    #   # couleur d'arrière plan
    palette.setColor(QPalette.Active, QPalette.Window, QColor(40, 41, 45))
    #   # couleur de la boite de texte éditable
    palette.setColor(QPalette.Active, QPalette.WindowText, Qt.white)

    pile.setPalette(palette)
    pile.keyPressEvent = lambda event : pile.setCurrentIndex(1)
    pile.showFullScreen()

    # Lancement du son
    interface["son_principal"].play()
    page_accueil.setFixedSize(pile.size())

    return pile

def creer_accueil(interface) -> tuple[QLabel, QPushButton] :
    """
    Crée la page d'accueil

    Return
    -------
    QLabel : La page d'accueil
    QPushButton : Le bouton commencer
    """
    image = QPixmap('images/pyland_accueil.png')  #../full_screen.png  #pyland_accueil.png # pour tester sous linux
    label = QLabel()
    disposition = QVBoxLayout()
    disposition.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

    bouton_commencer = QPushButton(texte_verify_0())
    style_sheet_1 = 'background-color : rgb(0, 255, 0); border-radius : 15%;'
    bouton_commencer.setStyleSheet(style_sheet_1)
    bouton_commencer.pressed.connect(lambda: bouton_commencer.setStyleSheet(STYLE_BOUTON_PRESSE + style_sheet_1))
    bouton_commencer.released.connect(lambda: bouton_commencer.setStyleSheet(style_sheet_1))
    bouton_commencer.setFont(POLICE_COMMENCER)
    bouton_commencer.setFixedSize(bouton_commencer.sizeHint().width() + 300, bouton_commencer.sizeHint().height() + 30)
    bouton_commencer.clicked.connect(lambda : interface["pile"].setCurrentIndex(1))

    bouton_reset = QPushButton("Reset\n(nécessite un redémarrage du jeu)\n! Attention cette action est irreversible !")
    style_sheet_2 = 'background-color : rgb(255, 0, 0); border-radius : 15%;'
    bouton_reset.setStyleSheet(style_sheet_2)
    bouton_reset.pressed.connect(lambda: bouton_reset.setStyleSheet(STYLE_BOUTON_PRESSE + style_sheet_2))
    bouton_reset.released.connect(lambda: bouton_reset.setStyleSheet(style_sheet_2))
    bouton_reset.setFont(POLICE_RESET)
    bouton_reset.setFixedSize(bouton_reset.sizeHint().width() + 100, bouton_reset.sizeHint().height() + 30)
    bouton_reset.clicked.connect(reset)

    bouton_exit = QPushButton("Quitter")
    style_sheet_3 = 'background-color : rgb(255, 255, 255); border-radius : 15%;'
    bouton_exit.setStyleSheet(style_sheet_3)
    bouton_exit.pressed.connect(lambda: bouton_exit.setStyleSheet(STYLE_BOUTON_PRESSE + style_sheet_3))
    bouton_exit.released.connect(lambda: bouton_exit.setStyleSheet(style_sheet_3))
    bouton_exit.setFont(POLICE_QUITTER)
    bouton_exit.setFixedSize(bouton_exit.sizeHint().width() + 50, bouton_exit.sizeHint().height() + 3)
    bouton_exit.clicked.connect(app.quit)

    disposition.addStretch()
    placer_centre(disposition, bouton_commencer, 0)
    placer_centre(disposition, bouton_reset, 50) # valeur de margin-top 
    placer_centre(disposition, bouton_exit, 25) # valeur de margin-top 
    label.setLayout(disposition)
    label.setAlignment(Qt.AlignCenter)
    label.setPixmap(image)

    return label

def repeter(player : QMediaPlayer, status : QMediaPlayer.MediaStatus) :
    """
    Repete la musique de fond
    Parameters
    ----------
    player : la musique de fond
    status : le statur de la musique

    Returns
    -------

    """
    if status == QMediaPlayer.EndOfMedia :
        player.setPosition(0)
        player.play()

def son(fichier : str, boucler : bool = True) -> QMediaPlayer:
    """
    s'occupe de jouer la musique de fond
    Parameters
    ----------
    fichier : les fichier avec la musique de fond
    boucler : si la musique doit se repeter ou non

    Returns
    -------

    """
    player = QMediaPlayer()
    player.setMedia(QMediaContent(QUrl.fromLocalFile(fichier)))
    if boucler :
        player.mediaStatusChanged.connect(lambda status : repeter(player, status))
    player.setVolume(30)
    return player

def creer_sons() -> tuple[QMediaPlayer]:
    """Crée les 2 sons : celui 'principal', joué la plupart du temps, et celui
    spécifique aux battailles.

    Returns
    --------
    QMediaPlayer : Le son principal
    QMediaPlayer : Le son des battailles
    """
    player = son(FICHIER_SON_PRINCIPAL)
    player_battle = son(FICHIER_SON_BATTLE)
    player_boss_final = son(FICHIER_SON_BOSS_FINAL)
    player_death = son(FICHIER_SON_DEATH, False)

    effet_sonore = QSoundEffect()
    effet_sonore.setSource(QUrl.fromLocalFile(FICHIER_SON_INACCESSIBLE))

    return player, player_battle, player_death, player_boss_final, effet_sonore

def creer_interface() -> dict:
    """
    Crée et renvoie le dictionnaire contenant toute l'interface
    Returns
    -------
    le dictionnaire en question
    """
    interface = {}
    interface["son_principal"], interface["son_battle"], interface["son_death"], interface["son_boss_final"], interface["son_inaccessible"] = creer_sons()
    interface["pile"] = creer_pile(interface)
    interface["fenêtre"] = creer_fenetre(interface["pile"])
    interface["barre_jeu"], interface["jeu"], interface["terminal"], interface["dialogue"], interface["barre_vie"], interface["timer_vie"] = creer_barre_jeu(interface["pile"])
    interface["barre_côté"], interface["zone_texte"], interface["pile_niveaux"], interface["bouton_lancer"] = creer_barre_cote(interface)
    interface["layout"] = creer_layout(interface)
    interface["fenêtre"].setLayout(interface["layout"])
    creer_codex(interface["pile"])

    return interface