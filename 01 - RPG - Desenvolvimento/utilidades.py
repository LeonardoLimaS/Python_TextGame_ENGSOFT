import os
import sys


# =========================================
# CAMINHO BASE DO PROJETO
# =========================================

def caminho_base():

    """
    Retorna o caminho base do projeto.

    Compatível com:
    - execução normal
    - PyInstaller
    """

    try:

        return sys._MEIPASS

    except Exception:

        return os.path.abspath(".")


# =========================================
# CAMINHO DE RECURSO
# =========================================

def caminho_recurso(caminho_relativo):

    """
    Retorna caminho absoluto
    para qualquer asset.
    """

    return os.path.join(
        caminho_base(),
        caminho_relativo
    )


# =========================================
# PASTA ASSETS
# =========================================

def pasta_assets():

    return caminho_recurso("assets")


# =========================================
# SONS
# =========================================

def caminho_som(nome_arquivo):

    return caminho_recurso(
        os.path.join(
            "assets",
            "sons",
            nome_arquivo
        )
    )


# =========================================
# IMAGENS
# =========================================

def caminho_imagem(nome_arquivo):

    return caminho_recurso(
        os.path.join(
            "assets",
            "imagens",
            nome_arquivo
        )
    )


# =========================================
# FONTES
# =========================================

def caminho_fonte(nome_arquivo):

    return caminho_recurso(
        os.path.join(
            "assets",
            "fontes",
            nome_arquivo
        )
    )