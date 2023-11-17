import matplotlib.pyplot as plt
import threading
import time


def block_1(N):
    tempo = 0
    for i in range(N):
        j = 1
        tempo += 1
        while j < N:
            # print(j)
            j = j * 2
            tempo += 1
    return tempo


def plot_data(x, y):
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title('Gráfico de Datos')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
    plt.show()


def calculate_and_plot(start, end):
    eje_x = []
    eje_y = []

    # Marcar el tiempo de inicio
    start_time = time.time()

    for i in range(start, end):
        print(f"El tiempo algorítmico de ejecución para {i + 1} elementos es de {block_1(i + 1)}")
        eje_x.append(i)
        eje_y.append(block_1(i + 1))

    # Marcar el tiempo de finalización
    end_time = time.time()

    # Calcular la duración total
    elapsed_time = end_time - start_time

    # Imprimir el resultado y el tiempo de ejecución
    print(f"Tiempo de ejecución total: {elapsed_time:.6f} segundos")

    # Graficar los datos
    plot_data(eje_x, eje_y)


# Establecer el rango de tamaños de entrada
inicio = 1
fin = 15000

# Crear un hilo para realizar la ejecución y representación en segundo plano
thread = threading.Thread(target=calculate_and_plot, args=(inicio, fin))

# Iniciar el hilo
thread.start()

# El programa principal puede continuar ejecutándose mientras el hilo trabaja en segundo plano
print("El programa principal continúa ejecutándose...")
