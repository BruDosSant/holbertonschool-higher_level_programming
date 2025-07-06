#!/usr/bin/python3
"""
7-add_item.py
Adds all arguments to a Python list,
then saves them to a JSON file
"""


import sys
import json
from os.path import exists

# Copiar la función de 5-save_to_json_file.py
def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

# Copiar la función de 6-load_from_json_file.py
def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
