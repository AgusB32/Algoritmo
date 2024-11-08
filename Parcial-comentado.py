print("============================================= Punto uno =============================================")
print("")

# Definición de la clase para crear un árbol binario de búsqueda específico para almacenar datos de Pokémons
class PokemonBinaryTree:
    # Clase interna que representa un nodo en el árbol
    class Node:
        def __init__(self, key, pokemon):
            self.key = key  # Clave de búsqueda (puede ser nombre, número o tipo)
            self.pokemon = pokemon  # Diccionario con los datos del Pokémon
            self.left = None  # Hijo izquierdo
            self.right = None  # Hijo derecho

    def __init__(self):
        self.root = None  # Inicialización de la raíz del árbol

    # Método para insertar un nodo en el árbol
    def insert(self, key, pokemon):
        # Función auxiliar para la inserción recursiva
        def _insert(root, key, pokemon):
            if root is None:  # Si el nodo actual es None, insertar aquí
                return PokemonBinaryTree.Node(key, pokemon)
            elif key < root.key:  # Si la clave es menor, insertar en el subárbol izquierdo
                root.left = _insert(root.left, key, pokemon)
            else:  # Si la clave es mayor o igual, insertar en el subárbol derecho
                root.right = _insert(root.right, key, pokemon)
            return root
        self.root = _insert(self.root, key, pokemon)  # Llamada inicial para insertar en la raíz

    # Método para buscar un Pokémon por clave exacta
    def search_by_exact_key(self, key):
        # Función auxiliar de búsqueda recursiva
        def _search(root, key):
            if root is None:  # Si el nodo actual es None, no se encontró el Pokémon
                return None
            if root.key == key:  # Si la clave coincide, devolver el Pokémon
                return root.pokemon
            elif key < root.key:  # Si la clave es menor, buscar en el subárbol izquierdo
                return _search(root.left, key)
            else:  # Si la clave es mayor, buscar en el subárbol derecho
                return _search(root.right, key)
        return _search(self.root, key)  # Llamada inicial en la raíz

    # Método para buscar Pokémons cuyos nombres contienen una subcadena dada (búsqueda por proximidad)
    def search_by_proximity(self, substring):
        results = []  # Lista para almacenar los resultados
        # Función auxiliar de búsqueda recursiva
        def _search(root, substring):
            if root:
                # Si el nombre contiene la subcadena, añadir el Pokémon a los resultados
                if substring.lower() in root.key.lower():
                    results.append(root.pokemon)
                _search(root.left, substring)  # Buscar en el subárbol izquierdo
                _search(root.right, substring)  # Buscar en el subárbol derecho
        _search(self.root, substring)  # Llamada inicial en la raíz
        return results  # Devolver los resultados

    # Método para obtener una lista de todos los Pokémons en orden ascendente según la clave del árbol
    def in_order(self):
        results = []  # Lista para almacenar los resultados en orden
        # Función auxiliar de recorrido en orden
        def _in_order(root):
            if root:
                _in_order(root.left)  # Recorrer el subárbol izquierdo
                results.append(root.pokemon)  # Añadir el Pokémon actual a los resultados
                _in_order(root.right)  # Recorrer el subárbol derecho
        _in_order(self.root)  # Llamada inicial en la raíz
        return results  # Devolver los resultados ordenados

# Crear tres árboles binarios de búsqueda: uno para nombre, otro para número y otro para tipo
name_tree = PokemonBinaryTree()
number_tree = PokemonBinaryTree()
type_tree = PokemonBinaryTree()

# Lista de datos de Pokémons para insertar en los árboles
pokemon_list = [
    {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None, "numero": 25},
    {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador", "numero": 6},
    {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno", "numero": 1},
    {"nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico", "numero": 121},
    {"nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None, "numero": 54},
    {"nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador", "numero": 130},
    {"nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra", "numero": 95},
    {"nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra", "numero": 74},
    {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None, "numero": 37},
    {"nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None, "numero": 9},
    {"nombre": "Umbreon", "nivel": 45, "tipo": "Siniestro", "subtipo": None, "numero": 197},
    {"nombre": "Nidoking", "nivel": 40, "tipo": "Veneno", "subtipo": "Tierra", "numero": 34}
]

# Insertar cada Pokémon en los tres árboles según su nombre, número y tipo
for pokemon in pokemon_list:
    name_tree.insert(pokemon["nombre"], pokemon)
    number_tree.insert(pokemon["numero"], pokemon)
    type_tree.insert(pokemon["tipo"], pokemon)

# b) Búsqueda por proximidad: muestra todos los Pokémons cuyo nombre contiene "bul"
print("b) Búsqueda de 'bul' en nombres:")
for pokemon in name_tree.search_by_proximity("bul"):
    print(pokemon)

# c) Mostrar todos los nombres de los Pokémons de los tipos específicos (Agua, Fuego, Planta y Eléctrico)
def show_pokemon_by_type(type_name):
    print(f"\nc) Pokémon de tipo '{type_name}':")
    for pokemon in type_tree.search_by_proximity(type_name):
        print(pokemon["nombre"])

show_pokemon_by_type("Agua")
show_pokemon_by_type("Fuego")
show_pokemon_by_type("Planta")
show_pokemon_by_type("Eléctrico")

# d) Listar en orden ascendente por número y nombre de Pokémon
print("\nd) Pokémon ordenados por número y nombre:")
for pokemon in number_tree.in_order():
    print(f"{pokemon['nombre']} (Número: {pokemon['numero']})")

# Listado en orden ascendente por nombre y nivel de Pokémon
print("\nPokémon ordenados por nivel y nombre:")
for pokemon in name_tree.in_order():
    print(f"{pokemon['nombre']} (Nivel: {pokemon['nivel']})")

# e) Mostrar datos específicos de los Pokémons: Jolteon, Lycanroc y Tyrantrum
print("\ne) Datos de Jolteon, Lycanroc y Tyrantrum:")
for name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
    result = name_tree.search_by_exact_key(name)
    if result:
        print(result)
    else:
        print(f"{name} no encontrado.")

# f) Contar la cantidad de Pokémons de tipo Eléctrico y Acero
def count_by_type(type_name):
    return len(type_tree.search_by_proximity(type_name))

print("\nf) Cantidad de Pokémon de tipo 'Eléctrico':", count_by_type("Eléctrico"))
print("Cantidad de Pokémon de tipo 'Acero':", count_by_type("Acero"))

print("")
print("")
print("============================================= Punto dos =============================================")
print("")

# Definición de la clase Graph para representar un grafo no dirigido con personajes de Star Wars
class Graph:
    def __init__(self):
        # Diccionario de adyacencia para almacenar los vértices (personajes) y las aristas (episodios compartidos)
        self.adjacency_list = {}

    # Método para añadir un personaje (vértice) al grafo
    def add_character(self, name):
        # Si el personaje no está en la lista de adyacencia, añadirlo con un diccionario vacío como valor
        if name not in self.adjacency_list:
            self.adjacency_list[name] = {}

    # Método para añadir una arista entre dos personajes, indicando los episodios compartidos
    def add_episode(self, char1, char2, episodes):
        # Asegurar que ambos personajes existen en el grafo y añadir la arista en ambas direcciones
        if char1 in self.adjacency_list and char2 in self.adjacency_list:
            self.adjacency_list[char1][char2] = episodes
            self.adjacency_list[char2][char1] = episodes

    # Algoritmo de Prim para encontrar el árbol de expansión mínimo (MST)
    def prim_mst(self):
        import heapq  # Biblioteca para trabajar con colas de prioridad (min-heaps)
        
        # Verificar si el grafo está vacío
        if not self.adjacency_list:
            return [], 0  # Si está vacío, devolver un MST vacío y peso cero
        
        # Seleccionar un nodo de inicio arbitrario
        start_node = next(iter(self.adjacency_list))
        visited = set()  # Conjunto para almacenar nodos visitados
        min_heap = [(0, start_node, None)]  # Cola de prioridad para la selección de aristas mínimas
        mst = []  # Lista para almacenar el MST resultante
        total_weight = 0  # Peso total del MST
        
        # Mientras haya elementos en la cola de prioridad
        while min_heap:
            # Extraer la arista con menor peso
            weight, current, related_character = heapq.heappop(min_heap)
            if current not in visited:  # Si el nodo actual no ha sido visitado
                visited.add(current)  # Marcarlo como visitado
                total_weight += weight  # Sumar el peso de la arista al peso total
                if related_character is not None:  # Si hay un personaje relacionado, añadir la arista al MST
                    mst.append((weight, current, related_character))
                
                # Agregar todas las aristas del nodo actual a la cola de prioridad
                for neighbor, edge_weight in self.adjacency_list[current].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, neighbor, current))
        
        # Devolver el MST y un booleano indicando si Yoda está en el MST
        return mst, 'Yoda' in visited

    # Método para determinar el máximo número de episodios compartidos entre dos personajes
    def max_episodes_shared(self):
        max_episodes = 0  # Inicializar el máximo de episodios compartidos a cero
        characters = (None, None)  # Tupla para almacenar los personajes con el máximo de episodios compartidos
        
        # Recorrer cada personaje y sus conexiones
        for char1 in self.adjacency_list:
            for char2, episodes in self.adjacency_list[char1].items():
                # Si se encuentra una mayor cantidad de episodios, actualizar los personajes y el valor máximo
                if episodes > max_episodes:
                    max_episodes = episodes
                    characters = (char1, char2)
        
        # Devolver los personajes y el número máximo de episodios compartidos
        return characters, max_episodes


# Crear una instancia del grafo para personajes de Star Wars
star_wars_graph = Graph()

# d) Añadir los personajes indicados en el grafo como vértices
characters = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

# Añadir cada personaje al grafo
for character in characters:
    star_wars_graph.add_character(character)

# Añadir aristas representando los episodios compartidos entre pares de personajes
star_wars_graph.add_episode("Luke Skywalker", "Darth Vader", 5)
star_wars_graph.add_episode("Yoda", "Darth Vader", 3)
star_wars_graph.add_episode("Yoda", "Luke Skywalker", 4)
star_wars_graph.add_episode("Boba Fett", "Han Solo", 2)
star_wars_graph.add_episode("C-3PO", "R2-D2", 7)
star_wars_graph.add_episode("Leia", "Luke Skywalker", 6)
star_wars_graph.add_episode("Rey", "Kylo Ren", 4)
star_wars_graph.add_episode("Chewbacca", "Han Solo", 5)
star_wars_graph.add_episode("BB-8", "Rey", 3)

# b) Hallar el árbol de expansión mínimo usando el algoritmo de Prim
mst, contains_yoda = star_wars_graph.prim_mst()
print("b) Árbol de expansión mínimo:")
# Mostrar cada arista del MST con su peso y los personajes relacionados
for weight, character, related_character in mst:
    print(f"Personaje: {character}, Relacionado con: {related_character}, Peso: {weight}")
# Verificar si Yoda está en el MST
print("¿Contiene a Yoda?", contains_yoda)

# c) Determinar los personajes que comparten el mayor número de episodios y cuántos episodios son
characters, max_shared = star_wars_graph.max_episodes_shared()
print(f"\nc) Máximo de episodios compartidos: {max_shared} entre {characters[0]} y {characters[1]}.")