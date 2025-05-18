#!/usr/bin/python3
def text_indentation(text):
    """
    Function that prints 2 new lines after ".?:" characters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i+1].strip(), end="\n\n")
            start = i + 1

    # Imprimir lo que queda, si hay algo después del último ".?:"
    if start < len(text):
        print(text[start:].strip(), end="")
