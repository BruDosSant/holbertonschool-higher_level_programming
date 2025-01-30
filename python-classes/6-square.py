#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


class Square:
    """A simple example class"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor que inicializa el tamaño y la posición del cuadrado."""
        self.size = size  # Usa el setter para validación
        self.position = position  # Usa el setter para validación

    @property
    def size(self):
        """Getter para obtener el tamaño del cuadrado."""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Setter para modificar el tamaño del cuadrado con validación."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        """Getter para obtener la posición del cuadrado."""
        return self._Square__position

    @position.setter
    def position(self, value):
        """Setter para modificar la posición del cuadrado con validación."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

    def area(self):
        """Método público que retorna el área del cuadrado."""
        return self._Square__size * self._Square__size

    def my_print(self):
        """
        Método público que imprime el cuadrado con el carácter '#' en
        la posición indicada.
        """
        if self.size == 0:
            print("")
            return

        # Imprimir líneas en blanco según la posición en y
        print("\n" * self.position[1], end="")

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
