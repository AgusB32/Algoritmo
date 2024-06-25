# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def contador(num):
    if num == 0:
        return 0
    else:
        return 1 + contador(num // 10)

num = int(input("Ingrese el numero al que le desee contar los digitos: "))
res = contador(num)
print(f"La cantidad de digitos que tiene {num} son: {res}")