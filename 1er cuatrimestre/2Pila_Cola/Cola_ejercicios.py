# 1) Eliminar de una cola de caracteres todas las vocales que aparecen.
from cola import Queue
from pila import Stack
from random import randint

cola_char = Queue()

for _ in range(10):
    letra = chr(randint(65, 90))
    cola_char.arrive(letra)

print("Cola original:")
for _ in range(cola_char.size()):
    print(cola_char.on_front(), end=" ")
    cola_char.move_to_end()

print("\n\nCola sin vocales:")
vocales = ['A', 'E', 'I', 'O', 'U']
size = cola_char.size()
for _ in range(size):
    if cola_char.on_front() in vocales:
        cola_char.attention() 
    else:
        cola_char.move_to_end()

for _ in range(cola_char.size()):
    print(cola_char.on_front(), end=" ")
    cola_char.move_to_end()




# 2) Utilizando operaciones de cola y pila, invertir el contenido de una cola.
from pila import Stack
from cola import Queue
from random import randint

cola = Queue()
cola_aux = Stack()

for i in range (7):
    letra = chr(randint(65, 90))
    cola.arrive(letra)

print("Cola original: ")
for i in range(cola.size()):
    print(cola.on_front(), end= " ")
    cola.move_to_end()

while cola.size() > 0:
    cola_aux.push(cola.attention())

print("\n\nCola invertida: ")
while cola_aux.size() > 0:
    print(cola_aux.pop(), end= " ")




# 3) Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.
from pila import Stack
from cola import Queue

def es_palindromo(secuencia):
    cola = Queue()
    pila = Stack()

    for char in secuencia:
        char = char.upper()
        if char.isalpha():
            cola.arrive(char)
            pila.push(char)

    while cola.size() > 0 and pila.size() > 0:
        if cola.attention() != pila.pop():
            return False

    return True 

secuencia = "Anita lava la tina"
print(f"La secuencia {secuencia} es: {es_palindromo(secuencia)}")




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