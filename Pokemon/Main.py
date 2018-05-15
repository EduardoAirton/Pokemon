# Eduardo Airton
#http://jogandootpokemon.blogspot.com.br/2013/04/tipos-de-pokemon-e-suas.html
#Tipos de pokemon usados: Fogo - Agua - Eletrico - Grama - Gelo
import os
from random import randint
from Artes import Artes

os.system('cls') #Limpa o prompt
os.system('mode con: cols=150 lines=40') #Determina o tamanho do console

class Pokemons:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.pontos = 0
        self.stamina = 2
        self.vida = 100
        self.defesa = False

    def adicionar_pontos(self):
        self.pontos += 1

    def atacar(self):
        ataque = 0
        i = 1

        while i != 0:
            print("Stamina = {}".format(self.stamina))
            print("1 - Atacar\n2 - Defender\n3 - ESPECIAL\n4 - Passar")
            ataque = int(input("-> "))
            if (ataque == 1 and self.stamina < 1) or (ataque == 2 and self.stamina < 2) or (ataque == 3 and self.stamina < 5):
                print("Stamina insuficiente")
            else:
                i = 0
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
        round = 0
        ataque1 = 0
        ataque2 = 0

        while round < 3:
            self.pokemon1.vida = 100
            self.pokemon2.vida = 100
            round += 1
            print("Round {}".format(round))
            
            while self.pokemon1.vida > 0 and self.pokemon2.vida > 0:

                if self.pokemon1.stamina < 5:
                    self.pokemon1.stamina += 1
                if self.pokemon2.stamina < 5:
                    self.pokemon2.stamina+= 1

                while self.pokemon1.stamina > 0:
                    print("Vida {} = {} ******** Vida {} = {}".format(self.pokemon1.nome,self.pokemon1.vida, self.pokemon2.nome, self.pokemon2.vida))
                    ataque1 = self.pokemon1.atacar()
                    if ataque1 == 4:
                        break
                    self.verificarAtaque(ataque1, self.pokemon1, self.pokemon2)

                while self.pokemon2.stamina > 0:
                    ataque2 = self.criarAtaque(self.pokemon2)
                    if ataque2 == 4:
                        break
                    print("TESTEEEEE ATAQUE2 = {}".format(ataque2))

                    self.verificarAtaque(ataque2, self.pokemon2, self.pokemon1)
                continue

    def verificarAtaque(self, tipoAtaque, pokemonAtaque, pokemonDefesa):
        #Fazer a parte de verificação de defesa
        if tipoAtaque == 1:
            pokemonAtaque.stamina -= 1
            if pokemonAtaque.FORTE1 == pokemonDefesa.tipo:
                pokemonDefesa.vida -= 15
                print("ATAQUE FORTE\n")
                print("{} atacou e {} Tomou 15 de DANO".format(pokemonAtaque.nome, pokemonDefesa.nome))
            elif (pokemonAtaque.FRACO1 or pokemonAtaque.FRACO2) == pokemonDefesa.tipo:
                pokemonDefesa.vida -= 5
                print("ATAQUE FRACO\n")
                print("{} Tomou 5 de DANO".format(pokemonDefesa.nome))
            else:
                pokemonDefesa.vida -= 10
                print("ATAQUE\n")
                print("{} atacou e {} Tomou 10 de DANO".format(pokemonAtaque.nome, pokemonDefesa.nome))

        elif tipoAtaque == 2:
            pokemonAtaque.stamina -= 2
            pokemonAtaque.defesa = True
        elif tipoAtaque == 3:
            print("{} utilizou o ESPECIAL e {} Tomou 25 de DANO".format(pokemonAtaque.nome, pokemonDefesa.nome))
            pokemonDefesa.vida -= 25
            pokemonAtaque.stamina -= 5
        else:
            return
        return

    def criarAtaque(self, pokemonAtaque):
        ataque = 0
        i = 1

        while i != 0:
            ataque = randint(0,5)
            print("Ataque = {}".format(ataque))
            if pokemonAtaque.stamina == 5:
                return 3
            elif ataque == 5:
                return 4
            elif (ataque == 1 and pokemonAtaque.stamina < 1) or (ataque == 2 and pokemonAtaque.stamina < 2) or (ataque == 3 and pokemonAtaque.stamina < 5):
                i = 1
            else:
                i = 0

        return ataque


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
