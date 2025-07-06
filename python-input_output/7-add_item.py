#!/usr/bin/python3
"""
7-add_item.py
Adds all arguments to a Python list,
then saves them to a JSON file
"""


import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Intentar cargar el archivo si existe
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Agregar los nuevos argumentos
items.extend(sys.argv[1:])

# Guardar la lista actualizada
save_to_json_file(items, filename)
