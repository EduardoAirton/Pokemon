class Mensagens():

    @staticmethod
    def roundInicio(self, round):
        roundString = "===================================== - Round {} - =====================================\n".format(round)
        print(roundString.center(150))

    @staticmethod
    def vidaMessage(self, pokemon1, pokemon2):
        vida = "Vida {} = {} ******** Vida {} = {}".format(pokemon1.nome, pokemon1.vida, pokemon2.nome, pokemon2.vida)
        print(vida.center(145))

    @staticmethod
    def vencedorMessage(self, pokemon):
        print("VENCEDOR FOI {}".format(pokemon.nome))

    @staticmethod
    def ataqueMessage(self, pokemonAtaque, pokemonDefesa, dano, opcao):
        print("====================================================")
        if opcao == 0:
            print("{} atacou e {} Tomou {} de DANO".format(pokemonAtaque.nome, pokemonDefesa.nome, dano))
        else:
            print("{} utilizou o ESPECIAL e {} Tomou {} de DANO".format(pokemonAtaque.nome, pokemonDefesa.nome, dano))
        print("====================================================\n")

    @staticmethod
    def errorMessage(self):
        print("\n----------------------\nERRO\nDigite um numero valido!\n------------------------\n")
