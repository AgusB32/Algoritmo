# 29 Desarrollar una función recursiva que permita calcular el método de la bisección de una función f(x).
def f(x):
    return x**3 - x - 2

def biseccion(f, a, b, tol):
    c = (a + b) / 2.0

    if abs(f(c)) < tol:
        return c

    if f(a) * f(c) < 0:
        return biseccion(f, a, c, tol)
    else:
        return biseccion(f, c, b, tol)

a = 1
b = 2
tol = 1e-5

raiz = biseccion(f, a, b, tol)
print(f"La raíz encontrada es: {raiz}")