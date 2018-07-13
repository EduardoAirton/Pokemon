# Eduardo Airton
#Tipos de pokemon usados: Fogo - Agua - Eletrico - Grama - Gelo

#Imports
import os
from random import randint
from Artes import Artes
from Pokemon import *
from Mensagens import *

os.system('cls') #Limpa o prompt
os.system('mode con: cols=150 lines=40') #Determina o tamanho do console

# Inicia uma luta e so termina quando 1 dos pokemons vence 2 ou mais lutas
class Luta():

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        self.pokemon1_lutaPontos = 0
        self.pokemon2_lutaPontos = 0

    def lutar(self):
        mensagem = Mensagens()
        print("====LUTA INICIADA====\n")
        print("== {} VS {} ==".format(self.pokemon1.nome, self.pokemon2.nome))
        round = 0
        ataque1 = 0
        ataque2 = 0
        pokemonRodada1 = 0
        pokemonRodada2 = 0

        while round < 3:

            self.pokemon1.vida = 100
            self.pokemon2.vida = 100
            round += 1
            os.system('cls') #Limpa o prompt
            mensagem.roundInicio(self, round)

            # Verifica se ambos os pokemons estao vivos caso contrario finaliza o round
            while self.pokemon1.vida > 0 and self.pokemon2.vida > 0:

                if self.pokemon1.stamina < 5:
                    self.pokemon1.stamina += 1
                if self.pokemon2.stamina < 5:
                    self.pokemon2.stamina+= 1

                # Continua rodando até que o pokemon fique sem stamina deixando o mesmo atacar enquanto tiver stamina disponivel
                while self.pokemon1.stamina > 0:
                    mensagem.vidaMessage(self, self.pokemon1, self.pokemon2)
                    ataque1 = self.pokemon1.atacar()
                    if ataque1 == 4:
                        break
                    self.verificarAtaque(ataque1, self.pokemon1, self.pokemon2)

                while self.pokemon2.stamina > 0:
                    ataque2 = self.criarAtaque(self.pokemon2)
                    if ataque2 == 4:
                        break
                    self.verificarAtaque(ataque2, self.pokemon2, self.pokemon1)
                continue
            #Atribui o vencedor
            if self.pokemon1.vida <= 0:
                mensagem.vidaMessage(self, pokemon2)
                pokemonRodada2 += 1
            else:
                mensagem.vidaMessage(self, pokemon1)
                pokemonRodada1 += 1

        # Verifica quem tem a maior quantidade de vitorias por rodada para anunciar o vencedor da partida
        if pokemonRodada1 > pokemonRodada2:
            mensagem.vidaMessage(self, pokemon1)
            self.pokemon1.adicionar_pontos()
        else:
            mensagem.vidaMessage(self, pokemon2)
            self.pokemon2.adicionar_pontos()

    # Verifica qual sera o nível do ataque dado
    def verificarAtaque(self, tipoAtaque, pokemonAtaque, pokemonDefesa):
        mensagem = Mensagens()
        dano = 0
        #Colocar o codigo repetido em uma função
        if tipoAtaque == 1:
            pokemonAtaque.stamina -= 1
            if pokemonAtaque.FORTE1 == pokemonDefesa.tipo:
                if pokemonDefesa.defesa == True:
                    print("\nATAQUE COM DEFESA")
                    pokemonDefesa.vida -= 8
                    dano = 8
                    pokemonDefesa.defesa == False
                else:
                    print("\nATAQUE FORTE")
                    pokemonDefesa.vida -= 15
                    dano = 15

            elif (pokemonAtaque.FRACO1 or pokemonAtaque.FRACO2) == pokemonDefesa.tipo:
                if pokemonDefesa.defesa == True:
                    print("\nATAQUE COM DEFESA")
                    pokemonDefesa.vida -= 5
                    dano = 5
                    pokemonDefesa.defesa == False
                else:
                    print("\nATAQUE FRACO")
                    pokemonDefesa.vida -= 8
                    dano = 8
                mensagem.ataqueMessage(self, pokemonAtaque, pokemonDefesa, dano, 0)
            else:
                if pokemonDefesa.defesa == True:
                    print("\nATAQUE COM DEFESA")
                    pokemonDefesa.vida -= 5
                    dano = 5
                    pokemonDefesa.defesa == False
                else:
                    print("\nATAQUE")
                    pokemonDefesa.vida -= 10
                    dano = 10
                mensagem.ataqueMessage(self, pokemonAtaque, pokemonDefesa, dano, 0)

        elif tipoAtaque == 2:
            pokemonAtaque.stamina -= 2
            pokemonAtaque.defesa = True
        elif tipoAtaque == 3:
            pokemonAtaque.stamina -= 5
            if pokemonDefesa.defesa == True:
                pokemonDefesa.vida -= 20
                pokemonDefesa.defesa == False
                dano = 20
            else:
                pokemonDefesa.vida -= 25
                dano = 25
            mensagem.ataqueMessage(self, pokemonAtaque, pokemonDefesa, dano, 1)
        else:
            return
        return

    # Retorna uma atque aleatorio para o adversario tentando criar varias formas de dificultar e dar mais dano ao pokemon adversario
    def criarAtaque(self, pokemonAtaque):
        ataque = 0
        i = 1

        while i != 0:
            ataque = randint(1,6)
            if pokemonAtaque.stamina == 5:
                return 3
            elif ataque == 5:
                return 4
            elif ataque == 6:
                return 1
            elif ((ataque == 1 or ataque == 6) and pokemonAtaque.stamina < 1) or (ataque == 2 and pokemonAtaque.stamina < 2) or (ataque == 3 and pokemonAtaque.stamina < 5):
                i = 1
            else:
                i = 0

        return ataque

# Main
if __name__ == '__main__':
    # todosPokemonsVivos = true
    nomePokemon = input("Escolha seu Pokemon \n Digite o nome: ")
    #tipoPokemon sera feito pelo thinker a ser finalizado

    # while(todosPokemonsVivos):
    #     #Roda todo o campeonato

    p1 = PokemonFogo("Eduardo")
    p2 = PokemonGelo("Outro")
    resultado = Luta(p1, p2)
    resultado.lutar()
