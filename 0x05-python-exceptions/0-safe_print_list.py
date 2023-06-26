#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    for a in my_list:
        len += 1
    try:
        print(len(my_list))
        if len < x:
            raise IndexError
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        pass
    finally:
        print()
