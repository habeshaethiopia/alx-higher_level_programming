#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    le = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception:
            break
        le += 1
    print()
    return le
