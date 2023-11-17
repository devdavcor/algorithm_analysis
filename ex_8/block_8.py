def buscar_valor(valor, A, n):
    i = 1
    while i <= n and A[i] != valor:
        i += 1
    return i

# Ejemplo de uso
valor_a_buscar = 42  # Puedes ajustar este valor según tus necesidades
A = [10, 20, 30, 42, 50]  # Puedes ajustar los elementos de la lista según tus necesidades
n = len(A)

resultado = buscar_valor(valor_a_buscar, A, n)
print(f"El índice del valor {valor_a_buscar} en la lista es: {resultado}")
