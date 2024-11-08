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



#Ejercicio comentado


from pila import Stack  # Importamos la estructura de pila desde el módulo `pila`

# Creamos las pilas necesarias
pila_aux = Stack()  # Pila auxiliar para restaurar la pila original `epV` después de la operación
epV = Stack()       # Pila que contiene los personajes del Episodio V
epVII = Stack()     # Pila que contiene los personajes del Episodio VII
interseccion = Stack()  # Pila para almacenar los personajes en común

# Agregamos personajes a la pila `epV` (personajes del Episodio V)
for personaje in ['Lobot','Han Solo','Bossk','Dengar','Chewbacca']:
    epV.push(personaje)

# Agregamos personajes a la pila `epVII` (personajes del Episodio VII)
for personaje in ['Kylo Ren','Luke Skywalker', 'Han Solo','Chewbacca','BB-8']:
    epVII.push(personaje)

# Empezamos a buscar la intersección
while epV.size() > 0:  # Mientras haya personajes en `epV`
    personaje_epV = epV.pop()  # Sacamos el personaje de `epV`
    pila_aux.push(personaje_epV)  # Lo guardamos en `pila_aux` para luego restaurarlo en `epV`
    aux_epVII = Stack()  # Pila auxiliar para restaurar `epVII` después de la operación

    while epVII.size() > 0:  # Iteramos sobre los personajes de `epVII`
        personaje_epVII = epVII.pop()  # Extraemos un personaje de `epVII`
        
        # Comparamos el personaje extraído de `epVII` con el personaje actual de `epV`
        if personaje_epVII == personaje_epV:
            interseccion.push(personaje_epVII)  # Si coinciden, lo agregamos a `interseccion`
        
        aux_epVII.push(personaje_epVII)  # Guardamos el personaje en `aux_epVII` para restaurar `epVII`

    # Restauramos `epVII` trasladando los personajes de `aux_epVII` de regreso a `epVII`
    while aux_epVII.size() > 0:
        epVII.push(aux_epVII.pop())

# Restauramos `epV` trasladando los personajes de `pila_aux` de regreso a `epV`
while pila_aux.size() > 0:
    epV.push(pila_aux.pop())

# Imprimimos los personajes que están en la pila `interseccion`
print("Los personajes que aparecen en ambos episodios son:")
while interseccion.size() > 0:
    print(interseccion.pop())  # Extraemos e imprimimos cada personaje de `interseccion`
