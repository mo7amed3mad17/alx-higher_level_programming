#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for i in my_list:
        if idx > (len(my_list) - 1):
            return None
        if idx == i - 1:
            return i
