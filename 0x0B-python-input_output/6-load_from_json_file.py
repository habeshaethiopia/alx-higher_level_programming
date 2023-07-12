#!/usr/bin/python3
"""the module doc"""
import json


def load_from_json_file(filename):
    """json read"""
    with open(filename) as f:
        return json.load(f)
