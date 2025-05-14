#!/usr/bin/python3
for num in range((0), (100)):
    if num >= 0 and num <= 9:
        print("0{}, ".format(num), end="")
    if num == 99:
        print("{}".format(num))
    else:
        print("{}, ".format(num), end="")
