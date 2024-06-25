# 6) Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#    casa de comic a la que pertenece (Marvel o DC) y biografía, implementar las funciones necesa-
#    rias para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from lista import search
from lista import remove

super_heroes = [
    {'nombre': "Linterna Verde", "año_aparicion": 1940, "casa_comic": "DC Comics", "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."},
    {'nombre': "Wolverine","año_aparicion": 1974,"casa_comic": "Marvel Comics","biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."},
    {'nombre': "Doctor Strange","año_aparicion": 1963,"casa_comic": "Marvel Comics","biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."},
    {'nombre': "Capitana Marvel","año_aparicion": 1968,"casa_comic": "Marvel Comics","biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."},
    {'nombre': "Mujer Maravilla","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."},
    {'nombre': "Flash","año_aparicion": 1940,"casa_comic": "DC Comics","biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."},
    {'nombre': "Star-Lord","año_aparicion": 1976,"casa_comic": "Marvel Comics","biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."},
    {'nombre': "Superman","año_aparicion": 1938,"casa_comic": "DC Comics","biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."},
    {'nombre': "Batman","año_aparicion": 1939,"casa_comic": "DC Comics","biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."},
    {'nombre': "Iron Man","año_aparicion": 1963,"casa_comic": "Marvel Comics","biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."},
    {'nombre': "Wonder Woman","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."},
    {'nombre': "Spider-Man","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."},
    {'nombre': "Thor","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."},
    {'nombre': "Aquaman","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."},
    {'nombre': "Green Arrow","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."},
    {'nombre': "Hulk","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."},
    {'nombre': "Black Widow","año_aparicion": 1964,"casa_comic": "Marvel Comics","biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."},
    {'nombre': "Mr. Fantástico","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."},
    {'nombre': "La Mujer Invisible","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."},
    {'nombre': "La Antorcha Humana","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."},
    {'nombre': "La Cosa","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."},
    {'nombre': "Capitán América","año_aparicion": 1941,"casa_comic": "Marvel Comics","biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."},
    {'nombre': "Ant-Man","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."}
]

# a)
eliminar = 'Linterna Verde'
remove(super_heroes, 'nombre', eliminar)
print(f'Habiendo eliminado a: {eliminar}')
# print(super_heroes)

# b)
aparicion = 1974
search(super_heroes, "año_aparicion", aparicion)
print(f'\nWolverine aparecio el año: {aparicion}')

# c) 
nameDR = "Doctor Strange"
index_Dr_Strange = search(super_heroes,'nombre', nameDR )
if index_Dr_Strange is not None:
    super_heroes[index_Dr_Strange]['casa_comic'] = 'Marvel'
else:
    print('Doctor Strange no se encuentra en la lista')

# d) 
def find_superheroes(list_values, keywords):
    heroes_with_keywords = []
    for hero in list_values:
        for i in keywords:
            if i in hero['biografia'].lower():
                heroes_with_keywords.append(hero['nombre'])
                break
    return heroes_with_keywords

keywords = ["traje", "armadura"]
heroes = find_superheroes(super_heroes, keywords)
print("\nSuperhéroes que mencionan 'traje' o 'armadura' en su biografía:")
for i in heroes:
    print(i)

print("")

# e)
for i in super_heroes:
    if i ["año_aparicion"] < 1963:
        print(f'Nombre: {i["nombre"]}, Casa: {i["casa_comic"]}')

# f) 

print("")

def busquedamar(list_values,pj1,pj2):
    pjcondicion1 = False
    pjcondicion2 = False
    casacomic1 = None
    casacomic2 = None
    for i in list_values:
        if 'nombre' in i:
            if i['nombre'] == pj1:
                pjcondicion1 = True
                casacomic1 = i['casa_comic']
            elif i['nombre'] == pj2:
                pjcondicion2 = True
                casacomic2 = i['casa_comic']
    return pjcondicion1, pjcondicion2, casacomic1, casacomic2

pj1 = "Mujer Maravilla"
pj2 = "Capitana Marvel"

condicion1, condicion2, casaco1, casaco2 = busquedamar(super_heroes,pj1,pj2)

if condicion1 == True and condicion2 == True:
    print("Mujer Maravilla esta en la casa: ",casaco1, " y Capitana Marvel en: " ,casaco2)
elif condicion1 == False and condicion2 == False:
        print("Ninguno de los personajes esta en la lista.")

print("")

# g)
def info_heroes_solicitados(heroe):
    print(f"Nombre: {heroe['nombre']}")
    print(f"Año de aparición: {heroe['año_aparicion']}")
    print(f"Casa de comic: {heroe['casa_comic']}")
    print(f"Biografía: {heroe['biografia']}")
    print()

heroes_to_find = ["Flash", "Star-Lord"]

for i in heroes_to_find:
    index = search(super_heroes, "nombre", i)
    if index is not None:
        info_heroes_solicitados(super_heroes[index])
    else:
        print(f"{i} no se encuentra en la lista.")

# h) listar los superhéroes que comienzan con la letra B, M y S;
def listar_superheroes_por_letra(super_heroes, letras):
    resultado = {letra: [] for letra in letras}
    for heroe in super_heroes:
        inicial = heroe['nombre'][0].upper()
        if inicial in letras:
            resultado[inicial].append(heroe['nombre'])
    return resultado

letras = ['B', 'M', 'S']
superheroes_por_letra = listar_superheroes_por_letra(super_heroes, letras)
print(superheroes_por_letra)


# i) determinar cuántos superhéroes hay de cada casa de comic.
def contar_superheroes_por_casa(super_heroes):
    conteo = {}
    for heroe in super_heroes:
        casa = heroe['casa_comic']
        if casa in conteo:
            conteo[casa] += 1
        else:
            conteo[casa] = 1
    return conteo

conteo_superheroes = contar_superheroes_por_casa(super_heroes)
print(conteo_superheroes)




# 15)
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