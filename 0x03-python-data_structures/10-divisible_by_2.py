#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divB2 = []
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i % 2 == 0:
            divB2.append(True)
        else:
            divB2.append(False)
    return divB2
