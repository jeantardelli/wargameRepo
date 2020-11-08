"""strategies_traditional

Example to show one way of implementing different design pattern strategies
in Python.

The example shown here resembles a 'traditional' implementation in  Python
(traditional = the one you may implement in languages like
C++). For a more Pythonic approach, see the file strategies_pythonic.py.

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
from traditional_dwarffighter import DwarfFighter
from traditional_unitfactory import UnitFactory
from traditional_unitfactory_kingdom import Kingdom

if __name__ == '__main__':
    # Strategy Example
    print("Strategy Pattern")
    print("="*17)
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

    # Factory example
    print("\nFactory Example")
    print("="*17)
    factory = UnitFactory()
    k = Kingdom(factory)
    elf_unit = k.recruit("ElfRider")
    print("Created an instance of: {0}".format(elf_unit.__class__.__name__))
