# Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def conversor(num):
    if num == 1:
        return str(1)
    else:
        return conversor(num//2) + str(num % 2)
    
num = int(input("Ingrse un numero que desee pasarlo a binario: "))
res = conversor(num)
print(f"{num} a binario es {res}")