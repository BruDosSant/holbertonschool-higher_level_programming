#!/usr/bin/python3
i = 97
print("".join("{}".format(chr(i)) for i in range(97, 123) if chr(i) not in ['q', 'e']), end="")
