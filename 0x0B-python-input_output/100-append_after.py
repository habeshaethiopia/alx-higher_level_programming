#!/usr/bin/python3
"""the module doc"""


def append_after(filename="", search_string="", new_string=""):
    """Append after the string"""
    with open(filename)as f:
        Data = f.readlines()
    new_data = ""
    for line in Data:
        new_data = new_data + line
        if search_string in line:
            new_data = new_data + new_string
    with open(filename, "w") as f:
        f.write(new_data)
