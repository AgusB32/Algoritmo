# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi 
# “con ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila.

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
# para encontrarlo,

# c. Utilizar un vector para representar la mochila.
mochila = ['taza con diseño de Yoda', 'sable de luz', 'libro de Star Wars', 'remera con el logo de Star Wars']
def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    if indice >= len(mochila):
        return None, objetos_sacados

objeto_actual = mochila[indice]



def usar_la_fuerza(mochila, indice=0, objetos_extraidos=0):
    # Caso base: si el índice supera la longitud de la mochila, o ya encontramos un sable de luz.
    if indice >= len(mochila):
        return None, objetos_extraidos
    
    # Obtenemos el objeto en el índice actual de la mochila.
    objeto_actual = mochila[indice]
    
    # Si el objeto actual es un sable de luz, retornamos su índice y la cantidad de objetos extraídos.
    if objeto_actual == "sable de luz":
        return indice, objetos_extraidos
    
    # Caso recursivo: seguimos buscando en los objetos restantes de la mochila.
    return usar_la_fuerza(mochila, indice + 1, objetos_extraidos + 1)

# Ejemplo de uso:
mochila = ["comida", "ropa", "herramientas", "sable de luz", "libro", "botiquín"]
indice_sable, objetos_extraidos = usar_la_fuerza(mochila)
if indice_sable is not None:
    print("Se encontró un sable de luz en la posición", indice_sable)
    print("Se necesitaron sacar", objetos_extraidos, "objetos para encontrarlo.")
else:
    print("No se encontró ningún sable de luz en la mochila.")