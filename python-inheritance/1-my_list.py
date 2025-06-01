#!/usr/bin/python3
"""
1-my_list.py
Esta es una clase que extiende la clase list de Python.
"""


class MyList(list):
    """Clase que extiende list con un método para imprimir la lista ordenada"""

    def print_sorted(self):
        """Imprime la lista en orden ascendente sin modificar la original."""

        print(sorted(self))
