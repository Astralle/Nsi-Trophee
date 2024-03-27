"""Ce fichier s'occupe d'executer le code que le joueur a écit"""
import os


def save_file():
    """
    Execute ou verifie que le fichier save.py est valide
    Returns
    -------

    """
    file_path = 'save.py'
    try:
        os.system(f'python {file_path}')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
