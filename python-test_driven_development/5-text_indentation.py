#!/usr/bin/python3
"""
Module that defines the function `text_indentation`.

This function prints text with two new lines after each '.', '?' or ':' 
character.
"""

def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?' or ':' character.

    Args:
        text (str): The input string to process.

    Raises:
        TypeError: If `text` is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i+1].strip(), end="\n\n")
            start = i + 1

    if start < len(text):
        print(text[start:].strip(), end="")
