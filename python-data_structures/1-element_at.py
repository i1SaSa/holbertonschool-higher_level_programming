#!/usr/bin/python3
def element_at(my_list, idx):
    lentgh = len(my_list)
    if idx > lentgh:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]
