#!/usr/bin/env python3
"""
improvisando 4 el final de la improvisacion
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializa un diccionario a un archivo XML."""
    # Crear el elemento raíz
    root = ET.Element("data")
    
    # Iterar sobre los elementos del diccionario y añadirlos al XML
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convertir a cadena de texto si es necesario
    
    # Crear un árbol XML y guardarlo en el archivo
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Deserializa un archivo XML a un diccionario de Python."""
    # Parsear el archivo XML
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Construir el diccionario a partir de los elementos XML
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
        # Asignar el texto del elemento al diccionario
    
    return dictionary
