# Eduardo Airton
#http://jogandootpokemon.blogspot.com.br/2013/04/tipos-de-pokemon-e-suas.html
#Tipos de pokemon usados: Fogo - Agua - Eletrico - Grama - Gelo
import os
import random
from artes import Artes

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

    def atacar(self):
        print("1 - Ataque 1\n2 - Ataque 2\n3 - Defender\n4 - ESPECIAL\n")
        ataque = input()
        return ataque

class pokemonFogo(Pokemons):
    def __init__(self, nome):
        super().__init__("Charizard")
        self.tipo = "Fogo"
        self.FORTE1 = "Grama"
        self.FRACO1 = "Agua"
        self.FRACO2 = "Fogo"
        self.arte = Artes.fogo;

class pokemonAgua(Pokemons):
    def __init__(self, nome):
        super().__init__("Blastoise")
        self.tipo = "Agua"
        self.FORTE1 = "Fogo"
        self.FRACO1 = "Agua"
        self.FRACO2 = "Grama"

class pokemonEletrico(Pokemons):
    def __init__(self, nome):
        super().__init__("Electabuzz")
        self.tipo = "Eletrico"
        self.FORTE1 = "Agua"
        self.FRACO1 = "Fogo"
        self.FRACO2 = "Grama"

class pokemonGrama(Pokemons):
    def __init__(self, nome):
        super().__init__("Vileplume")
        self.tipo = "Grama"
        self.FORTE2 = "Gelo"
        self.FRACO1 = "Agua"
        self.FRACO2 = "Fogo"

class pokemonGelo(Pokemons):
    def __init__(self, nome):
        super().__init__("Jynx")
        self.tipo = "Gelo"
        self.FORTE1 = "Grama"
        self.FRACO1 = "Fogo"
        self.FRACO2 = "Agua"

if __name__ == '__main__':
    poke = Artes()
    poke.pokemon3()






# def desenha_ring(altura = 15, largura = 60, simbolo = '#', preenchimento = ' '):
#     print(simbolo * largura)
#     for _ in range(altura-2):
#         print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
#     print(simbolo * largura)
