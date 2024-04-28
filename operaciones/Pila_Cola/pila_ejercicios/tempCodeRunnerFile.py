from pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

for i in range(3):
    num =randint(1,99)
    print(num)
    pila.push(num)

a = input("ingrese el numero a reemplazar")
b = input("ingrese el numero que desea ingresar")

while pila.size() > 0:
    data = pila.pop()
    if data == a:
        pila_aux.push(b)
    else:
        pila_aux.push(data)


while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

# Muestra la pila
print("Contenido de la pila después del reemplazo:")
while pila.size() > 0:
    print(pila.pop())