import random
import time
import os
from utilidades import Utilidades

# # =========================
# # UTILIDADES
# # =========================

# def limpar():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def pausa(seg=1.5):
#     time.sleep(seg)

# def narrar(texto, seg=2):
#     print(texto)
#     time.sleep(seg)

# # =========================
# # PERSONAGEM
# # =========================

# class Personagem:
#     def __init__(self, nome, vida, ataque_min, ataque_max, pocoes=1):
#         self.nome = nome
#         self.vida = vida
#         self.vida_max = vida
#         self.ataque_min = ataque_min
#         self.ataque_max = ataque_max
#         self.pocoes = pocoes

#     def atacar(self):
#         return random.randint(self.ataque_min, self.ataque_max)

#     def defender(self):
#         return random.randint(4, 8)

#     def usar_pocao(self):
#         if self.pocoes > 0:
#             cura = random.randint(15, 25)
#             self.vida = min(self.vida + cura, self.vida_max)
#             self.pocoes -= 1
#             print(f"\n🧪 Você recuperou {cura} HP!")
#         else:
#             print("\n❌ Sem poções!")

# # =========================
# # SISTEMA DE BATALHA
# # =========================

# def batalha(jogador, inimigo):
#     print(f"\n⚔️ {inimigo.nome} apareceu!\n")
#     pausa()

#     while jogador.vida > 0 and inimigo.vida > 0:

#         print(f"{jogador.nome}: {jogador.vida} HP")
#         print(f"{inimigo.nome}: {inimigo.vida} HP\n")

#         print("1 - Atacar")
#         print("2 - Defender")
#         print("3 - Usar Poção")
#         escolha = input("\nEscolha: ")

#         defesa = 0

#         if escolha == "1":
#             dano = jogador.atacar()
#             inimigo.vida -= dano
#             print(f"\n⚔️ Você causou {dano} de dano!")

#         elif escolha == "2":
#             defesa = jogador.defender()
#             print(f"\n🛡 Defesa ativa! Reduzirá {defesa} de dano.")

#         elif escolha == "3":
#             jogador.usar_pocao()

#         else:
#             print("Escolha inválida!")
#             continue

#         pausa()

#         if inimigo.vida > 0:
#             dano_inimigo = inimigo.atacar()
#             dano_inimigo = max(0, dano_inimigo - defesa)
#             jogador.vida -= dano_inimigo
#             print(f"💀 {inimigo.nome} causou {dano_inimigo} de dano!")

#         pausa()

#     if jogador.vida > 0:
#         print(f"\n🏆 {inimigo.nome} foi derrotado!")
#         jogador.vida = min(jogador.vida + 10, jogador.vida_max)
#         print("✨ Você recuperou 10 HP após a batalha!")
#         pausa(2)
#         return True
#     else:
#         return False

# # =========================
# # HISTÓRIA
# # =========================

# def introducao():
#     limpar()
#     print("🏰 ======================================= 🏰")
#     print("        O RESGATE DA PRINCESA LAYLA ")
#     print("🏰 ======================================= 🏰\n")
#     pausa(2)

#     narrar("Ano 1247...")
#     narrar("O necromante Malzor retorna das sombras.")
#     narrar("A princesa Layla foi sequestrada.")
#     narrar("O reino está à beira da destruição.\n")

#     narrar("O rei proclama:")
#     narrar('"Quem salvar minha filha será eterno!"\n')

#     narrar("Você aceita a missão...\n")

#     print("Escolha sua resposta:")
#     print("1 - 'Não temo as sombras.'")
#     print("2 - 'Pelo reino e pela honra.'")
#     print("3 - Permanecer em silêncio.")

#     escolha = input("\nSua escolha: ")

#     if escolha == "1":
#         narrar("\nAs sombras parecem se agitar...")
#     elif escolha == "2":
#         narrar("\nO vento sopra em aprovação...")
#     else:
#         narrar("\nO silêncio fortalece sua presença...")

#     narrar("\nVocê parte rumo à Floresta Sombria...")
#     pausa(2)

# def antes_do_chefe():
#     narrar("\n🏰 A Fortaleza Negra surge diante de você.")
#     narrar("Relâmpagos cortam o céu.")
#     narrar("Malzor aguarda no trono sombrio...\n")
#     pausa(2)

# def final_bom():
#     narrar("\nMalzor cai derrotado.")
#     narrar("A princesa corre até você.")
#     narrar("O reino está salvo!\n")
#     print("👑 FINAL HEROICO 👑")

# def final_ruim():
#     narrar("\nAs sombras consomem tudo...")
#     print("💀 VOCE PERDEU,FALTOU DETERMINAÇAO 💀")

# =========================
# JOGO PRINCIPAL
# =========================

# def jogo():

#     introducao()

#     print("\nEscolha sua classe:")
#     print("1 - Guerreiro (120 HP)")
#     print("2 - Arqueiro (100 HP)")
#     print("3 - Mago (80 HP)")

#     escolha = input("\nClasse: ")

#     if escolha == "1":
#         jogador = Personagem("Guerreiro", 120, 10, 18, 2)
#     elif escolha == "2":
#         jogador = Personagem("Arqueiro", 100, 12, 20, 2)
#     else:
#         jogador = Personagem("Mago", 80, 15, 25, 3)

#     # Inimigos
#     lobo = Personagem("Lobo Sombrio", 50, 8, 14)
#     cavaleiro = Personagem("Cavaleiro Corrompido", 80, 10, 18)
#     malzor = Personagem("Malzor, o Necromante", 120, 12, 22)

#     narrar("\n🌲 Um Lobo Sombrio surge na floresta!")
#     if not batalha(jogador, lobo):
#         final_ruim()
#         return

#     narrar("\n⚔️ Um Cavaleiro Corrompido bloqueia seu caminho!")
#     if not batalha(jogador, cavaleiro):
#         final_ruim()
#         return

#     antes_do_chefe()

#     if not batalha(jogador, malzor):
#         final_ruim()
#         return

#     final_bom()

# # =========================
# # INICIAR
# # =========================

# if __name__ == "__main__":
#     jogo()