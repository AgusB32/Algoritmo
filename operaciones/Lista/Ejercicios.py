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


# 6) Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#    casa de comic a la que pertenece (Marvel o DC) y biografía, implementar las funciones necesa-
#    rias para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from lista import search

super_heroes = [
    {"nombre": "Linterna Verde", "año_aparicion": 1940, "casa_comic": "DC Comics", "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."},
    {"nombre": "Wolverine","año_aparicion": 1974,"casa_comic": "Marvel Comics","biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."},
    {"nombre": "Doctor Strange","año_aparicion": 1963,"casa_comic": "Marvel Comics","biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."},
    {"nombre": "Capitana Marvel","año_aparicion": 1968,"casa_comic": "Marvel Comics","biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."},
    {"nombre": "Mujer Maravilla","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."},
    {"nombre": "Flash","año_aparicion": 1940,"casa_comic": "DC Comics","biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."},
    {"nombre": "Star-Lord","año_aparicion": 1976,"casa_comic": "Marvel Comics","biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."},
    {"nombre": "Superman","año_aparicion": 1938,"casa_comic": "DC Comics","biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."},
    {"nombre": "Batman","año_aparicion": 1939,"casa_comic": "DC Comics","biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."},
    {"nombre": "Iron Man","año_aparicion": 1963,"casa_comic": "Marvel Comics","biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."},
    {"nombre": "Wonder Woman","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."},
    {"nombre": "Spider-Man","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."},
    {"nombre": "Thor","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."},
    {"nombre": "Aquaman","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."},
    {"nombre": "Green Arrow","año_aparicion": 1941,"casa_comic": "DC Comics","biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."},
    {"nombre": "Hulk","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."},
    {"nombre": "Black Widow","año_aparicion": 1964,"casa_comic": "Marvel Comics","biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."},
    {"nombre": "Mr. Fantástico","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."},
    {"nombre": "La Mujer Invisible","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."},
    {"nombre": "La Antorcha Humana","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."},
    {"nombre": "La Cosa","año_aparicion": 1961,"casa_comic": "Marvel Comics","biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."},
    {"nombre": "Capitán América","año_aparicion": 1941,"casa_comic": "Marvel Comics","biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."},
    {"nombre": "Ant-Man","año_aparicion": 1962,"casa_comic": "Marvel Comics","biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."}
]

index = search(super_heroes,"nombre","Linterna Verde")

if index is not None:
    super_hero = super_heroes[index]
    print (f"El año de aparicion de {super_hero["nombre"]} es {super_hero["año_aparicion"]}")
else:
    primo("No esta en la lista")