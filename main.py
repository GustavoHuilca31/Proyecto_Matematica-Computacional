import random

def creatematrix(row, col):
    matrix = []
    for i in range(row):
        row_vals = []
        for j in range(col):
            value = random.randint(0, 1) 
            row_vals.append(value)
        matrix.append(row_vals)
    return matrix

def definirRelacion(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            print(f"Relación definida para matriz[{i}][{j}]: {matrix[i][j]}")
            if matrix[i][j] == 1:
                print("Son adyacentes")
            else:
                print("No son adyacentes")

def buscar_bucles(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if i == j and matrix[i][j]==1:
                print(f"Se forma bucle en [{i}][{j}]: {matrix[i][j]}")

row = int(input("Ingrese el numero de filas: "))
col = int(input("Ingrese el numero de columnas: "))
matrix = creatematrix(row, col)
print("Matriz generada:")
for i in range(row):
    print(matrix[i])

print("Relaciones definidas:")
definirRelacion(matrix)
buscar_bucles(matrix)