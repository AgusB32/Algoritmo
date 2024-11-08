# 5)
# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

from cola import Queue  # Usamos tu clase Queue
from arbol import BinaryTree  # Usamos tu clase BinaryTree

# a. Almacenar héroe o villano en cada nodo (ya está implementado al agregar nodos)

# b. Listar villanos ordenados alfabéticamente
def listar_villanos(arbol):
    villanos = []
    
    def __inorden_villanos(root):
        if root is not None:
            __inorden_villanos(root.left)
            if root.other_value.get('is_hero') is not True:
                villanos.append(root.value)
            __inorden_villanos(root.right)
    
    if arbol.root is not None:
        __inorden_villanos(arbol.root)
    
    return villanos

# c. Mostrar todos los superhéroes que empiezan con 'C'
def listar_superheroes_con_c(arbol):
    heroes_con_c = []
    
    def __inorden_superheroes_con_c(root):
        if root is not None:
            __inorden_superheroes_con_c(root.left)
            if root.other_value.get('is_hero') is True and root.value.startswith('C'):
                heroes_con_c.append(root.value)
            __inorden_superheroes_con_c(root.right)
    
    if arbol.root is not None:
        __inorden_superheroes_con_c(arbol.root)
    
    return heroes_con_c

# d. Contar cuántos superhéroes hay en el árbol (usamos la función contar_super_heroes de la clase BinaryTree)
def contar_superheroes(arbol):
    return arbol.contar_super_heroes()  # Ya implementado

# e. Modificar el nombre de Doctor Strange
def modificar_doctor_strange(arbol, nuevo_nombre):
    doctor = arbol.search("Doctor Strange")
    if doctor:
        doctor.value = nuevo_nombre
        print(f"Nombre modificado a: {nuevo_nombre}")
    else:
        print("Doctor Strange no se encuentra en el árbol.")

# f. Listar los superhéroes en orden descendente
def listar_superheroes_descendente(arbol):
    heroes_desc = []
    
    def __postorden_superheroes(root):
        if root is not None:
            __postorden_superheroes(root.right)
            if root.other_value.get('is_hero') is True:
                heroes_desc.append(root.value)
            __postorden_superheroes(root.left)
    
    if arbol.root is not None:
        __postorden_superheroes(arbol.root)
    
    return heroes_desc

# g. Generar un bosque (superhéroes y villanos)
def generar_bosque(arbol):
    arbol_heroes = BinaryTree()
    arbol_villanos = BinaryTree()

    def __separar_nodos(root):
        if root is not None:
            if root.other_value.get('is_hero') is True:
                arbol_heroes.insert_node(root.value, root.other_value)
            else:
                arbol_villanos.insert_node(root.value, root.other_value)
            __separar_nodos(root.left)
            __separar_nodos(root.right)
    
    if arbol.root is not None:
        __separar_nodos(arbol.root)
    
    return arbol_heroes, arbol_villanos

# Parte g-I: Contar nodos en cada árbol
def contar_nodos_arbol(arbol):
    return arbol.contar_super_heroes()

# Parte g-II: Barrido ordenado alfabéticamente de cada árbol
def barrido_ordenado_arbol(arbol):
    arbol.inorden()  # Ya tenemos un método inorden en BinaryTree

# Crear el árbol de personajes del MCU
arbol_mcu = BinaryTree()

# Insertamos algunos personajes del MCU
arbol_mcu.insert_node("Captain America", {'is_hero': True})
arbol_mcu.insert_node("Iron Man", {'is_hero': True})
arbol_mcu.insert_node("Thanos", {'is_hero': False})
arbol_mcu.insert_node("Doctor Strange", {'is_hero': True})
arbol_mcu.insert_node("Loki", {'is_hero': False})

# Listar villanos
villanos = listar_villanos(arbol_mcu)
print("Villanos ordenados alfabéticamente:", villanos)

# Superhéroes que empiezan con 'C'
heroes_con_c = listar_superheroes_con_c(arbol_mcu)
print("Superhéroes que empiezan con C:", heroes_con_c)

# Contar superhéroes
cantidad_superheroes = contar_superheroes(arbol_mcu)
print("Cantidad de superhéroes:", cantidad_superheroes)

# Modificar Doctor Strange
modificar_doctor_strange(arbol_mcu, "Dr. Strange")

# Listar superhéroes en orden descendente
heroes_desc = listar_superheroes_descendente(arbol_mcu)
print("Superhéroes en orden descendente:", heroes_desc)

# Generar un bosque
arbol_heroes, arbol_villanos = generar_bosque(arbol_mcu)

# Contar nodos en cada árbol
print("Cantidad de nodos en el árbol de superhéroes:", contar_nodos_arbol(arbol_heroes))
print("Cantidad de nodos en el árbol de villanos:", contar_nodos_arbol(arbol_villanos))

# Barrido ordenado alfabéticamente
print("Superhéroes ordenados:")
barrido_ordenado_arbol(arbol_heroes)

print("Villanos ordenados:")
barrido_ordenado_arbol(arbol_villanos)


#==============================Comentado==================================================


from cola import Queue  # Usamos la clase Queue proporcionada
from arbol import BinaryTree  # Usamos la clase BinaryTree proporcionada

# a. Almacenar héroe o villano en cada nodo (ya se implementa al agregar nodos al árbol)

# b. Listar villanos ordenados alfabéticamente
def listar_villanos(arbol):
    villanos = []  # Lista para almacenar los villanos en orden alfabético
    
    # Función de recorrido en orden para añadir villanos a la lista
    def __inorden_villanos(root):
        if root is not None:
            __inorden_villanos(root.left)  # Recorrido del subárbol izquierdo
            if root.other_value.get('is_hero') is not True:  # Verifica si es villano
                villanos.append(root.value)  # Añade el villano a la lista
            __inorden_villanos(root.right)  # Recorrido del subárbol derecho
    
    # Llama a la función interna si el árbol no está vacío
    if arbol.root is not None:
        __inorden_villanos(arbol.root)
    
    return villanos

# c. Mostrar todos los superhéroes que empiezan con 'C'
def listar_superheroes_con_c(arbol):
    heroes_con_c = []  # Lista para almacenar héroes que comienzan con 'C'
    
    # Función de recorrido en orden para verificar nombres
    def __inorden_superheroes_con_c(root):
        if root is not None:
            __inorden_superheroes_con_c(root.left)  # Recorre el subárbol izquierdo
            if root.other_value.get('is_hero') is True and root.value.startswith('C'):
                heroes_con_c.append(root.value)  # Añade el héroe a la lista si empieza con 'C'
            __inorden_superheroes_con_c(root.right)  # Recorre el subárbol derecho
    
    # Llama a la función interna si el árbol no está vacío
    if arbol.root is not None:
        __inorden_superheroes_con_c(arbol.root)
    
    return heroes_con_c

# d. Contar cuántos superhéroes hay en el árbol
def contar_superheroes(arbol):
    return arbol.contar_super_heroes()  # Llama a la función de conteo en BinaryTree

# e. Modificar el nombre de Doctor Strange
def modificar_doctor_strange(arbol, nuevo_nombre):
    # Busca al personaje "Doctor Strange" en el árbol
    doctor = arbol.search("Doctor Strange")
    if doctor:
        doctor.value = nuevo_nombre  # Cambia el nombre si el personaje está en el árbol
        print(f"Nombre modificado a: {nuevo_nombre}")
    else:
        print("Doctor Strange no se encuentra en el árbol.")

# f. Listar los superhéroes en orden descendente
def listar_superheroes_descendente(arbol):
    heroes_desc = []  # Lista para héroes en orden descendente
    
    # Función de recorrido postorden inverso para listado descendente
    def __postorden_superheroes(root):
        if root is not None:
            __postorden_superheroes(root.right)  # Recorre el subárbol derecho primero
            if root.other_value.get('is_hero') is True:
                heroes_desc.append(root.value)  # Añade el héroe si es héroe
            __postorden_superheroes(root.left)  # Recorre el subárbol izquierdo
    
    # Llama a la función interna si el árbol no está vacío
    if arbol.root is not None:
        __postorden_superheroes(arbol.root)
    
    return heroes_desc

# g. Generar un bosque (superhéroes y villanos)
def generar_bosque(arbol):
    arbol_heroes = BinaryTree()  # Árbol para superhéroes
    arbol_villanos = BinaryTree()  # Árbol para villanos

    # Función para separar héroes y villanos en dos árboles
    def __separar_nodos(root):
        if root is not None:
            # Inserta en el árbol correspondiente según el tipo de personaje
            if root.other_value.get('is_hero') is True:
                arbol_heroes.insert_node(root.value, root.other_value)
            else:
                arbol_villanos.insert_node(root.value, root.other_value)
            # Recorrido en ambos subárboles
            __separar_nodos(root.left)
            __separar_nodos(root.right)
    
    # Llama a la función interna si el árbol no está vacío
    if arbol.root is not None:
        __separar_nodos(arbol.root)
    
    return arbol_heroes, arbol_villanos

# Parte g-I: Contar nodos en cada árbol del bosque
def contar_nodos_arbol(arbol):
    return arbol.contar_super_heroes()  # Llama a la función de conteo en BinaryTree

# Parte g-II: Barrido ordenado alfabéticamente de cada árbol
def barrido_ordenado_arbol(arbol):
    arbol.inorden()  # Usa el método inorden de BinaryTree para barrido ordenado

# Crear el árbol de personajes del MCU
arbol_mcu = BinaryTree()

# Insertamos algunos personajes del MCU
arbol_mcu.insert_node("Captain America", {'is_hero': True})
arbol_mcu.insert_node("Iron Man", {'is_hero': True})
arbol_mcu.insert_node("Thanos", {'is_hero': False})
arbol_mcu.insert_node("Doctor Strange", {'is_hero': True})
arbol_mcu.insert_node("Loki", {'is_hero': False})

# Listar villanos en orden alfabético
villanos = listar_villanos(arbol_mcu)
print("Villanos ordenados alfabéticamente:", villanos)

# Listar superhéroes que empiezan con 'C'
heroes_con_c = listar_superheroes_con_c(arbol_mcu)
print("Superhéroes que empiezan con C:", heroes_con_c)

# Contar el total de superhéroes en el árbol
cantidad_superheroes = contar_superheroes(arbol_mcu)
print("Cantidad de superhéroes:", cantidad_superheroes)

# Modificar el nombre de Doctor Strange
modificar_doctor_strange(arbol_mcu, "Dr. Strange")

# Listar superhéroes en orden descendente
heroes_desc = listar_superheroes_descendente(arbol_mcu)
print("Superhéroes en orden descendente:", heroes_desc)

# Generar un bosque de superhéroes y villanos
arbol_heroes, arbol_villanos = generar_bosque(arbol_mcu)

# Contar nodos en cada árbol del bosque
print("Cantidad de nodos en el árbol de superhéroes:", contar_nodos_arbol(arbol_heroes))
print("Cantidad de nodos en el árbol de villanos:", contar_nodos_arbol(arbol_villanos))

# Barrido ordenado alfabéticamente de cada árbol del bosque
print("Superhéroes ordenados:")
barrido_ordenado_arbol(arbol_heroes)

print("Villanos ordenados:")
barrido_ordenado_arbol(arbol_villanos)
