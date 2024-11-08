# 23)
# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from cola import Queue
from arbol import BinaryTree

# Definición de la clase para la criatura
class Creature:
    def __init__(self, name, defeated_by=None, description=None, captured_by=None):
        self.name = name
        self.defeated_by = defeated_by  # Quien derrotó a la criatura
        self.description = description  # Descripción breve de la criatura
        self.captured_by = captured_by  # Quién capturó a la criatura

# Árbol de criaturas mitológicas
creatures_tree = BinaryTree()

# Cargar criaturas en el árbol
creatures = [
    ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", None), ("Pefredo", None), ("Enio", None), ("Escila", None),
    ("Caribdis", None), ("Euríale", None), ("Esteno", None), ("Medusa", "Perseo"),
    ("Ladón", "Heracles"), ("Águila del Cáucaso", None), ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"), ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"), ("Dragón de la Cólquida", None), ("Cerbero", None),
    ("Toro de Creta", "Teseo"), ("Cierva de Cerinea", "Heracles"), ("Jabalí de Erimanto", "Heracles")
]

# Insertamos las criaturas en el árbol
for name, defeated_by in creatures:
    creatures_tree.insert_node(name, {"defeated_by": defeated_by})

# Consultas

# a. Listado inorden de las criaturas y quienes las derrotaron
print("Listado Inorden de las criaturas y quién las derrotó:")
creatures_tree.inorden()

# b. Cargar descripción sobre cada criatura
cerbero = creatures_tree.search("Cerbero")
if cerbero:
    cerbero.other_value["description"] = "Un perro monstruoso con tres cabezas"
medusa = creatures_tree.search("Medusa")
if medusa:
    medusa.other_value["description"] = "Una de las tres gorgonas, derrotada por Perseo"

# c. Mostrar información de la criatura Talos
talos = creatures_tree.search("Talos")
if talos:
    print(f"Talos: {talos.value}, Derrotado por: {talos.other_value.get('defeated_by')}")

# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
heroes_count = {}
def count_defeats(root):
    if root is not None:
        defeated_by = root.other_value.get("defeated_by")
        if defeated_by:
            if defeated_by in heroes_count:
                heroes_count[defeated_by] += 1
            else:
                heroes_count[defeated_by] = 1
        count_defeats(root.left)
        count_defeats(root.right)

count_defeats(creatures_tree.root)
top_heroes = sorted(heroes_count.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 héroes que derrotaron más criaturas:", top_heroes)

# e. Listar las criaturas derrotadas por Heracles
print("Criaturas derrotadas por Heracles:")
defeated_by_heracles = []
def list_defeated_by_heracles(root):
    if root is not None:
        if root.other_value.get("defeated_by") == "Heracles":
            defeated_by_heracles.append(root.value)
        list_defeated_by_heracles(root.left)
        list_defeated_by_heracles(root.right)

list_defeated_by_heracles(creatures_tree.root)
print(defeated_by_heracles)

# f. Listar criaturas que no han sido derrotadas
print("Criaturas no derrotadas:")
undefeated_creatures = []
def list_undefeated(root):
    if root is not None:
        if root.other_value.get("defeated_by") is None:
            undefeated_creatures.append(root.value)
        list_undefeated(root.left)
        list_undefeated(root.right)

list_undefeated(creatures_tree.root)
print(undefeated_creatures)

# g. Actualizar capturas realizadas por Heracles
creatures_tree.search("Cerbero").other_value["captured_by"] = "Heracles"
creatures_tree.search("Toro de Creta").other_value["captured_by"] = "Heracles"
creatures_tree.search("Cierva de Cerinea").other_value["captured_by"] = "Heracles"
creatures_tree.search("Jabalí de Erimanto").other_value["captured_by"] = "Heracles"

# h. Modificar las criaturas capturadas por Heracles
criaturas_heracles = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]

for criatura in criaturas_heracles:
    nodo = creatures_tree.search(criatura)
    if nodo:
        nodo.other_value["captured_by"] = "Heracles"
    else:
        print(f"No se encontró la criatura {criatura} en el árbol.")

# i. Eliminar al Basilisco y las Sirenas
creatures_tree.delete_node("Basilisco")
creatures_tree.delete_node("Sirenas")

# j. Modificar nodo de Aves del Estínfalo, agregar que Heracles derrotó varias
aves_estinfalo = creatures_tree.search("Aves del Estínfalo")
if aves_estinfalo:
    aves_estinfalo.other_value["defeated_by"] = "Heracles (varias)"

# k. Modificar el nombre de la criatura Ladón a Dragón Ladón
ladon = creatures_tree.search("Ladón")
if ladon:
    ladon.value = "Dragón Ladón"

# l. Listado por nivel del árbol
print("Listado por nivel:")
creatures_tree.by_level()

# m. Mostrar criaturas capturadas por Heracles
print("Criaturas capturadas por Heracles:")
captured_by_heracles = []
def list_captured_by_heracles(root):
    if root is not None:
        if root.other_value.get("captured_by") == "Heracles":
            captured_by_heracles.append(root.value)
        list_captured_by_heracles(root.left)
        list_captured_by_heracles(root.right)

list_captured_by_heracles(creatures_tree.root)
print(captured_by_heracles)


#==============================Comentado==================================================


# Importamos las clases Queue y BinaryTree necesarias para el manejo de estructuras de datos
from cola import Queue
from arbol import BinaryTree

# Definición de la clase para almacenar la información de cada criatura mitológica
class Creature:
    def __init__(self, name, defeated_by=None, description=None, captured_by=None):
        self.name = name               # Nombre de la criatura
        self.defeated_by = defeated_by # Quién derrotó a la criatura
        self.description = description # Breve descripción de la criatura
        self.captured_by = captured_by # Quién capturó a la criatura

# Crear un árbol binario para almacenar las criaturas
creatures_tree = BinaryTree()

# Datos de las criaturas y quién las derrotó, en una lista
creatures = [
    ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", None), ("Pefredo", None), ("Enio", None), ("Escila", None),
    ("Caribdis", None), ("Euríale", None), ("Esteno", None), ("Medusa", "Perseo"),
    ("Ladón", "Heracles"), ("Águila del Cáucaso", None), ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"), ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"), ("Dragón de la Cólquida", None), ("Cerbero", None),
    ("Toro de Creta", "Teseo"), ("Cierva de Cerinea", "Heracles"), ("Jabalí de Erimanto", "Heracles")
]

# Insertar cada criatura en el árbol con su respectiva información
for name, defeated_by in creatures:
    creatures_tree.insert_node(name, {"defeated_by": defeated_by})

# Consultas

# a. Listado inorden de las criaturas y quién las derrotó
print("Listado Inorden de las criaturas y quién las derrotó:")
creatures_tree.inorden()

# b. Agregar una descripción a cada criatura
cerbero = creatures_tree.search("Cerbero")
if cerbero:
    cerbero.other_value["description"] = "Un perro monstruoso con tres cabezas"
medusa = creatures_tree.search("Medusa")
if medusa:
    medusa.other_value["description"] = "Una de las tres gorgonas, derrotada por Perseo"

# c. Mostrar información completa de la criatura "Talos"
talos = creatures_tree.search("Talos")
if talos:
    print(f"Talos: {talos.value}, Derrotado por: {talos.other_value.get('defeated_by')}")

# d. Determinar los 3 héroes o dioses que derrotaron la mayor cantidad de criaturas
heroes_count = {}  # Diccionario para contar las derrotas de cada héroe
def count_defeats(root):
    if root is not None:
        defeated_by = root.other_value.get("defeated_by")
        if defeated_by:
            heroes_count[defeated_by] = heroes_count.get(defeated_by, 0) + 1
        count_defeats(root.left)
        count_defeats(root.right)

count_defeats(creatures_tree.root)
top_heroes = sorted(heroes_count.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 héroes que derrotaron más criaturas:", top_heroes)

# e. Listar criaturas derrotadas por Heracles
print("Criaturas derrotadas por Heracles:")
defeated_by_heracles = []
def list_defeated_by_heracles(root):
    if root is not None:
        if root.other_value.get("defeated_by") == "Heracles":
            defeated_by_heracles.append(root.value)
        list_defeated_by_heracles(root.left)
        list_defeated_by_heracles(root.right)

list_defeated_by_heracles(creatures_tree.root)
print(defeated_by_heracles)

# f. Listar criaturas que no han sido derrotadas
print("Criaturas no derrotadas:")
undefeated_creatures = []
def list_undefeated(root):
    if root is not None:
        if root.other_value.get("defeated_by") is None:
            undefeated_creatures.append(root.value)
        list_undefeated(root.left)
        list_undefeated(root.right)

list_undefeated(creatures_tree.root)
print(undefeated_creatures)

# g. Marcar que Heracles capturó ciertas criaturas específicas
creatures_tree.search("Cerbero").other_value["captured_by"] = "Heracles"
creatures_tree.search("Toro de Creta").other_value["captured_by"] = "Heracles"
creatures_tree.search("Cierva de Cerinea").other_value["captured_by"] = "Heracles"
creatures_tree.search("Jabalí de Erimanto").other_value["captured_by"] = "Heracles"

# h. Actualizar campo 'captured_by' para criaturas capturadas por Heracles
criaturas_heracles = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]

for criatura in criaturas_heracles:
    nodo = creatures_tree.search(criatura)
    if nodo:
        nodo.other_value["captured_by"] = "Heracles"
    else:
        print(f"No se encontró la criatura {criatura} en el árbol.")

# i. Eliminar a "Basilisco" y "Sirenas" del árbol
creatures_tree.delete_node("Basilisco")
creatures_tree.delete_node("Sirenas")

# j. Modificar nodo de "Aves del Estínfalo" para añadir que Heracles derrotó varias
aves_estinfalo = creatures_tree.search("Aves del Estínfalo")
if aves_estinfalo:
    aves_estinfalo.other_value["defeated_by"] = "Heracles (varias)"

# k. Cambiar nombre de "Ladón" a "Dragón Ladón"
ladon = creatures_tree.search("Ladón")
if ladon:
    ladon.value = "Dragón Ladón"

# l. Realizar un listado de las criaturas por nivel en el árbol
print("Listado por nivel:")
creatures_tree.by_level()

# m. Mostrar criaturas capturadas por Heracles
print("Criaturas capturadas por Heracles:")
captured_by_heracles = []
def list_captured_by_heracles(root):
    if root is not None:
        if root.other_value.get("captured_by") == "Heracles":
            captured_by_heracles.append(root.value)
        list_captured_by_heracles(root.left)
        list_captured_by_heracles(root.right)

list_captured_by_heracles(creatures_tree.root)
print(captured_by_heracles)
