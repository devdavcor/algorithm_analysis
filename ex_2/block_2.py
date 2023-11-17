import random

# Solicitar al usuario la cantidad de elementos
N = int(input("Ingrese la cantidad de elementos en la lista: "))

# Crear una lista con N elementos aleatorios
lista = [random.randint(1, 100) for _ in range(N)]

# Imprimir elementos en consola
for elemento in lista:
    print(elemento)
