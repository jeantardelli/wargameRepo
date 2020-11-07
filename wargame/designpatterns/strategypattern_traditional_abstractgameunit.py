"""strategypattern_traditional_abstractgameunit

Example to show one way of implementing strategy design pattern in Python.

The example shown here resembles a 'traditional' implementation of trategy
pattern in Python (traditional = the one you may implement in languages like
C++). For a more Pythonic approach, see the file strategy_pythonic.py.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from abc import ABC, abstractmethod
from strategypattern_traditional_jumpstrategies import JumpStrategy

class AbstractGameUnit(ABC):
    """Base class for all the game characters.

    :arg string name: Name of the game character
    :arg JumpStrategy jump_object: Could be an instance of JumpStrategy or
                                   its subclasses. Default to None.
    :ivar jump_strategy: Choose the algorithm for jumping.
    """
    def __init__(self, name, jump_object=None):
        """Initializes the AbstractGameUnit object."""
        self.jump_strategy = None
        self.name = name
        self.set_jump_strategy(jump_object)

    def set_jump_strategy(self, jump_object=None):
        """Set up the object that defines the jump strategy.

        Choose an algorithm that defines the jump behaviour. The algorithm is
        represented by a 'strategy object'.

        :arg JumpStrategy jump_object: Instance of the class that should handle
                    how this game unit 'jumps'. Could be an instance of
                    JumpStrategy or its subclasses. Defaults to None.
        """
        if isinstance(jump_object, JumpStrategy):
            self.jump_strategy = jump_object
        else:
            self.jump_strategy = JumpStrategy()

    def jump(self):
        """Perform the jump operation (delegated)"""
        try:
            self.jump_strategy.jump()
        except AttributeError as err:
            print("Error: AbstractGameUnit.jump: self.jump_strategy: {0}"
                  "\nError details: {1}".format(self.jump_strategy, err.args))

    @abstractmethod
    def info(self):
        """Print information aboute this game unit."""
