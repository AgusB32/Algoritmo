# Dada una secuencia de caracteres, obtener dicha secuencia invertida.
def invertir(palabra):
    if len(palabra) == 0:
        return palabra
    else:
        return palabra[-1] + invertir(palabra[:-1])

palabra = input("Ingrese la palabra que desea invertir: ")
res = invertir(palabra)
print(f"La palabra invertida es: {res}")