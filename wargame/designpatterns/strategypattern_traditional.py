"""strategypattern_traditional

Example to show one way of implementing strategy design pattern in Python.

The example shown here resembles a 'traditional' implementation of trategy
pattern in Python (traditional = the one you may implement in languages like
C++). For a more Pythonic approach, see the file strategy_pythonic.py.

This module is compatible with Python 3.6.x.

RUNNING THE PROGRAM:
Assuming you have python in your environment variable PATH, type the following
in the command prompt to run the program:

        $ python name_of_the_file.py

(Replace name_of_the_file.py with the name of this file)

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from strategypattern_traditional_jumpstrategies import CanNotJump, PowerJump
from strategypattern_traditional_dwarffighter import DwarfFighter

if __name__ == '__main__':
    jump_strategy = CanNotJump()
    dwarf = DwarfFighter("Dwarf", jump_strategy)
    print("\n{STRATEGY-I} Dwarf trying to jump:")
    dwarf.jump()
    print("-"*56)

    # Optionally change the jump strategy later
    print("\n{STRATEGY-II} Dwarf given a 'magic potion' to jump:")
    dwarf.set_jump_strategy(PowerJump())
    dwarf.jump()
    print("-"*56)
