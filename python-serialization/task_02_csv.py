#!/usr/bin/env python3
"""
Improvisando parte 3
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Convierte un archivo CSV a JSON y guarda el resultado en data.json"""
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            # Usamos DictReader para leer el CSV como diccionarios
            csv_reader = csv.DictReader(csv_file)
            
            # Convertir cada fila del CSV en un diccionario
            data = [row for row in csv_reader]
            
            # Serializar la lista de diccionarios a JSON
            with open('data.json', mode='w') as json_file:
                json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        print(f"Error: El archivo {csv_filename} no fue encontrado.")
        return False
    except Exception as e:
        print(f"Error durante la conversión: {e}")
        return False
