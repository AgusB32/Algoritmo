# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi 
# “con ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila.

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
# para encontrarlo,

# c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    if indice >= len(mochila):
        return None, objetos_sacados

    objeto_actual = mochila[indice]
    
    if objeto_actual == "sable de luz":
        return indice, objetos_sacados
    
    return usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)

mochila = ['taza con diseño de Yoda', 'sable de luz', 'libro de Star Wars', 'remera con el logo de Star Wars']

indice_sable, objetos_sacados = usar_la_fuerza(mochila)

if indice_sable is None:
    print("No se encontró ningún sable de luz en la mochila.")
else:
    print("Se encontró un sable de luz en la posición", indice_sable)
    print("Se necesitaron sacar", objetos_sacados, "objetos para encontrarlo.")