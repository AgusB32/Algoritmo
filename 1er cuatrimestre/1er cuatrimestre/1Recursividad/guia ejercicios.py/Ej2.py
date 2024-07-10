# Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y
# un número entero positivo dado.
def suma(n):
    if n < 0:
        raise ValueError("El argumento debe ser no negativo")
    if n <= 1:
        return n
    else:
        return suma(n-1)+n
n = int(input('Ingrese un numero a ser sumado por todos los enteros anteriores: '))
res = suma(n)
print(f'El resultado de las sumas es: {res}')