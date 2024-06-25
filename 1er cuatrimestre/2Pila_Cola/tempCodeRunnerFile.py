from cola import Queue
from pila import Stack
from random import randint

cola_char = Queue()

for i in range(10):
    letra = chr(randint(65, 90))
    cola_char.arrive(letra)

for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()