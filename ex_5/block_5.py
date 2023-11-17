def suma_arreglo(arreglo):
    suma = 0
    for elemento in arreglo:
        suma += elemento
    return suma

# Solicitar al usuario la longitud del arreglo
N = int(input("Ingrese la longitud del arreglo: "))

# Crear un arreglo y llenarlo automáticamente con valores aleatorios (puedes ajustar esto según tus necesidades)
import random
arreglo = [random.randint(1, 100) for _ in range(N)]

# Mostrar el arreglo
print("Arreglo generado:", arreglo)

# Calcular y mostrar la suma de los elementos del arreglo
resultado = suma_arreglo(arreglo)
print(f"La suma de los elementos del arreglo es: {resultado}")
