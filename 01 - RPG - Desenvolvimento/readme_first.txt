Para funcionamento do projeto

1 - Instalar o Pygame versão comunity -> pip install pygame-ce
2 - Instalar o compilador empacotador pyintaller -> pip install pyintaller
3 - Para debugar e executar teste do jogo, este deverá ser sempre através do main.py


# Para compilar o projeto e Compilar o executável com todos os arquivos dentro -> 
# pyinstaller --onefile --windowed --add-data "assets;assets" main.py


Obs.: Para debugar o projeto usando o VScode, o caminho que aponta para o arquivo MP3, não é encontrado,
comente as linhas no arquivo (historia.py):


Comentar todo esse bloco
#########################
#    Música             #
#########################
#pygame.mixer.init()                            

#caminho_musica = caminho_recurso(
#    "assets/sons/medieval.mp3"
#)

#print(caminho_musica)

#pygame.mixer.music.load(caminho_musica)



Comentar somente a linha ....mixer.music.fadeout...
# =====================================
# EVENTOS
# =====================================

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:

                    #pygame.mixer.music.fadeout(2000) <<<<-------------------------- COMENTAR

                    executando = False
