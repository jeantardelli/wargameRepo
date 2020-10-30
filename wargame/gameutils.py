"""wargame.gameutils

This module contains some utility function for the game Attack of the Orcs

This modue is compatible with Python 3.5.x and later. It contains supporting
code for the book, Learning Python Application Development Packt Publishing.

This is my version of the code, it is pretty much similar to the original
author version.

:copyright: 2020, Jean Tardelli
:license: The MIT License (MIT). See LICENSE file for further details.
"""

import random

def weighted_random_selection(obj1, obj2):
    """Randomly return one of the following, obj1 or obj2

    :arg obj1: An instance of class AbstractGameUnit. It can be any object.
               The calling code should ensure the correct object is passed
               to this function.
    :arg obj2: Another instance of class AbstractGameUnit

    :return: obj1 or obj2

    .. seealso:: :py:func:`weighted_random_selection_alternate` which is an
                  alternative implementation that is used to demonstrate
                  the importance of unit testing.
    """
    selection = random.choices([id(obj1), id(obj2)], weights=[0.3, 0.7])
    if selection[0] == id(obj1):
        return obj1
    return obj2

def print_bold(msg, end='\n'):
    """Convinience function to print a message in bold style

    Optionally you can also specify how the bold text should end. By default it
    ends with a new line character.

    :arg msg: Message to be converted to bold style
    :arg end: Tell how the printed string should end (newline, space etc)
    """
    print("\033[1m" + msg + "\033[0m", end=end)
