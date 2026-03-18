#!/usr/bin/python3
"""
This module contains a function that prints text with indentation
based on specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to be printed (must be a string).

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    chunk = ""
    for char in text:
        chunk += char
        if char in ['.', '?', ':']:
            print(chunk.strip(' '))
            print("")
            chunk = ""

    if chunk.strip(' '):
        print(chunk.strip(' '), end="")
