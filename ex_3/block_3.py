def funcion(N):
    if N == 0:
        return 1
    else:
        return N * funcion(N - 1)

# Ejemplo de uso
N = int(input("Ingrese un número para calcular el producto: "))
resultado = funcion(N)
print(f"El producto de todos los números enteros positivos desde 0 hasta {N} es: {resultado}")
