# Desarrollar una función que permita convertir un número romano en un número decimal.
tabla = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def convercion(numeroR):
    if not numeroR:
        return 0
    
    elif len(numeroR) == 1:
        return tabla[numeroR]
    
    elif tabla[numeroR[0]] < tabla[numeroR[1:]]:
        return -tabla[numeroR[0]] + tabla[numeroR[1:]]
    
    else:
        return tabla[numeroR[0]] + tabla[numeroR[1:]]
numeroR = input("Ingrese un numero romano: ").upper()
res = convercion(numeroR)
print(f"{numeroR} convertido a decimal es {res}")