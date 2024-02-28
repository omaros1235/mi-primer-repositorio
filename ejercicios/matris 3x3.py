# Definir una matriz bidimensional de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimir la matriz
print("Matriz original:")
for fila in matriz:
    print(fila)

# Modificar un valor en la matriz (por ejemplo, cambiar el valor en la segunda fila y tercera columna)
matriz[1][2] = 10

# Imprimir la matriz después de la modificación
print("\nMatriz modificada:")
for fila in matriz:
    print(fila)