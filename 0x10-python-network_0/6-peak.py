#!/usr/bin/python3
"""the technical interview preparation"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers:
        highest = list_of_integers[0]
    else:
        return None
    for i in list_of_integers:
        if i > highest:
            highest = i
    return highest


if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
