import matplotlib.pyplot as plt
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

eje_x = []
eje_y = []

# Marcar el tiempo de inicio
start_time = time.time()

for i in range(15000):
    print(f"El tiempo algorítmico de ejecución para {i+1} elementos es de {block_1(i+1)}")
    eje_x.append(i)
    eje_y.append(block_1(i+1))

# Marcar el tiempo de finalización
end_time = time.time()

# Calcular la duración total
elapsed_time = end_time - start_time

# Imprimir el tiempo de ejecución total
print(f"Tiempo de ejecución total: {elapsed_time:.6f} segundos")

# Graficar los datos
plt.plot(eje_x, eje_y, marker='o', linestyle='-')
plt.title('Gráfico de Datos')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.show()

print(f"Pull")