# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

from cola import Queue

class Character:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def __str__(self):
        return f"{self.name} - {self.planet}"

# a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
def show_characters_by_planet(queue, planets):
    for character in queue.get_elements():
        if character.planet in planets:
            print(character)

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
def show_planet_of_characters(queue, character_names):
    for character in queue.get_elements():
        if character.name in character_names:
            print(f"{character.name} es de {character.planet}")

# c. Insertar un nuevo personaje antes del maestro Yoda
def insert_before_yoda(queue, new_character):
    temp_queue = Queue()
    inserted = False
    while queue.size() > 0:
        character = queue.attention()
        if character.name == "Yoda" and not inserted:
            temp_queue.arrive(new_character)
            inserted = True
        temp_queue.arrive(character)
    # Pasamos los elementos de la cola temporal a la original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

# d. Eliminar el personaje ubicado después de Jar Jar Binks
def remove_after_jar_jar(queue):
    temp_queue = Queue()
    remove_next = False
    while queue.size() > 0:
        character = queue.attention()
        if remove_next:
            remove_next = False  # Saltamos el siguiente personaje (después de Jar Jar Binks)
            continue
        temp_queue.arrive(character)
        if character.name == "Jar Jar Binks":
            remove_next = True
    # Pasamos los elementos de la cola temporal a la original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

# Creamos la cola de personajes
characters_queue = Queue()
characters_queue.arrive(Character("Luke Skywalker", "Tatooine"))
characters_queue.arrive(Character("Han Solo", "Corellia"))
characters_queue.arrive(Character("Leia Organa", "Alderaan"))
characters_queue.arrive(Character("Yoda", "Dagobah"))
characters_queue.arrive(Character("Jar Jar Binks", "Naboo"))
characters_queue.arrive(Character("Chewbacca", "Kashyyyk"))

# a. Mostrar personajes de Alderaan, Endor y Tatooine
print("Personajes de Alderaan, Endor y Tatooine:")
show_characters_by_planet(characters_queue, ["Alderaan", "Endor", "Tatooine"])

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
print("\nPlanetas de Luke Skywalker y Han Solo:")
show_planet_of_characters(characters_queue, ["Luke Skywalker", "Han Solo"])

# c. Insertar un nuevo personaje antes del maestro Yoda
print("\nInsertando a Obi-Wan Kenobi antes de Yoda:")
insert_before_yoda(characters_queue, Character("Obi-Wan Kenobi", "Stewjon"))
for character in characters_queue.get_elements():
    print(character)

# d. Eliminar el personaje después de Jar Jar Binks
print("\nEliminando el personaje después de Jar Jar Binks:")
remove_after_jar_jar(characters_queue)
for character in characters_queue.get_elements():
    print(character)



#=====================================Ejercicio comentado==================================================================================


# Importamos la clase Queue para manejar la estructura de la cola
from cola import Queue

# Definimos la clase Character para representar a cada personaje, incluyendo su nombre y planeta
class Character:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    # Método para representar al personaje como una cadena (nombre y planeta)
    def __str__(self):
        return f"{self.name} - {self.planet}"

# a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
# Esta función recorre la cola y muestra personajes que pertenecen a ciertos planetas
def show_characters_by_planet(queue, planets):
    for character in queue.get_elements():
        if character.planet in planets:
            print(character)

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
# Esta función recorre la cola y muestra el planeta de personajes específicos
def show_planet_of_characters(queue, character_names):
    for character in queue.get_elements():
        if character.name in character_names:
            print(f"{character.name} es de {character.planet}")

# c. Insertar un nuevo personaje antes del maestro Yoda
# Esta función inserta un personaje en la posición anterior al maestro Yoda
def insert_before_yoda(queue, new_character):
    temp_queue = Queue()  # Creamos una cola temporal
    inserted = False
    # Recorrer la cola original
    while queue.size() > 0:
        character = queue.attention()
        # Insertamos el nuevo personaje antes de Yoda
        if character.name == "Yoda" and not inserted:
            temp_queue.arrive(new_character)
            inserted = True
        temp_queue.arrive(character)
    # Transferimos los elementos de la cola temporal a la original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

# d. Eliminar el personaje ubicado después de Jar Jar Binks
# Esta función elimina al personaje que aparece justo después de Jar Jar Binks
def remove_after_jar_jar(queue):
    temp_queue = Queue()
    remove_next = False
    # Recorrer la cola original
    while queue.size() > 0:
        character = queue.attention()
        # Si la bandera está activada, omitimos el personaje actual
        if remove_next:
            remove_next = False
            continue
        temp_queue.arrive(character)
        # Activamos la bandera si encontramos a Jar Jar Binks
        if character.name == "Jar Jar Binks":
            remove_next = True
    # Transferimos los elementos de la cola temporal a la original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

# Creamos y cargamos la cola con personajes de Star Wars
characters_queue = Queue()
characters_queue.arrive(Character("Luke Skywalker", "Tatooine"))
characters_queue.arrive(Character("Han Solo", "Corellia"))
characters_queue.arrive(Character("Leia Organa", "Alderaan"))
characters_queue.arrive(Character("Yoda", "Dagobah"))
characters_queue.arrive(Character("Jar Jar Binks", "Naboo"))
characters_queue.arrive(Character("Chewbacca", "Kashyyyk"))

# a. Mostrar personajes de Alderaan, Endor y Tatooine
print("Personajes de Alderaan, Endor y Tatooine:")
show_characters_by_planet(characters_queue, ["Alderaan", "Endor", "Tatooine"])

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
print("\nPlanetas de Luke Skywalker y Han Solo:")
show_planet_of_characters(characters_queue, ["Luke Skywalker", "Han Solo"])

# c. Insertar un nuevo personaje antes del maestro Yoda
print("\nInsertando a Obi-Wan Kenobi antes de Yoda:")
insert_before_yoda(characters_queue, Character("Obi-Wan Kenobi", "Stewjon"))
for character in characters_queue.get_elements():
    print(character)

# d. Eliminar el personaje después de Jar Jar Binks
print("\nEliminando el personaje después de Jar Jar Binks:")
remove_after_jar_jar(characters_queue)
for character in characters_queue.get_elements():
    print(character)
