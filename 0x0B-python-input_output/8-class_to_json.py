#!/usr/bin/python3
"""the module doc"""
import json


def class_to_json(obj):
    """the class to json"""
    return json.dumps(obj.__dict__)
