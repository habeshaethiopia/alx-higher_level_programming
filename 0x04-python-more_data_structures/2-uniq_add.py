#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in my_list:
        f = 0
        for j in my_list:
            if i == j:
                f += 1
        if f == 1:
            sum += i
    return sum
