
def secuencia(palabra):
    if len(palabra) == 0:
        return palabra
    else:
        return palabra [-1] + secuencia(palabra[:-1])
print(secuencia("hola"))