# Implementar una función para calcular la potencia, dado dos números enteros, el primero representa
# la base y segundo el exponente.

def pot(n1,n2):
    if n2 == 0:
        return 1
    
    else:
        return n1 * pot(n1,n2-1)

n1 = int(input('Ingrese la base de su potencia: '))
n2 = int(input('Ingrese el exponente de su potencia: '))
res = pot(n1,n2)
print(f"El resultado de la operacion es: {res}")