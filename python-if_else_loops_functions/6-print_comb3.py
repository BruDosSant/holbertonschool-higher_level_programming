a b 
for a in range(10):
    for b in range(10):
        if a == b:
            continue
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}, ".format(a, b), end="")
