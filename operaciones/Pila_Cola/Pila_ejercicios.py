# Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de 
# “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un 
# algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes
# que aparecen en ambos episodios.

from pila import Stack

pila_aux = Stack()
epV = Stack()
epVII = Stack()

while epV.size > 0:
    if epV.on_top() == 


epV = ['Lobot','Han Solo','Bossk','Dengar','Chewbacca']
epVII = ['Kylo Ren','Luke Skywalker', 'Han Solo','Chewbacca','BB-8']