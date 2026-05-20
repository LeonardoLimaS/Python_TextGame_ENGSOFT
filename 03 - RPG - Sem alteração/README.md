Para funcionamento do projeto

1 - Instalar o Pygame versão comunity -> pip install pygame-ce
2 - Instalar o compilador empacotador pyintaller -> pip install pyintaller
3 - Para debugar e executar teste do jogo, este deverá ser sempre através do main.py


# Para compilar o projeto e Compilar o executável com todos os arquivos dentro -> pyinstaller --onefile --windowed --add-data "assets;assets" main.py


# Estutura do projeto

JogoGrupo/

│ main.py
│ config.py
│ personagens.py
│ batalha.py
│ historia.py
│ interface.py
│ utilidades.py
│

└── assets/
    │
    ├── sons/
    │   └── medieval.mp3
    │
    ├── imagens/
    │
    └── fontes/



# Organização do projeto

- main.py - Cérebro principal do RPG
✅ inicialização do jogo
✅ criação da janela
✅ fluxo das telas
✅ criação do jogador
✅ criação dos inimigos
✅ ordem das batalhas
✅ reinício do jogo
✅ tela de vitória e derrota



- Config.py - Configurações globais
✅ resolução da tela
✅ FPS
✅ cores
✅ constantes do jogo


- persongens.py - Classe dos personagens
✅ jogador
✅ inimigos
✅ ataque
✅ defesa
✅ poções
✅ vida


- batalha.py - Sistema de combate
✅ HUD da batalha
✅ ataques
✅ defesa
✅ uso de poções
✅ turnos
✅ barras de vida
✅ mensagens de combate


- historia.py - Sistema narrativo e telas
✅ introdução cinematográfica
✅ game over
✅ vitória
✅ efeitos visuais
✅ música
✅ partículas
✅ narrativa


- interface.py - Sistema visual/UI
✅ desenhar textos
✅ desenhar barras de vida
✅ fontes
✅ HUD
✅ renderização gráfica


- utilidades.py - Funções auxiliares
✅ caminhos de assets
✅ compatibilidade com EXE
✅ funções reutilizáveis


📁 assets/ - Arquivos externos do jogo

📁 assets/sons/
✅ música medieval
✅ efeitos sonoros
✅ sons de batalha


📁 assets/imagens/
✅ fundos
✅ sprites
✅ personagens
✅ efeitos
✅ interface


📁 assets/fontes/
✅ fontes customizadas
✅ estilo medieval
✅ fontes pixel art





# Fluxo do Jogo

main.py
↓
historia.py
↓
escolher classe
↓
batalha.py
↓
vitória/derrota
↓
reinício




