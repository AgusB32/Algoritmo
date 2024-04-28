def binario(numero):
    if numero==1:
        return str(1)
    else:
        return binario(numero//2) + str(numero%2)
print (binario(7))