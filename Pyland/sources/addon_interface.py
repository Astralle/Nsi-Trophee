"""
lance la bonne sauvegarde ou réinitialise la sauvegarde
"""


def reset():
    """
    Cette fonction écrit une sauvegarde vide dans le fichier save.txt
    Returns rien
    -------

    """
    save = open("all_texts/save.txt", "w")
    save.write("20/4/3/0/0/False/True/False/False/True/False/False/True/False/True/False/True/False/")
    save.close()


def texte_verify_0():
    """
    Cette fonction regarde si le bouton pour aller au jeu doit afficher Commencer ou Continuer
    Returns une string que le bouton affiche
    -------

    """
    save = open("all_texts/save.txt")
    texte = save.read()
    save.close()
    if texte == "20/4/3/0/0/False/True/False/False/True/False/False/True/False/True/False/True/False/":
        return "Commencer"
    else:
        return "Continuer"
