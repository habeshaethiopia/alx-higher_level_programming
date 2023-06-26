#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(len(my_list))
        for i in my_list:
            print(i, end="")
    except IndexError:
        pass
    finally:
        print()
