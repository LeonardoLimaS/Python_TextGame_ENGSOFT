Para funcionamento do projeto

1 - Instalar o Pygame versão comunity -> pip install pygame-ce
2 - Instalar o compilador empacotador pyintaller -> pip install pyintaller
3 - Para debugar e executar teste do jogo, este deverá ser sempre através do main.py


# Para compilar o projeto e Compilar o executável com todos os arquivos dentro -> 
# pyinstaller --onefile --windowed --add-data "assets;assets" main.py









# Música
1 - Para debugar e não gerar erro para encontrar o arquivo da música, utilizar caminho absoluto.
2 - Quando for compilar e gerar o executável, utilizar o caminho relativo.

Obs.: Para debugar o projeto usando o VScode, e o caminho que aponta para o arquivo MP3, não seja encontrado,
comente as linhas no arquivo (historia.py), todo o bloco Música e a linha (pygame.mixer.music.fadeout..) no final do arquivo bloco EVENTOS:

#########################
#    Música             #
#########################
pygame.mixer.init()                            

relativo -> caminho_musica = caminho_recurso("assets/sons/medieval.mp3")

absoluto -> caminho_musica = caminho_recurso(r"C:\Onedrive-Univassouras\OneDrive - Universidade de Vassouras\1 período\Matérias\Pensamento Computacional\TextGame\JogoGrupo\01 - RPG - Desenvolvimento\dist\assetss\sons\medieval.mp3")
  

print(caminho_musica)

pygame.mixer.music.load(caminho_musica)


# =====================================
# EVENTOS
# =====================================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:

                    pygame.mixer.music.fadeout(2000) ->Fade da música ao entrar na partida

                    executando = False
