# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 
# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

class Pokemon:
    def __init__(self, number, name, types, level):
        self.number = number
        self.name = name
        self.types = types
        self.level = level

    def __repr__(self):
        return f"{self.number} - {self.name} ({', '.join(self.types)}), Nivel: {self.level}"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        elif isinstance(key, int):
            return key % self.size

    def insert(self, key, value):
        hash_index = self.hash_function(key)
        self.table[hash_index].append(value)

    def get_items(self):
        items = []
        for bucket in self.table:
            items.extend(bucket)
        return items

size = 10
hash_table_type = HashTable(size)
hash_table_number = HashTable(size)
hash_table_level = HashTable(size)

def add_pokemon(pokemon):
    for type in pokemon.types:
        hash_table_type.insert(type, pokemon)

    hash_table_number.insert(pokemon.number % 10, pokemon)

    hash_table_level.insert(pokemon.level % 10, pokemon)

def show_pokemons_by_last_digit(digits):
    pokemons = []
    for digit in digits:
        pokemons.extend(hash_table_number.table[digit])
    return pokemons

def show_pokemons_by_level_multiples(multiples):
    pokemons = []
    for i in range(size):
        if any(i % multiple == 0 for multiple in multiples):
            pokemons.extend(hash_table_level.table[i])
    return pokemons

def show_pokemons_by_types(types):
    pokemons = []
    for type in types:
        index = hash_table_type.hash_function(type)
        if index < len(hash_table_type.table):
            pokemons.extend(hash_table_type.table[index])
    return pokemons

pokemons = [
    Pokemon(25, "Pikachu", ["Eléctrico"], 35),
    Pokemon(6, "Charizard", ["Fuego", "Volador"], 40),
    Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], 30),
    Pokemon(121, "Starmie", ["Agua", "Psíquico"], 30),
    Pokemon(54, "Psyduck", ["Agua"], 25),
    Pokemon(130, "Gyarados", ["Agua", "Volador"], 35),
    Pokemon(95, "Onix", ["Roca", "Tierra"], 38),
    Pokemon(74, "Geodude", ["Roca", "Tierra"], 28),
    Pokemon(37, "Vulpix", ["Fuego"], 20),
    Pokemon(9, "Blastoise", ["Agua"], 50),
    Pokemon(197, "Umbreon", ["Siniestro"], 45),
    Pokemon(34, "Nidoking", ["Veneno", "Tierra"], 40)
]

for pokemon in pokemons:
    add_pokemon(pokemon)

print("Pokémons cuyos números terminan en 3, 7 y 9:")
for pokemon in show_pokemons_by_last_digit([3, 7, 9]):
    print(pokemon)

print("\nPokémons cuyos niveles son múltiplos de 2, 5 y 10:")
for pokemon in show_pokemons_by_level_multiples([2, 5, 10]):
    print(pokemon)

print("\nPokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
for pokemon in show_pokemons_by_types(["Acero", "Fuego", "Eléctrico", "Hielo"]):
    print(pokemon)