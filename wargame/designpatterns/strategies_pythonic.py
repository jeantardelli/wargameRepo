"""strategies_pythonic

Example to show one way of implementing different design pattern strategies
in Python. The example shows how to use Python's first class functions to implement
strategy pattern, a simple refactory.

This module is compatible with Python 3.6.x

RUNNING THE PROGRAM:
Assuming you have python in your environment variable PATH, type the following
in the command prompt to run the program:

        python name_of_the_file.py

(Replace name_of_the_file.py with the name of this file)

.. seealso: For a somewhat 'traditional' approach, see the file
            strategies_traditional.py.

.. note:: The AbstractGameUnit is created as an abstract base class just to bring
          'some order' in subclasses. For example it enforces the
          subclasses to implement info method. If you don't want to enforce such
          rule, you can optionally make this class a simple base class
          (not the abstract class)

:copyright: 2020, Jean Tardelli

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
import sys
from strategypattern_pythonic_jumpstrategies import can_not_jump, power_jump
from pythonic_dwarffighter import DwarfFighter
from pythonic_unitfactory_kingdom import Kingdom

if sys.version_info < (3,0):
    print("This code requires Python 3.x. It is tested with 3.6")
    print("Looks like you are trying to run this using "
          "Python version: {0}.{1}".format(sys.version_info[0], sys.version_info[1]))
    sys.exit(1)

if __name__ == '__main__':
    # Strategy Pattern
    print("Strategy Design Pattern")
    print("="*23)
    # Pass the jump strategy (function) while instantiating the class.
    dwarf = DwarfFighter("Dwarf", can_not_jump)
    print("\n{STRATEGY-I} Dwarf trying to jump:")
    dwarf.jump()
    print("-"*56)

    # Optionally change the jump strategy later
    print("\n{STRATEGY-II} Dwarf given a 'magic potion' to jump:")
    dwarf.jump = power_jump
    dwarf.jump()
    print("-"*56)

    # Factory Strategy
    print("\nSimple Factoring")
    print("="*16)
    k = Kingdom()
    elf_unit = k.recruit("ElfRider")
    print("Created an instance of: {0}".format(elf_unit.__class__.__name__))
