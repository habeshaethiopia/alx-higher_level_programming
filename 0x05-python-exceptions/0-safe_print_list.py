#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    le = 0
    for a in my_list:
        le += 1
    try:

        if le < x:
            print(x)
            raise IndexError
        else:
            print(le)
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        pass
    finally:
        print()
