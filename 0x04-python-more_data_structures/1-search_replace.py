#!/usr/bin/python3
def search_replace(my_list, search, replace):
    List = my_list[:]
    for i in range(len(List)):
        if List[i] == search:
            List[i] = replace
    return List
