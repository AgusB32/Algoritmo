# ALGORITMO RECURSIVO, PAG 19 DEL LIBRO
     # factorial 5! = 5*4*3*2*1

def factorialI(numero):
    if numero == 0:
        return 1
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

print(factorialI(5))

def factorialR(numero):
    if numero ==0:
        return 1
    else:
        return numero * factorialR(numero-1)
print(factorialR(5))

def sumatoria(numero):
    if numero ==0:
        return 0
    else:
        return numero + sumatoria(numero-1)
    print (sumatoria(5))
    
    
#! ejercicio 3
#! 5 * 3= 5+5+5= N*M= N + (N* M-1)
def producto(num1, num2):
    if num2 ==1:
        return num1
    else:
        return num1 + producto(num1,num2-1)
print(producto(2,4))
        

# ejercicio 4
# 2^3=2*2*2= B*(B * Ex-1)
def potencia(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base,exponente-1)
print(potencia(2,3))

#26/03

# 6
def invertir_cadena(cadena):
    if len(cadena)==0:
        return cadena
    else:
        resuelta = cadena [-1] + invertir_cadena(cadena[:-1])
        return resuelta
print (invertir_cadena("hola"))
    #[:-1] saca el ultimo caracter
    
    
# 7


# 8

def convert_to_binary(numero):
    if numero <=1:
        return str(numero)
    else:
        return convert_to_binary(numero//2)+str(numero % 2)
print(convert_to_binary(13))

# 9


# 10
def count_digit(numero):
    if numero <10:
        return 1
    else:
        return 1 + count_digit(numero//10)
print(count_digit(123))

# 11
def invert_number(numero):
    if numero <10:
        return numero
    else:
        return (numero % 10) * 10 **len(str(numero//10)) + invert_number(numero//10)
print(invert_number(1234567))

# 12

def sumar_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero %10) + sumar_digitos(numero//10)
print(sumar_digitos(7777777))

#! 17
names =['jaun' , 'maria' , 'pepito', 'ana']
def barrido (lista):
    if len(lista)==1:
        return (lista[0])
    else:
        print(lista[-1])
        barrido (lista[:-1])
barrido(names)

#! 21
numeros= [1,2,3,7,10,23,45]
def recur(lista, buscado, primero,ultimo):
    medio= (primero + ultimo)//2
    if primero > ultimo:
        return None
    elif buscado == lista[medio]:
        return medio
    else:
        if buscado < lista[medio]:
            return recur(lista, buscado,primero,medio-1)
        else:
            return recur (lista, buscado, medio+1, ultimo)
pos= recur(numeros,7,0,len(numeros)-1)
print(f"posicion {pos}")
if pos is not None:
    print (pos,numeros[pos])
    

def raizaux(num_calc,valor=1):
    if num_calc == 0 or num_calc == 1:
        return num_calc
    else:
        resultado = valor * valor
        if resultado == num_calc:
            return valor
        elif resultado > num_calc:
            return valor-1
        else:
            return raizaux(num_calc, valor + 1)

print(raizaux(8))



#                                           Quicksort
"""Método de ordenamiento quicksort."""

def quicksort(lista, primero, ultimo):
    izquierda = primero
    derecha = ultimo-1
    pivote = ultimo
    print('indices', izquierda, derecha, lista[pivote])

    while (izquierda < derecha):

        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha):
            izquierda += 1
            print('deplazamineto izquierda', lista, izquierda)
            a = input()

        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda):
            derecha -= 1
            print('deplazamineto derecha', lista, derecha)
            a = input()

        if(izquierda < derecha):
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            print('intercambio interno', lista)
            a = input()

    if(lista[pivote] < lista[izquierda]):
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]
        print('intercambio pivote', lista)
        a = input()

    print('llamdas recursivas')
    if(primero < izquierda):
        quicksort(lista, primero, izquierda-1)
    if(ultimo > izquierda):
        quicksort(lista, izquierda+1, ultimo)

numeros=[4,9,1,5,8,2,4,5]
quicksort(numeros, 0, len(numeros)-1)