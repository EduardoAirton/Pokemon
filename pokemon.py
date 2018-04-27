# Eduardo Airton
#Tipos de pokemon usados: Fogo - Agua - Eletrico - Grama - Gelo
import os
import random

os.system('cls') #Limpa o prompt
os.system('mode con: cols=150 lines=40') #Determina o tamanho do console

class Pokemons:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.pontos = 0
        self.stamina = 5
        self.vida = 100

    def adicionar_pontos(self):
        self.pontos += 1

class pokemonFogo(Pokemons):
    def __init__(self, nome):
        super().__init__("Charizard")
        self.ATAQUE1 = 10
        self.ATAQUE2 = 20
        self.ATAQUE3 = 35

class pokemonAgua(Pokemons):
    def __init__(self, nome):
        super().__init__("Blastoise")

class pokemonEletrico(Pokemons):
    def __init__(self, nome):
        super().__init__("Electabuzz")

class pokemonGrama(Pokemons):
    def __init__(self, nome):
        super().__init__("Vileplume")

class pokemonGelo(Pokemons):
    def __init__(self, nome):
        super().__init__("Jynx")



# def desenha_ring(altura = 15, largura = 60, simbolo = '#', preenchimento = ' '):
#     print(simbolo * largura)
#     for _ in range(altura-2):
#         print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
#     print(simbolo * largura)
