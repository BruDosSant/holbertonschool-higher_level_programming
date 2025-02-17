#!/usr/bin/env python3
"""
improvisando parte 2
"""


import pickle


class CustomObject:
    """Clase personalizada con atributos serializables."""
    
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Muestra los atributos del objeto."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializa y guarda la instancia en un archivo."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Carga y deserializa un objeto desde un archivo."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Error during deserialization: {e}")
            return None
