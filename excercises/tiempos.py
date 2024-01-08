import matplotlib.pyplot as plt
import numpy as np
import math

def plot_functions(start, end):
    n_values = np.arange(start, end + 1)

    # Funciones
    lg_n = np.log2(n_values)
    sqrt_n = np.sqrt(n_values)
    n = n_values
    n_log_n = n_values * np.log2(n_values)
    n_squared = n_values ** 2
    n_cubed = n_values ** 3
    two_power_n = 2 ** n_values
    n_factorial = [math.factorial(i) for i in n_values]

    # Graficar
    plt.figure(figsize=(10, 10))  # Ajustar el tamaño de la figura
    plt.plot(n_values, lg_n, label='log(n)')
    plt.plot(n_values, sqrt_n, label='sqrt(n)')
    plt.plot(n_values, n, label='n')
    plt.plot(n_values, n_log_n, label='n*log(n)')
    plt.plot(n_values, n_squared, label='n^2')
    plt.plot(n_values, n_cubed, label='n^3')
    plt.plot(n_values, two_power_n, label='2^n')
    plt.plot(n_values, n_factorial, label='n!')

    # Añadir detalles
    plt.xlabel('n')
    plt.ylabel('Funciones')
    plt.title('Gráficas de funciones en diferentes escalas')
    plt.legend()
    plt.grid(True)
    plt.show()

# Pedir rango de valores
start_value = int(input("Ingrese el valor inicial del rango: "))
end_value = int(input("Ingrese el valor final del rango: "))

# Graficar las funciones en el rango dado
plot_functions(start_value, end_value)
