#!/usr/bin/python3
"""
increible
"""


def pascal_triangle(n):
    """increible"""
    if n <= 0:
        return []

    triangle = [[1]]  # Primera fila

    for i in range(1, n):
        prev_row = triangle[-1]  # Última fila generada
        new_row = [1]  # Comienza con 1

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
            # Suma de los de arriba

        new_row.append(1)  # Termina con 1
        triangle.append(new_row)  # Agrega la nueva fila

    return triangle
