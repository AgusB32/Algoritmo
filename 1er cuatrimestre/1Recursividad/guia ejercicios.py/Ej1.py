# Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num = int(input("Ingrese el valor que desea ser trabajado por Fibonacci: "))
res = fibonacci(num)
print(f"El resultado del valor trabajado por Fibonazi es: {res}")