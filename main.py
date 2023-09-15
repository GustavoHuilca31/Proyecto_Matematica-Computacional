import math

import tkinter as tk
from random import randint
import random

class GraphApp:
    def __init__(self, root):
        self.matrix = None
        self.root = root
        self.root.title("Graph Visualization")
        self.root.configure(bg="black")

        self.row_label = tk.Label(root, text="Número de Filas (máximo 5):", bg="black", fg="white")
        self.row_label.pack()
        self.row_entry = tk.Entry(root)
        self.row_entry.pack()

        self.col_label = tk.Label(root, text="Número de Columnas (máximo 15):", bg="black", fg="white")
        self.col_label.pack()
        self.col_entry = tk.Entry(root)
        self.col_entry.pack()

        self.create_button = tk.Button(root, text="Crear Matriz", command=self.create_matrix, bg="white", fg="black")
        self.create_button.pack()

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.node_radius = 20
        self.node_positions = {}


        self.matrix_text = tk.Text(root, height=10, width=30, bg="black", fg="white")
        self.matrix_text.pack()

        self.manual_matrix_button = tk.Button(root, text="Ingresar Matriz Manualmente",command=self.create_matrix_manual, bg="white", fg="black")
        self.manual_matrix_button.pack()

    def create_matrix(self):
        try:
            row = int(self.row_entry.get())
            col = int(self.col_entry.get())

            if row > 5:
                row = 5
                self.row_entry.delete(0, tk.END)
                self.row_entry.insert(0, "5")

            if col > 15:
                col = 15
                self.col_entry.delete(0, tk.END)
                self.col_entry.insert(0, "15")

            self.matrix = self.create_matrix_random(row, col)
            self.clear_canvas()
            self.draw_graph()
            self.display_matrix(self.matrix)

        except ValueError:
            self.clear_canvas()
            self.display_matrix([])  # Limpiar la matriz también
            self.canvas.create_text(250, 250, text="Ingrese números válidos para filas y columnas.", fill="red")

    def create_matrix_random(self, row, col):
        matrix = []
        for i in range(row):
            row_vals = []
            for j in range(col):
                value = random.randint(0, 1)
                row_vals.append(value)
            matrix.append(row_vals)
        return matrix

    def draw_graph(self):
        self.node_positions = {}

        if self.matrix:
            num_rows = len(self.matrix)
            num_cols = len(self.matrix[0])

            # Crear nodos para todos los vértices en la matriz
            for i in range(num_rows):
                x = randint(self.node_radius, self.canvas.winfo_width() - self.node_radius)
                y = randint(self.node_radius, self.canvas.winfo_height() - self.node_radius)
                self.node_positions[i] = (x, y)
                self.canvas.create_oval(x - self.node_radius, y - self.node_radius, x + self.node_radius,
                                        y + self.node_radius, outline="blue")

                # Agregar letras al centro de los nodos (A, B, C, ...)
                label = chr(ord('A') + i)
                self.canvas.create_text(x, y, text=label, fill="blue")

            # Dibujar relaciones basadas en la matriz
            for i in range(num_rows):
                for j in range(num_cols):
                    if self.matrix[i][j] == 1:
                        if i in self.node_positions and j in self.node_positions:
                            x1, y1 = self.node_positions[i]
                            x2, y2 = self.node_positions[j]

                            # Calcular el ángulo entre los nodos
                            angle = math.atan2(y2 - y1, x2 - x1)

                            # Verificar si es un bucle (apunta a sí mismo)
                            if i == j:
                                # Dibujar un círculo en lugar de una flecha
                                radius = self.node_radius * 0.8
                                self.canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius,
                                                        outline="black", width=2)
                            else:
                                # Ajustar las coordenadas de inicio y final para que las flechas salgan del borde del círculo
                                x1 += self.node_radius * math.cos(angle)
                                y1 += self.node_radius * math.sin(angle)
                                x2 -= self.node_radius * math.cos(angle)
                                y2 -= self.node_radius * math.sin(angle)
                                self.canvas.create_line(x1, y1, x2, y2, fill="black", arrow=tk.LAST)

    def create_matrix_manual(self):
        if self.matrix is not None:  # Verificar que self.matrix se haya inicializado
            # Crear una nueva ventana para que el usuario ingrese manualmente la matriz
            manual_matrix_window = tk.Toplevel(self.root)
            manual_matrix_window.title("Ingresar Matriz Manualmente")

            # Crear una cuadrícula de entrada de texto para la matriz
            manual_matrix_entries = []
            for i in range(len(self.matrix)):
                row_entries = []
                for j in range(len(self.matrix[0])):
                    entry = tk.Entry(manual_matrix_window, width=5)
                    entry.grid(row=i, column=j)
                    row_entries.append(entry)
                manual_matrix_entries.append(row_entries)

            # Agregar un botón para confirmar y guardar la matriz
            confirm_button = tk.Button(manual_matrix_window, text="Confirmar",
                                       command=lambda: self.save_manual_matrix(manual_matrix_entries,
                                                                               manual_matrix_window))
            confirm_button.grid(row=len(self.matrix), columnspan=len(self.matrix[0]))

    def save_manual_matrix(self, entries, window):
        try:
            manual_matrix = []
            for row in entries:
                row_values = []
                for entry in row:
                    value = int(entry.get())
                    row_values.append(value)
                manual_matrix.append(row_values)

            # Mostrar la matriz ingresada manualmente
            self.clear_canvas()
            self.matrix = manual_matrix
            self.draw_graph()
            self.display_matrix(self.matrix)

            # Cerrar la ventana de entrada manual
            window.destroy()

        except ValueError:
            # Manejar errores de entrada no válida si es necesario
            pass

    def display_matrix(self, matrix):
        self.matrix_text.delete(1.0, tk.END)
        matrix_str = "\n".join(" ".join(map(str, row)) for row in matrix)
        self.matrix_text.insert(tk.END, "Matriz de Adyacencia:\n" + matrix_str)

    def clear_canvas(self):
        self.canvas.delete("all")

def main():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
