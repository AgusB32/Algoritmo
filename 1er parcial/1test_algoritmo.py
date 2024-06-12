# 1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos.
vector = ['perro', 'gato', 'caballo', 'vaca', 'lobo']
print(vector)
print(" ")
def inverso(list):
    if not list:
        return
    else:
        inverso(list[1:])
        print(list[0],end= " ")

inverso(vector)

print(" ")
print(" ")


# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

from pila import Stack

def contar_unicos(pila, key):
    elementos_unicos = []
    pila_temp = Stack()
    
    while pila.size() > 0:
        elemento = pila.pop()
        if elemento[key] not in elementos_unicos:
            elementos_unicos.append(elemento[key])
        pila_temp.push(elemento)
    
    while pila_temp.size() > 0:
        pila.push(pila_temp.pop())
    
    return len(elementos_unicos)

# a) 
pila_dinosaurios = Stack()
for dino in dinosaurios:
    pila_dinosaurios.push(dino)

cantidad_especies = contar_unicos(pila_dinosaurios, "especie")
print("Cantidad de especies:", cantidad_especies)

print(" ")

# b) 
cantidad_descubridores = contar_unicos(pila_dinosaurios, "descubridor")
print("Cantidad de descubridores distintos:", cantidad_descubridores)

print(" ")

# c) 
print("Dinosaurios que empiezan con T:")
pila_dinosaurios_temp = Stack()
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    if dino["nombre"].startswith("T"):
        print(dino["nombre"])
    pila_dinosaurios_temp.push(dino)

while pila_dinosaurios_temp.size() > 0:
    pila_dinosaurios.push(pila_dinosaurios_temp.pop())

print(" ")

# d) 
print("Dinosaurios que pesan menos de 275 Kg:")
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    peso_kg = int(dino["peso"].split()[0])
    if peso_kg < 275:
        print(dino["nombre"])
    pila_dinosaurios_temp.push(dino)

while pila_dinosaurios_temp.size() > 0:
    pila_dinosaurios.push(pila_dinosaurios_temp.pop())

print(" ")

# e) 
pila_aparte = Stack()
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    if dino["nombre"].startswith(("A", "Q", "S")):
        pila_aparte.push(dino)
    pila_dinosaurios_temp.push(dino)

while pila_dinosaurios_temp.size() > 0:
    pila_dinosaurios.push(pila_dinosaurios_temp.pop())

print("Dinosaurios en la pila aparte que comienzan con A, Q, S:")
while pila_aparte.size() > 0:
    dino = pila_aparte.pop()
    print(dino["nombre"])

print(" ")


# 3. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie. implementar las funciones
# necesarias para resolver las actividades enumeradas a continuación:
# a) listado ordenado por nombre y por especie;
# b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d) mostrar los Jedi de especie humana y twi'lek;
# e) listar todos los Jedi que comienzan con A;
# f) mostrar los Jedi que usaron sable de luz de más de un color;
# g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
# i) Mostrar todos los Jedi que tengan el ranking de Grand Master.

from lista import search

jedis = [
    {
        "name": "Qui-Gon Jinn",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Tera Sinube/Count Dooku",
        "lightsaber_color": "Green",
        "homeworld": "Coruscant",
        "birth_year": "79ABY",
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Obi-Wan Kenobi",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Qui-Gon Jinn/Yoda",
        "lightsaber_color": "Blue",
        "homeworld": "Stewjon",
        "birth_year": "57ABY",
        "height": 1.82,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Anakin Skywalker/Darth Vader",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Obi-Wan Kenobi",
        "lightsaber_color": "Blue",
        "homeworld": "Tatooine",
        "birth_year": "41ABY",
        "height": 1.88,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Quinlan Vos",
        "rank": "Jedi Master",
        "species": "Human/Kiffar",
        "master": "Tholme",
        "lightsaber_color": "Green",
        "homeworld": "Kiffu",
        "birth_year": "59ABY",
        "height": 1.91,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Yoda",
        "rank": "Grand Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "896ABY",
        "height": 0.66,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Mace Windu",
        "rank": "Jedi Master/Master of the Order",
        "species": "Human",
        "master": "Cyslin Myr",
        "lightsaber_color": "Purple",
        "homeworld": "Haruun Kal",
        "birth_year": "72ABY",
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ki-Adi-Mundi",
        "rank": "Jedi Master",
        "species": "Cerean",
        "master": None,
        "lightsaber_color": "Purple/Blue",
        "homeworld": "Cerea",
        "birth_year": "92ABY",
        "height": 1.98,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Plo Koon",
        "rank": "Jedi Master",
        "species": "Kel Dor",
        "master": None,
        "lightsaber_color": "Yellow/Blue/Orange",
        "homeworld": "Dorin",
        "birth_year": "71ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Saesee Tiin",
        "rank": "Jedi Master",
        "species": "Iktotchi",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Iktotch",
        "birth_year": None,
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yaddle",
        "rank": "Jedi Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "509AYB",
        "height": 0.61,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Even Piell",
        "rank": "Jedi Master",
        "species": "Lannik",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Lannik",
        "birth_year": None,
        "height": 1.22,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Oppo Rancisis",
        "rank": "Jedi Master",
        "species": "Thisspiasian",
        "master": "Yaddle",
        "lightsaber_color": "Green",
        "homeworld": "Thisspias",
        "birth_year": "206ABY",
        "height": 1.38,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Adi Gallia",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.84,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yarael Poof",
        "rank": "Jedi Master",
        "species": "Quermian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Quermia",
        "birth_year": None,
        "height": 2.64,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Eeth Koth",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Iridonia",
        "birth_year": None,
        "height": 1.71,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Depa Billaba",
        "rank": "Jedi Master",
        "species": "Chalactan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Chalacta",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kit Fisto",
        "rank": "Jedi Master",
        "species": "Nautolan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Glee Anselm",
        "birth_year": None,
        "height": 1.96,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luminara Unduli",
        "rank": "Jedi Master",
        "species": "Mirialan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mirial",
        "birth_year": "58ABY",
        "height": 1.76,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Barriss Offee",
        "rank": "Padawan",
        "species": "Mirialan",
        "master": "Luminara Unduli",
        "lightsaber_color": "Blue",
        "homeworld": "Mirial",
        "birth_year": "40ABY",
        "height": 1.66,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Shaak Ti",
        "rank": "Jedi Master",
        "species": "Togruta",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Shili",
        "birth_year": None,
        "height": 1.87,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Coleman Trebor",
        "rank": "Jedi Master",
        "species": "Vurk",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Sembla",
        "birth_year": None,
        "height": 2.13,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Jocasta Nu",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.69,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Aayla Secura",
        "rank": "Jedi Knight",
        "species": "Twi'lek",
        "master": "Quinlan Vos",
        "lightsaber_color": "Blue",
        "homeworld": "Ryloth",
        "birth_year": "47ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Sifo-Dyas",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mundos Cassandranos",
        "birth_year": "75ABY",
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Count Dooku",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Yoda",
        "lightsaber_color": "Blue/Red",
        "homeworld": "Serenno",
        "birth_year": "102ABY",
        "height": 1.93,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Pablo-Jill",
        "rank": "Jedi Knight",
        "species": None,
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cúmulo Estelar Skustell",
        "birth_year": None,
        "height": 1.60,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bultar Swan",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Plo Koon",
        "lightsaber_color": "Green",
        "homeworld": "Kuat",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Agen Kolar",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Stass Allie",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Tholoth",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ahsoka Tano",
        "rank": "Padawan",
        "species": "Togruta",
        "master": "Anakin Skywalker",
        "lightsaber_color": "Green/Yellow/Blue/White",
        "homeworld": "Shili",
        "birth_year": "36ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Asajj Ventress",
        "rank": "Padawan",
        "species": "Dathomirian",
        "master": "Ky Narec",
        "lightsaber_color": "Yellow/Red",
        "homeworld": "Dathomir",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Ima-Gun Di",
        "rank": "Jedi Master",
        "species": "Nikto",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Nahdar Vebb",
        "rank": "Jedi Knight",
        "species": "Mon Calamari",
        "master": "Kit Fisto",
        "lightsaber_color": "Blue",
        "homeworld": "Dac",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bolla Ropal",
        "rank": "Jedi Master",
        "species": "Rodian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Rodia",
        "birth_year": None,
        "height": 1.75,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ord Enisence",
        "rank": "Jedi Master",
        "species": "Skrilling",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Agrimundo-2079",
        "birth_year": None,
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tera Sinube",
        "rank": "Jedi Master",
        "species": "Cosian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cosia",
        "birth_year": "102ABY",
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ky Narec",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Pong Krell",
        "rank": "Jedi Master",
        "species": "Besalisk",
        "master": None,
        "lightsaber_color": "Blue/Green",
        "homeworld": "Ojom",
        "birth_year": None,
        "height": 2.36,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Coleman Kcaj",
        "rank": "Jedi Master",
        "species": "Ongree",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Skustell",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplar",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplee",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tu-Anh",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": None,
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kanan Jarrus",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Depa Billaba",
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": "33ABY",
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ezra Bridger",
        "rank": "Padawan",
        "species": "Human",
        "master": "Kanan Jarrus",
        "lightsaber_color": "Blue",
        "homeworld": "Lothal",
        "birth_year": "19ABY",
        "height": 1.65,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luke Skywalker",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Obi-Wan Kenobi/Yoda",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Tatooine",
        "birth_year": "19ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Leia Organa",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Blue",
        "homeworld": "Alderaan",
        "birth_year": "19ABY",
        "height": 1.50,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ben Solo/Kylo Ren",
        "rank": "Padawan",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Chandrila",
        "birth_year": "5DBY",
        "height": 1.89,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Rey Skywalker",
        "rank": "Jedi Sentinel",
        "species": "Human",
        "master": "Luke Skywalker/Leia Organa",
        "lightsaber_color": "Blue/Green/Yellow",
        "homeworld": "Jakku",
        "birth_year": "15DYB",
        "height": 1.70,
        "to_darkside": None,
        "come_lightside": None
    }
 ]

# a) 
def comparar_jedi(jedi1, jedi2):
    if jedi1['name'] == jedi2['name']:
        if jedi1['species'] is None:
            return 1
        elif jedi2['species'] is None:
            return -1
        else:
            return jedi1['species'] > jedi2['species']
    else:
        return jedi1['name'] > jedi2['name']

def ordenar_jedi(jedis):
    ordenar_jedis = []
    jedis_copy = jedis.copy()
    while jedis_copy:
        _jedi = jedis_copy[0]
        for jedi in jedis_copy:
            if comparar_jedi(jedi, _jedi) < 0:
                _jedi = jedi
        jedis_copy.remove(_jedi)
        ordenar_jedis.append(_jedi)
    return ordenar_jedis

ordenar_jedis = ordenar_jedi(jedis)

for jedi in ordenar_jedis:
    print(f"Nombre: {jedi['name']}, Especie: {jedi['species']}")

print(" ")

# b)
jedi_nombres = ['Ahsoka Tano', 'Kit Fisto']

def info_de_x(jedis, jedi_nombres):
    for name in jedi_nombres:
        jedi_info = next((jedi for jedi in jedis if jedi["name"] == name), None)
        if jedi_info:
            print("Información de: ", name)
            for key, value in jedi_info.items():
                print(f"{key}: {value}")
            print()

info_de_x(jedis, jedi_nombres)

print(" ")

# c) 
def padawans_aprendices(jedis, masters):
    padawan_list = []
    for master in masters:
        for jedi in jedis:
            if jedi['master'] == master:
                padawan_list.append(jedi['name'])
    return padawan_list

masters = ['Yoda', 'Luke Skywalker']

padawan_list = padawans_aprendices(jedis, masters)

print("Los Padawan(aprendices) de Yoda y de Luke Skywalker son:")
for padawan in padawan_list:
    print(padawan)

print(" ")

# d) 
def buscar_jedi(jedis, especies):
    jedi_list = []
    for jedi in jedis:
        if jedi['species'] in especies:
            jedi_list.append(jedi)
    return jedi_list

especies_a_buscar = ['Human', "Twi'lek"]

jedi_list = buscar_jedi(jedis, especies_a_buscar)

print("Los Jedi de especie humana y Twi'lek son:")
for jedi in jedi_list:
    print(jedi['name'], "-", jedi['species'])

print(" ")

# e)
def filtrar_nombre(jedis, letra):
    filtrar_jedis = []
    for jedi in jedis:
        if jedi['name'].lower().startswith(letra.lower()):
            filtrar_jedis.append(jedi)
    return filtrar_jedis

def mostrar_jedi_con_A(jedis):
    print("Los Jedis que empiezan con A son:")
    for jedi in jedis:
        print(f"Name: {jedi['name']}")

jedis_con_A = filtrar_nombre(jedis, 'A')
mostrar_jedi_con_A(jedis_con_A)

print(" ")

# f) 
def jedi_muchos_colores(jedis):
    jedi_colorido = []
    for jedi in jedis:
        if jedi['lightsaber_color'] and '/' in jedi['lightsaber_color']:
            jedi_colorido.append(jedi)
    return jedi_colorido

def mostrar_jedis(jedis):
    print("Los Jedis que usaron sable de luz de más de un color son:")
    for jedi in jedis:
        print(f"Name: {jedi['name']}, Lightsaber Colors: {jedi['lightsaber_color']}")

jedis_multiples_colores = jedi_muchos_colores(jedis)
mostrar_jedis(jedis_multiples_colores)

print("")

# g) 
def jedi_amarillo_violeta(jedis):
    resultado = []
    for jedi in jedis:
        if jedi['lightsaber_color'] and ("Yellow" in jedi['lightsaber_color'] or "Purple" in jedi['lightsaber_color']):
            resultado.append(jedi['name'])
    return resultado

jedi_sables_especiales = jedi_amarillo_violeta(jedis)

print("Los Jedi que utilizaron sable de luz amarillo o violeta son:")
for jedi in jedi_sables_especiales:
    print(jedi)

print(" ")

# h) 
def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

def encontrar_padawans(jedis, masters):
    padawans = []
    for jedi in jedis:
        jedi_masters = jedi['master'] if jedi['master'] else []
        for master in masters:
            if master in jedi_masters:
                padawans.append(jedi['name'])
                break
    return padawans

masters_to_find = ["Qui-Gon Jinn", "Mace Windu"]
padawans = encontrar_padawans(jedis, masters_to_find)

print("Los Padawans de Qui-Gon Jinn y Mace Windu son:")
for padawan in padawans:
    print(padawan)

print("")

# i) 
def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index
    return None

def gran_master_rank(jedis, rank):
    grand_masters = []
    for jedi in jedis:
        if search([jedi], 'rank', rank) is not None:
            grand_masters.append(jedi)
    return grand_masters

rank_to_find = "Grand Master"
grand_masters = gran_master_rank(jedis, rank_to_find)

print("Los Jedi con el ranking de Grand Master son:")
for jedi in grand_masters:
    print(jedi['name'])
