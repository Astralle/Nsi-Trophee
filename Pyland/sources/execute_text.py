"""
fonction permettant d'exécuter le code entré par le joueur
"""
import io, contextlib

def execute_text(text_string: str) -> tuple[bool, str | Exception]:
    """Fonction qui exécute un code python sous forme de string et qui renvoie
    soit le résultat (False, output) ou l'erreur causé par la fonction (True, error)

    Args:
        text_string (str): Le code python sous forme de string (avec les \\n)

    Returns:
        tuple[bool, str | Exception]: (False, Exception) si le code cause une erreur
                                      (True, str) si le code renvoie correctement un résultat
    """
    try:
        # On renvoie stdout dans un StringIO buffer
        stdout_buffer = io.StringIO()
        with contextlib.redirect_stdout(stdout_buffer):
            exec(text_string, {})
        output = stdout_buffer.getvalue()
    except Exception as e:
        return (False, e)
    else:
        return (True, output.strip())