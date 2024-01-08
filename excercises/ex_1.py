# Algoritmo de Ordenamiento por Inserción en Python

def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        print(A)
        #print(f"----------Iteracion {j}----------")
        key = A[j]
        i = j - 1
        #print(f"El indice j es {j} y el indice i es de {i}")
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
            #print(f"El indice j es {j} y el indice i es de {i}")
        A[i + 1] = key
        #print(f"El indice j es {j} y el indice i es de {i}")

# Uso del algoritmo con un ejemplo
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Arreglo ordenado:", arr)
