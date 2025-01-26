#!/usr/bin/python3
"""
Module: 3-say_my_name

Write a function that prints a text with 2 new lines 
after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:
        print(text[i], end="")

        if text[i] in {'.', '?', ':'}:
            print("\n", end="")
            # Skip any spaces after the punctuation
            while i + 1 < length and text[i + 1] == ' ':
                i += 1

        i += 1
