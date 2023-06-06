#!/usr/bin/python3
def uppercase(str):
    st = str.lower()
    for c in st:
        print("{}".format(chr(ord(c)-32)), end="")
    print()
