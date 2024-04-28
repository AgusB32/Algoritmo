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