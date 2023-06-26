#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for a in range(list_length):
        try:
            res.append(my_list_1[a]/my_list_2[a])
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        except IndexError:
            print("out of range")
            res.append(0)
        except TypeError:
            res.append(0)
            print("wrong type")
        finally:
            {}
    return res
