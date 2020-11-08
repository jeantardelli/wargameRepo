"""pythonic_abstractgameunit

This is the super class contaning the properties of the different GameUnits
that are used in the desing patterns examples.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from abc import ABC, abstractmethod

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
    def __init__(self, name='strange', jump_strategy=None):
        """Initializes the AbstractGameUnit object."""
        self.name = name
        self.jump = jump_strategy

    @abstractmethod
    def info(self):
        """Prints information about this game unit."""
