# 1) Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#      último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#      mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#   además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

print("")
print("============================================= Punto uno =============================================")
print("")

class PokemonBinaryTree:
    class Node:
        def __init__(self, key, pokemon):
            self.key = key
            self.pokemon = pokemon
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key, pokemon):
        def _insert(root, key, pokemon):
            if root is None:
                return PokemonBinaryTree.Node(key, pokemon)
            elif key < root.key:
                root.left = _insert(root.left, key, pokemon)
            else:
                root.right = _insert(root.right, key, pokemon)
            return root
        self.root = _insert(self.root, key, pokemon)

    def search_by_exact_key(self, key):
        def _search(root, key):
            if root is None:
                return None
            if root.key == key:
                return root.pokemon
            elif key < root.key:
                return _search(root.left, key)
            else:
                return _search(root.right, key)
        return _search(self.root, key)

    def search_by_proximity(self, substring):
        results = []
        def _search(root, substring):
            if root:
                if substring.lower() in root.key.lower():
                    results.append(root.pokemon)
                _search(root.left, substring)
                _search(root.right, substring)
        _search(self.root, substring)
        return results

    def in_order(self):
        results = []
        def _in_order(root):
            if root:
                _in_order(root.left)
                results.append(root.pokemon)
                _in_order(root.right)
        _in_order(self.root)
        return results


name_tree = PokemonBinaryTree()
number_tree = PokemonBinaryTree()
type_tree = PokemonBinaryTree()

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

for pokemon in pokemon_list:
    name_tree.insert(pokemon["nombre"], pokemon)
    number_tree.insert(pokemon["numero"], pokemon)
    type_tree.insert(pokemon["tipo"], pokemon)


# b) 
print("b) Búsqueda de 'bul' en nombres:")
for pokemon in name_tree.search_by_proximity("bul"):
    print(pokemon)

# c) 
def show_pokemon_by_type(type_name):
    print(f"\nc) Pokémon de tipo '{type_name}':")
    for pokemon in type_tree.search_by_proximity(type_name):
        print(pokemon["nombre"])

show_pokemon_by_type("Agua")
show_pokemon_by_type("Fuego")
show_pokemon_by_type("Planta")
show_pokemon_by_type("Eléctrico")

# d) 
print("\nd) Pokémon ordenados por número y nombre:")
for pokemon in number_tree.in_order():
    print(f"{pokemon['nombre']} (Número: {pokemon['numero']})")

print("\nPokémon ordenados por nivel y nombre:")
for pokemon in name_tree.in_order():
    print(f"{pokemon['nombre']} (Nivel: {pokemon['nivel']})")

# e) 
print("\ne) Datos de Jolteon, Lycanroc y Tyrantrum:")
for name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
    result = name_tree.search_by_exact_key(name)
    if result:
        print(result)
    else:
        print(f"{name} no encontrado.")

# f) 
def count_by_type(type_name):
    return len(type_tree.search_by_proximity(type_name))

print("\nf) Cantidad de Pokémon de tipo 'Eléctrico':", count_by_type("Eléctrico"))
print("Cantidad de Pokémon de tipo 'Acero':", count_by_type("Acero"))

print("")
print("============================================= Punto dos =============================================")
print("")

# 2) Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:
# a) Dada vértice debe almacenar el nombre de un personaje, las aristas representan la
#   cantidad de episodios en los que aparecieron juntos ambos personajes que se
#   relacionan;
# b) Hallar el árbol de expansión mínimo y determinar si contiene a Yoda;
# c) Determinar cuál es el número máximo de episodios que comparten dos personajes, y quienes son.
# d) Cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO,
# Leia Rey, Rylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_character(self, name):
        if name not in self.adjacency_list:
            self.adjacency_list[name] = {}

    def add_episode(self, char1, char2, episodes):
        if char1 in self.adjacency_list and char2 in self.adjacency_list:
            self.adjacency_list[char1][char2] = episodes
            self.adjacency_list[char2][char1] = episodes

    def prim_mst(self):
        import heapq
        
        if not self.adjacency_list:
            return [], 0
        
        start_node = next(iter(self.adjacency_list))
        visited = set()
        min_heap = [(0, start_node, None)]
        mst = []
        total_weight = 0
        
        while min_heap:
            weight, current, related_character = heapq.heappop(min_heap)
            if current not in visited:
                visited.add(current)
                total_weight += weight
                if related_character is not None:
                    mst.append((weight, current, related_character))
                
                for neighbor, edge_weight in self.adjacency_list[current].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, neighbor, current))
        
        return mst, 'Yoda' in visited

    def max_episodes_shared(self):
        max_episodes = 0
        characters = (None, None)
        
        for char1 in self.adjacency_list:
            for char2, episodes in self.adjacency_list[char1].items():
                if episodes > max_episodes:
                    max_episodes = episodes
                    characters = (char1, char2)
        
        return characters, max_episodes


star_wars_graph = Graph()

# d)
characters = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for character in characters:
    star_wars_graph.add_character(character)


star_wars_graph.add_episode("Luke Skywalker", "Darth Vader", 5)
star_wars_graph.add_episode("Yoda", "Darth Vader", 3)
star_wars_graph.add_episode("Yoda", "Luke Skywalker", 4)
star_wars_graph.add_episode("Boba Fett", "Han Solo", 2)
star_wars_graph.add_episode("C-3PO", "R2-D2", 7)
star_wars_graph.add_episode("Leia", "Luke Skywalker", 6)
star_wars_graph.add_episode("Rey", "Kylo Ren", 4)
star_wars_graph.add_episode("Chewbacca", "Han Solo", 5)
star_wars_graph.add_episode("BB-8", "Rey", 3)

# b) 
mst, contains_yoda = star_wars_graph.prim_mst()
print("b) Árbol de expansión mínimo:")
for weight, character, related_character in mst:
    print(f"Personaje: {character}, Relacionado con: {related_character}, Peso: {weight}")
print("¿Contiene a Yoda?", contains_yoda)

# c) 
characters, max_shared = star_wars_graph.max_episodes_shared()
print(f"\nc) Máximo de episodios compartidos: {max_shared} entre {characters[0]} y {characters[1]}.")