#!/usr/bin/python3
"""the module doc"""
import json


def from_json_string(my_str):
    """form JSON to string"""
    str = json.loads(my_str)
    return str
