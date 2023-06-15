#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    re = []
    for i in set_2:
        for j in set_1:
            if i != j:
                if i not in re:
                    re.append(i)
                if j not in re:
                    re.append(j)
    return re
