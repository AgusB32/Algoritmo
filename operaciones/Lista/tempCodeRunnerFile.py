numeros = [22, 11, 30, 7, 13, 1]
print("Lista original", numeros)
def primo(numero):
    if numero <=1:
        return False
    if numero <=3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i+2) == 0:
            return False
        i += 6
    return True
sin_primos = [numero for numero in numeros if not primo(numero)]
print("Lista sin primos", sin_primos)