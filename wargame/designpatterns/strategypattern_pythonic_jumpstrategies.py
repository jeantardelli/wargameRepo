"""strategypattern_pythonic_jumpstrategies

Example to show a Pythonic way of implementing strategy desing pattern.

The example shows how to use Python's first class functions to implement
strategy pattern.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:copyright: The MIT License (MIT). See LICENSE file for further details.
"""
def can_not_jump():
    """A demo function representing a jump algorithm.

    .. note:: No actual agorithm is implemented, it just prints some information.
    """
    print("--> CanNotJump.jump: I can not jump")

def power_jump():
    """A demo function representing a jump algorithm.

    .. note:: No actual algorithm is implemented, it just prints some information.
    """
    print("--> PowerJump.jump: I can jump 100 feet from the ground!")

def horse_jump():
    """A demo function representing a jump algorithm.

    .. note:: No actual algorithm is implemented, it just prints some information.
    """
    print("--> HorseJump.jump: Jumping my horse.")
