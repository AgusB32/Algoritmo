# 16) Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de 
#     “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un 
#     algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes
#     que aparecen en ambos episodios.

from pila import Stack

pila_aux = Stack()
epV = Stack()
epVII = Stack()
interseccion = Stack()

for personaje in ['Lobot','Han Solo','Bossk','Dengar','Chewbacca']:
    epV.push(personaje)

for personaje in ['Kylo Ren','Luke Skywalker', 'Han Solo','Chewbacca','BB-8']:
    epVII.push(personaje)

while epV.size() > 0:
    personaje_epV = epV.pop()
    pila_aux.push(personaje_epV)
    aux_epVII = Stack()

    while epVII.size() > 0:
        personaje_epVII = epVII.pop()
        if personaje_epVII == personaje_epV:
            interseccion.push(personaje_epVII)
        aux_epVII.push(personaje_epVII)

    while aux_epVII.size() > 0:
        epVII.push(aux_epVII.pop())

while pila_aux.size() > 0:
    epV.push(pila_aux.pop())

print("Los personajes que aparecen en ambos episodios son:")
while interseccion.size() > 0:
    print(interseccion.pop())


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