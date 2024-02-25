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

# Acceder a elementos específicos de la matriz
elemento = matriz[1][2]
print("\nElemento en la segunda fila y tercera columna:", elemento)

# Modificar un valor en la matriz
matriz[0][0] = 10
print("\nMatriz después de modificar el primer elemento:")
for fila in matriz:
    print(fila)