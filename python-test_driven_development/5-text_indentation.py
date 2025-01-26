#!/usr/bin/python3
"""Este es un módulo que contiene una función para sumar d"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print_char = text[i]

        if print_char in ['.', '?', ':']:
            print(print_char)
            print()
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            print(print_char, end="")

        i += 1
