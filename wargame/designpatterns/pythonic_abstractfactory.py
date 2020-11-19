"""abstractfactory_pythonic

Example to show a Pythonic way of implementing an abstract factory pattern.

The example shows how to use Python's language feature (classes are first-class
objects) to implement an abstract factory. It also shows how to use a factory
WITHOUTH instatiating it (using class method and class variables)

This module was tested using Python 3.8

RUNNING THE PROGRAM
-------------------

Assuming you have python in your enviroment variable PATH, type the following
in the command prompt to run the program:

    python name_of_the_file.py

(Replace name_of_the_file.py with the name of this file.)

.. seealso:: The file pythonic_simplefactory.py which will help understanding
            the concept of a simple factory. You can also look at the alternate
            solution.

.. note:: The classes such as IronJacket, GoldLocket etc are just dummy classes
          to represent concrete factory products.

:copyright: 2020, Jean Tardelli

:license: The MIT License (MIT). See LICENSE file for further details.
"""
from pythonic_abstractfactory_kingdom import Kingdom
from pythonic_abstractfactory_dwarfkingdom import DwarfKingdom

if __name__ == '__main__':
    print("Buying accessories in default Kingdom...")
    kingdom = Kingdom()
    kingdom.buy_accessories("ironjacket", "goldenlocket")
    print("-"*56)
    print("Buying accessories in DwarfKingdom...")
    dwarf_kingdom = DwarfKingdom()
    dwarf_kingdom.buy_accessories("ironjacket", "goldenlocket")
