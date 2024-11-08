# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 

# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda 
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera
# sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla;

# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

pokemons = [
    {'numero': 1, 'nombre': 'Bulbasaur', 'tipo': ['Planta', 'Veneno'], 'nivel': 5},
    {'numero': 4, 'nombre': 'Charmander', 'tipo': ['Fuego'], 'nivel': 10},
    {'numero': 7, 'nombre': 'Squirtle', 'tipo': ['Agua'], 'nivel': 15},
    {'numero': 25, 'nombre': 'Pikachu', 'tipo': ['Electrico'], 'nivel': 20},
    {'numero': 37, 'nombre': 'Vulpix', 'tipo': ['Fuego'], 'nivel': 25},
    {'numero': 143, 'nombre': 'Snorlax', 'tipo': ['Normal'], 'nivel': 30},
    {'numero': 199, 'nombre': 'Slowking', 'tipo': ['Agua', 'Psiquico'], 'nivel': 35},
    {'numero': 1009, 'nombre': 'Mew', 'tipo': ['Psiquico'], 'nivel': 100}
]

def hash_tipo(pokemon):
    return pokemon['tipo']
def hash_numero(pokemon):
    return str(pokemon['numero'])[-1]
def hash_nivel(pokemon):
    return pokemon['nivel']

tabla_tipo = {}
tabla_numero = {}
tabla_nivel = {}

def agregar_pokemon(pokemon):
    for tipo in pokemon['tipo']:
        if tipo not in tabla_tipo:
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon)

    clave_numero = hash_numero(pokemon)
    if clave_numero not in tabla_numero:
        tabla_numero[clave_numero] = []
    tabla_numero[clave_numero].append(pokemon)

    clave_nivel = hash_nivel(pokemon)
    if clave_nivel not in tabla_nivel:
        tabla_nivel[clave_nivel] = []
    tabla_nivel[clave_nivel].append(pokemon)

# e - mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
def mostrarpokemonesnumero():
    for numero in tabla_numero:
        if numero == '3' or numero == '7' or numero == '9':
            pokemones = tabla_numero[numero]
            print(f"Pokémones que terminan en {numero}:")
            for pokemon in pokemones:
                print(pokemon)
            print()

# f - mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
def mostrarpokemonesnivel():
    print(f"Pokémones con niveles múltiplos de 2, 5 y 10:")
    print("")
    for nivel in tabla_nivel:
        if nivel % 2 == 0 and nivel % 5 == 0 and nivel % 10 == 0:
            pokemones = tabla_nivel[nivel]
            for pokemon in pokemones:
                print(pokemon)
            print()

# g - mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo
def mostrarpokemonestipo(tiposinteres):
    for tipo in tiposinteres:
        if tipo in tabla_tipo:
            pokemones = tabla_tipo[tipo]
            if pokemones:
                print(f'Pokémons de tipo: {tipo}:')
                for pokemon in pokemones:
                    print(pokemon)
                print()    
            else:
                print(f"No se encontraron Pokémones del tipo {tipo}")

for pokemon in pokemons:
    agregar_pokemon(pokemon)

print("")
print("---------------------------------------------------")
mostrarpokemonesnumero()
print("")
print("---------------------------------------------------")
mostrarpokemonesnivel()
print("")
print("---------------------------------------------------")
lista = ['Acero', 'Fuego', 'Electrico', 'Hielo']
mostrarpokemonestipo(lista)



#=====================================Ejercicio comentado==================================================================================



# Lista de Pokémones con datos predefinidos
pokemons = [
    {'numero': 1, 'nombre': 'Bulbasaur', 'tipo': ['Planta', 'Veneno'], 'nivel': 5},
    {'numero': 4, 'nombre': 'Charmander', 'tipo': ['Fuego'], 'nivel': 10},
    {'numero': 7, 'nombre': 'Squirtle', 'tipo': ['Agua'], 'nivel': 15},
    {'numero': 25, 'nombre': 'Pikachu', 'tipo': ['Electrico'], 'nivel': 20},
    {'numero': 37, 'nombre': 'Vulpix', 'tipo': ['Fuego'], 'nivel': 25},
    {'numero': 143, 'nombre': 'Snorlax', 'tipo': ['Normal'], 'nivel': 30},
    {'numero': 199, 'nombre': 'Slowking', 'tipo': ['Agua', 'Psiquico'], 'nivel': 35},
    {'numero': 1009, 'nombre': 'Mew', 'tipo': ['Psiquico'], 'nivel': 100}
]

# Función hash para clasificar por tipo de Pokémon
def hash_tipo(pokemon):
    return pokemon['tipo']

# Función hash para clasificar por el último dígito del número del Pokémon
def hash_numero(pokemon):
    return str(pokemon['numero'])[-1]

# Función hash para clasificar por nivel de Pokémon
def hash_nivel(pokemon):
    return pokemon['nivel']

# Estructuras de tabla hash para cada criterio de clasificación
tabla_tipo = {}
tabla_numero = {}
tabla_nivel = {}

# Función para agregar un Pokémon a las tres tablas hash
def agregar_pokemon(pokemon):
    # Cargar en tabla de tipos (maneja múltiples tipos)
    for tipo in pokemon['tipo']:
        if tipo not in tabla_tipo:
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon)

    # Cargar en tabla de números (último dígito del número)
    clave_numero = hash_numero(pokemon)
    if clave_numero not in tabla_numero:
        tabla_numero[clave_numero] = []
    tabla_numero[clave_numero].append(pokemon)

    # Cargar en tabla de niveles
    clave_nivel = hash_nivel(pokemon)
    if clave_nivel not in tabla_nivel:
        tabla_nivel[clave_nivel] = []
    tabla_nivel[clave_nivel].append(pokemon)

# e) Mostrar Pokémones cuyos números terminan en 3, 7 o 9
def mostrarpokemonesnumero():
    for numero in tabla_numero:
        if numero == '3' or numero == '7' or numero == '9':
            pokemones = tabla_numero[numero]
            print(f"Pokémones que terminan en {numero}:")
            for pokemon in pokemones:
                print(pokemon)
            print()

# f) Mostrar Pokémones con niveles múltiplos de 2, 5 y 10
def mostrarpokemonesnivel():
    print(f"Pokémones con niveles múltiplos de 2, 5 y 10:")
    for nivel in tabla_nivel:
        if nivel % 2 == 0 and nivel % 5 == 0 and nivel % 10 == 0:
            pokemones = tabla_nivel[nivel]
            for pokemon in pokemones:
                print(pokemon)
            print()

# g) Mostrar Pokémones de tipos específicos (Acero, Fuego, Electrifico, Hielo)
def mostrarpokemonestipo(tiposinteres):
    for tipo in tiposinteres:
        if tipo in tabla_tipo:
            pokemones = tabla_tipo[tipo]
            if pokemones:
                print(f'Pokémons de tipo: {tipo}:')
                for pokemon in pokemones:
                    print(pokemon)
                print()    
            else:
                print(f"No se encontraron Pokémones del tipo {tipo}")

# Cargar todos los Pokémones en las tablas hash
for pokemon in pokemons:
    agregar_pokemon(pokemon)

# Ejecución de las funciones de muestra
print("---------------------------------------------------")
mostrarpokemonesnumero()
print("---------------------------------------------------")
mostrarpokemonesnivel()
print("---------------------------------------------------")
lista = ['Acero', 'Fuego', 'Electrico', 'Hielo']
mostrarpokemonestipo(lista)