#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len (my_list):
        return None
    else:
        for iLO in range (my_list):
            if iLO == idx:
                return my_list(iLO)