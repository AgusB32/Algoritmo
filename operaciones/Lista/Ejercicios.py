# 1) Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
nodos = [
    {'Futbolista': 'Cristiano Ronaldo', 'Edad': 39 },
    {'Futbolista': 'Lionel Messi', 'Edad': 36 },
    {'Futbolista': 'Eden Hazard', 'Edad': 33 },
    {'Futbolista': 'Neymar da Silva Santos Júnior', 'Edad': 32 }
]

print(len(nodos))


# 2) Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.
lista_de_caracteres = ['avion', 'auto', 'puerta', 'iker', 'ojo', 'rata', 'rice']
vocales = ['a','e','i','o','u']

print('Lista antes de eliminar vocales: ',lista_de_caracteres)

for palabra in lista_de_caracteres[:]:
    
    palabra_sin_vocales = ""
    
    for caracter in palabra:
        if caracter not in vocales:
            palabra_sin_vocales += caracter
    lista_de_caracteres[lista_de_caracteres.index(palabra)] = palabra_sin_vocales

print('Lista sin vocales: ',lista_de_caracteres)

# 3) Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
#    una que contenga los números pares y otra para los números impares.

lista_enteros = [8, 5, 4, 6, 2, 4, 1, 5]
num_pares = []
num_impares = []

print("Numeros antes de ser divididos: ",lista_enteros)

for numeros in lista_enteros:
    if numeros % 2 == 0:
        num_pares.append(numeros)
    else:
        num_impares.append(numeros)

print("Los numeros pares son: ",num_pares)
print("Los numeros impares son: ",num_impares)


# 4) Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
import random
def num_aleatorio(tamaño_lista):
    return random.randint(0, tamaño_lista)

lista = [6,5,34,2,9,77,8,2]
print("La lista original es: ",lista)

tamaño_lista = len(lista)

new_num = int(input("Ingrese un numero para agregar a la lista"))

aleatorio = num_aleatorio(tamaño_lista)

lista.insert(aleatorio,new_num)

print("La lista con el nuevo numero ingresado es: ",lista)


# 5) Dada una lista de números enteros eliminar de estas los números primos.
numeros = [22, 11, 30, 7, 13, 1]
print("Lista original", numeros)

def primo(numero):
    if numero <=1:
        return False
    if numero <=3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i+2) == 0:
            return False
        i += 6
    return True
sin_primos = [numero for numero in numeros if not primo(numero)]

print("Lista sin primos", sin_primos)


# 6) 