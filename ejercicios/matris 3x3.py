def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def ordenar_fila(matriz, fila):
    # Seleccionamos la fila específica y la ordenamos utilizando Selection Sort
    n = len(matriz[0])
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if matriz[fila][j] < matriz[fila][min_index]:
                min_index = j
        matriz[fila][i], matriz[fila][min_index] = matriz[fila][min_index], matriz[fila][i]

# Matriz bidimensional de 3x3
matriz = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]

# Imprimimos la matriz original
print("Matriz Original:")
imprimir_matriz(matriz)

# Ordenamos la segunda fila (índice 1) utilizando Selection Sort
ordenar_fila(matriz, 1)

# Imprimimos la matriz después de ordenar la segunda fila
print("\nMatriz Después de Ordenar la Segunda Fila:")
imprimir_matriz(matriz)
