#!/usr/bin/python3
""" Amodule containing a function called text_indentation """


def text_indentation(text):
    """  function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    delimiter = [".", "?", ":"]
    new_line = 0
    for c in text:
        if c in delimiter:
            print(c, end="\n\n")
            new_line = 1
        else:
            if new_line == 1 and (c == " " or c == "\t"):
                pass
            else:
                print(c, end="")
                new_line = 0
