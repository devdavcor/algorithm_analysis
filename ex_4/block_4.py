# Inicializar variables
x = 0
cont = 1
n = 5  # Puedes ajustar este valor según tus necesidades
a = [1, 2, 3, 4, 5]  # Puedes ajustar los elementos de la lista según tus necesidades
b = [6, 7, 8, 9, 10]  # Puedes ajustar los elementos de la lista según tus necesidades

while True:
    x = x + a[cont - 1]
    x = x + b[cont - 1]
    cont = cont + 1

    if cont > n:
        break

print("El valor final de x es:", x)
