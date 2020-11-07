"""strategypattern_traditional_jumpstrategies

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

class JumpStrategy:
    """Base Class representing a jump strategy (an algorithm)."""
    def jump(self):
        """The actual jump algorithm.

        .. seealso:: AbstractGameUnit.jump() where this is called
                     (if this jump strategy is chosen)
        """
        print("--> JumpStrategy.jump: Default jump")

class CanNotJump(JumpStrategy):
    """Class whose instance represents a jump algorithm."""
    def jump(self):
        """The actual jump algorithm.

        .. seealso: AbstractGameUnit.jump() where this is called
                    (if this jump strategy is chosen)
        """
        print("--> CanNotJump.jump: I can not jump")

class HorseJump(JumpStrategy):
    """Class whose instance represents a jump algorithm"""
    def jump(self):
        """The actual jump algorithm.

        .. seealso: AbstractGameUnit.jump() where this is called
                    (if this jump strategy is chosen)
        """
        print("--> HorseJump.jump: Jumping with my horse.")

class PowerJump(JumpStrategy):
    """Class whose instance represents a jump algoritm."""
    def jump(self):
        """The actual jump algorithm.

        .. seealso: AbstractGameUnit.jump() where this is called
                    (if this jump strategy is chosen)
        """
        print("--> PowerJump.jump: I can jump 100 feet from the ground!")
