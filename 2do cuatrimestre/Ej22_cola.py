# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

from cola import Queue

class MCUCharacter:
    def __init__(self, character_name, superhero_name, gender):
        self.character_name = character_name
        self.superhero_name = superhero_name
        self.gender = gender

    def __str__(self):
        return f"{self.character_name}, {self.superhero_name}, {self.gender}"

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def find_character_by_superhero(queue, superhero_name):
    for character in queue.get_elements():
        if character.superhero_name == superhero_name:
            print(f"El personaje de {superhero_name} es {character.character_name}")
            return character.character_name
    print(f"No se encontró el personaje de {superhero_name}.")
    return None

# b. Mostrar los nombres de los superhéroes femeninos
def show_female_superheroes(queue):
    print("Superhéroes femeninos:")
    for character in queue.get_elements():
        if character.gender == "F":
            print(character.superhero_name)

# c. Mostrar los nombres de los personajes masculinos
def show_male_characters(queue):
    print("Personajes masculinos:")
    for character in queue.get_elements():
        if character.gender == "M":
            print(character.character_name)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def find_superhero_by_character(queue, character_name):
    for character in queue.get_elements():
        if character.character_name == character_name:
            print(f"El superhéroe de {character_name} es {character.superhero_name}")
            return character.superhero_name
    print(f"No se encontró el superhéroe de {character_name}.")
    return None

# e. Mostrar todos los datos de los personajes cuyos nombres comienzan con 'S'
def show_characters_starting_with_s(queue):
    print("Personajes o superhéroes cuyos nombres comienzan con 'S':")
    for character in queue.get_elements():
        if character.character_name.startswith("S") or character.superhero_name.startswith("S"):
            print(character)

# f. Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
def check_carol_danvers(queue):
    for character in queue.get_elements():
        if character.character_name == "Carol Danvers":
            print(f"Carol Danvers es {character.superhero_name}")
            return character.superhero_name
    print("Carol Danvers no se encuentra en la cola.")
    return None

# Creamos la cola de personajes MCU
mcu_queue = Queue()
mcu_queue.arrive(MCUCharacter("Tony Stark", "Iron Man", "M"))
mcu_queue.arrive(MCUCharacter("Steve Rogers", "Capitán América", "M"))
mcu_queue.arrive(MCUCharacter("Natasha Romanoff", "Black Widow", "F"))
mcu_queue.arrive(MCUCharacter("Carol Danvers", "Capitana Marvel", "F"))
mcu_queue.arrive(MCUCharacter("Scott Lang", "Ant-Man", "M"))
mcu_queue.arrive(MCUCharacter("Peter Parker", "Spider-Man", "M"))

# a. Determinar el nombre del personaje de Capitana Marvel
print("\na. Nombre del personaje de Capitana Marvel:")
find_character_by_superhero(mcu_queue, "Capitana Marvel")

# b. Mostrar los nombres de los superhéroes femeninos
print("\nb. Superhéroes femeninos:")
show_female_superheroes(mcu_queue)

# c. Mostrar los nombres de los personajes masculinos
print("\nc. Personajes masculinos:")
show_male_characters(mcu_queue)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
print("\nd. Superhéroe del personaje Scott Lang:")
find_superhero_by_character(mcu_queue, "Scott Lang")

# e. Mostrar todos los datos de los personajes cuyos nombres comienzan con 'S'
print("\ne. Personajes o superhéroes cuyos nombres comienzan con 'S':")
show_characters_starting_with_s(mcu_queue)

# f. Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
print("\nf. Carol Danvers en la cola:")
check_carol_danvers(mcu_queue)



#=====================================Ejercicio comentado==================================================================================


# Importamos la clase Queue desde el módulo cola
from cola import Queue

# Definimos la clase MCUCharacter que representa a un personaje del MCU
class MCUCharacter:
    def __init__(self, character_name, superhero_name, gender):
        # Inicializamos el nombre del personaje, el nombre del superhéroe y el género
        self.character_name = character_name
        self.superhero_name = superhero_name
        self.gender = gender

    def __str__(self):
        # Representación en cadena para mostrar fácilmente los datos del personaje
        return f"{self.character_name}, {self.superhero_name}, {self.gender}"

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def find_character_by_superhero(queue, superhero_name):
    # Recorremos los elementos de la cola
    for character in queue.get_elements():
        # Verificamos si el nombre del superhéroe coincide con el buscado
        if character.superhero_name == superhero_name:
            # Imprimimos y devolvemos el nombre del personaje
            print(f"El personaje de {superhero_name} es {character.character_name}")
            return character.character_name
    # Si no se encuentra el personaje, imprimimos un mensaje y devolvemos None
    print(f"No se encontró el personaje de {superhero_name}.")
    return None

# b. Mostrar los nombres de los superhéroes femeninos
def show_female_superheroes(queue):
    print("Superhéroes femeninos:")
    # Recorremos los elementos de la cola
    for character in queue.get_elements():
        # Verificamos si el género es femenino (F)
        if character.gender == "F":
            # Imprimimos el nombre del superhéroe
            print(character.superhero_name)

# c. Mostrar los nombres de los personajes masculinos
def show_male_characters(queue):
    print("Personajes masculinos:")
    # Recorremos los elementos de la cola
    for character in queue.get_elements():
        # Verificamos si el género es masculino (M)
        if character.gender == "M":
            # Imprimimos el nombre del personaje
            print(character.character_name)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def find_superhero_by_character(queue, character_name):
    # Recorremos los elementos de la cola
    for character in queue.get_elements():
        # Verificamos si el nombre del personaje coincide con el buscado
        if character.character_name == character_name:
            # Imprimimos y devolvemos el nombre del superhéroe
            print(f"El superhéroe de {character_name} es {character.superhero_name}")
            return character.superhero_name
    # Si no se encuentra el superhéroe, imprimimos un mensaje y devolvemos None
    print(f"No se encontró el superhéroe de {character_name}.")
    return None

# e. Mostrar todos los datos de los personajes cuyos nombres comienzan con 'S'
def show_characters_starting_with_s(queue):
    print("Personajes o superhéroes cuyos nombres comienzan con 'S':")
    # Recorremos los elementos de la cola
    for character in queue.get_elements():
        # Verificamos si el nombre del personaje o del superhéroe comienza con 'S'
        if character.character_name.startswith("S") or character.superhero_name.startswith("S"):
            # Imprimimos los datos del personaje
            print(character)

# f. Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
def check_carol_danvers(queue):
    # Recorremos los elementos de la cola
    for character in queue.get_elements():
        # Verificamos si el nombre del personaje es "Carol Danvers"
        if character.character_name == "Carol Danvers":
            # Imprimimos y devolvemos el nombre de su superhéroe
            print(f"Carol Danvers es {character.superhero_name}")
            return character.superhero_name
    # Si no se encuentra a Carol Danvers, imprimimos un mensaje y devolvemos None
    print("Carol Danvers no se encuentra en la cola.")
    return None

# Creamos la cola de personajes MCU
mcu_queue = Queue()
# Añadimos varios personajes a la cola con su nombre, superhéroe y género
mcu_queue.arrive(MCUCharacter("Tony Stark", "Iron Man", "M"))
mcu_queue.arrive(MCUCharacter("Steve Rogers", "Capitán América", "M"))
mcu_queue.arrive(MCUCharacter("Natasha Romanoff", "Black Widow", "F"))
mcu_queue.arrive(MCUCharacter("Carol Danvers", "Capitana Marvel", "F"))
mcu_queue.arrive(MCUCharacter("Scott Lang", "Ant-Man", "M"))
mcu_queue.arrive(MCUCharacter("Peter Parker", "Spider-Man", "M"))

# a. Determinar el nombre del personaje de Capitana Marvel
print("\na. Nombre del personaje de Capitana Marvel:")
find_character_by_superhero(mcu_queue, "Capitana Marvel")

# b. Mostrar los nombres de los superhéroes femeninos
print("\nb. Superhéroes femeninos:")
show_female_superheroes(mcu_queue)

# c. Mostrar los nombres de los personajes masculinos
print("\nc. Personajes masculinos:")
show_male_characters(mcu_queue)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
print("\nd. Superhéroe del personaje Scott Lang:")
find_superhero_by_character(mcu_queue, "Scott Lang")

# e. Mostrar todos los datos de los personajes cuyos nombres comienzan con 'S'
print("\ne. Personajes o superhéroes cuyos nombres comienzan con 'S':")
show_characters_starting_with_s(mcu_queue)

# f. Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
print("\nf. Carol Danvers en la cola:")
check_carol_danvers(mcu_queue)
