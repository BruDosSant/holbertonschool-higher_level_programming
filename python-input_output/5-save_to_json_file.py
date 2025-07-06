#!/usr/bin/python3
"""
increible
"""


import json


def save_to_json_file(my_obj, filename):
    """epectacular"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
