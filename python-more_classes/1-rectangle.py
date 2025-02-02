#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


class Rectangle:
    """Clase que define un rectángulo con ancho y alto."""

    def __init__(self, width=0, height=0):
        """Inicializa el rectángulo con ancho y alto opcionales."""


        self.width = width   # Se validará a través del setter
        self.height = height # Se validará a través del setter

    @property
    def width(self):
        """Getter para obtener el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter para modificar el ancho con validaciones."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter para obtener la altura del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter para modificar la altura con validaciones."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
