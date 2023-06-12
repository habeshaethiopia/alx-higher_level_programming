#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return None
    if idx > len(my_list)-1 or idx < 0:
        return my_list
    li = my_list[:]
    li.remove(my_list[idx])
    return li
