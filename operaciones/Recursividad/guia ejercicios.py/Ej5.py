#Desarrollar una función que permita convertir un número romano en un número decimal.

numeros_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def convercion(numr):
    if not numr:
        return 0
    
    if len(numr) == 1:
        return numeros_romanos[numr]

    if numeros_romanos[numr[0]] < numeros_romanos[numr[1]]:
        return numeros_romanos[numr[0]] + convercion(numr[1:])
    else:
            return numeros_romanos[numr[0]] + convercion(numr[1:])

numr = input('Ingrese el numero romano que desea pasarlo a decimal(usá mayus): ')
numd = convercion(numr)
print (f'El numero romano: {numr} pasado a decimal es: {numd}')