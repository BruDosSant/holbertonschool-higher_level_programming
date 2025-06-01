#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


class MyList(list):
    """Clase que extiende list con un método para imprimir la lista ordenada"""

    def print_sorted(self):
        """Imprime la lista en orden ascendente sin modificar la original."""

        print(sorted(self))
