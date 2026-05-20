# README.md — O Resgate da Princesa Layla

````md
# 🏰 O Resgate da Princesa Layla

Um jogo RPG em ASCII desenvolvido em Python utilizando a biblioteca Pygame.

O jogador escolhe uma classe, enfrenta inimigos em batalhas por turnos e derrota o necromante Malzor para salvar o reino.

---

# 📖 História

No ano de 1247, o reino mergulhou nas sombras.

O necromante Malzor retornou dos mortos e sequestrou a princesa Layla.

Agora apenas um herói pode enfrentar criaturas sombrias, atravessar o reino amaldiçoado e derrotar Malzor.

O destino do reino está em suas mãos.

---

# 🎮 Funcionalidades

✅ Sistema de batalhas RPG por turnos  
✅ Escolha de classes  
✅ Arte ASCII para personagens e inimigos  
✅ Introdução cinematográfica estilo Star Wars  
✅ Sistema de poções  
✅ Sistema de defesa  
✅ Animações de ataque  
✅ Animações de defesa  
✅ Animações de cura  
✅ Efeito CRT retrô  
✅ Tela de Game Over  
✅ Tela de Vitória  

---

# 🧙 Classes Jogáveis

## Guerreiro
- Vida: 120 HP
- Dano: 10 ~ 18
- Alta resistência

## Arqueiro
- Vida: 100 HP
- Dano: 12 ~ 20
- Balanceado

## Mago
- Vida: 80 HP
- Dano: 15 ~ 25
- Alto dano

---

# 👾 Inimigos

## Lobo Sombrio
Primeiro inimigo do jogo.

## Cavaleiro Corrompido
Inimigo intermediário.

## Malzor
Chefe final do jogo.

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
* escolha de classe
* gerenciamento das batalhas
* fluxo principal

---

## batalha.py

Controla:

* sistema de combate
* ataques
* defesa
* uso de poções
* animações
* HUD da batalha

---

## historia.py

Responsável pelas telas:

* introdução
* game over
* vitória

Também contém:

* efeito Star Wars
* estrelas animadas
* música
* efeitos visuais

---

## interface.py

Responsável por:

* textos
* barra de vida
* desenho ASCII
* efeito CRT
* caixas da interface

---

## personagens.py

Classe principal dos personagens.

Contém:

* ataque
* defesa
* poções
* atributos

---

## ascii_art.py

Armazena todas as artes ASCII:

* heróis
* monstros
* chefes

---

## config.py

Configurações globais:

* resolução
* FPS
* cores

---

## utilidades.py

Funções auxiliares do projeto.

Principal:

* carregamento seguro de arquivos

---

# ⚔️ Sistema de Combate

O combate funciona por turnos.

O jogador pode:

| Tecla | Ação       |
| ----- | ---------- |
| 1     | Atacar     |
| 2     | Defender   |
| 3     | Usar Poção |

Após a ação do jogador, o inimigo realiza seu ataque.

---

# 🎞️ Introdução Cinematográfica

O jogo possui:

* rolagem de texto em perspectiva
* efeito estilo Star Wars
* estrelas no fundo
* profundidade visual

---

# 📺 Efeito CRT

O jogo aplica:

* scanlines
* overlay escuro
* aparência retrô

Inspirado em monitores antigos.

---

# ▶️ Como Executar

## Instalar dependências

```bash
pip install pygame
```

---

## Executar o jogo

```bash
python main.py
```

---

# 🔊 Música

O projeto suporta música de fundo.

Arquivo esperado:

```bash
assets/sons/medieval.mp3
```

---

# 📦 Gerar Executável (.exe)

Instale o PyInstaller:

```bash
pip install pyinstaller
```

Gerar executável:

```bash
pyinstaller --onefile --windowed main.py
```

---

# 🧠 Conceitos Utilizados

O projeto utiliza diversos conceitos de programação:

* Programação Orientada a Objetos
* Loops
* Eventos
* Funções
* Modularização
* Animações
* Manipulação gráfica
* Sistema de estados
* Randomização
* Interface gráfica

---

# 🚀 Melhorias Futuras

* Sistema de níveis
* Inventário
* Loja
* Mais inimigos
* Magias especiais
* Sons de batalha
* Efeitos visuais avançados
* Sistema de mapa
* Bosses adicionais
* Multiplayer local

---

# 👨‍💻 Autor

Projeto desenvolvido para fins educacionais utilizando Python + Pygame.

---

# 📜 Licença

Projeto livre para estudos e modificações.

```
```
