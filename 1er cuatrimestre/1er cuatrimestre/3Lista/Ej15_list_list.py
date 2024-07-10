# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from lista import search

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120,
        "pokemons": [
            {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "pokemons": [
            {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None}
        ]
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100,
        "pokemons": [
            {"nombre": "Charizard", "nivel": 50, "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Dragapult", "nivel": 60, "tipo": "Dragón", "subtipo": "Fantasma"}
        ]
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30,
        "pokemons": [
            {"nombre": "Eevee", "nivel": 20, "tipo": "Normal", "subtipo": None},
            {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None}
        ]
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60,
        "pokemons": [
            {"nombre": "Duraludon", "nivel": 50, "tipo": "Acero", "subtipo": "Dragón"},
            {"nombre": "Flygon", "nivel": 45, "tipo": "Dragón", "subtipo": "Tierra"}
        ]
    }
]

pokemons = [
    {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Pikachu", "nivel": 20, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
    {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
    {"nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico"},
    {"nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None},
    {"nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
    {"nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None},
    {"nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None},
    {"nombre": "Umbreon", "nivel": 45, "tipo": "Siniestro", "subtipo": None},
    {"nombre": "Nidoking", "nivel": 40, "tipo": "Veneno", "subtipo": "Tierra"},
    {"nombre": "Dragonite", "nivel": 55, "tipo": "Dragón", "subtipo": "Volador"},
    {"nombre": "Aerodactyl", "nivel": 52, "tipo": "Roca", "subtipo": "Volador"}
]

# a)
nombre_entrenador = "Ash Ketchum"
def cantidad_pokemons(entrenadores, nombre_entrenador):
    index = search(entrenadores, 'nombre', nombre_entrenador)
    if index is not None:
        return len(entrenadores[index]['pokemons'])
    return 0

print(f"{nombre_entrenador} tiene {cantidad_pokemons(entrenadores, nombre_entrenador)} Pokémons.")

print(" ")

# b)
def entrenadores_con_mas_de_tres_torneos(entrenadores):
    return [entrenador['nombre'] for entrenador in entrenadores if entrenador['torneos_ganados'] > 3]

print("Entrenadores que han ganado más de tres torneos:", entrenadores_con_mas_de_tres_torneos(entrenadores))

print(" ")

# c) 
def obtener_mejor_entrenador(entrenadores):
    def torneos_ganados(entrenador):
        return entrenador['torneos_ganados']
    
    mejor_entrenador = max(entrenadores, key=torneos_ganados)
    return mejor_entrenador

def obtener_mejor_pokemon(pokemons):
    def nivel_pokemon(pokemon):
        return pokemon['nivel']
    
    mejor_pokemon = max(pokemons, key=nivel_pokemon)
    return mejor_pokemon

def pokemon_mayor_nivel_del_mejor_entrenador(entrenadores):
    mejor_entrenador = obtener_mejor_entrenador(entrenadores)
    mejor_pokemon = obtener_mejor_pokemon(mejor_entrenador['pokemons'])
    return mejor_pokemon

mejor_pokemon = pokemon_mayor_nivel_del_mejor_entrenador(entrenadores)
print(f"El Pokémon de mayor nivel del mejor entrenador es: {mejor_pokemon['nombre']} con nivel {mejor_pokemon['nivel']}")

print(" ")

# d) 
def mostrar_datos_entrenador(entrenadores, nombre_entrenador):
    index = search(entrenadores, 'nombre', nombre_entrenador)
    if index is not None:
        entrenador = entrenadores[index]
        print(f"Entrenador: {entrenador['nombre']}")
        print(f"Torneos ganados: {entrenador['torneos_ganados']}")
        print(f"Batallas perdidas: {entrenador['batallas_perdidas']}")
        print(f"Batallas ganadas: {entrenador['batallas_ganadas']}")
        print("Pokémons:")
        for pokemon in entrenador['pokemons']:
            print(f"  Nombre: {pokemon['nombre']}, Nivel: {pokemon['nivel']}, Tipo: {pokemon['tipo']}, Subtipo: {pokemon['subtipo']}")
    else:
        print(f"Entrenador {nombre_entrenador} no encontrado.")

nombre_entrenador = "Ash Ketchum"
mostrar_datos_entrenador(entrenadores, nombre_entrenador)

print(" ")

# e) 
def porcentaje_batallas_ganadas(entrenador):
    total_batallas = entrenador['batallas_ganadas'] + entrenador['batallas_perdidas']
    if total_batallas == 0:
        return 0
    return (entrenador['batallas_ganadas'] / total_batallas) * 100

def entrenadores_con_alto_porcentaje_victorias(entrenadores):
    return [entrenador['nombre'] for entrenador in entrenadores if porcentaje_batallas_ganadas(entrenador) > 79]

print("Entrenadores con más del 79% de batallas ganadas:", entrenadores_con_alto_porcentaje_victorias(entrenadores))

print(" ")

# f)
def entrenadores_con_tipos_especificos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        tiene_fuego_planta = False
        tiene_agua_volador = False
        for pokemon in entrenador['pokemons']:
            if (pokemon['tipo'] == 'Fuego' and pokemon['subtipo'] == 'Planta') or (pokemon['tipo'] == 'Planta' and pokemon['subtipo'] == 'Fuego'):
                tiene_fuego_planta = True
            if pokemon['tipo'] == 'Agua' and pokemon['subtipo'] == 'Volador':
                tiene_agua_volador = True
        if tiene_fuego_planta or tiene_agua_volador:
            resultado.append(entrenador['nombre'])
    if resultado:
        print("Entrenadores con Pokémon de tipo fuego/planta o agua/volador:", resultado)
    else:
        print("No hay ningún entrenador que tenga esos tipos de Pokémon")

entrenadores_con_tipos_especificos(entrenadores)

print(" ")

# g)
nombre_entrenador = "Leon"
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    index = search(entrenadores, 'nombre', nombre_entrenador)
    if index is not None:
        pokemons = entrenadores[index]['pokemons']
        total_nivel = sum(pokemon['nivel'] for pokemon in pokemons)
        cantidad_pokemons = len(pokemons)
        if cantidad_pokemons == 0:
            return 0
        return total_nivel / cantidad_pokemons
    return 0

print(f"Promedio de nivel de los Pokémons de {nombre_entrenador}: {promedio_nivel_pokemons(entrenadores, nombre_entrenador)}")

print(" ")

# h) 
def entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return len([entrenador for entrenador in entrenadores if any(pokemon['nombre'] == nombre_pokemon for pokemon in entrenador['pokemons'])])

nombre_pokemon = "Eevee"
print(f"Cantidad de entrenadores que tienen a {nombre_pokemon}: {entrenadores_con_pokemon(entrenadores, nombre_pokemon)}")

print(" ")

# i)
def entrenadores_con_pokemons_repetidos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon['nombre'] for pokemon in entrenador['pokemons']]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            resultado.append(entrenador['nombre'])
    return resultado
resultado = entrenadores_con_pokemons_repetidos(entrenadores)
if not resultado:
    print("No se encontraron entrenadores con Pokémons repetidos.")
else:
    print("Entrenadores con Pokémons repetidos:", resultado)

print(" ")

# j)
pokemons_especificos = ["Tyrantrum", "Terrakion", "Wingull"]
def entrenadores_con_pokemons_especificos(entrenadores, pokemons_especificos):
    return [entrenador['nombre'] for entrenador in entrenadores if any(pokemon['nombre'] in pokemons_especificos for pokemon in entrenador['pokemons'])]

resultado = entrenadores_con_pokemons_especificos(entrenadores, pokemons_especificos)
if not resultado:
    print("No se encontraron entrenadores con los Pokémon especificados.")
else:
    print("Entrenadores que tienen a Tyrantrum, Terrakion o Wingull:", resultado)

print(" ")

# k)
nombre_entrenador = "Raihan"
nombre_pokemon = "Flygon"

def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    index = search(entrenadores, 'nombre', nombre_entrenador)
    if index is not None:
        entrenador = entrenadores[index]
        for pokemon in entrenador['pokemons']:
            if pokemon['nombre'] == nombre_pokemon:
                print(f"Entrenador: {entrenador['nombre']}")
                print(f"Torneos ganados: {entrenador['torneos_ganados']}")
                print(f"Batallas perdidas: {entrenador['batallas_perdidas']}")
                print(f"Batallas ganadas: {entrenador['batallas_ganadas']}")
                print("Pokémons:")
                for p in entrenador['pokemons']:
                    print(f"  Nombre: {p['nombre']}, Nivel: {p['nivel']}, Tipo: {p['tipo']}, Subtipo: {p['subtipo']}")
                return True
    return False

if not entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    print(f"El entrenador {nombre_entrenador} no tiene al Pokémon {nombre_pokemon}.")
