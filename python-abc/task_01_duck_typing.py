from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Clase abstracta que representa una forma geométrica.
    
    Define dos métodos abstractos: 'area' y 'perimeter', 
    que deben ser implementados por las subclases.
    """

    @abstractmethod
    def area(self):
        """Método abstracto que calcula el área de la forma."""
        pass

    @abstractmethod
    def perimeter(self):
        """Método abstracto que calcula el perímetro de la forma."""
        pass

import math

class Circle(Shape):
    """
    Representa un círculo.
    
    La clase Circle implementa los métodos 'area' y 'perimeter' 
    para calcular el área y el perímetro del círculo.
    """
    
    def __init__(self, radius):
        if radius < 0:
            self.__radius = abs(radius)
        else:
            self.__radius = radius
    
    def area(self):
        """Calcula el área del círculo."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calcula el perímetro del círculo."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Representa un rectángulo.
    
    La clase Rectangle implementa los métodos 'area' y 'perimeter' 
    para calcular el área y el perímetro del rectángulo.
    """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Imprime el área y el perímetro de una forma (Shape).
    
    Esta función utiliza duck typing, por lo que no verifica el tipo del objeto,
    sino que confía en que el objeto tiene los métodos 'area' y 'perimeter'.
    """
    print(f"Área: {shape.area()}")
    print(f"Perímetro: {shape.perimeter()}")
