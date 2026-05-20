import os
import sys


def caminho_recurso(caminho_relativo):

    try:
        base_path = sys._MEIPASS

    except Exception:

        base_path = os.path.abspath(".")

    return os.path.join(
        base_path,
        caminho_relativo
    )