````md
# 🏰 O Resgate da Princesa Layla

Um jogo RPG retrô em ASCII desenvolvido em Python utilizando a biblioteca Pygame.

O projeto combina:
- batalhas por turnos
- animações em ASCII
- efeitos CRT
- introdução cinematográfica estilo Star Wars
- música medieval
- interface retrô inspirada em jogos clássicos

---

# 🎮 Gameplay

O jogador escolhe uma classe e enfrenta inimigos até chegar ao chefe final: Malzor, o necromante sombrio.

Durante as batalhas é possível:
- atacar
- defender
- usar poções
- visualizar animações
- acompanhar barras de vida em ASCII

---

# 📖 História

No ano de 1247, o reino mergulhou nas sombras.

O necromante Malzor retornou após décadas desaparecido e sequestrou a princesa Layla.

Criaturas amaldiçoadas espalharam o caos pelas terras do reino.

Agora apenas um herói poderá enfrentar o exército sombrio e salvar Layla antes que o reino seja destruído.

---

# ✨ Funcionalidades

## ⚔️ Sistema de batalha RPG
- combate por turnos
- dano aleatório
- defesa dinâmica
- sistema de poções

---

## 🎞️ Introdução cinematográfica
- texto em perspectiva estilo Star Wars
- rolagem 3D
- estrelas animadas
- profundidade visual

---

## 👾 ASCII ART
- personagens desenhados em ASCII
- inimigos em ASCII
- chefes em ASCII

---

## 🎬 Animações
- animação de ataque
- animação de defesa
- animação de cura
- movimentação dos personagens

---

## 📺 Efeito CRT Retrô
- scanlines
- overlay escuro
- visual de monitor antigo

---

## 🔊 Música
- música medieval de fundo
- fadeout ao iniciar o jogo

---

# 🧙 Classes Jogáveis

| Classe | Vida | Dano |
|---|---|---|
| Guerreiro | 120 HP | 10 ~ 18 |
| Arqueiro | 100 HP | 12 ~ 20 |
| Mago | 80 HP | 15 ~ 25 |

---

# 👹 Inimigos

| Inimigo | Tipo |
|---|---|
| Lobo Sombrio | Monstro |
| Cavaleiro Corrompido | Elite |
| Malzor | Boss Final |

---

# 🖥️ Tecnologias Utilizadas

- Python 3
- Pygame

---

# 📂 Estrutura do Projeto

```bash
Projeto/
│
├── main.py
├── batalha.py
├── historia.py
├── interface.py
├── personagens.py
├── ascii_art.py
├── config.py
├── utilidades.py
│
├── assets/
│   └── sons/
│       └── medieval.mp3
````

---

# 📜 Explicação dos Arquivos

## main.py

Arquivo principal do jogo.

Responsável por:

* iniciar o jogo
* seleção de classe
* gerenciamento das batalhas
* fluxo geral do jogo

---

## batalha.py

Responsável por:

* sistema de combate
* HUD de batalha
* animações
* dano
* defesa
* uso de poções

---

## historia.py

Responsável pelas telas:

* introdução
* vitória
* game over

Também controla:

* introdução estilo Star Wars
* música
* estrelas
* efeitos visuais

---

## interface.py

Responsável pelos elementos gráficos:

* textos
* barra de vida
* ASCII ART
* efeito CRT
* caixas ASCII

---

## personagens.py

Classe dos personagens.

Contém:

* atributos
* ataque
* defesa
* cura
* sistema de poções

---

## ascii_art.py

Armazena todas as artes ASCII:

* heróis
* monstros
* chefe final

---

## config.py

Configurações globais:

* resolução
* FPS
* cores

---

## utilidades.py

Funções auxiliares do projeto.

Principal função:

* carregamento seguro de assets para PyInstaller

---

# ⚔️ Sistema de Combate

## Comandos

| Tecla | Ação       |
| ----- | ---------- |
| 1     | Atacar     |
| 2     | Defender   |
| 3     | Usar Poção |

---

# 🎬 Sistema de Animações

## Ataque

O personagem avança em direção ao inimigo.

## Defesa

Escudo visual animado ao redor do jogador.

## Cura

Efeito circular de energia verde.

---

# 📺 Efeito CRT

O jogo utiliza:

* scanlines horizontais
* overlay escuro transparente
* visual retrô

Inspirado em monitores antigos.

---

# 🔊 Música

A música medieval é carregada através da pasta:

```bash
assets/sons/medieval.mp3
```

---

# ▶️ Como Executar

## Instalar dependências

```bash
pip install pygame
```

---

## Rodar o jogo

```bash
python main.py
```

---

# 📦 Gerar Executável (.exe)

## Instalar PyInstaller

```bash
pip install pyinstaller
```

---

## Gerar executável

```bash
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
```

---

# 🧠 Conceitos de Programação Utilizados

O projeto utiliza:

* Programação Orientada a Objetos
* Modularização
* Loops
* Eventos
* Renderização gráfica
* Manipulação de superfícies
* Sistema de animação
* Randomização
* Estados de jogo
* Interface gráfica
* Organização de projeto

---

# 🚀 Melhorias Futuras

* sistema de níveis
* inventário
* mapa explorável
* loja
* magias especiais
* efeitos sonoros
* partículas
* múltiplos bosses
* save/load
* multiplayer local

---

# 👨‍💻 Autor

Projeto desenvolvido para fins educacionais utilizando Python + Pygame.

---

# 📜 Licença

Projeto livre para estudos, modificações e aprendizado.

```
```
