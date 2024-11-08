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



#=====================================Ejercicio comentado==================================================================================



from lista import search
from lista import remove

# Definición de la lista de superhéroes, cada uno es un diccionario con su información relevante
super_heroes = [
    {'nombre': "Linterna Verde", "año_aparicion": 1940, "casa_comic": "DC Comics", "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."},
    ...
]

# a) Eliminar el nodo que contiene la información de "Linterna Verde"
eliminar = 'Linterna Verde'
remove(super_heroes, 'nombre', eliminar)  # Se llama a la función 'remove' para eliminar "Linterna Verde" por su nombre
print(f'Habiendo eliminado a: {eliminar}')

# b) Mostrar el año de aparición de "Wolverine"
aparicion = 1974
search(super_heroes, "año_aparicion", aparicion)  # Utiliza la función 'search' para encontrar el año de aparición
print(f'\nWolverine apareció el año: {aparicion}')

# c) Cambiar la casa de "Doctor Strange" a "Marvel"
nameDR = "Doctor Strange"
index_Dr_Strange = search(super_heroes, 'nombre', nameDR)  # Busca la posición de "Doctor Strange" en la lista
if index_Dr_Strange is not None:
    super_heroes[index_Dr_Strange]['casa_comic'] = 'Marvel'  # Cambia su casa de cómic a Marvel si se encuentra
else:
    print('Doctor Strange no se encuentra en la lista')

# d) Mostrar nombres de superhéroes cuya biografía menciona "traje" o "armadura"
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

# e) Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición es anterior a 1963
for i in super_heroes:
    if i["año_aparicion"] < 1963:
        print(f'Nombre: {i["nombre"]}, Casa: {i["casa_comic"]}')

# f) Mostrar la casa a la que pertenece "Capitana Marvel" y "Mujer Maravilla"
def busquedamar(list_values, pj1, pj2):
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
condicion1, condicion2, casaco1, casaco2 = busquedamar(super_heroes, pj1, pj2)

if condicion1 and condicion2:
    print("Mujer Maravilla está en la casa:", casaco1, "y Capitana Marvel en:", casaco2)
elif not condicion1 and not condicion2:
    print("Ninguno de los personajes está en la lista.")

# g) Mostrar toda la información de "Flash" y "Star-Lord"
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

# h) Listar los superhéroes que comienzan con la letra B, M y S
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

# i) Contar cuántos superhéroes hay de cada casa de comic
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
