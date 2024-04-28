# n^m = n * (n, m-1)
def funcion (base,exp):
    if exp == 0:
        return 1
    else:
        return base * funcion(base, exp - 1)
print (funcion(2,5))