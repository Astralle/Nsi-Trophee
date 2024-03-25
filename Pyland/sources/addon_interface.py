"""
lance la bonne sauvegarde ou réinitialise la sauvegarde
"""
VAR = 0


def reset():
    save = open("all_texts/save.txt", "w")
    save.write("20/4/3/0/0/False/True/False/False/True/False/False/True/False/True/False/True/False/")
    save.close()


def texte_verify_0():
    save = open("all_texts/save.txt")
    texte = save.read()
    save.close()
    if texte == "20/4/3/0/0/False/True/False/False/True/False/False/True/False/True/False/True/False/":
        return "Commencer"
    else:
        return "Continuer"
