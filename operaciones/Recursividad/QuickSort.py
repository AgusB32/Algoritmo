def quick_sort(lista, inicio, fin):
  if inicio < fin:
    pi = partition(lista, inicio, fin)
    quick_sort(lista, inicio, pi - 1)
    quick_sort(lista, pi + 1, fin)

def partition(lista, inicio, fin):  
  pivot = lista[fin]
  i = inicio - 1

  for j in range(inicio, fin):
    if lista[j] <= pivot:
      i = i + 1
      (lista[i], lista[j]) = (lista[j], lista[i])
  (lista[i + 1], lista[fin]) = (lista[fin], lista[i + 1])
  return i + 1

lista = [4,6,2,5,8,9,5,10]
print(lista)
quick_sort(lista, 0, len(lista)-1)
print(lista)