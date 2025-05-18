#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    messi = my_list [:]
    if idx < 0:
        return messi
    if idx >= len(messi):
        return messi
    else:
        messi [idx] = element
        return messi
