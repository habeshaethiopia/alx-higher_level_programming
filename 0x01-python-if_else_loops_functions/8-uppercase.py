#!/usr/bin/python3
def uppercase(str):
    st = str.lower()
    for c in st:
        if c.isalpha():
            c = chr(ord(c)-32)
        print("{}".format(c), end="")
    print()
