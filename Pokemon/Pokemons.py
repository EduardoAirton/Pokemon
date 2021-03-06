from Main import Pokemons

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
