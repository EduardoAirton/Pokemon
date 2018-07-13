#Eduardo Airton

#Classe pokemon que é utilizada para instanciar um novo pokemon
class Pokemons:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.pontos = 0
        self.stamina = 0
        self.vida = 100
        self.defesa = False

    # Adiciona um ponto no campeonato quando o pokemon vence a batalha
    def adicionar_pontos(self):
        self.pontos += 1

    # Da as opcoes e faz as verificações de ataque do pokemon
    def atacar(self):
        ataque = 0
        i = 1

        while i != 0:
            try:
                print("Stamina = {}".format(self.stamina))
                print("1 - Atacar\n2 - Defender\n3 - ESPECIAL\n4 - Passar")
                ataque = int(input("-> "))
            except ValueError:
                    print(ERRORMESSAGE)
                    continue
            if ataque > 4:
                print(ERRORMESSAGE)
            if (ataque == 1 and self.stamina < 1) or (ataque == 2 and self.stamina < 2) or (ataque == 3 and self.stamina < 5):
                print("Stamina insuficiente")
            else:
                i = 0
        return ataque

class PokemonAgua(Pokemons):
    def __init__(self, nome):
        super().__init__("Blastoise", "Agua")
        self.tipo = "Agua"
        self.FORTE1 = "Fogo"
        self.FRACO1 = "Agua"
        self.FRACO2 = "Grama"

class PokemonEletrico(Pokemons):
    def __init__(self, nome):
        super().__init__("Electabuzz", "Eletrico")
        self.tipo = "Eletrico"
        self.FORTE1 = "Agua"
        self.FRACO1 = "Fogo"
        self.FRACO2 = "Grama"

class PokemonGrama(Pokemons):
    def __init__(self, nome):
        super().__init__("Vileplume", "Grama")
        self.tipo = "Grama"
        self.FORTE2 = "Gelo"
        self.FRACO1 = "Agua"
        self.FRACO2 = "Fogo"

class PokemonFogo(Pokemons):
    def __init__(self, nome):
        super().__init__("Charizard", "Fogo")
        self.tipo = "Fogo"
        self.FORTE1 = "Grama"
        self.FRACO1 = "Agua"
        self.FRACO2 = "Fogo"

class PokemonGelo(Pokemons):
    def __init__(self, nome):
        super().__init__("Jynx", "Gelo")
        self.tipo = "Gelo"
        self.FORTE1 = "Grama"
        self.FRACO1 = "Fogo"
        self.FRACO2 = "Agua"
