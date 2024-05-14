# 16) Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de 
#     “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un 
#     algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes
#     que aparecen en ambos episodios.

from pila import Stack

pila_aux = Stack()
epV = Stack()
epVII = Stack()

while epV.size > 0:
    if epV.on_top() == 


epV = ['Lobot','Han Solo','Bossk','Dengar','Chewbacca']
epVII = ['Kylo Ren','Luke Skywalker', 'Han Solo','Chewbacca','BB-8']






# 24) Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#     su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#     necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición 
# uno la cima de la pila.

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece.

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow).

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.