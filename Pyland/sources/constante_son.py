"""
Charge les sons.
"""

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QSoundEffect
from constantes import FICHIER_SON_INACCESSIBLE


def creer_son(chemin : str) -> QSoundEffect:
    son = QSoundEffect()
    son.setSource(QUrl.fromLocalFile(chemin))
    return son


SON_INACCESSIBLE = creer_son(FICHIER_SON_INACCESSIBLE)