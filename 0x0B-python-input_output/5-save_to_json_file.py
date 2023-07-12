#!/usr/bin/python3
"""the module doc"""
import json


def save_to_json_file(my_obj, filename):
    """the file .json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
