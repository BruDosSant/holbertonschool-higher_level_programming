#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Clase abstracta que representa a un animal.

    Esta clase define el método abstracto 'sound', que debe ser implementado 
    por las subclases para devolver el sonido característico de cada animal.
    """
    
    @abstractmethod
    def sound(self):
        """Este método debe ser implementado por las subclases
        para retornar el sonido característico del animal."""
        pass

class Dog(Animal):
    """
    Clase que representa a un perro, que es un tipo de Animal.

    Implementa el método 'sound' para devolver el sonido característico de un perro.
    """
    
    def sound(self):
        """Devuelve el sonido característico del perro."""
        return "Bark"

class Cat(Animal):
    """
    Clase que representa a un gato, que es un tipo de Animal.

    Implementa el método 'sound' para devolver el sonido característico de un gato.
    """
    
    def sound(self):
        """Devuelve el sonido característico del gato."""
        return "Meow"
