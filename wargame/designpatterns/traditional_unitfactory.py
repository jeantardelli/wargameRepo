"""traditional_unitfactory

Example to show one way of refactoring files in Python.

The example shown here resembles a 'traditional' implementation of refactoring 
in Python (traditional = the one you may implement in languages like
C++). For a more Pythonic approach, see the file strategies_pythonic.py.

This module is compatible with Python 3.6.x.

:copyright: 2020, Jean Tardelli

:license: The MIT license (MIT). See LICENSE file for further details.
"""
from traditional_dwarffighter import DwarfFighter
from traditional_elflord import ElfLord
from traditional_elfrider import ElfRider
from traditional_knight import Knight
from traditional_fairy import Fairy
from traditional_orcrider import OrcRider
from traditional_orcfighter import OrcFighter
from traditional_wizard import Wizard

class UnitFactory:
    """A simple factory to create and return instances of game units.

    .. seealso:: `Kingdom` class and various classes like `ElfRider`, `Knight`, etc.
    """
    def __init__(self):
        self.unit_type = None

    def create_unit(self, unit_type):
        """The work horse method to create and return instances of a game unit.

        :arg string unit_type: The ype of unit requestaed by the client.
        :return: An instance of a game unit such as ElfRider, Knight, Dwarf, etc.
        """
        unit = None
        unit_type = unit_type.lower()

        if unit_type == 'elfrider':
            unit = ElfRider()
        elif unit_type == 'knight':
            unit = Knight()
        elif unit_type == 'dwarffighter':
            unit = DwarfFighter()
        elif unit_type == 'orcrider':
            unit = OrcRider()
        elif unit_type == 'orcfighter':
            unit = OrcFighter()
        elif unit_type == 'wizard':
            unit = Wizard()
        elif unit_type == 'elflord':
            unit = ElfLord()
        elif unit_type == 'fairy':
            unit = Fairy()

        return unit
