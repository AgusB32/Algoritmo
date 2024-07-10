# Implementar una función para calcular el producto de dos números enteros dados.
def prod(n1,n2):
    if n1 == 1:
        return n2

    elif n2 == 1:
        return n1

    elif n1 == 0 or n2 == 0:
        return 0

    else:
        return prod(n1,n2-1) + n1

n1 = int(input('Ingrese el primero numero que desea multiplicar: '))
n2 = int(input('Ingrese el segundo numero que desea multiplicar: '))
res = prod(n1,n2)
print(f"El resultado de la multiplicacion es: {res}")