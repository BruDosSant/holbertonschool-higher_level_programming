#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    total = 0

    for arg in argv[1:]:
        total += int(arg)

    print(total)
