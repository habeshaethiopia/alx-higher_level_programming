#!/usr/bin/python3
"""the module doc"""
import sys
import os.path
arg = sys.argv[1:]
save_j = __import__('5-save_to_json_file').save_to_json_file
load_j = __import__('6-load_from_json_file').load_from_json_file


def main():
    """the main function"""
    str = []
    if os.path.exists('add_item.json'):
        str = load_j('add_item.json')
    save_j(str + arg, "add_item.json")


main()
