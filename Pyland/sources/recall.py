"""
récupère le fichier sauvegarde pour réacitalier le jeu

sauvegarde de base : 20/4/3/0/0/False/True/False/False/True/False/False/True/False/True/False/True/False/
"""

def recall():
    """
    lit la sauvegarde du fichier de sauvegarde
    Returns
    -------
    toutes les variables a réimplanter
    """
    f = open("all_texts/save.txt", "r")
    save_data = f.read()
    if save_data == "":
        save_data = "20/4/3/0/0/False/True/False/False/True/False/False/True/False/True/False/True/False/"
    list_data = []
    temp = ""

    for i in save_data:
        if i != "/":
            temp += i
        elif i == "/":
            temp = temp_to_actual(temp)
            list_data.append(temp)
            temp = ""

    var_to_read = var_in_dico(list_data)

    return var_to_read


def temp_to_actual(temp):
    """
    Renvoie les varaibles sous les bonnes formes , autre que str
    Parameters
    ----------
    temp : les variables en temps que str

    Returns
    -----
    les varaibles sous les bonnes formes--
    """
    if temp == "True":
        temp = True
    elif temp == "False":
        temp = False
    else:
        temp = int(temp)
    return temp


def var_in_dico(list_data):
    """
    Renvoie les varaibles dans un dico
    Parameters
    ----------
    list_data : toues les données sous le bon facteur

    Returns
    -------
    le dico
    """
    var_to_read = {
        "player_hp": list_data[0],
        "player_pos_0": list_data[1],
        "player_pos_1": list_data[2],
        "background_position_0": list_data[3],
        "background_position_1": list_data[4],
        "start_game": list_data[5],
        "ambuscade_gobelin": list_data[6],
        "farore_libre": list_data[7],
        "araigne_revele": list_data[8],
        "araigne_vivante": list_data[9],
        "scorpion_calme": list_data[10],
        "undead_revele": list_data[11],
        "undead_vivant": list_data[12],
        "mage_infiltre": list_data[13],
        "parz_karl_vivant": list_data[14],
        "mage_teleporte": list_data[15],
        "aldirien_vivant": list_data[16],
        'saal_lio_arrive': list_data[17],
    }
    return var_to_read
