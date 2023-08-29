from pickle import FALSE
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
            if matrix[i][j] == 1:
                print(f"Relación definida para matriz[V{i}][V{j}]: {matrix[i][j]}")
                print("Son adyacentes")
            else:
                print(f"Relación definida para matriz[V{i}][V{j}]: {matrix[i][j]}")
                print("No son adyacentes")


def buscar_bucles(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        if i < col and matrix[i][i] == 1:
            print(f"Se forma bucle en [V{i}][V{i}]: {matrix[i][i]}")


def buscar_camino(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for vertex in range(row):
        connected_vertices = []
        for j in range(col):
            if matrix[vertex][j] == 1:
                connected_vertices.append(j)
        if len(connected_vertices) == 0:
            print(f"El vértice {vertex} no está conectado a ningún otro vértice.")
        else:
            print(f"El vértice {vertex} está conectado a los vértices: {connected_vertices}")


def dfs(vertex, matrix, visited):
    visited[vertex] = True
    row = len(matrix)
    for j in range(row):
        if matrix[vertex][j] == 1 and not visited[j]:
            dfs(j, matrix, visited)


def verificar_camino(matrix):
    row = len(matrix)
    col = len(matrix[0])
    visited = [False] * row
    dfs(0, matrix, visited)

    if all(visited):
        print("El grafo es conexo.")
    else:
        print("El grafo no es conexo.")


row = int(input("Ingrese el numero de filas (máximo 5): "))
col = int(input("Ingrese el numero de columnas (máximo 15): "))
if row > 5 or col > 15:
    while row > 5 or col > 15:
        row = int(input("Ingrese de nuevo el numero de filas (máximo 5): "))
        col = int(input("Ingrese de nuevo el numero de columnas (máximo 15): "))

matrix = creatematrix(row, col)
print("Matriz generada:")
for i in range(row):
    print(matrix[i])

if matrix:
    print("Relaciones definidas:")
    definirRelacion(matrix)
    buscar_bucles(matrix)
    print("MOSTRANDO Caminos entre vertices...")
    buscar_camino(matrix)
    print("Verificando Caminos...")
    verificar_camino(matrix)
else:
    print("La matriz está vacía y no se pueden definir relaciones ni buscar bucles.")
