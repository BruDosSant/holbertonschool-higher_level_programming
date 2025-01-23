#!/usr/bin/python3
def no_c(my_string):
    temp = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            temp += char
    return temp
