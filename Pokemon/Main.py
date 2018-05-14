# Eduardo Airton
#http://jogandootpokemon.blogspot.com.br/2013/04/tipos-de-pokemon-e-suas.html
#Tipos de pokemon usados: Fogo - Agua - Eletrico - Grama - Gelo
import os
import random
from Artes import Artes

os.system('cls') #Limpa o prompt
os.system('mode con: cols=150 lines=40') #Determina o tamanho do console

class Pokemons:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.pontos = 0
        self.stamina = 3
        self.vida = 100
        self.defesa = False

    def adicionar_pontos(self):
        self.pontos += 1

    def atacar(self):
        print("Stamina = {}".format(self.stamina))
        print("1 - Atacar\n2 - Defender\n3 - ESPECIAL\n4 - Passar")
        ataque = int(input("-> "))
        if (ataque == 1 and self.stamina > 1) or (ataque == 2 and self.stamina > 2) or (ataque == 3 and self.stamina == 5):
            return ataque


class Luta():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        self.pokemon1_lutaPontos = 0
        self.pokemon2_lutaPontos = 0

    def lutar(self):
        print("====LUTA INICIADA====\n")
        print("== {} VS {} ==".format(self.pokemon1.nome, self.pokemon2.nome))
        round = 1
        diferenca = 0
        ataque1 = 0

        while round < 3 or diferenca < 2:
            print("Round {}".format(round))
            while self.pokemon1.vida > 0 or self.pokemon2.vida > 0:
                print("Vida {} = {} ******** Vida {} = {}".format(self.pokemon1.nome,self.pokemon1.vida, self.pokemon2.nome, self.pokemon2.vida))
                resultadoAtaque = 0
                while ataque1 != 4 or self.pokemon1.stamina > 0:
                    ataque1 = self.pokemon1.atacar()
                    verificarAtaque(ataque1, self.pokemon1, self.pokemon2)

    def verificarAtaque(self, tipoAtaque, pokemonAtaque, pokemonDefesa):
        if tipoAtaque == 1:
            pokemonAtaque.stamina -= 1
            if pokemonAtaque.FORTE1 == pokemonDefesa.tipo:
                pokemonDefesa.vida -= 15
                Print("ATAQUE FORTE\n")
                print("{} atacou e {} Tomou 15 de DANO".format(pokemonAtaque.nome, pokemonDefesa.nome))
            if (pokemonAtaque.FRACO1 or pokemonAtaque.FRACO2) == pokemonDefesa.tipo:
                pokemonDefesa.vida -= 5
                Print("ATAQUE FRACO\n")
                print("{} Tomou 5 de DANO".format(pokemonDefesa.nome))
        elif tipoAtaque == 2:
            pokemonAtaque.stamina -= 2
            pokemonAtaque.defesa = True
        else:
            print("{} utilizou o ESPECIAL e {} Tomou 25 de DANO".format(pokemonAtaque.nome, pokemonDefesa.nome))
            pokemonDefesa.vida -= 25
            pokemonAtaque.stamina -= 5
        return

class PokemonFogo(Pokemons):
    def __init__(self, nome):
        super().__init__("Charizard", "Fogo")
        self.tipo = "Fogo"
        self.FORTE1 = "Grama"
        self.FRACO1 = "Agua"
        self.FRACO2 = "Fogo"
        #self.arte = Artes.fogo;
class PokemonGelo(Pokemons):
    def __init__(self, nome):
        super().__init__("Jynx", "Gelo")
        self.tipo = "Gelo"
        self.FORTE1 = "Grama"
        self.FRACO1 = "Fogo"
        self.FRACO2 = "Agua"

if __name__ == '__main__':
    p1 = PokemonFogo("Eduardo")
    p2 = PokemonGelo("Outro")
    resultado = Luta(p1, p2)

    resultado.lutar()








# def desenha_ring(altura = 15, largura = 60, simbolo = '#', preenchimento = ' '):
#     print(simbolo * largura)
#     for _ in range(altura-2):
#         print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
#     print(simbolo * largura)
