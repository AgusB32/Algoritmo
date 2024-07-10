# 4) Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
from pila import Stack
from cola import Queue
from random import randint

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

cola_numeros = Queue()

for _ in range(10):
    num = randint(1, 50)
    cola_numeros.arrive(num)

print("\n\nCola de números aleatorios:")
for _ in range(cola_numeros.size()):
    print(cola_numeros.on_front(), end=" ")
    cola_numeros.move_to_end()

cola_primos = Queue()

size = cola_numeros.size()
for _ in range(size):
    num = cola_numeros.attention()
    if es_primo(num):
        cola_primos.arrive(num)

print("\n\nCola de números primos:")
for _ in range(cola_primos.size()):
    print(cola_primos.on_front(), end=" ")
    cola_primos.move_to_end()