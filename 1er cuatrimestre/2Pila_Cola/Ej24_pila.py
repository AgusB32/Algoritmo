# 24) Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#     su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#     necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición 
# uno la cima de la pila.

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece.

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow).

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from pila import Stack

def encontrar_posicion(pila, nombre):
    temp_pila = Stack()
    posicion = 1
    encontrado = False

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['nombre'] == nombre:
            encontrado = True
            break
        posicion += 1

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return posicion if encontrado else None

def personajes_mas_de_5_peliculas(pila):
    temp_pila = Stack()
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['peliculas'] > 5:
            personajes.append(personaje)

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return personajes

def peliculas_black_widow(pila):
    temp_pila = Stack()
    peliculas = 0

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['nombre'] == 'Black Widow':
            peliculas = personaje['peliculas']
            break

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return peliculas

def personajes_nombres_CDG(pila):
    temp_pila = Stack()
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['nombre'][0] in ['C', 'D', 'G']:
            personajes.append(personaje)

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return personajes

pila_personajes = Stack()

personajes_mcu = [
    {'nombre': 'Captain America', 'peliculas': 9},
    {'nombre': 'Iron Man', 'peliculas': 10},
    {'nombre': 'Black Widow', 'peliculas': 8},
    {'nombre': 'Spider-Man', 'peliculas': 5},
    {'nombre': 'Thor', 'peliculas': 7},
    {'nombre': 'Hawkeye', 'peliculas': 5},
    {'nombre': 'Doctor Strange', 'peliculas': 3},
    {'nombre': 'Groot', 'peliculas': 4},
    {'nombre': 'Rocket Raccoon', 'peliculas': 4},
    {'nombre': 'Hulk', 'peliculas': 6},
]

for personaje in personajes_mcu:
    pila_personajes.push(personaje)

# a.
pos_rocket = encontrar_posicion(pila_personajes, 'Rocket Raccoon')
pos_groot = encontrar_posicion(pila_personajes, 'Groot')

print(f"Posición de Rocket Raccoon: {pos_rocket}")
print(f"Posición de Groot: {pos_groot}")

# b.
mas_de_5_peliculas = personajes_mas_de_5_peliculas(pila_personajes)
print("Personajes que participaron en más de 5 películas:")
for personaje in mas_de_5_peliculas:
    print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas")

# c.
peliculas_bw = peliculas_black_widow(pila_personajes)
print(f"Black Widow participó en {peliculas_bw} películas")

# d.
personajes_cdg = personajes_nombres_CDG(pila_personajes)
print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes_cdg:
    print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas")



#=====================================Ejercicio comentado==================================================================================



from pila import Stack  # Importamos la estructura de pila desde el módulo `pila`

# Función para encontrar la posición de un personaje dado en la pila
def encontrar_posicion(pila, nombre):
    temp_pila = Stack()  # Pila temporal para restaurar la pila original
    posicion = 1  # Contador de la posición en la pila, iniciando en la cima
    encontrado = False  # Bandera para indicar si se encontró el personaje

    # Desapilamos cada elemento hasta encontrar el personaje o vaciar la pila
    while pila.size() > 0:
        personaje = pila.pop()  # Extraemos un personaje
        temp_pila.push(personaje)  # Lo guardamos en la pila temporal para restaurar luego

        # Si el personaje es el que buscamos, marcamos que fue encontrado
        if personaje['nombre'] == nombre:
            encontrado = True
            break
        posicion += 1  # Incrementamos la posición si no es el personaje buscado

    # Restauramos la pila original pasando los elementos de la pila temporal
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    # Retornamos la posición si se encontró; de lo contrario, retornamos None
    return posicion if encontrado else None

# Función para obtener los personajes que participaron en más de 5 películas
def personajes_mas_de_5_peliculas(pila):
    temp_pila = Stack()  # Pila temporal para restaurar `pila`
    personajes = []  # Lista para almacenar los personajes que cumplen la condición

    # Desapilamos cada personaje de la pila
    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)  # Guardamos el personaje en la pila temporal

        # Verificamos si el personaje participó en más de 5 películas
        if personaje['peliculas'] > 5:
            personajes.append(personaje)  # Lo agregamos a la lista si cumple la condición

    # Restauramos la pila original pasando los elementos de la pila temporal
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return personajes  # Retornamos la lista de personajes que cumplen la condición

# Función para encontrar la cantidad de películas en las que participó Black Widow
def peliculas_black_widow(pila):
    temp_pila = Stack()  # Pila temporal para restaurar `pila`
    peliculas = 0  # Variable para almacenar la cantidad de películas

    # Desapilamos cada personaje de la pila
    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)  # Guardamos el personaje en la pila temporal

        # Verificamos si el personaje es Black Widow
        if personaje['nombre'] == 'Black Widow':
            peliculas = personaje['peliculas']  # Asignamos la cantidad de películas
            break  # Salimos del bucle si encontramos el personaje

    # Restauramos la pila original pasando los elementos de la pila temporal
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return peliculas  # Retornamos la cantidad de películas de Black Widow

# Función para obtener los personajes cuyos nombres empiezan con C, D o G
def personajes_nombres_CDG(pila):
    temp_pila = Stack()  # Pila temporal para restaurar `pila`
    personajes = []  # Lista para almacenar los personajes que cumplen la condición

    # Desapilamos cada personaje de la pila
    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)  # Guardamos el personaje en la pila temporal

        # Verificamos si el nombre del personaje empieza con C, D o G
        if personaje['nombre'][0] in ['C', 'D', 'G']:
            personajes.append(personaje)  # Lo agregamos a la lista si cumple la condición

    # Restauramos la pila original pasando los elementos de la pila temporal
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return personajes  # Retornamos la lista de personajes que cumplen la condición

# Creamos la pila `pila_personajes` para almacenar los personajes de MCU
pila_personajes = Stack()

# Lista de diccionarios con los personajes y su cantidad de películas
personajes_mcu = [
    {'nombre': 'Captain America', 'peliculas': 9},
    {'nombre': 'Iron Man', 'peliculas': 10},
    {'nombre': 'Black Widow', 'peliculas': 8},
    {'nombre': 'Spider-Man', 'peliculas': 5},
    {'nombre': 'Thor', 'peliculas': 7},
    {'nombre': 'Hawkeye', 'peliculas': 5},
    {'nombre': 'Doctor Strange', 'peliculas': 3},
    {'nombre': 'Groot', 'peliculas': 4},
    {'nombre': 'Rocket Raccoon', 'peliculas': 4},
    {'nombre': 'Hulk', 'peliculas': 6},
]

# Apilamos cada personaje en `pila_personajes`
for personaje in personajes_mcu:
    pila_personajes.push(personaje)

# a. Encontramos la posición de Rocket Raccoon y Groot en la pila
pos_rocket = encontrar_posicion(pila_personajes, 'Rocket Raccoon')
pos_groot = encontrar_posicion(pila_personajes, 'Groot')
print(f"Posición de Rocket Raccoon: {pos_rocket}")
print(f"Posición de Groot: {pos_groot}")

# b. Obtenemos los personajes que participaron en más de 5 películas
mas_de_5_peliculas = personajes_mas_de_5_peliculas(pila_personajes)
print("Personajes que participaron en más de 5 películas:")
for personaje in mas_de_5_peliculas:
    print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas")

# c. Obtenemos la cantidad de películas en las que participó Black Widow
peliculas_bw = peliculas_black_widow(pila_personajes)
print(f"Black Widow participó en {peliculas_bw} películas")

# d. Obtenemos los personajes cuyos nombres empiezan con C, D o G
personajes_cdg = personajes_nombres_CDG(pila_personajes)
print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes_cdg:
    print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas")
