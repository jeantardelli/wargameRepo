"""strategypattern_pythonic_abstractgameunit

Example to show a Pythonic way of implementing strategy desing pattern.

The example shows how to use Python's first class functions to implement
strategy pattern.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:copyright: The MIT License (MIT). See LICENSE file for further details.
"""
from abc import ABC, abstractmethod
from collections.abc import Callable

class AbstractGameUnit(ABC):
    """Base class for all the game characters.

    :arg string name: Name of the game character.
    :arg jump_strategy: A callable (function) that represents an algorithm to jump.
    :ivar jump: The jump_strategy function is assigned to this variable.

    .. note: This is created as an abstract class and requires subclasses to
             override the 'info' method. However, you can change this to a simple
             class (not abstract) if you don't want to enforce any interface of the
             subclasses.
    .. seealso: DwarfFighter (a subclass)
    """
    def __init__(self, name, jump_strategy):
        """Initializes the AbstractGameUnit object."""
        assert(isinstance(jump_strategy, Callable))
        self.name = name
        self.jump = jump_strategy

    @abstractmethod
    def info(self):
        """Prints information about this game unit."""
