# 1) Eliminar de una cola de caracteres todas las vocales que aparecen.
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

print()
vocales = ['A', 'E', 'I', 'O', 'U']

for i in range(cola_char.size()):
    if cola_char.on_front() in vocales:
        cola_char.attention()
    else:
        cola_char.move_to_end()

for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()


# 2) Utilizando operaciones de cola y pila, invertir el contenido de una cola.
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

for i in range(cola_char.size()):
    if cola_char.onfront():
        


# 3) Dada una secuencia de caracteres utilizando operaciones de cola y pila
# determinar si es un palíndromo.






# 4) Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

