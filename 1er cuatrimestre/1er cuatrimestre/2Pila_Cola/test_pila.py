#Eliminar de una pila todos los elementos impares, es decir
#que en la misma solo queden números pares.
from pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

for i in range(10):
    pila.push(randint(1, 99))

print("Contenido original de la pila:")
while pila.size() > 0:
    data = pila.pop()
    print(data, end=" ")        # el end=" " sirve para que la pila se muestre de forma horizontal
    if data % 2 == 0:
        pila_aux.push(data)

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print("\n\nContenido de la pila solo con números pares:") #aplico \n\n para dar dos "enters" al momento de printear
while pila.size() > 0:
    print(pila.pop(), end=" ")
print()