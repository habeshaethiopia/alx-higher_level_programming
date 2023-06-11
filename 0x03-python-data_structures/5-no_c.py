#!/usr/bin/python3
def no_c(my_string):
    str = my_string[:]
    for i in range(len(str)):
        if str[i] == "c" or str[i] == "C":
            str[i] = ""
    return str
