#!/usr/bin/env python3
"""
improvisando
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializa un diccionario en formato JSON y lo guarda en un archivo.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """
    Carga y deserializa un archivo JSON, retornando un diccionario de Python.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
