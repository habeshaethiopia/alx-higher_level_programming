#!/usr/bin/python3
""" Amodule containing a function called text_indentation """


def text_indentation(text):
    """  function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    delimiter = [".", "?", ":"]
    for c in text:
        if c in delimiter:
            print()
            print()
        print(c, end="")
