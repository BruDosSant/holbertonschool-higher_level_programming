#!/usr/bin/python3
"""
increible
"""


import json


def load_from_json_file(filename):
    """epectacular"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
