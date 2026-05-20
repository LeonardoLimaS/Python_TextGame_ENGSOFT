Para funcionamento do projeto

1 - Instalar o Pygame versão comunity -> pip install pygame-ce
2 - Instalar o compilador empacotador pyintaller -> pip install pyintaller
3 - Para debugar e executar teste do jogo, este deverá ser sempre através do main.py


# Para compilar o projeto e Compilar o executável com todos os arquivos dentro -> pyinstaller --onefile --windowed --add-data "assets;assets" main.py





# Estutura do projeto
# Documentação do Projeto
# O Resgate da Princesa Layla
## Visão Geral

O projeto **O Resgate da Princesa Layla** é um RPG 2D desenvolvido em Python utilizando a biblioteca Pygame.

O jogo possui:

* Sistema de batalhas;
* Introdução cinematográfica estilo Star Wars;
* Interface visual em ASCII retrô;
* Efeito CRT;
* Sistema de classes;
* Sistema de poções;
* Sistema de defesa;
* Game Over;
* Tela de vitória.

O objetivo do jogador é derrotar os inimigos e salvar a princesa Layla.

---

# Tecnologias Utilizadas

* Python
* Pygame
* Programação Orientada a Objetos (POO)

---

# Estrutura do Projeto

```text
TextGame/
│
├── main.py
├── batalha.py
├── personagens.py
├── historia.py
├── interface.py
├── config.py
├── utilidades.py
├── assets/
│   ├── sons/
│   │   └── medieval.mp3
│   └── imagens/
│
└── build/
```

---

# Explicação de Cada Arquivo

## main.py

Arquivo principal do jogo.

Responsável por:

* iniciar o pygame;
* criar a janela;
* controlar o fluxo do jogo;
* selecionar classes;
* iniciar batalhas;
* controlar reinício do jogo.

### Principais funções

#### jogo()

Função principal.

Fluxo:

1. Introdução;
2. Escolha da classe;
3. Batalha 1;
4. Batalha 2;
5. Chefe final;
6. Vitória ou derrota.

---

#### escolher_classe(tela)

Permite ao jogador escolher:

* Guerreiro;
* Arqueiro;
* Mago.

Cada classe possui atributos diferentes.

---

# batalha.py

Responsável pelo sistema de combate.

## Função principal

### tela_batalha(tela, jogador, inimigo)

Executa:

* HUD da batalha;
* desenho das barras de vida;
* ações do jogador;
* ataques;
* defesa;
* poções;
* dano do inimigo;
* verificação de vitória e derrota.

---

## Sistema de Ataque

O dano é aleatório:

```python
random.randint(ataque_min, ataque_max)
```

---

## Sistema de Defesa

Quando o jogador escolhe defender:

```python
defesa = jogador.defender()
```

O dano recebido é reduzido.

---

## Sistema de Poções

Recupera HP:

```python
cura = jogador.usar_pocao()
```

---

# personagens.py

Define a classe Personagem.

## Classe Personagem

Atributos:

```python
nome
vida
vida_max
ataque_min
ataque_max
pocoes
```

---

## Métodos

### atacar()

Retorna dano aleatório.

---

### defender()

Retorna valor de defesa.

---

### usar_pocao()

Recupera vida.

---

# historia.py

Responsável pelas telas narrativas.

## Funções

### tela_introducao(tela)

Mostra:

* estrelas;
* introdução estilo Star Wars;
* perspectiva 3D;
* efeito CRT;
* animação do texto.

---

### tela_game_over(tela)

Mostra:

* tela de derrota;
* opção de reiniciar;
* opção de sair.

---

### tela_vitoria(tela)

Mostra a tela final após derrotar Malzor.

---

# interface.py

Responsável pela interface visual.

## Funções

### desenhar_texto()

Renderiza texto na tela.

---

### desenhar_barra_vida()

Cria barra de vida em ASCII:

```text
[##########----------]
```

---

### desenhar_caixa_ascii()

Desenha caixas estilo terminal retrô.

---

# config.py

Arquivo de configurações globais.

## Configurações principais

```python
LARGURA = 1024
ALTURA = 768
FPS = 60
```

---

## Cores

```python
PRETO
BRANCO
VERDE
AZUL
VERMELHO
```

---

# utilidades.py

Arquivo de funções auxiliares.

## caminho_recurso()

Usado para localizar arquivos quando o jogo é compilado em executável.

Compatível com:

* PyInstaller;
* executáveis Windows.

---

# Sistema Visual ASCII

O projeto utiliza:

* fonte Consolas;
* barras de vida ASCII;
* caixas estilo terminal;
* interface retrô.

Exemplo:

```text
[##########----------] 50/100
```

---

# Sistema CRT

O efeito CRT simula monitores antigos.

Elementos:

* scanlines;
* overlay escuro;
* brilho verde;
* visual retrô.

Código utilizado:

```python
for y in range(0, ALTURA, 4):
    pygame.draw.line(...)
```

---

# Introdução Estilo Star Wars

A introdução utiliza:

* perspectiva;
* escalonamento;
* inclinação;
* movimento vertical;
* profundidade.

O texto diminui conforme sobe na tela.

---

# Sistema de Eventos

Todo o jogo utiliza o sistema de eventos do Pygame:

```python
for evento in pygame.event.get():
```

Eventos principais:

* teclado;
* fechamento da janela;
* interação do jogador.

---

# Fluxo do Jogo

```text
INTRODUÇÃO
     ↓
ESCOLHA DA CLASSE
     ↓
BATALHA 1
     ↓
BATALHA 2
     ↓
CHEFE FINAL
     ↓
VITÓRIA
```

---

# Classes Disponíveis

## Guerreiro

```text
HP: 120
Ataque: 10-18
Poções: 2
```

---

## Arqueiro

```text
HP: 100
Ataque: 12-20
Poções: 2
```

---

## Mago

```text
HP: 80
Ataque: 15-25
Poções: 3
```

---

# Inimigos

## Lobo Sombrio

```text
HP: 50
Ataque: 8-14
```

---

## Cavaleiro Corrompido

```text
HP: 80
Ataque: 10-18
```

---

## Malzor

```text
HP: 120
Ataque: 12-22
```

---

# Compilação do Projeto

## Instalar PyInstaller

```bash
pip install pyinstaller
```

---

## Gerar executável

```bash
pyinstaller --onefile --windowed main.py
```

---

# Problemas Resolvidos Durante o Desenvolvimento

## Terminal aparecendo junto com o Pygame

Solução:

```bash
--windowed
```

---

## Assets não encontrados

Solução:

uso da função:

```python
caminho_recurso()
```

---

## Reinício do jogo mantendo vida do inimigo

Solução:

recriar os inimigos dentro da função jogo().

---

## Defesa e poção não funcionando

Correção da lógica de batalha.

---

# Melhorias Futuras

* inventário;
* sistema de níveis;
* múltiplos mapas;
* animações;
* efeitos sonoros;
* ataques especiais;
* sprites animados;
* salvamento de progresso.

---

# Conclusão

O projeto demonstra conceitos importantes de:

* programação em Python;
* orientação a objetos;
* manipulação gráfica;
* desenvolvimento de jogos;
* eventos;
* interfaces visuais;
* efeitos retrô.

O jogo combina elementos clássicos de RPG com visual ASCII cinematográfico inspirado em jogos retrô e na abertura de Star Wars.




