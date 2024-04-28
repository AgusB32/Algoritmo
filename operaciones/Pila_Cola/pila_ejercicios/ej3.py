from pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

for i in range(10):
    pila.push(randint(1, 99))

elemento_a_reemplazar = input ("Ingrese el numero que desea reemplazar: ")
nuevo_elemento = input("Ingrese el numero que desea ingresar: ")

while pila.size() > 0:
    data = pila.pop()
    if data == elemento_a_reemplazar:
        pila_aux.push(nuevo_elemento)
    else:
        pila_aux.push(data)


while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print("Pila original con ocurrencias de", elemento_a_reemplazar, "reemplazadas por", nuevo_elemento)
while pila.size() > 0:
    print(pila.pop())