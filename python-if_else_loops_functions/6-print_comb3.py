#!/usr/bin/python3
c = 1
for a in range(9):
    for b in range(c,10):
        if a == b:
            continue
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}, ".format(a, b), end="")
    c += 1
