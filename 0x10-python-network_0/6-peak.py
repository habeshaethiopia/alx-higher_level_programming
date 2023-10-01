#!/usr/bin/python3
"""the technical interview preparation"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    n = len(list_of_integers)
    if n == 0:
        return None
    left = 0
    right = n - 1
    while left < right:
        mid = int((left + right) / 2)
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]


if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
